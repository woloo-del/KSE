"""Reproduce audit from preserved county ZIP, with hashes and bounded extraction."""
import hashlib
import argparse
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.gis.county_package import inspect_parcels


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--county', choices=('0462', '0406'), default='0462')
    county = parser.parse_args().county
    rural = county == '0406'
    manifest = 'probe_results_wegrowo_rural_2026-10-06.json' if rural else 'probe_results_county_export_2026-10-06.json'
    source_id = 'COUNTY_EXPORT_GRUDZIADZ_RURAL_GPKG' if rural else 'COUNTY_EXPORT_GRUDZIADZ_GPKG'
    rows = json.loads((ROOT / 'data/catalog' / manifest).read_text(encoding='utf8'))
    source = next(r for r in rows if r['source_id'] == source_id)
    archive = ROOT / source['local_path']
    if hashlib.sha256(archive.read_bytes()).hexdigest() != source['sha256']:
        raise ValueError('SOURCE_HASH_MISMATCH')
    with zipfile.ZipFile(archive) as z:
        members = z.infolist()
        if len(members) != 1 or members[0].filename != county + '.gpkg' or members[0].file_size > 250 * 1024 * 1024:
            raise ValueError('UNEXPECTED_ARCHIVE_CONTENT')
        raw = z.read(members[0])
    stem = 'grudziadz_rural_parcels' if rural else 'grudziadz_parcels'
    path = ROOT / f'data/staging/research/{stem}_2026-10-06.gpkg'
    if path.exists() and path.read_bytes() != raw:
        raise ValueError('REFUSE_CHANGED_STAGING_FILE')
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(raw)
    result = {'source': source, 'package_sha256': hashlib.sha256(raw).hexdigest(),
              'audit': inspect_parcels(path)}
    output = 'county_rural_export_audit_2026-10-06.json' if rural else 'county_export_audit_2026-10-06.json'
    (ROOT / 'data/reference' / output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(json.dumps(result['audit'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
