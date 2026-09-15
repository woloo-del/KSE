"""Checks against preserved public evidence; no synthetic grid facts."""
import json
from pathlib import Path
import tempfile
import unittest

from grid_engine.observation_history import Observation, as_known
from grid_engine.shared_connection import Evidence
from scripts.build_radkowice_history import build, save

ROOT = Path(__file__).resolve().parents[1]


class RadkowiceHistoryTests(unittest.TestCase):
    def test_replay_preserved_evidence(self):
        saved = json.loads((ROOT / 'data/reference/radkowice_observation_history_v1.json').read_text(encoding='utf-8'))
        self.assertEqual(build(saved['recorded_at']), saved)
        self.assertEqual(len(saved['observations']), 3)
        for raw in saved['observations']:
            item = Observation(**{**raw, 'evidence': Evidence(**raw['evidence'])})
            result = as_known((item,), entity_id=item.entity_id, field=item.field,
                              scenario=item.scenario, unit=None,
                              known_at=saved['recorded_at'], effective_on='2026-09-15')
            self.assertEqual(result['status'], 'UNKNOWN')
            self.assertEqual(len(result['unresolved_validity']), 1)
            self.assertEqual(item.classification, 'REPORTED')

    def test_snapshot_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'snapshot.json'
            save({'version': 1}, path)
            before = path.read_bytes()
            save({'version': 1}, path)
            with self.assertRaisesRegex(ValueError, 'HISTORY_SNAPSHOT_EXISTS'):
                save({'version': 2}, path)
            self.assertEqual(path.read_bytes(), before)
