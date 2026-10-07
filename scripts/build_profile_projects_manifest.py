"""Bind locally retained PSE rows to source profiles; never overwrite a version."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.profile_projects import project_details
from connectors.pse.project_pipeline import parse


def run() -> None:
    profile_path = ROOT / 'data/reference/pse_scale_benchmark_2026-07-31_v1.json'
    profiles = json.loads(profile_path.read_bytes())
    source = ROOT / profiles['provenance']['local_path']
    if hashlib.sha256(source.read_bytes()).hexdigest() != profiles['provenance']['sha256']:
        raise ValueError('SOURCE_SNAPSHOT_CHANGED')
    path = ROOT / 'data/processed/pse_bulk_pipeline_2026-07-31_v1.json'
    raw = path.read_bytes()
    imported = json.loads(raw)
    reproduced = parse(source)
    reproduced['provenance'] = profiles['provenance']
    if reproduced != imported:
        raise ValueError('PROJECT_IMPORT_NOT_REPRODUCIBLE')
    details = project_details(imported, profiles)
    manifest = {'method': 'profile_projects_v1',
                'profiles_sha256': hashlib.sha256(profile_path.read_bytes()).hexdigest(),
                'projects_sha256': hashlib.sha256(raw).hexdigest(),
                'source_date': imported['source_date'],
                'record_count': sum(len(rows) for rows in details.values()),
                'parser_sha256': hashlib.sha256((ROOT / 'connectors/pse/project_pipeline.py').read_bytes()).hexdigest()}
    target = ROOT / 'data/reference/pse_profile_projects_manifest_2026-07-31_v1.json'
    content = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    if target.exists() and target.read_text(encoding='utf-8') != content:
        raise ValueError('EXISTING_VERSION_DIFFERS')
    if not target.exists():
        target.write_text(content, encoding='utf-8', newline='\n')
    print(json.dumps(manifest))


if __name__ == '__main__':
    run()
