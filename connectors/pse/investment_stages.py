"""Parse the two explicitly numbered Radkowice stages, without PRSP identity inference."""
import re
from connectors.pse.investment_dates import Sections


def parse_stages(html: str) -> list[dict]:
    parser = Sections()
    parser.feed(html)
    parser.close()
    parser.finish()
    records = []
    for title, _ in parser.blocks:
        if 'Radkowice' not in title or 'Etap' not in title:
            continue
        match = re.fullmatch(r'Rozbudowa i modernizacja stacji 220/110 kV Radkowice [–-] Etap (II|I) \((w przygotowaniu|w budowie|zakończona)\)', title)
        if not match:
            raise ValueError('STAGE_HEADER_CHANGED')
        stage, status = match.groups()
        records.append({'stage': stage, 'title_reported': title,
                        'status_reported': status, 'classification': 'REPORTED',
                        'operator_task_id': None, 'specific_asset_identity': None,
                        'commissioning_date': None, 'source_date': None})
    if sorted(r['stage'] for r in records) != ['I', 'II']:
        raise ValueError('MISSING_OR_DUPLICATE_STAGE')
    return sorted(records, key=lambda r: r['stage'])
