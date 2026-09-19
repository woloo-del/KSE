"""Synthetic geometry tests only: no fabricated station or production records."""
import math
import unittest

from shapely.geometry import Point, Polygon, box

from gis.ownership_area import Parcel, summarize_buffer

CENTER = Point(500000, 500000)
SOURCE = {'synthetic': {'locator': 'synthetic:test-fixture', 'retrieval_date': '2026-09-19', 'sha256': '0' * 64}}


def parcel(identifier, geometry, group=7):
    return Parcel(identifier, geometry, group, 'synthetic')


def calculate(parcels, **kwargs):
    return summarize_buffer(center=CENTER, center_source_id='synthetic', parcels=parcels,
                            sources=SOURCE, crs='EPSG:2180', **kwargs)


class OwnershipAreaTests(unittest.TestCase):
    def test_empty_is_unknown_not_private(self):
        result = calculate([])
        self.assertAlmostEqual(result['unknown_total']['percent_of_buffer'], 100)
        self.assertEqual(result['geometric_coverage']['area_m2'], 0)
        self.assertIsNone(result['ownership_binary_split'])

    def test_full_coverage_and_clipping(self):
        result = calculate([parcel('large', box(498000, 498000, 502000, 502000))])
        self.assertAlmostEqual(result['groups']['7']['percent_of_buffer'], 100)
        self.assertLess(result['groups']['7']['area_m2'], 16000000)
        self.assertLess(abs(result['buffer_area_m2'] - math.pi * 1000**2) / (math.pi * 1000**2), 0.00011)

    def test_half_buffer_missing_geometry(self):
        result = calculate([parcel('half', box(498000, 498000, 500000, 502000), 1)])
        self.assertAlmostEqual(result['groups']['1']['percent_of_buffer'], 50)
        self.assertAlmostEqual(result['unknown_components']['missing_geometry']['percent_of_buffer'], 50)

    def test_touching_boundary_is_not_overlap(self):
        result = calculate([parcel('left', box(498000, 498000, 500000, 502000), 1),
                            parcel('right', box(500000, 498000, 502000, 502000), 7)])
        self.assertAlmostEqual(result['groups']['1']['percent_of_buffer'], 50)
        self.assertAlmostEqual(result['groups']['7']['percent_of_buffer'], 50)
        self.assertEqual(result['overlap_pairs'], [])

    def test_missing_group_is_separate_from_uncovered(self):
        result = calculate([parcel('half', box(498000, 498000, 500000, 502000), None)])
        self.assertAlmostEqual(result['unknown_components']['missing_group']['percent_of_buffer'], 50)
        self.assertAlmostEqual(result['unknown_components']['missing_geometry']['percent_of_buffer'], 50)
        self.assertAlmostEqual(result['unknown_total']['percent_of_buffer'], 100)

    def test_overlap_union_not_sum_and_same_group_still_flagged(self):
        result = calculate([parcel(str(i), box(498000, 498000, 502000, 502000), 7) for i in range(3)])
        self.assertEqual(len(result['overlap_pairs']), 3)
        self.assertAlmostEqual(result['unknown_components']['overlap']['percent_of_buffer'], 100)
        self.assertEqual(result['groups']['7']['area_m2'], 0)

    def test_partial_overlap_removed_from_each_group(self):
        result = calculate([parcel('full', box(498000, 498000, 502000, 502000), 1),
                            parcel('right', box(500000, 498000, 502000, 502000), 7)])
        self.assertAlmostEqual(result['groups']['1']['percent_of_buffer'], 50)
        self.assertEqual(result['groups']['7']['area_m2'], 0)
        self.assertAlmostEqual(result['unknown_total']['percent_of_buffer'], 50)

    def test_hole_and_outside_parcel(self):
        polygon = Polygon(box(498000, 498000, 502000, 502000).exterior.coords,
                          [box(499900, 499900, 500100, 500100).exterior.coords])
        result = calculate([parcel('hole', polygon, 15), parcel('outside', box(510000, 510000, 511000, 511000))])
        self.assertEqual(result['intersecting_parcel_count'], 1)
        self.assertAlmostEqual(result['unknown_components']['missing_geometry']['area_m2'], 40000)
        self.assertIsNone(result['ownership_binary_split'])

    def test_reject_bad_inputs(self):
        valid = parcel('a', box(499000, 499000, 501000, 501000))
        for rows in [[valid, valid], [parcel('x', Point(500000, 500000))],
                     [parcel('x', box(0, 0, 1, 1), True)], [Parcel('x', valid.geometry, 7, 'missing')]]:
            with self.assertRaises(ValueError):
                calculate(rows)
        for radius in [0, -1, float('nan'), float('inf'), True]:
            with self.assertRaises(ValueError):
                calculate([], radius_m=radius)
        with self.assertRaisesRegex(ValueError, 'METRIC_CRS_REQUIRED'):
            summarize_buffer(center=CENTER, center_source_id='synthetic', parcels=[], sources=SOURCE, crs='EPSG:4326')

    def test_reproducible_order_sensitive_to_source(self):
        a = parcel('a', box(498000, 498000, 500000, 502000), 1)
        b = parcel('b', box(500000, 498000, 502000, 502000), 7)
        self.assertEqual(calculate([a, b]), calculate([b, a]))
        changed = Parcel('b', b.geometry, b.registration_group, b.source_id, '2026-09-18')
        self.assertNotEqual(calculate([a, b])['input_fingerprint'], calculate([a, changed])['input_fingerprint'])
