"""Independent expected values for the preserved operator sample."""
import unittest
from pathlib import Path
from scripts.research_radkowice import extract


class RadkowiceResearchTests(unittest.TestCase):
    @unittest.skipUnless(Path('data/raw/research/2026-09-10/pse_pipeline_url_2026-07-31.xlsx').exists(), 'Restore raw research archive')
    def test_actual_operator_sample(self):
        rows = extract()['records']
        self.assertEqual([r['row'] for r in rows], [787, 843, 847])
        self.assertEqual([r['project_name'] for r in rows], ['MEE Chałupki','MEE Radkowice','MEE Chęciny'])
        self.assertEqual([r['connection_export_MW'] for r in rows], [96.96,50,100])
        self.assertEqual([r['connection_import_MW'] for r in rows], [98.8992,50,102])
        self.assertTrue(all(r['voltage_kV'] == 220 for r in rows))
        self.assertTrue(all(r['status_reported'] == 'UMOWA O PRZYŁĄCZENIE obowiązująca' for r in rows))
        self.assertTrue(all(r['source_date']=='2026-07-31' and len(r['snapshot_sha256'])==64 for r in rows))


if __name__ == '__main__':
    unittest.main()
