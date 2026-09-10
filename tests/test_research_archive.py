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


if __name__ == "__main__":
    unittest.main()
