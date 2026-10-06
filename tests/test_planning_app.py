from pathlib import Path
import unittest
from pyproj import Transformer
from shapely.geometry import Point
from connectors.gis.planning_app import read_plan_extent


def fixture(coords='5924000 6552000 5924100 6552000 5924100 6552100 5924000 6552000'):
    return f'''<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0" xmlns:app="https://www.gov.pl/static/zagospodarowanieprzestrzenne/schemas/app/1.0" xmlns:gml="http://www.opengis.net/gml/3.2" numberReturned="1"><wfs:member><app:AktPlanowaniaPrzestrzennego><gml:identifier>synthetic</gml:identifier><app:tytul>Synthetic test only</app:tytul><app:zasiegPrzestrzenny><gml:MultiSurface srsDimension="2" srsName="http://www.opengis.net/def/crs/EPSG/0/2177"><gml:surfaceMember><gml:Polygon><gml:exterior><gml:LinearRing><gml:posList>{coords}</gml:posList></gml:LinearRing></gml:exterior></gml:Polygon></gml:surfaceMember></gml:MultiSurface></app:zasiegPrzestrzenny></app:AktPlanowaniaPrzestrzennego></wfs:member></wfs:FeatureCollection>'''.encode()


class PlanningAppTests(unittest.TestCase):
    def test_axes_match_explicit_easting_northing(self):
        metadata, geometry = read_plan_extent(fixture())
        transform = Transformer.from_crs(2177, 2180, always_xy=True)
        x, y = transform.transform(6552030, 5924070)
        self.assertTrue(geometry.contains(Point(x, y)))
        self.assertEqual(metadata['current_legal_status'], 'NOT_VERIFIED')
        self.assertEqual(metadata['scope'], 'WHOLE_PLAN_EXTENT_NOT_LAND_USE_ZONE')

    def test_swapped_axes_rejected(self):
        with self.assertRaisesRegex(ValueError, 'AXIS'):
            read_plan_extent(fixture('6552000 5924000 6552000 5924100 6552100 5924100 6552000 5924000'))

    def test_open_ring_and_unknown_crs_rejected(self):
        for raw in [fixture('5924000 6552000 5924100 6552000 5924100 6552100 5924001 6552000'),
                    fixture().replace(b'EPSG/0/2177', b'EPSG/0/4326')]:
            with self.assertRaises(ValueError): read_plan_extent(raw)

    def test_entities_rejected(self):
        with self.assertRaisesRegex(ValueError, 'UNSUPPORTED_XML'):
            read_plan_extent(b'<!DOCTYPE test>' + fixture())

    def test_nested_dimension_conflict_rejected(self):
        with self.assertRaisesRegex(ValueError, 'NESTED'):
            read_plan_extent(fixture().replace(b'<gml:posList>', b'<gml:posList srsDimension="3">'))

    def test_preserved_plans(self):
        for name in ('plan97', 'plan79'):
            path = Path(f'data/raw/research/2026-10-06/{name}.gml')
            if not path.exists(): self.skipTest('Restore plan followup archive')
            metadata, geometry = read_plan_extent(path.read_bytes())
            self.assertTrue(geometry.is_valid)
            self.assertEqual(metadata['signature_validation'], 'NOT_PERFORMED')
