"""Read-only inventory and technical inspection; derived output stays private."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from contextlib import closing
from pathlib import Path
import sqlite3
import zipfile
from datetime import datetime, timezone


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def inspect_gpkg(path: Path) -> dict:
    with closing(sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.row_factory = sqlite3.Row
        tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        result = {'integrity': db.execute('PRAGMA quick_check').fetchone()[0], 'layers': [],
                  'spatial_reference_systems': [dict(r) for r in db.execute('SELECT * FROM gpkg_spatial_ref_sys')]}
        for row in db.execute('SELECT * FROM gpkg_contents'):
            layer = dict(row)
            table = quote_identifier(row['table_name'])
            columns = [dict(r) for r in db.execute(f'PRAGMA table_info({table})')]
            geometry = [dict(r) for r in db.execute('SELECT * FROM gpkg_geometry_columns WHERE table_name=?', (row['table_name'],))]
            geometry_names = {g['column_name'] for g in geometry}
            fields = [c['name'] for c in columns if c['name'] not in geometry_names]
            layer.update(columns=columns, geometry=geometry, count=db.execute(f'SELECT count(*) FROM {table}').fetchone()[0])
            projection = ','.join(quote_identifier(c) for c in fields)
            records = [dict(r) for r in db.execute(f'SELECT {projection} FROM {table}')]
            layer['sample_attributes'] = records[:3]
            layer['radkowice_matches'] = [r for r in records if any('radkow' in str(v).casefold() for v in r.values())]
            layer['null_counts'] = {c: sum(r[c] is None for r in records) for c in fields}
            layer['null_geometry_count'] = db.execute(f'SELECT count(*) FROM {table} WHERE {quote_identifier(next(iter(geometry_names)))} IS NULL').fetchone()[0] if geometry_names else None
            if 'xcoord' in fields and 'ycoord' in fields:
                layer['invalid_attribute_coordinate_count'] = sum(
                    not (isinstance(r['xcoord'], (int, float)) and isinstance(r['ycoord'], (int, float))
                         and math.isfinite(r['xcoord']) and math.isfinite(r['ycoord'])
                         and -180 <= r['xcoord'] <= 180 and -90 <= r['ycoord'] <= 90)
                    for r in records) if row['srs_id'] == 4326 else None
            name_field = next((c for c in ('Name', 'Nazwa stacji', 'Nazwa obiektu') if c in fields), None)
            layer['duplicate_names'] = {k:v for k,v in Counter(r[name_field] for r in records).items() if k and v > 1} if name_field else {}
            layer['geometry_validation'] = 'NOT_PERFORMED; coordinate attributes are not a geometry accuracy check'
            result['layers'].append(layer)
        result['metadata'] = [dict(r) for r in db.execute('SELECT * FROM gpkg_metadata')] if 'gpkg_metadata' in tables else []
        return result


def inspect(root: Path, output: Path) -> None:
    private = Path(__file__).resolve().parents[1] / 'data/private'
    root, output = root.resolve(), output.resolve()
    if not root.is_relative_to(private.resolve()) or not output.is_relative_to(private.resolve()):
        raise ValueError('Input and output must remain under data/private.')
    if output.exists() or output.is_relative_to(root):
        raise ValueError('Use a new output directory outside the source tree.')
    files = sorted(p for p in root.rglob('*') if p.is_file())
    output.mkdir(parents=True)
    entries = []
    for i, path in enumerate(files, 1):
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        entry = {'id': f'F{i:03}', 'path': path.relative_to(private).as_posix(),
                 'size': path.stat().st_size, 'sha256': digest}
        try:
            if path.suffix.lower() == '.pdf':
                from pypdf import PdfReader
                reader = PdfReader(path)
                pages = [p.extract_text() or '' for p in reader.pages]
                entry.update(page_count=len(pages), metadata={str(k): str(v) for k, v in (reader.metadata or {}).items()},
                             text_characters=[len(p) for p in pages])
                target = output / (entry['id'] + '.txt')
                target.write_text('\n\n'.join(f'=== PAGE {n} ===\n{t}' for n,t in enumerate(pages,1)), encoding='utf-8')
                entry['text_file'] = target.name
            elif path.suffix.lower() == '.gpkg':
                entry['gpkg'] = inspect_gpkg(path)
            elif path.suffix.lower() in ('.zip', '.kmz'):
                with zipfile.ZipFile(path) as archive:
                    entry['archive_members'] = [{'name': z.filename, 'size': z.file_size} for z in archive.infolist()]
        except Exception as exc:
            entry['inspection_error'] = f'{type(exc).__name__}: {exc}'
        entries.append(entry)
    (output / 'inventory.json').write_text(json.dumps({'schema_version':'private_inspection_v1',
        'retrieved_at':datetime.now(timezone.utc).isoformat(), 'access':'PRIVATE',
        'source_date':None, 'records':entries},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(entries)} files inspected; results: {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    inspect(args.root,args.output)
