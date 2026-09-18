from copy import deepcopy
import unittest
from backend.local_app import snapshot
from grid_engine.evidence_links import link_records


class EvidenceLinkTests(unittest.TestCase):
    def setUp(self):
        data = snapshot()
        self.ledger, self.graph = data['aggregated_evidence'], data['graph']

    def test_same_rows_link_but_not_independent_confirmation(self):
        r = link_records(self.ledger, self.graph)
        self.assertEqual(r['status_counts'], {'UNLINKED': 73, 'SAME_SOURCE_RECORD': 3})
        self.assertTrue(all(not x['cross_source_identity_confirmed'] and not x['physical_connection_confirmed'] for x in r['links']))

    def test_same_name_is_not_identity(self):
        for e in self.graph['entities']:
            if e['kind'] == 'PROJECT_RECORD':
                previous = e['id']
                e['id'] += '-other'
                for edge in self.graph['relationships']:
                    if edge['from_id'] == previous:
                        edge['from_id'] = e['id']
        self.assertEqual(link_records(self.ledger, self.graph)['status_counts'], {'UNLINKED': 76})

    def test_same_id_but_different_snapshot_not_linked(self):
        project = next(r for r in self.ledger['records'] if r['record_kind'] == 'PROJECT_PUBLICATION')
        project['provenance']['snapshot_sha256'] = '0' * 64
        r = link_records(self.ledger, self.graph)
        self.assertEqual(r['status_counts']['SAME_SOURCE_RECORD'], 2)
        self.assertIn('SOURCE_OR_VERSION_CONFLICT', [x['reason'] for x in r['links']])

    def test_inputs_unchanged_and_duplicate_rejected(self):
        original = deepcopy(self.ledger)
        link_records(self.ledger, self.graph)
        self.assertEqual(original, self.ledger)
        self.ledger['records'].append(deepcopy(self.ledger['records'][0]))
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_EVIDENCE_ID'):
            link_records(self.ledger, self.graph)
