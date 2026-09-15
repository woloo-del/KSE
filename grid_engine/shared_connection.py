"""Documentary position inventory. No electrical capacity calculation or database I/O."""
from dataclasses import asdict, dataclass
from datetime import date, datetime
from decimal import Decimal
import re
from typing import Literal


@dataclass(frozen=True)
class Evidence:
    source_id: str
    locator: str
    snapshot_sha256: str
    retrieval_date: str
    source_date: str | None
    access: Literal['PUBLIC', 'PRIVATE']
    origin: Literal['DOCUMENT', 'USER_PROVIDED']

    def validate(self) -> None:
        if not self.source_id or not self.locator:
            raise ValueError('MISSING_PROVENANCE')
        if not re.fullmatch(r'[a-f0-9]{64}', self.snapshot_sha256):
            raise ValueError('INVALID_SNAPSHOT_HASH')
        retrieved = datetime.fromisoformat(self.retrieval_date.replace('Z', '+00:00'))
        if retrieved.tzinfo is None:
            raise ValueError('RETRIEVAL_TIMEZONE_REQUIRED')
        if self.source_date is not None:
            if date.fromisoformat(self.source_date) > retrieved.date():
                raise ValueError('SOURCE_DATE_AFTER_RETRIEVAL')
        if self.access not in {'PUBLIC', 'PRIVATE'} or self.origin not in {'DOCUMENT', 'USER_PROVIDED'}:
            raise ValueError('INVALID_SOURCE_CLASSIFICATION')


@dataclass(frozen=True)
class Assignment:
    """Explicit assignment to this shared connection, not a station-level project entry."""
    project_id: str
    position_id: str | None
    connection_id: str
    scenario: Literal['CURRENT', 'PLANNED']
    confirmed: bool
    evidence: Evidence


@dataclass(frozen=True)
class SharedConnectionSnapshot:
    snapshot_id: str
    connection_id: str
    as_of: str
    scenario: Literal['CURRENT', 'PLANNED']
    maximum_positions: int | None
    position_evidence: Evidence | None
    assignments: tuple[Assignment, ...] = ()
    inventory_complete: bool = False
    coverage_evidence: Evidence | None = None
    export_limit_MW: Decimal | None = None
    export_evidence: Evidence | None = None
    import_limit_MW: Decimal | None = None
    import_evidence: Evidence | None = None


