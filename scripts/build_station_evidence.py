"""Build immutable aggregation from four allowlisted public snapshots, offline."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from grid_engine.station_evidence import aggregate, encode

INPUTS = {
    'pipeline': 'data/reference/radkowice_pipeline_view_2026-07-31_v1.json',
    'plan': 'data/reference/radkowice_development_plan_2026-04_v1.json',
    'osm': 'data/reference/osm_radkowice_station_audit_2026-09-17_v2.json',
    'review': 'data/reference/radkowice_investment_dates_2026-09-17_v1.json',
}


def build() -> dict:
    raw = {key: (ROOT / name).read_bytes() for key, name in INPUTS.items()}
    result = aggregate(**{key: json.loads(value) for key, value in raw.items()})
    result['input_sha256'] = {INPUTS[key]: hashlib.sha256(value).hexdigest() for key, value in raw.items()}
    result['method_code_sha256'] = hashlib.sha256((ROOT / 'grid_engine/station_evidence.py').read_bytes()).hexdigest()
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    payload = encode(build())
    if args.output.exists():
        if args.output.read_bytes() != payload:
            raise ValueError('OUTPUT_EXISTS_WITH_DIFFERENT_CONTENT: choose a new version')
    else:
        with args.output.open('xb') as stream:
            stream.write(payload)
    print('Evidence aggregation ready:', len(json.loads(payload)['records']), 'source records')
