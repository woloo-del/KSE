import copy
import json
from pathlib import Path
import unittest

from grid_engine.evidence_graph import validate_graph


class EvidenceGraphTests(unittest.TestCase):
    def setUp(self):
        self.graph=json.loads(Path('data/reference/radkowice_evidence_graph_v1.json').read_text(encoding='utf-8'))

    def test_real_graph_keeps_unknowns_and_plans(self):
        validate_graph(self.graph)
        self.assertEqual(len(self.graph['entities']),11)
        planned=[e for e in self.graph['relationships'] if e['relation']=='PLANNED_CONNECTION']
        self.assertEqual(len(planned),3)
        self.assertTrue(all(e['to_id']=='radkowice-level-220' for e in planned))
        station=next(e for e in self.graph['entities'] if e['id']=='radkowice')
        self.assertIsNone(station['attributes']['equipment_ownership'])

    def test_missing_source_rejected(self):
        self.graph['entities'][0]['evidence']=[]
        with self.assertRaisesRegex(ValueError,'MISSING_EVIDENCE'): validate_graph(self.graph)

    def test_user_ownership_claims_remain_separate(self):
        self.assertEqual(self.graph['user_context']['source_type'],'USER_PROVIDED')
        self.assertEqual(len(self.graph['user_context']['claims']),3)
        levels=[e for e in self.graph['entities'] if e['kind']=='VOLTAGE_LEVEL_REFERENCE']
        self.assertTrue(all(e['attributes']['owner_id'] is None for e in levels))
        self.assertFalse(any(e['relation']=='OWNED_BY' for e in self.graph['relationships']))

    def test_dangling_relationship_rejected(self):
        self.graph['relationships'][0]['to_id']='missing-test-entity'
        with self.assertRaisesRegex(ValueError,'DANGLING_ENDPOINT'): validate_graph(self.graph)

    def test_duplicate_identity_rejected(self):
        self.graph['entities'].append(copy.deepcopy(self.graph['entities'][0]))
        with self.assertRaisesRegex(ValueError,'DUPLICATE_ENTITY'): validate_graph(self.graph)

    def test_agreement_cannot_become_physical_connection(self):
        next(e for e in self.graph['relationships'] if e['relation']=='PLANNED_CONNECTION')['physical_connection_confirmed']=True
        with self.assertRaisesRegex(ValueError,'PLANNED_IS_NOT_CONNECTED'): validate_graph(self.graph)

    def test_graph_cannot_become_power_flow_by_flag(self):
        self.graph['power_flow_ready']=True
        with self.assertRaisesRegex(ValueError,'NOT_A_POWER_FLOW_MODEL'): validate_graph(self.graph)

    def test_tariff_date_not_retrieval_date(self):
        edge=next(e for e in self.graph['relationships'] if e['relation']=='TARIFF_RECIPIENT')
        self.assertEqual(edge['evidence'][0]['source_date'],'2025-12-03')
        self.assertTrue(edge['evidence'][0]['retrieval_date'].startswith('2026-09-11'))

    @unittest.skipUnless(Path('data/raw/research/2026-09-11/pse_tariff_2026.pdf').exists(), 'Restore local source PDFs')
    def test_rebuild_matches_saved_graph(self):
        from scripts.build_radkowice_graph import build
        self.assertEqual(build(),self.graph)


if __name__=='__main__': unittest.main()
