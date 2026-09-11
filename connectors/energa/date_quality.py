"""Conservative date gate for research PDFs; does not parse project rows."""
from datetime import datetime
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote

from pypdf import PdfReader


def assess_dates(filename: str, first_page: str, title: str = '') -> dict:
    """Keep competing date claims. Agreement is not proof of dataset freshness."""
    patterns = {
        'filename': (unquote(urlsplit(filename).path), r'(\d{4}_\d{2}_\d{2})', '%Y_%m_%d'),
        'header': (first_page, r'Stan\s+na\s+(\d{2}\.\d{2}\.\d{4})', '%d.%m.%Y'),
        'metadata_title': (title, r'stan[_\s]+(\d{2}\.\d{2}\.\d{4})', '%d.%m.%Y'),
    }
    claims, errors = {}, []
    for origin, (text, pattern, fmt) in patterns.items():
        parsed = set()
        for match in re.findall(pattern, text, flags=re.IGNORECASE):
            try:
                parsed.add(datetime.strptime(match, fmt).date().isoformat())
            except ValueError:
                errors.append('INVALID_DATE:'+origin)
        claims[origin] = sorted(parsed)
    dates = set(d for values in claims.values() for d in values)
    if errors:
        code = 'INVALID_DATE'
    elif len(dates) > 1:
        code = 'DATE_CONFLICT'
    elif len(claims['header']) != 1:
        code = 'HEADER_DATE_MISSING'
    else:
        code = 'DATE_COHERENT'
    accepted = code == 'DATE_COHERENT'
    return {
        'method_version': 'energa_date_gate_v1', 'claims': claims, 'errors': errors,
        'code': code, 'quarantined': not accepted,
        'source_date': claims['header'][0] if accepted else None,
        'source_date_classification': 'REPORTED' if accepted else 'UNKNOWN',
        'current_pipeline_eligible': False,
        'limitation': 'Date coherence alone does not validate rows, completeness, legal use or freshness.',
    }


def inspect_pdf(path: Path, source_url: str) -> dict:
    with path.open('rb') as stream:
        if stream.read(5) != b'%PDF-':
            raise ValueError('SOURCE_CHANGED: expected PDF signature')
    pdf = PdfReader(path)
    if not pdf.pages:
        raise ValueError('SCHEMA_ERROR: empty PDF')
    return assess_dates(source_url, pdf.pages[0].extract_text() or '',
                        str(pdf.metadata.title or '') if pdf.metadata else '')


if __name__ == '__main__':
    import argparse
    import hashlib
    import json
    from datetime import timezone
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--source-url', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = inspect_pdf(args.pdf, args.source_url)
    result.update(source_url=args.source_url, source_page=1,
                  snapshot_sha256=hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
                  checked_at_utc=datetime.now(timezone.utc).isoformat())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(result['code'])
