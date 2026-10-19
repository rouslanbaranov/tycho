# Reusable legacy baseline and modernization worksheet

> Template for [Tycho's legacy evidence model](../authoring/models/legacy-modernization-profile.md), issue [#18](https://github.com/rouslanbaranov/tycho/issues/18). Fill only with authorized system information outside the public Tycho repository; publish here only synthetic or independently public cases. A blank worksheet is not a factual system assessment.

## 1. Identification, decision and evidence control

| Field | Entry |
|---|---|
| Baseline ID / revision / observation period | `<id>` / `<revision>` / `<window and timezone>` |
| Scope and excluded boundaries | `<user journeys, interfaces, data, services, exclusions>` |
| Decision context | `<stabilize, modernize, or evaluate retention>` |
| Responsible roles | `<evidence owner, architect, security, operator, reviewer>` |
| Status | `draft / evidence under review / approved by identified reviewer` |
| Source snapshot | `<repository revision, document section, config and metric window>` |
| Workload profile | [Requirements/workload template](requirements-workload-profile.md) or `unknown` |
| Out-of-date indicators | `<source drift, unsupported version, measurement age, recheck trigger>` |

**Provenance contract:** mark each material statement `observed`, `documented`, `hypothesis`, `assumption` or `unknown`. For a non-public real system, do not transfer company source code, diagrams, architecture or identifiers into Tycho.

## 2. Module, runtime and deployment boundaries

| Component ID / capability | Ownership and ingress/egress | Runtime + exact version/support source | Deployment unit, isolation and scaling limit | Status, evidence and gaps |
|---|---|---|---|---|
| `<COMP-1>` | `<responsibility and callers>` | `<version; source or unknown>` | `<VM/pod/process/function; boundaries>` | `<type; evidence; unknown>` |

Add a **single original Mermaid component diagram** only after establishing actor, state owner, direction and whether each boundary is factual or hypothesized. Explain it textually.

## 3. Data ownership, transactions and integrations

| Data set / interface | Writer and other readers | Local ACID / transaction boundary | Delivery, ordering, retry and identity | Compatibility constraints | Evidence / missing test |
|---|---|---|---|---|---|
| `<DATA/IFACE-1>` | `<owner + consumers>` | `<commit/unknown>` | `<API, event, batch; guarantees/unknown>` | `<versions/overlap>` | `<source>` |

Trace at least one critical journey from request entry through each persisted state transition and external effect. State explicitly whether local commit covers notification or broker publication. Where the design genuinely uses an outbox, the [canonical outbox chapter](../book/distributed/transactional-outbox-and-idempotency.md) owns mechanism semantics; do not assume it is deployed merely because mentioned in this worksheet.

## 4. Observations versus candidate causes

| Observation ID | What users/telemetry showed | Timestamp/window, sample and source | Hypothesized cause | Rival explanation | Falsification or next measurement |
|---|---|---|---|---|---|
| `OBS-1` | `<reproducible symptom>` | `<actual pointer or unknown>` | `<testable hypothesis>` | `<alternative or unknown>` | `<trace/test>` |

**Blocking rule:** a symptom without sufficient causal evidence may justify investigation or stabilization, **not** a forced target pattern (e.g., microservices or sharding).

## 5. Workload, SLOs and operating constraints

Refer to the [requirements/workload model](../authoring/models/requirements-workload-profile.md). Record the actual offered/admitted/completed operation mix, burst duration, hot keys, latency/error distribution, resource bottlenecks and failure classes, or record specific measurement gaps. No fixed RPS/DAU threshold selects an architecture.

| Constraint | Hard gate or preference | Exact window / unit / boundary | Evidence/owner | Acceptance and missing verification |
|---|---|---|---|---|
| `<SLO or invariant>` | `hard / preference` | `<scope and target>` | `<versioned pointer>` | `<method>` |

## 6. Compatibility, downtime, recovery, irreversibility

| Change boundary | Old/new combinations to support | Permitted outage / RPO / RTO (or unknown) | Forward/rollback constraint | Reconciliation invariant and required test |
|---|---|---|---|---|
| `<API/data/consumer>` | `<old-old, old-new, new-old, new-new where meaningful>` | `<approved values or unknown>` | `<irreversible write/unknown>` | `<key and test>` |

If the previous schema cannot read newly committed data, a code rollback alone is not valid. Identify a forward-recovery gate and who can authorize the irreversible step. Never invent a restoration result.

## 7. Proposed modernization goals and exclusions

| Goal ID | Current baseline / evidence state | Measurable target and window | Non-goal / hard constraint | Experiment and gate | Review trigger |
|---|---|---|---|---|---|
| `GOAL-1` | `<value or unknown>` | `<observable business/system outcome>` | `<what must stay unchanged>` | `<reproducible pass/fail>` | `<rollback/reconsider>` |

**Allowable conclusions:** retain and measure; stabilize without decomposition; investigate the missing state/causal boundary; compare target architectures; or select a staged transition after evidence gates. A mandatory restructuring recommendation without decisive evidence is **not** an allowable conclusion.

## 8. Baseline review outcome

- Sources/sections actually inspected (including code revisions): `<links and dates>`
- Open access, license, version and privacy constraints: `<gaps>`
- Semantic review (reviewer, date and result; never invent): `<pending>`
- Reproducible checks actually run: `<command or unrun>`
- Critical unknowns and named verification owners: `<table or links>`
- Decision status: `insufficient evidence / retain / measure / candidate comparison ready`
- Re-evaluation trigger: `<new measurement, release, dependency change, incident>`

The filled version should be tied to a real or deliberately fictional evidence source. For a public Tycho example, use the original fictional workshop baseline already embedded in the [model](../authoring/models/legacy-modernization-profile.md), not an employer architecture.