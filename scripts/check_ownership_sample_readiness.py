"""Replay archived Grudziadz sample through the metric adapter and completeness gate."""
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.ownership_snapshot import prepare_snapshot


def main() -> None:
    manifest = json.loads((ROOT / 'data/catalog/probe_results_ownership_comparison_2026-09-19.json').read_text(encoding='utf-8'))
    source = next(row for row in manifest if row['source_id'].endswith('_WFS'))
    # A query midpoint is a reproducible research point, never an asserted station location.
    bbox = parse_qs(urlparse(source['url']).query)['BBOX'][0].split(',')
    south, west, north, east = map(float, bbox[:4])
    result = prepare_snapshot((ROOT / source['local_path']).read_bytes(), source=source,
                              longitude=(west + east) / 2, latitude=(south + north) / 2,
                              center_source_id='GRUDZIADZ_RESEARCH_QUERY_MIDPOINT',
                              center_source={'locator': source['url'], 'sha256': source['sha256'],
                                             'retrieval_date': source['retrieval_date'],
                                             'method': 'Midpoint of archived query bbox; not station identity.'})
    (ROOT / 'data/reference/ownership_sample_readiness_2026-09-19.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(result['status'], result['blocking_reasons'])


if __name__ == '__main__':
    main()
