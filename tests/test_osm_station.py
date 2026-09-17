import unittest

from connectors.gis.osm_station import audit, voltage_kv


def fixture():
    # Synthetic coordinates and IDs; square station and two transformers.
    return b'''<osm><node id="1" lat="1" lon="1"/><node id="2" lat="1" lon="2"/>
    <node id="3" lat="2" lon="2"/><node id="4" lat="2" lon="1"/>
    <node id="5" lat="1.5" lon="1.5" version="1" timestamp="2024-01-01T00:00:00Z"><tag k="power" v="transformer"/></node>
    <node id="6" lat="3" lon="3" version="1" timestamp="2024-01-01T00:00:00Z"><tag k="power" v="transformer"/></node>
    <way id="10" version="1" timestamp="2024-01-01T00:00:00Z"><nd ref="1"/><nd ref="2"/><nd ref="3"/><nd ref="4"/><nd ref="1"/>
    <tag k="power" v="substation"/><tag k="operator" v="Synthetic operator"/></way></osm>'''


class OsmStationTests(unittest.TestCase):
    def test_units_and_multivoltage_not_summed(self):
        self.assertEqual(voltage_kv('220000;110000;15000'), [220, 110, 15])
        for value in [None, '110 kV', '110000/220000', '0', 'unknown']:
            self.assertIsNone(voltage_kv(value))

    def test_outside_response_node_not_station_equipment(self):
        result = audit(fixture(), 10)
        self.assertEqual(result['summary']['returned_power_elements'], 3)
        self.assertEqual(result['summary']['selected_power_tags']['transformer'], 1)
        self.assertTrue(all(r['equipment_owner'] is None for r in result['records']))
        self.assertFalse(result['power_flow_ready'])

    def test_missing_geometry_is_not_silently_closed(self):
        with self.assertRaisesRegex(ValueError, 'MISSING_WAY_NODE'):
            audit(fixture().replace(b'<nd ref="4"/>', b'<nd ref="99"/>'), 10)

    def test_unclosed_polygon_rejected(self):
        with self.assertRaisesRegex(ValueError, 'NOT_CLOSED'):
            audit(fixture().replace(b'<nd ref="4"/><nd ref="1"/>', b'<nd ref="4"/>'), 10)

    def test_html_and_entity_declarations_rejected(self):
        for data in [b'<html/>', b'<!DOCTYPE osm><osm/>']:
            with self.assertRaises(ValueError):
                audit(data, 10)

    def test_duplicate_id_and_invalid_coordinate_rejected(self):
        duplicate = fixture().replace(b'<osm>', b'<osm><node id="1" lat="1" lon="1"/>')
        with self.assertRaisesRegex(ValueError, 'IDENTITIES'):
            audit(duplicate, 10)
        with self.assertRaisesRegex(ValueError, 'COORDINATES'):
            audit(fixture().replace(b'lat="1.5"', b'lat="nan"'), 10)


if __name__ == '__main__':
    unittest.main()
