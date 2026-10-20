# Tycho — selected finite edition outline and ownership boundaries

> **Current disposition — 2026-10-20, after PR #218 merge:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

**Editorial selection, 2026-10-20 (work in progress).** The ten-volume, 69-chapter scope is retained from [the proposed outline](../book/PROPOSED-STRUCTURE.md) after reviewing the 69 substantive owner draft articles. This is the **target final contents order**, not a claim that the edition exists or that every chapter has passed the new content-completeness gate. Chapters below link to **actual current manuscript files**, not empty promised pages. Formal publish/freeze is #214 after #213.

## Editorial decisions

- Reading progression: requirements → boundaries → execution → distributed semantics → data → caching/search → performance → deployment → operations/security → modernization decisions. V10 depends on all; a domain specialist may enter elsewhere through explicit prerequisites.
- Exactly one primary canonical page owner per question. Keep immutable `tycho.page.*` IDs and preserve earlier researched secondary pages; a move/split requires a reviewed identity, path, source and link migration record.
- A chapter landing must add an original owner question, boundary, ordered actual pages, worked result and next links. A volume landing must contribute a real synthesis and prerequisite-guided route. Neither may merely duplicate a source article. Initially an existing complete article may be **one substantial child page** of a chapter; split only when independently testable subquestions warrant it.
- All technical illustrations distinguish normal, partial failure and recovery, evidence types and whether an operation/measurement was actually executed. Adjacent concepts link canonically, not by rewriting each other's detailed mechanism.

## V01 — Requirements, quality attributes and architecture fundamentals

**Purpose and mission:** translate a problem into observable behavior, constraints and competing qualities without naming a solution prematurely.

**Prerequisites:** None; a concrete user outcome or proposed system boundary is enough.

**Required volume synthesis:** A reasoned requirements contract that distinguishes offered demand, qualities, hard constraints, observed data and speculative improvements.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V01/C01: Problem framing and system boundaries** — Which actors, outcomes, interfaces and external failure dependencies define the system? | [Current explanatory manuscript](../book/application/problem-framing-and-system-boundaries.md) |
| **V01/C02: Workload and demand models** — How do active users, offered arrivals, concurrency, operation mix and skew differ? | [Current explanatory manuscript](../book/performance/workload-demand-and-arrival-models.md) |
| **V01/C03: Quality attributes and trade-offs** — How are performance, availability, consistency, cost, security and changeability made measurable? | [Current explanatory manuscript](../book/application/quality-drivers-and-architecture-views.md) |
| **V01/C04: Evidence, hypotheses and architecture experiments** — What do sources, estimates, simulations and measurements actually prove? | [Current explanatory manuscript](../book/application/architecture-evidence-hypotheses-and-experiments.md) |
| **V01/C05: Architecture descriptions and decision records** — What belongs in diagrams, views, assumptions, ADRs and source-linked evidence? | [Current explanatory manuscript](../book/application/architecture-views-and-decision-records.md) |
| **V01/C06: Capacity, operational constraints and total cost** — Which hard gates and team/budget limits invalidate otherwise appealing options? | [Current explanatory manuscript](../book/application/operational-constraints-and-total-cost-gates.md) |

## V02 — Application boundaries and interaction contracts

**Purpose and mission:** decide responsibilities and system boundaries before distributing them.

**Prerequisites:** V01/C01, C03, C06.

