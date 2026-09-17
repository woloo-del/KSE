"""Reproduce a limited public PRSP review; never treat planned years as commissioning."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.pse.development_plan import extract_row


def build() -> dict:
    meta = json.loads((ROOT / 'data/catalog/probe_results_radkowice_prsp_2026-09-17.json').read_text(encoding='utf8'))[0]
    source = ROOT / meta['local_path']
    if hashlib.sha256(source.read_bytes()).hexdigest() != meta['sha256']:
        raise ValueError('SNAPSHOT_CHANGED')
    pdf = PdfReader(source)
    if len(pdf.pages) != 120 or 'Kwiecień 2026' not in pdf.pages[0].extract_text():
        raise ValueError('PLAN_EDITION_CHANGED')
    specifications = [
        (58, 'III.82', 'Modernizacja (rozbudowa) linii 220 kV Kielce-Radkowice',
         'Rozbudowa stacji 400/220 kV Joachimów', 'PLANNED_IN_DOCUMENT'),
        (67, 'II.47', 'Rozbudowa i modernizacja stacji 220/110 kV Radkowice',
         'II.48 ', 'IMPLEMENTATION_REPORTED_IN_DOCUMENT'),
    ]
    records = []
    for page, row_id, title, next_anchor, status in specifications:
        row = extract_row(pdf.pages[page-1].extract_text(), row_id, title, next_anchor)
        row.update({'source_id': meta['source_id'], 'source_url': meta['url'],
                    'source_page': page, 'snapshot_sha256': meta['sha256'],
                    'retrieval_date': meta['retrieval_date'], 'source_quality': 'B',
                    'source_date': None, 'source_month': '2026-04', 'source_date_precision': 'MONTH',
                    'status_in_document': status, 'current_status': 'UNKNOWN',
                    'valid_from': None, 'valid_to': None,
                    'completion_year_meaning': 'TECHNICAL_FINANCIAL_AND_FORMAL_COMPLETION',
                    'completion_definition_page': 62 if page == 58 else 75})
        records.append(row)
    return {'method': 'radkowice_prsp_review_v1', 'access': 'PUBLIC_SOURCE_REVIEW',
            'document_status': 'POST_CONSULTATION_DRAFT', 'approval_verified': False,
            'records': records, 'limitations': [
                'Limited to two verified investment rows, not the full investment or project list.',
                'Planned completion includes financial and formal closure, not only energization.',
                'No automatic identity match to the transformer replacement or private bus bridge.',
                'No additional available MW, current commissioning or promise of connection is established.',
            ]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = build()
    with args.output.open('x', encoding='utf8', newline='\n') as target:
        target.write(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(args.output)
