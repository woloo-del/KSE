"""Real snapshot expectations and explicitly synthetic edge-case mutations."""
import copy
import json
from pathlib import Path
import unittest
from scripts.build_radkowice_pipeline import build_view


class PipelineViewTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads(Path('data/reference/radkowice_pse_projects_2026-07-31.json').read_text(encoding='utf-8'))

    def test_actual_agreements_are_planned_rows_with_directional_sums(self):
        result = build_view(self.sample)
        group = result['groups']['B_PLANNED']
        self.assertEqual(group['known_source_row_count'], 3)
        self.assertEqual(group['powers']['export']['known_row_sum_MW'], '246.96')
        self.assertEqual(group['powers']['import']['known_row_sum_MW'], '250.8992')
        self.assertIsNone(group['station_project_count'])
        for name in ['A_CONNECTED', 'C_AWAITING_RESPONSE']:
            self.assertEqual(result['groups'][name]['known_source_row_count'], 0)
            self.assertIsNone(result['groups'][name]['powers']['export']['known_row_sum_MW'])
        self.assertTrue(all(row['bridge_assignment'] is None for row in result['records']))

    def test_synthetic_unknown_status_and_past_date_do_not_imply_connection(self):
        self.sample['records'][0]['status_reported'] = 'SYNTHETIC UNRECOGNIZED STATUS'
        self.sample['records'][0]['delivery_start_date_reported'] = '2020-01-01'
        result = build_view(self.sample)
        self.assertEqual(result['records'][0]['group'], 'UNKNOWN')
        self.assertEqual(result['groups']['C_AWAITING_RESPONSE']['known_source_row_count'], 0)

    def test_synthetic_missing_power_is_not_zero(self):
        self.sample['records'] = self.sample['records'][:1]
        self.sample['records'][0]['connection_export_MW'] = None
        self.sample['records'][0]['connection_import_MW'] = 0
        powers = build_view(self.sample)['groups']['B_PLANNED']['powers']
        self.assertIsNone(powers['export']['known_row_sum_MW'])
        self.assertEqual(powers['export']['missing_power_rows'], 1)
        self.assertEqual(powers['import']['known_row_sum_MW'], '0')

    def test_synthetic_invalid_inputs_rejected(self):
        for field, value in [('source_date', '2026-08-31'), ('source_url', ''),
                             ('connection_export_MW', -1), ('connection_import_MW', float('nan')),
                             ('connection_export_MW', True)]:
            sample = copy.deepcopy(self.sample)
            sample['records'][0][field] = value
            with self.assertRaises(ValueError):
                build_view(sample)
        self.sample['records'].append(copy.deepcopy(self.sample['records'][0]))
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_SOURCE_RECORD'):
            build_view(self.sample)
