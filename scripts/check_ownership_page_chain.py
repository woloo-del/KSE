"""Replay the small archived GUGiK paging experiment without making requests."""
import hashlib
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.ownership_paging import inspect_pages


def main() -> None:
    rows = json.loads((ROOT / 'data/catalog/probe_results_ownership_paging_2026-09-19.json').read_text(encoding='utf-8'))
    inputs = []
    for source in rows:
        raw = (ROOT / source['local_path']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != source['sha256']:
            raise ValueError('HASH_MISMATCH')
        inputs.append((raw, source))
    capabilities, caps_source = next(row for row in inputs if row[1]['source_id'].endswith('_CAPS'))
    root = ET.fromstring(capabilities)
    if root.tag != '{http://www.opengis.net/wfs/2.0}WFS_Capabilities':
        raise ValueError('INVALID_CAPABILITIES')
    ns = '{http://www.opengis.net/ows/1.1}'
    constraints = {el.get('name'): el.findtext(ns + 'DefaultValue') for el in root.findall('.//' + ns + 'Constraint')}
    result = inspect_pages([row for row in inputs if '_PAGE_' in row[1]['source_id']],
                           transaction_safe=constraints.get('PagingIsTransactionSafe') == 'TRUE')
    result['capabilities_source'] = caps_source
    result['paging_constraints'] = {key: constraints.get(key) for key in ('ImplementsResultPaging', 'PagingIsTransactionSafe', 'CountDefault')}
    result['scope'] = 'TWO_RECORD_RESEARCH_QUERY_NOT_STATION_BUFFER'
    (ROOT / 'data/reference/ownership_paging_audit_2026-09-19.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(result['status'], result['blocking_reasons'])


if __name__ == '__main__':
    main()
