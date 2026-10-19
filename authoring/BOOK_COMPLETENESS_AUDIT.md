# Tycho — ten-volume, 69-chapter content coverage audit

**Assessment:** 2026-10-19; **scope:** content-first editorial baseline for [Issue #213](https://github.com/rouslanbaranov/tycho/issues/213).
**Authority:** the provisional chapter questions in [the proposed table of contents](../book/PROPOSED-STRUCTURE.md). This is a verification snapshot, not a publication certificate.

## Executive result

- The proposed outline contains **10 volumes and 69 chapters**. All 10 volume rows were compared against titles and section headings in currently reachable technical prose.
- The current book is **not assembled** into those volume/chapter/page paths. Across 13 inspected topical landing pages, **33 directly reachable technical prose files** were identified and their headings and size checked. They contain real prose; they are not 69 separate canonical chapter units.
- Of 69 proposed questions: **38 directly addressed**, **23 partially addressed**, **8 without a focused book treatment verified**, counting the new unreviewed V02/C05 draft on this branch. **None is independently certified publication-complete by this desk audit.** The middle category is not “done”; even directly addressed material must be checked for the chapter's entire scope and admitted evidence.
- Source discovery was limited to current root/topic navigation and linked Markdown files accessed from GitHub. The entire Git tree was **not exhaustively enumerated** and repository-wide executable checks **were not run**. Reconcile this matrix with a full local inventory and content review before presenting the classification as comprehensive proof.
- Educational graph storage/traversal remains a legitimate V06/C06 topic; a curated concept/decision graph for Tycho is **not required**. Search/MCP/deployment infrastructure work is excluded from this manuscript completion gate.

### Labels

- **D — Direct:** one or more substantive existing book pages address the core chapter question; depth, uniqueness of canonical owner and evidence still require review.
- **P — Partial:** only a subset is handled, across source pages or authoring-method artifacts, and a substantive chapter owner/deepening is required.
- **M — Missing focused treatment:** no substantial dedicated treatment of this chapter's main question was verified in inspected book prose. A related mention or method file does not count as a chapter.

## Planned chapter ownership vs. verified current prose

### V01 — Requirements, quality attributes and architecture fundamentals

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V01/C01 — Problem framing and system boundaries | P | [Technical page](../book/application/quality-drivers-and-architecture-views.md) | Need a focused system-context/problem-frame walkthrough with actors, interfaces, outcomes and exclusions. |
| V01/C02 — Workload and demand models | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Expand a complete measurable workload/demand profile beyond experimental mechanics. |
| V01/C03 — Quality attributes and trade-offs | D | [Technical page](../book/application/quality-drivers-and-architecture-views.md) | Deepen systematic quality conflict evaluation and acceptance across stakeholder perspectives. |
| V01/C04 — Evidence, hypotheses and architecture experiments | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Separate hypothesis/evidence design and experimental validity from capacity examples. |
| V01/C05 — Architecture descriptions and decision records | P | [Technical page](../book/application/quality-drivers-and-architecture-views.md) | Unify architectural views and bounded ADR reading into one canonical chapter. |
| V01/C06 — Capacity, operational constraints and total cost | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Add end-to-end total-cost and team/operations hard-gate comparisons. |

### V02 — Application boundaries and interaction contracts

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V02/C01 — Layered, modular and ports-and-adapters design | D | [Technical page](../book/application/architecture-styles-and-module-boundaries.md) | Confirm full layered/ports/adapters mechanics, dependency enforcement and limits. |
| V02/C02 — Domain boundaries, data ownership and contracts | P | [Technical page](../book/application/architecture-styles-and-module-boundaries.md) | Add explicit domain ownership, data contracts, mapping and boundary evolution. |
| V02/C03 — Modular monolith and internal events | P | [Technical page](../book/application/architecture-styles-and-module-boundaries.md) | Expand modular-monolith lifecycle, internal events, invariants and deployment countercases. |
| V02/C04 — SOA, microservices and distributed boundaries | D | [Technical page](../book/application/architecture-styles-and-module-boundaries.md) | Deepen SOA versus microservices decisions with independent deployment conditions. |
| V02/C05 — Public APIs, HTTP/RPC and compatibility | D | [New chapter draft](../book/application/http-rpc-contracts-and-compatibility.md) | Newly written; pending independent technical review, full local verification and final V02 chapter/page assembly. |
| V02/C06 — Integration adapters and anti-corruption boundaries | P | [Technical page](../book/application/architecture-evolution-and-extraction.md) | Write anti-corruption adapter contracts and long-lived coexistence with original failure scenarios. |
| V02/C07 — Authorization boundaries and multitenancy | P | [Technical page](../book/security/identity-authorization-and-isolation.md) | Move/link ownership-specific multitenancy boundaries without duplicating security chapter. |

### V03 — Execution models, concurrency and flow control

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V03/C01 — Threads, tasks and coordination | P | [Technical page](../book/execution/platform-threads-executors-and-virtual-threads.md) | Clarify concurrency primitives, cancellation, contention and work-queue ownership. |
| V03/C02 — Java execution and virtual threads | D | [Technical page](../book/execution/platform-threads-executors-and-virtual-threads.md) | Retain JDK-scoped virtual-thread contraindications and downstream capacity tests. |
| V03/C03 — Reactive streams, demand and cancellation | D | [Technical page](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) | Complete demand, scheduling and end-to-end backpressure decision examples. |
| V03/C04 — Asynchronous APIs and streaming | P | [Technical page](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) | Add explicit async API/protocol streaming/cancellation and deadline interoperability. |
| V03/C05 — Thread, connection and buffer pools | D | [Technical page](../book/scaling/connection-pools-hikaricp-pgbouncer.md) | Integrate thread, connection and buffer budgets into one cross-layer model. |
| V03/C06 — Memory, GC, CPU and blocking diagnostics | M | No focused book page verified | Write focused CPU/memory/GC/blocking diagnosis and instrumentation contract with versioned primary references. |

### V04 — Distributed coordination and event integration

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V04/C01 — Time, causality and ordering | D | [Technical page](../book/distributed/causality-ordering-and-consensus.md) | Maintain separate causal-order guarantees and counterexamples. |
| V04/C02 — Replication, consensus and leader changes | P | [Technical page](../book/distributed/causality-ordering-and-consensus.md) | Expand replication/leader changes, quorum failure assumptions and safety/liveness distinction. |
| V04/C03 — Consistency and distributed transactions | D | [Technical page](../book/distributed/transaction-isolation-and-sagas.md) | Test invariant scope and real cross-boundary limitations of transaction choices. |
| V04/C04 — Retries, idempotency and duplicate effects | D | [Technical page](../book/distributed/transactional-outbox-and-idempotency.md) | Preserve scoped idempotency identities and duplicate-effect failure cases. |
| V04/C05 — Outbox, inbox, sagas and durable workflows | D | [Technical page](../book/distributed/transactional-outbox-and-idempotency.md) | Integrate saga ownership and durable-workflow recovery without canonical duplication. |
| V04/C06 — Messaging families and delivery contracts | D | [Technical page](../book/integration/messaging-families-and-durable-workflows.md) | Reconcile per-broker ordering/ack/retention guarantees and limits. |
| V04/C07 — Kafka logs, partitions and transactions | D | [Technical page](../book/integration/kafka-partitions-replication-and-contracts.md) | Deepen producer/consumer transaction, version and replay failure edge cases. |
| V04/C08 — Stateful/event-time stream processing | D | [Technical page](../book/integration/stateful-stream-processing-and-cdc.md) | Verify watermarks, checkpoint/savepoint and CDC recovery cases. |

### V05 — Data models, engines and lifecycle

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V05/C01 — Relational modeling and transaction isolation | D | [Technical page](../book/data/postgresql-mvcc-indexes-and-query-plans.md) | Keep relational constraints, visibility and isolation scope explicit. |
| V05/C02 — PostgreSQL MVCC, WAL and recovery | D | [Technical page](../book/data/postgresql-wal-replication-and-recovery.md) | Maintain PostgreSQL version and physical/logical replica evidence. |
| V05/C03 — Query planning, indexes and access paths | D | [Technical page](../book/data/postgresql-mvcc-indexes-and-query-plans.md) | Check planner statistics/index write costs and observed-versus-estimated distinctions. |
| V05/C04 — Alternative data models and stores | D | [Technical page](../book/data/storage-model-alternatives-and-workload-fit.md) | Add selection examples where competing data models fail hard gates. |
| V05/C05 — Partitioning, sharding and rebalancing | D | [Technical page](../book/scaling/shard-keys-hotspots-and-resharding.md) | Reconcile ownership movement and online resharding with data invariants. |
| V05/C06 — Schema evolution, data migration and retention | D | [Technical page](../book/delivery/progressive-delivery-and-schema-evolution.md) | Make schema/data lifecycle, compatibility and retention canonical in this volume. |
| V05/C07 — Replication, backups and restore drills | P | [Technical page](../book/data/postgresql-wal-replication-and-recovery.md) | Add versioned backup/restore drills, corruption and independently proven recoverability. |

### V06 — Caching, indexing and information retrieval

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V06/C01 — Local and distributed caching | D | [Technical page](../book/scaling/local-distributed-caching-and-invalidation.md) | Separate authority from invalidation and cache-failure acceptance. |
| V06/C02 — Hot keys, cache stampedes and read amplification | D | [Technical page](../book/scaling/local-distributed-caching-and-invalidation.md) | Deepen hot-key, stampede and overload comparative mechanisms. |
| V06/C03 — Lexical full-text indexing and ranking | D | [Technical page](../book/search/lexical-indexing-bm25-and-sql-fts.md) | Retain query analyzer, BM25 and index-update/version trade-offs. |
| V06/C04 — Vector embeddings and nearest-neighbor retrieval | D | [Technical page](../book/search/vector-hnsw-faiss-pgvector.md) | Expand embedding drift, exact baseline and filtered ANN limitations. |
| V06/C05 — Hybrid retrieval and reranking | D | [Technical page](../book/search/hybrid-ranking-graph-and-evaluation.md) | Extend hybrid fusion/rerank falsifiable comparisons. |
| V06/C06 — Graph relationships and traversal | P | [Technical page](../book/search/hybrid-ranking-graph-and-evaluation.md) | Graph models are an educational topic only; add graph data/queries without building a curated Tycho graph. |
| V06/C07 — Retrieval evaluation and index lifecycle | P | [Technical page](../book/search/hybrid-ranking-graph-and-evaluation.md) | Give retrieval evaluation and index lifecycle dedicated canonical treatment and sample protocols. |

### V07 — Performance, scale and resilience under load

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V07/C01 — Queueing, Little's Law and measurement boundaries | D | [Technical page](../book/performance/queueing-littles-law.md) | Maintain assumptions and synthetic finite-window counterexample. |
| V07/C02 — Contention, saturation and scaling laws | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Add saturation/contended resources and system-specific scaling-law limitations. |
| V07/C03 — Load-test methods and benchmark validity | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Separate load-test fixture validity, open versus closed demand and reproducibility. |
| V07/C04 — Tail latency, fan-out and time budgets | M | No focused book page verified | Write tail-latency and fan-out deadline budgeting with failure and percentile counterexamples. |
| V07/C05 — Overload protection and graceful degradation | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Expand admission, shedding, queue bounds, retry storms and degraded-mode correctness. |
| V07/C06 — Horizontal/vertical scaling and autoscaling delay | M | No focused book page verified | Write autoscaling lag, cold start, stabilization and workload-following counterexamples. |
| V07/C07 — Capacity planning and cost/performance trade-offs | P | [Technical page](../book/performance/workload-profiles-and-capacity-experiments.md) | Add defensible capacity planning and total-cost sensitivity models. |

### V08 — Delivery, deployment and disaster recovery

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V08/C01 — CI/CD architecture and artifact provenance | D | [Technical page](../book/delivery/ci-cd-provenance-and-gitops.md) | Unify build/test/promotion/release contracts. |
| V08/C02 — Supply chain and release verification | P | [Technical page](../book/delivery/ci-cd-provenance-and-gitops.md) | Deepen artifact signing, SBOM, evidence and independently verifiable supply-chain gates. |
| V08/C03 — VMs, containers, orchestration and serverless | D | [Technical page](../book/deployment/runtime-placement-and-control-plane.md) | Keep VM/container/managed/serverless and control-plane failure distinctions. |
| V08/C04 — GitOps, rollout and progressive delivery | D | [Technical page](../book/delivery/progressive-delivery-and-schema-evolution.md) | Integrate GitOps reconciliation and rollout decision under mixed versions. |
| V08/C05 — Backward-compatible database change | D | [Technical page](../book/delivery/progressive-delivery-and-schema-evolution.md) | Make expand/migrate/contract and rollback/no-return boundaries explicit. |
| V08/C06 — High availability and failure-domain placement | D | [Technical page](../book/deployment/multi-region-disaster-recovery-contracts.md) | Explain failure domains, multi-zone placement and measurable failover. |
| V08/C07 — Multi-region recovery and data reconciliation | D | [Technical page](../book/deployment/multi-region-disaster-recovery-contracts.md) | Give recovery drill, data reconciliation and fencing primary ownership. |

### V09 — Observability, security and operational architecture

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V09/C01 — SLIs, SLOs and error budgets | D | [Technical page](../book/observability/metrics-slo-timeseries-architecture.md) | Ensure measurable service outcome and error-budget alert decisions. |
| V09/C02 — Metrics ingestion, cardinality and time-series storage | D | [Technical page](../book/observability/metrics-slo-timeseries-architecture.md) | Extend cardinality/resource/retention budgets with reviewable calculations. |
| V09/C03 — Distributed tracing and propagation | D | [Technical page](../book/observability/trace-context-lineage-and-audit.md) | Keep W3C-context propagation and sampling limitations distinct from proof. |
| V09/C04 — Logging, audit and lineage | D | [Technical page](../book/observability/trace-context-lineage-and-audit.md) | Separate log, immutable business audit and lineage ownership. |
| V09/C05 — Identity, authorization and threat modeling | D | [Technical page](../book/security/identity-authorization-and-isolation.md) | Retain explicit object authorization, trust model and service boundaries. |
| V09/C06 — Incident response and operational change | M | No focused book page verified | Write focused incident command, diagnostic chronology, containment and learning/recovery process. |
| V09/C07 — Safety, isolation and privacy in agent-accessible services | M | No focused book page verified | Write agent-access safety, privacy/isolation, untrusted retrieved content and source resolution at the book-concept level. |

### V10 — Decision support and modernization playbooks

| Planned chapter | Coverage | Observed primary material | Outstanding work |
|---|---|---|---|
| V10/C01 — Architecture requirement and workload profiles | M | No focused book page verified | Write the canonical book chapter interpreting and applying the existing requirements/workload method; authoring/models is supporting method, not book prose. |
| V10/C02 — Baseline analysis for existing software | M | No focused book page verified | Write canonical legacy-baseline architecture assessment chapter using only independent synthetic cases; method exists in authoring/models. |
| V10/C03 — Pattern applicability and contraindications | P | [Technical page](../book/decisions/cross-domain-modernization-and-adr-examples.md) | Turn method cards/contraindications into a navigable pattern-selection book chapter. |
| V10/C04 — Alternatives, experiments and ADRs | P | [Technical page](../book/decisions/cross-domain-modernization-and-adr-examples.md) | Expand condition-gated alternative analysis and ADR falsification examples. |
| V10/C05 — Target architecture versus transition states | P | [Technical page](../book/decisions/cross-domain-modernization-and-adr-examples.md) | Develop target versus transition states with reversible and non-reversible steps. |
| V10/C06 — Search and question routes for architecture agents | M | No focused book page verified | Write self-contained agent-oriented question/reading routes independent of an implemented MCP/search service. |
| V10/C07 — Cross-domain worked comparisons and unresolved cases | D | [Technical page](../book/decisions/cross-domain-modernization-and-adr-examples.md) | Expand original cross-domain worked decisions and insufficient-evidence outcomes. |

## Content remediation recorded in this branch

- **V02/C05 moved from M to D (not accepted):** new original [HTTP and RPC compatibility chapter](../book/application/http-rpc-contracts-and-compatibility.md), using independently verified RFC 9110, RFC 9457, OpenAPI 3.2.1, gRPC and Protocol Buffers documentation. Its application landing now links to it. No executable client/provider tests, independent review or full-repository validation has run; publication completeness is not claimed.
- Initial main-at-audit classification before this new chapter was **37 D / 23 P / 9 M**. The current feature-branch classification is **38 D / 23 P / 8 M**, all still subject to inventory and quality review.

## High-priority confirmed editorial gaps

1. **Unwritten focused subject coverage (M):** CPU/GC diagnostic decision-making; tail latency/fan-out budgets; autoscaling delay and stabilization; incident response; agent-facing trust/privacy controls; V10 requirements and legacy synthesis; agent-oriented reading route. Each needs original substantial material and precise admissible sources.
2. **Deepen fragmented subjects (P):** requirements and quality experimentation, modernization transitions, bounded architecture styles, graph concepts as *book content*, retrieval evaluation, cost modeling, recovery validation, and supply-chain acceptance.
3. **Normalize ownership:** current topical research pages often span multiple intended chapters. Preserve their proven material; split by genuinely separate reader question only, and establish one canonical source of explanation. Do not copy the same mechanism into every mapped chapter.
4. **Validate maturity:** confirm all claims with exact independently public versioned sources; review original diagrams, failure matrices, tests and limits. Existing self-authored researched pages are not evidence of independent domain approval or of real system benchmarking.
5. **Structural publication is separate:** book root, 10 volume landings, 69 chapter landings and bounded child pages will be built under [#214](https://github.com/rouslanbaranov/tycho/issues/214) only when the manuscript is substantively complete. No empty chapter placeholders are accepted as completion.

## Recommended execution order

1. Establish a complete repository Markdown inventory and reconcile every page/link with this 69-row table.
2. Write the M subjects in dependency order, prioritizing interoperability, runtime diagnosis, capacity, safety and V10 decision guidance. Use bounded reviewable authoring slices and independent public sources.
3. Deepen P subjects; for D subjects perform a chapter-specific acceptance review and extend when the chapter question is not completely answered.
4. Resolve canonical owners and evidence states; keep this matrix updated as chapters become genuinely ready.
5. After all 69 are editorially content-complete, move to [final ten-volume book assembly #214](https://github.com/rouslanbaranov/tycho/issues/214): chapter/page structure, metadata, full navigation, end-to-end checks and an edition release.

## Explicit nonclaims

This document does not assert that 69 technical chapters exist, that all technical pages were discovered, that the sources were independently reviewed, that a full local validation/CI suite ran, or that a buildable final edition exists. Old repository READMEs and checkpoints that state no technical chapters or no metadata tooling are stale and must be reconciled as a separate scoped change.
