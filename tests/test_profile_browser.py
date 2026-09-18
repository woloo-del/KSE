import json
from pathlib import Path
import tempfile
import unittest

from backend.profile_browser import browser_data, FILES, ROOT


class BrowserTests(unittest.TestCase):
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