def summarize(snapshot: SharedConnectionSnapshot) -> dict:
    """Count explicit positions within one curated, dated scenario.

    Completeness is a supplied, evidenced assertion, never deduced from list length.
    The caller must resolve historical versions before constructing a snapshot.
    """
    if not snapshot.snapshot_id or not snapshot.connection_id:
        raise ValueError('MISSING_ID')
    date.fromisoformat(snapshot.as_of)
    if snapshot.scenario not in {'CURRENT', 'PLANNED'}:
        raise ValueError('INVALID_SCENARIO')
    if type(snapshot.inventory_complete) is not bool:
        raise ValueError('INVALID_COVERAGE')
    count = snapshot.maximum_positions
    if count is not None and (type(count) is not int or count < 0):
        raise ValueError('INVALID_POSITION_COUNT')
    if count is not None and snapshot.position_evidence is None:
        raise ValueError('MISSING_POSITION_EVIDENCE')
    if snapshot.inventory_complete and snapshot.coverage_evidence is None:
        raise ValueError('MISSING_COVERAGE_EVIDENCE')
    for value, proof in [(snapshot.export_limit_MW, snapshot.export_evidence),
                         (snapshot.import_limit_MW, snapshot.import_evidence)]:
        if value is not None:
            if not isinstance(value, Decimal) or not value.is_finite() or value < 0:
                raise ValueError('INVALID_MW_LIMIT')
            if proof is None:
                raise ValueError('MISSING_LIMIT_EVIDENCE')
    evidence = [p for p in [snapshot.position_evidence, snapshot.coverage_evidence,
                            snapshot.export_evidence, snapshot.import_evidence] if p is not None]
    positions: set[str] = set()
    projects: set[str] = set()
    unresolved = 0
    for assignment in snapshot.assignments:
        if assignment.connection_id != snapshot.connection_id or assignment.scenario != snapshot.scenario:
            raise ValueError('ASSIGNMENT_SCOPE_MISMATCH')
        if not assignment.project_id or type(assignment.confirmed) is not bool:
            raise ValueError('INVALID_ASSIGNMENT')
        if assignment.position_id is not None and not assignment.position_id.strip():
            raise ValueError('EMPTY_POSITION_ID')
        evidence.append(assignment.evidence)
        if assignment.confirmed:
            projects.add(assignment.project_id)
        if not assignment.confirmed or assignment.position_id is None:
            unresolved += 1
            continue
        if assignment.position_id in positions:
            raise ValueError('DUPLICATE_OR_CONFLICTING_POSITION')
        positions.add(assignment.position_id)
    for proof in evidence:
        proof.validate()
    if count is not None and len(positions) > count:
        raise ValueError('ASSIGNMENTS_EXCEED_POSITION_COUNT')
    reasons = []
    if count is None:
        reasons.append('MAXIMUM_POSITIONS_UNKNOWN')
    if not snapshot.inventory_complete:
        reasons.append('INVENTORY_INCOMPLETE')
    if unresolved:
        reasons.append('UNRESOLVED_ASSIGNMENTS')
    unassigned = None if reasons else count - len(positions)
    access = 'PRIVATE' if any(p.access == 'PRIVATE' for p in evidence) else 'PUBLIC'

    def limit(value: Decimal | None, proof: Evidence | None) -> dict:
        return {'value':str(value) if value is not None else None, 'unit':'MW',
                'classification':'REPORTED' if value is not None else 'UNKNOWN',
                'evidence':asdict(proof) if proof is not None else None}

    return {
        'method':'shared_connection_inventory_v1', 'snapshot_id':snapshot.snapshot_id,
        'connection_id':snapshot.connection_id, 'as_of':snapshot.as_of, 'scenario':snapshot.scenario,
        'access':access, 'maximum_positions':count,
        'position_evidence':asdict(snapshot.position_evidence) if snapshot.position_evidence else None,
        'inventory_complete':snapshot.inventory_complete,
        'assignments':[asdict(a) for a in snapshot.assignments],
        'known_assigned_positions':len(positions), 'known_distinct_projects':len(projects),
        'unresolved_assignment_records':unresolved,
        'unassigned_positions':{'value':unassigned,'unit':'position',
            'classification':'CALCULATED' if unassigned is not None else 'UNKNOWN',
            'formula':'maximum_positions - known_assigned_positions' if unassigned is not None else None,
            'reasons':reasons},
        'reported_export_limit':limit(snapshot.export_limit_MW, snapshot.export_evidence),
        'reported_import_limit':limit(snapshot.import_limit_MW, snapshot.import_evidence),
        'available_export_MW':None, 'available_import_MW':None,
        'electrical_capacity_classification':'UNKNOWN', 'power_flow_ready':False,
        'evidence':[asdict(p) for p in evidence],
        'limitations':['Unassigned positions are not an offer of grid connection.',
                      'No completeness, freshness or electrical feasibility inferred from list length.',
                      'MW limits are not remaining connection capacity.']}


def require_public_result(result: dict) -> None:
    """A fail-closed export guard, not authentication or a full access-control system."""
    if result.get('access') != 'PUBLIC' or not result.get('evidence'):
        raise ValueError('PUBLIC_EXPORT_NOT_ALLOWED')
    if any(proof.get('access') != 'PUBLIC' for proof in result['evidence']):
        raise ValueError('PUBLIC_EXPORT_NOT_ALLOWED')
