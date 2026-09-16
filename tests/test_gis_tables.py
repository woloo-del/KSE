"""Synthetic attribute rows, no private fixtures."""
from types import SimpleNamespace
from pathlib import Path
import unittest
from unittest.mock import Mock, patch
from scripts.compare_private_gis_tables import compare_rows, normalized, read_table, WPZP_HEADERS, WPZP_FIELDS


class GisTableTests(unittest.TestCase):
    def test_order_independent_with_duplicate_multiplicity(self):
        features=[SimpleNamespace(fid=1,properties={'Name':'A'}),SimpleNamespace(fid=2,properties={'Name':'B'})]
        rows=[{'row':2,'values':['B']},{'row':3,'values':['A']},{'row':4,'values':['A']}]
        result=compare_rows(['Name'],rows,features)
        self.assertEqual([m['gpkg_fid'] for m in result['matches']],[2,1])
        self.assertEqual(result['unmatched_xlsx_rows'][0]['row'],4)

    def test_missing_column_is_schema_error(self):
        with self.assertRaisesRegex(ValueError,'SCHEMA'):
            compare_rows(['Name'],[],[SimpleNamespace(fid=1,properties={})])

    def test_only_boundary_whitespace_and_line_endings_normalized(self):
        self.assertEqual(normalized(' A\r\nB '),'A\nB')
        self.assertNotEqual(normalized('A  B'),normalized('A B'))
        self.assertIsNone(normalized(None))
        self.assertEqual(normalized(2024),'2024')

    def test_changed_value_preserves_both_records(self):
        result=compare_rows(['Name'],[{'row':2,'values':['A']}],[SimpleNamespace(fid=1,properties={'Name':'B'})])
        self.assertFalse(result['matches'])
        self.assertEqual(result['unmatched_gpkg_rows'][0]['values'],['B'])

    def workbook(self, rows):
        sheet=Mock()
        sheet.iter_rows.return_value=iter(rows)
        return Mock(worksheets=[sheet])

    def test_duplicate_wpzp_display_header_uses_verified_positions(self):
        book=self.workbook([[None,*WPZP_HEADERS],[None,*range(11)]])
        with patch('scripts.compare_private_gis_tables.load_workbook',return_value=book):
            fields,rows=read_table(Path('synthetic - WPZP.xlsx'))
        self.assertEqual(fields,WPZP_FIELDS)
        self.assertEqual(fields[3],'W-PZP')
        self.assertEqual(fields[8],'Voivodship')
        book.close.assert_called_once()

    def test_schema_change_is_not_silent_column_shift(self):
        book=self.workbook([[None,'Unknown']])
        with patch('scripts.compare_private_gis_tables.load_workbook',return_value=book):
            with self.assertRaisesRegex(ValueError,'SCHEMA'):
                read_table(Path('synthetic - WPZP.xlsx'))
        book.close.assert_called_once()

    def test_formula_rejected_without_using_stale_cached_result(self):
        book=self.workbook([[None,'Name'],[None,'=1+1']])
        with patch('scripts.compare_private_gis_tables.load_workbook',return_value=book) as loader:
            with self.assertRaisesRegex(ValueError,'FORMULA'):
                read_table(Path('synthetic.xlsx'))
        self.assertFalse(loader.call_args.kwargs['data_only'])
        book.close.assert_called_once()


if __name__=='__main__': unittest.main()
