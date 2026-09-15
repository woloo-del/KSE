"""Synthetic parameter history only; not technical evidence for Radkowice."""
from dataclasses import asdict, replace
import json
from pathlib import Path
import tempfile
import unittest

from grid_engine.historical_connection_parameters import historical_inventory_v2
from grid_engine.observation_history import Observation
from grid_engine.shared_connection import Evidence, require_public_result
from scripts.analyze_historical_assignments import analyze_file


class ParameterHistoryTests(unittest.TestCase):
    def setUp(self):
        self.proof = Evidence('SYNTHETIC', 'test fixture', 'a'*64,
                              '2026-01-02T00:00:00Z', '2026-01-01', 'PUBLIC', 'DOCUMENT')
        self.template = Observation('o', 'test-connection', 'maximum_positions', 'PLANNED',
                                    '4', 'position', 'REPORTED', self.proof,
                                    '2026-01-03T00:00:00Z', '2026-01-01', '2026-02-01')

    def item(self, field, value, unit=None, **kwargs):
        return replace(self.template, observation_id=field, field=field, value=value, unit=unit, **kwargs)

    def query(self, *items, **kwargs):
        params = dict(connection_id='test-connection', scenario='PLANNED',
                      known_at='2026-01-10T00:00:00Z', effective_on='2026-01-05')
        return historical_inventory_v2(tuple(items), **(params | kwargs))

    def complete(self):
        return [self.template, self.item('inventory_complete', 'true'),
                self.item('position_project:p1', 'project-A')]

    def test_explicit_dated_coverage_allows_positions_never_mw(self):
        result = self.query(*self.complete(), self.item('export_limit_MW', '12.34567890123456789', 'MW'),
                            self.item('import_limit_MW', '0', 'MW'))
        self.assertEqual(result['unassigned_positions']['value'], 3)
        self.assertEqual(result['reported_export_limit']['value'], '12.34567890123456789')
        self.assertEqual(result['reported_import_limit']['value'], '0')
        self.assertIsNone(result['available_export_MW'])
        self.assertIsNone(result['available_import_MW'])

    def test_missing_false_unknown_or_undated_coverage_never_implies_complete(self):
        candidates = [None, self.item('inventory_complete', 'false'),
                      self.item('inventory_complete', None, classification='UNKNOWN'),
                      self.item('inventory_complete', 'true', valid_to=None)]
        for coverage in candidates:
            with self.subTest(coverage=coverage):
                result = self.query(self.template, *([coverage] if coverage else []))
                self.assertFalse(result['inventory_complete'])
                self.assertIsNone(result['unassigned_positions']['value'])

    def test_conflicting_coverage_and_maximum_are_not_selected(self):
        for field, value, unit, contrary in [('maximum_positions', '4', 'position', '6'),
                                            ('inventory_complete', 'true', None, 'false')]:
            first = self.item(field, value, unit)
            other = replace(first, observation_id='other', value=contrary,
                            evidence=replace(self.proof, source_id='OTHER'))
            result = self.query(first, other)
            self.assertEqual(result['parameter_history'][field]['status'], 'CONFLICT')
            self.assertIsNone(result['unassigned_positions']['value'])

    def test_complete_claim_cannot_override_position_conflict(self):
        items = self.complete()
        items.append(replace(items[-1], observation_id='conflict', value='project-B',
                             evidence=replace(self.proof, source_id='OTHER')))
        result = self.query(*items)
        self.assertTrue(result['inventory_complete'])  # source claim retained
        self.assertIsNone(result['unassigned_positions']['value'])
        self.assertIn('UNRESOLVED_POSITION_HISTORIES', result['unassigned_positions']['reasons'])

    def test_expired_position_still_prevents_free_position_inference(self):
        items = self.complete()
        items[-1] = replace(items[-1], valid_to='2026-01-04')
        self.assertIsNone(self.query(*items)['unassigned_positions']['value'])

    def test_parameter_correction_preserves_old_knowledge(self):
        corrected = replace(self.template, observation_id='new', value='6', supersedes='o',
                            correction_reason='Synthetic correction', recorded_at='2026-01-15T00:00:00Z')
        self.assertEqual(self.query(self.template, corrected)['maximum_positions'], 4)
        later = self.query(self.template, corrected, known_at='2026-01-20T00:00:00Z')
        self.assertEqual(later['maximum_positions'], 6)
        self.assertEqual(len(later['evidence']), 2)

    def test_future_and_other_scenario_parameters_are_not_borrowed(self):
        for item in [replace(self.template, scenario='CURRENT'),
                     replace(self.template, valid_from='2026-01-20'),
                     replace(self.template, recorded_at='2026-01-20T00:00:00Z')]:
            self.assertIsNone(self.query(item)['maximum_positions'])

    def test_user_claim_and_private_conflict_preserve_provenance(self):
        user = replace(self.template, evidence=replace(self.proof, origin='USER_PROVIDED'))
        self.assertIsNone(self.query(user)['maximum_positions'])
        private = replace(self.template, observation_id='private', value='6',
                          evidence=replace(self.proof, source_id='OTHER', access='PRIVATE'))
        result = self.query(self.template, private)
        self.assertEqual(result['access'], 'PRIVATE')
        with self.assertRaisesRegex(ValueError, 'PUBLIC_EXPORT_NOT_ALLOWED'):
            require_public_result(result)

    def test_invalid_units_numbers_and_coverage_rejected(self):
        bad = [self.item('maximum_positions', '4', 'MW'), self.item('maximum_positions', '4.0', 'position'),
               self.item('maximum_positions', '-1', 'position'), self.item('inventory_complete', 'yes'),
               self.item('export_limit_MW', 'NaN', 'MW'), self.item('import_limit_MW', '-1', 'MW')]
        for item in bad:
            with self.subTest(item=item), self.assertRaises(ValueError):
                self.query(item)

    def test_assignments_exceeding_documented_maximum_fail_validation(self):
        with self.assertRaisesRegex(ValueError, 'ASSIGNMENTS_EXCEED_POSITION_COUNT'):
            self.query(replace(self.template, value='0'), self.item('position_project:p1', 'project-A'))

    def test_explicit_zero_complete_empty_inventory_is_distinct_from_unknown(self):
        result = self.query(replace(self.template, value='0'), self.item('inventory_complete', 'true'))
        self.assertEqual(result['unassigned_positions']['value'], 0)

    def test_runner_preserves_v1_and_requires_v2_opt_in(self):
        request = {'schema_version': 'historical_assignments_request_v1',
                   'query': dict(connection_id='test-connection', scenario='PLANNED',
                                 known_at='2026-01-10T00:00:00Z', effective_on='2026-01-05'),
                   'observations': [asdict(i) for i in self.complete()]}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'
            source.write_text(json.dumps(request), encoding='utf-8')
            old = analyze_file(source, root/'v1.json', root/'private')
            request['schema_version'] = 'historical_connection_request_v2'
            source.write_text(json.dumps(request), encoding='utf-8')
            new = analyze_file(source, root/'v2.json', root/'private')
            self.assertEqual(old['method'], 'historical_shared_assignments_v1')
            self.assertIsNone(old['maximum_positions'])
            self.assertEqual(new['method'], 'historical_shared_connection_v2')
            self.assertEqual(new['unassigned_positions']['value'], 3)
            self.assertIn('grid_engine/historical_connection_parameters.py', new['reproducibility']['code_sha256'])
