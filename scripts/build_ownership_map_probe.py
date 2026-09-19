"""Reproduce the ownership completeness observation from checksummed raw HTML."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.ownership_map import inspect_county


def main() -> None:
    manifest = json.loads((ROOT / 'data/catalog/probe_results_ownership_map_2026-09-19.json').read_text(encoding='utf-8'))
    source = next(row for row in manifest if row['source_id'] == 'GUGIK_OWNERSHIP_MAP_COUNTY_HTML')
    raw = (ROOT / source['local_path']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != source['sha256']:
        raise ValueError('SOURCE_HASH_MISMATCH')
    result = {'method_version': 'ownership_map_completeness_v1', 'source': source, 'observation': inspect_county(raw)}
    (ROOT / 'data/reference/ownership_map_probe_2026-09-19.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
