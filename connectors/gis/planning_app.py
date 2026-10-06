"""Narrow APP 1.0 reader: plan extent only, never land-use zones or station identity."""
import math
import xml.etree.ElementTree as ET

from pyproj import Transformer, network
from shapely.geometry import MultiPolygon, Polygon

NS = {'wfs': 'http://www.opengis.net/wfs/2.0',
      'app': 'https://www.gov.pl/static/zagospodarowanieprzestrzenne/schemas/app/1.0',
      'gml': 'http://www.opengis.net/gml/3.2'}
XLINK = '{http://www.w3.org/1999/xlink}'
CRS = 'http://www.opengis.net/def/crs/EPSG/0/2177'


def read_plan_extent(raw: bytes) -> tuple[dict, MultiPolygon]:
    if len(raw) > 5_000_000 or b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ValueError('UNSUPPORTED_XML')
    root = ET.fromstring(raw)
    if root.tag != '{' + NS['wfs'] + '}FeatureCollection':
        raise ValueError('NOT_FEATURE_COLLECTION')
    members = root.findall('wfs:member', NS)
    if root.get('numberReturned') != str(len(members)):
        raise ValueError('MEMBER_COUNT_MISMATCH')
    plans = root.findall('wfs:member/app:AktPlanowaniaPrzestrzennego', NS)
    if len(plans) != 1:
        raise ValueError('EXPECTED_SINGLE_PLAN')
    plan = plans[0]
    identifier = plan.findtext('gml:identifier', namespaces=NS)
    title = plan.findtext('app:tytul', namespaces=NS)
    if not identifier or not title:
        raise ValueError('MISSING_PLAN_IDENTITY')
    surfaces = plan.findall('app:zasiegPrzestrzenny/gml:MultiSurface', NS)
    if len(surfaces) != 1 or surfaces[0].get('srsName') != CRS or surfaces[0].get('srsDimension') != '2':
        raise ValueError('UNSUPPORTED_GEOMETRY_OR_CRS')
    for element in surfaces[0].iter():
        if element.get('srsName', CRS) != CRS or element.get('srsDimension', '2') != '2':
            raise ValueError('CONFLICTING_NESTED_CRS_OR_DIMENSION')
    if network.is_network_enabled():
        raise ValueError('PROJ_NETWORK_MUST_BE_DISABLED')
    # EPSG:2177 GML uses northing/easting. EPSG:2180 output is also northing/easting.
    transform = Transformer.from_crs(2177, 2180, always_xy=False, allow_ballpark=False, only_best=True)

    def ring(element):
        if element is None or len(element) != 1 or element[0].tag != '{' + NS['gml'] + '}LinearRing':
            raise ValueError('UNSUPPORTED_RING')
        children = list(element[0])
        if len(children) != 1 or children[0].tag != '{' + NS['gml'] + '}posList':
            raise ValueError('UNSUPPORTED_COORDINATES')
        values = [float(v) for v in (children[0].text or '').split()]
        if len(values) < 8 or len(values) % 2 or not all(math.isfinite(v) for v in values):
            raise ValueError('INVALID_COORDINATES')
        pairs = list(zip(values[::2], values[1::2]))
        if pairs[0] != pairs[-1]:
            raise ValueError('UNCLOSED_RING')
        points = []
        for north, east in pairs:
            if not (5_000_000 < north < 6_500_000 and 6_000_000 < east < 7_000_000):
                raise ValueError('AXIS_OR_COORDINATE_RANGE')
            y, x = transform.transform(north, east, errcheck=True)
            points.append((x, y))
        return points

    polygons = []
    for member in surfaces[0]:
        if member.tag != '{' + NS['gml'] + '}surfaceMember' or len(member) != 1:
            raise ValueError('UNSUPPORTED_SURFACE')
        polygon = member[0]
        if polygon.tag != '{' + NS['gml'] + '}Polygon' or len(polygon.findall('gml:exterior', NS)) != 1:
            raise ValueError('UNSUPPORTED_POLYGON')
        if any(e.tag not in {'{' + NS['gml'] + '}exterior', '{' + NS['gml'] + '}interior'} for e in polygon):
            raise ValueError('UNSUPPORTED_POLYGON_CHILD')
        polygons.append(Polygon(ring(polygon.find('gml:exterior', NS)),
                                [ring(e) for e in polygon.findall('gml:interior', NS)]))
    geometry = MultiPolygon(polygons)
    if geometry.is_empty or not geometry.is_valid:
        raise ValueError('INVALID_PLAN_GEOMETRY')
    status = plan.find('app:status', NS)
    return {'method_version': 'app_plan_extent_v1', 'plan_id': identifier, 'title': title,
            'source_crs': 'EPSG:2177', 'output_crs': 'EPSG:2180',
            'effective_from_reported': plan.findtext('app:obowiazujeOd', namespaces=NS),
            'source_timestamp': root.get('timeStamp'),
            'status_reported': status.get(XLINK + 'href') if status is not None else None,
            'scope': 'WHOLE_PLAN_EXTENT_NOT_LAND_USE_ZONE',
            'signature_validation': 'NOT_PERFORMED',
            'current_legal_status': 'NOT_VERIFIED'}, geometry
