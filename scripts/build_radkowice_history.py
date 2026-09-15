"""Replay public PSE status evidence without inventing continuous validity."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path

from grid_engine.observation_history import Observation, validate_history
from grid_engine.shared_connection import Evidence
from scripts.research_radkowice import extract


def build(recorded_at: str) -> dict:
    source = extract()  # Verifies the original XLSX bytes against the catalog hash.
    observations = []
    for row in source['records']:
        observations.append(Observation(
            observation_id=row['research_record_id'] + '_status_v1',
            entity_id=row['research_record_id'], field='application_status_reported',
            scenario='SOURCE_SNAPSHOT', value=row['status_reported'], unit=None,
            classification='REPORTED', recorded_at=recorded_at,
            evidence=Evidence(
                source_id=row['source_id'],
                locator=row['sheet'] + '!' + row['cells']['status_reported'],
                snapshot_sha256=row['snapshot_sha256'],
                retrieval_date=row['retrieval_date'], source_date=row['source_date'],
                access='PUBLIC', origin='DOCUMENT',
            ),
        ))
    validate_history(tuple(observations))
    return {
        'schema_version': 'observation_history_v1',
        'method': 'radkowice_status_history_v1',
        'recorded_at': recorded_at,
        'source_urls': sorted({row['source_url'] for row in source['records']}),
        'limitations': [
            'Source record IDs are not resolved canonical project IDs.',
            'One historical snapshot; no observed lifecycle transitions.',
            'Publication and agreement dates do not establish continuous validity.',
            'Reported agreements do not prove physical connection or current status.',
        ],
        'observations': [asdict(item) for item in observations],
    }


def save(bundle: dict, output: Path) -> None:
    content = (json.dumps(bundle, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    if output.exists():
        if output.read_bytes() != content:
            raise ValueError('HISTORY_SNAPSHOT_EXISTS_USE_NEW_VERSION')
        return
    with output.open('xb') as stream:
        stream.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recorded-at', required=True, help='Actual first registration time, with timezone')
    parser.add_argument('--output', type=Path, default=Path('data/reference/radkowice_observation_history_v1.json'))
    args = parser.parse_args()
    save(build(args.recorded_at), args.output)
    print(args.output)
