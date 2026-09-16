"""Restore the real archive into an isolated folder; never alter original inputs."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("research_archive", ROOT / "scripts/research_archive.py")
assert SPEC and SPEC.loader
archive_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(archive_module)


class ArchiveRestoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads((ROOT / "data/catalog/archive_manifest.json").read_text(encoding="utf-8"))
        cls.archive = ROOT / cls.manifest["archive_path"]
        cls.temp = tempfile.TemporaryDirectory(prefix="kse_archive_test_", dir=ROOT / "data/staging")
        cls.test_root = Path(cls.temp.name).resolve()
        if not cls.test_root.is_relative_to((ROOT / "data/staging").resolve()):
            raise RuntimeError("Unexpected test cleanup directory")
        cls.test_manifest = cls.test_root / "data/catalog/archive_manifest.json"
        cls.test_manifest.parent.mkdir(parents=True)
        cls.test_manifest.write_text(json.dumps(cls.manifest), encoding="utf-8")
        archive_module.ROOT = cls.test_root
        archive_module.MANIFEST = cls.test_manifest
        archive_module.restore(cls.archive)

    @classmethod
    def tearDownClass(cls) -> None:
        archive_module.ROOT = ROOT
        archive_module.MANIFEST = ROOT / "data/catalog/archive_manifest.json"
        cls.temp.cleanup()

    def test_all_restored_bytes_match_manifest(self) -> None:
        for item in self.manifest["files"]:
            with self.subTest(path=item["path"]):
                path = self.test_root / item["path"]
                self.assertEqual(path.stat().st_size, item["bytes"])
                self.assertEqual(archive_module.sha256(path), item["sha256"])

    def test_corrupt_archive_rejected(self) -> None:
        invalid = self.test_root / "synthetic_invalid_archive.zip"
        invalid.write_bytes(b"SYNTHETIC TEST INPUT, NOT GRID DATA")
        with self.assertRaisesRegex(ValueError, "Archive hash mismatch"):
            archive_module.restore(invalid)

    def test_existing_different_file_is_preserved(self) -> None:
        target = self.test_root / "data/raw/research/2026-09-10/pge_capacity_landing.html"
        original = target.read_bytes()
        synthetic = b"SYNTHETIC TEST INPUT, NOT GRID DATA"
        try:
            target.write_bytes(synthetic)
            with self.assertRaisesRegex(ValueError, "Existing different file preserved"):
                archive_module.restore(self.archive)
            self.assertEqual(target.read_bytes(), synthetic)
        finally:
            target.write_bytes(original)

    def test_new_radkowice_archives_restore_and_verify_without_writing(self) -> None:
        for name in ['radkowice_archive_manifest.json', 'radkowice_tariff_archive.json',
                     'radkowice_wolica_archive.json', 'radkowice_followup_archive_2026-09-15.json',
                     'radkowice_decision_archive_2026-09-15.json']:
            manifest_path = ROOT / 'data/catalog' / name
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
            archive = ROOT / manifest.get('archive', manifest.get('archive_path'))
            members = manifest.get('members', manifest.get('files'))
            archive_module.restore(archive, manifest_path, verify_only=True)
            for member in members:
                self.assertFalse((self.test_root / member.get('local_path', member.get('path'))).exists())
            archive_module.restore(archive, manifest_path)
            for member in members:
                self.assertEqual(archive_module.sha256(self.test_root / member.get('local_path', member.get('path'))), member['sha256'])

    def test_duplicate_and_unsafe_manifest_paths_rejected_before_write(self) -> None:
        for name in ['../outside.txt', 'data/raw/research/../../private/file', 'data/raw/research/file:stream', 'C:/outside', 'data\\raw\\research\\file']:
            invalid = dict(self.manifest, files=[dict(self.manifest['files'][0], path=name)])
            path = self.test_root / 'invalid_manifest.json'
            path.write_text(json.dumps(invalid), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Invalid archive member path'):
                archive_module.restore(self.archive, path)
        invalid = dict(self.manifest, files=[self.manifest['files'][0]] * 2)
        path.write_text(json.dumps(invalid), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Duplicate manifest member'):
            archive_module.restore(self.archive, path)


if __name__ == "__main__":
    unittest.main()
