import copy
import json
from pathlib import Path
import unittest

from scripts.describe_private_wegrowo_land import describe


class LandGroupReviewTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = json.loads(Path('data/reference/registration_group_labels.json').read_text(encoding='utf8'))
        self.result = {'method_version': 'registration_group_buffer_v1', 'access': 'PRIVATE',
                       'ownership_binary_split': None, 'radius_m': 1000, 'crs': 'EPSG:2180',
                       'groups': {str(i): {'area_ha': 0, 'percent_of_buffer': 0} for i in range(1, 17)},
                       'unknown_total': {'area_m2': 1}, 'sources': {}}

    def test_explains_coownership_without_binary_conversion(self):
        original = copy.deepcopy(self.result)
        text = describe(self.result, self.dictionary)
        self.assertIn('przeważającej sumy udziałów', text)
        self.assertIn('Grupa 15 nie rozstrzyga', text)
        self.assertIn('Skarb Państwa — z użytkowaniem wieczystym', text)
        self.assertEqual(self.result, original)

    def test_missing_category_is_not_silently_dropped(self):
        del self.result['groups']['15']
        with self.assertRaisesRegex(ValueError, 'DICTIONARY_MISMATCH'):
            describe(self.result, self.dictionary)

    def test_rejects_public_or_binary_result(self):
        for key, value in [('access', 'PUBLIC'), ('ownership_binary_split', {'private': 100})]:
            with self.subTest(key=key):
                changed = {**self.result, key: value}
                with self.assertRaisesRegex(ValueError, 'UNEXPECTED_SCOPE'):
                    describe(changed, self.dictionary)
