import unittest
from connectors.pse.mention_context import contexts, annotate
from scripts.build_pse_mention_context import build


class ContextTests(unittest.TestCase):
    def test_station_voltage_is_local_not_line_voltage(self):
        title = 'Rozbudowa stacji 220/110 kV Test wraz z linią 400 kV Other'
        row = contexts(title, 'Test', 400)[0]
        self.assertEqual(row['context_kind'], 'EXPLICIT_STATION_LABEL')
        self.assertEqual(row['station_label_voltage_kV'], [220, 110])
        self.assertEqual(row['profile_voltage_comparison'], 'NOT_LISTED')

    def test_unknown_voltage_and_complex_notation_not_guessed(self):
        for title in ['Dostosowanie stacji Test do pracy na napięciu 400 kV',
                      'Budowa stacji 400(220)/110 kV Test']:
            row = contexts(title, 'Test', 110)[0]
            self.assertEqual(row['profile_voltage_comparison'], 'UNKNOWN')

    def test_farm_line_and_longer_name_are_not_station_identity(self):
        for title in ['Linia 400 kV Test-Other', 'Budowa stacji 400 kV Test Systemowa',
                      'Budowa stacji 400 kV Test Nowy']:
            self.assertEqual(contexts(title, 'Test', 400)[0]['context_kind'], 'OTHER_OR_UNRESOLVED_MENTION')
        self.assertEqual(contexts('Przyłączenie FW Test', 'Test', 110)[0]['context_kind'], 'EXPLICIT_FARM_LABEL')

    def test_each_occurrence_and_offsets_are_preserved(self):
        title = 'Budowa stacji 110 kV Test wraz z przyłączeniem FW Test'
        rows = contexts(title, 'Test', 110)
        self.assertEqual([r['context_kind'] for r in rows], ['EXPLICIT_STATION_LABEL', 'EXPLICIT_FARM_LABEL'])
        for r in rows:
            self.assertEqual(title[r['start']:r['end']], r['matched_text'])

    def test_broken_references_fail(self):
        with self.assertRaisesRegex(ValueError, 'MISSING_HEADING'):
            annotate({'headings': [], 'profiles': [{'heading_ids': ['missing']}]})

    def test_real_results_never_promote_identity(self):
        result = build()
        self.assertGreater(result['metrics']['profiles_with_explicit_station_label'], 0)
        for r in result['records']:
            self.assertIsNone(r['canonical_station_id'])
            self.assertIsNone(r['current_station_voltage_kV'])
            self.assertTrue(r['review_required'])


if __name__ == '__main__':
    unittest.main()
