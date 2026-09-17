"""Review compound group values against single-group records in the same source layer."""
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
from connectors.gis.compound_groups import candidate_components, compare_peer_values


def review(root: Path, output: Path) -> dict:
    private=(ROOT/'data/private').resolve()
    root,output=root.resolve(),output.resolve()
    if not root.is_relative_to(private) or not output.is_relative_to(private) or output.is_relative_to(root) or output.exists():
        raise ValueError('Use private source directory and new separate private output directory.')
    paths=sorted(root.glob('*.gpkg'))
    if not paths: raise ValueError('NO_GEOPACKAGES_FOUND')
    inputs,records,errors=[],[],[]
    for path in paths:
        digest=hashlib.sha256(path.read_bytes()).hexdigest()
        source=path.relative_to(private).as_posix()
        inputs.append({'path':source,'sha256':digest})
        features,geometry_errors=read_features(path)
        errors.extend({'source_file':source,**error} for error in geometry_errors)
        peers=defaultdict(list)
        for feature in features:
            observations,_=capacity_observations(feature.properties)
            for item in observations:
                name=item['scope_name']
                if item['scope_type']=='GROUP' and name and '/' not in name:
                    peers[(feature.table,name,item['source_field'])].append({'fid':feature.fid,'value':item['value']})
        for feature in features:
            group=feature.properties.get('Group')
            if not isinstance(group,str) or '/' not in group: continue
            description=feature.properties.get('Composition of group (PL)') or ''
            observations,_=capacity_observations(feature.properties)
            for item in observations:
                if item['scope_type']!='GROUP': continue
                record={'source_file':source,'source_sha256':digest,'source_table':feature.table,
                    'source_fid':feature.fid,'source_field':item['source_field'],'group_label':group,
                    'description':description,'raw_value':item['raw_value'],'target_year':item['target_year'],
                    'components':[],'approved_value':None,'status':'REVIEW_REQUIRED'}
                try:
                    components=candidate_components(group,description,item['raw_value'])
                    for component in components:
                        references=peers[(feature.table,component['group_name'],item['source_field'])]
                        component['peer_records']=references
                        component['comparison']=compare_peer_values(component['candidate_value_MW'],references)
                    record['components']=components
                except (ValueError,AttributeError) as exc:
                    record['error']=str(exc)
                records.append(record)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=digest: raise ValueError('SOURCE_CHANGED')
    result={'method':'compound_groups_review_v1','access':'PRIVATE','retrieval_date':datetime.now(timezone.utc).isoformat(),
        'inputs':inputs,'records':records,'geometry_errors':errors,'limitations':[
            'Ordinal association is inferred; comparison uses the same compilation, not independent operator evidence.',
            'No station section IDs, network topology, direction or current available capacity are established.',
            'Original unresolved observations remain unchanged. No sums or automatic corrections.']}
    output.mkdir(parents=True)
    (output/'group_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
    print(f'Reviewed {len(records)} compound source cells.')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path);parser.add_argument('output',type=Path)
    args=parser.parse_args();review(args.root,args.output)
