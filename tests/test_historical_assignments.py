"""Synthetic integration fixtures only; no invented Radkowice assignments."""
from dataclasses import replace
import json
from pathlib import Path
import unittest

from grid_engine.historical_assignments import historical_inventory
from grid_engine.observation_history import Observation
from grid_engine.shared_connection import Evidence, require_public_result


class HistoricalAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.proof = Evidence('SYNTHETIC', 'synthetic assignment', 'a' * 64,
                              '2026-01-02T00:00:00Z', '2026-01-01', 'PUBLIC', 'DOCUMENT')
        self.item = Observation('o1', 'test-connection', 'position_project:p1', 'PLANNED',
                                'test-project-A', None, 'REPORTED', self.proof,
                                '2026-01-03T00:00:00Z', '2026-01-01', '2026-02-01')

    def query(self, *items, **overrides):
        args = dict(connection_id='test-connection', scenario='PLANNED',
                    known_at='2026-01-20T00:00:00Z', effective_on='2026-01-10')
        return historical_inventory(tuple(items), **(args | overrides))

    def test_counts_never_imply_capacity_or_completeness(self):
        result = self.query(self.item)
        self.assertEqual(result['known_distinct_projects'], 1)
        self.assertEqual(result['known_assigned_positions'], 1)
        self.assertFalse(result['inventory_complete'])
        self.assertIsNone(result['unassigned_positions']['value'])
        self.assertIsNone(result['available_export_MW'])
        require_public_result(result)

    def test_correction_replays_old_and_new_project(self):
        corrected = replace(self.item, observation_id='o2', value='test-project-B',
                            recorded_at='2026-01-15T00:00:00Z', supersedes='o1',
                            correction_reason='Synthetic typo correction')
        old = self.query(self.item, corrected, known_at='2026-01-10T00:00:00Z')
        new = self.query(self.item, corrected)
        self.assertEqual(old['assignments'][0]['project_id'], 'test-project-A')
        self.assertEqual(new['assignments'][0]['project_id'], 'test-project-B')
        self.assertEqual(len(new['evidence']), 2)

    def test_conflict_does_not_arbitrarily_count_either_project(self):
        other = replace(self.item, observation_id='o2', value='test-project-B',
                        evidence=replace(self.proof, source_id='SYNTHETIC_OTHER'))
        result = self.query(self.item, other)
        self.assertEqual(result['known_assigned_positions'], 0)
        self.assertEqual(result['unresolved_position_histories'], 1)
        self.assertEqual(result['position_history'][0]['status'], 'CONFLICT')
        self.assertEqual(len(result['evidence']), 2)

    def test_unknown_validity_and_user_claim_do_not_count(self):
        for item in (replace(self.item, valid_to=None),
                     replace(self.item, evidence=replace(self.proof, origin='USER_PROVIDED')),
                     replace(self.item, value=None, classification='UNKNOWN')):
            with self.subTest(item=item):
                result = self.query(item)
                self.assertEqual(result['known_assigned_positions'], 0)
                self.assertEqual(result['unresolved_position_histories'], 1)

    def test_expired_assignment_is_not_a_free_position(self):
        result = self.query(self.item, effective_on='2026-02-01')
        self.assertEqual(result['known_assigned_positions'], 0)
        self.assertIsNone(result['unassigned_positions']['value'])

    def test_future_position_and_private_source_are_not_visible_early(self):
        future = replace(self.item, observation_id='future', field='position_project:secret',
                         recorded_at='2026-01-25T00:00:00Z',
                         evidence=replace(self.proof, access='PRIVATE'))
        result = self.query(self.item, future)
        self.assertEqual(len(result['position_history']), 1)
        self.assertEqual(result['access'], 'PUBLIC')
        self.assertNotIn('secret', str(result))

    def test_superseded_private_evidence_still_protects_result(self):
        private = replace(self.item, evidence=replace(self.proof, access='PRIVATE'))
        public = replace(self.item, observation_id='o2', recorded_at='2026-01-15T00:00:00Z',
                         supersedes='o1', correction_reason='Synthetic correction')
        result = self.query(private, public)
        self.assertEqual(result['access'], 'PRIVATE')
        with self.assertRaisesRegex(ValueError, 'PUBLIC_EXPORT_NOT_ALLOWED'):
            require_public_result(result)

    def test_station_status_and_other_scopes_never_become_assignments(self):
        for item in (replace(self.item, field='application_status_reported'),
                     replace(self.item, entity_id='other-connection'),
                     replace(self.item, scenario='CURRENT')):
            result = self.query(item)
            self.assertEqual(result['known_assigned_positions'], 0)
            self.assertEqual(result['evidence'], [])

    def test_real_radkowice_status_history_cannot_populate_bridge(self):
        path = Path(__file__).resolve().parents[1] / 'data/reference/radkowice_observation_history_v1.json'
        raw = json.loads(path.read_text(encoding='utf-8'))
        history = tuple(Observation(**{**item, 'evidence': Evidence(**item['evidence'])})
                        for item in raw['observations'])
        result = historical_inventory(history, connection_id='radkowice-shared-connection',
                                      scenario='PLANNED', known_at=raw['recorded_at'],
                                      effective_on='2026-09-15')
        self.assertEqual(result['assignments'], [])
        self.assertIsNone(result['unassigned_positions']['value'])

    def test_same_project_can_have_two_positions(self):
        second = replace(self.item, observation_id='o2', field='position_project:p2')
        result = self.query(self.item, second)
        self.assertEqual(result['known_distinct_projects'], 1)
        self.assertEqual(result['known_assigned_positions'], 2)

    def test_same_value_multiple_sources_counts_once_retains_both(self):
        second = replace(self.item, observation_id='o2', evidence=replace(self.proof, source_id='OTHER'))
        result = self.query(self.item, second)
        self.assertEqual(result['known_assigned_positions'], 1)
        self.assertEqual(len(result['evidence']), 2)

    def test_rejects_units_empty_positions_and_invalid_scenarios(self):
        for item in (replace(self.item, unit='MW'), replace(self.item, field='position_project:')):
            with self.assertRaisesRegex(ValueError, 'INVALID_POSITION_OBSERVATION'):
                self.query(item)
        with self.assertRaisesRegex(ValueError, 'INVALID_SCENARIO'):
            self.query(scenario='invented')
