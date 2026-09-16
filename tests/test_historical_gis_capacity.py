"""Synthetic attributes only."""
import unittest
from connectors.gis.historical_capacity import parse_mw, capacity_observations


class HistoricalGisCapacityTests(unittest.TestCase):
    def test_zero_is_not_missing(self):
        self.assertEqual(parse_mw('0MW'),(0.0,'REPORTED'))
        self.assertEqual(parse_mw('-MW'),(None,'UNKNOWN'))
        self.assertEqual(parse_mw(None),(None,'UNKNOWN'))
        self.assertEqual(parse_mw('N/D'),(None,'UNKNOWN'))
        self.assertEqual(parse_mw('18,7 MW'),(18.7,'REPORTED'))

    def test_invalid_units_and_nonfinite_values_rejected(self):
        for raw in ['100kW','NaN MW','infMW','-2MW','1,2,3MW',100]:
            with self.assertRaises(ValueError): parse_mw(raw)

    def test_group_not_assigned_to_station_or_current_year(self):
        rows,errors=capacity_observations({'Name':'SYNTHETIC','Group':'GROUP A','Free Capacities of Group - 2026':'20MW'})
        self.assertFalse(errors)
        self.assertEqual(rows[0]['scope_type'],'GROUP')
        self.assertFalse(rows[0]['current_capacity_eligible'])
        self.assertFalse(rows[0]['summation_eligible'])
        self.assertEqual(rows[0]['direction'],'UNKNOWN')
        self.assertIsNone(rows[0]['source_date'])

    def test_voltage_specific_city_district(self):
        rows,errors=capacity_observations({'City District':'SYNTHETIC','Free Capacities of City District (15kV) - 2029':'2MW','Free Capacities of City District (110kV) - 2029':'2MW'})
        self.assertFalse(errors)
        self.assertEqual([r['voltage_kv'] for r in rows],[15,110])

    def test_unidentified_area_is_not_municipality(self):
        rows,errors=capacity_observations({'Commune':'SYNTHETIC','Free Capacities of Area - 2024':'0MW'})
        self.assertIsNone(rows[0]['scope_name'])

    def test_unknown_column_and_bad_value_remain_errors(self):
        rows,errors=capacity_observations({'Free Capacities renamed':'1MW','Free Capacities - 2024':'1kW'})
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['validation_status'],'REVIEW_REQUIRED')
        self.assertIsNone(rows[0]['value'])
        self.assertEqual(len(errors),2)

    def test_compound_value_never_becomes_sum_or_direction(self):
        rows,errors=capacity_observations({'Group':'SYNTHETIC','Free Capacities of Group - 2024':'15/25MW'})
        self.assertIsNone(rows[0]['value'])
        self.assertEqual(rows[0]['raw_value'],'15/25MW')
        self.assertEqual(rows[0]['classification'],'UNKNOWN')
        self.assertEqual(len(errors),1)


if __name__=='__main__': unittest.main()