**Required volume synthesis:** Map ownership and interface semantics before splitting deployment: modular monolith, services and adapters are conditional alternatives; tenancy crosses every boundary.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V02/C01: Layered, modular and ports-and-adapters design** — How are dependencies directed and replaceable? | [Current explanatory manuscript](../book/application/layered-hexagonal-ports-and-adapters.md) |
| **V02/C02: Domain boundaries, data ownership and contracts** — When should business capabilities form module or service boundaries? | [Current explanatory manuscript](../book/application/domain-boundaries-data-ownership-and-contracts.md) |
| **V02/C03: Modular monolith and internal events** — Which coupling and deployment constraints fit an in-process architecture? | [Current explanatory manuscript](../book/application/modular-monolith-and-internal-events.md) |
| **V02/C04: SOA, microservices and distributed boundaries** — When is independent deployment justified by measured coordination cost? | [Current explanatory manuscript](../book/application/service-orientation-microservices-and-distribution.md) |
| **V02/C05: Public APIs, HTTP/RPC and compatibility** — How do deadlines, versioning, retries and API contracts evolve? | [Current explanatory manuscript](../book/application/http-rpc-contracts-and-compatibility.md) |
| **V02/C06: Integration adapters and anti-corruption boundaries** — How can incompatible domains and legacy contracts coexist? | [Current explanatory manuscript](../book/application/anti-corruption-adapters-and-coexistence.md) |
| **V02/C07: Authorization boundaries and multitenancy** — What must be isolated between clients, organizations and data owners? | [Current explanatory manuscript](../book/application/authorization-boundaries-and-multitenancy.md) |

## V03 — Execution models, concurrency and flow control

**Purpose and mission:** explain the execution and resource budgets behind a request.

**Prerequisites:** V01/C02 and V02/C05.

**Required volume synthesis:** A resource-budget view tracing request admission, execution/task/connection pools and cancellation to the external effect boundary.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V03/C01: Threads, tasks and coordination** — What creates concurrency and which shared state creates contention? | [Current explanatory manuscript](../book/execution/threads-tasks-structured-coordination.md) |
| **V03/C02: Java execution and virtual threads** — What improves concurrency without creating downstream capacity? | [Current explanatory manuscript](../book/execution/platform-threads-executors-and-virtual-threads.md) |
| **V03/C03: Reactive streams, demand and cancellation** — How do backpressure, scheduling and blocking boundaries affect execution? | [Current explanatory manuscript](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) |
| **V03/C04: Asynchronous APIs and streaming** — Which flow and cancellation semantics are required across protocols? | [Current explanatory manuscript](../book/execution/asynchronous-apis-streaming-and-cancellation.md) |
| **V03/C05: Thread, connection and buffer pools** — How do pool sizes, queues and timeouts compose across layers? | [Current explanatory manuscript](../book/scaling/connection-pools-hikaricp-pgbouncer.md) |
| **V03/C06: Memory, GC, CPU and blocking diagnostics** — How should bottleneck observations constrain execution-model choice? | [Current explanatory manuscript](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) |

## V04 — Distributed coordination and event integration

**Purpose and mission:** describe what can and cannot be guaranteed across failure-prone boundaries.

**Prerequisites:** V02/C02, C05; V03/C03–C05.

**Required volume synthesis:** A failure trace from request to durable state to event consumer: causal order, retry identity and transaction scope are different promises.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V04/C01: Time, causality and ordering** — Which ordering can a distributed system observe or guarantee? | [Current explanatory manuscript](../book/distributed/causality-ordering-and-consensus.md) |
| **V04/C02: Replication, consensus and leader changes** — Which failure assumptions sustain agreement or availability? | [Current explanatory manuscript](../book/distributed/replication-consensus-and-leader-change.md) |
| **V04/C03: Consistency and distributed transactions** — Which invariants need coordination, isolation or reconciliation? | [Current explanatory manuscript](../book/distributed/transaction-isolation-and-sagas.md) |
| **V04/C04: Retries, idempotency and duplicate effects** — Which side effects survive retries and ambiguous acknowledgements? | [Current explanatory manuscript](../book/distributed/retries-idempotency-and-ambiguous-effects.md) |
| **V04/C05: Outbox, inbox, sagas and durable workflows** — How are state changes coordinated without claiming global atomicity? | [Current explanatory manuscript](../book/distributed/outbox-inbox-sagas-and-durable-workflows.md) |
| **V04/C06: Messaging families and delivery contracts** — What are the consequences of acknowledgement, retention and consumer state? | [Current explanatory manuscript](../book/integration/messaging-families-and-durable-workflows.md) |
| **V04/C07: Kafka logs, partitions and transactions** — What do producer/consumer guarantees cover and what stays at application level? | [Current explanatory manuscript](../book/integration/kafka-partitions-replication-and-contracts.md) |
| **V04/C08: Stateful/event-time stream processing** — How do replay, watermarks, state stores and recovery shape correctness? | [Current explanatory manuscript](../book/integration/stateful-stream-processing-and-cdc.md) |

