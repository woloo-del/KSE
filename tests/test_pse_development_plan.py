import unittest
from pathlib import Path

from connectors.pse.development_plan import extract_row
from scripts.build_radkowice_development_plan import build, ROOT


class PlanTests(unittest.TestCase):
    def parse(self, body):
        return extract_row('Rok rozpoczęcia Rok zakończenia II.1 Synthetic ' + body,
                           'II.1', 'Synthetic', 'II.2 ')

    def test_years_are_not_current_capacity(self):
        row = self.parse('Purpose 2020 2024 II.2 Other 2025 2027')
        self.assertEqual(row['completion_year_reported'], 2024)
        self.assertIsNone(row['commissioning_date'])
        self.assertIsNone(row['additional_available_capacity_MW'])
        self.assertFalse(row['current_grid_eligible'])

    def test_missing_year_does_not_take_neighbour_year(self):
        with self.assertRaisesRegex(ValueError, 'SCHEMA'):
            self.parse('Purpose 2020 II.2 Other 2025 2027')

    def test_reversed_years_rejected(self):
        with self.assertRaisesRegex(ValueError, 'ORDER'):
            self.parse('Purpose 2030 2024 II.2 Other')

    def test_footnote_or_changed_boundary_requires_review(self):
        for body in ['Purpose 2020 2024 (2) II.2 Other', 'Purpose 2020 2024 II.3 Other']:
            with self.assertRaises(ValueError):
                self.parse(body)

    @unittest.skipUnless((ROOT / 'data/raw/research/2026-09-17/pse_prsp_2027_2036_post_consultation.pdf').exists(), 'Restore source archive for replay')
    def test_real_snapshot(self):
        result = build()
        self.assertEqual([(r['operator_task_id'], r['completion_year_reported']) for r in result['records']],
                         [('III.82', 2034), ('II.47', 2032)])
        self.assertFalse(result['approval_verified'])


if __name__ == '__main__':
    unittest.main()
