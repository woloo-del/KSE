import json
from pathlib import Path
import unittest
from xml.sax.saxutils import escape

from connectors.gis.ownership_paging import fetch_page_chain, inspect_pages, validated_next
from tests.test_ownership_normalization import synthetic
from tests.test_ownership_snapshot import source


def page(index, *, matched='2', next_page=None, identifier=None):
    url = source(b'', COUNT=1, STARTINDEX=index)['url']
    attributes = f'numberReturned="1" numberMatched="{matched}"'
    if next_page is not None:
        attributes += f' next="{escape(next_page, {chr(34): "&quot;"})}"'
    raw = synthetic().replace(b'numberReturned="1"', attributes.encode())
    raw = raw.replace(b'>synthetic<', f'>{identifier or str(index)}<'.encode())
    manifest = source(raw, COUNT=1, STARTINDEX=index)
    manifest['source_id'] = f'synthetic-page-{index}'
    return raw, manifest


def chain():
    second = page(1)
    return [page(0, next_page=second[1]['url']), second]


class OwnershipPagingTests(unittest.TestCase):
    def test_complete_chain_preserves_page_provenance(self):
        result = inspect_pages(chain(), transaction_safe=True)
        self.assertEqual(result['status'], 'PAGE_CHAIN_READY_FOR_SPATIAL_REVIEW')
        self.assertEqual(result['unique_parcel_count'], 2)
        self.assertEqual([r['source_id'] for r in result['observations']], ['synthetic-page-0', 'synthetic-page-1'])
        self.assertIsNone(result['area_result'])

    def test_unsafe_snapshot_and_unknown_count_remain_blocked(self):
        second = page(1, matched='unknown')
        first = page(0, matched='unknown', next_page=second[1]['url'])
        result = inspect_pages([first, second])
        self.assertTrue(result['server_sequence_exhausted'])
        self.assertEqual(result['blocking_reasons'], ['MATCHED_COUNT_UNKNOWN', 'TRANSACTIONAL_SNAPSHOT_NOT_GUARANTEED'])

    def test_truncation_and_changed_totals(self):
        self.assertIn('PAGE_CHAIN_NOT_FINISHED', inspect_pages(chain()[:1])['blocking_reasons'])
        changed = chain(); changed[1] = page(1, matched='3')
        with self.assertRaisesRegex(ValueError, 'MATCHED_COUNT_CHANGED'):
            inspect_pages(changed)

    def test_duplicate_and_missing_page(self):
        duplicate = chain(); duplicate[1] = page(1, identifier='0')
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_PARCEL'):
            inspect_pages(duplicate)
        for rows in [chain()[1:], list(reversed(chain())), [page(0), page(1)]]:
            with self.assertRaises(ValueError):
                inspect_pages(rows)

    def test_foreign_changed_or_looping_next_is_rejected(self):
        valid = page(1)[1]['url']
        for bad in [valid.replace('example.invalid', 'foreign.invalid'), valid.replace('STARTINDEX=1', 'STARTINDEX=0'),
                    valid + '&FILTER=changed', valid.replace('COUNT=1', 'COUNT=2')]:
            raw, manifest = page(0, next_page=bad)
            with self.assertRaises(ValueError):
                validated_next(raw, manifest['url'])

    def test_fetch_limits_and_archiving_before_parse(self):
        inputs = chain(); by_url = {s['url']: (raw, s) for raw, s in inputs}
        fetched, archived = [], []
        def fetch(url):
            fetched.append(url); return by_url[url][0]
        def archive(url, raw):
            archived.append(raw); return by_url[url][1]
        pages = fetch_page_chain(inputs[0][1]['url'], fetch=fetch, archive=archive)
        self.assertEqual(len(pages), 2)
        fetched.clear()
        with self.assertRaisesRegex(ValueError, 'PAGE_LIMIT_REACHED'):
            fetch_page_chain(inputs[0][1]['url'], fetch=fetch, archive=archive, max_pages=1)
        self.assertEqual(len(fetched), 1)
        archived.clear()
        with self.assertRaises(ValueError):
            fetch_page_chain(inputs[0][1]['url'], fetch=lambda url: b'<Exception/>', archive=archive)
        self.assertEqual(archived, [b'<Exception/>'])

    def test_real_archived_pages(self):
        rows = json.loads(Path('data/catalog/probe_results_ownership_paging_2026-09-19.json').read_text(encoding='utf8'))
        inputs = []
        for row in rows:
            if '_PAGE_' in row['source_id']:
                path = Path(row['local_path'])
                if not path.exists(): self.skipTest('Restore paging archive')
                inputs.append((path.read_bytes(), row))
        result = inspect_pages(inputs)
        self.assertEqual(result['unique_parcel_count'], 2)
        self.assertTrue(result['server_sequence_exhausted'])
        self.assertIn('MATCHED_COUNT_UNKNOWN', result['blocking_reasons'])
