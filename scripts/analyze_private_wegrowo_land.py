"""Local spatial diagnostic using the user's unverified historical GIS point.

Writes private outputs only; does not publish a station location or a legal split.
"""
import hashlib
import json
from pathlib import Path
import sys

from shapely.geometry import Point

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.geopackage import read_features
from connectors.gis.county_package import select_parcels
from gis.coordinates import PolishMetricProjection
from gis.ownership_area import BUFFER_QUAD_SEGS, summarize_buffer


def main() -> None:
    private_path = ROOT / 'data/private/GPZ gpkg/Stacje NN_WN.gpkg'
    features, errors = read_features(private_path)
    if errors:
        raise ValueError('PRIVATE_GIS_DECODE_ERRORS')
    matches = [f for f in features if f.fid == 95 and f.properties.get('Name') == 'Grudziądz (Węgrowo) 400/220/110kV']
    if len(matches) != 1 or matches[0].srs_id != 4326 or matches[0].geometry.geom_type != 'Point':
        raise ValueError('EXPECTED_HISTORICAL_CANDIDATE_NOT_FOUND')
    original = matches[0].geometry
    projection = PolishMetricProjection()
    center = projection.project(Point(original.x, original.y))
    source_rows = json.loads((ROOT / 'data/catalog/probe_results_county_export_2026-10-06.json').read_text(encoding='utf8'))
    source = next(r for r in source_rows if r['source_id'] == 'COUNTY_EXPORT_GRUDZIADZ_GPKG')
    archived_bytes = (ROOT / source['local_path']).read_bytes()
    if hashlib.sha256(archived_bytes).hexdigest() != source['sha256']:
        raise ValueError('PACKAGE_SOURCE_HASH_MISMATCH')
    package_path = ROOT / 'data/staging/research/grudziadz_parcels_2026-10-06.gpkg'
    audit_metadata = json.loads((ROOT / 'data/reference/county_export_audit_2026-10-06.json').read_text(encoding='utf8'))
    if hashlib.sha256(package_path.read_bytes()).hexdigest() != audit_metadata['package_sha256']:
        raise ValueError('UNPACKED_PACKAGE_HASH_MISMATCH')
    parcels, audit = select_parcels(package_path, buffer=center.buffer(1000, quad_segs=BUFFER_QUAD_SEGS), source_id=source['source_id'])
    sources = {source['source_id']: {'locator': source['url'], 'sha256': source['sha256'], 'retrieval_date': source['retrieval_date']},
               'USER_GIS_CANDIDATE': {'locator': 'private:Stacje NN_WN.gpkg#fid=95',
                                      'sha256': hashlib.sha256(private_path.read_bytes()).hexdigest(),
                                      'retrieval_date': '2026-10-06', 'source_state': 'user-reported 2024',
                                      'identity_status': 'HISTORICAL_CANDIDATE_UNVERIFIED'}}
    result = summarize_buffer(center=center, center_source_id='USER_GIS_CANDIDATE', parcels=parcels,
                              sources=sources, crs='EPSG:2180')
    result.update(access='PRIVATE', station_identity_status='HISTORICAL_CANDIDATE_UNVERIFIED',
                  station_geometry_method='Explicit x/y projection; source point Z not used for planar buffer.',
                  package_audit=audit, transformation=projection.metadata(),
                  status='PARTIAL_SPATIAL_DIAGNOSTIC_NOT_COMPLETE_STATION_REPORT')
    output = ROOT / 'data/private/reviews/wegrowo_land_2026-10-06'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'land_diagnostic.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('Selected parcels:', len(parcels), 'geometry coverage (%):', result['geometric_coverage']['percent_of_buffer'])


if __name__ == '__main__':
    main()
