"""Offline, reproducible bulk import of one checksummed PSE workbook."""
import hashlib
import json
from pathlib import Path
import sys
from time import perf_counter
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from connectors.pse.project_pipeline import parse, profiles


def run() -> None:
    catalog=json.loads((ROOT/'data/catalog/data_sources.json').read_text(encoding='utf-8'))
    evidence=next(e for s in catalog['sources'] if s['source_id']=='PSE_PIPELINE' for e in s['evidence'] if e['local_path'].endswith('.xlsx'))
    path=ROOT/evidence['local_path']
    if hashlib.sha256(path.read_bytes()).hexdigest()!=evidence['sha256']:raise ValueError('SNAPSHOT_CHANGED')
    start=perf_counter(); imported=parse(path)
    if imported["source_date"]!="2026-07-31":raise ValueError("SOURCE_DATE_CHANGED")
    result=profiles(imported); elapsed=perf_counter()-start
    provenance={k:evidence[k] for k in ('url','sha256','retrieval_date','local_path')}
    result.update(provenance=provenance, method_code_sha256=hashlib.sha256((ROOT/'connectors/pse/project_pipeline.py').read_bytes()).hexdigest())
    imported['provenance']=provenance
    target=ROOT/'data/processed/pse_bulk_pipeline_2026-07-31_v1.json';target.parent.mkdir(parents=True,exist_ok=True)
    for output,value in [(target,imported),(ROOT/'data/reference/pse_scale_benchmark_2026-07-31_v1.json',result)]:
        content=json.dumps(value,ensure_ascii=False,indent=2,default=str)+'\n'
        if output.exists() and output.read_text(encoding='utf-8')!=content:raise ValueError('EXISTING_VERSION_DIFFERS')
        if not output.exists():output.write_text(content,encoding='utf-8',newline='\n')
    print(json.dumps({'metrics':result['metrics'],'elapsed_seconds':round(elapsed,3),'footnotes':len(imported['footnotes']),'blank_rows':imported['blank_rows']},ensure_ascii=False))

if __name__=='__main__':run()
