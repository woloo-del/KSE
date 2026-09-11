import json
from pathlib import Path
import unittest
from unittest.mock import patch

from scripts.build_radkowice_graph import build
from grid_engine.evidence_graph import validate_graph


class WolicaEvidenceTests(unittest.TestCase):
    def test_rebuild_and_preserve_previous_snapshot(self):
        result = build(2)
        saved = json.loads(Path('data/reference/radkowice_evidence_graph_v2.json').read_text(encoding='utf-8'))
        self.assertEqual(result, saved)
        self.assertEqual(len(result['entities']), 13)
        self.assertEqual(len(result['relationships']), 13)
        previous = build(1)
        self.assertEqual(result['entities'][:11], previous['entities'])
        self.assertEqual(result['relationships'][:10], previous['relationships'])

    def test_section_plan_does_not_become_current_line_rating(self):
        result = build(2)
        investment = next(e for e in result['entities'] if e['kind']=='GRID_INVESTMENT_RECORD')
        attrs = investment['attributes']
        self.assertEqual(attrs['planned_parameters']['section_length_m'], 991.8)
        self.assertEqual(attrs['construction_status'], 'UNKNOWN')
        self.assertIsNone(attrs['additional_available_export_MW'])
        line = next(e for e in result['relationships'] if e['id']=='line-radkowice-wolica')
        self.assertIsNone(line['total_line_length_m'])
        self.assertIsNone(line['thermal_capacity_MVA'])
        self.assertEqual(line['evidence'][0]['source_date'], '2024-11-29')
        self.assertFalse(any(e['relation']=='OWNED_BY' for e in result['relationships']))

    def test_changed_source_text_rejected(self):
        from scripts.build_radkowice_graph import add_wolica_evidence
        with patch('scripts.build_radkowice_graph.PdfReader') as reader:
            reader.return_value.pages = []
            with self.assertRaisesRegex(ValueError, 'WOLICA_EVIDENCE_CHANGED'):
                add_wolica_evidence({'entities':[], 'relationships':[]})

    def test_unsupported_voltage_rejected(self):
        graph = build(2)
        next(e for e in graph['relationships'] if e['relation']=='REPORTED_LINE')['voltage_kV']=15
        with self.assertRaisesRegex(ValueError,'UNVERIFIED_VOLTAGE'):
            validate_graph(graph)


if __name__ == '__main__':
    unittest.main()
