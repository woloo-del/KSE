"""Synthetic input files only; no user documents are read by these tests."""
from dataclasses import asdict
from decimal import Decimal
import json
import hashlib
from pathlib import Path
import tempfile
import unittest

from scripts.analyze_shared_connection import analyze_file, decode_snapshot
from grid_engine.shared_connection import Evidence, SharedConnectionSnapshot


class ReplayTests(unittest.TestCase):
    def setUp(self):
        proof = Evidence('SYNTHETIC_REPLAY', 'synthetic fixture',
            hashlib.sha256(b'SYNTHETIC REPLAY ONLY').hexdigest(),
            '2026-09-11T00:00:00Z','2026-09-10','PUBLIC','DOCUMENT')
        self.input = asdict(SharedConnectionSnapshot('SYNTHETIC_SNAPSHOT','SYNTHETIC_BRIDGE',
            '2026-09-11','PLANNED',4,proof))

    def test_decimal_limits_are_not_rounded_by_binary_float(self):
        self.input['export_limit_MW']='12.34567890123456789'
        self.input['export_evidence']=self.input['position_evidence']
        parsed=decode_snapshot(json.dumps(self.input).encode())
        self.assertEqual(parsed.export_limit_MW,Decimal('12.34567890123456789'))

    def test_unknown_fields_and_nonfinite_values_rejected(self):
        self.input['unexpected_field']=1
        with self.assertRaises(TypeError): decode_snapshot(json.dumps(self.input).encode())
        with self.assertRaisesRegex(ValueError,'NONFINITE_JSON_NUMBER'):
            decode_snapshot(b'{"maximum_positions":NaN}')

    def test_private_path_blocks_export_even_with_public_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); private=root/'private'; private.mkdir()
            source=private/'input.json'; source.write_text(json.dumps(self.input),encoding='utf-8')
            out=root/'public.json'
            with self.assertRaisesRegex(ValueError,'PUBLIC_EXPORT_NOT_ALLOWED'):
                analyze_file(source,out,private)
            self.assertFalse(out.exists())

    def test_replay_is_deterministic_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'input.json'
            source.write_text(json.dumps(self.input),encoding='utf-8')
            first=root/'result1.json'; second=root/'result2.json'
            analyze_file(source,first,root/'private')
            analyze_file(source,second,root/'private')
            original=first.read_bytes()
            self.assertEqual(original,second.read_bytes())
            with self.assertRaises(FileExistsError):
                analyze_file(source,first,root/'private')
            self.assertEqual(first.read_bytes(),original)

    def test_private_evidence_cannot_export_from_public_input_folder(self):
        self.input['position_evidence']['access']='PRIVATE'
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'input.json'
            source.write_text(json.dumps(self.input),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'PUBLIC_EXPORT_NOT_ALLOWED'):
                analyze_file(source,root/'output.json',root/'private')
            result=analyze_file(source,root/'private/result.json',root/'private')
            self.assertEqual(result['access'],'PRIVATE')


if __name__=='__main__':
    unittest.main()
