"""Lexical discovery in a historical compilation; never infer electrical connectivity."""
from __future__ import annotations

NAME_FIELDS = ('Name', 'Nazwa obiektu', 'Nazwa stacji', 'Nazwa linii')
DESCRIPTION_FIELDS = ('Nazwa zadania inwestycyjnego', 'Nazwa lub opis planowanego zadania',
                      'Nazwa lub opis planowanej modernizacji', 'Nazwa lub opis realizowanego zadania',
                      'Nazwa lub opis zrealizowanego zadania')


def canonical_text(value: str) -> str:
    return ' '.join(value.casefold().split())


def discover(properties: dict, query: str) -> list[dict]:
    """Preserve match context: object name, group label and task description differ."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError('NONEMPTY_QUERY_REQUIRED')
    term = canonical_text(query)
    matches = []
    for field in (*NAME_FIELDS, 'Group', *DESCRIPTION_FIELDS):
        value = properties.get(field)
        if not isinstance(value, str):
            continue
        normalized = canonical_text(value)
        if field == 'Group':
            group_parts = [canonical_text(part) for part in value.split('/')]
            matched = term in group_parts
            kind = 'EXACT_GROUP_LABEL' if len(group_parts) == 1 else 'COMPOUND_GROUP_COMPONENT'
        else:
            matched = term in normalized
            kind = 'NAME_MENTION' if field in NAME_FIELDS else 'TASK_MENTION'
        if matched:
            matches.append({'source_field': field, 'raw_value': value, 'match_kind': kind,
                            'electrical_relationship': 'UNKNOWN'})
    return matches
