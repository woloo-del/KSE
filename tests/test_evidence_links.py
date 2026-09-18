from copy import deepcopy
import unittest
from backend.local_app import snapshot
from grid_engine.evidence_links import link_records, review_queue


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


class ReviewQueueTests(unittest.TestCase):
    def test_real_groups_preserve_evidence_without_requiring_telemetry(self):
        data = snapshot()
        groups = data['evidence_review_queue']['groups']
        self.assertEqual(sorted(g['evidence_count'] for g in groups), [2, 2, 69])
        self.assertEqual({n for g in groups for n in g['request_ids']}, {'NEED-014', 'NEED-017', 'NEED-018'})
        linked = {r['evidence_id'] for r in data['evidence_links']['links'] if r['status'] == 'SAME_SOURCE_RECORD'}
        self.assertFalse(linked & {e for g in groups for e in g['evidence_ids']})

    def test_missing_request_fails_instead_of_dangling_reference(self):
        data = snapshot()
        with self.assertRaisesRegex(ValueError, 'MISSING_REVIEW_REQUEST'):
            review_queue(data['evidence_links'], [])

    def test_received_document_does_not_resolve_identity(self):
        data = snapshot()
        for r in data['requests']:
            r['status'] = 'Zweryfikowano'
        queue = review_queue(data['evidence_links'], data['requests'])
        self.assertTrue(all(g['review_status'] == 'OPEN' for g in queue['groups']))

    def test_unknown_reason_goes_to_internal_review(self):
        links = {'links': [{'status': 'UNLINKED', 'reason': 'SOURCE_OR_VERSION_CONFLICT', 'evidence_id': 'test'}]}
        original = deepcopy(links)
        group = review_queue(links, [])['groups'][0]
        self.assertEqual(group['request_ids'], [])
        self.assertEqual(group['owner'], 'INTERNAL_DATA_REVIEW')
        self.assertEqual(links, original)
