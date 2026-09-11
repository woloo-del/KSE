# AGENTS.md

## 1. Project Mission

This repository contains a **Grid Connection Intelligence Platform** for renewable energy, battery storage and hybrid energy projects.

The primary market is Poland, with architecture that should allow future expansion to other European countries.

The system is intended to help answer:

> Given the location and technical parameters of a new PV, Wind, BESS or hybrid project, what is the current grid situation, what other investments compete for the same infrastructure, what constraints exist, and how likely is a technically feasible grid connection?

The system must be:

- data-driven,
- auditable,
- explainable,
- conservative where data is incomplete,
- explicit about uncertainty,
- modular,
- maintainable,
- reproducible.

The system must never present inferred or estimated grid information as confirmed operator data.

---

# 2. Priority Order

When making technical or product decisions, follow this priority:

1. **Data correctness**
2. **Source provenance**
3. **Grid model correctness**
4. **Validation**
5. **Explainability**
6. **Analytics**
7. **Scoring**
8. **Performance**
9. **UI / visual polish**

Do not optimise presentation before the underlying data model is reliable.

---

# 3. Current Development Philosophy

The project should be developed iteratively:

**RESEARCH  
→ DATA DISCOVERY  
→ FEASIBILITY  
→ DATA MODEL  
→ ARCHITECTURE  
→ CONNECTORS  
→ GRID MODEL  
→ ANALYTICS  
→ SCORING  
→ MVP UI  
→ VALIDATION  
→ ITERATION**

Do not skip directly to dashboard development.

The first useful product is a reliable analytical engine, not a visually attractive map.

---

# 4. Repository Awareness

Before making significant changes:

1. inspect the repository structure,
2. inspect existing documentation,
3. inspect existing data schemas,
4. inspect existing connectors,
5. inspect tests,
6. inspect the decision log,
7. understand previous implementation decisions.

Do not create duplicate modules if equivalent functionality already exists.

Prefer extending existing abstractions over creating parallel implementations.

---

# 5. Expected Repository Structure

The repository should broadly follow:

```text
/
├── backend/
├── frontend/
├── connectors/
│   ├── pse/
│   ├── pge/
│   ├── enea/
│   ├── tauron/
│   ├── energa/
│   ├── stoen/
│   ├── entsoe/
│   ├── bip/
│   └── gis/
├── data/
│   ├── raw/
│   ├── staging/
│   ├── processed/
│   ├── reference/
│   └── catalog/
├── database/
├── grid_engine/
├── scoring/
├── gis/
├── scripts/
├── tests/
├── docs/
├── config/
├── README.md
└── AGENTS.md
```

This structure may evolve if technically justified.

Any substantial structural change must be documented in:

```text
/docs/decision_log.md
```

---

# 6. Core Domain Model

The system should model the electrical grid as interconnected entities.

Core entities include:

```text
GRID_NODE
SUBSTATION
GPZ
BUS
TRANSFORMER
LINE
FEEDER
PROJECT
GENERATION_ASSET
STORAGE_ASSET
DEMAND_ASSET
CONNECTION_POINT
GRID_INVESTMENT
OPERATOR
SOURCE
OBSERVATION
```

Typical relationship:

```text
PROJECT
  ↓
CONNECTION_POINT
  ↓
FEEDER / LINE
  ↓
GPZ / SUBSTATION
  ↓
110 kV NETWORK
  ↓
PSE SUBSTATION
  ↓
220 / 400 kV NETWORK
```

Do not assume that every relationship is known.

Relationships may have:

```text
confirmed
probable
inferred
unknown
```

status.

---

# 7. Energy Project Types

The application must support:

```text
PV
WIND
BESS
PV + BESS
WIND + BESS
PV + WIND
PV + WIND + BESS
OTHER HYBRID
DEMAND
DATA CENTER
ELECTROLYSER / HYDROGEN
```

Do not reduce every project to a single installed MW value.

---

# 8. BESS Modelling Rules

Battery Energy Storage Systems must be modelled differently from generators.

A BESS should support at least:

```text
P_export_MW
P_import_MW
energy_capacity_MWh
duration_h
PCC_export_limit_MW
PCC_import_limit_MW
```

Grid impact must be analysed separately for:

