"""Reproduce public source claims without selecting a single commissioning year."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from connectors.pse.investment_dates import annual_report_completion_year,portal_completion_year


def build() -> dict:
    manifest=json.loads((ROOT/'data/catalog/probe_results_radkowice_investment_dates_2026-09-17.json').read_text(encoding='utf8'))
    byid={r['source_id']:r for r in manifest}
    raw={}
    for sid,meta in byid.items():
        raw[sid]=(ROOT/meta['local_path']).read_bytes()
        if hashlib.sha256(raw[sid]).hexdigest()!=meta['sha256']:raise ValueError('SNAPSHOT_CHANGED')
    pdf=PdfReader(ROOT/byid['PSE_IMPACT_REPORT_2023']['local_path'])
    years={
        'PSE_IMPACT_REPORT_2023':annual_report_completion_year(pdf.pages[46].extract_text(),pdf.pages[47].extract_text()),
        'PSE_INVESTMENTS_RADK':portal_completion_year(raw['PSE_INVESTMENTS_RADK'].decode('utf8')),
    }
    claims=[]
    for sid,year in years.items():
        meta=byid[sid]
        claims.append({'source_id':sid,'completion_year_reported':year,'classification':'REPORTED',
            'source_date':None,'valid_from':None,'valid_to':None,'source_quality':'B',
            'evidence':{'source_id':sid,'url':meta['url'],'snapshot_sha256':meta['sha256'],
                'retrieval_date':meta['retrieval_date'],'source_date':None,
                'locator':'PDF pages 47–48; edition 2024, reporting year 2023' if sid=='PSE_IMPACT_REPORT_2023' else 'h4: wymiana transformatora Radkowice; following completion paragraph'}})
    return {'method':'radkowice_investment_dates_v1','access':'PUBLIC_SOURCE_REVIEW','verified_date':'2026-09-17',
        'subject':'Wymiana transformatora i dostosowanie infrastruktury w Radkowicach',
        'claims':claims,'status':'UNRESOLVED_DATE_OR_SCOPE' if len(set(years.values()))>1 else 'CONSISTENT_REPORTED_YEARS',
        'same_project_identity':'UNCONFIRMED','selected_completion_year':None,'physical_commissioning_date':None,
        'transformer_rating_MVA':None,'additional_available_capacity_MW':None,
        'explanation':'Podobna nazwa zadania nie rozstrzyga identyczności zakresu. Nie wybrano nowszego wskazania automatycznie.',
        'limitations':['Rok zakończenia zadania nie jest automatycznie datą załączenia urządzenia.',
            'Brak identyfikatora jednostki, zakresu odbioru i mocy znamionowej; nie wyliczono dodatkowych MW.']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    with args.output.open('x',encoding='utf8',newline='\n') as target:
        target.write(json.dumps(build(),ensure_ascii=False,indent=2)+'\n')
    print(args.output)
