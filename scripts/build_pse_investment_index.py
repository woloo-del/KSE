"""Rebuild public documentary leads for all 50 PSE benchmark profiles offline."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.pse.investment_index import parse_headings, profile_mentions


def build() -> dict:
    meta = json.loads((ROOT / 'data/catalog/probe_results_radkowice_stages_2026-09-18.json').read_text(encoding='utf-8'))[0]
    raw = (ROOT / meta['local_path']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != meta['sha256']:
        raise ValueError('SNAPSHOT_CHANGED')
    profile_path = ROOT / 'data/reference/pse_scale_benchmark_2026-07-31_v1.json'
    profile_bytes = profile_path.read_bytes()
    headings = parse_headings(raw.decode('utf-8'))
    links = profile_mentions(json.loads(profile_bytes)['profiles'], headings)
    used = {h for link in links for h in link['heading_ids']}
    return {
        'method': 'pse_investment_heading_index_v1',
        'source': {k: meta[k] for k in ('source_id', 'url', 'local_path', 'sha256', 'retrieval_date')},
        'source_quality': 'B', 'source_date': None,
        'profiles_sha256': hashlib.sha256(profile_bytes).hexdigest(),
        'code_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in
                        ['connectors/pse/investment_index.py', 'connectors/pse/investment_dates.py']},
        'metrics': {'nonempty_heading_occurrences': sum(len(h['h4_positions']) for h in headings),
                    'distinct_heading_texts': len(headings), 'profiles': len(links),
                    'profiles_with_mentions': sum(bool(l['heading_ids']) for l in links),
                    'referenced_heading_texts': len(used), 'confirmed_station_identities': 0},
        'headings': [h for h in headings if h['heading_id'] in used],
        'profiles': links,
        'limitations': ['Name mention may concern a line, wind farm or another station.',
                       'No alias resolution, voltage assignment or canonical station merge.',
                       'Heading status describes the task, not station commissioning.',
                       'Duplicate text is stored once with all locators; not independent evidence.',
                       'Undated historical snapshot, not live confirmation of project progress.'],
    }


if __name__ == '__main__':
    result = build()
    output = ROOT / 'data/reference/pse_investment_heading_index_2026-09-18_v1.json'
    content = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if output.exists() and output.read_text(encoding='utf-8') != content:
        raise ValueError('EXISTING_VERSION_DIFFERS')
    if not output.exists():
        output.write_text(content, encoding='utf-8', newline='\n')
    print(json.dumps(result['metrics']))
