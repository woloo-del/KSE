"""Reproduce private point-in-plan checks without promoting station identity."""
import hashlib
import json
from pathlib import Path
import sys

from shapely.geometry import Point

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.planning_app import read_plan_extent


def main() -> None:
    directory = ROOT / 'data/private/reviews/wegrowo_land_2026-10-06'
    input_bytes = (directory / 'land_diagnostic_two_counties.json').read_bytes()
    diagnostic = json.loads(input_bytes)
    if diagnostic['access'] != 'PRIVATE' or diagnostic['crs'] != 'EPSG:2180':
        raise ValueError('UNEXPECTED_INPUT_SCOPE')
    point = Point(diagnostic['center']['x'], diagnostic['center']['y'])
    sources = json.loads((ROOT / 'data/catalog/probe_results_wegrowo_plan_followup_2026-10-06.json').read_text(encoding='utf8'))
    results = []
    for source_id in ('GRUDZIADZ_PLAN97_GML', 'GRUDZIADZ_PLAN79_GML'):
        matches = [s for s in sources if s['source_id'] == source_id]
        if len(matches) != 1:
            raise ValueError('SOURCE_NOT_UNIQUE')
        source = matches[0]
        raw = (ROOT / source['local_path']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != source['sha256']:
            raise ValueError('SOURCE_HASH_MISMATCH')
        metadata, geometry = read_plan_extent(raw)
        results.append({**metadata, 'source': source, 'covers_candidate_point': geometry.covers(point),
                        'classification': 'CALCULATED'})
    output = {'access': 'PRIVATE', 'station_identity_status': diagnostic['station_identity_status'],
              'input_sha256': hashlib.sha256(input_bytes).hexdigest(), 'plans': results,
              'conclusion': 'Plan coverage is not confirmation of the 14E zone or current station boundary.'}
    text = json.dumps(output, ensure_ascii=False, indent=2) + '\n'
    path = directory / 'plan_extent_checks_v1.json'
    if path.exists() and path.read_text(encoding='utf8') != text:
        raise ValueError('REFUSE_OVERWRITE_DIFFERENT_RESULT')
    path.write_text(text, encoding='utf8')
    print('Checked two preserved plans; station identity not promoted.')


if __name__ == '__main__':
    main()