```text
CHARGING
DISCHARGING
```

Do not assume:

```text
50 MW BESS = 50 MW PV
```

The system should distinguish between:

```text
generation constraint
demand constraint
```

where possible.

---

# 9. Hybrid and Cable Pooling Rules

Always distinguish:

```text
installed_generation_capacity
installed_storage_capacity
maximum_export_at_PCC
maximum_import_at_PCC
```

Example:

```text
PV = 30 MW
BESS = 30 MW
PCC export limit = 30 MW
```

must not automatically be interpreted as:

```text
60 MW export
```

The grid model must respect PCC constraints and operating scenarios.

---

# 10. Voltage Levels

At minimum, distinguish:

```text
LV
SN / MV
110 kV
220 kV
400 kV
```

Never aggregate technical conclusions across voltage levels without justification.

The availability and quality of data may differ significantly between:

- SN,
- 110 kV,
- 220 kV,
- 400 kV.

Confidence should reflect this.

---

# 11. Data Provenance — Mandatory

Every significant data point must be traceable to a source.

Where possible, records should include:

```text
source_id
source_url
source_owner
source_title
source_document
source_page
source_date
retrieval_date
valid_from
valid_to
source_version
source_quality
```

No important grid parameter should exist in the analytical layer without provenance.

---

# 12. Data Classification

Every value exposed by the system must be classified as one of:

```text
REPORTED
MEASURED
CALCULATED
ESTIMATED
INFERRED
UNKNOWN
```

Definitions:

### REPORTED

Explicitly published by an authoritative source.

Example:

```text
Transformer rated power = 63 MVA
```

from an operator document.

### MEASURED

Derived directly from telemetry or measurement data.

### CALCULATED

Deterministically calculated from known inputs.

The formula and input values must be available.

### ESTIMATED

Produced by an approximation model.

The methodology and confidence must be available.

### INFERRED

Derived from indirect evidence.

Example:

A project is likely connected to GPZ X based on:

- geographic proximity,
- voltage,
- published connection document,
- line topology.

### UNKNOWN

There is insufficient evidence.

Use `UNKNOWN` instead of inventing a value.

---

# 13. No Hallucinated Grid Data

This is a critical project rule.

Never invent:

- transformer ratings,
- line capacities,
- line lengths,
- voltage levels,
- bus topology,
- project connection points,
- available connection capacity,
- grid loading,
- project status,
- connection conditions,
- operator investment dates.

If a value cannot be established:

```text
value = null
status = UNKNOWN
```

is preferable to an unsupported estimate.

If estimation is justified, mark it explicitly as:

```text
ESTIMATED
```

and store:

```text
method
inputs
assumptions
confidence
```

---

# 14. Source Hierarchy

Use approximately the following source priority:

```text
A — official operator structured data / official API
B — official operator document
C — official administrative document / BIP
D — official company / investor publication
E — reliable industry source
F — media
G — community / open-source inference
H — model inference
```

This hierarchy may be refined later.

When sources conflict, do not silently choose one.

Store the conflict where practical.

Prefer the most authoritative and most recent source, but retain historical evidence.

---

# 15. Historical Data

Do not destructively overwrite grid information.

Where appropriate, preserve:

```text
source_date
retrieval_date
valid_from
valid_to
version
```

The system should eventually be able to answer:

> What did we know about this node on a specific historical date?

---

# 16. Source Discovery Rules

When researching new data sources, explicitly check for:

```text
API
REST API
WMS
WFS
WMTS
ArcGIS REST
GeoJSON
JSON
CSV
XLSX
XML
HTML
PDF
BIP
open data portal
GitHub repository
```

Prefer machine-readable sources over document parsing.

Preferred order:

```text
official API
↓
official structured download
↓
official GIS service
↓
official HTML
↓
official XLSX / CSV
↓
official PDF
↓
scraping
↓
secondary sources
```

---

# 17. Data Source Registry

Every relevant source should be registered in:

```text
/data/catalog/data_sources.*
```

and documented in:

```text
/docs/01_data_research.md
```

Recommended fields:

