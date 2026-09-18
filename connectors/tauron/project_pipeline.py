"""Bounded text adapter for the preserved TAURON PDF; no MW column guessing."""
from collections import Counter
import hashlib
import re

ROW = re.compile(r'^(\d+)\s+(\S+)\s+TAURON Dystrybucja S\.A\.\s+Osoba (prawna|fizyczna)\s+(.*?)\s+(SN|nN|NN|110 kV)\s+(TAK|NIE)\s+(\S+)\s+(.*)$')
STATUSES = {'UMOWA O PRZYŁĄCZENIE obowiązująca', 'WARUNKI PRZYŁĄCZENIA wydane',
    'UMOWA O PRZYŁĄCZENIE - obiekt przyłączony', 'WARUNKI PRZYŁĄCZENIA utraciły ważność',
    'WNIOSEK wycofany', 'WNIOSEK kompletny - w trakcie analizy technicznej i ekonomicznej',
    'WNIOSEK niekompletny', 'UMOWA O PRZYŁĄCZENIE rozwiązana', 'ODMOWA PRZYŁĄCZENIA', 'WNIOSEK w weryfikacji'}


def parse_pages(pages: list[str]) -> dict:
    if not pages or 'Wprowadza' not in pages[0] or '[MW]' not in pages[0]:raise ValueError('HEADER_CHANGED')
    dates=set(re.findall(r'Stan na (\d{2}\.\d{2}\.\d{4})r?\.', '\n'.join(pages)))
    if len(dates)!=1:raise ValueError('SOURCE_DATE_MISSING_OR_CONFLICT')
    records=[]
    for page,text in enumerate(pages,1):
        for line in text.splitlines():
            if 'TAURON Dystrybucja S.A.' not in line:continue
            m=ROW.fullmatch(line.strip())
            if not m:raise ValueError(f'ROW_LAYOUT_CHANGED_PAGE_{page}')
            seq,object_id,applicant,point,voltage,multi,tech,tail=m.groups()
            matches=[s for s in STATUSES if s in tail]
            if len(matches)!=1:raise ValueError(f'STATUS_CHANGED_PAGE_{page}')
            reasons=[]
            if multi=='TAK':reasons.append('MULTIPLE_POINTS')
            # Recognize a source code form, never decode it into a station name.
            if not re.fullmatch(r'[A-Z]{3}[34]',point):reasons.append('POINT_NOT_SINGLE_CODE')
            profile_id=None if reasons else hashlib.sha256(f'TAURON_PIPELINE|{point}|{voltage}'.encode()).hexdigest()
            records.append({'row_number':int(seq),'page':page,'operator_object_id':object_id,
                'applicant_category':applicant,'point_reported':point,'voltage_reported':voltage,
                'multiple_points_reported':multi,'technology_reported':tech,'status_reported':matches[0],
                'profile_id':profile_id,'canonical_station_id':None,'classification':'REPORTED',
                'export_MW':None,'import_MW':None,'power_extraction_status':'NOT_EXTRACTED_FROM_FLATTENED_PDF',
                'review_reasons':reasons,'raw_line':line})
    if [r['row_number'] for r in records]!=list(range(1,len(records)+1)) or not records:
        raise ValueError('ROW_SEQUENCE_GAP_OR_DUPLICATE')
    counts=Counter(r['operator_object_id'] for r in records)
    for r in records:
        if counts[r['operator_object_id']]>1:r['review_reasons'].append('REPEATED_OPERATOR_OBJECT_ID')
    return {'source_date_reported':next(iter(dates)), 'records':records,
            'unique_operator_ids':len(counts), 'repeated_operator_ids':sum(n>1 for n in counts.values())}


def summarize(data: dict) -> dict:
    rows=data['records'];groups={}
    for r in rows:
        if r['profile_id'] is None:continue
        g=groups.setdefault(r['profile_id'],{'profile_id':r['profile_id'],'point_code':r['point_reported'],
            'voltage_reported':r['voltage_reported'],'canonical_station_id':None,'row_numbers':[], 'status_counts':Counter()})
        g['row_numbers'].append(r['row_number']);g['status_counts'][r['status_reported']]+=1
    return {'method':'tauron_bulk_text_v1','source_date_reported':data['source_date_reported'],
        'metrics':{'source_records':len(rows),'source_code_voltage_groups':len(groups),
            'grouped_records':sum(r['profile_id'] is not None for r in rows),
            'ungrouped_records':sum(r['profile_id'] is None for r in rows),
            'records_requiring_identity_review':sum(bool(r['review_reasons']) for r in rows),
            'reason_counts':dict(Counter(x for r in rows for x in r['review_reasons'])),
            'unique_operator_ids':data['unique_operator_ids'],'repeated_operator_ids':data['repeated_operator_ids'],
            'status_counts':dict(Counter(r['status_reported'] for r in rows)),
            'power_values_extracted':0,'canonical_stations_verified':0},
        'sample_profiles':sorted(groups.values(),key=lambda g:(g['voltage_reported'],g['point_code']))[:50],
        'limitations':['Point codes are not verified GPZ names; no decoding by code suffix.',
            'Repeated object IDs are preserved, never deduplicated as projects.',
            'PDF text omits blank columns; power values are not inferred by token position.',
            'Connected status is reported by the source, not independent operational confirmation.',
            'Grouping statistics do not measure matching accuracy or nationwide coverage.']}
