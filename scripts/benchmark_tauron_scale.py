"""Bulk TAURON adapter with a source-bound extraction cache."""
import hashlib,json,sys,time
from pathlib import Path
import pypdf
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from connectors.tauron.project_pipeline import parse_pages,summarize

def run():
    c=json.loads((ROOT/'data/catalog/data_sources.json').read_text(encoding='utf-8'))
    e=next(e for s in c['sources'] if s['source_id']=='TAURON_PIPELINE' for e in s['evidence'] if e['local_path'].endswith('.pdf'))
    raw=ROOT/e['local_path'];digest=hashlib.sha256(raw.read_bytes()).hexdigest()
    if digest!=e['sha256']:raise ValueError('SNAPSHOT_CHANGED')
    cache=ROOT/f'data/staging/research/tauron_text_{digest}.json'
    start=time.perf_counter()
    if cache.exists():
        stored=json.loads(cache.read_text(encoding='utf-8'));pages=stored['pages']
        if stored['source_sha256']!=digest or stored['text_sha256']!=hashlib.sha256(json.dumps(pages,ensure_ascii=False).encode()).hexdigest():raise ValueError('CACHE_CHANGED')
    else:
        pdf=pypdf.PdfReader(raw);pages=[p.extract_text() for p in pdf.pages]
        cache.parent.mkdir(parents=True,exist_ok=True)
        cache.write_text(json.dumps({'source_sha256':digest,'text_sha256':hashlib.sha256(json.dumps(pages,ensure_ascii=False).encode()).hexdigest(),'pypdf_version':pypdf.__version__,'pages':pages},ensure_ascii=False),encoding='utf-8')
    data=parse_pages(pages);result=summarize(data)
    result['provenance']={k:e[k] for k in ('url','sha256','retrieval_date','local_path')}
    result['method_code_sha256']=hashlib.sha256((ROOT/'connectors/tauron/project_pipeline.py').read_bytes()).hexdigest()
    result['text_sha256']=hashlib.sha256(json.dumps(pages,ensure_ascii=False).encode()).hexdigest()
    data['provenance']=result['provenance']
    for path,obj in [(ROOT/'data/processed/tauron_bulk_pipeline_2026-09-10_v1.json',data),(ROOT/'data/reference/tauron_scale_benchmark_2026-09-10_v1.json',result)]:
        content=json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
        if path.exists() and path.read_text(encoding='utf-8')!=content:raise ValueError('EXISTING_VERSION_DIFFERS')
        path.parent.mkdir(parents=True,exist_ok=True)
        if not path.exists():path.write_text(content,encoding='utf-8',newline='\n')
    print(json.dumps({'metrics':result['metrics'],'seconds_from_cache_or_extract':round(time.perf_counter()-start,3)},ensure_ascii=False))
if __name__=='__main__':run()
