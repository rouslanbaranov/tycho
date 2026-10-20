# #213 editorial review, second pass — technical claims, contradiction gates and evidence limits

> **Current disposition — 2026-10-20, after PR #218 merge:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

> Source snapshot for these editorial comparisons: the PR's prior full-Python-pass baseline `8a1bb1f`, followed by version-specific repairs on `book/tycho-manuscript-completion-20261020`. Prepared 2026-10-20. This is a scoped assistant-performed **source/claim review**, not an external human expert sign-off. It does **not** claim all external pages were exhaustively read or all chapter assertions validated.

## Summary and exact vocabulary

- **69/69 canonical manuscripts were read at the level of structure, principal mechanisms, source lists and the chapter's worked failure/choice scenario**, cross-compared by owner domain (V01–V10). This is a *coverage pass*, **not** a completed claim-by-claim review of every sentence.
- The `23` entries in the table below are **selected independently compared claims**, representing **22 distinct chapters**. Their source URLs are primary standards/vendor/project documentation and each entry explicitly confines the conclusion. These are **claim-level** dispositions, **not** full-chapter acceptance.
- **47 chapters** did not receive a new independent public-source check in this second pass: manuscript/consistency screening is not labeled evidence of factual verification. They stay open. `SCOPED SUPPORT` means only the named central mechanism is supported, not that its fictional example ran. `REVISED — SOURCE SCOPED` means source review exposed a compatibility/assumption caveat that was **written into the actual book**.
- Independent chapter approvals: **0/69**. Draft PR #217 and #213 remain open. Neither the already reported Python baseline PASS nor a rebuilt hash index can prove content completeness.

## Primary source-to-claim checks

