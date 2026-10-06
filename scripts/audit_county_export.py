"""Reproduce audit from preserved county ZIP, with hashes and bounded extraction."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.county_package import inspect_parcels


def main() -> None:
    rows = json.loads((ROOT / 'data/catalog/probe_results_county_export_2026-10-06.json').read_text(encoding='utf8'))
    source = next(r for r in rows if r['source_id'] == 'COUNTY_EXPORT_GRUDZIADZ_GPKG')
    archive = ROOT / source['local_path']
    if hashlib.sha256(archive.read_bytes()).hexdigest() != source['sha256']:
        raise ValueError('SOURCE_HASH_MISMATCH')
    with zipfile.ZipFile(archive) as z:
        members = z.infolist()
        if len(members) != 1 or members[0].filename != '0462.gpkg' or members[0].file_size > 250 * 1024 * 1024:
            raise ValueError('UNEXPECTED_ARCHIVE_CONTENT')
        raw = z.read(members[0])
    path = ROOT / 'data/staging/research/grudziadz_parcels_2026-10-06.gpkg'
    if path.exists() and path.read_bytes() != raw:
        raise ValueError('REFUSE_CHANGED_STAGING_FILE')
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(raw)
    result = {'source': source, 'package_sha256': hashlib.sha256(raw).hexdigest(),
              'audit': inspect_parcels(path)}
    (ROOT / 'data/reference/county_export_audit_2026-10-06.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(json.dumps(result['audit'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
