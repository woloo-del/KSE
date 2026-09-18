"""Synthetic fixtures ensure lexical candidates never become confirmed stations."""
import unittest
from connectors.gis.station_candidates import candidates, split_station_label


def profile(name='Test', voltage=110):
    return {'profile_id': 'synthetic', 'name_reported': name, 'voltage_kV': voltage}


def station(name='Test 220/110kV', fid=1):
    return {'table': 'synthetic', 'fid': fid, 'name': name}


class CandidateTests(unittest.TestCase):
    def test_suffix_only_and_no_alias_merging(self):
        self.assertEqual(split_station_label(' Test 400 / 110 kV '), ('test', (400, 110)))
        for name in ['Test (planowana)', 'Test Systemowa', 'SE Test', 'Tęst']:
            self.assertEqual(candidates([profile(name)], [station()])[0]['review_status'],
                             'NO_EXACT_NAME_CANDIDATE')

    def test_candidate_is_never_confirmed(self):
        row = candidates([profile(' TEST ')], [station()])[0]
        self.assertEqual(row['review_status'], 'SINGLE_NAME_VOLTAGE_CANDIDATE')
        self.assertFalse(row['identity_confirmed'])
        self.assertIsNone(row['canonical_station_id'])

    def test_voltage_conflict_unknown_and_duplicate_names(self):
        self.assertEqual(candidates([profile(voltage=400)], [station()])[0]['review_status'], 'VOLTAGE_NOT_LISTED')
        self.assertEqual(candidates([profile()], [station('Test')])[0]['review_status'], 'VOLTAGE_UNKNOWN')
        row = candidates([profile()], [station(), station('Test 400kV', 2)])[0]
        self.assertEqual(row['review_status'], 'AMBIGUOUS_NAME')
        self.assertEqual(len(row['candidates']), 2)

    def test_duplicate_locators_and_profiles_fail(self):
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_SOURCE_LOCATOR'):
            candidates([profile()], [station(), station()])
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_PROFILE_ID'):
            candidates([profile(), profile()], [station()])


if __name__ == '__main__':
    unittest.main()
