"""Build the small, source-backed Radkowice documentary graph."""
import hashlib
import json
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from grid_engine.evidence_graph import validate_graph


def read(relative: str):
    return json.loads((ROOT/relative).read_text(encoding='utf-8-sig'))


def evidence(meta: dict, locator: str, source_date=None) -> dict:
    if hashlib.sha256((ROOT/meta['local_path']).read_bytes()).hexdigest() != meta['sha256']:
        raise ValueError('SNAPSHOT_CHANGED')
    return {'source_id':meta['source_id'], 'url':meta['url'], 'locator':locator,
            'snapshot_sha256':meta['sha256'], 'retrieval_date':meta['retrieval_date'],
            'source_date':source_date, 'valid_from':None, 'valid_to':None}


def build() -> dict:
    manifests = read('data/catalog/radkowice_snapshot_manifest.json')
    bip = next(x for x in manifests if x['source_id']=='CHECINY_ENERGY_PLAN')
    tariff = read('data/catalog/radkowice_tariff_snapshot.json')
    station_proof = evidence(bip, 'PDF page 21; section 4.2.1')
    tariff_proof = evidence(tariff, 'PDF pages 42, 43, 46; tables 6 and 7', '2025-12-03')
    pdf = PdfReader(ROOT/tariff['local_path'])
    text = ' '.join((pdf.pages[p].extract_text() or '') for p in [41,42,45])
    normalized = ' '.join(text.split())
    for required in ['OSD02 PGE Dystrybucja S.A.', 'OSD02 Radkowice T I', '3 grudnia 2025']:
        if required not in normalized:
            raise ValueError('TARIFF_EVIDENCE_CHANGED:'+required)
    entities, edges = [], []

    def entity(id, kind, name, proof, **attributes):
        entities.append({'id':id,'kind':kind,'name':name,'classification':'REPORTED',
                         'evidence':[proof], 'attributes':attributes})

    def edge(id, src, dst, relation, proof, **attributes):
        edges.append({'id':id,'from_id':src,'to_id':dst,'relation':relation,
                      'classification':'REPORTED','evidence':[proof],**attributes})

    entity('radkowice','STATION_REFERENCE','SE Radkowice',station_proof,
           equipment_ownership=None, transformer_inventory=None, operating_topology=None)
    for voltage in [220,110]:
        node=f'radkowice-level-{voltage}'
        entity(node,'VOLTAGE_LEVEL_REFERENCE',f'Radkowice {voltage} kV',station_proof,
               voltage_kV=voltage, physical_bus_id=None, owner_id=None)
        edge('contains-'+str(voltage),'radkowice',node,'HAS_REPORTED_VOLTAGE',station_proof)
    for id, name in [('kielce','Kielce'),('polaniec','Połaniec'),('kielce-piaski','Kielce Piaski')]:
        entity(id,'STATION_REFERENCE',name,station_proof)
        edge('line-radkowice-'+id,'radkowice-level-220',id,'REPORTED_LINE',station_proof,
             voltage_kV=220, operational_state='UNKNOWN', thermal_capacity_MVA=None,
             impedance_ohm=None, circuit_operator_id=None)
    entity('pge','OPERATOR','PGE Dystrybucja S.A.',tariff_proof, external_tariff_code='OSD02')
    entity('radkowice-md','DELIVERY_POINT_REFERENCE','Radkowice — MD w taryfie',tariff_proof,
           tariff_type='T', tariff_group='I', physical_equipment_id=None)
    edge('md-recipient','radkowice-md','pge','TARIFF_RECIPIENT',tariff_proof)
    edge('md-name','radkowice-md','radkowice','REFERS_TO_STATION_NAME',tariff_proof,
         note='Name reference; not an ownership or electrical connectivity assertion.')
    sample=read('data/reference/radkowice_pse_projects_2026-07-31.json')
    from scripts.research_radkowice import extract
    if sample != extract():
        raise ValueError('PROJECT_SAMPLE_CHANGED')
    for row in sample['records']:
        proof={'source_id':row['source_id'],'url':row['source_url'],
               'snapshot_sha256':row['snapshot_sha256'],'retrieval_date':row['retrieval_date'],
               'source_date':row['source_date'],'locator':f"{row['sheet']} row {row['row']} E/F/Q",
               'valid_from':None,'valid_to':None}
        if row['voltage_kV'] != 220 or row['status_reported'] != 'UMOWA O PRZYŁĄCZENIE obowiązująca':
            raise ValueError('PROJECT_SEMANTICS_CHANGED')
        entity(row['research_record_id'],'PROJECT_RECORD',row['project_name'],proof,
               canonical_project_id=None, source_record=row)
        edge('planned-'+str(row['row']),row['research_record_id'],'radkowice-level-220',
             'PLANNED_CONNECTION',proof,physical_connection_confirmed=False)
    graph={'schema_version':'evidence_graph_v1','method':'radkowice_documentary_v1',
           'power_flow_ready':False,'temporal_scope':'Mixed dated source observations; not a current operational snapshot.',
           'entities':entities,'relationships':edges,
           'user_context':read('data/project/radkowice_user_claims.json'),
           'unknowns':['PGE/PSE equipment ownership boundary','110 kV project coverage',
                       'Transformer ratings and inventory','Line impedances and limits','Actual loading',
                       'Complete project deduplication','Commercial reuse permissions']}
    validate_graph(graph)
    return graph


if __name__=='__main__':
    graph=build()
    target=ROOT/'data/reference/radkowice_evidence_graph_v1.json'
    target.write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f"Validated: {len(graph['entities'])} entities, {len(graph['relationships'])} relationships")
