"""Aggregation must preserve evidence without inferring assets, status or capacity."""
from copy import deepcopy
import json
import unittest
from scripts.build_station_evidence import INPUTS, ROOT, build
from grid_engine.station_evidence import aggregate, encode


class StationEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.inputs = {key: json.loads((ROOT / name).read_bytes()) for key, name in INPUTS.items()}

    def test_replay_is_deterministic_and_retains_all_record_families(self):
        a = build()
        self.assertEqual(encode(a), encode(build()))
        self.assertEqual(a['record_counts'], {'PROJECT_PUBLICATION': 3, 'GRID_INVESTMENT_PUBLICATION': 2,
                                            'OSM_SPATIAL_RECORD': 69, 'INVESTMENT_DATE_CLAIM': 2})
        self.assertIsNone(a['unique_project_count'])
        self.assertEqual(len(a['input_sha256']), 4)

    def test_duplicate_source_record_fails_instead_of_inflating_count(self):
        self.inputs['pipeline']['records'].append(deepcopy(self.inputs['pipeline']['records'][0]))
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_SOURCE_RECORD'):
            aggregate(**self.inputs)

    def test_missing_provenance_and_wrong_station_fail(self):
        self.inputs['pipeline']['records'][0]['snapshot_sha256'] = None
        with self.assertRaisesRegex(ValueError, 'MISSING_PROVENANCE'):
            aggregate(**self.inputs)
        self.inputs['pipeline']['station'] = 'Other'
        with self.assertRaisesRegex(ValueError, 'UNSUPPORTED_STATION'):
            aggregate(**self.inputs)

    def test_spatial_records_and_date_conflict_are_not_promoted(self):
        result = aggregate(**self.inputs)
        self.assertEqual(result['unresolved_review']['status'], 'UNRESOLVED_DATE_OR_SCOPE')
        self.assertIsNone(result['unresolved_review']['selected_completion_year'])
        osm = [r for r in result['records'] if r['record_kind'] == 'OSM_SPATIAL_RECORD']
        self.assertTrue(all(r['station_association'] == 'CALCULATED_SPATIAL_ASSOCIATION_ONLY' for r in osm))
        self.assertTrue(all(r['interpretation'] == 'NOT_ASSESSED' for r in result['records']))
        self.assertTrue(all(r['canonical_entity_id'] is None for r in result['records']))

    def test_no_mutation_or_aliasing_of_inputs(self):
        original = deepcopy(self.inputs)
        result = aggregate(**self.inputs)
        result['records'][0]['source_record'].clear()
        self.assertEqual(self.inputs, original)

    def test_schema_change_is_not_silently_accepted(self):
        self.inputs['osm']['method'] = 'future_unknown'
        with self.assertRaisesRegex(ValueError, 'SOURCE_SCHEMA_CHANGED'):
            aggregate(**self.inputs)
