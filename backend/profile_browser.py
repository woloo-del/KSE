"""Read-only profile browser contract, restricted to named public snapshots."""
from pathlib import Path
import hashlib
import json
from backend.profile_projects import project_details

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    'profiles': 'pse_scale_benchmark_2026-07-31_v1.json',
    'index': 'pse_investment_heading_index_2026-09-18_v1.json',
    'contexts': 'pse_mention_context_2026-09-18_v1.json',
    'projects_manifest': 'pse_profile_projects_manifest_2026-07-31_v1.json',
}
PROJECTS_PATH = 'data/processed/pse_bulk_pipeline_2026-07-31_v1.json'


def browser_data(root: Path = ROOT) -> dict:
    raw = {key: (root / 'data/reference' / name).read_bytes() for key, name in FILES.items()}
    hashes = {key: hashlib.sha256(value).hexdigest() for key, value in raw.items()}
    loaded = {key: json.loads(value) for key, value in raw.items()}
    index, context = loaded['index'], loaded['contexts']
    if index['profiles_sha256'] != hashes['profiles'] or context['input_sha256'] != hashes['index']:
        raise ValueError('PROFILE_SNAPSHOT_MISMATCH')
    profiles = loaded['profiles']['profiles']
    manifest = loaded['projects_manifest']
    project_raw = (root / PROJECTS_PATH).read_bytes()
    project_hash = hashlib.sha256(project_raw).hexdigest()
    if (manifest['profiles_sha256'] != hashes['profiles'] or
            manifest['projects_sha256'] != project_hash):
        raise ValueError('PROJECT_SNAPSHOT_MISMATCH')
    imported = json.loads(project_raw)
    details = project_details(imported, loaded['profiles'])
    direct = {(r['profile_id'], r['heading_id']): any(m['context_kind'] == 'EXPLICIT_STATION_LABEL' for m in r['mentions']) for r in context['records']}
    if len(direct) != len(context['records']):
        raise ValueError('DUPLICATE_CONTEXT')
    links = {p['profile_id']: p['heading_ids'] for p in index['profiles']}
    if len(links) != len(index['profiles']) or len({p['profile_id'] for p in profiles}) != len(profiles):
        raise ValueError('DUPLICATE_PROFILE')
    if set(links) != {p['profile_id'] for p in profiles}:
        raise ValueError('PROFILE_SET_MISMATCH')
    expected = {(p, h) for p, ids in links.items() for h in ids}
    if set(direct) != expected:
        raise ValueError('CONTEXT_SET_MISMATCH')
    headings = {h['heading_id']: {'title': h['title_reported'], 'status': h['status_reported'], 'positions': h['h4_positions']} for h in index['headings']}
    if len(headings) != len(index['headings']) or any(h not in headings for _, h in expected):
        raise ValueError('HEADING_SET_MISMATCH')
    return {'profiles': [{'id': p['profile_id'], 'name': p['name_reported'], 'voltage': p['voltage_kV'],
                         'count': len(p['record_ids']), 'statuses': p['status_counts'],
                         'reviewCount': len(p['review_record_ids']),
                         'projects': details[p['profile_id']],
                         'links': [{'id': h, 'direct': direct[(p['profile_id'], h)]} for h in links[p['profile_id']]]} for p in profiles],
            'headings': headings,
            'provenance': {'pipeline_source_date': loaded['profiles']['source_date'],
                           'pipeline_source': loaded['profiles']['provenance'],
                           'investment_source': index['source'],
                           'input_sha256': {**{FILES[k]: v for k, v in hashes.items()}, PROJECTS_PATH: project_hash}},
            'pipeline_footnotes': imported['footnotes'],
            'scope': 'SOURCE_PROFILES_NOT_CANONICAL_STATIONS'}
