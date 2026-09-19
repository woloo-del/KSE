import unittest
from pathlib import Path
from connectors.gis.ownership_map import inspect_county


def fixture():
    fields = {'TERYT': '0000', 'Nazwa jednostki': 'SYNTHETIC', 'Liczba działek': '10',
              'Liczba duplikatów (działek)': '0', 'b.d. – brak danych o grupie': '10',
              'Data ostatniej aktualizacji': 'synthetic date'}
    fields.update({f'{i} - synthetic group': '0' for i in range(1, 17)})
    return ''.join(f'<li><span class="list-item-value">{k}</span>{v}</li>' for k, v in fields.items()).encode()


class OwnershipMapTests(unittest.TestCase):
    def test_missing_is_not_private_or_area(self):
        result = inspect_county(fixture())
        self.assertEqual(result['availability'], 'NO_GROUP_VALUES_IN_SNAPSHOT')
        self.assertIsNone(result['ownership_area_percent'])

    def test_partial_requires_local_check(self):
        raw = fixture()
        raw = raw.replace(b'1 - synthetic group</span>0', b'1 - synthetic group</span>1', 1)
        raw = raw.replace('b.d. – brak danych o grupie</span>10'.encode(), 'b.d. – brak danych o grupie</span>9'.encode())
        self.assertEqual(inspect_county(raw)['availability'], 'REQUIRES_LOCAL_COVERAGE_CHECK')

    def test_changed_schema_and_counts_fail(self):
        for raw in [b'<ExceptionReport/>', fixture().replace(b'Liczba dzia', b'Changed dzia'),
                    fixture().replace(b'16 - synthetic group', b'17 - synthetic group'),
                    fixture().replace(b'</span>10', b'</span>11', 1)]:
            with self.assertRaises((ValueError, KeyError)):
                inspect_county(raw)

    def test_archived_primary_source(self):
        path = Path('data/raw/research/2026-09-19/ownership_map_county_html.html')
        if not path.exists():
            self.skipTest('Restore ownership map archive')
        result = inspect_county(path.read_bytes())
        self.assertEqual((result['teryt'], result['parcel_count'], result['missing_group_count']), ('2604', 264634, 264634))
