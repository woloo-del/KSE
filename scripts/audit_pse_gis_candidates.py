"""Offline shortlist against a private historical compilation; no identity promotion."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.geopackage import read_features
from connectors.gis.station_candidates import candidates


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> None:
    source = ROOT / 'data/private/GPZ gpkg/Stacje NN_WN.gpkg'
    profiles = ROOT / 'data/reference/pse_scale_benchmark_2026-07-31_v1.json'
    hashes = {'gis_sha256': digest(source), 'profiles_sha256': digest(profiles),
              'method_sha256': digest(ROOT / 'connectors/gis/station_candidates.py')}
    features, errors = read_features(source)
    if errors:
        raise ValueError('GIS_VALIDATION_ERRORS')
    stations = [{'table': f.table, 'fid': f.fid, 'name': f.properties['Name'],
                 'code_reported': f.properties.get('Code')} for f in features]
    rows = candidates(json.loads(profiles.read_text(encoding='utf-8'))['profiles'], stations)
    if digest(source) != hashes['gis_sha256'] or digest(profiles) != hashes['profiles_sha256']:
        raise ValueError('SOURCE_CHANGED')
    result = {'method': 'pse_gis_candidates_v2', 'access': 'PRIVATE',
              'provenance': hashes, 'source_path': source.relative_to(ROOT).as_posix(),
              'profiles_path': profiles.relative_to(ROOT).as_posix(),
              'gis_source_date': None, 'gis_year_user_reported': 2024,
              'reviewed_at': '2026-09-18',
              'metrics': {'profiles': len(rows), 'gis_records': len(stations),
                          'status_counts': dict(sorted(Counter(r['review_status'] for r in rows).items())),
                          'confirmed_identities': 0, 'matching_error_rate': None,
                          'manual_review_minutes': None}, 'rows': rows}
    output = ROOT / 'data/private/analysis/pse_gis_candidates_2026-09-18_v2.json'
    content = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and output.read_text(encoding='utf-8') != content:
        raise ValueError('EXISTING_VERSION_DIFFERS')
    if not output.exists():
        output.write_text(content, encoding='utf-8', newline='\n')
    print(json.dumps(result['metrics'], ensure_ascii=False))


if __name__ == '__main__':
    run()
