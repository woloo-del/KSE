"""Immutable documentary history with separate knowledge and validity time axes."""
from dataclasses import asdict, dataclass
from datetime import date, datetime

from grid_engine.shared_connection import Evidence


def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('TIMEZONE_REQUIRED')
    return parsed


@dataclass(frozen=True)
class Observation:
    observation_id: str
    entity_id: str
    field: str
    scenario: str
    value: str | None
    unit: str | None
    classification: str
    evidence: Evidence
    recorded_at: str
    valid_from: str | None = None
    valid_to: str | None = None
    explicitly_open_ended: bool = False
    supersedes: str | None = None
    correction_reason: str | None = None

    @property
    def key(self) -> tuple[str, str, str, str | None]:
        return self.entity_id, self.field, self.scenario, self.unit


def validate_history(history: tuple[Observation, ...]) -> None:
    by_id: dict[str, Observation] = {}
    replaced: set[str] = set()
    last_recorded = None
    for item in history:
        if any(not isinstance(v, str) or not v.strip() for v in
               [item.observation_id, item.entity_id, item.field, item.scenario]):
            raise ValueError('MISSING_OBSERVATION_KEY')
        if item.observation_id in by_id:
            raise ValueError('DUPLICATE_OBSERVATION_ID')
        if item.classification not in {'REPORTED', 'UNKNOWN'}:
            raise ValueError('UNSUPPORTED_CLASSIFICATION')
        if ((item.classification == 'UNKNOWN') != (item.value is None)
                or (item.value is not None and (not isinstance(item.value, str) or not item.value.strip()))):
            raise ValueError('INVALID_OBSERVATION_VALUE')
        if item.unit is not None and (not isinstance(item.unit, str) or not item.unit.strip()):
            raise ValueError('INVALID_UNIT')
        item.evidence.validate()
        recorded = timestamp(item.recorded_at)
        if last_recorded is not None and recorded < last_recorded:
            raise ValueError('KNOWLEDGE_TIME_ORDER')
        last_recorded = recorded
        if timestamp(item.evidence.retrieval_date) > recorded:
            raise ValueError('RECORDED_BEFORE_RETRIEVAL')
        start = date.fromisoformat(item.valid_from) if item.valid_from is not None else None
        end = date.fromisoformat(item.valid_to) if item.valid_to is not None else None
        if type(item.explicitly_open_ended) is not bool:
            raise ValueError('INVALID_OPEN_ENDED_FLAG')
        if end is not None and (start is None or end <= start):
            raise ValueError('INVALID_VALIDITY_INTERVAL')
        if item.explicitly_open_ended and (start is None or end is not None):
            raise ValueError('INVALID_OPEN_ENDED_INTERVAL')
        if item.supersedes is not None:
            old = by_id.get(item.supersedes)
            if old is None:
                raise ValueError('MISSING_CORRECTION_TARGET')
            if item.supersedes in replaced:
                raise ValueError('BRANCHED_CORRECTION')
            if old.key != item.key or old.evidence.source_id != item.evidence.source_id:
                raise ValueError('CORRECTION_SCOPE_MISMATCH')
            if not item.correction_reason or not item.correction_reason.strip():
                raise ValueError('MISSING_CORRECTION_REASON')
            if recorded <= timestamp(old.recorded_at):
                raise ValueError('CORRECTION_TIME_ORDER')
            replaced.add(item.supersedes)
        elif item.correction_reason is not None:
            raise ValueError('REASON_WITHOUT_CORRECTION')
        by_id[item.observation_id] = item


def append_observation(history: tuple[Observation, ...], item: Observation) -> tuple[Observation, ...]:
    result = (*history, item)
    validate_history(result)
    return result


def as_known(history: tuple[Observation, ...], *, entity_id: str, field: str,
             scenario: str, unit: str | None, known_at: str, effective_on: str) -> dict:
    """Return evidence at two explicit cutoffs; never select the latest value silently."""
    validate_history(history)
    cutoff, effective = timestamp(known_at), date.fromisoformat(effective_on)
    key = entity_id, field, scenario, unit
    visible = [item for item in history if item.key == key and timestamp(item.recorded_at) <= cutoff]
    replaced = {item.supersedes for item in visible if item.supersedes is not None}
    candidates = [item for item in visible if item.observation_id not in replaced]
    active, undated = [], []
    for item in candidates:
        if item.valid_from is not None and date.fromisoformat(item.valid_from) > effective:
            continue
        if item.valid_from is None or (item.valid_to is None and not item.explicitly_open_ended):
            undated.append(item)
        elif (date.fromisoformat(item.valid_from) <= effective
              and (item.valid_to is None or effective < date.fromisoformat(item.valid_to))):
            active.append(item)
    values = sorted({item.value for item in active if item.value is not None})
    reasons = []
    if not active:
        reasons.append('NO_APPLICABLE_OBSERVATION')
    if undated:
        reasons.append('VALIDITY_UNRESOLVED')
    if any(item.value is None for item in active):
        reasons.append('EXPLICIT_UNKNOWN_OBSERVATION')
    if len(values) > 1:
        status, value = 'CONFLICT', None
    elif reasons:
        status, value = 'UNKNOWN', None
    else:
        status, value = 'REPORTED', values[0]
    return {
        'method':'observation_history_v1', 'entity_id':entity_id, 'field':field,
        'scenario':scenario, 'unit':unit, 'known_at':known_at, 'effective_on':effective_on,
        'status':status, 'value':value, 'candidate_values':values, 'reasons':reasons,
        'active':[asdict(item) for item in active],
        'unresolved_validity':[asdict(item) for item in undated],
        'visible_history':[asdict(item) for item in visible],
        'access':'PRIVATE' if any(item.evidence.access == 'PRIVATE' for item in visible) else 'PUBLIC',
        'evidence':[asdict(item.evidence) for item in visible],
    }
