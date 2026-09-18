import json
from pathlib import Path
import unittest
from connectors.tauron.project_pipeline import parse_pages,summarize

HEADER='Wprowadzana [MW] Stan na 30.06.2026r.\n'
# Synthetic test-only row; powers deliberately sparse to test no positional guessing.
ROW='1 123 TAURON Dystrybucja S.A. Osoba prawna ABC3 SN NIE MEE 0,0 50,0 UMOWA O PRZYŁĄCZENIE obowiązująca 01.01.2026'

class TauronBulkTests(unittest.TestCase):
    def test_no_guessing_power_or_station_identity(self):
        r=parse_pages([HEADER+ROW])['records'][0]
        self.assertIsNotNone(r['profile_id']);self.assertIsNone(r['canonical_station_id'])
        self.assertIsNone(r['export_MW']);self.assertIsNone(r['import_MW'])
        self.assertEqual(r['point_reported'],'ABC3')

    def test_unknown_point_and_multipoint_not_grouped(self):
        for text in [ROW.replace('ABC3','Stacja obca'),ROW.replace(' SN NIE ', ' SN TAK ')]:
            self.assertIsNone(parse_pages([HEADER+text])['records'][0]['profile_id'])

    def test_duplicate_ids_retained_but_duplicate_ordinals_rejected(self):
        d=parse_pages([HEADER+ROW+'\n'+ROW.replace('1 123','2 123')])
        self.assertEqual(len(d['records']),2)
        self.assertEqual(d['repeated_operator_ids'],1)
        self.assertTrue(all('REPEATED_OPERATOR_OBJECT_ID' in r['review_reasons'] for r in d['records']))
        with self.assertRaises(ValueError):parse_pages([HEADER+ROW+'\n'+ROW])

    def test_header_layout_unknown_status_and_gap_fail(self):
        for text in [ROW,HEADER+ROW.replace('1 123','2 123'),HEADER+ROW.replace('obowiązująca','NOWY STATUS'),HEADER+ROW.replace('Osoba prawna','unexpected')]:
            with self.assertRaises(ValueError):parse_pages([text])

    def test_real_extraction_counts_and_reported_connection(self):
        p=Path('data/staging/research/tauron_text_ce11455a2575454588fef46f711700b476ead67f4cd0b9a829b96e6698bc83b8.json')
        if not p.exists():self.skipTest('Run source extraction benchmark first')
        d=parse_pages(json.loads(p.read_text(encoding='utf-8'))['pages']);s=summarize(d)
        self.assertEqual(s['metrics']['source_records'],10955)
        self.assertEqual(s['metrics']['status_counts']['UMOWA O PRZYŁĄCZENIE - obiekt przyłączony'],342)
        self.assertEqual(d['records'][0]['point_reported'],'SKB3')
        self.assertEqual(d['records'][0]['page'],1)
        self.assertEqual(d['records'][-1]['page'],98)
        self.assertEqual(d['records'][-1]['row_number'],10955)
        self.assertEqual(len(s['sample_profiles']),50)

