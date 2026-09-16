"""Synthetic SQLite fixtures only; private source contents are not test fixtures."""
import hashlib
from pathlib import Path
import sqlite3
import tempfile
import unittest

from scripts.inspect_private_materials import inspect, inspect_gpkg


class PrivateInspectionTests(unittest.TestCase):
    def test_readonly_gpkg_inspection_and_quality_warnings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'synthetic.gpkg'
            with sqlite3.connect(path) as db:
                db.executescript('''
                    CREATE TABLE gpkg_spatial_ref_sys(srs_id INTEGER);
                    INSERT INTO gpkg_spatial_ref_sys VALUES(4326);
                    CREATE TABLE gpkg_contents(table_name TEXT,srs_id INTEGER);
                    INSERT INTO gpkg_contents VALUES('test layer',4326);
                    CREATE TABLE gpkg_geometry_columns(table_name TEXT,column_name TEXT);
                    INSERT INTO gpkg_geometry_columns VALUES('test layer','geom');
                    CREATE TABLE "test layer"(fid INTEGER,geom BLOB,Name TEXT,xcoord REAL,ycoord REAL);
                    INSERT INTO "test layer" VALUES(1,x'00','SYNTHETIC',20,51);
                    INSERT INTO "test layer" VALUES(2,NULL,'SYNTHETIC',200,51);
                ''')
            db.close()
            before = hashlib.sha256(path.read_bytes()).hexdigest()
            result = inspect_gpkg(path)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), before)
            self.assertEqual(result['integrity'], 'ok')
            layer = result['layers'][0]
            self.assertEqual(layer['count'], 2)
            self.assertEqual(layer['null_geometry_count'], 1)
            self.assertEqual(layer['invalid_attribute_coordinate_count'], 1)
            self.assertEqual(layer['duplicate_names'], {'SYNTHETIC': 2})
            self.assertNotIn('geom',layer['sample_attributes'][0])

    def test_inspection_refuses_output_outside_private(self):
        with self.assertRaises(ValueError):
            inspect(Path('data/private'),Path('data/public-review'))

    def test_inspection_refuses_output_inside_input(self):
        with self.assertRaises(ValueError):
            inspect(Path('data/private'),Path('data/private/review-invalid'))