```text
source_id
operator
source_name
url
data_owner
country
data_category
voltage_level
geographical_scope
format
api_available
gis_available
update_frequency
historical_data
authentication
license
commercial_use
machine_readable
scraping_required
reliability
data_quality_score
key_fields
known_limitations
priority
last_verified
```

---

# 18. Connector Architecture

Operator-specific data ingestion belongs in:

```text
/connectors/
```

Use modular connectors such as:

```text
connectors/pse/
connectors/pge/
connectors/enea/
connectors/tauron/
connectors/energa/
connectors/stoen/
connectors/entsoe/
connectors/bip/
connectors/gis/
```

A connector should conceptually implement:

```text
fetch()
parse()
normalize()
validate()
store()
```

Do not mix operator-specific extraction logic with grid scoring logic.

---

# 19. Preserve Raw Data

When technically and legally possible, keep the original downloaded source in:

```text
/data/raw/
```

Do not modify raw source files.

Transformations should follow:

```text
RAW
↓
STAGING
↓
NORMALIZED
↓
ANALYTICAL
```

This allows the ingestion pipeline to be audited and reproduced.

---

# 20. File Naming

Use deterministic and readable names.

Example:

```text
pse_available_capacity_2026-09-10.xlsx
pge_development_plan_2026_2031.pdf
energa_grid_nodes_2026-09-10.geojson
```

Avoid names such as:

```text
data2.csv
final.xlsx
new_final2.json
```

---

# 21. Units

Store units explicitly.

Preferred standard internal units:

```text
Power: MW
Energy: MWh
Voltage: kV
Apparent power: MVA
Current: A
Distance: km or m
Coordinates: EPSG:4326 unless explicitly stated otherwise
```

Never silently mix:

```text
W
kW
MW
GW
```

or:

```text
VA
kVA
MVA
```

Unit conversion must be explicit and tested.

---

# 22. Coordinate Systems

For geospatial ingestion:

- preserve original CRS metadata,
- normalize analytical coordinates where appropriate,
- use EPSG identifiers,
- do not assume every GIS source uses EPSG:4326.

Polish GIS sources may use coordinate systems such as:

```text
EPSG:2180
```

Transform coordinates explicitly.

---

# 23. Entity Resolution

The same grid entity may appear under several names.

Example:

```text
GPZ Radkowice
SE Radkowice
Radkowice 110 kV
RADKOWICE
```

Use:

```text
canonical_id
canonical_name
aliases
operator_id
coordinates
voltage
operator
```

for entity resolution.

Matching may use:

```text
exact identifiers
normalized names
geographic proximity
operator
voltage
topology
fuzzy matching
```

Never merge entities based solely on fuzzy name similarity.

Ambiguous matches must retain an uncertainty indicator.

---

# 24. Project Entity Resolution

The same project may appear under:

- investor name,
- SPV name,
- project name,
- cadastral location,
- municipality,
- connection point,
- environmental decision name.

Avoid duplicate project records.

Track aliases and source-specific identifiers.

---

# 25. Grid Topology

Network topology should support at least:

```text
NODE
EDGE
TRANSFORMER
PROJECT
```

Each relationship should ideally include:

```text
source
confidence
validity period
```

Do not infer topology solely from visual map proximity unless clearly marked as inferred.

---

# 26. Grid Capacity Analysis

Never define available grid capacity simply as:

```text
transformer_capacity - installed_generation
```

unless explicitly presented as a crude screening metric.

A meaningful analysis may eventually consider:

```text
transformer capacity
line thermal rating
generation
demand
simultaneity
reverse flow
BESS charging
BESS discharging
N-1
voltage constraints
grid topology
planned projects
issued connection conditions
contracted connections
curtailment
redispatching
historical load
planned reinforcements
```

If only some variables are available, explicitly state the analytical limitations.

---

# 27. Power Flow

Do not run power-flow calculations simply because a topology can be drawn.

A valid power-flow model requires sufficient electrical parameters.

Check for availability of at least relevant:

```text
bus data
line impedance
line limits
transformer data
generation
load
topology
operational assumptions
```

If electrical parameters are insufficient, use a heuristic analytical model instead.

Label it accordingly.

Potential libraries to evaluate include:

```text
pandapower
PyPSA
GridCal
```

Do not introduce a library unless it materially improves the project.

---

# 28. Grid Connection Score

