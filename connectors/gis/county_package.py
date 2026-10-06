"""Read-only audit of the parcel layer; never read transactions or extra attributes."""
from collections import Counter
from contextlib import closing
from pathlib import Path
import sqlite3
from shapely.errors import GEOSException

from connectors.gis.geopackage import decode_geometry
from gis.ownership_area import Parcel
from shapely.geometry.base import BaseGeometry


def inspect_parcels(path: Path) -> dict:
    groups, dates, acquired, errors = Counter(), Counter(), Counter(), Counter()
    seen, duplicates = set(), set()
    with closing(sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.execute('PRAGMA trusted_schema=OFF')
        if db.execute('PRAGMA quick_check').fetchone() != ('ok',):
            raise ValueError('SQLITE_INTEGRITY_FAILED')
        metadata = db.execute("SELECT column_name,srs_id FROM gpkg_geometry_columns WHERE table_name='dzialki'").fetchall()
        if metadata != [('geometry', 2180)]:
            raise ValueError('UNSUPPORTED_PARCEL_SCHEMA_OR_CRS')
        changed = db.execute("SELECT last_change FROM gpkg_contents WHERE table_name='dzialki'").fetchone()
        count = 0
        for identifier, group, date, retrieval, blob in db.execute(
            'SELECT id_dzialki,grupa_rejestrowa,data,czas_pozyskania,geometry FROM dzialki'
        ):
            count += 1
            if not identifier:
                errors['MISSING_ID'] += 1
            elif identifier in seen:
                duplicates.add(identifier)
            seen.add(identifier)
            if group is None or group == 0:
                groups['UNKNOWN'] += 1
            elif type(group) is int and 1 <= group <= 16:
                groups[str(group)] += 1
            else:
                errors['INVALID_GROUP'] += 1
            dates[date or 'UNKNOWN'] += 1
            acquired[retrieval or 'UNKNOWN'] += 1
            try:
                geometry = decode_geometry(blob, 2180)
                if geometry.is_empty or not geometry.is_valid or geometry.has_z or geometry.geom_type not in ('Polygon', 'MultiPolygon'):
                    errors['INVALID_GEOMETRY'] += 1
            except (ValueError, GEOSException) as exc:
                # Count errors without logging source rows or private attributes.
                errors['GEOMETRY_DECODE_' + type(exc).__name__] += 1
    return {'method_version': 'county_parcel_audit_v1', 'classification': 'CALCULATED',
            'layer': 'dzialki', 'crs': 'EPSG:2180', 'record_count': count,
            'unique_nonempty_ids': len(seen - {None, ''}), 'duplicate_id_count': len(duplicates),
            'registration_group_counts': dict(sorted(groups.items())),
            'source_date_values': dict(sorted(dates.items())),
            'source_retrieval_values': dict(sorted(acquired.items())),
            'gpkg_last_change': changed[0] if changed else None,
            'errors': dict(errors), 'ownership_area_percent': None,
            'limitations': ['File consistency is not a single legal validity date for all parcels.',
                           'County package is not proof of coverage of a station buffer.',
                           'Only parcel geometry, ID, group and dates were inspected.']}


def select_parcels(path: Path, *, buffer: BaseGeometry, source_id: str) -> tuple[list[Parcel], dict]:
    """Read the audited EPSG:2180 layer and return only positive-area intersections."""
    if not source_id or buffer.is_empty or not buffer.is_valid or buffer.geom_type not in ('Polygon', 'MultiPolygon'):
        raise ValueError('INVALID_SELECTION_INPUT')
    audit = inspect_parcels(path)
    if audit['errors'] or audit['duplicate_id_count']:
        raise ValueError('PACKAGE_REQUIRES_REVIEW')
    selected = []
    with closing(sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.execute('PRAGMA trusted_schema=OFF')
        for identifier, group, date, blob in db.execute('SELECT id_dzialki,grupa_rejestrowa,data,geometry FROM dzialki'):
            geometry = decode_geometry(blob, 2180)
            if geometry.intersection(buffer).area > 0:
                selected.append(Parcel(identifier, geometry, group if group else None, source_id, date or None))
    return selected, audit
