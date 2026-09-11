"""Validation for a documentary graph, never an electrical power-flow model."""
from datetime import date, datetime
import re


def validate_graph(graph: dict) -> None:
    if graph.get('schema_version') != 'evidence_graph_v1':
        raise ValueError('SCHEMA_VERSION')
    entities = graph['entities']
    ids = [e['id'] for e in entities]
    if len(ids) != len(set(ids)):
        raise ValueError('DUPLICATE_ENTITY')
    edges = graph['relationships']
    if len({e['id'] for e in edges}) != len(edges):
        raise ValueError('DUPLICATE_RELATIONSHIP')
    for item in entities + edges:
        if not item.get('evidence'):
            raise ValueError('MISSING_EVIDENCE')
        for evidence in item['evidence']:
            if not evidence.get('source_id') or not evidence.get('locator'):
                raise ValueError('MISSING_LOCATOR')
            if not re.fullmatch('[a-f0-9]{64}', evidence.get('snapshot_sha256', '')):
                raise ValueError('INVALID_HASH')
            if evidence.get('source_date'):
                date.fromisoformat(evidence['source_date'])
            datetime.fromisoformat(evidence['retrieval_date'].replace('Z', '+00:00'))
        if item.get('classification') not in {'REPORTED', 'CALCULATED', 'INFERRED'}:
            raise ValueError('INVALID_CLASSIFICATION')
    for edge in edges:
        if edge['from_id'] not in ids or edge['to_id'] not in ids:
            raise ValueError('DANGLING_ENDPOINT')
        if edge['relation'] == 'PLANNED_CONNECTION' and edge['physical_connection_confirmed'] is not False:
            raise ValueError('PLANNED_IS_NOT_CONNECTED')
        if edge['relation'] == 'REPORTED_LINE' and edge.get('voltage_kV') != 220:
            raise ValueError('UNVERIFIED_VOLTAGE')
    if graph['power_flow_ready'] is not False:
        raise ValueError('NOT_A_POWER_FLOW_MODEL')
