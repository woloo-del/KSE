"""Link identical source records, never infer that neighboring assets are connected."""
from collections import Counter
import hashlib
from pathlib import Path

from grid_engine.evidence_graph import validate_graph


def link_records(ledger: dict, graph: dict) -> dict:
    if ledger.get('method') != 'radkowice_evidence_aggregation_v1':
        raise ValueError('UNSUPPORTED_LEDGER')
    validate_graph(graph)
    entities = {r['id']: r for r in graph['entities']}
    ids = [r['evidence_id'] for r in ledger['records']]
    if len(set(ids)) != len(ids):
        raise ValueError('DUPLICATE_EVIDENCE_ID')
    results = []
    for record in ledger['records']:
        target = entities.get(record['source_record_key'])
        provenance = record['provenance']
        status, reason, entity_id = 'UNLINKED', 'NO_EXACT_SOURCE_RECORD_MATCH', None
        if record['record_kind'] == 'PROJECT_PUBLICATION' and target and target['kind'] == 'PROJECT_RECORD':
            if any(e['source_id'] == provenance['source_id'] and e['snapshot_sha256'] == provenance['snapshot_sha256'] for e in target['evidence']):
                status, reason, entity_id = 'SAME_SOURCE_RECORD', 'EXACT_RECORD_ID_SOURCE_AND_SNAPSHOT', target['id']
            else:
                reason = 'SOURCE_OR_VERSION_CONFLICT'
        elif record['record_kind'] == 'OSM_SPATIAL_RECORD':
            reason = 'SPATIAL_ASSOCIATION_IS_NOT_ENTITY_IDENTITY'
        elif record['record_kind'] == 'INVESTMENT_DATE_CLAIM':
            reason = 'INVESTMENT_SCOPE_IDENTITY_UNCONFIRMED'
        elif record['record_kind'] == 'GRID_INVESTMENT_PUBLICATION':
            reason = 'OPERATOR_TASK_NOT_RESOLVED_TO_GRAPH_ASSET'
        results.append({'evidence_id': record['evidence_id'], 'graph_entity_id': entity_id,
                        'status': status, 'reason': reason,
                        'cross_source_identity_confirmed': False,
                        'physical_connection_confirmed': False})
    return {'method': 'exact_evidence_record_link_v1', 'links': results,
            'status_counts': dict(Counter(r['status'] for r in results)),
            'method_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'limitations': ['Matches identify the same publication row in two derived views, not independent corroboration.',
                           'No matching by name, proximity or common station label.',
                           'Unlinked means identity not resolved, not that an asset is absent.',
                           'No new physical grid edges or confirmed operating status are created.']}
