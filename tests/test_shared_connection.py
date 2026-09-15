"""Synthetic fixtures only. These counts and powers describe no real grid asset."""
from dataclasses import replace
from decimal import Decimal
import hashlib
import unittest

from grid_engine.shared_connection import (
    Assignment, Evidence, SharedConnectionSnapshot, require_public_result, summarize,
)


class SharedConnectionTests(unittest.TestCase):
    def setUp(self):
        self.proof = Evidence('SYNTHETIC_SOURCE', 'synthetic fixture',
            hashlib.sha256(b'SYNTHETIC FIXTURE ONLY').hexdigest(),
            '2026-09-11T00:00:00Z','2026-09-10','PUBLIC','DOCUMENT')
        self.base = SharedConnectionSnapshot('SYNTHETIC_SNAPSHOT','SYNTHETIC_BRIDGE',
            '2026-09-11','PLANNED',4,self.proof)

    def assignment(self, position='slot-1', project='test-project', **changes):
        return replace(Assignment(project,position,self.base.connection_id,
                                  'PLANNED',True,self.proof), **changes)

    def complete(self, **changes):
        return replace(self.base, inventory_complete=True, coverage_evidence=self.proof, **changes)

    def test_empty_partial_inventory_is_not_four_free_positions(self):
        result=summarize(self.base)
        self.assertEqual(result['known_assigned_positions'],0)
        self.assertIsNone(result['unassigned_positions']['value'])
        self.assertIn('INVENTORY_INCOMPLETE',result['unassigned_positions']['reasons'])

    def test_complete_inventory_calculates_positions_but_never_mw(self):
        result=summarize(self.complete(assignments=(self.assignment(),)))
        self.assertEqual(result['unassigned_positions']['value'],3)
        self.assertEqual(result['unassigned_positions']['classification'],'CALCULATED')
        self.assertIsNone(result['available_export_MW'])
        self.assertIsNone(result['available_import_MW'])
        self.assertFalse(result['power_flow_ready'])

    def test_completeness_needs_evidence(self):
        with self.assertRaisesRegex(ValueError,'MISSING_COVERAGE_EVIDENCE'):
            summarize(replace(self.base,inventory_complete=True))

    def test_unknown_capacity_and_zero_are_different(self):
        unknown=summarize(self.complete(maximum_positions=None,position_evidence=None))
        zero=summarize(self.complete(maximum_positions=0))
        self.assertIsNone(unknown['unassigned_positions']['value'])
        self.assertEqual(zero['unassigned_positions']['value'],0)

    def test_probable_and_unlocated_assignments_prevent_availability(self):
        for a in [self.assignment(confirmed=False),self.assignment(position=None)]:
            result=summarize(self.complete(assignments=(a,)))
            self.assertEqual(result['unresolved_assignment_records'],1)
            self.assertIsNone(result['unassigned_positions']['value'])
            self.assertEqual(result['known_distinct_projects'],1 if a.confirmed else 0)

    def test_duplicate_or_conflicting_position_is_not_silently_deduplicated(self):
        for second in [self.assignment(),self.assignment(project='different-test-project')]:
            with self.assertRaisesRegex(ValueError,'DUPLICATE_OR_CONFLICTING_POSITION'):
                summarize(replace(self.base,assignments=(self.assignment(),second)))

    def test_projects_and_positions_are_separate_counts(self):
        result=summarize(self.complete(assignments=(self.assignment(),self.assignment(position='slot-2'))))
        self.assertEqual(result['known_assigned_positions'],2)
        self.assertEqual(result['known_distinct_projects'],1)

    def test_reported_directional_limits_preserve_zero_and_unknown(self):
        result=summarize(replace(self.base,export_limit_MW=Decimal('0'),export_evidence=self.proof))
        self.assertEqual(result['reported_export_limit']['value'],'0')
        self.assertIsNone(result['reported_import_limit']['value'])
        self.assertIsNone(result['available_export_MW'])

    def test_invalid_numbers_and_missing_limit_evidence_rejected(self):
        for value in [Decimal('-1'),Decimal('NaN'),Decimal('Infinity'),50.0]:
            with self.assertRaisesRegex(ValueError,'INVALID_MW_LIMIT'):
                summarize(replace(self.base,export_limit_MW=value,export_evidence=self.proof))
        with self.assertRaisesRegex(ValueError,'MISSING_LIMIT_EVIDENCE'):
            summarize(replace(self.base,export_limit_MW=Decimal('12')))
        for count in [-1,True,2.5]:
            with self.assertRaisesRegex(ValueError,'INVALID_POSITION_COUNT'):
                summarize(replace(self.base,maximum_positions=count))

    def test_excess_assignments_rejected(self):
        with self.assertRaisesRegex(ValueError,'ASSIGNMENTS_EXCEED_POSITION_COUNT'):
            summarize(replace(self.base,maximum_positions=0,assignments=(self.assignment(),)))

    def test_station_or_different_scenario_cannot_be_used_as_bridge_assignment(self):
        for a in [self.assignment(connection_id='SYNTHETIC_STATION'),self.assignment(scenario='CURRENT')]:
            with self.assertRaisesRegex(ValueError,'ASSIGNMENT_SCOPE_MISMATCH'):
                summarize(replace(self.base,assignments=(a,)))

    def test_private_unresolved_input_taints_entire_result(self):
        private=replace(self.proof,access='PRIVATE',origin='USER_PROVIDED')
        result=summarize(replace(self.base,assignments=(self.assignment(confirmed=False,evidence=private),)))
        self.assertEqual(result['access'],'PRIVATE')
        with self.assertRaisesRegex(ValueError,'PUBLIC_EXPORT_NOT_ALLOWED'):
            require_public_result(result)
        result['access']='PUBLIC'
        with self.assertRaisesRegex(ValueError,'PUBLIC_EXPORT_NOT_ALLOWED'):
            require_public_result(result)

    def test_public_result_preserves_provenance(self):
        result=summarize(self.base)
        require_public_result(result)
        self.assertEqual(result['evidence'][0]['snapshot_sha256'],self.proof.snapshot_sha256)
        self.assertEqual(result['as_of'],'2026-09-11')

    def test_invalid_provenance_rejected(self):
        with self.assertRaisesRegex(ValueError,'INVALID_SNAPSHOT_HASH'):
            summarize(replace(self.base,position_evidence=replace(self.proof,snapshot_sha256='bad')))

    def test_provenance_dates_are_not_silently_reinterpreted(self):
        for proof, error in [
            (replace(self.proof,retrieval_date='2026-09-11T00:00:00'),'RETRIEVAL_TIMEZONE_REQUIRED'),
            (replace(self.proof,source_date='2026-09-12'),'SOURCE_DATE_AFTER_RETRIEVAL')]:
            with self.assertRaisesRegex(ValueError,error):
                summarize(replace(self.base,position_evidence=proof))


if __name__=='__main__':
    unittest.main()
