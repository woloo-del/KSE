"""Embed public snapshots in a self-contained UI concept; no network requests."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from shapely.geometry import LineString, Point, Polygon, box, mapping
from shapely.geometry.polygon import orient

ROOT = Path(__file__).resolve().parents[1]


def build() -> str:
    source = ROOT / 'data/raw/research/2026-09-17/osm_radkowice_station_area.xml'
    probes = json.loads((ROOT / 'data/catalog/probe_results_osm_radkowice_2026-09-17.json').read_text(encoding='utf8'))
    expected = next(p['sha256'] for p in probes if p['source_id'] == 'OSM_RADK_STATION_AREA')
    raw = source.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Source snapshot changed')
    tree = ET.fromstring(raw)
    nodes = {n.get('id'): (float(n.get('lon')), float(n.get('lat'))) for n in tree.findall('node')}
    station = next(w for w in tree.findall('way') if w.get('id') == '199098055')
    station_coords = [nodes[n.get('ref')] for n in station.findall('nd')]
    polygon = Polygon(station_coords)
    xmin, ymin, xmax, ymax = polygon.bounds
    extent = box(xmin-.0007, ymin-.0007, xmax+.0007, ymax+.0007)
    features = []
    for way in tree.findall('way'):
        tags = {t.get('k'): t.get('v') for t in way.findall('tag')}
        is_station = way.get('id') == '199098055'
        kind = 'station' if is_station else 'power' if tags.get('power') in {'line', 'minor_line', 'cable'} else 'building' if 'building' in tags else 'road' if 'highway' in tags else None
        if kind is None:
            continue
        coords = [nodes[n.get('ref')] for n in way.findall('nd')]
        if len(coords) < 2:
            continue
        shape = Polygon(coords) if kind in {'station', 'building'} and len(coords) >= 4 and coords[0] == coords[-1] else LineString(coords)
        if not shape.is_valid:
            continue
        shape = shape.intersection(extent)
        if shape.is_empty:
            continue
        if shape.geom_type == 'Polygon':
            shape = orient(shape, sign=-1)
        features.append({'type': 'Feature', 'properties': {'kind': kind, 'voltage': tags.get('voltage', ''), 'osm_id': way.get('id')}, 'geometry': mapping(shape)})
    features.sort(key=lambda f: ['station', 'building', 'road', 'power'].index(f['properties']['kind']))
    transformers = []
    for node in tree.findall('node'):
        tags = {t.get('k'): t.get('v') for t in node.findall('tag')}
        if tags.get('power') == 'transformer' and polygon.covers(Point(nodes[node.get('id')])):
            voltage = '220/110 kV' if tags.get('voltage:primary') == '220000' and tags.get('voltage:secondary') == '110000' else None
            transformers.append({'id': node.get('id'), 'coordinates': nodes[node.get('id')], 'label': 'Transformator — tagi OSM' + (' 220/110 kV' if voltage else ''), 'voltage': voltage})
    pipeline_path = ROOT / 'data/reference/radkowice_pipeline_view_2026-07-31_v1.json'
    pipeline = json.loads(pipeline_path.read_text(encoding='utf8'))
    data = {'features': {'type': 'FeatureCollection', 'features': features}, 'boundary': {'type': 'MultiPoint', 'coordinates': list(extent.exterior.coords)}, 'transformers': transformers, 'projects': pipeline['records'], 'source_hashes': {'osm': expected, 'pipeline': hashlib.sha256(pipeline_path.read_bytes()).hexdigest()}, 'method': 'platform_concept_v1', 'classification': 'UI_PROTOTYPE_WITH_PUBLIC_SNAPSHOT_DATA'}
    path = ROOT / 'docs/prototypes/platform-concept.html'
    fragment = path.read_text(encoding='utf8')
    embedded = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    block = '<!-- DATA_START -->\n<script type="application/json" id="kse-concept-data">' + embedded + '</script>\n<!-- DATA_END -->'
    result, count = re.subn(r'<!-- DATA_START -->.*?<!-- DATA_END -->', lambda _: block, fragment, flags=re.S)
    if count != 1 or len(result.encode()) >= 1_000_000:
        raise ValueError('Invalid fragment')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--copy-to', type=Path)
    args = parser.parse_args()
    result = build()
    (ROOT / 'docs/prototypes/platform-concept.html').write_bytes(result.encode())
    if args.copy_to:
        args.copy_to.write_bytes(result.encode())
    print('Public snapshot concept built; no private inputs.')