## V05 — Data models, engines and lifecycle

**Purpose and mission:** connect data integrity, workload, engine internals and deployment costs.

**Prerequisites:** V04/C03–C05.

**Required volume synthesis:** A data-authority and lifecycle model from constraint/index/WAL through partitioning, migration and verified restore; storage engine is not an architecture shortcut.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V05/C01: Relational modeling and transaction isolation** — Which invariants and anomalies are relevant to the data contract? | [Current explanatory manuscript](../book/data/relational-modeling-and-transaction-isolation.md) |
| **V05/C02: PostgreSQL MVCC, WAL and recovery** — What are the consequences of durability, vacuum and replication mechanisms? | [Current explanatory manuscript](../book/data/postgresql-wal-replication-and-recovery.md) |
| **V05/C03: Query planning, indexes and access paths** — Which read/write trade-offs explain an observed query plan? | [Current explanatory manuscript](../book/data/postgresql-indexes-statistics-and-query-plans.md) |
| **V05/C04: Alternative data models and stores** — When are document, wide-column, KV, distributed SQL or analytical stores useful? | [Current explanatory manuscript](../book/data/storage-model-alternatives-and-workload-fit.md) |
| **V05/C05: Partitioning, sharding and rebalancing** — How do hot keys, routing, joins and ownership affect scale? | [Current explanatory manuscript](../book/scaling/shard-keys-hotspots-and-resharding.md) |
| **V05/C06: Schema evolution, data migration and retention** — What compatibility windows and irreversibility constraints exist? | [Current explanatory manuscript](../book/data/schema-lifecycle-and-semantic-migration.md) |
| **V05/C07: Replication, backups and restore drills** — How do consistency, lag, RPO/RTO and restore evidence connect? | [Current explanatory manuscript](../book/data/backup-restore-pitr-and-recovery-drills.md) |

## V06 — Caching, indexing and information retrieval

**Purpose and mission:** show why different acceleration and search mechanisms solve different problems.

**Prerequisites:** V02/C02; V05/C03–C06.

**Required volume synthesis:** Clarify authority/cache/projection/search separation; show lexical, vector, hybrid and graph fits with quantitative evaluation and failure boundaries.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V06/C01: Local and distributed caching** — How do authority, freshness, eviction and invalidation differ? | [Current explanatory manuscript](../book/scaling/local-and-distributed-cache-design.md) |
| **V06/C02: Hot keys, cache stampedes and read amplification** — When does adding a cache worsen recovery or contention? | [Current explanatory manuscript](../book/scaling/cache-invalidation-stampede-and-hot-keys.md) |
| **V06/C03: Lexical full-text indexing and ranking** — Which queries need tokenization, inverted indexes, BM25 or filtering? | [Current explanatory manuscript](../book/search/lexical-indexing-bm25-and-sql-fts.md) |
| **V06/C04: Vector embeddings and nearest-neighbor retrieval** — What are exact versus approximate search and recall trade-offs? | [Current explanatory manuscript](../book/search/vector-hnsw-faiss-pgvector.md) |
| **V06/C05: Hybrid retrieval and reranking** — When do fusion and metadata filters improve measured relevance? | [Current explanatory manuscript](../book/search/hybrid-ranking-graph-and-evaluation.md) |
| **V06/C06: Graph relationships and traversal** — When is explicit typed connectivity preferable to lexical or vector similarity? | [Current explanatory manuscript](../book/search/graph-data-models-and-traversal.md) |
| **V06/C07: Retrieval evaluation and index lifecycle** — How are index freshness, reproducibility, latency and result quality measured? | [Current explanatory manuscript](../book/search/retrieval-evaluation-and-index-lifecycle.md) |

