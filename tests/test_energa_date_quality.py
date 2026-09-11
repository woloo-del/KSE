"""Synthetic date fixtures are isolated from real source validation."""
import unittest
from pathlib import Path
from connectors.energa.date_quality import assess_dates, inspect_pdf


class DateGateTests(unittest.TestCase):
    def test_conflict_quarantines(self):
        r = assess_dates('2026_08_31.pdf', 'Stan na 30.06.2026 r.')
        self.assertEqual(r['code'], 'DATE_CONFLICT')
        self.assertIsNone(r['source_date'])
        self.assertTrue(r['quarantined'])

    def test_coherence_is_not_current_pipeline_permission(self):
        r = assess_dates('2026_06_30.pdf', 'Stan na 30.06.2026 r.')
        self.assertEqual(r['source_date'], '2026-06-30')
        self.assertFalse(r['current_pipeline_eligible'])

    def test_row_dates_are_not_header(self):
        r = assess_dates('2026_06_30.pdf', 'Wniosek 30.06.2026')
        self.assertEqual(r['code'], 'HEADER_DATE_MISSING')

    def test_invalid_date(self):
        self.assertEqual(assess_dates('2026_06_31.pdf', 'Stan na 30.06.2026')['code'], 'INVALID_DATE')

    def test_multiple_headers(self):
        self.assertTrue(assess_dates('x.pdf', 'Stan na 30.06.2026; Stan na 31.08.2026')['quarantined'])

    def test_metadata_conflict(self):
        self.assertEqual(assess_dates('2026_08_31.pdf', 'Stan na 31.08.2026', 'EOP_stan_30.06.2026.xlsx')['code'], 'DATE_CONFLICT')

    def test_real_snapshot(self):
        path = Path('data/raw/research/2026-09-10/energa_pipeline_2026-08-31.pdf')
        if not path.exists():
            self.skipTest('Restore research archive to test real PDF')
        self.assertEqual(inspect_pdf(path, '2026_08_31.pdf')['claims']['header'], ['2026-06-30'])


if __name__ == '__main__':
    unittest.main()
