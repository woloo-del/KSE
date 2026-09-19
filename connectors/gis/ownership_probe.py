"""Inspect a bounded WFS sample; never equate an empty ownership field with private land."""
import xml.etree.ElementTree as ET
import math
import re


def inspect_sample(raw: bytes) -> dict:
    root = ET.fromstring(raw)
    wfs, ms = '{http://www.opengis.net/wfs/2.0}', '{http://mapserver.gis.umn.edu/mapserver}'
    if root.tag != wfs + 'FeatureCollection':
        raise ValueError('NOT_WFS_FEATURE_COLLECTION')
    members = root.findall(wfs + 'member')
    if root.get('numberReturned') != str(len(members)):
        raise ValueError('RETURNED_COUNT_MISMATCH')
    counts = {'missing': 0, 'empty': 0, 'populated': 0}
    seen = set()
    for member in members:
        parcel = member.find(ms + 'dzialki')
        if parcel is None:
            raise ValueError('UNEXPECTED_FEATURE_TYPE')
        identifier = parcel.findtext(ms + 'ID_DZIALKI')
        if not identifier or identifier in seen:
            raise ValueError('MISSING_OR_DUPLICATE_PARCEL_ID')
        seen.add(identifier)
        group = parcel.find(ms + 'GRUPA_REJESTROWA')
        state = 'missing' if group is None else 'empty' if not (group.text or '').strip() else 'populated'
        counts[state] += 1
    return {'returned_parcels': len(members), 'number_matched_reported': root.get('numberMatched'),
            'registration_group_field': counts, 'ownership_area_percent': None,
            'scope': 'BOUNDED_SAMPLE_NOT_1KM_COVERAGE', 'ownership_classification': 'NOT_PERFORMED'}


def normalize_sample(raw: bytes) -> dict:
    """Normalize only verified 2D GML Polygon/4326 shape; reject other encodings.

    This is a bounded research parser, not nationwide pagination or coverage proof.
    Source CRS uses latitude/longitude; GeoJSON uses longitude/latitude.
    """
    from shapely.geometry import Polygon, mapping

    summary = inspect_sample(raw)
    root = ET.fromstring(raw)
    gml = '{http://www.opengis.net/gml/3.2}'
    ms = '{http://mapserver.gis.umn.edu/mapserver}'
    features = []
    for parcel in root.findall('{http://www.opengis.net/wfs/2.0}member/' + ms + 'dzialki'):
        for field in ('ID_DZIALKI', 'GRUPA_REJESTROWA', 'DATA', 'geom'):
            if len(parcel.findall(ms + field)) > 1:
                raise ValueError('DUPLICATE_PARCEL_FIELD')
        group_text = (parcel.findtext(ms + 'GRUPA_REJESTROWA') or '').strip()
        if group_text and not re.fullmatch(r'(?:[1-9]|1[0-6])', group_text):
            raise ValueError('UNSUPPORTED_REGISTRATION_GROUP')
        geom = parcel.find(ms + 'geom')
        if geom is None or len(geom) != 1 or geom[0].tag != gml + 'Polygon':
            raise ValueError('UNSUPPORTED_GEOMETRY')
        polygon = geom[0]
        if polygon.get('srsName') != 'urn:ogc:def:crs:EPSG::4326':
            raise ValueError('UNSUPPORTED_CRS')
        exterior, interiors = [], []
        for boundary in polygon:
            if boundary.tag not in (gml + 'exterior', gml + 'interior'):
                raise ValueError('UNSUPPORTED_BOUNDARY')
            if len(boundary) != 1 or boundary[0].tag != gml + 'LinearRing':
                raise ValueError('UNSUPPORTED_RING')
            ring = boundary[0]
            if len(ring) != 1 or ring[0].tag != gml + 'posList' or ring[0].get('srsDimension') != '2':
                raise ValueError('UNSUPPORTED_COORDINATES')
            values = [float(v) for v in (ring[0].text or '').split()]
            if len(values) < 8 or len(values) % 2 or not all(math.isfinite(v) for v in values):
                raise ValueError('INVALID_COORDINATES')
            points = [(values[i + 1], values[i]) for i in range(0, len(values), 2)]
            if any(not (-180 <= lon <= 180 and -90 <= lat <= 90) for lon, lat in points) or points[0] != points[-1]:
                raise ValueError('INVALID_RING')
            (exterior if boundary.tag == gml + 'exterior' else interiors).append(points)
        if len(exterior) != 1:
            raise ValueError('INVALID_EXTERIOR_COUNT')
        shape = Polygon(exterior[0], interiors)
        if shape.is_empty or not shape.is_valid or shape.area <= 0:
            raise ValueError('INVALID_GEOMETRY')
        features.append({'type': 'Feature', 'id': parcel.findtext(ms + 'ID_DZIALKI'),
                         'geometry': mapping(shape), 'properties': {
                             'registration_group': int(group_text) if group_text else None,
                             'source_date_raw': (parcel.findtext(ms + 'DATA') or '').strip() or None,
                             'classification': 'REPORTED', 'ownership_category': None,
                             'source_crs': 'urn:ogc:def:crs:EPSG::4326',
                             'geometry_conversion': 'GML_lat_lon_to_GeoJSON_lon_lat'}})
    return {'type': 'FeatureCollection', 'features': features, 'probe_summary': summary}
