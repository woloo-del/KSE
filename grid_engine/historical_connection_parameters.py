"""Version 2 historical inventory: explicit dated parameters and coverage claims."""
from decimal import Decimal
import re

from grid_engine.historical_assignments import historical_inventory
from grid_engine.observation_history import Observation, as_known, timestamp
from grid_engine.shared_connection import Assignment, Evidence, SharedConnectionSnapshot, summarize

PARAMETERS = {'maximum_positions': 'position', 'inventory_complete': None,
              'export_limit_MW': 'MW', 'import_limit_MW': 'MW'}


def parameter_value(field: str, value: str | None) -> int | bool | Decimal | None:
    if value is None:
        return None
    if field == 'inventory_complete':
        if value not in {'true', 'false'}:
            raise ValueError('INVALID_COMPLETENESS_VALUE')
        return value == 'true'
    pattern = r'(0|[1-9][0-9]*)' if field == 'maximum_positions' else r'(0|[1-9][0-9]*)(\.[0-9]+)?'
    if not re.fullmatch(pattern, value):
        raise ValueError('INVALID_HISTORICAL_PARAMETER_VALUE')
    return int(value) if field == 'maximum_positions' else Decimal(value)


def historical_inventory_v2(history: tuple[Observation, ...], *, connection_id: str,
                            scenario: str, known_at: str, effective_on: str) -> dict:
    base = historical_inventory(history, connection_id=connection_id, scenario=scenario,
                                known_at=known_at, effective_on=effective_on)
    cutoff = timestamp(known_at)
    # Invalid units must not disappear through querying only the expected unit.
    for item in history:
        if (item.entity_id == connection_id and item.scenario == scenario
                and item.field in PARAMETERS and timestamp(item.recorded_at) <= cutoff):
            if item.unit != PARAMETERS[item.field]:
                raise ValueError('HISTORICAL_PARAMETER_UNIT_MISMATCH')
            parameter_value(item.field, item.value)
    values, proofs, views = {}, {}, {}
    for field, unit in PARAMETERS.items():
        view = as_known(history, entity_id=connection_id, field=field, scenario=scenario,
                        unit=unit, known_at=known_at, effective_on=effective_on)
        documents = [i for i in view['active'] if i['evidence']['origin'] == 'DOCUMENT']
        usable = view['status'] == 'REPORTED' and bool(documents)
        view['used_in_inventory'] = usable
        if view['status'] == 'REPORTED' and not documents:
            view['reasons'].append('DOCUMENTARY_CONFIRMATION_MISSING')
        values[field] = parameter_value(field, view['value']) if usable else None
        proofs[field] = Evidence(**documents[0]['evidence']) if usable else None
        views[field] = view
    snapshot = SharedConnectionSnapshot(
        snapshot_id='historical_connection_view_v2', connection_id=connection_id,
        as_of=effective_on, scenario=scenario,
        maximum_positions=values['maximum_positions'], position_evidence=proofs['maximum_positions'],
        inventory_complete=values['inventory_complete'] is True, coverage_evidence=proofs['inventory_complete'],
        export_limit_MW=values['export_limit_MW'], export_evidence=proofs['export_limit_MW'],
        import_limit_MW=values['import_limit_MW'], import_evidence=proofs['import_limit_MW'],
        assignments=tuple(Assignment(**{**a, 'evidence': Evidence(**a['evidence'])}) for a in base['assignments']),
    )
    result = summarize(snapshot)
    # A completeness claim cannot resolve conflicting, expired or undated position histories.
    if base['unresolved_position_histories']:
        unassigned = result['unassigned_positions']
        unassigned.update(value=None, classification='UNKNOWN', formula=None)
        unassigned['reasons'].append('UNRESOLVED_POSITION_HISTORIES')
    all_views = [*base['position_history'], *views.values()]
    result.update({
        'method': 'historical_shared_connection_v2', 'inventory_method': result['method'],
        'known_at': known_at, 'effective_on': effective_on,
        'position_history': base['position_history'], 'parameter_history': views,
        'unresolved_position_histories': base['unresolved_position_histories'],
        'evidence': [p for view in all_views for p in view['evidence']],
        'access': 'PRIVATE' if any(view['access'] == 'PRIVATE' for view in all_views) else 'PUBLIC',
    })
    result['limitations'].extend([
        'Coverage is an explicit dated documentary claim, not an independent audit of all projects.',
        'Unknown, conflicting or unresolved position histories block unassigned-position calculation.',
        'Reported limits are separate import/export limits, never available connection capacity.',
        'Reported assignment is not proof of commissioning; planned parameters remain in PLANNED.',
    ])
    return result
