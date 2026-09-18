"""Synthetic rows isolate ambiguity; real source verifies pilot equivalence and accounting."""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from types import SimpleNamespace
from connectors.pse.project_pipeline import normalize_row, power, parse, profiles
ROOT=Path(__file__).resolve().parents[1]


def row():
    r=[None]*29
    for i,v in {1:'Synthetic BESS',2:'PSE S.A.',3:'Synthetic SPV',4:'Synthetic station',5:220,6:'NIE',7:'MEE',8:50,9:20,16:'UMOWA O PRZYŁĄCZENIE obowiązująca'}.items():r[i]=v
    return r


class BulkTests(unittest.TestCase):
    def test_import_export_zero_and_missing_remain_distinct(self):
        r=row();r[8]=0;r[9]='-';n=normalize_row(tuple(r),5)
        self.assertEqual(n['export_MW'],'0');self.assertIsNone(n['import_MW'])
        self.assertEqual(power('251,4\xa0'),('251.4',None))

    def test_footnote_and_multivalue_power_not_silently_numeric(self):
        for v in ['232,9E','0A1','129\n240',-1,True,float('inf')]:
            self.assertIsNone(power(v)[0]);self.assertIsNotNone(power(v)[1])

    def test_multiple_points_and_voltage_200_not_assigned(self):
        for field,value in [(4,'A; B'),(4,'A\nB'),(5,200),(5,'220;400'),(6,'TAK'),(16,'unknown')]:
            r=row();r[field]=value;n=normalize_row(tuple(r),5)
            self.assertIsNone(n['profile_id']);self.assertTrue(n['review_reasons'])

    def test_aliases_and_voltage_levels_not_merged(self):
        rows=[]
        for i,(name,voltage) in enumerate([('Skawina',220),('Skwina',220),('Skawina',110)]):
            r=row();r[4]=name;r[5]=voltage;rows.append(normalize_row(tuple(r),i+5))
        result=profiles({'source_date':'2026-07-31','records':rows})
        self.assertEqual(len(result['profiles']),3)
        self.assertTrue(all(p['canonical_station_id'] is None for p in result['profiles']))

    def test_real_snapshot_reconciles_and_preserves_radkowice(self):
        evidence=json.loads((ROOT/'data/reference/pse_scale_benchmark_2026-07-31_v1.json').read_text(encoding='utf-8'))['provenance']
        path=ROOT/evidence['local_path']
        if not path.exists():self.skipTest('Restore source archive for real-snapshot test')
        data=parse(path)
        self.assertEqual(len(data['records'])+len(data['footnotes'])+data['blank_rows'],data['physical_data_rows'])
        self.assertEqual(len(data['records']),892)
        radk=[r for r in data['records'] if r['point_reported']=='Radkowice']
        self.assertEqual([r['row'] for r in radk],[787,843,847])
        self.assertEqual([r['export_MW'] for r in radk],['96.96','50','100'])
        self.assertIsNone(next(r for r in data['records'] if r['row']==116)['profile_id'])
        original=deepcopy(data);result=profiles(data)
        self.assertEqual(data,original)
        self.assertEqual(len(result['profiles']),50)
        self.assertEqual({p['voltage_kV'] for p in result['profiles']},{110,220,400})
        ids=[r for p in result['profiles'] for r in p['record_ids']]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertIsNone(result['metrics']['matching_error_rate'])


class HeaderTests(unittest.TestCase):
    def test_changed_unit_or_date_fails_before_rows(self):
        from connectors.pse.project_pipeline import HEADERS
        for mutation in [{'I4':'Wprowadzana [kW]'}, {'A1':'New layout'}]:
            cells={k:v+' [MW]' for k,v in HEADERS.items()}
            cells['A1']='Stan na 31.07.2026';cells.update(mutation)
            class FakeSheet:
                def __getitem__(self,key):return SimpleNamespace(value=cells[key])
            class FakeBook:
                def __getitem__(self,key):return FakeSheet()
                def close(self):pass
            with patch('connectors.pse.project_pipeline.load_workbook',return_value=FakeBook()):
                with self.assertRaises(ValueError):parse('synthetic')
