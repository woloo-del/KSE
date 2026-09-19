import unittest
from pathlib import Path
from connectors.gis.ownership_probe import inspect_sample


class OwnershipProbeTests(unittest.TestCase):
    def test_missing_empty_and_populated_are_distinct_without_classification(self):
        xml = '''<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:ms="http://mapserver.gis.umn.edu/mapserver" numberReturned="3">'''
        for i, field in enumerate(['', '<ms:GRUPA_REJESTROWA/>', '<ms:GRUPA_REJESTROWA>7</ms:GRUPA_REJESTROWA>']):
            xml += f'<wfs:member><ms:dzialki><ms:ID_DZIALKI>synthetic-{i}</ms:ID_DZIALKI>{field}</ms:dzialki></wfs:member>'
        result = inspect_sample((xml + '</wfs:FeatureCollection>').encode())
        self.assertEqual(result['registration_group_field'], {'missing': 1, 'empty': 1, 'populated': 1})
        self.assertIsNone(result['ownership_area_percent'])

    def test_error_and_truncated_count_fail(self):
        for raw in [b'<ExceptionReport/>', b'<FeatureCollection xmlns="http://www.opengis.net/wfs/2.0" numberReturned="2"/>']:
            with self.assertRaises(ValueError):
                inspect_sample(raw)

    def test_preserved_station_sample(self):
        path = Path(__file__).resolve().parents[1] / 'data/raw/research/2026-09-19/gugik_radkowice_station_sample.gml'
        if not path.exists():
            self.skipTest('Restore the checksummed source archive first')
        result = inspect_sample(path.read_bytes())
        self.assertEqual(result['returned_parcels'], 1)
        self.assertEqual(result['registration_group_field']['empty'], 1)
