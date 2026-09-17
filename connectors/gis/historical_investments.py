"""Source-record normalization for the supplied historical GIS, not asset resolution."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Layer:
    name_field: str
    description_field: str
    historical_category: str
    required_fields: tuple[str, ...] = ()


TASK = 'Nazwa zadania inwestycyjnego'
PURPOSE = 'Podstawowy cel realizacji zadania inwestycyjnego'
LAYERS = {
    'LINIE - Realizowane zadania inwestycyjne przez PSE': Layer(TASK, PURPOSE, 'IMPLEMENTATION_LAYER', ('Rok rozpoczęcia', 'Rok zakończenia')),
    'STACJE - Realizowane zadania inwestycyjne przez PSE': Layer('Nazwa obiektu', TASK, 'IMPLEMENTATION_LAYER', (PURPOSE, 'Rok rozpoczęcia', 'Rok zakończenia')),
    'Planowane linie elektroenergetyczne': Layer('Nazwa linii', 'Nazwa lub opis realizowanego zadania', 'PLANNED_LAYER'),
    'Planowane modernizacje - linie elektroenergetyczne': Layer('Nazwa linii', 'Nazwa lub opis planowanej modernizacji', 'PLANNED_LAYER'),
    'Planowane modernizacje - stacje elektroenergetyczne': Layer('Nazwa stacji', 'Nazwa lub opis planowanego zadania', 'PLANNED_LAYER'),
    'Planowane stacje elektroenergetyczne': Layer('Nazwa obiektu', '(1) Źródło informacji o planowanej stacji\nelektroenergetycznej', 'PLANNED_LAYER'),
    'Stacje elektroenergetyczne - WPZP': Layer('Name', 'Comment', 'SPATIAL_PLAN_LAYER', ('Status', 'Year', 'Link')),
    'Zmodernizowane linie elektroenergetyczne': Layer('Nazwa linii', 'Nazwa lub opis zrealizowanego zadania', 'COMPLETED_LAYER'),
    'Zmodernizowane stacje elektroenergetyczne': Layer('Nazwa stacji', 'Nazwa lub opis zrealizowanego zadania', 'COMPLETED_LAYER'),
}


def year_observation(raw: object, source_field: str) -> dict:
    """Do not extract one year from a range or a multi-task field."""
    text = str(raw).strip() if raw is not None else ''
    year = int(text) if re.fullmatch(r'[0-9]{4}', text) and int(text) > 0 else None
    return {'value': year, 'raw_value': raw, 'source_field': source_field,
            'classification': 'REPORTED' if year is not None else 'UNKNOWN',
            'review_required': bool(text) and year is None,
            'evidence_scope': 'SUPPLIED_COMPILATION_ONLY'}


def source_links(properties: dict) -> list[dict]:
    """Discover URL candidates only; retain field context and do not fetch them."""
    links = []
    for field, value in properties.items():
        if not isinstance(value, str):
            continue
        for match in re.finditer(r'https?://[^\s<>"\']+', value):
            candidate = match.group().rstrip('.,;')
            # Remove only unbalanced closing punctuation from surrounding prose.
            while candidate.endswith(')') and candidate.count(')') > candidate.count('('):
                candidate = candidate[:-1]
            try:
                parsed = urlsplit(candidate)
                valid = bool(parsed.hostname) and parsed.username is None and parsed.password is None
            except ValueError:
                valid = False
            links.append({'url_candidate': candidate, 'source_field': field,
                          'syntax_valid': valid, 'verification_status': 'NOT_VERIFIED',
                          'last_verified': None})
    return links


def normalize_record(stem: str, table: str, fid: int, properties: dict,
                     source_file: str, source_sha256: str) -> dict:
    if stem not in LAYERS:
        raise ValueError('UNSUPPORTED_INVESTMENT_LAYER')
    layer = LAYERS[stem]
    required = {layer.name_field, layer.description_field, *layer.required_fields}
    if not required.issubset(properties):
        raise ValueError('INVESTMENT_SCHEMA_CHANGED')
    if not isinstance(fid, int) or isinstance(fid, bool) or not re.fullmatch(r'[0-9a-f]{64}', source_sha256):
        raise ValueError('INVALID_SOURCE_IDENTITY')
    identity = json.dumps([source_file, source_sha256, table, fid], ensure_ascii=False, separators=(',', ':'))
    issues = []
    if not isinstance(properties[layer.name_field], str) or not properties[layer.name_field].strip():
        issues.append('MISSING_OR_INVALID_NAME')
    if stem.startswith('STACJE -'):
        issues.append('TASK_PURPOSE_COLUMNS_DIFFER_BETWEEN_GPKG_AND_XLSX_EXPORTS')
    years = {field: year_observation(properties[field], field)
             for field in ('Rok rozpoczęcia', 'Rok zakończenia', 'Year') if field in properties}
    start = years.get('Rok rozpoczęcia', {}).get('value')
    end = years.get('Rok zakończenia', {}).get('value')
    if start is not None and end is not None and start > end:
        issues.append('START_AFTER_END_SOURCE_VALUES_RETAINED')
    if any(y['review_required'] for y in years.values()):
        issues.append('YEAR_FIELD_REQUIRES_REVIEW')
    return {
        'source_record_id': 'gis-investment-' + hashlib.sha256(identity.encode()).hexdigest(),
        'canonical_investment_id': None,
        'source_file': source_file, 'source_sha256': source_sha256,
        'source_table': table, 'source_fid': fid,
        'source_quality': 'UNKNOWN', 'primary_source_verified': False,
        'name': properties[layer.name_field], 'name_source_field': layer.name_field,
        'description': properties[layer.description_field], 'description_source_field': layer.description_field,
        'historical_layer_category': layer.historical_category,
        'category_basis': {'classification': 'INFERRED', 'source_layer': stem,
                           'method': 'literal_layer_label_only'},
        'source_status_raw': properties.get('Status'),
        'current_status': 'UNKNOWN', 'current_status_classification': 'UNKNOWN',
        'year_observations': years, 'source_date': None, 'valid_from': None, 'valid_to': None,
        'actual_commissioning_date': None, 'additional_available_capacity_MW': None,
        'current_grid_eligible': False, 'future_capacity_eligible': False,
        'source_links': source_links(properties), 'quality_issues': issues,
        'raw_properties': dict(properties),
    }
