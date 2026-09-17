"""Synthetic group labels and capacities only."""
import unittest
from connectors.gis.compound_groups import candidate_components,compare_peer_values


class CompoundGroupTests(unittest.TestCase):
    def test_numbered_order_and_zero_preserved(self):
        result=candidate_components('B/A','(1) Grupa B: station / (2) Grupa A: station','0/12,5MW')
        self.assertEqual([(x['group_name'],x['candidate_value_MW']) for x in result],[('B',0),('A',12.5)])
        self.assertTrue(all(x['association_classification']=='INFERRED' and not x['summation_eligible'] for x in result))

    def test_reordered_description_rejected(self):
        with self.assertRaisesRegex(ValueError,'ORDER'):
            candidate_components('A/B','(1) Grupa B: s / (2) Grupa A: s','1/2MW')

    def test_count_units_missing_and_duplicate_groups_rejected(self):
        for group,raw in [('A/B','1MW'),('A/B','1/2kW'),('A/B','-/2MW'),('A/A','1/2MW')]:
            with self.assertRaises(ValueError): candidate_components(group,'(1) Grupa A: s / (2) Grupa B: s',raw)

    def test_peer_disagreement_cannot_be_majority_vote(self):
        self.assertEqual(compare_peer_values(5,[{'value':5},{'value':5},{'value':10}]),'CONFLICT')
        self.assertEqual(compare_peer_values(5,[{'value':None}]),'NO_NUMERIC_REFERENCE')
        self.assertEqual(compare_peer_values(5,[{'value':5},{'value':None}]),'CONSISTENT_KNOWN_VALUES_WITH_GAPS')
        self.assertEqual(compare_peer_values(0,[{'value':0}]),'CONSISTENT_WITHIN_COMPILATION')
