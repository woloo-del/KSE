"""Synthetic source rows only; no private project fixtures."""
import unittest

from connectors.gis.historical_investments import normalize_record, source_links, year_observation


class HistoricalInvestmentTests(unittest.TestCase):
    def record(self, **changes):
        properties = {'Name': 'Synthetic station', 'Comment': 'test', 'Status': 'planned',
                      'Year': '2020', 'Link': 'https://example.org/source'}
        properties.update(changes)
        return normalize_record('Stacje elektroenergetyczne - WPZP', 'test', 1, properties, 'test.gpkg', 'a' * 64)

    def test_past_year_never_means_commissioned(self):
        result = self.record()
        self.assertEqual(result['year_observations']['Year']['value'], 2020)
        self.assertEqual(result['current_status'], 'UNKNOWN')
        self.assertIsNone(result['actual_commissioning_date'])
        self.assertIsNone(result['additional_available_capacity_MW'])
        self.assertFalse(result['current_grid_eligible'])
        self.assertFalse(result['future_capacity_eligible'])

    def test_multi_task_range_and_decimal_are_not_single_year(self):
        for raw in ('Task 1: 2024; Task 2: 2027', '2024–2027', '2024.0', '0000', True):
            result = year_observation(raw, 'year')
            self.assertIsNone(result['value'])
            self.assertEqual(result['raw_value'], raw)
            self.assertTrue(result['review_required'])
        self.assertFalse(year_observation(None, 'year')['review_required'])

    def test_identity_stable_but_distinct_source_rows_not_merged(self):
        first = self.record()
        self.assertEqual(first['source_record_id'], self.record()['source_record_id'])
        other = normalize_record('Stacje elektroenergetyczne - WPZP', 'test', 2,
                                 first['raw_properties'], 'test.gpkg', 'a' * 64)
        self.assertNotEqual(first['source_record_id'], other['source_record_id'])
        self.assertIsNone(other['canonical_investment_id'])

    def test_links_keep_context_and_are_not_verified(self):
        result = source_links({'description': '(source: https://example.org/a(b)).', 'Link': 'https://example.org/x'})
        self.assertEqual(result[0]['url_candidate'], 'https://example.org/a(b)')
        self.assertEqual(result[0]['source_field'], 'description')
        self.assertTrue(all(r['verification_status'] == 'NOT_VERIFIED' for r in result))

    def test_invalid_url_does_not_crash_or_become_trusted(self):
        self.assertFalse(source_links({'Link': 'http://[invalid'})[0]['syntax_valid'])
        self.assertFalse(source_links({'Link': 'https://user:pass@example.org'})[0]['syntax_valid'])

    def test_missing_required_field_rejected(self):
        with self.assertRaisesRegex(ValueError, 'SCHEMA'):
            normalize_record('Stacje elektroenergetyczne - WPZP', 'test', 1, {}, 'test.gpkg', 'a' * 64)

    def test_pse_export_conflict_and_reverse_years_preserved(self):
        properties = {'Nazwa obiektu': 'Synthetic', 'Nazwa zadania inwestycyjnego': 'Task',
                      'Podstawowy cel realizacji zadania inwestycyjnego': 'Purpose',
                      'Rok rozpoczęcia': '2030', 'Rok zakończenia': '2020'}
        result = normalize_record('STACJE - Realizowane zadania inwestycyjne przez PSE', 'test', 1,
                                  properties, 'test.gpkg', 'a' * 64)
        self.assertIn('START_AFTER_END_SOURCE_VALUES_RETAINED', result['quality_issues'])
        self.assertIn('TASK_PURPOSE_COLUMNS_DIFFER_BETWEEN_GPKG_AND_XLSX_EXPORTS', result['quality_issues'])
        self.assertEqual(result['raw_properties'], properties)
        self.assertEqual(result['description'], 'Task')

    def test_completed_layer_does_not_confirm_current_status_or_gain(self):
        result = normalize_record('Zmodernizowane linie elektroenergetyczne', 'test', 1,
                                  {'Nazwa linii': 'Synthetic', 'Nazwa lub opis zrealizowanego zadania': '2 x 63 MVA'},
                                  'test.gpkg', 'a' * 64)
        self.assertEqual(result['historical_layer_category'], 'COMPLETED_LAYER')
        self.assertEqual(result['current_status'], 'UNKNOWN')
        self.assertFalse(result['primary_source_verified'])
        self.assertIsNone(result['additional_available_capacity_MW'])

    def test_missing_name_preserved_for_review(self):
        result = self.record(Name=None)
        self.assertIn('MISSING_OR_INVALID_NAME', result['quality_issues'])
        self.assertIsNone(result['name'])


if __name__ == '__main__':
    unittest.main()
