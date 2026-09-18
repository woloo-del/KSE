"""Generate an inline concept from explicit public snapshots, without network access."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build(output: Path) -> None:
    def read(name):
        return json.loads((ROOT / 'data/reference' / name).read_text(encoding='utf-8'))
    profiles = read('pse_scale_benchmark_2026-07-31_v1.json')['profiles']
    index = read('pse_investment_heading_index_2026-09-18_v1.json')
    contexts = read('pse_mention_context_2026-09-18_v1.json')['records']
    direct = {(r['profile_id'], r['heading_id']): any(m['context_kind'] == 'EXPLICIT_STATION_LABEL' for m in r['mentions']) for r in contexts}
    links = {p['profile_id']: p['heading_ids'] for p in index['profiles']}
    data = {'profiles': [{'name': p['name_reported'], 'voltage': p['voltage_kV'],
                         'count': len(p['record_ids']), 'statuses': p['status_counts'],
                         'reviewCount': len(p['review_record_ids']),
                         'links': [{'id': h, 'direct': direct[(p['profile_id'], h)]} for h in links[p['profile_id']]]} for p in profiles],
            'headings': {h['heading_id']: {'title': h['title_reported'], 'status': h['status_reported'], 'positions': h['h4_positions']} for h in index['headings']}}
    template = (ROOT / 'docs/prototypes/evidence-workspace.template.html').read_text(encoding='utf-8')
    assert template.count('__KSE_DATA__') == 1
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.replace('__KSE_DATA__', payload), encoding='utf-8', newline='\n')
    print(f'{len(profiles)} profiles; {output.stat().st_size} bytes')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    build(parser.parse_args().output)
