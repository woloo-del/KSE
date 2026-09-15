"""Synthetic assertions only; no fictitious records are added to the pilot data."""
from dataclasses import replace
import hashlib
import unittest

from grid_engine.observation_history import Observation, append_observation, as_known
from grid_engine.shared_connection import Evidence, require_public_result


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.proof=Evidence('SYNTHETIC_SOURCE','synthetic fixture',
            hashlib.sha256(b'SYNTHETIC HISTORY ONLY').hexdigest(),
            '2026-01-05T10:00:00Z','2026-01-01','PUBLIC','DOCUMENT')
        self.item=Observation('o1','test-project','application_status','CURRENT',
            'connection_conditions',None,'REPORTED',self.proof,'2026-01-05T11:00:00Z',
            '2026-01-01','2026-02-01')

    def query(self, history, **kwargs):
        return as_known(history,entity_id='test-project',field='application_status',
            scenario='CURRENT',unit=None,known_at=kwargs.get('known_at','2026-01-20T00:00:00Z'),
            effective_on=kwargs.get('effective_on','2026-01-10'))

    def correction(self, **kwargs):
        return replace(self.item,observation_id='o2',value='connection_agreement',
            recorded_at='2026-01-15T10:00:00Z',supersedes='o1',correction_reason='Synthetic correction',**kwargs)

    def test_append_preserves_original_history(self):
        original=(self.item,)
        updated=append_observation(original,self.correction())
        self.assertEqual(len(original),1)
        self.assertEqual(len(updated),2)
        self.assertEqual(original[0].value,'connection_conditions')

    def test_retrospective_correction_changes_knowledge_not_old_view(self):
        history=append_observation((self.item,),self.correction())
        self.assertEqual(self.query(history,known_at='2026-01-10T00:00:00Z')['value'],'connection_conditions')
        self.assertEqual(self.query(history)['value'],'connection_agreement')
        self.assertEqual(len(self.query(history)['visible_history']),2)

    def test_later_document_is_not_known_before_ingestion(self):
        result=self.query((self.item,),known_at='2026-01-04T00:00:00Z')
        self.assertEqual(result['status'],'UNKNOWN')
        self.assertEqual(result['visible_history'],[])

    def test_valid_to_is_exclusive(self):
        self.assertEqual(self.query((self.item,),effective_on='2026-01-31')['status'],'REPORTED')
        self.assertEqual(self.query((self.item,),effective_on='2026-02-01')['status'],'UNKNOWN')

    def test_unknown_end_is_not_automatically_open_ended(self):
        unknown=replace(self.item,valid_to=None)
        self.assertEqual(self.query((unknown,))['status'],'UNKNOWN')
        explicit=replace(unknown,explicitly_open_ended=True)
        self.assertEqual(self.query((explicit,))['status'],'REPORTED')

    def test_future_start_does_not_contaminate_past_view(self):
        future=replace(self.item,observation_id='o2',valid_from='2027-01-01',valid_to=None)
        self.assertEqual(self.query((self.item,future))['status'],'REPORTED')

    def test_independent_conflicting_sources_remain_visible(self):
        other=replace(self.item,observation_id='o2',value='cancelled',
                      evidence=replace(self.proof,source_id='SYNTHETIC_OTHER'))
        result=self.query((self.item,other))
        self.assertEqual(result['status'],'CONFLICT')
        self.assertIsNone(result['value'])
        self.assertEqual(len(result['active']),2)

    def test_same_value_does_not_duplicate_selected_value(self):
        other=replace(self.item,observation_id='o2',evidence=replace(self.proof,source_id='SYNTHETIC_OTHER'))
        result=self.query((self.item,other))
        self.assertEqual(result['status'],'REPORTED')
        self.assertEqual(len(result['evidence']),2)

    def test_explicit_unknown_and_unknown_validity_are_not_silently_discarded(self):
        for other in [replace(self.item,observation_id='o2',value=None,classification='UNKNOWN'),
                      replace(self.item,observation_id='o2',valid_from=None,valid_to=None)]:
            self.assertEqual(self.query((self.item,other))['status'],'UNKNOWN')

    def test_reject_duplicate_identity_and_backdated_append(self):
        with self.assertRaisesRegex(ValueError,'DUPLICATE_OBSERVATION_ID'):
            append_observation((self.item,),self.item)
        old=replace(self.item,observation_id='o2',recorded_at='2026-01-05T10:30:00Z')
        with self.assertRaisesRegex(ValueError,'KNOWLEDGE_TIME_ORDER'):
            append_observation((self.item,),old)

    def test_correction_cannot_replace_different_entity_or_source(self):
        for other in [self.correction(entity_id='other'),
                      self.correction(evidence=replace(self.proof,source_id='SYNTHETIC_OTHER'))]:
            with self.assertRaisesRegex(ValueError,'CORRECTION_SCOPE_MISMATCH'):
                append_observation((self.item,),other)

    def test_correction_requires_prior_target_and_reason(self):
        with self.assertRaisesRegex(ValueError,'MISSING_CORRECTION_TARGET'):
            append_observation((),self.correction())
        with self.assertRaisesRegex(ValueError,'MISSING_CORRECTION_REASON'):
            append_observation((self.item,),replace(self.correction(),correction_reason=None))

    def test_correction_chain_is_linear(self):
        history=append_observation((self.item,),self.correction())
        branch=replace(self.correction(),observation_id='o3',recorded_at='2026-01-16T10:00:00Z')
        with self.assertRaisesRegex(ValueError,'BRANCHED_CORRECTION'):
            append_observation(history,branch)
        chain=replace(branch,supersedes='o2',value='cancelled')
        self.assertEqual(self.query(append_observation(history,chain))['value'],'cancelled')

    def test_private_correction_does_not_leak_into_public_export(self):
        correction=self.correction(evidence=replace(self.proof,access='PRIVATE'))
        history=append_observation((self.item,),correction)
        before=self.query(history,known_at='2026-01-10T00:00:00Z')
        require_public_result(before)
        with self.assertRaisesRegex(ValueError,'PUBLIC_EXPORT_NOT_ALLOWED'):
            require_public_result(self.query(history))

    def test_units_and_scenarios_are_separate(self):
        other=replace(self.item,observation_id='o2',value='cancelled',scenario='PLANNED')
        unit=replace(self.item,observation_id='o3',value='12',unit='MW')
        self.assertEqual(len(self.query((self.item,other,unit))['active']),1)

    def test_invalid_time_and_value_contracts_rejected(self):
        cases=[(replace(self.item,recorded_at='2026-01-05T11:00:00'),'TIMEZONE_REQUIRED'),
               (replace(self.item,recorded_at='2026-01-04T11:00:00Z'),'RECORDED_BEFORE_RETRIEVAL'),
               (replace(self.item,valid_to='2025-12-01'),'INVALID_VALIDITY_INTERVAL'),
               (replace(self.item,value=None),'INVALID_OBSERVATION_VALUE'),
               (replace(self.item,classification='ESTIMATED'),'UNSUPPORTED_CLASSIFICATION')]
        for item, error in cases:
            with self.assertRaisesRegex(ValueError,error): append_observation((),item)


if __name__=='__main__': unittest.main()