The project will eventually include:

```text
Grid Connection Score: 0–100
```

Do not invent arbitrary weights prematurely.

The score must be based on variables that can actually be sourced or responsibly estimated.

Possible factors include:

```text
available capacity
project pipeline
transformer utilisation
line utilisation
generation concentration
demand
planned reinforcements
curtailment
redispatching
connection refusals
connection conditions
distance
voltage level
network topology
BESS flexibility
data confidence
```

Every score must be explainable.

The system should be able to answer:

```text
Why did this project receive 43/100?
```

---

# 29. Separate Score and Confidence

Never conflate:

```text
Grid Connection Score
```

with:

```text
Data Confidence Score
```

Example:

```text
Grid Connection Score: 78 / 100
Data Confidence: 41%
```

means:

the available evidence suggests a favourable connection situation, but available information is incomplete.

Both measures are necessary.

---

# 30. Confidence Model

Confidence should consider factors such as:

```text
source authority
source recency
source completeness
topology certainty
coverage of competing projects
availability of technical parameters
availability of operational data
consistency between sources
```

Prefer explainable confidence calculation over opaque machine-learning output.

---

# 31. Scenario Analysis

Where relevant, analysis should support:

```text
CURRENT GRID
FUTURE GRID
BASE CASE
CONSERVATIVE
OPTIMISTIC
```

For BESS additionally:

```text
CHARGING CASE
DISCHARGING CASE
```

For hybrid projects include PCC constraints.

---

# 32. Future Grid

Operator network investments should be represented separately from existing assets.

Possible states:

```text
existing
planned
under_construction
commissioned
cancelled
unknown
```

Store expected dates where available.

Do not treat a planned reinforcement as existing capacity.

---

# 33. Competition for Connection Capacity

A key analytical function is determining projects potentially competing for the same grid infrastructure.

Relevant projects may include:

```text
PV
Wind
BESS
hybrids
large industrial loads
data centers
hydrogen / electrolysers
other large demand projects
```

Competition may occur at:

```text
feeder
GPZ
transformer
110 kV line
PSE node
regional network
```

Do not assume projects connected to geographically nearby substations necessarily compete for the same constraint.

Topology matters.

---

# 34. Status of Projects

Project lifecycle should be represented explicitly where evidence permits.

Potential statuses:

```text
identified
planned
administrative_proceedings
connection_conditions
connection_agreement
permitted
under_construction
operational
cancelled
unknown
```

Do not infer advanced project status from a single early administrative notice.

---

# 35. Data Quality Validation

Each ingestion pipeline must include validation appropriate to the source.

Tests should include where relevant:

```text
schema validation
type validation
unit validation
range checks
null checks
duplicate detection
coordinate validation
voltage consistency
temporal consistency
historical anomaly detection
cross-source validation
```

Example:

A transformer rating of:

```text
6300 MVA
```

at a normal GPZ should trigger review rather than silently enter the database.

---

# 36. Parser Testing

Every important parser should have tests.

Where possible keep representative source fixtures.

Example:

```text
tests/fixtures/pse/
tests/fixtures/pge/
```

A change in an operator website should cause:

```text
test failure
```

or:

```text
validation warning
```

rather than silent corruption.

---

# 37. Error Handling

Never silently ignore ingestion errors.

Classify errors where practical:

```text
FETCH_ERROR
PARSE_ERROR
SCHEMA_ERROR
VALIDATION_ERROR
SOURCE_CHANGED
RATE_LIMITED
AUTH_ERROR
UNKNOWN_ERROR
```

Store sufficient diagnostic information.

Do not expose sensitive local environment information in user-facing logs.

---

# 38. Scraping

Scraping should be used only when more stable structured interfaces are unavailable.

Before implementing scraping:

1. check for an API,
2. inspect network requests where appropriate,
3. check for GIS services,
4. check for downloadable structured files,
5. check applicable terms and restrictions.

Scrapers should be resilient to minor HTML changes.

Avoid brittle selectors where alternatives exist.

---

# 39. Licensing

For every important external dataset, investigate:

```text
license
redistribution rights
commercial use
attribution requirements
rate limits
terms of service
```

Do not assume that public accessibility automatically permits unrestricted commercial reuse.