## V07 — Performance, scale and resilience under load

**Purpose and mission:** connect load and failure conditions to observed limits, avoiding universal thresholds.

**Prerequisites:** V01/C02–C04; V03/C05; V04/C04.

**Required volume synthesis:** A capacity envelope joining Little's Law, offered load, contention, tails, overload controls, autoscaling lag and cost with falsification.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V07/C01: Queueing, Little's Law and measurement boundaries** — What do arrival, throughput, mean response and in-flight counts imply? | [Current explanatory manuscript](../book/performance/queueing-littles-law.md) |
| **V07/C02: Contention, saturation and scaling laws** — When does coordination dominate additional capacity? | [Current explanatory manuscript](../book/performance/contention-saturation-and-scaling-laws.md) |
| **V07/C03: Load-test methods and benchmark validity** — How do open/closed arrivals, warmup and coordinated omission bias conclusions? | [Current explanatory manuscript](../book/performance/load-testing-and-benchmark-validity.md) |
| **V07/C04: Tail latency, fan-out and time budgets** — Why can p99 degrade despite adequate mean capacity? | [Current explanatory manuscript](../book/performance/tail-latency-fanout-and-deadline-budgets.md) |
| **V07/C05: Overload protection and graceful degradation** — How should admissions, queues, retries and shedding be bounded? | [Current explanatory manuscript](../book/performance/overload-admission-control-and-graceful-degradation.md) |
| **V07/C06: Horizontal/vertical scaling and autoscaling delay** — Which headroom, statefulness and failure assumptions shape capacity? | [Current explanatory manuscript](../book/performance/autoscaling-lag-and-capacity-limits.md) |
| **V07/C07: Capacity planning and cost/performance trade-offs** — What experiments can confirm or falsify a scaling hypothesis? | [Current explanatory manuscript](../book/performance/capacity-planning-and-cost-performance.md) |

## V08 — Delivery, deployment and disaster recovery

**Purpose and mission:** distinguish producing deployable software from safely releasing and operating it.

**Prerequisites:** V02/C05; V04/C03–C05; V05/C06–C07.

**Required volume synthesis:** A cutover chain linking artifact trust, mixed versions, deployments, failure domains, data authority and recovery after the no-return point.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V08/C01: CI/CD architecture and artifact provenance** — Which boundaries separate build, test, publication and production deployment? | [Current explanatory manuscript](../book/delivery/ci-cd-provenance-and-gitops.md) |
| **V08/C02: Supply chain and release verification** — How are reproducibility, signatures and promotion controls established? | [Current explanatory manuscript](../book/delivery/sbom-attestation-and-release-verification.md) |
| **V08/C03: VMs, containers, orchestration and serverless** — Which topology suits operational and workload requirements? | [Current explanatory manuscript](../book/deployment/runtime-placement-and-control-plane.md) |
| **V08/C04: GitOps, rollout and progressive delivery** — How do rolling, blue/green, canary, rollback and analysis gates differ? | [Current explanatory manuscript](../book/delivery/gitops-canary-and-progressive-rollout.md) |
| **V08/C05: Backward-compatible database change** — What permits old and new binaries/data schemas to coexist? | [Current explanatory manuscript](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) |
| **V08/C06: High availability and failure-domain placement** — What survives machine, zone, dependency or region loss? | [Current explanatory manuscript](../book/deployment/availability-zones-placement-and-failure-domains.md) |
| **V08/C07: Multi-region recovery and data reconciliation** — How are RPO/RTO, split brain, recovery routes and failback validated? | [Current explanatory manuscript](../book/deployment/disaster-recovery-and-recovery-objectives.md) |

## V09 — Observability, security and operational architecture

**Purpose and mission:** make system behavior measurable, operable and bounded by explicit security constraints.