| Canonical owner | Narrow claim compared | Source actually consulted | Supports but does NOT establish | Disposition |
|---|---|---|---|---|
| [V01/C02](../book/performance/workload-demand-and-arrival-models.md) | k6 open-model scheduled arrivals are not coupled to response completion; closed model is | [Official source](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) | Supports generator-model distinction; it does not validate Tycho's invented 2-second service time or any real arrival forecast | SCOPED SUPPORT |
| [V02/C03](../book/application/modular-monolith-and-internal-events.md) | Spring @TransactionalEventListener defaults to AFTER_COMMIT and a post-commit bound resource may still be accessible without a later commit | [Official source](https://docs.spring.io/spring-framework/reference/7.1/data-access/transaction/event.html) | Transaction-bound listener phase is a framework guarantee; crash-durable delivery or a second committed effect is not | SCOPED SUPPORT |
| [V02/C05](../book/application/http-rpc-contracts-and-compatibility.md) | RFC 9110 idempotency describes intended effect of identical requests; client can retry known-idempotent methods after uncertain response | [Official source](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | Does not make a custom POST automatically safe or establish a business key's persistence | SCOPED SUPPORT |
| [V03/C01](../book/execution/threads-tasks-structured-coordination.md) | StructuredTaskScope is preview-only in Java 25 and fork/join controls task lifetime | [Official source](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/StructuredTaskScope.html) | Cannot infer a completed external transaction was rolled back after cancellation; no Java fixture executed | SCOPED SUPPORT |
| [V03/C04](../book/execution/asynchronous-apis-streaming-and-cancellation.md) | gRPC cancellation ends caller interest/work and does not roll back prior changes | [Official source](https://grpc.io/docs/what-is-grpc/core-concepts/) | Does not create a durable streaming replay cursor or exactly-once processing | SCOPED SUPPORT |
| [V03/C05](../book/scaling/connection-pools-hikaricp-pgbouncer.md) | PgBouncer transaction pooling supports protocol-level named prepared statements with version/configuration gates | [Official source](https://www.pgbouncer.org/faq.html) | From 1.21.0 with tracked prepared statements; SQL PREPARE and other session state remain distinct; no JDBC interoperability test | REVISED — SOURCE SCOPED |
| [V04/C03](../book/distributed/transaction-isolation-and-sagas.md) | PostgreSQL Serializable detects dangerous read/write patterns and may abort a transaction | [Official source](https://www.postgresql.org/docs/17/applevel-consistency.html) | Transaction retry must cover the whole decision; no atomicity of external saga effects | SCOPED SUPPORT |
| [V04/C07](../book/integration/kafka-partitions-replication-and-contracts.md) | Kafka 4.1 ELR applies on new clusters by default; 4.0 introduced feature and upgraded clusters need explicit state verification | [Official source](https://kafka.apache.org/41/operations/eligible-leader-replicas/) | Not evidence for unconditional RF=3 losslessness or external DB/offset exactly-once | REVISED — SOURCE SCOPED |
| [V05/C01](../book/data/relational-modeling-and-transaction-isolation.md) | PostgreSQL cross-row constraints/Serializable must be chosen for overlapping-interval business invariant | [Official source](https://www.postgresql.org/docs/17/applevel-consistency.html) | General snapshot-level reads alone are not business exclusion; unrun sample DDL remains hypothetical | SCOPED SUPPORT |
| [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | PostgreSQL ALTER TABLE takes ACCESS EXCLUSIVE unless another lock is specified for that subform | [Official source](https://www.postgresql.org/docs/17/sql-altertable.html) | An additive schema change cannot be assumed instant or lock-free; lock level depends on exact statement | SCOPED SUPPORT |
| [V06/C04](../book/search/vector-hnsw-faiss-pgvector.md) | pgvector approximate scan filters after candidate retrieval; 0.8.0 added iterative scan controls | [Official source](https://github.com/pgvector/pgvector/blob/master/README.md#filtering) | May cause insufficient eligible top-k; it does not imply authorized content leaks if separate ACL enforcement is correct | SCOPED SUPPORT |
| [V06/C06](../book/search/graph-data-models-and-traversal.md) | Neo4j variable-length *m..n syntax still available but is not GQL-conformant | [Official source](https://neo4j.com/docs/cypher-manual/25/patterns/variable-length-paths/) | Graph and CTE have different path uniqueness; no queries executed; Neo4j 2026.02 database language defaults need pinning | REVISED — SOURCE SCOPED |
| [V07/C01](../book/performance/queueing-littles-law.md) | Little's Law L = throughput × mean residence is an average conservation identity in matching boundaries | [Official source](https://www.columbia.edu/~ww2040/LL_OR.pdf) | Not a transient backlog equation using independent p99 or offered load; mathematical examples checked as synthetic | SCOPED SUPPORT |
| [V07/C03](../book/performance/load-testing-and-benchmark-validity.md) | k6 dropped_iterations indicates unsent planned work, with generator exhaustion and SUT slowdown among causes | [Official source](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/) | Cannot infer backend capacity from the scheduled rate when starts were dropped | SCOPED SUPPORT |
| [V08/C01](../book/delivery/ci-cd-provenance-and-gitops.md) | Argo CD cannot roll back application with automated sync enabled | [Official source](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/) | GitOps reconciliation alone cannot undo persisted new-only data; deployment configuration must be version pinned | SCOPED SUPPORT |
| [V08/C01](../book/delivery/ci-cd-provenance-and-gitops.md) | SLSA v1.0 Build and v1.2 Build/Source tracks are different published contracts | [Official source](https://slsa.dev/spec/v1.2/build-track-basics) | Cross-version level names cannot be combined into a single blanket claim about build compliance | REVISED — SOURCE SCOPED |
| [V08/C02](../book/delivery/sbom-attestation-and-release-verification.md) | SLSA v1.2 Build L2 requires authentic signed/verified provenance from hosted build platform; L3 hardened build isolation | [Official source](https://slsa.dev/spec/v1.2/build-track-basics) | Attestation presence or valid signature by arbitrary identity does not establish SLSA level or release authorization | SCOPED SUPPORT |
| [V08/C05](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | PostgreSQL ALTER TABLE lock level is subcommand-specific; ACCESS EXCLUSIVE is the default unless otherwise noted | [Official source](https://www.postgresql.org/docs/17/sql-altertable.html) | No generalized lock-free migration; statement/transaction/existing data must be examined | SCOPED SUPPORT |
| [V08/C07](../book/deployment/disaster-recovery-and-recovery-objectives.md) | RPO and RTO are business-chosen recovery objectives, not benefits guaranteed by replication or region placement | [Official source](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_planning_for_recovery_objective_defined_recovery.html) | Only a valid recovery drill and specified failure model can establish achieved result | SCOPED SUPPORT |
| [V09/C02](../book/observability/metric-pipelines-cardinality-and-retention.md) | OpenTelemetry temporality distinguishes cumulative and delta metric series; conversion has conditions | [Official source](https://opentelemetry.io/docs/specs/otel/metrics/data-model/) | Metrics are not a complete audit ledger; the vendor backend's sampled/incomplete data needs separate evidence | SCOPED SUPPORT |
| [V09/C03](../book/observability/distributed-tracing-context-and-sampling.md) | W3C Baggage permits arbitrary propagated values with privacy/trust-boundary risk | [Official source](https://www.w3.org/TR/baggage/) | Not an authenticated tenant credential; propagation alone does not prove safe gateway filtering | SCOPED SUPPORT |
| [V09/C05](../book/security/identity-authorization-and-isolation.md) | OWASP authorization uses deny-by-default and permission checks on every protected request | [Official source](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Gateway token verification is not equivalent to every object/action/tenant authorization | SCOPED SUPPORT |
| [V09/C07](../book/security/safe-agent-access-and-knowledge-isolation.md) | OWASP denies privileged authorization to source text or simple retrieval matches | [Official source](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Source covers object authorization principle, not a measured agent-injection resistance test | SCOPED SUPPORT |

## Cross-chapter contradiction review and repairs in this pass

**R-08 V03/C05, PgBouncer 1.21+ feature scope.** Older advice that transaction pooling and prepared statements are categorically incompatible is wrong for the supported protocol-level named-statement case: PgBouncer provides `max_prepared_statements` tracking. The chapter already warned conditionally but failed to explain this version-specific compatibility. Added a matrix distinguishing protocol-level named statements, SQL `PREPARE`, session-affine state, JDBC configuration and testing. **Fix in manuscript; integration fixture not run.**

**R-09 V08/C01 ↔ V08/C02, SLSA generations.** V08/C01 cites **SLSA v1.0 Build**, while V08/C02 cites **SLSA v1.2 Build plus Source track**. They are intentionally different versions, not a contradiction if scoped, but readers could combine them into an invented universal level. Added an explicit cross-chapter and track/level comparison to V08/C01. **Fix in manuscript; no deployment verifier was run.**

**R-10 V04/C07, Kafka 4.1 ELR default on new versus upgraded clusters.** The original Kafka 4.1 chapter mentions eligible leader election without foregrounding its **new-cluster default versus existing-cluster upgrade** nuance. Official 4.1 operations reference makes that distinction; added an explicit broker-condition/fault-test subsection. **Fix in manuscript; no Kafka cluster was tested.**

**R-11 V06/C06, Cypher 5/25 grammar and path uniqueness.** Prior synthetic Cypher query uses valid legacy variable-length syntax, which is still documented but not GQL conformant; current new databases may default to Cypher 25. SQL example uses node-simple traversal (`visited`), whereas Cypher relationship-unique paths can revisit vertices. Added version/uniqueness caveat. **Fix in manuscript; neither query executed in a database.**

### Consistency checks that did NOT reveal a substantive contradiction

- **Timeout / commit / cancellation:** V02/C05, V03/C04, V04/C04–C07, V05/C02 and V08/C07 consistently distinguish *unknown client outcome* from *non-commit*; no unconditional cross-system exactly-once guarantee was detected in sampled central sections. This is not a whole-book formal safety proof.
- **Database authority / migration:** V02/C02, V04/C03, V05/C01/C05/C06/C07, V08/C04/C05 and V10/C05 consistently keep a named writer, separate projections from state authority and mark irreversible writes. No claim that an image-only rollback restores new-only persisted data was found in the central sections reviewed.
- **Reactive/virtual-thread trade-offs:** V03/C01–C06 and V07/C02/C05–C07 distinguish execution concurrency from database/queue/lock limits, with release-specific caveats. **Java 25 StructuredTaskScope remains preview API**; do not infer the code examples are release-agnostic or compiled.
- **Retrieval and authorization:** V06/C03–C07, V09/C05/C07 and V10/C06 consistently distinguish retrieval ranking and graph path existence from authorization or evidentiary truth; successful semantic match must not grant tool or tenant permissions.
- **Evidence taxonomy:** M9 case links in V02–V10 are marked historical first-party or synthetic transfer material, not universal benchmarks. Case-specific underlying first-party statement-by-statement validation was **not** performed for all 35 M9 pages during this pass and remains a separate acceptance duty.

## Snapshot mathematics sanity checks (synthetic inputs, not measurements)

| Worked example | Independent arithmetic | Interpretation |
|---|---|---|
| V01/C06 staffing | `60 + (36 × 10 / 8) = 105`; `140 + (36 × 25 / 8) = 252.5` engineer-days | Partial staffing accounting, **not** total financial TCO |
| V03/C05 connection fleet | `8 × 20 = 160` potential app leases versus 60 configured backend slots | Cannot infer 160 simultaneous database executions |
| V07/C01 latency mixture | `0.95×0.10 + 0.05×2.10 = 0.20` seconds; `120×0.20=24` average in system | Mean, not p99, enters Little's Law under matched stable boundary |
| V07/C02 Amdahl | `1/(0.2 + 0.8/8) = 3.333…` conditional speedup | Serial fraction bound, **not** a real fleet forecast |
| V07/C06 scale reaction | `15 + 10 + 20 + 25 = 70` seconds > 40-second burst | Hypothetical delayed scale, no cluster experiment |
| V09/C01 error allowance | `10,000 × (1−0.999) = 10` allowed errors; `30 / 10 = 300%` budget consumed | Illustrative SLO under stipulated eligibility |
| V09/C02 label cardinality | `40×5×3×2,000 = 1,200,000` series; `1,200,000 / 15 = 80,000` samples/s if all sampled each interval | Maximum Cartesian product and fictional full occupancy |

These arithmetic spot checks can be repeated deterministically, but are not a proxy for SQL, JVM, broker, migration, DR or authorized-retrieval integration tests.

## All 69 owners: review coverage versus technical acceptance

Every primary chapter received **manuscript-level topical and owner-overlap screening**; the following status intentionally separates chapters with a *selected* public claim independently compared from chapters that still require that step. For both groups, **full editorial acceptance remains OPEN**.

| Chapter | Manuscript | This pass | Risk priority for next source/implementation review |
|---|---|---|---|
| V01/C01 | [Problem framing and system boundaries](../book/application/problem-framing-and-system-boundaries.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V01/C02 | [Workload and demand models](../book/performance/workload-demand-and-arrival-models.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V01/C03 | [Quality attributes and trade-offs](../book/application/quality-drivers-and-architecture-views.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V01/C04 | [Evidence, hypotheses and architecture experiments](../book/application/architecture-evidence-hypotheses-and-experiments.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V01/C05 | [Architecture descriptions and decision records](../book/application/architecture-views-and-decision-records.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V01/C06 | [Capacity, operational constraints and total cost](../book/application/operational-constraints-and-total-cost-gates.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V02/C01 | [Layered, modular and ports-and-adapters design](../book/application/layered-hexagonal-ports-and-adapters.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V02/C02 | [Domain boundaries, data ownership and contracts](../book/application/domain-boundaries-data-ownership-and-contracts.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V02/C03 | [Modular monolith and internal events](../book/application/modular-monolith-and-internal-events.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V02/C04 | [SOA, microservices and distributed boundaries](../book/application/service-orientation-microservices-and-distribution.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V02/C05 | [Public APIs, HTTP/RPC and compatibility](../book/application/http-rpc-contracts-and-compatibility.md) | SELECTED CLAIM SOURCE-CHECKED | Normal |
| V02/C06 | [Integration adapters and anti-corruption boundaries](../book/application/anti-corruption-adapters-and-coexistence.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V02/C07 | [Authorization boundaries and multitenancy](../book/application/authorization-boundaries-and-multitenancy.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V03/C01 | [Threads, tasks and coordination](../book/execution/threads-tasks-structured-coordination.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V03/C02 | [Java execution and virtual threads](../book/execution/platform-threads-executors-and-virtual-threads.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V03/C03 | [Reactive streams, demand and cancellation](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V03/C04 | [Asynchronous APIs and streaming](../book/execution/asynchronous-apis-streaming-and-cancellation.md) | SELECTED CLAIM SOURCE-CHECKED | Normal |
| V03/C05 | [Thread, connection and buffer pools](../book/scaling/connection-pools-hikaricp-pgbouncer.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V03/C06 | [Memory, GC, CPU and blocking diagnostics](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V04/C01 | [Time, causality and ordering](../book/distributed/causality-ordering-and-consensus.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V04/C02 | [Replication, consensus and leader changes](../book/distributed/replication-consensus-and-leader-change.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V04/C03 | [Consistency and distributed transactions](../book/distributed/transaction-isolation-and-sagas.md) | SELECTED CLAIM SOURCE-CHECKED | Normal |
| V04/C04 | [Retries, idempotency and duplicate effects](../book/distributed/retries-idempotency-and-ambiguous-effects.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V04/C05 | [Outbox, inbox, sagas and durable workflows](../book/distributed/outbox-inbox-sagas-and-durable-workflows.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V04/C06 | [Messaging families and delivery contracts](../book/integration/messaging-families-and-durable-workflows.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V04/C07 | [Kafka logs, partitions and transactions](../book/integration/kafka-partitions-replication-and-contracts.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V04/C08 | [Stateful/event-time stream processing](../book/integration/stateful-stream-processing-and-cdc.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V05/C01 | [Relational modeling and transaction isolation](../book/data/relational-modeling-and-transaction-isolation.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V05/C02 | [PostgreSQL MVCC, WAL and recovery](../book/data/postgresql-wal-replication-and-recovery.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V05/C03 | [Query planning, indexes and access paths](../book/data/postgresql-indexes-statistics-and-query-plans.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V05/C04 | [Alternative data models and stores](../book/data/storage-model-alternatives-and-workload-fit.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V05/C05 | [Partitioning, sharding and rebalancing](../book/scaling/shard-keys-hotspots-and-resharding.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V05/C06 | [Schema evolution, data migration and retention](../book/data/schema-lifecycle-and-semantic-migration.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V05/C07 | [Replication, backups and restore drills](../book/data/backup-restore-pitr-and-recovery-drills.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V06/C01 | [Local and distributed caching](../book/scaling/local-and-distributed-cache-design.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V06/C02 | [Hot keys, cache stampedes and read amplification](../book/scaling/cache-invalidation-stampede-and-hot-keys.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V06/C03 | [Lexical full-text indexing and ranking](../book/search/lexical-indexing-bm25-and-sql-fts.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V06/C04 | [Vector embeddings and nearest-neighbor retrieval](../book/search/vector-hnsw-faiss-pgvector.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V06/C05 | [Hybrid retrieval and reranking](../book/search/hybrid-ranking-graph-and-evaluation.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V06/C06 | [Graph relationships and traversal](../book/search/graph-data-models-and-traversal.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V06/C07 | [Retrieval evaluation and index lifecycle](../book/search/retrieval-evaluation-and-index-lifecycle.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V07/C01 | [Queueing, Little's Law and measurement boundaries](../book/performance/queueing-littles-law.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V07/C02 | [Contention, saturation and scaling laws](../book/performance/contention-saturation-and-scaling-laws.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V07/C03 | [Load-test methods and benchmark validity](../book/performance/load-testing-and-benchmark-validity.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V07/C04 | [Tail latency, fan-out and time budgets](../book/performance/tail-latency-fanout-and-deadline-budgets.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V07/C05 | [Overload protection and graceful degradation](../book/performance/overload-admission-control-and-graceful-degradation.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V07/C06 | [Horizontal/vertical scaling and autoscaling delay](../book/performance/autoscaling-lag-and-capacity-limits.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V07/C07 | [Capacity planning and cost/performance trade-offs](../book/performance/capacity-planning-and-cost-performance.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V08/C01 | [CI/CD architecture and artifact provenance](../book/delivery/ci-cd-provenance-and-gitops.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V08/C02 | [Supply chain and release verification](../book/delivery/sbom-attestation-and-release-verification.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V08/C03 | [VMs, containers, orchestration and serverless](../book/deployment/runtime-placement-and-control-plane.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V08/C04 | [GitOps, rollout and progressive delivery](../book/delivery/gitops-canary-and-progressive-rollout.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V08/C05 | [Backward-compatible database change](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V08/C06 | [High availability and failure-domain placement](../book/deployment/availability-zones-placement-and-failure-domains.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V08/C07 | [Multi-region recovery and data reconciliation](../book/deployment/disaster-recovery-and-recovery-objectives.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V09/C01 | [SLIs, SLOs and error budgets](../book/observability/service-level-indicators-objectives-and-alerts.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V09/C02 | [Metrics ingestion, cardinality and time-series storage](../book/observability/metric-pipelines-cardinality-and-retention.md) | SELECTED CLAIM SOURCE-CHECKED | Normal |
| V09/C03 | [Distributed tracing and propagation](../book/observability/distributed-tracing-context-and-sampling.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V09/C04 | [Logging, audit and lineage](../book/observability/logs-audit-and-data-lineage.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V09/C05 | [Identity, authorization and threat modeling](../book/security/identity-authorization-and-isolation.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V09/C06 | [Incident response and operational change](../book/observability/incident-response-and-operational-change.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V09/C07 | [Safety, isolation and privacy in agent-accessible services](../book/security/safe-agent-access-and-knowledge-isolation.md) | SELECTED CLAIM SOURCE-CHECKED | High |
| V10/C01 | [Architecture requirement and workload profiles](../book/decisions/requirements-and-workload-architecture-profiles.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V10/C02 | [Baseline analysis for existing software](../book/decisions/legacy-baseline-and-modernization-evidence.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V10/C03 | [Pattern applicability and contraindications](../book/decisions/pattern-applicability-and-contraindications.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V10/C04 | [Alternatives, experiments and ADRs](../book/decisions/architecture-alternatives-experiments-and-adrs.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V10/C05 | [Target architecture versus transition states](../book/decisions/target-and-transition-architecture-states.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | High |
| V10/C06 | [Search and question routes for architecture agents](../book/decisions/question-routes-for-architecture-analysis.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |
| V10/C07 | [Cross-domain worked comparisons and unresolved cases](../book/decisions/cross-domain-modernization-and-adr-examples.md) | REVIEWED IN MANUSCRIPT; SOURCE CLAIM-CHECK PENDING | Normal |

## Mandatory next gate

1. Complete rigorous **statement-by-statement** external-source checks, especially every versioned protocol/driver/SQL example and all M9 first-party historical claims; record paragraph anchor, published subsection/revision, contradiction and verdict.
2. For fabricated tests, require a hand-checked oracle where possible. SQL/Cypher/Java/Kafka/Hikari/Flink integration behaviors must remain **proposed**, not "PASS", until run under version-pinned conditions. Actual source documentation cannot prove an invented deployment.
3. Rebuild routing index after book edits and run the full Python validation suite again on the final exact PR commit. Report both command output and revision; previous `8a1bb1f` baseline PASS does **not** transfer automatically.
4. Maintain `DEEPENED — REVIEW OPEN` for all 69 until genuinely independent content review/acceptance. #214 (physical edition/publishing) starts only after substantive approval. Owner-cancelled visual rendering/live MCP checks are not reinstated.