Document limitations.

---

# 40. Secrets

Never commit:

```text
API keys
passwords
tokens
private credentials
private database URLs
```

Use:

```text
.env
```

and provide:

```text
.env.example
```

with placeholder values.

Ensure `.env` is ignored by Git.

---

# 41. Technology Stack

Preferred technologies to consider:

Backend:

```text
Python
FastAPI
```

Data processing:

```text
Pandas
Polars
GeoPandas
```

Database:

```text
PostgreSQL
PostGIS
```

Grid modelling:

```text
pandapower
PyPSA
```

Frontend:

```text
React
Next.js
```

Mapping:

```text
MapLibre
Leaflet
```

Infrastructure:

```text
Docker
```

These are preferences, not mandatory constraints.

Do not introduce unnecessary infrastructure.

For MVP, prefer operational simplicity.

---

# 42. Database Choice

Default preference for MVP:

```text
PostgreSQL + PostGIS
```

Do not introduce Neo4j only because the network can be represented as a graph.

Evaluate whether relational topology tables are sufficient.

Consider:

```text
PostGIS
pgRouting
```

before adding another persistent database.

Major architecture decisions must be recorded in the decision log.

---

# 43. Database Design

Prefer stable canonical IDs.

Avoid using human-readable names as primary keys.

Example:

```text
substation_id
line_id
transformer_id
project_id
source_id
```

External operator identifiers should be preserved separately.

---

# 44. API Design

Backend endpoints should expose clear domain resources.

Possible future examples:

```text
/nodes
/substations
/lines
/transformers
/projects
/grid-investments
/sources
/analysis/grid-connection
/analysis/node
/analysis/project
```

Do not expose raw database structures directly as the long-term API contract.

---

# 45. Separation of Concerns

Keep separate:

```text
data ingestion
normalization
database
grid topology
analytical calculations
scoring
API
frontend
```

Do not place grid calculation logic inside UI components.

Do not place web scraping inside analytical modules.

---

# 46. Configuration

Source URLs and operator-specific settings should be configurable.

Prefer:

```text
/config/
```

or structured environment configuration.

Avoid scattering URLs and magic constants across the codebase.

---

# 47. No Magic Numbers

Grid calculations and scoring must not contain unexplained constants such as:

```python
score += 17
```

Every threshold or coefficient must be:

- named,
- documented,
- justified,
- configurable where appropriate.

---

# 48. Explainability

Every analytical result should ideally support a structure similar to:

```json
{
  "value": 42,
  "unit": "MW",
  "classification": "ESTIMATED",
  "confidence": 0.68,
  "method": "...",
  "inputs": [],
  "assumptions": [],
  "sources": []
}
```

The user should be able to inspect why a result was produced.

---

# 49. UI Principle

The primary UI should eventually support a map, but the map is not the source of truth.

The UI should allow the user to inspect:

```text
grid asset
technical parameters
sources
connected projects
competing projects
known capacity
estimated capacity
planned upgrades
confidence
grid connection score
```

Avoid presenting complex analytical conclusions solely through colours.

Always make key numerical and textual evidence available.

---

# 50. User Input Model

The analysis engine should eventually accept project parameters such as:

```text
technology
coordinates
connection_voltage
P_export
P_import
energy_capacity
PCC_limit
preferred_connection_point
project_status
target_connection_date
```

User input should not overwrite external source data.

Store project scenarios separately.

---

# 51. Candidate Connection Points

Eventually, the system should be capable of identifying alternative candidate connection points.

Ranking may consider:

```text
distance
voltage
network strength
known available capacity
known pipeline
planned upgrades
connection complexity
route feasibility
data confidence
```

Do not rank solely by straight-line distance.

---

# 52. Spatial Constraints

Future spatial analysis may consider:

```text
cadastral parcels
land ownership constraints
roads
railways
rivers
protected areas
forests
flood zones
settlements
terrain
existing infrastructure
```

Do not mix these constraints into the electrical grid model itself.

Create a separate spatial feasibility layer.

---

# 53. Documentation

Maintain at least:

```text
README.md

docs/
  01_data_research.md
  02_feasibility_matrix.md
  03_system_architecture.md
  04_data_model.md
  05_grid_capacity_methodology.md
  06_scoring_methodology.md
  07_data_quality.md
  08_roadmap.md
  decision_log.md
```

