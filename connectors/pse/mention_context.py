"""Conservative textual context; never establishes asset identity or connectivity."""
from __future__ import annotations

import re


def contexts(title: str, name: str, voltage_kV: int) -> list[dict]:
    if not name.strip():
        raise ValueError('EMPTY_NAME')
    result = []
    # Preserve character positions by matching original text, without casefold expansion.
    for match in re.finditer(r'(?<!\w)' + re.escape(name) + r'(?!\w)', title, re.I):
        before, after = title[:match.start()], title[match.end():]
        station = re.search(
            r'\bstacji\s+(?:elektroenergetycznej\s+)?'
            r'(?:(?P<voltage>\d+(?:/\d+)*)\s*kV\s+)?$', before, re.I)
        # Reject a shorter name embedded in a longer station label.
        name_end = re.match(r'\s*(?:$|\(|[–—-]|wraz\b|w\b|dla\b|oraz\b|o\b)', after, re.I)
        farm = re.search(r'\b(?:FW|farmy wiatrowej|farmy fotowoltaicznej)\s*$', before, re.I)
        if station and name_end:
            kind = 'EXPLICIT_STATION_LABEL'
            volts = [int(v) for v in station['voltage'].split('/')] if station['voltage'] else []
        elif farm:
            kind, volts = 'EXPLICIT_FARM_LABEL', []
        else:
            kind, volts = 'OTHER_OR_UNRESOLVED_MENTION', []
        result.append({'start': match.start(), 'end': match.end(),
                       'matched_text': match[0], 'context_kind': kind,
                       'station_label_voltage_kV': volts,
                       'profile_voltage_comparison': ('LISTED' if voltage_kV in volts else
                                                       'NOT_LISTED' if volts else 'UNKNOWN'),
                       'classification': 'INFERRED'})
    return result


def annotate(index: dict) -> list[dict]:
    headings = {h['heading_id']: h for h in index['headings']}
    if len(headings) != len(index['headings']):
        raise ValueError('DUPLICATE_HEADING_ID')
    rows = []
    for profile in index['profiles']:
        for heading_id in profile['heading_ids']:
            if heading_id not in headings:
                raise ValueError('MISSING_HEADING')
            mentions = contexts(headings[heading_id]['title_reported'], profile['name_reported'], profile['voltage_kV'])
            if not mentions:
                raise ValueError('MENTION_NOT_FOUND')
            rows.append({'profile_id': profile['profile_id'], 'heading_id': heading_id,
                         'mentions': mentions, 'canonical_station_id': None,
                         'identity_status': 'UNCONFIRMED', 'interpretation': 'unknown',
                         'current_station_voltage_kV': None,
                         'review_required': True})
    return rows
