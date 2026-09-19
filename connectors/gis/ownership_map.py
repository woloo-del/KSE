"""Inspect GUGiK county completeness HTML as inert text, without running scripts."""
import html
import re


def inspect_county(raw: bytes) -> dict:
    text = raw.decode('utf-8')
    fields = {}
    for item in re.findall(r'<li\b[^>]*>(.*?)</li>', text, re.S):
        match = re.fullmatch(r'\s*<span class="list-item-value">(.*?)</span>(.*?)\s*', item, re.S)
        if match:
            label, value = [' '.join(html.unescape(re.sub(r'<[^>]+>', '', part)).split()) for part in match.groups()]
            if label in fields:
                raise ValueError('DUPLICATE_FIELD')
            fields[label] = value
    teryt = fields.get('TERYT', '')
    if not re.fullmatch(r'\d{4}', teryt):
        raise ValueError('MISSING_COUNTY_ID')
    groups = {}
    for label, value in fields.items():
        match = re.match(r'^(\d+) - ', label)
        if match:
            key = int(match[1])
            if key in groups or not value.isdecimal():
                raise ValueError('INVALID_GROUP_COUNT')
            groups[key] = int(value)
    if set(groups) != set(range(1, 17)):
        raise ValueError('INCOMPLETE_GROUPS')
    total = int(fields['Liczba działek'])
    missing = int(fields['b.d. – brak danych o grupie'])
    duplicates = int(fields['Liczba duplikatów (działek)'])
    if min(total, missing, duplicates) < 0 or sum(groups.values()) + missing != total:
        raise ValueError('COUNT_MISMATCH')
    date_fields = [value for label, value in fields.items() if label.startswith('Data ostatniej aktualizacji')]
    if len(date_fields) != 1 or not fields.get('Nazwa jednostki'):
        raise ValueError('MISSING_METADATA')
    return {'classification': 'REPORTED', 'scope': 'COUNTY_SERVICE_SNAPSHOT_NOT_STATION_BUFFER',
            'teryt': teryt, 'county_name': fields['Nazwa jednostki'],
            'parcel_count': total, 'missing_group_count': missing,
            'group_counts': groups, 'duplicate_count': duplicates,
            'source_last_subset_retrieval_label': date_fields[0],
            'ownership_area_percent': None,
            'availability': 'NO_GROUP_VALUES_IN_SNAPSHOT' if total > 0 and missing == total else 'REQUIRES_LOCAL_COVERAGE_CHECK'}
