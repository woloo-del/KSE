import unittest
from pathlib import Path

from connectors.gis.ownership_probe import normalize_sample
from connectors.gis.ownership_map import inspect_parcel


def synthetic(group='7', coords='53 18 53 19 54 19 54 18 53 18'):
    return f'''<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
      xmlns:ms="http://mapserver.gis.umn.edu/mapserver" xmlns:gml="http://www.opengis.net/gml/3.2" numberReturned="1">
      <wfs:member><ms:dzialki><ms:ID_DZIALKI>synthetic</ms:ID_DZIALKI><ms:GRUPA_REJESTROWA>{group}</ms:GRUPA_REJESTROWA><ms:DATA/>
      <ms:geom><gml:Polygon srsName="urn:ogc:def:crs:EPSG::4326"><gml:exterior><gml:LinearRing>
      <gml:posList srsDimension="2">{coords}</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></ms:geom>
      </ms:dzialki></wfs:member></wfs:FeatureCollection>'''.encode()


class OwnershipNormalizationTests(unittest.TestCase):
    def test_axis_order_and_missing_date(self):
        feature = normalize_sample(synthetic())['features'][0]
        self.assertEqual(feature['geometry']['coordinates'][0][0], (18, 53))
        self.assertEqual(feature['properties']['registration_group'], 7)
        self.assertIsNone(feature['properties']['source_date_raw'])
        self.assertIsNone(feature['properties']['ownership_category'])

    def test_unknown_and_company_are_not_private(self):
        for group in ['', '15']:
            props = normalize_sample(synthetic(group))['features'][0]['properties']
            self.assertEqual(props['registration_group'], int(group) if group else None)
            self.assertIsNone(props['ownership_category'])

    def test_unsupported_values_fail(self):
        for raw in [synthetic('17'), synthetic('0'), synthetic('7').replace(b'EPSG::4326', b'EPSG::2180'),
                    synthetic(coords='53 18 54 19 53 19 54 18 53 18'),
                    synthetic(coords='53 18 53 19 54 19 54 18'),
                    synthetic(coords='nan 18 53 19 54 19 54 18 nan 18'),
                    synthetic().replace(b'srsDimension="2"', b'srsDimension="3"')]:
            with self.assertRaises(ValueError):
                normalize_sample(raw)

    def test_holes_preserved_and_duplicate_fields_rejected(self):
        hole = b'<gml:interior><gml:LinearRing><gml:posList srsDimension="2">53.2 18.2 53.4 18.2 53.4 18.4 53.2 18.4 53.2 18.2</gml:posList></gml:LinearRing></gml:interior>'
        raw = synthetic().replace(b'</gml:Polygon>', hole + b'</gml:Polygon>')
        self.assertEqual(len(normalize_sample(raw)['features'][0]['geometry']['coordinates']), 2)
        duplicate = synthetic().replace(b'<ms:DATA/>', b'<ms:DATA/><ms:GRUPA_REJESTROWA>9</ms:GRUPA_REJESTROWA>')
        with self.assertRaises(ValueError):
            normalize_sample(duplicate)

    def test_html_read_without_execution_and_reject_ambiguity(self):
        raw = b'000000_0.0000.1 const groupid = 0; const fetchdt = new Date("synthetic"); throw Error("do not execute");'
        self.assertIsNone(inspect_parcel(raw)['registration_group'])
        for extra in [b' const groupid = 7;', b' 000000_0.0000.2']:
            with self.assertRaises(ValueError):
                inspect_parcel(raw + extra)

    def test_real_cross_source_id_and_group(self):
        root = Path('data/raw/research/2026-09-19')
        if not (root / 'ownership_grudziadz_wfs.gml').exists():
            self.skipTest('Restore ownership comparison archive')
        features = normalize_sample((root / 'ownership_grudziadz_wfs.gml').read_bytes())['features']
        parcel = inspect_parcel((root / 'ownership_grudziadz_parcel.html').read_bytes())
        match = [f for f in features if f['id'] == parcel['parcel_id']]
        self.assertEqual(len(match), 1)
        self.assertEqual(match[0]['properties']['registration_group'], parcel['registration_group'])
        self.assertEqual(parcel['registration_group'], 7)
