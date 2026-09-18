"""Bulk heading index: documentary mentions, not grid or task identities."""
from __future__ import annotations

import hashlib
import re

from connectors.pse.investment_dates import Sections, normalized

STATUSES = r'w przygotowaniu|w budowie|zakończona'


def parse_headings(html: str) -> list[dict]:
    parser = Sections()
    parser.feed(html)
    parser.close()
    parser.finish()
    records = {}
    for position, (title, _) in enumerate(parser.blocks, 1):
        if not title:
            continue
        if title not in records:
            statuses = re.findall(r'\((' + STATUSES + r')\)', title)
            final = re.search(r'\((' + STATUSES + r')\)$', title)
            records[title] = {
                'heading_id': hashlib.sha256(title.encode('utf-8')).hexdigest(),
                'title_reported': title, 'h4_positions': [],
                'status_reported': final[1] if len(statuses) == 1 and final else None,
                'status_review_required': len(statuses) != 1 or final is None,
                'classification': 'REPORTED', 'source_date': None,
                'canonical_station_id': None, 'operator_task_id': None,
                'commissioning_date': None,
            }
        records[title]['h4_positions'].append(position)
    if not records:
        raise ValueError('NO_HEADINGS')
    return list(records.values())


def profile_mentions(profiles: list[dict], headings: list[dict]) -> list[dict]:
    results = []
    for profile in profiles:
        name = normalized(profile['name_reported']).casefold()
        if not name:
            raise ValueError('EMPTY_PROFILE_NAME')
        pattern = re.compile(r'(?<!\w)' + re.escape(name) + r'(?!\w)')
        matches = [h['heading_id'] for h in headings
                   if pattern.search(h['title_reported'].casefold())]
        results.append({'profile_id': profile['profile_id'],
                        'name_reported': profile['name_reported'],
                        'voltage_kV': profile['voltage_kV'],
                        'heading_ids': matches, 'relationship': 'NAME_MENTION_ONLY',
                        'classification': 'INFERRED', 'canonical_station_id': None,
                        'voltage_relevance': 'UNKNOWN', 'interpretation': 'unknown'})
    return results
