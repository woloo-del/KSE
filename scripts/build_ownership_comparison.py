"""Reproduce bounded ownership discovery; no station buffer or area claim."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.ownership_map import inspect_county, inspect_parcel
from connectors.gis.ownership_probe import normalize_sample


def main() -> None:
    manifest = json.loads((ROOT / 'data/catalog/probe_results_ownership_comparison_2026-09-19.json').read_text(encoding='utf-8'))
    raw_by_id = {}
    for source in manifest:
        raw = (ROOT / source['local_path']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != source['sha256']:
            raise ValueError('SOURCE_HASH_MISMATCH')
        raw_by_id[source['source_id']] = raw
    counties = [{'source_id': key, **inspect_county(raw)} for key, raw in raw_by_id.items() if key.endswith('_AREA')]
    parcel = inspect_parcel(raw_by_id['GUGIK_OWNERSHIP_GRUDZIADZ_PARCEL'])
    normalized = normalize_sample(raw_by_id['GUGIK_OWNERSHIP_GRUDZIADZ_WFS'])
    matched = [f for f in normalized['features'] if f['id'] == parcel['parcel_id']]
    if len(matched) != 1:
        raise ValueError('PARCEL_NOT_UNIQUELY_MATCHED')
    agreement = matched[0]['properties']['registration_group'] == parcel['registration_group']
    result = {'method_version': 'ownership_comparison_v1', 'scope': 'DISCOVERY_POINTS_NOT_STATIONS_OR_1KM_BUFFERS',
              'sources': manifest, 'counties': counties, 'wms_parcel': parcel,
              'wfs_summary': normalized['probe_summary'], 'exact_id_group_agreement': agreement,
              'independent_confirmation': False,
              'limitations': ['WMS and WFS may share the same county source.', 'WFS DATA empty; WMS retrieval time is not ownership validity.',
                              'Small selected sample, no nationwide or station-buffer completeness.', 'Commercial reuse not cleared.'],
              'ownership_area_percent': None}
    staging = ROOT / 'data/staging/research/ownership_grudziadz_sample_2026-09-19.geojson'
    staging.parent.mkdir(parents=True, exist_ok=True)
    normalized['sources'] = [source for source in manifest if source['source_id'].endswith('_WFS')]
    staging.write_text(json.dumps(normalized, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'data/reference/ownership_comparison_2026-09-19.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
