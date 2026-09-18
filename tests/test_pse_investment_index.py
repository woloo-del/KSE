"""Synthetic HTML plus preserved operator snapshot; never promote mentions."""
import unittest
from connectors.pse.investment_index import parse_headings, profile_mentions
from scripts.build_pse_investment_index import build


class InvestmentIndexTests(unittest.TestCase):
    def test_duplicate_text_keeps_locators(self):
        rows = parse_headings('<h4>Task (w budowie)</h4><h4></h4><h4>Task (w budowie)</h4>')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['h4_positions'], [1, 3])

    def test_compound_and_missing_status_require_review(self):
        for title in ['Task', 'Task (nowy status)', 'A (w budowie) B (zakończona)']:
            row = parse_headings('<h4>' + title + '</h4>')[0]
            self.assertIsNone(row['status_reported'])
            self.assertTrue(row['status_review_required'])
        self.assertEqual(parse_headings('<h4>A (zakończona)</h4>')[0]['status_reported'], 'zakończona')

    def test_boundary_and_no_alias_or_voltage_promotion(self):
        headings = parse_headings('<h4>Linia Test-Other 400 kV (w budowie)</h4><h4>Tester</h4>')
        profiles = [{'profile_id': str(i), 'name_reported': name, 'voltage_kV': 110}
                    for i, name in enumerate(['Test', 'Test (planowana)', 'Test Systemowa'])]
        rows = profile_mentions(profiles, headings)
        self.assertEqual([len(r['heading_ids']) for r in rows], [1, 0, 0])
        self.assertTrue(all(r['canonical_station_id'] is None and r['voltage_relevance'] == 'UNKNOWN' for r in rows))

    def test_missing_html_stops(self):
        with self.assertRaisesRegex(ValueError, 'NO_HEADINGS'):
            parse_headings('<html>Service unavailable</html>')

    def test_real_snapshot_profiles_and_multistage(self):
        result = build()
        self.assertEqual(result['metrics']['profiles'], 50)
        self.assertEqual(result['metrics']['confirmed_station_identities'], 0)
        baczyna = [h for h in result['headings'] if 'Etap II (w przygotowaniu) Budowa' in h['title_reported']]
        self.assertTrue(baczyna)
        self.assertTrue(all(h['status_reported'] is None for h in baczyna))


if __name__ == '__main__':
    unittest.main()
