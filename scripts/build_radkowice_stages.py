"""Rebuild stage observations from an immutable public snapshot."""
import hashlib
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.pse.investment_stages import parse_stages


def build() -> dict:
    meta = json.loads((ROOT/'data/catalog/probe_results_radkowice_stages_2026-09-18.json').read_text(encoding='utf-8'))[0]
    raw = (ROOT/meta['local_path']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != meta['sha256']:
        raise ValueError('SNAPSHOT_CHANGED')
    records = parse_stages(raw.decode('utf-8'))
    for r in records:
        r.update(source_id=meta['source_id'], source_url=meta['url'],
                 retrieval_date=meta['retrieval_date'], snapshot_sha256=meta['sha256'],
                 locator='h4: '+r['title_reported'], source_quality='B')
    return {'method': 'radkowice_portal_stages_v1', 'records': records,
            'method_code_sha256': hashlib.sha256((ROOT/'connectors/pse/investment_stages.py').read_bytes()).hexdigest(),
            'limitations': ['Undated website status, not independent confirmation of work progress.',
                           'No mapping to PRSP II.47, bus bridge or transformer identity established.']}


if __name__ == '__main__':
    output = ROOT/'data/reference/radkowice_portal_stages_2026-09-18_v1.json'
    content = json.dumps(build(), ensure_ascii=False, indent=2)+'\n'
    if output.exists():
        if output.read_text(encoding='utf-8') != content:
            raise ValueError('EXISTING_VERSION_DIFFERS')
    else:
        output.write_text(content, encoding='utf-8', newline='\n')
    print(output)
