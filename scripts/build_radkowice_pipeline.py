"""Build a source-scoped research view; not a deduplicated station inventory."""
from __future__ import annotations

from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.research_radkowice import extract

METHOD = 'radkowice_pse_pipeline_view_v1'
AGREEMENT_STATUS = 'UMOWA O PRZYŁĄCZENIE obowiązująca'


def build_view(sample: dict) -> dict:
    """Only the evidenced agreement status is mapped; other statuses stay unknown."""
    rows = sample['records']
    seen: set[str] = set()
    output = []
    for row in rows:
        record_id = row['research_record_id']
        if record_id in seen:
            raise ValueError('DUPLICATE_SOURCE_RECORD')
        seen.add(record_id)
        if (row['source_id'] != 'PSE_PIPELINE' or row['source_date'] != '2026-07-31'
                or row['connection_point_reported'] != 'Radkowice' or row['voltage_kV'] != 220
                or row['classification'] != 'REPORTED'):
            raise ValueError('UNSUPPORTED_SOURCE_SCOPE')
        for field in ['snapshot_sha256', 'source_url', 'retrieval_date', 'sheet', 'row', 'cells']:
            if not row.get(field):
                raise ValueError('MISSING_PROVENANCE')
        powers = {}
        for field in ['connection_export_MW', 'connection_import_MW']:
            value = row[field]
            if isinstance(value, bool):
                raise ValueError('INVALID_POWER')
            number = None if value is None else Decimal(str(value))
            if number is not None and (not number.is_finite() or number < 0):
                raise ValueError('INVALID_POWER')
            powers[field] = None if number is None else str(number)
        output.append({**row, **powers,
                       'group': 'B_PLANNED' if row['status_reported'] == AGREEMENT_STATUS else 'UNKNOWN',
                       'status_interpretation': 'Agreement does not confirm completed connection; no inference from delivery date.',
                       'project_identity_resolved_across_sources': False,
                       'bridge_assignment': None})
    groups = {}
    for group in ['A_CONNECTED', 'B_PLANNED', 'C_AWAITING_RESPONSE', 'UNKNOWN']:
        selected = [row for row in output if row['group'] == group]
        sums = {}
        for direction in ['export', 'import']:
            field = f'connection_{direction}_MW'
            values = [Decimal(row[field]) for row in selected if row[field] is not None]
            sums[direction] = {
                'known_row_sum_MW': str(sum(values, Decimal('0'))) if values else None,
                'missing_power_rows': sum(row[field] is None for row in selected),
                'classification': 'CALCULATED' if values else 'UNKNOWN',
                'formula': f'SUM(non-null {field} for listed source_record_ids)',
                'source_record_ids': [row['research_record_id'] for row in selected if row[field] is not None],
            }
        groups[group] = {'known_source_row_count': len(selected), 'station_project_count': None,
                         'powers': sums,
                         'coverage': 'PARTIAL; zero rows means no supporting records in this view, not zero station projects.'}
    return {'method': METHOD, 'source_date': '2026-07-31',
            'station': 'Radkowice', 'voltage_kV': 220,
            'coverage': 'One preserved PSE snapshot; no complete PGE inventory or cross-source entity resolution.',
            'limitations': ['Sums describe rows, not deduplicated projects, actual flows or reserved/available grid capacity.',
                            'No confirmation of physical connection or outstanding unanswered applications.',
                            'No assignment to shared bridge; no station score or probability.'],
            'groups': groups, 'records': output}


def main() -> None:
    result = build_view(extract())
    result['code_sha256'] = {
        str(path.relative_to(ROOT).as_posix()): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [Path(__file__), ROOT / 'scripts/research_radkowice.py']}
    target = ROOT / 'data/reference/radkowice_pipeline_view_2026-07-31_v1.json'
    content = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    if target.exists():
        if target.read_bytes() != content:
            raise ValueError('EXISTING_DIFFERENT_VIEW: retain history and use a new version')
    else:
        with target.open('xb') as stream:
            stream.write(content)
    print(target)


if __name__ == '__main__':
    main()
