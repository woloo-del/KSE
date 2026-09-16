"""Audit local GPKG geometry and paired KMZ coordinates without changing source data."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import shapely
from shapely.geometry import Point, LineString, MultiLineString
from connectors.gis.geopackage import read_features

KML = '{http://www.opengis.net/kml/2.2}'
# Serialization comparison only; this is not a location-accuracy threshold.
SERIALIZATION_TOLERANCE_DEGREES = 1e-8


def kmz_features(path: Path) -> tuple[dict, list]:
    found, errors = {}, []
    with zipfile.ZipFile(path) as archive:
        names = [n for n in archive.namelist() if n.lower().endswith('.kml')]
        if len(names) != 1:
            raise ValueError('EXPECTED_SINGLE_KML_DOCUMENT')
        raw = archive.read(names[0])
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ValueError('UNSUPPORTED_XML_DECLARATION')
    root = ET.fromstring(raw)
    for index, place in enumerate(root.iter(KML+'Placemark'),1):
        fields = {e.attrib['name']:e.text for e in place.iter(KML+'SimpleData')}
        fields.update({e.attrib['name']:e.findtext(KML+'value') for e in place.iter(KML+'Data')})
        fid = fields.get('fid')
        key = 'fid:'+fid if fid is not None else 'placemark:'+str(index)
        try:
            if key in found:
                raise ValueError('DUPLICATE_FID')
            parts = []
            for tag, constructor in [('Point',Point),('LineString',LineString)]:
                for element in place.iter(KML+tag):
                    value = element.findtext(KML+'coordinates') or ''
                    coordinates = [tuple(float(c) for c in word.split(',')[:2]) for word in value.split()]
                    if not coordinates or any(len(c)!=2 or not all(math.isfinite(x) for x in c) for c in coordinates):
                        raise ValueError('INVALID_KML_COORDINATES')
                    if tag=='Point' and len(coordinates)!=1:
                        raise ValueError('INVALID_POINT_COORDINATE_COUNT')
                    parts.append(constructor(coordinates[0] if tag=='Point' else coordinates))
            if len(parts)==1:
                geometry=parts[0]
            elif parts and all(p.geom_type=='LineString' for p in parts):
                geometry=MultiLineString(parts)
            else:
                raise ValueError('UNSUPPORTED_KML_GEOMETRY')
            found[key]={'fid':fid,'geometry':geometry,'name':place.findtext(KML+'name'),'fields':fields}
        except (ValueError, shapely.errors.GEOSException) as exc:
            errors.append({'placemark':index,'fid':fid,'error':str(exc)})
    return found,errors


def comparable(geometry):
    """KML may unwrap a single-part MultiLineString; compare its XY representation."""
    geometry = shapely.force_2d(geometry)
    if geometry.geom_type == 'MultiLineString' and len(geometry.geoms) == 1:
        geometry = geometry.geoms[0]
    return shapely.normalize(geometry)


def compare_exports(features: list, kml: dict) -> dict:
    """Consume each export record once; geometry-only matches are not entity matches."""
    remaining = dict(kml)
    matches, issues = [], []
    for feature in features:
        direct = 'fid:'+str(feature.fid)
        candidates = [direct] if direct in remaining else [k for k,v in remaining.items() if v['fid'] is None]
        same = [k for k in candidates if shapely.equals_exact(comparable(feature.geometry), comparable(remaining[k]['geometry']), SERIALIZATION_TOLERANCE_DEGREES)]
        if same:
            key = same[0]
            matches.append({'fid':feature.fid,'kmz_key':key,'method':'fid_and_xy' if key==direct else 'xy_multiset_only'})
            del remaining[key]
        else:
            issues.append({'fid':feature.fid,'issue':'KMZ_GEOMETRY_MISMATCH' if direct in remaining else 'NO_KMZ_EQUIVALENT'})
    return {'matches':matches,'issues':issues,'extra_keys':sorted(remaining)}


def audit(root: Path, output: Path) -> dict:
    private=(ROOT/'data/private').resolve()
    root, output = root.resolve(), output.resolve()
    if not root.is_relative_to(private) or not output.is_relative_to(private) or output.is_relative_to(root) or output.exists():
        raise ValueError('Use private source directory and a new separate private output directory.')
    layers, all_points, inputs = [], defaultdict(list), []
    paths=sorted(root.glob('*.gpkg'))
    if not paths: raise ValueError('NO_GEOPACKAGES_FOUND')
    for path in paths:
        original_hash=hashlib.sha256(path.read_bytes()).hexdigest()
        inputs.append({'path':path.relative_to(private).as_posix(),'sha256':original_hash})
        features, errors = read_features(path)
        pair=path.with_suffix('.kmz')
        kml, kml_errors = kmz_features(pair) if pair.exists() else ({},[{'error':'MISSING_KMZ'}])
        if pair.exists(): inputs.append({'path':pair.relative_to(private).as_posix(),'sha256':hashlib.sha256(pair.read_bytes()).hexdigest()})
        issues=list(errors)
        duplicates=defaultdict(list)
        for f in features:
            geom=f.geometry
            if f.srs_id!=4326:
                issues.append({'fid':f.fid,'issue':'UNSUPPORTED_CRS_FOR_COMPARISON'});continue
            if geom.is_empty or not geom.is_valid:
                issues.append({'fid':f.fid,'issue':'EMPTY_OR_INVALID_GEOMETRY','reason':shapely.is_valid_reason(geom)});continue
            if geom.geom_type.upper()!=f.declared_type:
                issues.append({'fid':f.fid,'issue':'DECLARED_GEOMETRY_TYPE_MISMATCH'})
            coordinates=shapely.get_coordinates(geom)
            if any(not(math.isfinite(x) and math.isfinite(y) and -180<=x<=180 and -90<=y<=90) for x,y in coordinates):
                issues.append({'fid':f.fid,'issue':'COORDINATE_RANGE'})
            normalized=shapely.normalize(shapely.force_2d(geom))
            key=shapely.to_wkb(normalized).hex()
            duplicates[key].append(f.fid)
            if geom.geom_type=='Point':
                label=f.properties.get('Name',f.properties.get('Nazwa stacji',f.properties.get('Nazwa obiektu')))
                all_points[key].append({'file':path.name,'fid':f.fid,'name':label})
                x,y=f.properties.get('xcoord'),f.properties.get('ycoord')
                if x is not None and y is not None:
                    if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in [x,y]) or max(abs(geom.x-x),abs(geom.y-y))>SERIALIZATION_TOLERANCE_DEGREES:
                        issues.append({'fid':f.fid,'issue':'GEOMETRY_ATTRIBUTE_COORDINATE_MISMATCH'})
        comparison=compare_exports([f for f in features if f.srs_id==4326],kml)
        issues.extend(comparison['issues'])
        if hashlib.sha256(path.read_bytes()).hexdigest()!=original_hash: raise ValueError('SOURCE_CHANGED_DURING_AUDIT')
        layers.append({'file':path.name,'decoded_features':len(features),'geometry_errors':errors,'issues':issues,
            'kmz_records':len(kml),'kmz_errors':kml_errors,'kmz_extra_ids':comparison['extra_keys'],'kmz_xy_matches':len(comparison['matches']),
            'kmz_match_details':comparison['matches'],
            'same_xy_geometry_within_layer':[v for v in duplicates.values() if len(v)>1]})
    result={'method':'private_geometry_audit_v2','access':'PRIVATE','retrieval_date':datetime.now(timezone.utc).isoformat(),
        'shapely_version':shapely.__version__,'geos_version':shapely.geos_version_string,
        'comparison_tolerance_degrees':SERIALIZATION_TOLERANCE_DEGREES,
        'limitations':['2D coordinate/serialization audit, not surveyed accuracy or electrical topology.',
                      'Coincident coordinates are review candidates, not automatic entity merges.',
                      'KMZ without fid: compare coordinate multisets only, without asserting entity identity.',
                      'Does not compare every KMZ attribute or validate every GeoPackage requirement.'],
        'inputs':inputs,'layers':layers,'coincident_point_groups':[v for v in all_points.values() if len(v)>1]}
    output.mkdir(parents=True)
    (output/'geometry_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
    print(f"Audited {len(layers)} layers; {sum(len(l['issues']) for l in layers)} feature issues. Output: {output}")
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path);parser.add_argument('output',type=Path)
    args=parser.parse_args();audit(args.root,args.output)
