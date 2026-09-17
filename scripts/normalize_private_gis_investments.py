"""Build an immutable private registry of historical investment source records."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.geopackage import read_features
from connectors.gis.historical_investments import LAYERS, normalize_record


def build(root: Path, output: Path) -> dict:
    private = (ROOT / 'data/private').resolve()
    root, output = root.resolve(), output.resolve()
    if not root.is_relative_to(private) or not output.is_relative_to(private) or output.is_relative_to(root) or output.exists():
        raise ValueError('Use private source directory and new separate private output directory.')
    paths = [root / (stem + '.gpkg') for stem in LAYERS]
    if not all(p.is_file() for p in paths):
        raise ValueError('EXPECTED_INVESTMENT_LAYER_MISSING')
    records, inputs = [], []
    for path in paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        source = path.relative_to(private).as_posix()
        features, errors = read_features(path)
        if errors:
            raise ValueError('GEOMETRY_ERRORS_PREVENT_COMPLETE_REGISTRY')
        inputs.append({'path': source, 'sha256': digest, 'records': len(features)})
        for feature in features:
            records.append(normalize_record(path.stem, feature.table, feature.fid,
                                            feature.properties, source, digest))
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('SOURCE_CHANGED_DURING_NORMALIZATION')
    if len({r['source_record_id'] for r in records}) != len(records):
        raise ValueError('DUPLICATE_SOURCE_RECORD_ID')
    references = defaultdict(list)
    for record in records:
        for link in record['source_links']:
            if link['syntax_valid']:
                references[link['url_candidate']].append({
                    'source_record_id': record['source_record_id'], 'source_field': link['source_field']})
    queue = [{'url': url, 'verification_status': 'NOT_VERIFIED', 'references': refs}
             for url, refs in sorted(references.items())]
    summary = {
        'source_records': len(records), 'unique_investments': None,
        'historical_categories': dict(Counter(r['historical_layer_category'] for r in records)),
        'records_with_links': sum(bool(r['source_links']) for r in records),
        'records_with_quality_issues': sum(bool(r['quality_issues']) for r in records),
        'confirmed_current_statuses': 0,
        'distinct_url_candidates': len(queue),
    }
    result = {'method': 'historical_investment_records_v1', 'access': 'PRIVATE',
              'retrieval_date': datetime.now(timezone.utc).isoformat(),
              'compilation_year_user_declared': 2024, 'compilation_year_independently_verified': False,
              'inputs': inputs, 'summary': summary, 'records': records,
              'limitations': [
                  'Counts describe source records, not unique investments or projects.',
                  'Historical layer membership does not establish current status or commissioning.',
                  'Years may describe a plan; elapsed dates never activate an investment.',
                  'Source URLs are candidates preserved from the compilation, not verified evidence.',
                  'No topology, ownership, electrical parameters or additional MW are derived.',
                  'PSE station task/purpose export discrepancy is retained, not corrected.',
              ]}
    output.mkdir(parents=True)
    (output / 'investment_records.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf8')
    (output / 'source_verification_queue.json').write_text(
        json.dumps({'method': 'exact_url_grouping_v1', 'access': 'PRIVATE', 'items': queue},
                   ensure_ascii=False, indent=2, allow_nan=False), encoding='utf8')
    (output / 'review.md').write_text(
        '# Historyczny rejestr wpisów o inwestycjach\n\n'
        'Wynik prywatny. Liczby dotyczą rekordów źródłowych, nie unikalnych inwestycji.\n\n'
        + '\n'.join(f'- {key}: {value}' for key, value in summary.items())
        + '\n\nBieżący status wszystkich wpisów pozostaje UNKNOWN. Daty z kompilacji nie są potwierdzeniem załączenia. '
        'Linki wymagają osobnej weryfikacji. Szczegóły, oryginalne pola, hashe i ograniczenia: investment_records.json.\n', encoding='utf8')
    print(json.dumps(summary, ensure_ascii=False))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    build(args.root, args.output)
