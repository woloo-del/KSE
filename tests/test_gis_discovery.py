import unittest

from connectors.gis.discovery import discover


class GisDiscoveryTests(unittest.TestCase):
    def test_group_match_is_not_asset_name_or_electrical_edge(self):
        matches = discover({'Name': 'Synthetic A', 'Group': 'Synthetic B'}, 'synthetic b')
        self.assertEqual([m['match_kind'] for m in matches], ['EXACT_GROUP_LABEL'])
        self.assertEqual(matches[0]['electrical_relationship'], 'UNKNOWN')

    def test_group_name_substring_does_not_merge_different_groups(self):
        self.assertEqual(discover({'Group': 'Synthetic B East'}, 'Synthetic B'), [])

    def test_compound_group_retains_ambiguity_and_raw_value(self):
        matches = discover({'Group': ' Synthetic A / Synthetic B '}, 'synthetic b')
        self.assertEqual(matches[0]['match_kind'], 'COMPOUND_GROUP_COMPONENT')
        self.assertEqual(matches[0]['raw_value'], ' Synthetic A / Synthetic B ')

    def test_task_mention_is_not_station_identity(self):
        matches = discover({'Nazwa zadania inwestycyjnego': 'Connection from Synthetic A to B'}, 'Synthetic A')
        self.assertEqual(matches[0]['match_kind'], 'TASK_MENTION')

    def test_empty_query_rejected_and_nontext_ignored(self):
        with self.assertRaises(ValueError):
            discover({}, ' ')
        self.assertEqual(discover({'Name': None, 'Group': 42}, 'Synthetic'), [])


if __name__ == '__main__':
    unittest.main()