Documentation should evolve together with implementation.

---

# 54. Decision Log

For significant technical decisions update:

```text
/docs/decision_log.md
```

Use:

```text
Date:
Decision:
Context:
Options considered:
Selected option:
Reason:
Trade-offs:
Consequences:
```

Examples requiring documentation:

- database architecture,
- grid graph representation,
- major library selection,
- scoring methodology,
- confidence methodology,
- data source replacement,
- substantial schema changes.

---

# 55. Research Documentation

When researching sources, record:

```text
URL
owner
date checked
data available
format
update frequency
access method
licensing
technical limitations
reliability
intended use
```

Do not merely bookmark URLs.

Explain what each source contributes to the system.

---

# 56. Feasibility Classification

Before implementing a major analytical feature classify it as:

```text
AVAILABLE_DIRECTLY
CALCULABLE
ESTIMABLE
NOT_CURRENTLY_AVAILABLE
```

This classification should be evidence-based.

Example:

```text
Real-time GPZ transformer utilisation:
NOT_CURRENTLY_AVAILABLE
```

is a valid conclusion.

Do not implement artificial precision because a business requirement asks for a value.

---

# 57. Uncertainty

Prefer ranges when the underlying data does not justify a point estimate.

Better:

```text
Estimated available export capacity:
20–45 MW
```

than:

```text
Available capacity:
34.72 MW
```

when inputs are incomplete.

Avoid false precision.

---

# 58. Dates

Always distinguish:

```text
publication date
effective date
retrieval date
observation date
planned commissioning date
```

When analysing changing grid conditions, use the relevant temporal context.

---

# 59. Current vs Future State

Never mix:

```text
current installed infrastructure
```

with:

```text
planned infrastructure
```

without explicit scenario labelling.

Example:

```text
CURRENT GRID — 2026
FUTURE GRID — 2030
```

---

# 60. Testing Requirements

Before considering a task complete:

- run relevant tests,
- run formatting/linting where configured,
- verify modified parsers against sample data,
- verify schemas,
- check for obvious regressions.

Do not claim tests passed unless they were actually executed.

If tests cannot be run, state why.

---

# 61. Code Quality

Prefer:

- small focused modules,
- explicit typing,
- clear domain names,
- pure analytical functions where practical,
- reusable parsers,
- documented schemas.

Avoid:

- giant files,
- global mutable state,
- deeply nested control flow,
- copy-paste connectors,
- undocumented side effects.

---

# 62. Python

For Python code:

- use type hints,
- prefer dataclasses or validated models for domain structures,
- consider Pydantic for API/data validation,
- isolate I/O from transformation logic,
- write testable functions.

Do not use notebook-only implementation for production functionality.

Notebooks may be used for exploration.

---

# 63. DataFrames

Use DataFrames where they are appropriate for transformations.

Do not use Pandas as a substitute for a proper domain/database model once data becomes persistent.

For large pipelines, evaluate Polars when there is a measurable benefit.

---

# 64. Performance

Correctness comes before optimisation.

Do not optimise prematurely.

However, avoid obviously inefficient patterns such as:

- loading entire large datasets repeatedly,
- repeated network requests for unchanged resources,
- unindexed spatial queries,
- N+1 database access.

Cache raw external data where legally and technically appropriate.

---

# 65. Logging

Use structured logging where practical.

Important events include:

```text
source fetched
source changed
parser succeeded
parser failed
validation failed
records inserted
records updated
entity match uncertain
analysis executed
```

Avoid verbose logging of every trivial loop operation.

---

# 66. Reproducibility

An analytical result should be reproducible using:

```text
input project parameters
data snapshot
method version
configuration
analysis timestamp
```

Where possible assign methodology versions such as:

```text
grid_capacity_method = "heuristic_v0.2"
connection_score_method = "score_v0.1"
```

---

# 67. Method Versioning

Changes to analytical methodology should not silently reinterpret historical results.

Record methodology versions.

Major scoring changes should be documented.

---

# 68. Security

This system may eventually hold commercially sensitive project data.

Design with separation between:

```text
public external data
internal project data
user input
derived analytics
```

