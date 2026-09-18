"""Local pilot API contract and conservative assessment behavior."""
import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

from backend.local_app import Handler, snapshot
from grid_engine.screening_opinion import assess


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.pipeline = snapshot()['pipeline']

    def test_bess_directions_remain_independent_without_available_capacity(self):
        result = assess({'technology':'BESS','voltage_kV':220,'export_MW':'50','import_MW':'20','energy_MWh':'200'}, self.pipeline)
        self.assertEqual([d['requested_MW'] for d in result['directions']], ['50','20'])
        self.assertTrue(all(d['available_MW'] is None for d in result['directions']))
        self.assertIsNone(result['score'])
        self.assertIsNone(result['probability'])
        self.assertTrue(all(f['basis'] for f in result['findings']))

    def test_110_case_does_not_use_220_agreements_as_positive_evidence(self):
        result = assess({'technology':'PV+BESS','voltage_kV':110,'export_MW':'30'}, self.pipeline)
        ids = {f['id'] for f in result['findings']}
        self.assertIn('NO_110_PIPELINE', ids)
        self.assertNotIn('DOCUMENTED_AGREEMENTS', ids)
        self.assertEqual(result['project']['export_MW'], '30')

    def test_unknown_and_zero_are_distinct(self):
        result = assess({'technology':'BESS','voltage_kV':220,'import_MW':'0'}, self.pipeline)
        self.assertIsNone(result['directions'][0]['requested_MW'])
        self.assertEqual(result['directions'][1]['requested_MW'],'0')
        self.assertNotEqual(result['directions'][0]['conclusion'],result['directions'][1]['conclusion'])

    def test_invalid_user_values_rejected(self):
        for value in ['-1','NaN','Infinity',True,'abc']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                assess({'technology':'BESS','voltage_kV':220,'export_MW':value}, self.pipeline)
        with self.assertRaises(ValueError):
            assess({'technology':'BESS','voltage_kV':220,'source_override':{}}, self.pipeline)


class LocalApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def test_public_data_and_assets_are_available(self):
        with urlopen(self.url+'/api/station') as response:
            data = json.load(response)
        self.assertEqual(len(data['pipeline']['records']),3)
        self.assertEqual(len(data['graph']['entities']),13)
        self.assertEqual(data['evidence_links']['status_counts'], {'SAME_SOURCE_RECORD': 3, 'UNLINKED': 73})
        self.assertIn('NEED-011',{r['id'] for r in data['requests']})
        for route in ['/', '/app.js','/style.css']:
            with urlopen(self.url+route) as response:
                self.assertEqual(response.status,200)
                self.assertIn("default-src 'self'",response.headers['Content-Security-Policy'])

    def test_arbitrary_repository_and_private_paths_are_not_served(self):
        for route in ['/_secrets/key.txt','/data/private/test.pdf','/README.md','/../AGENTS.md','/api/unknown']:
            with self.subTest(route=route), self.assertRaises(HTTPError) as result:
                urlopen(self.url+route)
            self.assertEqual(result.exception.code,404)

    def test_post_assessment_records_method_and_input_versions(self):
        request = Request(self.url+'/api/assessment', data=json.dumps({'technology':'BESS','voltage_kV':220,'export_MW':'50','import_MW':'50'}).encode(),headers={'Content-Type':'application/json'})
        with urlopen(request) as response:
            result=json.load(response)
        self.assertEqual(result['method'],'documentary_screening_v2')
        self.assertEqual(len(result['method_code_sha256']),64)
        self.assertEqual(len(result['input_sha256']),7)
        ledger = result['evidence_snapshot']['aggregated_evidence']
        self.assertEqual(ledger['source_record_count'], 76)
        self.assertIsNone(ledger['unique_project_count'])
        self.assertEqual(len(ledger['input_sha256']), 4)
        self.assertTrue(any(f['id']=='INVESTMENT_DATE_OR_SCOPE_UNRESOLVED' for f in result['findings']))
        self.assertIsNone(result['evidence_snapshot']['investment_review']['selected_completion_year'])
        self.assertEqual(result['input_sha256'], result['evidence_snapshot']['input_sha256'])
        self.assertEqual(len(result['evidence_snapshot']['pipeline']['records']),3)
        plan = result['evidence_snapshot']['development_plan']
        self.assertEqual(len(plan['records']), 2)
        self.assertEqual(plan['document_status'], 'POST_CONSULTATION_DRAFT')
        self.assertTrue(all(r['additional_available_capacity_MW'] is None for r in plan['records']))
        self.assertIn('evaluated_at',result)

    def test_bad_payload_is_a_readable_error(self):
        request = Request(self.url+'/api/assessment',data=b'{',headers={'Content-Type':'application/json'})
        with self.assertRaises(HTTPError) as result:
            urlopen(request)
        self.assertEqual(result.exception.code,400)
        self.assertNotIn('Traceback',result.exception.read().decode())