**Prerequisites:** V02/C07, V04/C04; V07/C03.

**Required volume synthesis:** A user-visible truth/accountability loop: metrics, traces, audit, security and incident recovery have different completeness and trust guarantees.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V09/C01: SLIs, SLOs and error budgets** — Which user outcomes are measured and how do budgets guide changes? | [Current explanatory manuscript](../book/observability/service-level-indicators-objectives-and-alerts.md) |
| **V09/C02: Metrics ingestion, cardinality and time-series storage** — How do scrape/push, temporality, labels, retention and scale interact? | [Current explanatory manuscript](../book/observability/metric-pipelines-cardinality-and-retention.md) |
| **V09/C03: Distributed tracing and propagation** — Which context, sampling and async boundaries determine trace usefulness? | [Current explanatory manuscript](../book/observability/distributed-tracing-context-and-sampling.md) |
| **V09/C04: Logging, audit and lineage** — How do security audit, event lineage and operational logs differ? | [Current explanatory manuscript](../book/observability/logs-audit-and-data-lineage.md) |
| **V09/C05: Identity, authorization and threat modeling** — Where do trust boundaries and permission checks have to sit? | [Current explanatory manuscript](../book/security/identity-authorization-and-isolation.md) |
| **V09/C06: Incident response and operational change** — What evidence distinguishes recovery, mitigation and restored guarantees? | [Current explanatory manuscript](../book/observability/incident-response-and-operational-change.md) |
| **V09/C07: Safety, isolation and privacy in agent-accessible services** — What can remote readers infer or retrieve under bounded permissions? | [Current explanatory manuscript](../book/security/safe-agent-access-and-knowledge-isolation.md) |

## V10 — Decision support and modernization playbooks

**Purpose and mission:** apply validated knowledge to constrained choices while allowing “measure first”, “retain design” and “insufficient evidence” outcomes.

**Prerequisites:** All earlier volumes; V01/C01–C06 first.

**Required volume synthesis:** A full legacy-to-target-to-transition ADR with alternatives, reversible and irreversible stages, costs, authorization, evidence and an explicit unknown/refusal outcome.

| Reading order / owning question | Existing substantive primary page |
|---|---|
| **V10/C01: Architecture requirement and workload profiles** — What inputs are required before comparing candidate patterns? | [Current explanatory manuscript](../book/decisions/requirements-and-workload-architecture-profiles.md) |
| **V10/C02: Baseline analysis for existing software** — Which observed limitations justify changing the architecture? | [Current explanatory manuscript](../book/decisions/legacy-baseline-and-modernization-evidence.md) |
| **V10/C03: Pattern applicability and contraindications** — Which evidence, preconditions and failures bound a pattern's usefulness? | [Current explanatory manuscript](../book/decisions/pattern-applicability-and-contraindications.md) |
| **V10/C04: Alternatives, experiments and ADRs** — Which hypotheses distinguish feasible options under hard constraints? | [Current explanatory manuscript](../book/decisions/architecture-alternatives-experiments-and-adrs.md) |
| **V10/C05: Target architecture versus transition states** — What is safe during coexistence, migration, rollback and recovery? | [Current explanatory manuscript](../book/decisions/target-and-transition-architecture-states.md) |
| **V10/C06: Search and question routes for architecture agents** — How can requirements, symptoms and evidence guide selective reading? | [Current explanatory manuscript](../book/decisions/question-routes-for-architecture-analysis.md) |
| **V10/C07: Cross-domain worked comparisons and unresolved cases** — How does a decision stay falsifiable and attributable to its sources? | [Current explanatory manuscript](../book/decisions/cross-domain-modernization-and-adr-examples.md) |

## Canonical ownership conflicts to resolve explicitly

