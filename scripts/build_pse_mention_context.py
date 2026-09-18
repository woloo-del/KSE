"""Classify the context of archived name mentions without changing the source index."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.pse.mention_context import annotate


def build() -> dict:
    path = ROOT / 'data/reference/pse_investment_heading_index_2026-09-18_v1.json'
    raw = path.read_bytes()
    rows = annotate(json.loads(raw))
    station_rows = [r for r in rows if any(m['context_kind'] == 'EXPLICIT_STATION_LABEL' for m in r['mentions'])]
    return {'method': 'pse_mention_context_v1',
            'input_path': path.relative_to(ROOT).as_posix(),
            'input_sha256': hashlib.sha256(raw).hexdigest(),
            'code_sha256': hashlib.sha256((ROOT / 'connectors/pse/mention_context.py').read_bytes()).hexdigest(),
            'metrics': {'profile_heading_pairs': len(rows),
                        'mention_counts': dict(sorted(Counter(m['context_kind'] for r in rows for m in r['mentions']).items())),
                        'profiles_with_explicit_station_label': len({r['profile_id'] for r in station_rows}),
                        'confirmed_identities': 0},
            'records': rows,
            'limitations': ['Text context is not identity verification.',
                           'Listed voltage belongs to the task wording, not necessarily current infrastructure.',
                           'No transfer of line voltage, stage status or station ownership to profiles.',
                           'Other mentions include line endpoints and unsupported station wording; not a negative match.']}


if __name__ == '__main__':
    result = build()
    output = ROOT / 'data/reference/pse_mention_context_2026-09-18_v1.json'
    content = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if output.exists() and output.read_text(encoding='utf-8') != content:
        raise ValueError('EXISTING_VERSION_DIFFERS')
    if not output.exists():
        output.write_text(content, encoding='utf-8', newline='\n')
    print(json.dumps(result['metrics']))
