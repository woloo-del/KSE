"""Resolve documentary position assignments before counting a historical inventory."""
from grid_engine.observation_history import Observation, as_known, timestamp, validate_history
from grid_engine.shared_connection import Assignment, Evidence, SharedConnectionSnapshot, summarize

POSITION_PREFIX = 'position_project:'


def historical_inventory(history: tuple[Observation, ...], *, connection_id: str,
                         scenario: str, known_at: str, effective_on: str) -> dict:
    """A position field contains a project ID, never a nearby station's project list.

    Maximum positions and completeness deliberately remain unknown: this adapter
    resolves assignments only, without borrowing parameters from a current snapshot.
    """
    validate_history(history)
    cutoff = timestamp(known_at)
    visible = [item for item in history
               if item.entity_id == connection_id and item.scenario == scenario
               and item.field.startswith(POSITION_PREFIX)
               and timestamp(item.recorded_at) <= cutoff]
    for item in visible:
        if item.unit is not None or not item.field[len(POSITION_PREFIX):].strip():
            raise ValueError('INVALID_POSITION_OBSERVATION')
    views, assignments = [], []
    for field in sorted({item.field for item in visible}):
        view = as_known(history, entity_id=connection_id, field=field, scenario=scenario,
                        unit=None, known_at=known_at, effective_on=effective_on)
        view['position_id'] = field[len(POSITION_PREFIX):]
        # A user statement alone is not documentary confirmation of assignment.
        documented = [item for item in view['active']
                      if item['evidence']['origin'] == 'DOCUMENT']
        view['included_in_count'] = view['status'] == 'REPORTED' and bool(documented)
        if view['included_in_count']:
            assignments.append(Assignment(
                project_id=view['value'], position_id=view['position_id'],
                connection_id=connection_id, scenario=scenario, confirmed=True,
                evidence=Evidence(**documented[0]['evidence']),
            ))
        elif view['status'] == 'REPORTED':
            view['reasons'].append('DOCUMENTARY_CONFIRMATION_MISSING')
        views.append(view)
    result = summarize(SharedConnectionSnapshot(
        snapshot_id='historical_assignment_view', connection_id=connection_id,
        as_of=effective_on, scenario=scenario, maximum_positions=None,
        position_evidence=None, assignments=tuple(assignments),
    ))
    # Retain all relevant evidence, including conflicts and superseded private input.
    result.update({
        'method': 'historical_shared_assignments_v1',
        'inventory_method': result['method'],
        'known_at': known_at, 'effective_on': effective_on,
        'position_history': views,
        'unresolved_position_histories': sum(not view['included_in_count'] for view in views),
        'evidence': [proof for view in views for proof in view['evidence']],
        'access': 'PRIVATE' if any(view['access'] == 'PRIVATE' for view in views) else 'PUBLIC',
    })
    result['limitations'].extend([
        'Only explicit documentary position assignments with resolved validity are counted.',
        'Unresolved position histories remain visible and do not count as confirmed assignments.',
        'No historical maximum, completeness or MW limits are inferred from current data.',
        'Reported assignment is not proof of physical commissioning.',
    ])
    return result
