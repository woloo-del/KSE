"""Audit the real preserved snapshot; no synthetic grid records are exported."""
import unittest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from scripts.audit_pse_pipeline_statuses import audit


class PseStatusAuditTests(unittest.TestCase):
    def test_changed_snapshot_is_rejected_before_workbook_parse(self):
        with patch('scripts.audit_pse_pipeline_statuses.Path.read_bytes', return_value=b'SYNTHETIC CORRUPT INPUT'), patch('scripts.audit_pse_pipeline_statuses.load_workbook') as loader:
            with self.assertRaisesRegex(ValueError, 'SNAPSHOT_HASH_MISMATCH'):
                audit()
            loader.assert_not_called()

    def test_changed_status_header_rejected_and_workbook_closed(self):
        workbook = MagicMock()
        workbook.__getitem__.return_value = {
            'A1': SimpleNamespace(value='Stan na 31.07.2026'),
            'B4': SimpleNamespace(value='Nazwa Obiektu'),
            'E4': SimpleNamespace(value='Lokalizacja miejsca'),
            'Q4': SimpleNamespace(value='SYNTHETIC CHANGED HEADER'),
        }
        with patch('scripts.audit_pse_pipeline_statuses.load_workbook', return_value=workbook):
            with self.assertRaisesRegex(ValueError, 'HEADER_CHANGED:Q4'):
                audit()
        workbook.close.assert_called_once()

    def test_real_application_stages_and_station_mentions(self):
        result = audit()
        expected = {
            'WARUNKI PRZYŁĄCZENIA wydane': 553,
            'UMOWA O PRZYŁĄCZENIE obowiązująca': 195,
            'WNIOSEK kompletny - w trakcie analizy technicznej i ekonomicznej': 97,
            'ODMOWA PRZYŁĄCZENIA': 29,
            'WNIOSEK w weryfikacji': 17,
            'WNIOSEK niekompletny': 1,
        }
        self.assertEqual({key: value['row_count'] for key, value in result['statuses'].items()}, expected)
        all_rows = [r for group in result['statuses'].values() for r in group['rows']]
        self.assertEqual(len(all_rows), len(set(all_rows)))
        self.assertFalse(set(all_rows) & set(result['nonempty_rows_without_status']))
        self.assertEqual(len(result['nonempty_rows_without_status']), 10)
        self.assertEqual([r['row'] for r in result['radkow_substring_mentions']], [787, 843, 847])
        self.assertTrue(all(r['status_reported'] == 'UMOWA O PRZYŁĄCZENIE obowiązująca' for r in result['radkow_substring_mentions']))
        self.assertTrue(all(r['operator_object_id'] == '-' for r in result['radkow_substring_mentions']))
        self.assertEqual(result['source_date'], '2026-07-31')
