import hashlib
import json
from pathlib import Path
import unittest
from urllib.parse import urlencode

from shapely.geometry import Point

from connectors.gis.ownership_snapshot import prepare_snapshot
from gis.coordinates import PolishMetricProjection
from tests.test_ownership_normalization import synthetic


def source(raw, bbox='52,17,55,20,urn:ogc:def:crs:EPSG::4326', **extra):
    params = dict(SERVICE='WFS', VERSION='2.0.0', REQUEST='GetFeature', TYPENAMES='ms:dzialki',
                  SRSNAME='urn:ogc:def:crs:EPSG::4326', COUNT=3, BBOX=bbox)
    params.update(extra)
    return {'source_id': 'synthetic-wfs', 'url': 'https://example.invalid/wfs?' + urlencode(params),
            'retrieval_date': '2026-09-19', 'sha256': hashlib.sha256(raw).hexdigest()}


def prepare(raw, manifest=None):
    return prepare_snapshot(raw, source=manifest or source(raw), longitude=18.5, latitude=53.5,
                            center_source_id='synthetic-center', center_source={
                                'locator': 'synthetic:test-point', 'sha256': '0' * 64, 'retrieval_date': '2026-09-19'})


class OwnershipSnapshotTests(unittest.TestCase):
    def test_projection_axes_and_roundtrip(self):
        projection = PolishMetricProjection()
        projected = projection.project(Point(19, 52))
        self.assertAlmostEqual(projected.x, 500000, places=5)  # CRS central meridian / false easting.
        self.assertTrue(450000 < projected.y < 470000)
        restored = projection.geographic(projected)
        self.assertAlmostEqual(restored.x, 19, places=8)
        self.assertAlmostEqual(restored.y, 52, places=8)
        for point in [Point(52, 19), Point(0, 0), Point(19, 52, 0)]:
            with self.assertRaises(ValueError):
                projection.project(point)

    def test_complete_single_response_flows_into_area(self):
        raw = synthetic().replace(b'numberReturned="1"', b'numberReturned="1" numberMatched="1"')
        result = prepare(raw)
        self.assertEqual(result['status'], 'SINGLE_RESPONSE_READY_FOR_REVIEW')
        self.assertAlmostEqual(result['area_result']['groups']['7']['percent_of_buffer'], 100)
        self.assertEqual(result['center']['role'], 'RESEARCH_POINT_NOT_VERIFIED_STATION')

    def test_small_bbox_suppresses_area_even_with_all_records(self):
        raw = synthetic().replace(b'numberReturned="1"', b'numberReturned="1" numberMatched="1"')
        result = prepare(raw, source(raw, bbox='53.499,18.499,53.501,18.501,urn:ogc:def:crs:EPSG::4326'))
        self.assertIn('REQUEST_BBOX_DOES_NOT_COVER_BUFFER', result['blocking_reasons'])
        self.assertIsNone(result['area_result'])

    def test_unknown_truncated_or_next_suppress_area(self):
        for attributes, expected in [(b'numberMatched="unknown"', 'MATCHED_COUNT_UNKNOWN'),
                                     (b'numberMatched="2"', 'RESPONSE_NOT_COMPLETE'),
                                     (b'numberMatched="1" next="https://example.invalid/next"', 'MORE_PAGES_DECLARED')]:
            raw = synthetic().replace(b'numberReturned="1"', b'numberReturned="1" ' + attributes)
            result = prepare(raw)
            self.assertIn(expected, result['blocking_reasons'])
            self.assertIsNone(result['area_result'])

    def test_hash_and_filtered_request_rejected(self):
        raw = synthetic()
        manifest = source(raw); manifest['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'SOURCE_HASH_MISMATCH'):
            prepare(raw, manifest)
        for manifest in [source(raw, FILTER='private-only'), source(raw, STARTINDEX=2), source(raw, RESULTTYPE='hits')]:
            with self.assertRaises(ValueError):
                prepare(raw, manifest)

    def test_real_sample_does_not_become_1km_report(self):
        manifest_path = Path('data/catalog/probe_results_ownership_comparison_2026-09-19.json')
        rows = json.loads(manifest_path.read_text(encoding='utf-8'))
        manifest = next(row for row in rows if row['source_id'].endswith('_WFS'))
        path = Path(manifest['local_path'])
        if not path.exists():
            self.skipTest('Restore ownership comparison archive')
        result = prepare_snapshot(path.read_bytes(), source=manifest, longitude=18.76, latitude=53.48,
                                  center_source_id='query-point', center_source={
                                      'locator': manifest['url'], 'sha256': manifest['sha256'],
                                      'retrieval_date': manifest['retrieval_date']})
        self.assertEqual(result['returned_parcels'], 2)
        self.assertEqual(result['blocking_reasons'], ['REQUEST_BBOX_DOES_NOT_COVER_BUFFER'])
        self.assertIsNone(result['area_result'])
