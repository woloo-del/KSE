"""Synthetic file replay tests, without reading private workspace sources."""
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from grid_engine.observation_history import Observation
from grid_engine.shared_connection import Evidence
from scripts.analyze_historical_assignments import analyze_file, decode_request, CODE_FILES, ROOT


class HistoricalReplayTests(unittest.TestCase):
    def setUp(self):
        proof = Evidence('SYNTHETIC', 'synthetic fixture', 'a' * 64,
                         '2026-01-02T00:00:00Z', '2026-01-01', 'PUBLIC', 'DOCUMENT')
        self.item = Observation('o1', 'synthetic-connection', 'position_project:p1',
                                'PLANNED', 'synthetic-project', None, 'REPORTED', proof,
                                '2026-01-03T00:00:00Z', '2026-01-01', '2026-02-01')
        self.request = {
            'schema_version': 'historical_assignments_request_v1',
            'query': {'connection_id': 'synthetic-connection', 'scenario': 'PLANNED',
                      'known_at': '2026-01-10T00:00:00Z', 'effective_on': '2026-01-05'},
            'observations': [asdict(self.item)],
        }

    def write(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.request), encoding='utf-8')

    def test_deterministic_manifest_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'; self.write(source)
            first, second = root/'first.json', root/'second.json'
            result = analyze_file(source, first, root/'private')
            analyze_file(source, second, root/'private')
            before = first.read_bytes()
            self.assertEqual(before, second.read_bytes())
            manifest = result.pop('reproducibility')
            self.assertEqual(manifest['input_sha256'], hashlib.sha256(source.read_bytes()).hexdigest())
            payload = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
            self.assertEqual(manifest['analysis_payload_sha256'], hashlib.sha256(payload).hexdigest())
            self.assertEqual(set(manifest['code_sha256']), set(CODE_FILES))
            for name, digest in manifest['code_sha256'].items():
                self.assertEqual(digest, hashlib.sha256((ROOT/name).read_bytes()).hexdigest())
            with self.assertRaises(FileExistsError):
                analyze_file(source, first, root/'private')
            self.assertEqual(first.read_bytes(), before)

    def test_query_is_an_explicit_part_of_replay_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'; self.write(source)
            first = analyze_file(source, root/'first.json', root/'private')
            self.request['query']['effective_on'] = '2026-02-01'; self.write(source)
            second = analyze_file(source, root/'second.json', root/'private')
            self.assertEqual(first['known_assigned_positions'], 1)
            self.assertEqual(second['known_assigned_positions'], 0)
            self.assertNotEqual(first['reproducibility']['input_sha256'], second['reproducibility']['input_sha256'])

    def test_future_private_input_protects_entire_manifest(self):
        future = replace(self.item, observation_id='o2', recorded_at='2026-01-20T00:00:00Z',
                         evidence=replace(self.item.evidence, access='PRIVATE'))
        self.request['observations'].append(asdict(future))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'; self.write(source)
            with self.assertRaisesRegex(ValueError, 'PUBLIC_EXPORT_NOT_ALLOWED'):
                analyze_file(source, root/'public.json', root/'private')
            self.assertFalse((root/'public.json').exists())
            result = analyze_file(source, root/'private/result.json', root/'private')
            self.assertEqual(result['access'], 'PRIVATE')
            self.assertEqual(len(result['evidence']), 1)  # future record is not in the temporal view

    def test_private_origin_overrides_public_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'private/input.json'; self.write(source)
            with self.assertRaisesRegex(ValueError, 'PUBLIC_EXPORT_NOT_ALLOWED'):
                analyze_file(source, root/'public.json', root/'private')
            self.assertFalse((root/'public.json').exists())

    def test_duplicate_access_field_fails_before_output_creation(self):
        raw = json.dumps(self.request).replace('"access": "PUBLIC"', '"access": "PRIVATE", "access": "PUBLIC"')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'; source.write_text(raw, encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'DUPLICATE_JSON_FIELD'):
                analyze_file(source, root/'result.json', root/'private')
            self.assertFalse((root/'result.json').exists())

    def test_secret_paths_rejected_before_read_or_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for source, output in [(root/'_secrets/missing.json', root/'out.json'),
                                   (root/'missing.json', root/'_secrets/out.json')]:
                with self.assertRaisesRegex(ValueError, 'SECRET_PATH_FORBIDDEN'):
                    analyze_file(source, output, root/'private')

    def test_unknown_schema_fields_and_invalid_values_fail_closed(self):
        cases = [self.request | {'unexpected': True}, self.request | {'schema_version': 'v999'},
                 self.request | {'query': self.request['query'] | {'extra': 1}},
                 self.request | {'observations': {}},
                 self.request | {'observations': [asdict(self.item) | {'extra': 1}]}]
        for request in cases:
            with self.subTest(request=request), self.assertRaises((ValueError, TypeError)):
                decode_request(json.dumps(request).encode())
        with self.assertRaisesRegex(ValueError, 'NONFINITE_JSON_NUMBER'):
            decode_request(b'{"value":NaN}')

    def test_empty_evidence_cannot_be_exported_as_public_inventory(self):
        self.request['observations'] = []
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'input.json'; self.write(source)
            with self.assertRaisesRegex(ValueError, 'PUBLIC_EXPORT_NOT_ALLOWED'):
                analyze_file(source, root/'public.json', root/'private')