| Potential overlapping chapters | Editorial ownership decision |
|---|---|
| V01/C02 vs V07/C01 | V01/C02 owns workload vocabulary/arrival model; V07/C01 owns queue conservation and finite-window measurement counterexamples. |
| V02/C07 vs V09/C05 | V02/C07 owns tenant/domain placement and object isolation design; V09/C05 owns threat modeling, authn/authz protocols and credential boundaries. |
| V02/C03 vs V04/C05 | V02/C03 owns in-process module events; V04/C05 owns durable cross-boundary outbox/inbox/saga orchestration. |
| V03/C05 vs V07/C02 | V03/C05 owns thread/connection/buffer pool contracts; V07/C02 owns saturation, contention and scaling models. |
| V04/C01 vs V04/C02 | V04/C01 owns causality and observable order; V04/C02 owns replication and leader/quorum implementation. |
| V04/C03 vs V05/C01 | V04/C03 owns cross-system consistency/coordination; V05/C01 owns local relational modeling and isolation. |
| V04/C04 vs V04/C05 | V04/C04 owns logical effect/dedup/ambiguous outcomes; V04/C05 owns durable publication and multi-step compensations. |
| V05/C02 vs V05/C07 vs V08/C07 | V05/C02 owns WAL/replication internals; V05/C07 owns DB backup/restore/PITR; V08/C07 owns region-level traffic fencing, RTO/RPO, user recovery. |
| V05/C06 vs V08/C05 vs V10/C05 | V05/C06 owns semantic data migration; V08/C05 owns mixed-version DDL/deployment compatibility; V10/C05 owns staged system-wide modernization decisions. |
| V06/C03 vs V06/C05 vs V06/C07 | V06/C03 owns lexical inverted index; V06/C05 owns fusion/reranking; V06/C07 owns evaluation datasets and index lifecycle. |
| V06/C06 vs platform graph | V06/C06 teaches graph data/traversal as subject. Tycho infrastructure is graph-free; no curated concept graph is in scope. |
| V08/C01 vs V08/C04 | V08/C01 owns build artifact provenance and CI/CD topology; V08/C04 owns exposure, GitOps reconciliation and canary stop conditions. |
| V09/C03 vs V09/C04 | V09/C03 owns trace context and sampling; V09/C04 owns durable log/audit/lineage obligations. |
| V10/C06 vs Tycho MCP | V10/C06 teaches agent evidence/question routing. An implemented hosted MCP is a separate postponed infrastructure concern. |

## Page and assembly decisions

The 69 linked source articles are **already substantive Markdown prose**, not final numbered chapter directories. During #214 create meaningful `book/volumes/v01/.../v10` entries (final path naming chosen once) and real chapter landings only as the appropriate chapters have passed #213. Preserve each source ID when moving the original technical page, update `canonical_path`, `parent_id`, `sources/document-identities.json`, incoming links and related IDs, and capture an old→new path/ID migration table; do not silently create a duplicate canonical owner. A chapter can be single-page if it answers one bounded question fully. Genuine independent mechanism questions may be split after source inspection and page-level claim routing.

Every volume should end in a synthesis rather than only navigation: (1) what the volume equips the reader to decide, (2) which invariants carry into the next volume, (3) a counterexample that prevents an overly broad recommendation, (4) what published evidence and Tycho synthetic reasoning establish or do not establish, and (5) explicit remaining editorial limitations. Tie relevant M9 chapters to [specific supports and nonclaims](M9_CHAPTER_TRANSFER_AND_NONCLAIMS_2026-10-20.md); the 29 cases and six decision playbooks are an applied reading layer, not volume 11.

## Release gate

Before publication, recheck all 69 owner-question dispositions, all ten synthesis pages, canonical IDs/parent paths, source/claim provenance, internal links/anchors and Mermaid syntax. Regenerate derived index from the frozen tree, run the actual Python validators/test suite and record exit codes. Owner-cancelled visual rendering and live MCP checks remain **cancelled**; green structural checks never substitute for semantic reading. See [the executable register](BOOK_COMPLETION_EXECUTION_REGISTER_2026-10-20.md) and [#214](https://github.com/rouslanbaranov/tycho/issues/214).
