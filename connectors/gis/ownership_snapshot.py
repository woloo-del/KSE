"""Gate one archived GUGiK WFS response before any station-buffer calculation.

This intentionally rejects paged/unknown-count/filtered responses. It does not
fetch, merge live pages or claim cadastral completeness from WFS counters.
"""
import hashlib
import math
import xml.etree.ElementTree as ET
from urllib.parse import parse_qsl, urlparse

from shapely.geometry import Point, shape

from connectors.gis.ownership_probe import normalize_sample
from gis.coordinates import PolishMetricProjection
from gis.ownership_area import BUFFER_QUAD_SEGS, Parcel, summarize_buffer


def _request_bbox(url: str) -> tuple[float, ...]:
    parsed = urlparse(url)
    pairs = [(k.lower(), v) for k, v in parse_qsl(parsed.query)]
    params = dict(pairs)
    allowed = {'service', 'version', 'request', 'typenames', 'count', 'srsname', 'bbox', 'startindex'}
    if len(params) != len(pairs) or set(params) - allowed:
        raise ValueError('AMBIGUOUS_OR_FILTERED_REQUEST')
    expected = {'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature',
                'typenames': 'ms:dzialki', 'srsname': 'urn:ogc:def:crs:EPSG::4326'}
    if any(params.get(k) != v for k, v in expected.items()) or params.get('startindex', '0') != '0':
        raise ValueError('UNSUPPORTED_REQUEST')
    parts = params.get('bbox', '').split(',')
    if len(parts) != 5 or parts[-1] != expected['srsname']:
        raise ValueError('UNSUPPORTED_BBOX_CRS')
    south, west, north, east = map(float, parts[:4])
    if not all(math.isfinite(v) for v in (south, west, north, east)) or not (-90 <= south < north <= 90 and -180 <= west < east <= 180):
        raise ValueError('INVALID_BBOX')
    return west, south, east, north


def prepare_snapshot(raw: bytes, *, source: dict, longitude: float, latitude: float,
                     center_source_id: str, center_source: dict, radius_m: float = 1000) -> dict:
    """Point is only a research input; this function cannot verify a station identity."""
    if hashlib.sha256(raw).hexdigest() != source['sha256']:
        raise ValueError('SOURCE_HASH_MISMATCH')
    if not source.get('source_id') or source['source_id'] == center_source_id:
        raise ValueError('DISTINCT_SOURCE_IDS_REQUIRED')
    if not center_source_id or not source.get('retrieval_date') or not all(center_source.get(k) for k in ('locator', 'retrieval_date', 'sha256')):
        raise ValueError('MISSING_PROVENANCE')
    center_hash = center_source['sha256']
    if not isinstance(center_hash, str) or len(center_hash) != 64 or any(c not in '0123456789abcdef' for c in center_hash):
        raise ValueError('INVALID_CENTER_HASH')
    if isinstance(radius_m, bool) or not math.isfinite(radius_m) or radius_m <= 0:
        raise ValueError('INVALID_RADIUS')
    bbox = _request_bbox(source['url'])
    normalized = normalize_sample(raw)
    projection = PolishMetricProjection()
    center = projection.project(Point(longitude, latitude))
    geographic_buffer = projection.geographic(center.buffer(radius_m, quad_segs=BUFFER_QUAD_SEGS))
    west, south, east, north = geographic_buffer.bounds
    bbox_contains_buffer = bbox[0] <= west and bbox[1] <= south and bbox[2] >= east and bbox[3] >= north
    root = ET.fromstring(raw)
    matched = root.get('numberMatched', '')
    matched_count = int(matched) if matched.isascii() and matched.isdecimal() else None
    reasons = []
    if not bbox_contains_buffer:
        reasons.append('REQUEST_BBOX_DOES_NOT_COVER_BUFFER')
    if matched_count is None:
        reasons.append('MATCHED_COUNT_UNKNOWN')
    elif matched_count != len(normalized['features']):
        reasons.append('RESPONSE_NOT_COMPLETE')
    if root.get('next'):
        reasons.append('MORE_PAGES_DECLARED')
    parcels = [Parcel(f['id'], projection.project(shape(f['geometry'])),
                      f['properties']['registration_group'], source['source_id'],
                      f['properties']['source_date_raw']) for f in normalized['features']]
    sources = {source['source_id']: {'locator': source['url'], 'sha256': source['sha256'],
                                   'retrieval_date': source['retrieval_date']},
               center_source_id: center_source}
    result = {'method_version': 'ownership_snapshot_gate_v1', 'source': source,
              'center': {'longitude': longitude, 'latitude': latitude, 'source_id': center_source_id,
                         'source': center_source, 'role': 'RESEARCH_POINT_NOT_VERIFIED_STATION'},
              'radius_m': radius_m, 'request_bbox_lon_lat': bbox,
              'transformation': projection.metadata(), 'returned_parcels': len(parcels),
              'number_matched_reported': matched_count, 'blocking_reasons': reasons,
              'status': 'BLOCKED_INCOMPLETE_INPUT' if reasons else 'SINGLE_RESPONSE_READY_FOR_REVIEW',
              'area_result': None,
              'limitations': ['Known matching count only verifies this response, not source cadastral completeness.',
                             'No station identity, ownership validity, reuse permission or legal classification established.']}
    if not reasons:
        result['area_result'] = summarize_buffer(center=center, center_source_id=center_source_id,
                                                parcels=parcels, sources=sources, crs='EPSG:2180', radius_m=radius_m)
    return result
