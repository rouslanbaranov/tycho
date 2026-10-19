# Legacy baseline and modernization profile — evidence-first contract

> Issue [#18](https://github.com/rouslanbaranov/tycho/issues/18), E01-02 / M1. Original decision-method model v0.1, prepared 2026-10-19. This is NOT a description of an employer or real legacy system, not a deployed migration, and not a substitute for a measured workload. Source review and synthetic example are identified below.

## Why an existing system is not a greenfield problem

A modernization recommendation is invalid if it describes only a desired target architecture and ignores the current enforceable interfaces, state ownership, transactional guarantees, unsupported runtime components or the process for getting safely from current to target. First record a **versioned current-state baseline**. Keep this separate from the existing [requirements/workload profile](requirements-workload-profile.md), which describes demand, objectives, quality scenarios and unknowns.

A baseline can be incomplete without being fictional: use `unknown` and an evidence task rather than substituting an architectural assumption. The label *monolith* does not itself prove performance, maintainability, scale or reliability problems.

## 1. Identity, evidence quality and decision boundary

Every baseline records:

| Field | Contract |
|---|---|
| `baseline_id`, `revision`, `observed_at` | Stable local identifier, revision and observation window; no invented timestamp or unapproved YAML schema |
| `scope` | User/business journey, ingress/egress and components included/excluded |
| `owner_and_review` | Accountable roles and explicit review status, not inferred approval |
| `source_snapshot` | Repository revision(s), public docs/section, artifact/check/build versions and measurement interval where legally accessible |
| `truth_type` | `observed`, `documented`, `hypothesis`, `assumed`, or `unknown` at EACH material claim |
| `confidence_and_age` | What may have drifted and how to re-check it |
| `decision_problem` | Modernize for a measurable need, retain, stabilize, or investigate; target design is NOT an input premise |

Never treat a diagram or stakeholder recollection as measured production evidence. If access is unavailable, use a question/validation plan, not an invented code inventory.

## 2. Current-state map and enforceable boundaries

Map these **separately** rather than collapsing them into a single technology inventory:

| Dimension | Minimum baseline evidence | What must not be inferred |
|---|---|---|
| Functional modules | Capability owner, API/UI surface, dependency direction, change coupling and deployment unit | Package names alone establish runtime isolation |
| Runtime and dependencies | Exact version, support status with vendor reference, deployment topology, start/stop mode, upgrade blockers and library compatibility | A technology is obsolete merely because it is old |
| Integration | Synchronous API/event/file/interface consumers, contract versions, authentication and backwards compatibility | A caller may be updated atomically with the callee |
| Data ownership | Database/schemas, writers, key identity, retention, external readers, replication and data migrations | A new service automatically owns its old shared tables |
| Transaction boundaries | Local commit domain, calls made before/after commit, outbox or broker responsibility, duplicate and ordering semantics | An HTTP success implies cross-system exactly-once effect |
| Execution/workload | Offered/admitted RPS, business TPS, latency tails, failure windows, bounded pools, resource and queue telemetry | More threads or replicas guarantee useful capacity |
| Operability | Test coverage by critical path, monitoring, deploy frequency, rollback mechanism and restoration exercise | A rollback plan is feasible without a mixed-version/data test |
| Security and compliance | Principal, authorization boundary, secret flow, data classification, audit trail and explicit obligations | A new network boundary implies security isolation |

A valid baseline names missing source/evidence for each answer. Treat shared databases and cross-process transactions as decision-critical constraints until disproven, not generic anti-pattern labels.

## 3. Observations, hypotheses and the evidence gap

Use this problem register, never a free-form `legacy problems` list:

| ID | User-observed or instrumented symptom | Evidence and window | Candidate cause (**hypothesis**) | Rival explanation | Test that distinguishes them |
|---|---|---|---|---|---|
| `OBS-n` | Timestamped event, measured ratio, confirmed bug or reproducible failure | Immutable/revisitable pointer; sampling limits | Optional, explicitly testable | At least one plausible alternative or `unknown` | A concrete measurement, trace, controlled fault or code inspection |

**Decision rule:** a reported slowdown justifies investigating throughput/latency and queue location. It does NOT prove that the system needs microservices, Kafka, distributed caching or sharding. Confidence follows the evidence, not the preferred solution.

## 4. Nonnegotiable coexistence and transition constraints

Record required **behavioral compatibility** (status codes, schemas, contracts, authentication, ordering, data meaning), old/new client overlap, maximum coexistence duration, release window, allowable outage and RPO/RTO *per named failure class*. Include migration reversibility, parallel writes, reconciliation keys, retention and data ownership transitions. If reverting code cannot undo a new persisted schema or external side effect, specify forward recovery and a no-return gate; the word `rollback` is insufficient.

For each proposed migration increment, require:

1. **Precondition:** source snapshot, affected consumers, interface contract, observability and named invariants.
2. **Change:** single bounded capability/interface/data owner; what remains old and what becomes new.
3. **Compatibility evidence:** old-old, old-new, new-old and new-new combinations where relevant; required backfill/reconciliation.
4. **Safety gate:** synthetic/integration/concurrency/failure exercise, pre-declared success and rollback/forward-recovery triggers.
5. **Exit:** transition owner, measurable outcome and explicit condition before retiring old paths.

Do not automatically choose a strangler proxy: a perimeter may be un-interceptable; a branch-by-abstraction change inside the monolith or simply maintaining a modular monolith can be safer. The ability to operate both versions is a **measured dependency**, not a style preference.

## 5. Outcomes, hard constraints, non-goals and acceptance

Link each modernization objective to the established [requirements profile](requirements-workload-profile.md). Declare baseline metric (or `unknown`), target, units, numerator/denominator, environment, measurement window, sampling/exclusions, user impact, owner and expiration/revisit trigger.

| Outcome class | Example of an acceptable contract | An invalid substitute |
|---|---|---|
| Correctness | No double seat allocation across concurrent requests in repeatable failure tests | `Use event-driven architecture` |
| Reliability | Recovery drill meets approved RTO/RPO for a specified outage while preserving invariant | `Move to Kubernetes` |
| Deployability | Mixed-version contract tests pass during a defined overlap window | `Adopt GitOps` |
| Performance | Measured good-event SLI passes at the **specified workload and scope** without hiding overload rejects | `Support 1,000 users` |
| Cost and operations | Cost envelope and required support/call-out capability are documented per environment | `Microservices are cheaper` |

State **non-goals** such as avoiding organization-wide runtime changes or not replacing an unrelated data store. Hard gate violation eliminates a candidate even when other attributes score well. If the baseline evidence is missing, valid outcomes include **retain**, **stabilize first**, **investigate**, or **insufficient evidence**.

## 6. Original synthetic worked baseline — workshop registration

This example deliberately reuses the invented workshop-registration journey from [the outbox pilot](../../book/distributed/transactional-outbox-and-idempotency.md) as a **fictional decision exercise**, not a new factual claim or real workload.

- **Declared scenario assumptions:** one deployable registration application with a local relational database, confirmation endpoint and a separate notification consumer. Several consumers use a versioned registration API. Release tooling and operational telemetry are not yet inventoried (`unknown`).
- **Hypothetical proposed symptom `OBS-1`:** a user receives a timeout after submitting a registration, but a later read sometimes shows the seat reserved. **No measurement or observation is claimed.** Hypothesis H1: the local transaction committed and the HTTP acknowledgement was lost. Alternative H2: the client observed a stale read or attempted a duplicate registration. Required tests: transaction log/ID correlation, idempotency-key invariants, concurrent same-key retries and confirmed state after injected lost replies.
- **Compatibility constraint:** old API consumers must continue to submit commands during a mixed-version release. Its real duration and permissible breaking changes are `unknown`, requiring consumer inventory and contract tests.
- **Downtime/RPO/RTO:** `unknown`. Do not propose a cutover or guarantee rollback until stakeholders define and exercise them.
- **Potential goal:** return a stable logical outcome for repeated same-intent request keys without allocating another seat; validate by fault-injection and DB constraints.
- **Non-goal:** extracting the registration service into a separate deployment before the causes and state ownership are understood.

~~~mermaid
flowchart LR
    Client["Workshop client (synthetic)"] --> API["Registration API"]
    API --> DB[("Local transaction owner")]
    API -.-> Notify["Separate notification boundary"]
    DB --> Record["Registration state"]
    DB --> Outbox["Optional committed outbox intent"]
    API --> Gate{"Compatibility and evidence gate"}
    Gate -->|insufficient| Investigate["Measure, retain current boundary"]
    Gate -->|validated| Transition["Evaluate incremental change"]
~~~

Text alternative: the fictional client calls a registration API. A local database owns durable state; an external notification boundary is separate. The architecture question is whether existing behavior and compatibility can be verified, not whether a new service should be immediately deployed. The outbox node is a **candidate** and does not imply an existing implementation.

### Candidate reasoning, not architecture approval

- **A — stabilize in place:** add end-to-end request identity, test missing-response paths and maintain one local transaction. Prefer when the invariant can be enforced locally; test the smallest change.
- **B — outbox and relay:** consider only if independently reliable notification is a real requirement. Costs include relay, lag and consumer deduplication; [outbox pilot](../../book/distributed/transactional-outbox-and-idempotency.md) owns the factual mechanism.
- **C — split into independently deployed services:** defer until evidence shows a need for independent deployment/scaling or ownership and the data/interface/transition constraints can be satisfied. A new service does not make a local state transaction span two independent databases.

**Decision status:** `insufficient evidence`. No real workloads, repository revisions, compatibility matrix or recovery exercises have been provided for this invented system.

## 7. Public reference and provenance boundary

The profile structure and fields are Tycho-original. Narrow primary-source points inspected 2026-10-19:

| Ref | Published source and specifically inspected part | Supports, and does not establish |
|---|---|---|
| L01 | [arc42, Section 3: Context and Scope](https://docs.arc42.org/section-3/), *Content*, *Motivation* | Delimiting users, neighboring systems and business/technical interfaces; not that any invented integration actually exists |
| L02 | [arc42, Section 5: Building Block View](https://docs.arc42.org/section-5/), *Content*, *Motivation* | Hierarchical decomposition and dependencies; not live ownership or transaction guarantees |
| L03 | [Martin Fowler, Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html), article dated 2024-08-22, discussion of incremental modernization | Rationale for incremental change; not a universal mandate to split into microservices |
| L04 | [AWS Prescriptive Guidance, Strangler fig pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html), *Transform*, *Coexist*, *Eliminate* and trade-offs | Coexistence, interceptable interfaces and rollback planning in its stated context; not an evaluated migration of the synthetic workshop |
| L05 | [AWS Prescriptive Guidance, Branch by abstraction pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html), implementation steps | An internal interception alternative for deep components with upstream dependencies; not a universal better option |
| L06 | [Tycho outbox pilot](../../book/distributed/transactional-outbox-and-idempotency.md), failure/retry boundaries and exact source ledger | Canonical mechanism and public evidence for local transaction/outbox; not a deployed system |

**Review and validation:** this is a first original authoring model and synthetic reasoning exercise, not externally reviewed. No real legacy system was inspected, no migration performed, no measured success or SLO demonstrated, and no deployment test run. Do not mark #18 complete solely for producing this document; check navigation, source boundaries and template usability first.
