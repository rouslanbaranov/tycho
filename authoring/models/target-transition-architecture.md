# Target and transition architecture — two distinct contracts

> Tycho E01-05, [issue #21](https://github.com/rouslanbaranov/tycho/issues/21), original authoring method v0.1, 2026-10-19. A target diagram does **not** show how a live system gets there. These are technology-neutral design and validation contracts, not a real migration or a released implementation.

## The separation of concerns

A **target architecture** specifies responsibilities, interfaces, runtime/deployment topology, state ownership, quality scenarios and observable desired end conditions. A **transition architecture** describes real intermediate operating states, order of irreversible effects, coexistence, compatibility, safety hold points and fallback. Both link to the same [requirements/workload profile](requirements-workload-profile.md), the [legacy baseline](legacy-modernization-profile.md) for brownfield change, and an [evidence-backed decision record](candidate-comparison-adr.md). No approved ADR means a proposed target is only a candidate.

Use the [target template](../../templates/target-architecture.md) and the independent [transition template](../../templates/transition-architecture.md). Keep owners explicit and links reversible to canonical book evidence. This is an authoring model, not a frontmatter JSON Schema or graph type.

For the agent-facing staged proposal built on this model, see
[the staged modernization contract](../ROCINANTE-STAGED-MODERNIZATION-CONTRACT.md).

## 1. Target architecture contract

| Domain | Required design statement | Required verification before claiming success |
|---|---|---|
| Capabilities and responsibilities | Functional boundaries, authorized owner, consumers and out-of-scope cases | Requirement-to-responsibility trace and negative case |
| Static components | APIs, services, workers, datastores, caches, queues, control and data planes | Actual ownership/dependency graph, version and code/config snapshot when available |
| State and consistency | Single authoritative writer or explicitly specified coordination; identity, schema/version, transactions and invariants | Race/retry, duplicate/ordering and restoration tests for that chosen contract |
| Runtime/deployment | Zones, processes/containers, connection/queue budgets, scaling and fault domains | Named environment and capacity/failure observations; not a topology illustration alone |
| Security/trust | Authentication, authorization, tenancy, secrets and audit boundaries | Threat-model obligations and actual authorized checks |
| Quality goals | Named eligible user events, deadlines, availability, RPO/RTO, cost and operational burden | Observed/performed tests at the given workload, or explicit pending state |
| Operational ownership | Alerting, runbooks, release/recovery, maintenance and rollback/forward duty | Named staffed roles and exercises, not an inferred capability |

A target may deliberately remain a **modular monolith**. No migration mechanism should be chosen merely because a diagram has multiple boxes.

## 2. Transition states and provenance

Represent each intermediate state as a versioned contract:

| State field | Required content |
|---|---|
| `transition_id / state_id / revision` | Stable identity; predecessors; exact branch/release and immutable artifact when available |
| `live_topology` | Old and new components, routing, active owner of each write, service accounts and caller versions |
| `compatibility_matrix` | Old-client/old-server, old-client/new-server, new-client/old-server, new/new combinations where relevant; defined request/response schema and behavioral semantics |
| `data_path` | Old schema, expanded schema, backfill direction, authoritative writer, CDC/outbox/event offset, read path and reconciliation keys |
| `deployment_guard` | Preflight checks, evidence to enter, canary/exercise blast radius, observation window and rollback limit |
| `exit_guard` | What makes the state complete, verified, and safe to remove; unverified constraints remain blocking |
| `recovery` | Revert code/routing while compatible, or mandatory forward recovery after irreversible data or external effect |
| `provenance` | ADR, requirements, repository revisions, source/experiment scope, review state and incident/revisit triggers |

State transitions can be **rejected** if any hard gate is unknown or failed. Different software versions and data schemas must be modeled together; “run old and new simultaneously” is not a compatibility proof.

## 3. Mixed-version and data migration rules

A safe change is not determined by deployment order alone. Write contracts for readers and writers of old and new data formats, including asynchronous consumers; user-visible errors and retries; schema evolution; authoritative source of truth; and irreversibility.

Suggested **proposed**, not automatic, expansion sequence:

1. **Expand:** introduce additive interface/schema elements while preserving behavior of all currently supported clients and readers. Validate old/new interactions before routing users. Do not assume an additive field is semantically harmless.
2. **Migrate:** switch one class of consumer or one bounded routing slice; backfill with a checkpoint, idempotent/resumable batch identity and reconciliation. A dual-write is a distributed consistency problem, not an acceptable migration default; if unavoidable, document exact atomicity gap and detection/recovery.
3. **Contract:** only after proof that all required readers/writers have migrated and records are reconciled, remove compatibility shims, old fields, routes or subscriptions. Treat deletion and backfill overwrite as potential no-return steps.

Track data-set identity, schema version and migration batch/revision; source/target row/event counts and semantic equality (not just record totals); replay idempotence; lag/timestamps; backfill pause/resume; out-of-order updates and retention horizon. If a restored older binary cannot understand new writes, **rollback of code alone is unsafe**; block rollback and require an explicit forward-recovery procedure.

## 4. Go/no-go and failure-testing boundaries

At each increment, record a **pre-agreed** go/no-go table:

| Gate class | Named action/test | Evidence to capture | NO-GO behavior |
|---|---|---|---|
| Compatibility | Supported old/new client and schema contract tests | Versions, requests, errors and business semantics | Keep prior routes; do not retire readers |
| Invariant correctness | Concurrent writes, retries, duplicates and fault injection | Durable state/reconciliation after injected crash | Stop rollout; reconcile before retry |
| Service quality | Defined offered workload, admitted vs successful operations, latency/error SLI | Actual timestamps, sample and deployment revision | Hold/rollback within proven reversible window |
| Durability/recovery | Restore exercise for selected failure class, approved RPO/RTO | Restore origin, tested path, observations | Forward-repair or remain old; no fabricated RPO/RTO |
| Operational ability | Named on-call, secrets/permissions, alert coverage, runbook | Actual responsible person/system, response rehearsal | Do not proceed to irreversibility without support |

An empty cell is an **unknown**, not an approval. The approval owner, actual decision time and immutable artifact should be recorded; never infer readiness from a green CI job that did not exercise data or rollout scenarios.

## 5. Rollback, forward recovery and the point of no return

Three distinct classes need different actions:

- **Fully reversible:** traffic can be routed back, both binaries can read all relevant states, outstanding work can be replayed/deduplicated, no authoritative irreversible effect occurred. Test recovery with a fault, not by re-reading a playbook.
- **Conditionally reversible:** only for a bounded time before data writes, contract shifts or schema migration make old readers unsafe. Name the gate and freeze/observation window.
- **Forward-recovery only:** old schema no longer represents new valid records, a remote irreversible side effect occurred, or all old consumers have been removed. Revert is not a recovery method; define repair, migration-forward or restore-from-verified-backup path with explicit data-loss bounds.

State recovery targets as actual approved requirements **or unknown**. A 0 RPO target on a slide is not evidence that recovery was tested.

## 6. Original synthetic migration map

~~~mermaid
stateDiagram-v2
    [*] --> Existing: baseline measured
    Existing --> Expand: additive compatibility verified
    Expand --> Coexist: supported old and new readers pass
    Coexist --> Reconcile: bounded backfill with checkpoints
    Reconcile --> Cutover: invariant, lag and restore gates pass
    Cutover --> Target: old paths retired only after evidence
    Expand --> Existing: reversible, no incompatible writes
    Coexist --> Existing: only while rollback guard holds
    Reconcile --> Repair: divergence or crash
    Repair --> Reconcile: resumable replay and recheck
    Cutover --> Repair: irreversible effect / forward recovery
~~~

Text alternative: first establish baseline and compatible expanded interfaces; old and new run in a bounded coexistence state. Backfill and reconciliation precede cutover. Early states may revert only if old software can still read stored data; failures after irreversible effects require explicit repair/forward recovery, not an imaginary code rollback. This is a synthetic planning state machine.

## 7. Public-source boundary and trade-offs

These are **narrow inspected source passages**, not a migration that Tycho performed (inspection 2026-10-19):

| ID | Primary public document and scope | Supports / does NOT prove |
|---|---|---|
| T01 | [arc42, Runtime View §6](https://docs.arc42.org/section-6/), *Content* and *Motivation* | Runtime behavior and failures need scenarios; no proof that any proposed service runs |
| T02 | [arc42, Deployment View §7](https://docs.arc42.org/section-7/), *Content* | Software-to-infrastructure allocation and environment scope; not a performance result |
| T03 | [AWS Prescriptive Guidance, Strangler fig](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html), *Transform, Coexist, Eliminate* and listed disadvantages | Incremental perimeter interception and rollback complications; not automatically applicable to deeply internal components |
| T04 | [AWS Prescriptive Guidance, Branch by abstraction](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html), implementation steps and limitations | Coexistence by internal abstraction when perimeter interception is unavailable; its stated data-consistency limitation precludes blanket guarantees |
| T05 | [Danilo Sato, Parallel Change, Martin Fowler site, 13 May 2014](https://martinfowler.com/bliki/ParallelChange.html), *expand / migrate / contract* and database refactoring applications | Interface and schema compatibility transitions; not a turnkey dual-write consistency protocol |

The safety checks, schema matrix, stage IDs and validation gates above are Tycho's original design prescriptions. They **require actual tests and authorization** to become an approved migration. Specific database engine transactional rules, CDC formats, backup and restore behavior must be read from version-specific primary sources when a real target system is selected.
