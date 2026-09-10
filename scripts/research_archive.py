"""Create or restore a checksummed local archive; never overwrite different data."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/catalog/archive_manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def create() -> None:
    paths = sorted([
        *[p for p in (ROOT / "data/raw/research/2026-09-10").rglob("*") if p.is_file()],
        *[p for p in (ROOT / "data/staging/research").rglob("*") if p.is_file()],
        *list((ROOT / "data/catalog").glob("probe_results_*.json")),
    ])
    records = [{"path": p.relative_to(ROOT).as_posix(), "sha256": sha256(p), "bytes": p.stat().st_size} for p in paths]
    content_id = hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()[:16]
    archive = ROOT / f"data/archives/research_2026-09-10_{content_id}.zip"
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_STORED) as output:
            for record, path in zip(records, paths, strict=True):
                info = zipfile.ZipInfo(record["path"], date_time=(2026, 9, 10, 0, 0, 0))
                info.compress_type = zipfile.ZIP_STORED
                output.writestr(info, path.read_bytes())
    manifest = {"snapshot_date": "2026-09-10", "archive_path": archive.relative_to(ROOT).as_posix(), "archive_sha256": sha256(archive), "archive_bytes": archive.stat().st_size, "files": records, "note": "Local audit archive, excluded from Git. Copy to a separate private backup location; URL alone cannot restore changed source bytes."}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Archive ready: {archive.name}; {len(records)} files; {archive.stat().st_size} bytes")


def restore(archive: Path) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if sha256(archive) != manifest["archive_sha256"]:
        raise ValueError("Archive hash mismatch; nothing restored")
    expected = {item["path"]: item for item in manifest["files"]}
    with zipfile.ZipFile(archive) as source:
        if len(source.namelist()) != len(expected) or set(source.namelist()) != set(expected):
            raise ValueError("Archive file list mismatch; nothing restored")
        pending = []
        for name, record in expected.items():
            target = (ROOT / name).resolve()
            allowed = [ROOT / "data/raw/research", ROOT / "data/staging/research", ROOT / "data/catalog"]
            if not any(target.is_relative_to(base.resolve()) for base in allowed):
                raise ValueError("Archive target outside allowed research directories")
            data = source.read(name)
            if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
                raise ValueError("Archive member mismatch; nothing restored")
            if target.exists():
                if sha256(target) != record["sha256"]:
                    raise ValueError(f"Existing different file preserved: {name}")
            else:
                pending.append((target, data))
        for target, data in pending:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as output:
                output.write(data)
    print(f"Verified {len(expected)} archive members; restored {len(pending)} missing files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["create", "restore"])
    parser.add_argument("archive", nargs="?", type=Path)
    args = parser.parse_args()
    if args.operation == "create":
        create()
    elif args.archive is None:
        parser.error("restore requires the backup ZIP path")
    else:
        restore(args.archive)
