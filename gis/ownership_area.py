"""Auditable planar parcel overlay; no legal ownership or grid feasibility inference."""
from dataclasses import dataclass
import hashlib
import json
import math
from typing import Sequence

import shapely
from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union
from shapely.strtree import STRtree

METHOD = 'registration_group_buffer_v1'
CRS = 'EPSG:2180'
# 256 circle segments: maximum radial approximation error at 1 km < 0.076 m.
BUFFER_QUAD_SEGS = 64
# Floating-point partition check only; never used to discard parcel overlaps.
PARTITION_REL_TOLERANCE = 1e-9
PARTITION_ABS_TOLERANCE_M2 = 1e-6


@dataclass(frozen=True)
class Parcel:
    parcel_id: str
    geometry: BaseGeometry
    registration_group: int | None
    source_id: str
    source_date: str | None = None


def _validate_geometry(geometry: BaseGeometry, allowed: set[str]) -> None:
    if geometry.geom_type not in allowed or geometry.is_empty or geometry.has_z or not geometry.is_valid:
        raise ValueError('INVALID_GEOMETRY')
    if not all(math.isfinite(v) for v in geometry.bounds):
        raise ValueError('NONFINITE_GEOMETRY')


def summarize_buffer(*, center: Point, center_source_id: str, parcels: Sequence[Parcel],
                     sources: dict[str, dict], crs: str, radius_m: float = 1000) -> dict:
    """All inputs must already be explicitly transformed to EPSG:2180 (x=easting).

    Uncovered area, absent groups and overlapping parcel polygons stay separate.
    Any positive-area overlap is withheld from all group totals, even same-group
    overlaps. Touching boundaries have zero area and are not a conflict.
    Source metadata is preserved; geometric coverage never proves survey completeness.
    """
    if crs != CRS:
        raise ValueError('METRIC_CRS_REQUIRED')
    if isinstance(radius_m, bool) or not math.isfinite(radius_m) or radius_m <= 0:
        raise ValueError('INVALID_RADIUS')
    _validate_geometry(center, {'Point'})
    used_sources = {center_source_id, *(p.source_id for p in parcels)}
    for source_id in used_sources:
        source = sources.get(source_id, {})
        if not source_id or not all(source.get(k) for k in ('locator', 'retrieval_date', 'sha256')):
            raise ValueError('MISSING_PROVENANCE')
        digest = source['sha256']
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError('INVALID_SOURCE_HASH')
    seen = set()
    for parcel in parcels:
        if not parcel.parcel_id or parcel.parcel_id in seen:
            raise ValueError('DUPLICATE_OR_MISSING_PARCEL_ID')
        seen.add(parcel.parcel_id)
        if parcel.registration_group is not None and (type(parcel.registration_group) is not int or parcel.registration_group not in range(1, 17)):
            raise ValueError('INVALID_GROUP')
        _validate_geometry(parcel.geometry, {'Polygon', 'MultiPolygon'})
    buffer = center.buffer(radius_m, quad_segs=BUFFER_QUAD_SEGS)
    ordered = sorted(parcels, key=lambda p: p.parcel_id)
    clipped = [(p, p.geometry.intersection(buffer)) for p in ordered]
    clipped = [(p, g) for p, g in clipped if g.area > 0]
    geometries = [g for _, g in clipped]
    tree = STRtree(geometries)
    overlaps, pairs = [], []
    for i, geometry in enumerate(geometries):
        for j in sorted(int(k) for k in tree.query(geometry, predicate='intersects') if int(k) > i):
            overlap = geometry.intersection(geometries[j])
            if overlap.area > 0:
                overlaps.append(overlap)
                pairs.append({'parcel_ids': [clipped[i][0].parcel_id, clipped[j][0].parcel_id],
                              'overlap_m2': overlap.area})
    conflict = unary_union(overlaps)
    covered = unary_union(geometries)
    missing_geometry = buffer.difference(covered)
    by_group = {}
    for parcel, geometry in clipped:
        by_group.setdefault(parcel.registration_group, []).append(geometry)

    def area(geometry: BaseGeometry) -> dict:
        return {'area_m2': geometry.area, 'area_ha': geometry.area / 10000,
                'percent_of_buffer': geometry.area / buffer.area * 100}

    groups = {str(group): area(unary_union(by_group.get(group, [])).difference(conflict)) for group in range(1, 17)}
    missing_group = unary_union(by_group.get(None, [])).difference(conflict)
    unknown = unary_union([missing_geometry, missing_group, conflict])
    partition_area = sum(v['area_m2'] for v in groups.values()) + unknown.area
    if not math.isclose(partition_area, buffer.area, rel_tol=PARTITION_REL_TOLERANCE,
                        abs_tol=PARTITION_ABS_TOLERANCE_M2):
        raise ValueError('AREA_PARTITION_MISMATCH')
    input_metadata = {'center_wkb': center.wkb_hex, 'center_source_id': center_source_id,
                      'radius_m': radius_m, 'crs': crs,
                      'sources': {k: sources[k] for k in sorted(used_sources)},
                      'parcels': [{'id': p.parcel_id, 'geometry_wkb': p.geometry.wkb_hex,
                                   'group': p.registration_group, 'source_id': p.source_id,
                                   'source_date': p.source_date} for p in ordered]}
    fingerprint = hashlib.sha256(json.dumps(input_metadata, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return {'method_version': METHOD, 'classification': 'CALCULATED', 'crs': crs,
            'radius_m': radius_m, 'buffer_quad_segs': BUFFER_QUAD_SEGS,
            'center': {'x': center.x, 'y': center.y, 'source_id': center_source_id},
            'input_fingerprint': fingerprint, 'sources': input_metadata['sources'],
            'runtime': {'shapely': shapely.__version__, 'geos': shapely.geos_version_string},
            'buffer_area_m2': buffer.area, 'geometric_coverage': area(covered),
            'groups': groups, 'unknown_total': area(unknown),
            'unknown_components': {'missing_geometry': area(missing_geometry),
                                   'missing_group': area(missing_group), 'overlap': area(conflict)},
            'overlap_pairs': pairs, 'input_parcel_count': len(parcels),
            'intersecting_parcel_count': len(clipped),
            'parcel_observations': [{'parcel_id': p.parcel_id, 'source_id': p.source_id,
                                    'source_date': p.source_date, 'registration_group': p.registration_group,
                                    'clipped_area_m2_before_overlap_exclusion': g.area} for p, g in clipped],
            'ownership_binary_split': None,
            'limitations': ['Coverage describes supplied geometry only, not completeness or freshness of EGiB.',
                            'Registration groups are not a validated public/private ownership split.',
                            'Positive-area overlaps are excluded from every group total.',
                            'Planar polygonal buffer in EPSG:2180; not a surveyed land boundary.']}
