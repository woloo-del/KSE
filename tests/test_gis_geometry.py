"""Synthetic fixtures; never embed user GIS data in tests."""
import struct
import sqlite3
import hashlib
from pathlib import Path
import tempfile
import unittest
import zipfile

import shapely
from shapely.geometry import Point, LineString, MultiLineString
from connectors.gis.geopackage import Feature, decode_geometry, read_features
from scripts.audit_private_gis_geometry import kmz_features, compare_exports


def packet(geom, flags=1, srs=4326, envelope=b''):
    return b'GP\x00'+bytes([flags])+struct.pack('<i' if flags&1 else '>i',srs)+envelope+shapely.to_wkb(geom)


def feature(fid, geom):
    return Feature('synthetic',fid,4326,geom,{},geom.geom_type.upper())


class GeometryTests(unittest.TestCase):
    def test_endianness_and_envelope(self):
        for flags, envelope in [(0,b''),(1,b''),(3,struct.pack('<dddd',20,20,50,50))]:
            self.assertTrue(decode_geometry(packet(Point(20,50),flags,envelope=envelope),4326).equals(Point(20,50)))

    def test_invalid_headers(self):
        for blob in [b'bad', packet(Point(1,2),srs=2180),packet(Point(1,2),flags=0x21),packet(Point(1,2),flags=11),packet(Point(1,2),flags=3)[:10]]:
            with self.assertRaises(ValueError): decode_geometry(blob,4326)

    def test_empty_flag(self):
        self.assertTrue(decode_geometry(packet(Point(),flags=17),4326).is_empty)
        with self.assertRaisesRegex(ValueError,'EMPTY_FLAG'): decode_geometry(packet(Point()),4326)

    def test_kmz_without_fid_and_data_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'test.kmz'
            with zipfile.ZipFile(path,'w') as archive:
                archive.writestr('doc.kml','<kml xmlns="http://www.opengis.net/kml/2.2"><Placemark id="88"><ExtendedData><Data name="Operator"><value>SYNTHETIC</value></Data></ExtendedData><Point><coordinates>20,50,0</coordinates></Point></Placemark></kml>')
            records,errors=kmz_features(path)
            self.assertFalse(errors)
            self.assertIsNone(records['placemark:1']['fid'])
            self.assertEqual(records['placemark:1']['fields']['Operator'],'SYNTHETIC')

    def test_multiset_consumes_each_geometry_once(self):
        result=compare_exports([feature(1,Point(1,2)),feature(2,Point(1,2))],{'placemark:1':{'fid':None,'geometry':Point(1,2)}})
        self.assertEqual(len(result['matches']),1)
        self.assertEqual(len(result['issues']),1)
        self.assertEqual(result['matches'][0]['method'],'xy_multiset_only')

    def test_explicit_fid_mismatch_not_repaired_by_other_fid(self):
        result=compare_exports([feature(1,Point(1,2))],{'fid:1':{'fid':'1','geometry':Point(3,4)},'fid:2':{'fid':'2','geometry':Point(1,2)}})
        self.assertFalse(result['matches'])
        self.assertEqual(result['issues'][0]['issue'],'KMZ_GEOMETRY_MISMATCH')

    def test_single_part_line_wrapper(self):
        line=LineString([(1,2),(3,4)])
        result=compare_exports([feature(1,MultiLineString([line]))],{'fid:1':{'fid':'1','geometry':line}})
        self.assertEqual(len(result['matches']),1)

    def test_readonly_reader_quarantines_invalid_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'synthetic.gpkg'
            with sqlite3.connect(path) as db:
                db.executescript('CREATE TABLE gpkg_geometry_columns(table_name TEXT,column_name TEXT,srs_id INTEGER,geometry_type_name TEXT); INSERT INTO gpkg_geometry_columns VALUES(\'station\',\'geom\',4326,\'POINT\'); CREATE TABLE station(fid INTEGER,geom BLOB,Name TEXT);')
                db.executemany('INSERT INTO station VALUES(?,?,?)',[(1,packet(Point(20,50)),'SYNTHETIC'),(2,b'bad','SYNTHETIC')])
            db.close()
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            features,errors=read_features(path)
            self.assertEqual(len(features),1)
            self.assertEqual(errors[0]['fid'],2)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),digest)


if __name__=='__main__': unittest.main()
