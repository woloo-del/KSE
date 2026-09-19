"""Inspect a bounded WFS sample; never equate an empty ownership field with private land."""
import xml.etree.ElementTree as ET


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
