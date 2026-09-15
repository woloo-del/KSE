"""Replay one explicit history request; embed its audit manifest in the result."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from grid_engine.historical_assignments import historical_inventory
from grid_engine.historical_connection_parameters import historical_inventory_v2
from grid_engine.observation_history import Observation, validate_history
from grid_engine.shared_connection import Evidence, require_public_result
from grid_engine.strict_json import decode_json

CODE_FILES = (
    'grid_engine/strict_json.py', 'grid_engine/observation_history.py',
    'grid_engine/shared_connection.py', 'grid_engine/historical_assignments.py',
    'scripts/analyze_historical_assignments.py',
)
QUERY_FIELDS = {'connection_id', 'scenario', 'known_at', 'effective_on'}


def decode_request(raw: bytes) -> tuple[tuple[Observation, ...], dict]:
    data = decode_json(raw)
    if not isinstance(data, dict) or set(data) != {'schema_version', 'query', 'observations'}:
        raise ValueError('INVALID_HISTORY_REQUEST_FIELDS')
    if data['schema_version'] not in {'historical_assignments_request_v1', 'historical_connection_request_v2'}:
        raise ValueError('UNSUPPORTED_HISTORY_REQUEST_VERSION')
    query = data['query']
    if (not isinstance(query, dict) or set(query) != QUERY_FIELDS
            or any(not isinstance(v, str) or not v.strip() for v in query.values())):
        raise ValueError('INVALID_HISTORY_QUERY')
    if not isinstance(data['observations'], list):
        raise ValueError('INVALID_OBSERVATION_LIST')
    history = tuple(Observation(**{**item, 'evidence': Evidence(**item['evidence'])})
                    for item in data['observations'])
    validate_history(history)
    return history, query


def analyze_file(input_path: Path, output_path: Path, private_root: Path) -> dict:
    input_path, output_path, private_root = input_path.resolve(), output_path.resolve(), private_root.resolve()
    if any('_secrets' in [p.lower() for p in path.parts] for path in (input_path, output_path)):
        raise ValueError('SECRET_PATH_FORBIDDEN')
    if input_path.suffix.lower() != '.json' or output_path.suffix.lower() != '.json':
        raise ValueError('JSON_PATH_REQUIRED')
    raw = input_path.read_bytes()
    history, query = decode_request(raw)
    version2 = decode_json(raw)['schema_version'] == 'historical_connection_request_v2'
    engine = historical_inventory_v2 if version2 else historical_inventory
    result = engine(history, **query)
    # The file manifest fingerprints the WHOLE input, including future/private records.
    # Therefore persisted results are stricter than the in-memory temporal view.
    if input_path.is_relative_to(private_root) or any(i.evidence.access == 'PRIVATE' for i in history):
        result['access'] = 'PRIVATE'
    if not output_path.is_relative_to(private_root):
        require_public_result(result)
    payload = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')
    result['reproducibility'] = {
        'schema_version': 'historical_assignments_manifest_v1',
        'input_sha256': hashlib.sha256(raw).hexdigest(),
        'analysis_payload_sha256': hashlib.sha256(payload).hexdigest(),
        'payload_encoding': 'UTF-8; sorted keys; compact JSON; exclude reproducibility; no final newline',
        'code_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
                       (*CODE_FILES, 'grid_engine/historical_connection_parameters.py')},
        'python_version': platform.python_version(),
        'python_implementation': platform.python_implementation(),
        'query': query,
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(encoded)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = analyze_file(args.input, args.output, ROOT/'data/private')
    print(f"Saved {result['access']} historical result with embedded manifest; no available-MW calculation.")
