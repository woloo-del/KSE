"""Spatial audit of a bounded OSM XML snapshot; no operational topology inference."""
from __future__ import annotations

from collections import Counter
from decimal import Decimal
import math
import re
import xml.etree.ElementTree as ET

from shapely.geometry import LineString, Point, Polygon


def voltage_kv(raw: str | None) -> list[float] | None:
    """OSM voltage values are volts; semicolon-separated values stay separate."""
    if raw is None or not re.fullmatch(r'[1-9][0-9]*(?:;[1-9][0-9]*)*', raw):
        return None
    return [float(Decimal(part) / 1000) for part in raw.split(';')]


def audit(data: bytes, station_way_id: int) -> dict:
    if b'<!DOCTYPE' in data.upper() or b'<!ENTITY' in data.upper():
        raise ValueError('UNSUPPORTED_XML_DECLARATION')
    root = ET.fromstring(data)
    if root.tag != 'osm':
        raise ValueError('NOT_OSM_XML')
    elements = [e for e in root if e.tag in {'node', 'way', 'relation'}]
    identities = [(e.tag, e.get('id')) for e in elements]
    if any(identity[1] is None for identity in identities) or len(set(identities)) != len(identities):
        raise ValueError('INVALID_OSM_IDENTITIES')
    tags = {id(e): {t.get('k'): t.get('v') for t in e.findall('tag')} for e in elements}
    nodes = {}
    for e in elements:
        if e.tag == 'node':
            lon, lat = float(e.get('lon', 'nan')), float(e.get('lat', 'nan'))
            if not math.isfinite(lon) or not math.isfinite(lat) or not -180 <= lon <= 180 or not -90 <= lat <= 90:
                raise ValueError('INVALID_OSM_COORDINATES')
            nodes[e.get('id')] = (lon, lat)
    station = next((e for e in elements if e.tag == 'way' and e.get('id') == str(station_way_id)), None)
    if station is None or tags[id(station)].get('power') != 'substation':
        raise ValueError('STATION_WAY_NOT_FOUND')

    def geometry(element):
        refs = [n.get('ref') for n in element.findall('nd')]
        if any(ref not in nodes for ref in refs):
            raise ValueError('MISSING_WAY_NODE')
        return refs, [nodes[ref] for ref in refs]

    refs, coords = geometry(station)
    if len(refs) < 4 or refs[0] != refs[-1]:
        raise ValueError('STATION_POLYGON_NOT_CLOSED')
    polygon = Polygon(coords)
    if polygon.is_empty or not polygon.is_valid:
        raise ValueError('INVALID_STATION_POLYGON')
    selected = []
    for e in elements:
        t = tags[id(e)]
        if 'power' not in t or e.tag == 'relation':
            continue
        if e.tag == 'node':
            selected_spatially = polygon.covers(Point(nodes[e.get('id')]))
            node_ids = None
            selection = 'POINT_COVERED_BY_STATION_POLYGON'
        else:
            node_ids, coordinates = geometry(e)
            if len(coordinates) < 2:
                raise ValueError('INVALID_POWER_WAY')
            selected_spatially = polygon.intersects(LineString(coordinates))
            selection = 'WAY_INTERSECTS_STATION_POLYGON'
        if not selected_spatially:
            continue
        if not e.get('version') or not e.get('timestamp'):
            raise ValueError('MISSING_OSM_VERSION_METADATA')
        voltages = {key: {'raw_value': value, 'value_kV': voltage_kv(value),
                          'classification': 'CALCULATED' if voltage_kv(value) is not None else 'UNKNOWN',
                          'unit_conversion': 'V / 1000; semicolon components retained'}
                    for key, value in t.items() if key == 'voltage' or key.startswith('voltage:')}
        selected.append({'osm_type': e.tag, 'osm_id': int(e.get('id')), 'osm_version': int(e.get('version')),
                         'osm_edit_timestamp': e.get('timestamp'),
                         'osm_url': f"https://www.openstreetmap.org/{e.tag}/{e.get('id')}",
                         'tags_reported_by_osm': t, 'source_quality': 'G',
                         'tag_value_classification': 'REPORTED',
                         'reporting_authority': 'OSM_COMMUNITY_NOT_OPERATOR',
                         'voltage_observations': voltages, 'node_ids': node_ids,
                         'spatial_selection': {'method': selection, 'classification': 'CALCULATED'},
                         'electrical_connectivity': 'UNKNOWN', 'equipment_owner': None,
                         'available_capacity_MW': None, 'operator_verified': False})
    return {'method': 'osm_station_spatial_audit_v1', 'station_osm_way_id': station_way_id,
            'attribution': '© OpenStreetMap contributors', 'license': 'ODbL-1.0',
            'license_url': 'https://www.openstreetmap.org/copyright',
            'summary': {'returned_osm_elements': len(elements),
                        'returned_power_elements': sum('power' in tags[id(e)] for e in elements),
                        'spatially_selected_records': len(selected),
                        'selected_power_tags': dict(Counter(r['tags_reported_by_osm']['power'] for r in selected))},
            'records': selected, 'power_flow_ready': False,
            'limitations': ['OSM map responses include complete ways and nodes beyond the requested bounding box.',
                           'Spatial inclusion and shared node IDs do not confirm energized electrical connectivity.',
                           'Edit timestamps are not commissioning, observation or measurement dates.',
                           'Operator tags do not establish ownership of all equipment inside the station polygon.',
                           'Relations are retained in raw XML but not resolved into electrical circuits by this audit.',
                           'Neither completeness nor current engineering parameters are established.']}
