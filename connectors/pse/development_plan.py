"""Bounded extraction of two visually verified rows in the April 2026 PRSP draft."""
import re


def extract_row(page_text: str, row_id: str, title: str, next_anchor: str) -> dict:
    text = ' '.join(page_text.split())
    if 'Rok rozpoczęcia Rok zakończenia' not in text:
        raise ValueError('PLAN_HEADER_CHANGED')
    start = row_id + ' ' + title + ' '
    if text.count(start) != 1:
        raise ValueError('PLAN_ROW_MISSING_OR_DUPLICATED')
    tail = text.split(start, 1)[1]
    if next_anchor not in tail:
        raise ValueError('PLAN_ROW_BOUNDARY_MISSING')
    body = tail.split(next_anchor, 1)[0].strip()
    match = re.fullmatch(r'(.+?) (20\d{2}) (20\d{2})', body)
    if not match or re.search(r'\b(?:II|III)\.\d+\b', body):
        raise ValueError('PLAN_ROW_SCHEMA_CHANGED')
    begin, end = int(match[2]), int(match[3])
    if begin > end:
        raise ValueError('PLAN_YEAR_ORDER_INVALID')
    return {'operator_task_id': row_id, 'title_reported': title,
            'purpose_reported': match[1], 'start_year_reported': begin,
            'completion_year_reported': end, 'classification': 'REPORTED',
            'commissioning_date': None, 'additional_available_capacity_MW': None,
            'current_grid_eligible': False}
