"""Aggregate evidence records without merging entities or assessing connection capacity."""
from collections import Counter
from copy import deepcopy
import hashlib
import json
import re


def aggregate(pipeline: dict, plan: dict, osm: dict, review: dict) -> dict:
    """Bounded Radkowice adapter; source record counts are not asset counts."""
    if pipeline.get('station') != 'Radkowice' or pipeline.get('voltage_kV') != 220:
        raise ValueError('UNSUPPORTED_STATION_SCOPE')
    if osm.get('station_osm_way_id') != 199098055:
        raise ValueError('UNSUPPORTED_OSM_SCOPE')
    expected = [(pipeline, 'radkowice_pse_pipeline_view_v1'), (plan, 'radkowice_prsp_review_v1'),
                (osm, 'osm_station_spatial_audit_v1'), (review, 'radkowice_investment_dates_v1')]
    if any(value.get('method') != method for value, method in expected):
        raise ValueError('SOURCE_SCHEMA_CHANGED')
    records, identities = [], set()

    def add(kind: str, key: str, title: str, association: str, evidence: dict, original: dict) -> None:
        for field in ('source_id', 'source_url', 'retrieval_date', 'snapshot_sha256', 'locator'):
            if not evidence.get(field):
                raise ValueError('MISSING_PROVENANCE:' + field)
        if not re.fullmatch(r'[0-9a-f]{64}', evidence['snapshot_sha256']):
            raise ValueError('INVALID_SOURCE_HASH')
        identity = f"{kind}:{evidence['source_id']}:{key}"
        if identity in identities:
            raise ValueError('DUPLICATE_SOURCE_RECORD')
        identities.add(identity)
        records.append({'evidence_id': hashlib.sha256(identity.encode()).hexdigest(),
                        'record_kind': kind, 'source_record_key': key, 'title': title,
                        'station_association': association, 'canonical_entity_id': None,
                        'interpretation': 'NOT_ASSESSED', 'provenance': deepcopy(evidence),
                        'source_record': deepcopy(original)})

    for r in pipeline['records']:
        if r['connection_point_reported'] != 'Radkowice' or r['voltage_kV'] != 220:
            raise ValueError('PROJECT_SCOPE_CONFLICT')
        evidence = {k: r.get(k) for k in ('source_id', 'source_url', 'source_date', 'retrieval_date', 'snapshot_sha256')}
        evidence.update(source_quality='B', locator=f"{r['sheet']}!row {r['row']}")
        add('PROJECT_PUBLICATION', r['research_record_id'], r['project_name'], 'REPORTED_CONNECTION_POINT', evidence, r)
    for r in plan['records']:
        evidence = {k: r.get(k) for k in ('source_id', 'source_url', 'source_date', 'source_month', 'source_date_precision', 'retrieval_date', 'snapshot_sha256', 'source_quality')}
        evidence['locator'] = f"PDF page {r['source_page']}; task {r['operator_task_id']}"
        add('GRID_INVESTMENT_PUBLICATION', r['operator_task_id'], r['title_reported'], 'REVIEWED_DOCUMENTARY_ASSOCIATION', evidence, r)
    for r in osm['records']:
        s = osm['source']
        key = f"{r['osm_type']}/{r['osm_id']}"
        evidence = {'source_id': s['source_id'], 'source_url': r['osm_url'], 'source_date': None,
                    'retrieval_date': s['retrieval_date'], 'snapshot_sha256': s['sha256'],
                    'source_quality': 'G', 'locator': key, 'source_version': r['osm_version'],
                    'edit_timestamp_not_observation_date': r['osm_edit_timestamp']}
        add('OSM_SPATIAL_RECORD', key, r['tags_reported_by_osm'].get('name') or key,
            'CALCULATED_SPATIAL_ASSOCIATION_ONLY', evidence, r)
    for r in review['claims']:
        s = r['evidence']
        evidence = {'source_id': s['source_id'], 'source_url': s['url'], 'source_date': s.get('source_date'),
                    'retrieval_date': s['retrieval_date'], 'snapshot_sha256': s['snapshot_sha256'],
                    'locator': s['locator'], 'source_quality': r['source_quality']}
        add('INVESTMENT_DATE_CLAIM', s['source_id'], review['subject'], 'REVIEWED_SUBJECT_IDENTITY_UNCONFIRMED', evidence, r)
    records.sort(key=lambda r: r['evidence_id'])
    return {'method': 'radkowice_evidence_aggregation_v1', 'station': 'Radkowice',
            'scope': 'PUBLIC_SNAPSHOTS_ONLY_NOT_CURRENT_COMPLETE_INVENTORY',
            'record_counts': dict(sorted(Counter(r['record_kind'] for r in records).items())),
            'source_record_count': len(records), 'unique_project_count': None, 'unique_asset_count': None,
            'records': records, 'unresolved_review': deepcopy(review),
            'attribution': {'osm': '© OpenStreetMap contributors', 'license': 'ODbL-1.0',
                            'url': 'https://www.openstreetmap.org/copyright'},
            'limitations': ['Aggregation of evidence, not a merge of grid entities.',
                           'No capacity, loading, feasibility, probability or score is calculated.',
                           'Source dates and status claims are retained; retrieval date does not make them current.',
                           'Spatial association does not establish electrical connectivity or equipment ownership.',
                           'Planned projects are not commissioned assets; no automatic positive/negative assessment.',
                           'OSM-derived records remain identifiable separately from operator publications.']}


def encode(result: dict) -> bytes:
    return (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n').encode('utf8')
