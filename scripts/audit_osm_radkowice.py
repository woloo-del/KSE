"""Replay a checksummed public OSM station snapshot without additional requests."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.osm_station import audit


def build() -> dict:
    probes = json.loads((ROOT / 'data/catalog/probe_results_osm_radkowice_2026-09-17.json').read_text(encoding='utf8'))
    meta = next(p for p in probes if p['source_id'] == 'OSM_RADK_STATION_AREA')
    data = (ROOT / meta['local_path']).read_bytes()
    if hashlib.sha256(data).hexdigest() != meta['sha256']:
        raise ValueError('SNAPSHOT_CHANGED')
    result = audit(data, 199098055)
    result['source'] = meta
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = build()
    with args.output.open('x', encoding='utf8', newline='\n') as target:
        target.write(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    print(json.dumps(result['summary']))