Do not expose internal project information through public endpoints.

---

# 69. External Requests

Respect:

- rate limits,
- retries,
- timeout handling,
- caching,
- source availability.

Implement exponential backoff where appropriate.

Do not aggressively scrape operator websites.

---

# 70. Git Discipline

Prefer small coherent commits when committing is part of the workflow.

Do not commit:

```text
.env
credentials
large temporary datasets
generated caches
node_modules
Python virtual environments
```

Keep `.gitignore` current.

---

# 71. Dependency Discipline

Before adding a dependency ask:

1. Is it already available?
2. Is it necessary?
3. Is it maintained?
4. Does its licence allow intended use?
5. Can the task be solved reliably without it?

Avoid unnecessary dependency growth.

---

# 72. Research Before Dependency Choice

Do not automatically use:

```text
Neo4j
Airflow
Kafka
Kubernetes
Spark
```

because they are common infrastructure technologies.

Introduce them only when project scale or requirements justify them.

For the initial system, prefer:

```text
simple
local
observable
testable
replaceable
```

components.

---

# 73. MVP Philosophy

MVP should prove:

1. we can reliably ingest relevant grid data,
2. we can resolve grid entities,
3. we can represent basic topology,
4. we can associate competing projects with infrastructure,
5. we can generate a defensible grid-connection assessment.

MVP does not need nationwide perfect coverage.

A high-quality pilot region is preferable to unreliable nationwide data.

---

# 74. Proof-of-Concept Region

For early implementation, choose one representative area containing:

- at least one GPZ,
- 110 kV infrastructure,
- generation projects,
- available public data,
- preferably a nearby PSE node.

Build a real model using real data.

Do not use fabricated sample infrastructure except inside explicit tests.

---

# 75. Synthetic Data

Synthetic data is allowed only for:

- unit tests,
- UI development,
- isolated algorithm tests.

Synthetic records must be clearly marked.

Never mix synthetic data with production analytical outputs.

---

# 76. Communication With the User

Do not ask for approval for minor implementation decisions.

Proceed autonomously with:

- file organisation,
- tests,
- refactoring,
- naming,
- implementation details.

Ask or flag decisions when they materially affect:

- business logic,
- interpretation of grid data,
- scoring methodology,
- confidence methodology,
- project scope,
- major architecture,
- external licensing constraints.

When uncertainty exists but implementation can safely continue, document the assumption and proceed.

---

# 77. Before Starting a Major Task

Before major implementation:

1. understand the goal,
2. inspect existing code,
3. inspect relevant documentation,
4. identify available data,
5. identify uncertainty,
6. decide whether the task is research, ingestion, modelling, analytics or UI,
7. modify the smallest appropriate part of the system.

---

# 78. After Completing a Major Task

Provide a concise summary containing:

```text
What was done
Files changed
Tests performed
Key findings
Known limitations
Recommended next step
```

Do not claim functionality beyond what was actually implemented.

---

# 79. Research Integrity

When conducting external research:

- verify important facts against primary sources,
- prefer current documentation,
- record the verification date,
- distinguish outdated documents from current data,
- do not rely on search snippets as evidence,
- investigate whether structured underlying data exists.

For key technical parameters, use multiple-source verification when possible.

---

# 80. Conflicting Sources

If sources disagree:

Do not silently average or overwrite values.

Store or report:

```text
Source A:
value

Source B:
value

Likely explanation:
...

Preferred value:
...

Confidence:
...
```

where practical.

---

# 81. Negative Findings Are Valuable

Examples:

```text
No public transformer loading data found.
```

```text
No reliable mapping between MV feeders and projects is available.
```

```text
Available capacity cannot be reconstructed accurately from public sources.
```

These are valid research conclusions.

Do not invent workarounds solely to satisfy the desired product concept.

---

# 82. Avoid False Precision

If data supports only qualitative assessment, use:

```text
LOW
MEDIUM
HIGH
```

rather than artificially precise values.

Numerical scoring should only be introduced when methodology supports it.

---

# 83. Analytical Evidence

An analysis should ideally distinguish:

```text
FACTS
CALCULATIONS
ASSUMPTIONS
INFERENCES
RISKS
UNKNOWN VARIABLES
```

