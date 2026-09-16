"""Preserve historical GIS capacity fields as private, source-addressable observations."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from connectors.gis.geopackage import read_features
from connectors.gis.historical_capacity import capacity_observations


def normalize(root: Path, output: Path, compilation_year: int) -> dict:
    private=(ROOT/'data/private').resolve()
    root,output=root.resolve(),output.resolve()
    if not root.is_relative_to(private) or not output.is_relative_to(private) or output.is_relative_to(root) or output.exists():
        raise ValueError('Use private source directory and a new separate private output directory.')
    paths=sorted(root.glob('*.gpkg'))
    if not paths: raise ValueError('NO_GEOPACKAGES_FOUND')
    records,errors,inputs=[],[],[]
    retrieval=datetime.now(timezone.utc).isoformat()
    groups=defaultdict(list)
    for path in paths:
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        source=path.relative_to(private).as_posix()
        inputs.append({'path':source,'sha256':digest})
        features,parse_errors=read_features(path)
        errors.extend({'source_file':source,**e} for e in parse_errors)
        for feature in features:
            values,validation_errors=capacity_observations(feature.properties)
            errors.extend({'source_file':source,'fid':feature.fid,**e} for e in validation_errors)
            for item in values:
                item.update({'source_file':source,'source_sha256':digest,'source_table':feature.table,'source_fid':feature.fid,
                    'source_entity_name':feature.properties.get('Name'),'source_operator_label':feature.properties.get('OSD'),
                    'retrieval_date':retrieval,'source_version':digest,'access':'PRIVATE'})
                identity=json.dumps([digest,feature.table,feature.fid,item['source_field']],ensure_ascii=False,separators=(',',':'))
                item['observation_id']='GIS-HIST-'+hashlib.sha256(identity.encode()).hexdigest()
                records.append(item)
                if item['scope_type'] in {'GROUP','CITY_DISTRICT'} and item['scope_name']:
                    groups[(source,item['scope_type'],item['scope_name'],item['target_year'],item['voltage_kv'])].append(item)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=digest: raise ValueError('SOURCE_CHANGED_DURING_NORMALIZATION')
    diagnostics=[]
    for key,items in groups.items():
        distinct={i['value'] for i in items}
        diagnostics.append({'source_file':key[0],'scope_type':key[1],'scope_name':key[2],'target_year':key[3],
            'voltage_kv':key[4],'source_record_count':len(items),'values_mw':sorted(v for v in distinct if v is not None),
            'includes_unknown':None in distinct,'status':'CONFLICT' if len(distinct-{None})>1 else 'INCOMPLETE' if None in distinct else 'CONSISTENT',
            'observation_ids':[i['observation_id'] for i in items]})
    result={'method':'historical_gis_capacity_v1','access':'PRIVATE','retrieval_date':retrieval,
        'compilation_year_user_reported':compilation_year,'inputs':inputs,'observations':records,'errors':errors,'group_diagnostics':diagnostics,
        'limitations':['Values transcribed from a compilation, not verified against original operator publications.',
            'Year columns do not establish publication or observation dates. Future year columns remain historical forecasts.',
            'No direction inferred. No repeated group values summed. No station available-capacity conclusion.',
            'Missing source area identifiers remain unknown. Group diagnostics do not prove electrical topology.']}
    output.mkdir(parents=True)
    target=output/'capacity_observations.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
    print(f'{len(records)} historical observations; {len(errors)} validation errors. Output: {target}')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path);parser.add_argument('output',type=Path)
    parser.add_argument('--compilation-year',type=int,required=True,help='Year declared by the provider, not derived from filesystem dates.')
    args=parser.parse_args();normalize(args.root,args.output,args.compilation_year)
