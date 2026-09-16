"""Read-only core GeoPackage geometry decoding (OGC GeoPackage 1.3.1 §2.1.3)."""
from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
import sqlite3
import struct

import shapely
from shapely.geometry.base import BaseGeometry


@dataclass(frozen=True)
class Feature:
    table: str
    fid: int
    srs_id: int
    geometry: BaseGeometry
    properties: dict
    declared_type: str


def decode_geometry(blob: bytes, expected_srs: int) -> BaseGeometry:
    if not isinstance(blob, bytes) or len(blob) < 13 or blob[:2] != b'GP' or blob[2] != 0:
        raise ValueError('INVALID_GEOPACKAGE_HEADER')
    flags = blob[3]
    if flags & 0xE0:
        raise ValueError('UNSUPPORTED_GEOPACKAGE_FLAGS')
    envelope_code = (flags >> 1) & 7
    if envelope_code > 4:
        raise ValueError('INVALID_ENVELOPE_CODE')
    order = '<' if flags & 1 else '>'
    srs = struct.unpack_from(order + 'i', blob, 4)[0]
    if srs != expected_srs:
        raise ValueError('GEOMETRY_CRS_MISMATCH')
    offset = 8 + (0, 32, 48, 48, 64)[envelope_code]
    if len(blob) < offset + 5:
        raise ValueError('TRUNCATED_GEOMETRY')
    geometry = shapely.from_wkb(blob[offset:], on_invalid='raise')
    if bool(flags & 0x10) != geometry.is_empty:
        raise ValueError('EMPTY_FLAG_MISMATCH')
    return geometry


def quote(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def read_features(path: Path) -> tuple[list[Feature], list[dict]]:
    features, errors = [], []
    with closing(sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        db.row_factory = sqlite3.Row
        for layer in db.execute('SELECT * FROM gpkg_geometry_columns'):
            table, column = layer['table_name'], layer['column_name']
            for row in db.execute(f'SELECT * FROM {quote(table)}'):
                properties = dict(row)
                blob = properties.pop(column)
                fid = properties.get('fid')
                try:
                    if fid is None:
                        raise ValueError('FID_REQUIRED_BY_AUDIT')
                    geometry = decode_geometry(blob, layer['srs_id'])
                    features.append(Feature(table, fid, layer['srs_id'], geometry, properties, layer['geometry_type_name']))
                except (ValueError, shapely.errors.GEOSException) as exc:
                    errors.append({'table':table,'fid':fid,'error':str(exc)})
    return features, errors
