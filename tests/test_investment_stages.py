import unittest
from connectors.pse.investment_stages import parse_stages

# Synthetic markup used only to validate parser failure modes.
TITLE = 'Rozbudowa i modernizacja stacji 220/110 kV Radkowice – Etap '
HTML = '<h4>'+TITLE+'II (w przygotowaniu)</h4><h4>'+TITLE+'I (w budowie)</h4>'

class StageTests(unittest.TestCase):
    def test_stages_separate_and_no_identity_inference(self):
        rows = parse_stages(HTML)
        self.assertEqual([r['stage'] for r in rows], ['I', 'II'])
        self.assertEqual(rows[0]['status_reported'], 'w budowie')
        self.assertTrue(all(r['operator_task_id'] is None and r['commissioning_date'] is None for r in rows))
    def test_missing_duplicate_and_changed_status_rejected(self):
        for bad in [HTML.split('<h4>')[1], HTML+HTML, HTML.replace('w budowie','nieznany')]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse_stages(bad)
    def test_nested_markup_and_whitespace(self):
        self.assertEqual(parse_stages(HTML.replace('Etap I ', 'Etap <b>I</b>  ')), parse_stages(HTML))
