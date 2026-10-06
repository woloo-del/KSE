import sqlite3
import struct
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from shapely.geometry import box
from connectors.gis.county_package import inspect_parcels, select_parcels


class CountyPackageTests(unittest.TestCase):
    def fixture(self, directory, rows, crs=2180):
        path = Path(directory) / 'synthetic.gpkg'
        with closing(sqlite3.connect(path)) as db:
            db.executescript('CREATE TABLE gpkg_geometry_columns(table_name,column_name,srs_id); CREATE TABLE gpkg_contents(table_name,last_change); CREATE TABLE dzialki(id_dzialki,grupa_rejestrowa,data,czas_pozyskania,geometry);')
            db.execute('INSERT INTO gpkg_geometry_columns VALUES(?,?,?)', ('dzialki','geometry',crs))
            db.execute('INSERT INTO gpkg_contents VALUES(?,?)', ('dzialki','synthetic'))
            db.executemany('INSERT INTO dzialki VALUES(?,?,?,?,?)', rows)
            db.commit()
        return path

    def test_counts_unknown_duplicates_and_geometry_errors(self):
        blob = b'GP\x00\x01' + struct.pack('<i',2180) + box(1,1,2,2).wkb
        with tempfile.TemporaryDirectory() as directory:
            result = inspect_parcels(self.fixture(directory, [('synthetic-a',7,None,'test',blob),('synthetic-a',None,None,'test',blob),('synthetic-b',99,None,'test',b'bad')]))
        self.assertEqual(result['duplicate_id_count'],1)
        self.assertEqual(result['registration_group_counts'],{'7':1,'UNKNOWN':1})
        self.assertEqual(result['errors']['INVALID_GROUP'],1)
        self.assertEqual(result['errors']['GEOMETRY_DECODE_ValueError'],1)
        self.assertIsNone(result['ownership_area_percent'])

    def test_wrong_crs_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError,'CRS'):
                inspect_parcels(self.fixture(directory, [],4326))

    def test_selection_excludes_outside_and_boundary_touch(self):
        def blob(geometry):
            return b'GP\x00\x01' + struct.pack('<i',2180) + geometry.wkb
        with tempfile.TemporaryDirectory() as directory:
            path = self.fixture(directory, [('inside',7,None,'test',blob(box(1,1,2,2))),
                                            ('touch',7,None,'test',blob(box(3,1,4,2))),
                                            ('outside',7,None,'test',blob(box(10,10,11,11)))])
            selected, audit = select_parcels(path,buffer=box(0,0,3,3),source_id='synthetic')
        self.assertEqual([p.parcel_id for p in selected],['inside'])
        self.assertEqual(audit['record_count'],3)
        self.assertEqual(selected[0].source_id,'synthetic')

    def test_selection_rejects_bad_package_instead_of_partial_output(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.fixture(directory,[('bad',7,None,'test',b'bad')])
            with self.assertRaisesRegex(ValueError,'PACKAGE_REQUIRES_REVIEW'):
                select_parcels(path,buffer=box(0,0,3,3),source_id='synthetic')

    def test_preserved_source(self):
        path = Path('data/staging/research/grudziadz_parcels_2026-10-06.gpkg')
        if not path.exists(): self.skipTest('Run audit_county_export after archive restore')
        result = inspect_parcels(path)
        self.assertEqual(result['record_count'],24230)
        self.assertEqual(result['unique_nonempty_ids'],24230)
        self.assertEqual(result['errors'],{})
        self.assertEqual(sum(result['registration_group_counts'].values()),24230)
