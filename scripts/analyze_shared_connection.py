"""Replay a curated JSON snapshot without downloading data or scanning folders."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from grid_engine.shared_connection import (
    Assignment, Evidence, SharedConnectionSnapshot, require_public_result, summarize,
)


def decode_snapshot(raw: bytes) -> SharedConnectionSnapshot:
    def reject_constant(value: str) -> None:
        raise ValueError('NONFINITE_JSON_NUMBER')

    data = json.loads(raw.decode('utf-8-sig'), parse_float=Decimal, parse_constant=reject_constant)
    for field in ['position_evidence', 'coverage_evidence', 'export_evidence', 'import_evidence']:
        if data.get(field) is not None:
            data[field] = Evidence(**data[field])
    for field in ['export_limit_MW', 'import_limit_MW']:
        value = data.get(field)
        if value is not None:
            if type(value) not in {str, int, Decimal}:
                raise ValueError('INVALID_MW_LIMIT')
            data[field] = Decimal(value)
    data['assignments'] = tuple(Assignment(**{**a, 'evidence':Evidence(**a['evidence'])})
                                for a in data.get('assignments', []))
    return SharedConnectionSnapshot(**data)


def analyze_file(input_path: Path, output_path: Path, private_root: Path) -> dict:
    input_path, output_path, private_root = input_path.resolve(), output_path.resolve(), private_root.resolve()
    if input_path.suffix.lower() != '.json' or output_path.suffix.lower() != '.json':
        raise ValueError('JSON_PATH_REQUIRED')
    if '_secrets' in [part.lower() for part in input_path.parts]:
        raise ValueError('SECRET_INPUT_FORBIDDEN')
    raw = input_path.read_bytes()
    result = summarize(decode_snapshot(raw))
    # Files originating in the private workspace stay private even if mislabeled.
    if input_path.is_relative_to(private_root):
        result['access'] = 'PRIVATE'
    if not output_path.is_relative_to(private_root):
        require_public_result(result)
    result['reproducibility'] = {
        'input_sha256':hashlib.sha256(raw).hexdigest(),
        'engine_sha256':hashlib.sha256((ROOT/'grid_engine/shared_connection.py').read_bytes()).hexdigest(),
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Historical results are immutable: caller chooses a new output version.
    with output_path.open('x', encoding='utf-8', newline='\n') as file:
        file.write(encoded)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = analyze_file(args.input, args.output, ROOT/'data/private')
    print(f"Saved {result['access']} result; method={result['method']}; no available-MW calculation.")
