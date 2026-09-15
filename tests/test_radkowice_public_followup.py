"""Verify preserved public research evidence; no inferred technical parameters."""
import hashlib
import json
from pathlib import Path
import unittest
import zipfile
from pypdf import PdfReader
from scripts.validate_research import validate

ROOT = Path(__file__).resolve().parents[1]


class PublicFollowupTests(unittest.TestCase):
    def test_catalog_validator_covers_later_and_repeated_snapshots(self):
        result=validate()
        self.assertEqual(result['errors'],[])
        names={i['name'] for i in result['checks'] if i['passed']}
        for expected in ['probe_snapshot_identities_unique','all_raw_files_have_manifests',
                         'probe_references:CHECINY_ENERGY_PLAN','probe_references:PSE_TARIFF_2026',
                         'snapshot_sha256:PSE_RADK_BRIDGE_NOTICE_2025']:
            self.assertIn(expected,names)

    def test_archive_and_raw_bytes_match_all_three_sources(self):
        manifest=json.loads((ROOT/'data/catalog/radkowice_followup_archive_2026-09-15.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest['members']),3)
        self.assertEqual(hashlib.sha256((ROOT/manifest['archive']).read_bytes()).hexdigest(),manifest['sha256'])
        with zipfile.ZipFile(ROOT/manifest['archive']) as archive:
            for member in manifest['members']:
                expected=member['sha256']
                self.assertEqual(hashlib.sha256((ROOT/member['local_path']).read_bytes()).hexdigest(),expected)
                self.assertEqual(hashlib.sha256(archive.read(member['local_path'])).hexdigest(),expected)

    def test_bridge_document_is_forecast_not_commissioning(self):
        pdf=PdfReader(ROOT/'data/raw/research/2026-09-15/pse_bridge_notice_2025.pdf')
        text=' '.join(pdf.pages[28].extract_text().split())
        self.assertIn('Rozbudowa SE Radkowice o pole 220kV wraz z mostem szynowym.',text)
        self.assertIn('prognozowanych',text)
        self.assertIn('wyłącznie do celów informacyjnych',text)
        self.assertIn('Na potrzeby niniejszego ogłoszenia',text)
        self.assertIn('31/03/2025',pdf.pages[36].extract_text())

    def test_rdos_notice_identifies_decision_not_construction(self):
        text=(ROOT/'data/raw/research/2026-09-15/rdos_radkowice_piaski_2025.html').read_text(encoding='utf-8')
        self.assertIn('WOO-I.420.7.2025.PJ/PP.14',text)
        self.assertIn('Radkowice - Kielce Piaski',text)
        self.assertIn('09.12.2025',text)