This distinction should eventually be visible to the user.

---

# 84. Grid Engineering Caution

A commercial connection assessment is not equivalent to an official connection study performed by the operator.

The platform should be presented as:

```text
screening
intelligence
decision support
connection opportunity assessment
```

not as a replacement for:

- OSD/OSP grid studies,
- official connection conditions,
- power-system engineering studies required by operators.

---

# 85. Main Product Principle

The platform must answer not only:

> What infrastructure exists here?

but primarily:

> What does the available evidence imply for the connection prospects of this specific project?

All development should remain aligned with this objective.

---

# 86. Current Execution Rule

Unless explicitly instructed otherwise, work in this order:

```text
1. Verify available evidence
2. Improve data acquisition
3. Improve data quality
4. Improve topology
5. Improve analytical methodology
6. Improve scoring
7. Improve UI
```

If asked to implement a feature that depends on unavailable data, first verify whether that data can actually be obtained.

---

# 87. Definition of Done

A feature is not complete simply because code executes.

A feature is complete when:

```text
implementation exists
+
source data is traceable
+
validation exists
+
tests exist where appropriate
+
limitations are documented
+
output is explainable
```

---

# 88. Final Non-Negotiable Rules

Never:

1. fabricate grid data,
2. hide uncertainty,
3. present estimates as operator data,
4. confuse project MW with network capacity,
5. treat BESS exactly like generation,
6. ignore PCC limits for hybrid systems,
7. treat planned infrastructure as existing infrastructure,
8. silently overwrite historical data,
9. use undocumented scoring weights,
10. report tests as passed without running them,
11. prioritise dashboard appearance over data integrity,
12. assume geographic proximity proves electrical connectivity,
13. assume publicly visible data can automatically be commercially reused,
14. create artificial numerical precision unsupported by evidence.

Always:

1. cite data provenance,
2. preserve uncertainty,
3. validate inputs,
4. preserve original source evidence,
5. document material decisions,
6. prefer primary sources,
7. keep analytical logic explainable,
8. maintain modular architecture,
9. distinguish current and future grid scenarios,
10. treat data quality as part of the product.

---

# 89. Immediate Project Objective

Until the research and feasibility phases are completed, focus primarily on:

```text
DATA DISCOVERY
DATA CATALOGUE
SOURCE VALIDATION
LICENSING
CONNECTOR FEASIBILITY
TOPOLOGY FEASIBILITY
GRID CAPACITY FEASIBILITY
```

Do not spend substantial effort building the production frontend yet.

The first major project milestone is a defensible answer to:

> Can a reliable Grid Connection Intelligence Platform for Poland be built from currently accessible data, and what realistic analytical accuracy can be achieved for MV, 110 kV and PSE 220/400 kV networks?

---

# 90. Versioning and Reproducibility — User Request 2026-09-10

Version project documentation, code, configuration, source catalogs, dependency versions and audit manifests in Git. The private remote is `https://github.com/woloo-del/KSE.git`.

After a coherent, validated work increment, create a descriptive local commit when Git identity and access are configured. Report its identifier. Push when the user requests sending changes; distinguish a local commit from a successful push. Never force-push to resolve an ordinary synchronization problem.

Preserve exact raw input bytes in immutable, checksummed snapshots. Large raw datasets and generated caches are not ordinary Git contents. Record the archive manifest in Git and maintain a separate private backup of the source archive; do not claim that URLs and hashes alone reproduce a changed historical source. See `docs/reproducibility.md` and `docs/git_workflow.md`.

---

# 91. TODO and Project Reports — User Request 2026-09-10

Maintain `data/project/todo.json` as the authoritative task register. Preserve stable task IDs, dependencies, priorities, next actions, acceptance criteria and completion evidence. Update it as work progresses; never mark a task complete only because its specification exists. Do not invent deadlines. Retain completed tasks and Git history.

`TODO.md` and the detailed Excel report are generated views. Use `scripts/generate_project_report.ps1` to refresh them at reporting milestones or when requested. Keep task changes in the JSON, not only in Excel. Clearly distinguish a generated snapshot from live source data. Reporting scripts must read an explicit list of project files and must not read `_secrets`, credentials, or arbitrary environment contents.
