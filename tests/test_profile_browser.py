import json
from pathlib import Path
import tempfile
import unittest
import copy

from backend.profile_browser import browser_data, FILES, ROOT
from backend.profile_projects import project_details


class BrowserTests(unittest.TestCase):
    def setUp(self):
        self.profiles = json.loads((ROOT / 'data/reference' / FILES['profiles']).read_bytes())
        self.imported = json.loads((ROOT / 'data/processed/pse_bulk_pipeline_2026-07-31_v1.json').read_bytes())

    def test_all_selected_records_preserved_with_direction_and_applicant(self):
        result = project_details(self.imported, self.profiles)
        self.assertEqual(sum(map(len, result.values())), 282)
        original = {r['record_id']: r for r in self.imported['records']}
        for rows in result.values():
            for row in rows:
                for field in ('applicant', 'export_MW', 'import_MW', 'raw_export', 'raw_import'):
                    self.assertEqual(row[field], original[row['record_id']][field])

    def test_cross_profile_or_voltage_association_rejected(self):
        for field, value in [('profile_id', 'wrong'), ('voltage_reported', 15)]:
            data = copy.deepcopy(self.imported)
            selected = self.profiles['profiles'][0]['record_ids'][0]
            next(r for r in data['records'] if r['record_id'] == selected)[field] = value
            with self.assertRaisesRegex(ValueError, 'PROJECT_ASSOCIATION_MISMATCH'):
                project_details(data, self.profiles)

    def test_missing_duplicate_and_inconsistent_summary_rejected(self):
        data = copy.deepcopy(self.imported)
        data['records'].append(data['records'][0])
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_PROJECT_RECORD'):
            project_details(data, self.profiles)
        p = copy.deepcopy(self.profiles)
        p['profiles'][0]['record_ids'].append('missing')
        with self.assertRaisesRegex(ValueError, 'PROJECT_RECORD_SET_MISMATCH'):
            project_details(self.imported, p)
        p = copy.deepcopy(self.profiles)
        p['profiles'][0]['status_counts'] = {}
        with self.assertRaisesRegex(ValueError, 'PROJECT_SUMMARY_MISMATCH'):
            project_details(self.imported, p)

    def test_changed_project_snapshot_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / 'data/reference'
            target.mkdir(parents=True)
            for name in FILES.values():
                (target / name).write_bytes((ROOT / 'data/reference' / name).read_bytes())
            path = root / 'data/processed/pse_bulk_pipeline_2026-07-31_v1.json'
            path.parent.mkdir(parents=True)
            path.write_text('{}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'PROJECT_SNAPSHOT_MISMATCH'):
                browser_data(root)

    def test_mixed_snapshots_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'data/reference'
            target.mkdir(parents=True)
            for name in FILES.values():
                (target / name).write_bytes((ROOT / 'data/reference' / name).read_bytes())
            p = target / FILES['profiles']
            data = json.loads(p.read_bytes())
            data['profiles'][0]['name_reported'] = 'Synthetic replacement'
            p.write_text(json.dumps(data), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'PROFILE_SNAPSHOT_MISMATCH'):
                browser_data(Path(tmp))
