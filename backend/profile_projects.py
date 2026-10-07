"""Validate documentary project rows before exposing them in station profiles."""
from collections import Counter
from decimal import Decimal, InvalidOperation

FIELDS = ('record_id', 'row', 'project_name', 'applicant', 'technology_reported',
          'status_reported', 'export_MW', 'import_MW', 'raw_export', 'raw_import',
          'point_reported', 'voltage_reported', 'classification', 'review_reasons')


def project_details(imported: dict, profiles: dict) -> dict:
    if (imported['source_date'] != profiles['source_date'] or
            imported['provenance'] != profiles['provenance']):
        raise ValueError('PROJECT_SOURCE_MISMATCH')
    records = {r['record_id']: r for r in imported['records']}
    if len(records) != len(imported['records']):
        raise ValueError('DUPLICATE_PROJECT_RECORD')
    result = {}
    for p in profiles['profiles']:
        ids = p['record_ids']
        if len(ids) != len(set(ids)) or any(i not in records for i in ids):
            raise ValueError('PROJECT_RECORD_SET_MISMATCH')
        rows = [records[i] for i in ids]
        for row in rows:
            if (row['profile_id'] != p['profile_id'] or
                    row['point_reported'].strip() != p['name_reported'] or
                    row['voltage_reported'] != p['voltage_kV'] or
                    row['classification'] != 'REPORTED' or
                    row['record_id'] != f"pse_pipeline_row_{row['row']}"):
                raise ValueError('PROJECT_ASSOCIATION_MISMATCH')
            for field in ('export_MW', 'import_MW'):
                if row[field] is None:
                    continue
                try:
                    value = Decimal(row[field])
                except (InvalidOperation, TypeError, ValueError):
                    raise ValueError('INVALID_PROJECT_POWER') from None
                if not value.is_finite() or value < 0:
                    raise ValueError('INVALID_PROJECT_POWER')
        if (dict(Counter(r['status_reported'] for r in rows)) != p['status_counts'] or
                {r['record_id'] for r in rows if r['review_reasons']} != set(p['review_record_ids'])):
            raise ValueError('PROJECT_SUMMARY_MISMATCH')
        result[p['profile_id']] = [{key: row[key] for key in FIELDS} for row in rows]
    return result
