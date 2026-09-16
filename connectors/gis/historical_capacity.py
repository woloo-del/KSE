"""Normalize historical compilation fields, without interpreting them as current capacity."""
from __future__ import annotations

from decimal import Decimal
import re

FIELD = re.compile(r'^Free Capacities(?P<scope> of Group| of Area| of City District \((?P<kv>\d+)kV\))? - (?P<year>\d{4})$')
POWER = re.compile(r'^(\d+(?:[.,]\d+)?)\s*MW$', re.IGNORECASE)


def parse_mw(raw: object) -> tuple[float | None, str]:
    if raw is None or (isinstance(raw,str) and raw.strip() in {'','-MW','- MW','-----','N/D'}):
        return None,'UNKNOWN'
    if not isinstance(raw,str) or not (match := POWER.fullmatch(raw.strip())):
        raise ValueError('UNSUPPORTED_CAPACITY_VALUE_OR_UNIT')
    return float(Decimal(match.group(1).replace(',','.'))),'REPORTED'


def capacity_observations(properties: dict) -> tuple[list[dict], list[dict]]:
    """One observation per source field; preserve repeated group records, never sum them."""
    observations, errors = [], []
    for field, raw in properties.items():
        if not field.startswith('Free Capacities'):
            continue
        match=FIELD.fullmatch(field)
        if match is None:
            errors.append({'field':field,'raw_value':raw,'error':'UNSUPPORTED_CAPACITY_FIELD'})
            continue
        scope=match.group('scope')
        if scope==' of Group':
            scope_type,scope_name='GROUP',properties.get('Group')
        elif scope and scope.startswith(' of City District'):
            scope_type,scope_name='CITY_DISTRICT',properties.get('City District')
        elif scope==' of Area':
            scope_type,scope_name='AREA',None
        else:
            scope_type,scope_name='UNVERIFIED',None
        validation_status='PARSED'
        try:
            value,classification=parse_mw(raw)
        except ValueError as exc:
            errors.append({'field':field,'raw_value':raw,'error':str(exc)})
            value,classification=None,'UNKNOWN'
            validation_status='REVIEW_REQUIRED'
        observations.append({
            'source_field':field,'raw_value':raw,'value':value,'unit':'MW',
            'classification':classification,'reporting_authority':'USER_SUPPLIED_COMPILATION',
            'validation_status':validation_status,
            'scope_type':scope_type,'scope_name':scope_name,
            'voltage_kv':int(match.group('kv')) if match.group('kv') else None,
            'target_year':int(match.group('year')),'source_date':None,'valid_from':None,'valid_to':None,
            'direction':'UNKNOWN','current_capacity_eligible':False,'summation_eligible':False,
            'temporal_interpretation':'HISTORICAL_COMPILATION_YEAR_COLUMN',
        })
    return observations, errors
