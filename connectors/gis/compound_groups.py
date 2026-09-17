"""Review ordinal group/value associations; never promote them to verified capacity."""
import re
from connectors.gis.historical_capacity import parse_mw

GROUP_DESCRIPTION = re.compile(r'\((\d+)\)\s*Grupa\s+([^:]+):')


def candidate_components(group: str, description: str, raw: str) -> list[dict]:
    names=[name.strip() for name in group.split('/')]
    if len(names)<2 or any(not name for name in names) or len(set(names))!=len(names):
        raise ValueError('INVALID_COMPOUND_GROUP')
    described=GROUP_DESCRIPTION.findall(description)
    if described!=[(str(i),name) for i,name in enumerate(names,1)]:
        raise ValueError('GROUP_DESCRIPTION_ORDER_MISMATCH')
    if not raw.endswith('MW'): raise ValueError('UNSUPPORTED_UNIT')
    parts=raw[:-2].split('/')
    if len(parts)!=len(names): raise ValueError('COMPONENT_COUNT_MISMATCH')
    result=[]
    for position,(name,part) in enumerate(zip(names,parts),1):
        value,classification=parse_mw(part.strip()+'MW')
        if value is None: raise ValueError('MISSING_COMPONENT')
        result.append({'position':position,'group_name':name,'candidate_value_MW':value,
            'association_classification':'INFERRED','numeric_token_classification':classification,
            'direction':'UNKNOWN','current_capacity_eligible':False,'summation_eligible':False,
            'method':'ordered_group_names_and_numbered_description_v1'})
    return result


def compare_peer_values(value: float, peers: list[dict]) -> str:
    known={p['value'] for p in peers if p['value'] is not None}
    if not known: return 'NO_NUMERIC_REFERENCE'
    if known!={value}: return 'CONFLICT'
    if any(p['value'] is None for p in peers): return 'CONSISTENT_KNOWN_VALUES_WITH_GAPS'
    return 'CONSISTENT_WITHIN_COMPILATION'
