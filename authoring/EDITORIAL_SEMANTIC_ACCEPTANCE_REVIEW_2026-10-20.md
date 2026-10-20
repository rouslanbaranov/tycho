# Tycho #213 — semantic and source acceptance review, first recorded pass

> **Current disposition — 2026-10-20, after PR #218 merge:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


> **Review baseline:** GitHub commit `8a1bb1f977bb92080a911f478020e5b9e47b69cf` on Draft PR [#217](https://github.com/rouslanbaranov/tycho/pull/217), 2026-10-20. **This document is a desk-review and claim-verification work product, not an independent third-party endorsement.** It does not edit any of the 136 indexed book/source documents. The currently reported **13/13 Python validation groups and 195 tests PASS** on the pinned snapshot remain the technical result, not proof of semantic acceptance. Visual rendering and live MCP checks remain owner-cancelled.

## Verdict and methodology

**Editorial outcome: HOLD #213 OPEN. No chapter is marked ACCEPTED.** The 69 canonical manuscripts were examined in an initial evidence-coverage pass: section structures, public-source-link footprint, original/synthetic evidence labels, and explicit non-execution disclaimers were inspected, alongside the chapter-specific acceptance probes in the previously prepared execution register. Selected high-risk assertions were then read in their chapter context and compared with named public primary standards/manuals. This is a meaningful **first screening**, **not** 69 complete independent claim-by-claim factual reviews.

- **69/69** primary chapters have substantive content and source/evidence sections with public references; manuscript-specific synthetic examples are identified. This is necessary groundwork, not a sufficiency criterion.
- **69/69** still require explicit semantic/source acceptance disposition. A passed route-index/schema/navigation/unit-test suite does not prove the text's technical correctness or the case studies' historical conclusions.
- Findings below are **observed content omissions or source-verification tasks** at the pinned revision, with severity and exact closure evidence. They must be repaired and reviewed before the affected row can pass; other rows remain queued, not implicitly approved.
- We distinguish **documented behavior** (primary-source semantics), **original reasoning** (conditional architecture synthesis), **fictional case** (invented assumptions), and **observed run** (none claimed in these cases). Source versions, observed behavior and authority boundaries must not be conflated.
- **Index safety:** this review file is in `authoring/`, not a book page. Any subsequent edits to indexed manuscripts require a fresh route-index rebuild and Python rerun on the changed revision; the previous PASS is pinned only to `8a1bb1f`.

## Confirmed review findings

### F-01 — V01/C02, evidence gap, medium

**Page:** [Workload and demand models](../book/performance/workload-demand-and-arrival-models.md), particularly “Arrival shape” and “Worked example: lost offered load versus server rejection”.

**What exists:** correctly distinguishes offered/scheduled/started/completed operations, documents k6 open/closed generators and includes synthetic burst/dropped-iteration arithmetic.

**What is not yet demonstrated:** the original #213 acceptance probe calls for **paired open/closed arrival traces at equal declared population/work/service-time assumptions**, including exact admitted work, queue/backlog, generator feedback and units. Two different account-population scenarios are not that controlled pair. Provide a reproducible hand-computed trace (fictional, not measured), ensure the same denominator, and state the decision change under slowdown.

**Source basis:** [Grafana k6 open versus closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) and [dropped iterations](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/). The source describes generator models, not measured Tycho service capacity.

### F-02 — V01/C06, acceptance gap, medium

**Page:** [Operational constraints and TCO gates](../book/application/operational-constraints-and-total-cost-gates.md), “Engineering walkthrough — Hard constraints before weighted cost scoring”.

**What exists:** the synthetic three-year staffing calculation (105 versus 252.5 engineer-days) is internally arithmetically consistent. Hard gates and cost-category coverage are explicit.

**What remains:** the declared acceptance probe asks for sensitivity **including** storage/audit retention, migration double-running and rollback/forward-repair costs. The chapter only itemizes those as factors, not a sensitivity comparison with quantities and ranges; they are not numerically tested in the illustrative decision. Add a bounded, unit-consistent toy model (no invented market price), and show an option changes ranking or fails under one range. Prevent overlap with V07/C07 by treating this as the hard-gate example rather than duplicating capacity-planning methodology.

**Source basis:** [arc42 constraints](https://docs.arc42.org/section-2/) and [AWS cost design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) are category/framework guidance, not project prices.

### F-03 — V02/C03, source nuance, medium

**Page:** [Modular monolith and internal events](../book/application/modular-monolith-and-internal-events.md), “Internal events have multiple execution and durability contracts”.

**Verified supported core:** Spring `@TransactionalEventListener` can run at `AFTER_COMMIT` by default, and does **not** create a crash-durable delivery guarantee. The chapter correctly says both.

**Missing engineering caveat:** Spring's official annotation JavaDoc warns that after-commit/after-completion listeners can still access transaction resources that appear active **although the transaction is already completed**; data access at that point should not be represented as a newly committed independent transaction. Where a listener intentionally persists a follow-up update, explain the distinct transaction boundary and its failure/retry semantics. Also document no-active-transaction behavior and `fallbackExecution` when illustrating event registration.

**Source basis:** [Spring Framework transaction-bound events](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) and [annotation JavaDoc](https://github.com/spring-projects/spring-framework/blob/main/spring-tx/src/main/java/org/springframework/transaction/event/TransactionalEventListener.java). The source does not prove a listener completed or survived a crash.

### F-04 — V03/C02, provenance refresh, low

**Page:** [Virtual-thread capacity](../book/execution/platform-threads-executors-and-virtual-threads.md), “Pinning depends on the JDK release”.

**What appears sound:** separates JDK 21–23 monitor pinning from JDK 24 JEP 491 monitor changes, and explicitly avoids generalizing to native/foreign methods or every JVM configuration.

**Pending:** the historical research note claims the canonical JEP 491 text was not fully accessible to its author, while the chapter now links it. Independently inspect the canonical [JEP 491](https://openjdk.org/jeps/491) by release/status and narrow compatibility conditions, preserve the original reading date and amend current review status without fabricating tests on any JDK. The [OpenJDK implementation review](https://mail.openjdk.org/pipermail/nio-dev/2024-November/018122.html) discusses special legacy locking mode. No invalid JDK assertion has been established here.

### F-05 — V06/C06, comparative example gap, medium

**Page:** [Graph models and traversal](../book/search/graph-data-models-and-traversal.md).

**What exists:** direction, time-bounded edges, cycles/degree effects, access rules and a Cypher-style bounded *pattern*, plus a discussion of equivalent relational recursive CTEs.

**Missing:** the declared acceptance probe calls for a **bounded path query in Cypher and an equivalent relational query** over the *same tiny graph and answer set*. Neither a full executable-looking Cypher query with tenant/time checks nor a corresponding SQL/CTE query/result table is given. Add version-scoped illustrative queries, bounded depth/cycle handling and a shared expected answer; flag them unexecuted and keep Tycho's non-curated-graph infrastructure decision intact.

**Source basis:** [Neo4j Cypher patterns](https://neo4j.com/docs/cypher-manual/current/patterns/) and [variable-length paths](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-paths/). A SQL implementation needs separate PostgreSQL recursive query semantics support before authoritative acceptance.

### F-06 — V09/C03, explicit acceptance omission, high

**Page:** [Distributed tracing and sampling](../book/observability/distributed-tracing-context-and-sampling.md), “Propagation is also a trust boundary” and “Worked trust-boundary example”.

**What exists:** detailed forged `traceparent`/sampled-bit handling, W3C trace-context security references, sampling limits and separation from business audit evidence.

**Missing:** the explicit V09/C03 acceptance probe requires a **forged `baggage` scenario** at a cross-service boundary, including header propagation/filtering, sensitive metadata and what happens when an untrusted value reaches a telemetry backend or downstream tenant. The current manuscript does not contain the word `baggage` at the pinned revision. Add a bounded negative test and the **separate W3C Baggage** source, without conflating its semantics with `traceparent` or `tracestate`.

**Source basis:** [W3C Trace Context security](https://www.w3.org/TR/trace-context/#security-considerations) and [W3C Baggage, sections 4–5](https://www.w3.org/TR/baggage/), which explicitly warns about sensitive values propagated across trust boundaries.

## Source spot-checks supporting the review (not complete acceptance)

| Chapter | Compared to official source | Narrow supported finding | Limitation |
|---|---|---|---|
| V05/C01 | [PostgreSQL 17 §5.5](https://www.postgresql.org/docs/17/ddl-constraints.html), [§8.17.10](https://www.postgresql.org/docs/17/rangetypes.html) | Exclusion constraints can enforce non-overlapping ranges; plain cross-row CHECK is not a sound substitute | The book's particular SQL/extension concurrency fixture was not executed |
| V02/C03 | Spring official reference and annotation JavaDoc linked above | Transaction-phase listener versus crash-durable event, plus post-commit resource caveat | Not verified against a running Spring Modulith/DB combination |
| V03/C02 | [OpenJDK JEP 491 implementation discussion](https://mail.openjdk.org/pipermail/nio-dev/2024-November/018122.html) | Monitor unmounting depends on JDK release/locking mode; historical exception exists | No actual JVM runtime or benchmark, final canonical JEP review pending |
| V09/C03 | W3C Trace Context / W3C Baggage references above | Untrusted propagation of baggage can disclose private fields; sampled bit is not permission | No gateway/collector test performed |
| V08/C02 | [SLSA specification 1.2](https://slsa.dev/spec/v1.2/) | Current chapter selects a real versioned supply-chain specification | Other SBOM/signer claims still need assertion-by-assertion acceptance |

## Additional independent public-source spot-checks

- **V04/C07 Kafka transactions:** [Apache Kafka 4.1 Design — Message Delivery Semantics / Using Transactions](https://kafka.apache.org/41/design/design/) describes transactionally coordinated Kafka producer output and consumer offsets, explicitly discussing separate external-output coordination. The manuscript appropriately rejects an automatic atomic commit with unrelated PostgreSQL/email effects. **Result:** selected central scope claim appears supported at the chosen *older* Kafka release; actual application configuration and every other chapter claim remain unreviewed.
- **V06/C04 pgvector filtered ANN:** the [pgvector Filtering, Multitenancy and Iterative Index Scans sections](https://github.com/pgvector/pgvector#filtering) describe approximate-index filtering after candidate scanning, potential recall loss under selective predicates, and iterative scans since 0.8.0. The chapter's candidate-filtering counterexample is consistent with that described mechanism. **Result:** selected architectural mechanism supported, not a measured Tycho recall result; production-specific guidance still needs a pinned pgvector tag/build and ACL review. Note that a shared ANN index influencing recall is a *retrieval-quality* issue separate from the strict no-unauthorized-result security requirement.
- **V01/C02 open/closed claim:** [k6 Open and Closed Models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) confirms that closed-model arrivals depend on iteration completion whereas arrival-rate executors attempt to schedule independently. The explanation is sound, but the **paired, equal-input demonstration** demanded by the acceptance probe is still absent (F-01).

These checks compare deliberately narrow statements with official references. They are **not** a global source audit and do not grant formal chapter acceptance.

## Per-chapter acceptance queue (all 69; no silent approvals)

**Disposition legend:** `FINDING` means a specific review defect or evidence gap was recorded above; `CLAIM REVIEW PENDING` means the initial evidence-footprint screening found source references but has **not** yet individually validated each substantive assertion or given approval. **Priority is risk of unreviewed conclusions, not proven error severity.** The original executable acceptance probe remains authoritative and is restated so follow-up work can record an actual independent decision.

| Owner | Canonical manuscript | Initial disposition | Priority | Specific closing probe from #213 |
|---|---|---|---|---|
| V01/C01 | [Problem framing and system boundaries](../book/application/problem-framing-and-system-boundaries.md) | Claim-level review pending | Normal | Trace a synthetic reservation request across a third-party outage; document explicit excluded actors and who owns each recovery action |
| V01/C02 | [Workload and demand models](../book/performance/workload-demand-and-arrival-models.md) | **FINDING F-01** | High | Provide paired open/closed-arrival traces and show why same daily users produce different resource budgets |
| V01/C03 | [Quality attributes and trade-offs](../book/application/quality-drivers-and-architecture-views.md) | Claim-level review pending | Normal | Create a trade-off table with at least one unacceptable option despite a stronger headline metric |
| V01/C04 | [Evidence, hypotheses and architecture experiments](../book/application/architecture-evidence-hypotheses-and-experiments.md) | Claim-level review pending | Normal | Write a preregistered compare-cache-vs-query experiment with a negative result and a decision-reversal rule |
| V01/C05 | [Architecture descriptions and decision records](../book/application/architecture-views-and-decision-records.md) | Claim-level review pending | Normal | Trace one failure from sequence through component ownership to ADR consequence; verify no view implies unsupported deployment behavior |
| V01/C06 | [Capacity, operational constraints and total cost](../book/application/operational-constraints-and-total-cost-gates.md) | **FINDING F-02** | Normal | Run hypothetical sensitivity scenarios with explicit units, staffing, storage retention, migration and rollback costs; no invented market prices |
| V02/C01 | [Layered, modular and ports-and-adapters design](../book/application/layered-hexagonal-ports-and-adapters.md) | Claim-level review pending | Normal | Follow one error from adapter through domain invariant and persistence; demonstrate what a module test can and cannot prove |
| V02/C02 | [Domain boundaries, data ownership and contracts](../book/application/domain-boundaries-data-ownership-and-contracts.md) | Claim-level review pending | Normal | Test conflicting updates from two teams during semantic schema version coexistence; make the single-writer invariant explicit |
| V02/C03 | [Modular monolith and internal events](../book/application/modular-monolith-and-internal-events.md) | **FINDING F-03** | High | Show crash before commit, after commit and during callback; compare modular-monolith repair with premature service extraction |
| V02/C04 | [SOA, microservices and distributed boundaries](../book/application/service-orientation-microservices-and-distribution.md) | Claim-level review pending | Normal | Use same fictional workflow in monolith, SOA and service-split alternatives with a falsifiable decision/rollback gate |
| V02/C05 | [Public APIs, HTTP/RPC and compatibility](../book/application/http-rpc-contracts-and-compatibility.md) | Claim-level review pending | Normal | Build an old/new client compatibility matrix including timeout after commit, unknown outcome and retry budget |
| V02/C06 | [Integration adapters and anti-corruption boundaries](../book/application/anti-corruption-adapters-and-coexistence.md) | Claim-level review pending | Normal | Trace a lost acknowledgement through an anti-corruption adapter; establish reconciliation and retirement milestones |
| V02/C07 | [Authorization boundaries and multitenancy](../book/application/authorization-boundaries-and-multitenancy.md) | Claim-level review pending | Normal | Test cross-tenant identity, cache, event and bulk-export negative cases; qualify isolation guarantees and breach detection |
| V03/C01 | [Threads, tasks and coordination](../book/execution/threads-tasks-structured-coordination.md) | Claim-level review pending | Normal | Compare task failure before sibling completion with cancellation that does not undo a committed external effect |
| V03/C02 | [Java execution and virtual threads](../book/execution/platform-threads-executors-and-virtual-threads.md) | **FINDING F-04** | High | Contrast throughput under blocking I/O versus CPU-bound work with bounded downstream connections; avoid performance claims without runs |
| V03/C03 | [Reactive streams, demand and cancellation](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) | Claim-level review pending | Normal | Provide a downstream-stall test contract and show when a reactive path merely relocates queues |
| V03/C04 | [Asynchronous APIs and streaming](../book/execution/asynchronous-apis-streaming-and-cancellation.md) | Claim-level review pending | Normal | Propose one slow-consumer and disconnect/retry protocol with explicit buffer owner and loss/duplication boundary |
| V03/C05 | [Thread, connection and buffer pools](../book/scaling/connection-pools-hikaricp-pgbouncer.md) | Claim-level review pending | Normal | Calculate synthetic per-replica and fleet limits, held-connection latency, queue growth and timeout propagation |
| V03/C06 | [Memory, GC, CPU and blocking diagnostics](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | Claim-level review pending | Normal | Walk a false virtual-thread regression hypothesis through JFR/profiler observations and possible disconfirmation |
| V04/C01 | [Time, causality and ordering](../book/distributed/causality-ordering-and-consensus.md) | Claim-level review pending | Normal | Create counterexample where timestamp order differs from causality; name what extra coordination is required |
| V04/C02 | [Replication, consensus and leader changes](../book/distributed/replication-consensus-and-leader-change.md) | Claim-level review pending | Normal | Walk follower isolation, leader replacement, stale writes and membership change; state client-observable unknown results |
| V04/C03 | [Consistency and distributed transactions](../book/distributed/transaction-isolation-and-sagas.md) | Claim-level review pending | Normal | Compare local serializable retry against cross-service saga compensation for simultaneous cancel/accept; demonstrate unprotected side effect |
| V04/C04 | [Retries, idempotency and duplicate effects](../book/distributed/retries-idempotency-and-ambiguous-effects.md) | Claim-level review pending | High | Write a truth table for lost ack, redelivery, key reuse and dedup expiry including unrecoverable ambiguity |
| V04/C05 | [Outbox, inbox, sagas and durable workflows](../book/distributed/outbox-inbox-sagas-and-durable-workflows.md) | Claim-level review pending | High | Simulate crash at each commit/publish/ack/compensation boundary; prove only stated invariants without global exactly-once claims |
| V04/C06 | [Messaging families and delivery contracts](../book/integration/messaging-families-and-durable-workflows.md) | Claim-level review pending | Normal | Choose between work queue, ephemeral fanout and replayable log for a fictional order flow; enumerate broker and consumer failure contracts |
| V04/C07 | [Kafka logs, partitions and transactions](../book/integration/kafka-partitions-replication-and-contracts.md) | Claim-level review pending | High | Construct crash-after-DB-effect-before-offset and rebalance/replay timeline; identify irreducible application dedup need |
| V04/C08 | [Stateful/event-time stream processing](../book/integration/stateful-stream-processing-and-cdc.md) | Claim-level review pending | High | Trace late out-of-order correction after snapshot and crash, plus user-visible correction/restore policies |
| V05/C01 | [Relational modeling and transaction isolation](../book/data/relational-modeling-and-transaction-isolation.md) | Claim-level review pending | High | Show overlapping reservations under write-skew then design a database-enforced constraint and retry-on-conflict protocol |
| V05/C02 | [PostgreSQL MVCC, WAL and recovery](../book/data/postgresql-wal-replication-and-recovery.md) | Claim-level review pending | High | Trace committed primary write not replayed by a lagging replica; state recovery, divergence and evidence requirements |
| V05/C03 | [Query planning, indexes and access paths](../book/data/postgresql-indexes-statistics-and-query-plans.md) | Claim-level review pending | Normal | Compare two workload distributions under one index with an execution-plan hypothesis and plan regression test |
| V05/C04 | [Alternative data models and stores](../book/data/storage-model-alternatives-and-workload-fit.md) | Claim-level review pending | Normal | Create a 4-way decision with at least one hard-fail document/wide-column/distributed-SQL candidate |
| V05/C05 | [Partitioning, sharding and rebalancing](../book/scaling/shard-keys-hotspots-and-resharding.md) | Claim-level review pending | High | Simulate tenant hot spot migrating while writes continue; specify missing/duplicate record reconciliation |
| V05/C06 | [Schema evolution, data migration and retention](../book/data/schema-lifecycle-and-semantic-migration.md) | Claim-level review pending | High | Define old/new client compatibility matrix and an irreversible write with forward-repair versus rollback policy |
| V05/C07 | [Replication, backups and restore drills](../book/data/backup-restore-pitr-and-recovery-drills.md) | Claim-level review pending | High | Propose an isolated user-level restore drill including archive gap, corruption detection and verified query invariants |
| V06/C01 | [Local and distributed caching](../book/scaling/local-and-distributed-cache-design.md) | Claim-level review pending | Normal | Model stale read after cross-instance update with permitted stale interval and capacity impact of cache loss |
| V06/C02 | [Hot keys, cache stampedes and read amplification](../book/scaling/cache-invalidation-stampede-and-hot-keys.md) | Claim-level review pending | Normal | Show race interleaving of invalidate, slow fill, new write; test old value never overwrites newer generation |
| V06/C03 | [Lexical full-text indexing and ranking](../book/search/lexical-indexing-bm25-and-sql-fts.md) | Claim-level review pending | Normal | Compare lexical query coverage, tokenization and staleness with controlled relevance judgments; keep index generation identity |
| V06/C04 | [Vector embeddings and nearest-neighbor retrieval](../book/search/vector-hnsw-faiss-pgvector.md) | Claim-level review pending | High | Evaluate synthetic filtered-neighbor false negatives and index rebuild rollback; quantify recall only as proposed experiment |
| V06/C05 | [Hybrid retrieval and reranking](../book/search/hybrid-ranking-graph-and-evaluation.md) | Claim-level review pending | High | Work a hand-computed fusion counterexample and decision to refuse low-evidence answers, independent of search-engine choice |
| V06/C06 | [Graph relationships and traversal](../book/search/graph-data-models-and-traversal.md) | **FINDING F-05** | High | Contrast bounded Cypher path query with equivalent relational join; explicitly exclude any Tycho infrastructure graph |
| V06/C07 | [Retrieval evaluation and index lifecycle](../book/search/retrieval-evaluation-and-index-lifecycle.md) | Claim-level review pending | High | Design offline evaluation with held-out questions, versioned index, stale citation and permission-leak failure gates |
| V07/C01 | [Queueing, Little's Law and measurement boundaries](../book/performance/queueing-littles-law.md) | Claim-level review pending | High | Contrast finite-window backlog growth with steady-state arithmetic and define recoverability test after overload |
| V07/C02 | [Contention, saturation and scaling laws](../book/performance/contention-saturation-and-scaling-laws.md) | Claim-level review pending | Normal | Trace moving bottleneck from CPU to database at additional replicas; add overload recovery and hysteresis criteria |
| V07/C03 | [Load-test methods and benchmark validity](../book/performance/load-testing-and-benchmark-validity.md) | Claim-level review pending | High | Write a controlled synthetic benchmark protocol with a negative scenario and criteria that invalidate its own inference |
| V07/C04 | [Tail latency, fan-out and time budgets](../book/performance/tail-latency-fanout-and-deadline-budgets.md) | Claim-level review pending | High | Compare hypothetical serial, parallel and hedge request budgets under retry storm; state cost/overload stop gate |
| V07/C05 | [Overload protection and graceful degradation](../book/performance/overload-admission-control-and-graceful-degradation.md) | Claim-level review pending | Normal | Run hypothetical dependency outage through bulkhead/open-circuit/recovery hysteresis with outcome and fairness metrics |
| V07/C06 | [Horizontal/vertical scaling and autoscaling delay](../book/performance/autoscaling-lag-and-capacity-limits.md) | Claim-level review pending | Normal | Model lagging autoscaler and hot-key failure where more replicas do not help; define scale-in safety and reversal |
| V07/C07 | [Capacity planning and cost/performance trade-offs](../book/performance/capacity-planning-and-cost-performance.md) | Claim-level review pending | Normal | Compare provision, throttle, optimize and simplify choices under worst-case price/usage bounds; avoid claimed real prices |
| V08/C01 | [CI/CD architecture and artifact provenance](../book/delivery/ci-cd-provenance-and-gitops.md) | Claim-level review pending | Normal | Walk compromised runner and rollback attempt through signature/provenance and blast-radius gates; explicitly compare GitOps pull vs direct push |
| V08/C02 | [Supply chain and release verification](../book/delivery/sbom-attestation-and-release-verification.md) | Claim-level review pending | High | Design negative verification for wrong artifact digest, missing SBOM and untrusted signer; do not imply executed signing |
| V08/C03 | [VMs, containers, orchestration and serverless](../book/deployment/runtime-placement-and-control-plane.md) | Claim-level review pending | Normal | Trace control-plane loss while steady-state data-plane processes run; map irreversible placement and isolation conditions |
| V08/C04 | [GitOps, rollout and progressive delivery](../book/delivery/gitops-canary-and-progressive-rollout.md) | Claim-level review pending | High | Define failure of a canary after schema change and explicit rollback versus roll-forward policy across mixed versions |
| V08/C05 | [Backward-compatible database change](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | Claim-level review pending | High | Build deploy-order matrix and failed backfill with lossless rollback before no-return, forward repair after |
| V08/C06 | [High availability and failure-domain placement](../book/deployment/availability-zones-placement-and-failure-domains.md) | Claim-level review pending | Normal | Use zonal outage where cross-zone service still fails due to shared state; define measurable failover drill acceptance |
| V08/C07 | [Multi-region recovery and data reconciliation](../book/deployment/disaster-recovery-and-recovery-objectives.md) | Claim-level review pending | High | Write split-brain failover/return timeline with irreversible writes, no-return decision and user-level restore checks |
| V09/C01 | [SLIs, SLOs and error budgets](../book/observability/service-level-indicators-objectives-and-alerts.md) | Claim-level review pending | Normal | Show synthetic budget burn during dependency incident and a valid policy to defer a change, not invented production SLO |
| V09/C02 | [Metrics ingestion, cardinality and time-series storage](../book/observability/metric-pipelines-cardinality-and-retention.md) | Claim-level review pending | Normal | Compute synthetic high-cardinality retention cost and show reset/missing-sample false interpretations |
| V09/C03 | [Distributed tracing and propagation](../book/observability/distributed-tracing-context-and-sampling.md) | **FINDING F-06** | High | Trace sampled-out parent and forged baggage through cross-service request; distinguish tracing from audit proof |
| V09/C04 | [Logging, audit and lineage](../book/observability/logs-audit-and-data-lineage.md) | Claim-level review pending | Normal | Walk an authorized change from request through durable audit record and derived data lineage, including dropped telemetry |
| V09/C05 | [Identity, authorization and threat modeling](../book/security/identity-authorization-and-isolation.md) | Claim-level review pending | High | Threat-model multi-tenant request on proxy/cache/event boundary, with denied cross-object access and residual risks |
| V09/C06 | [Incident response and operational change](../book/observability/incident-response-and-operational-change.md) | Claim-level review pending | Normal | Develop one synthetic incident where index divergence looks like latency; define reversible containment and postmortem uncertainty |
| V09/C07 | [Safety, isolation and privacy in agent-accessible services](../book/security/safe-agent-access-and-knowledge-isolation.md) | Claim-level review pending | High | Test prompt injection and cross-tenant retrieval leakage with explicit no-hosted-MCP limitation and refusal boundaries |
| V10/C01 | [Architecture requirement and workload profiles](../book/decisions/requirements-and-workload-architecture-profiles.md) | Claim-level review pending | Normal | Produce a complete fictional intake profile for a candidate design without assuming a preferred style |
| V10/C02 | [Baseline analysis for existing software](../book/decisions/legacy-baseline-and-modernization-evidence.md) | Claim-level review pending | Normal | Trace measured-before-vs-hypothesized-after claims for catalogue import, compatibility and reversibility |
| V10/C03 | [Pattern applicability and contraindications](../book/decisions/pattern-applicability-and-contraindications.md) | Claim-level review pending | Normal | For same workload, reject two fashionable alternatives with falsifiable tests; link each mechanism's canonical owner |
| V10/C04 | [Alternatives, experiments and ADRs](../book/decisions/architecture-alternatives-experiments-and-adrs.md) | Claim-level review pending | Normal | Write sensitivity analysis where changing one requirement changes preferred architecture; mark invented numbers synthetic |
| V10/C05 | [Target architecture versus transition states](../book/decisions/target-and-transition-architecture-states.md) | Claim-level review pending | High | Test failure after new-only write, idempotent replay and roll-forward when restoring old read path would violate invariants |
| V10/C06 | [Search and question routes for architecture agents](../book/decisions/question-routes-for-architecture-analysis.md) | Claim-level review pending | High | Demonstrate wrong-route and stale-source rejection, stable ID links and token-efficient expansion criteria |
| V10/C07 | [Cross-domain worked comparisons and unresolved cases](../book/decisions/cross-domain-modernization-and-adr-examples.md) | Claim-level review pending | Normal | Provide a complete contrasting legacy modernization ADR with at least one undecidable choice and evidence that would settle it |

## Remediation checkpoint — 2026-10-20 (after baseline `8a1bb1f`)

**Actual book corrections landed:** `250cb6eff558f3971b1af68b6a9f47a367435263`; the controlled six-second trace arithmetic was then corrected in `c3470fe903ab1f99caee4717b345f2cf038d94e1`. The six edited page paths are the exact F-01–F-06 manuscripts above. **They are FIXED IN MANUSCRIPT / SOURCE-REVIEW OPEN, not ACCEPTED**. Earlier finding descriptions remain immutable *baseline observations*, rather than being rewritten as if the gaps never existed.

| Finding | Implemented change and bounded source check | Required remaining signoff |
|---|---|---|
| F-01 V01/C02 | Equal service capacity and deterministic closed-vs-open schedule, six-second offered/completed/backlog table with consistent completion boundaries; explicit k6 source and synthetic label | Independent trace arithmetic/readability review; no k6 execution claimed |
| F-02 V01/C06 | Synthetic 36-month staffing, 90/365-day retention (logical GiB), 45-day double-running and recovery-effort range; sensitivity/reversal under operational gates | Review which dimensions are hard gates vs invented rates; no pricing or real TCO inferred |
| F-03 V02/C03 | Official Spring `@TransactionalEventListener` JavaDoc caveat for already-completed resources, distinct `REQUIRES_NEW` boundary, `fallbackExecution` / no active transaction and non-durability | Run or independently inspect a version-pinned listener/transaction fixture; do not infer recovery guaranteed |
| F-04 V03/C02 | Primary Oracle JDK 24 release evidence confirming JEP 491 delivered, dated OpenJDK implementation-review `LM_LEGACY` caveat, honest note that canonical JEP full text was not fetched | Independent canonical JEP/build-specific confirmation; no JVM execution claimed |
| F-05 V06/C06 | Paired illustrative bounded Cypher and PostgreSQL 17 recursive CTE using same six-node topology, date/tenant guards, expected `U1,U2`, visited-set cycle prevention | Query-engine execution and data/ACL fixture needed before claiming database-specific behavior confirmed |
| F-06 V09/C03 | Separate W3C Baggage normative source, forged tenant/sensitive-key propagation across gateway, provider and telemetry, explicit negative test | Gateway/OTel version configuration and negative security test still proposed, not run |

**Index update:** `55d0abc48ebc38770873c87d249ad908fa5949bc` updates precisely the six changed indexed document SHA-256 checksums and rebuilds the deterministic index snapshot over the unchanged 136-document set; previous snapshot was `e4b4be35…` and newly computed snapshot is `20b86bfb7cb8a2be820d570c66a463ff1f00ae0a7c5d37624239212612c980b6`. The regeneration reproduced the previous pinned digest from the original serialized canonical data before modifying any hashes, and preserved the existing IDs and routing metadata. This is a **deterministic programmatic checksum rebuild**, **not** execution of `scripts/route_index.py` in Python.

**Technical retest status: PENDING.** Previous 13/13 and 195/195 PASS remain valid **only at `8a1bb1f`**. The six new chapters have been read for Markdown H1/fence sanity and source links but the complete repository Python validators, Markdown anchors, SQL/Cypher runtime and independent full-source review have **not** been rerun. A local checkout remains blocked by GitHub DNS resolution in this session. Do not upgrade acceptance status until that follow-up has genuinely run.

## F-07 — standalone Tycho scope contamination risk; corrected

An additional **69/69 canonical-chapter literal-scope scan** checked for explicit `UBS`, `Adro`, `Rocinante`, `900-page`, and distinctive large-system repository/chapter counts. There were **no literal UBS/Adro/Rocinante matches** in the 69 primary chapters. Two V06 search chapters nonetheless contained a **900-page example corpus size**, overlapping a different book's known sizing and unnecessary for a standalone System Design text:

- V06/C03 `book/search/lexical-indexing-bm25-and-sql-fts.md`: removed a prescriptive sentence about a 900-page book needing a distributed cluster and replaced it with a corpus-independent measured-decision criterion.
- V06/C04 `book/search/vector-hnsw-faiss-pgvector.md`: replaced the 900-page corpus sizing statement with an explicitly input-dependent chunk/vector/metadata/index formula.

**Status:** corrected in `30a524b8ee1b83bee118b3666885e46ab3c890ca`; this is editorial scope hygiene, **not evidence** that these two texts actually contained private data. The lexical scan cannot detect every implicit source provenance or similarity. Tycho remains a public, self-contained System Design book and must not import private architecture facts.

## Latest index and targeted static regression checkpoint

- All **eight** edited book pages from F-01–F-07 are indexed with refreshed per-page SHA-256. Latest deterministic index commit is `3e12b6729cd2639c71c3804d4f974cad38ec6e59`, new snapshot `e0bfb5c986de597d074654caae40b6017c5b22476d56cfbd61b4a452b91eae48`, document count **136**, stable IDs/routing metadata unchanged.
- **Targeted GitHub-tree scan:** eight changed chapter files and **133 Markdown-link occurrences** checked for local-file target presence. Found **0 missing local targets**, one H1 per file, balanced triple-backtick fences, and no remaining `900-page` expression in these eight files. This is not a full-fragment-anchor parser, source verification or executable test suite.
- **Python validation status on this latest revision: NOT RUN.** The previous exact-run 13/13 group and 195/195 tests remain evidence **only for `8a1bb1f`**, not for the revised index/book. Before marking any content accepted or promoting PR #217, run the complete Python test/validation suite in a runnable checkout on the new pinned commit and record log artifacts and checked SHA; if the index was rebuilt, verify `scripts/route_index.py` produces exactly the same snapshot and metadata.
- All eight changed chapters remain **SELF-REVIEW FIXED / INDEPENDENT CLAIM REVIEW OPEN**. Other 61 canonical owners are still queued for full source-by-claim editorial acceptance. **Zero of 69 chapters independently accepted.**

## Formal acceptance gate and next edit policy

For each of the 69 chapters, record (a) reviewed manuscript revision and editor identity/role, (b) checked claim(s) and precise official source section/version or clearly labeled mathematical derivation, (c) explicit counterexample/recovery behavior and canonical owner, (d) fiction versus observed/public case classification, (e) unresolved contradictions / requested fix, and (f) the exact review disposition **REJECT / REVISE / SELF-REVIEW PASS / INDEPENDENTLY ACCEPTED**. Do **not** set independent acceptance from word counts, index success, reference presence or an AI-written scenario alone.

Resolve F-01–F-06 and verify claim-level correctness before promoting those six rows. A broader scan may discover new issues in remaining rows; no prior absence of findings should be treated as approval. Review and corrections must remain on PR #217 until controlled merge; after any indexed-document changes, regenerate the route index and re-run full Python tests. Only after independent content signoff for all owners should #213 close and #214 assemble the physical ten-volume edition.
