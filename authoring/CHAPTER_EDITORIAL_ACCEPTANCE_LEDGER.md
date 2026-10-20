# Editorial acceptance ledger — all 69 proposed Tycho chapters

> **Historical manuscript transition — 2026-10-20, before edition assembly:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


## Current package acceptance — 2026-10-20

The owner confirms that independent acceptance of the integrated manuscript,
including this 69-chapter package, is **COMPLETED**. Visual rendering and live
MCP checks are **CANCELLED by owner decision**. See the authoritative
[acceptance disposition](ACCEPTANCE_DISPOSITION_2026-10-20.md). The dated
`PENDING` rows below are the historical pre-review register, not the current
package verdict. No missing reviewer identity or per-chapter evidence is
fabricated, and no GitHub issue or milestone is closed by this record.

**Checkpoint:** 2026-10-19; PR [#215](https://github.com/rouslanbaranov/tycho/pull/215) draft, tracked by [content issue #213](https://github.com/rouslanbaranov/tycho/issues/213). Source: [69-row question coverage audit](BOOK_COMPLETENESS_AUDIT.md) and GitHub-file reads from the same branch. This is a **review-control document, not release sign-off**.

## Current objectively verified state

- **69 distinct proposed Vxx/Cxx IDs, 69 distinct primary Markdown paths, 69/69 files fetched from the active branch**. No primary article is now assigned to two planned chapter IDs; the eight historical multi-owner overlap groups have been separated **at file-path ownership level**.
- **111,272 whitespace-separated Markdown tokens/words** across the 69 primary drafts at this checkpoint (sum of simple `trim().split(/\s+/)` counts returned while re-reading files). This **includes Markdown syntax, tables, reference URLs, diagram labels and citations**: it is neither prose word count nor pagination, and indicates no completeness or quality threshold. It excludes preserved earlier shared research and unlisted supplementary pages.
- **All 69 chapter content/technical/source acceptance states are still PENDING**. No chapter is certified merely by having an H1, source links, 1,000 words or a Mermaid diagram. The editorial contract explicitly rejects fixed page or word quotas.
- **44/44 distinct local link-target files** referenced by the preceding 13 newly authored owner drafts were re-fetched and existed. This tests target file existence **only**; anchors, individual assertions, bibliography versions, diagram rendering and complete repo navigation remain unchecked.
- **Four narrow public reference samples** independently rechecked during this checkpoint: public consumer-deduplication pattern (Microservices.io), saga local-transaction/compensation semantics (Microservices.io), PostgreSQL 17 isolation behaviors, and Kubernetes topology spread constraints; independent URL/document checks do not establish full source-to-claim acceptance or runtime tests. Published AWS recovery automation guidance was also inspected for its fail-safe stop rule.
- **Nothing has been merged**; the planned edition under [#214](https://github.com/rouslanbaranov/tycho/issues/214) does not exist yet. No external/private system content, agents, scheduled workers, MCP/search infrastructure or curated book knowledge graph was added during this verification.

## Draft size and review planning by proposed volume

| Planned volume | Unique primary drafts | Count incl. Markdown markup | Per-chapter count range |
|---|---:|---:|---|
| V01 | 6 | 9,979 | 1,355–2,168 |
| V02 | 7 | 11,453 | 1,354–2,357 |
| V03 | 6 | 8,620 | 1,018–1,861 |
| V04 | 8 | 12,552 | 1,219–1,787 |
| V05 | 7 | 10,950 | 1,131–2,065 |
| V06 | 7 | 9,743 | 1,113–1,711 |
| V07 | 7 | 13,367 | 1,408–3,068 |
| V08 | 7 | 9,646 | 1,045–1,841 |
| V09 | 7 | 11,015 | 1,173–1,856 |
| V10 | 7 | 13,947 | 1,617–2,453 |
| **All** | **69** | **111,272** | **1,018–3,068** |

These numbers are **triage signals, not required word targets**. A relatively short chapter may be complete if the question is narrow and well explained; a relatively long one may be repetitive or contain unverified claims.

## Per-chapter review register

**Status key:** `PENDING` means the draft and primary owner have been identified, but a reviewer has **not yet signed off** on completeness, scientific/technical accuracy, copyright-safe independent source admission, absence of unsupported generalization, consistency with other chapters, rendered navigable structure or experiment limits. The historical matrix's `D` means **direct topical treatment**, not acceptance.

| Chapter | Proposed question owner | Unique primary draft | Markdown whitespace-separated count | Editorial acceptance |
|---|---|---|---:|---|
| V01/C01 | Problem framing and system boundaries | [Primary draft](../book/volumes/v01/c01/problem-framing-and-system-boundaries.md) | 2,168 | PENDING |
| V01/C02 | Workload and demand models | [Primary draft](../book/volumes/v01/c02/workload-demand-and-arrival-models.md) | 1,825 | PENDING |
| V01/C03 | Quality attributes and trade-offs | [Primary draft](../book/volumes/v01/c03/quality-drivers-and-architecture-views.md) | 1,823 | PENDING |
| V01/C04 | Evidence, hypotheses and architecture experiments | [Primary draft](../book/volumes/v01/c04/architecture-evidence-hypotheses-and-experiments.md) | 1,387 | PENDING |
| V01/C05 | Architecture descriptions and decision records | [Primary draft](../book/volumes/v01/c05/architecture-views-and-decision-records.md) | 1,421 | PENDING |
| V01/C06 | Capacity, operational constraints and total cost | [Primary draft](../book/volumes/v01/c06/operational-constraints-and-total-cost-gates.md) | 1,355 | PENDING |
| V02/C01 | Layered, modular and ports-and-adapters design | [Primary draft](../book/volumes/v02/c01/layered-hexagonal-ports-and-adapters.md) | 1,432 | PENDING |
| V02/C02 | Domain boundaries, data ownership and contracts | [Primary draft](../book/volumes/v02/c02/domain-boundaries-data-ownership-and-contracts.md) | 1,810 | PENDING |
| V02/C03 | Modular monolith and internal events | [Primary draft](../book/volumes/v02/c03/modular-monolith-and-internal-events.md) | 1,359 | PENDING |
| V02/C04 | SOA, microservices and distributed boundaries | [Primary draft](../book/volumes/v02/c04/service-orientation-microservices-and-distribution.md) | 1,488 | PENDING |
| V02/C05 | Public APIs, HTTP/RPC and compatibility | [Primary draft](../book/volumes/v02/c05/http-rpc-contracts-and-compatibility.md) | 2,357 | PENDING |
| V02/C06 | Integration adapters and anti-corruption boundaries | [Primary draft](../book/volumes/v02/c06/anti-corruption-adapters-and-coexistence.md) | 1,653 | PENDING |
| V02/C07 | Authorization boundaries and multitenancy | [Primary draft](../book/volumes/v02/c07/authorization-boundaries-and-multitenancy.md) | 1,354 | PENDING |
| V03/C01 | Threads, tasks and coordination | [Primary draft](../book/volumes/v03/c01/threads-tasks-structured-coordination.md) | 1,018 | PENDING |
| V03/C02 | Java execution and virtual threads | [Primary draft](../book/volumes/v03/c02/platform-threads-executors-and-virtual-threads.md) | 1,309 | PENDING |
| V03/C03 | Reactive streams, demand and cancellation | [Primary draft](../book/volumes/v03/c03/reactor-webflux-r2dbc-and-backpressure.md) | 1,567 | PENDING |
| V03/C04 | Asynchronous APIs and streaming | [Primary draft](../book/volumes/v03/c04/asynchronous-apis-streaming-and-cancellation.md) | 1,217 | PENDING |
| V03/C05 | Thread, connection and buffer pools | [Primary draft](../book/volumes/v03/c05/connection-pools-hikaricp-pgbouncer.md) | 1,648 | PENDING |
| V03/C06 | Memory, GC, CPU and blocking diagnostics | [Primary draft](../book/volumes/v03/c06/cpu-memory-gc-and-blocking-diagnostics.md) | 1,861 | PENDING |
| V04/C01 | Time, causality and ordering | [Primary draft](../book/volumes/v04/c01/causality-ordering-and-consensus.md) | 1,726 | PENDING |
| V04/C02 | Replication, consensus and leader changes | [Primary draft](../book/volumes/v04/c02/replication-consensus-and-leader-change.md) | 1,219 | PENDING |
| V04/C03 | Consistency and distributed transactions | [Primary draft](../book/volumes/v04/c03/transaction-isolation-and-sagas.md) | 1,787 | PENDING |
| V04/C04 | Retries, idempotency and duplicate effects | [Primary draft](../book/volumes/v04/c04/retries-idempotency-and-ambiguous-effects.md) | 1,458 | PENDING |
| V04/C05 | Outbox, inbox, sagas and durable workflows | [Primary draft](../book/volumes/v04/c05/outbox-inbox-sagas-and-durable-workflows.md) | 1,487 | PENDING |
| V04/C06 | Messaging families and delivery contracts | [Primary draft](../book/volumes/v04/c06/messaging-families-and-durable-workflows.md) | 1,564 | PENDING |
| V04/C07 | Kafka logs, partitions and transactions | [Primary draft](../book/volumes/v04/c07/kafka-partitions-replication-and-contracts.md) | 1,715 | PENDING |
| V04/C08 | Stateful/event-time stream processing | [Primary draft](../book/volumes/v04/c08/stateful-stream-processing-and-cdc.md) | 1,596 | PENDING |
| V05/C01 | Relational modeling and transaction isolation | [Primary draft](../book/volumes/v05/c01/relational-modeling-and-transaction-isolation.md) | 1,574 | PENDING |
| V05/C02 | PostgreSQL MVCC, WAL and recovery | [Primary draft](../book/volumes/v05/c02/postgresql-wal-replication-and-recovery.md) | 1,569 | PENDING |
| V05/C03 | Query planning, indexes and access paths | [Primary draft](../book/volumes/v05/c03/postgresql-indexes-statistics-and-query-plans.md) | 1,456 | PENDING |
| V05/C04 | Alternative data models and stores | [Primary draft](../book/volumes/v05/c04/storage-model-alternatives-and-workload-fit.md) | 2,065 | PENDING |
| V05/C05 | Partitioning, sharding and rebalancing | [Primary draft](../book/volumes/v05/c05/shard-keys-hotspots-and-resharding.md) | 1,526 | PENDING |
| V05/C06 | Schema evolution, data migration and retention | [Primary draft](../book/volumes/v05/c06/schema-lifecycle-and-semantic-migration.md) | 1,131 | PENDING |
| V05/C07 | Replication, backups and restore drills | [Primary draft](../book/volumes/v05/c07/backup-restore-pitr-and-recovery-drills.md) | 1,629 | PENDING |
| V06/C01 | Local and distributed caching | [Primary draft](../book/volumes/v06/c01/local-and-distributed-cache-design.md) | 1,254 | PENDING |
| V06/C02 | Hot keys, cache stampedes and read amplification | [Primary draft](../book/volumes/v06/c02/cache-invalidation-stampede-and-hot-keys.md) | 1,338 | PENDING |
| V06/C03 | Lexical full-text indexing and ranking | [Primary draft](../book/volumes/v06/c03/lexical-indexing-bm25-and-sql-fts.md) | 1,337 | PENDING |
| V06/C04 | Vector embeddings and nearest-neighbor retrieval | [Primary draft](../book/volumes/v06/c04/vector-hnsw-faiss-pgvector.md) | 1,503 | PENDING |
| V06/C05 | Hybrid retrieval and reranking | [Primary draft](../book/volumes/v06/c05/hybrid-ranking-graph-and-evaluation.md) | 1,711 | PENDING |
| V06/C06 | Graph relationships and traversal | [Primary draft](../book/volumes/v06/c06/graph-data-models-and-traversal.md) | 1,113 | PENDING |
| V06/C07 | Retrieval evaluation and index lifecycle | [Primary draft](../book/volumes/v06/c07/retrieval-evaluation-and-index-lifecycle.md) | 1,487 | PENDING |
| V07/C01 | Queueing, Little's Law and measurement boundaries | [Primary draft](../book/volumes/v07/c01/queueing-littles-law.md) | 3,068 | PENDING |
| V07/C02 | Contention, saturation and scaling laws | [Primary draft](../book/volumes/v07/c02/contention-saturation-and-scaling-laws.md) | 1,457 | PENDING |
| V07/C03 | Load-test methods and benchmark validity | [Primary draft](../book/volumes/v07/c03/load-testing-and-benchmark-validity.md) | 1,773 | PENDING |
| V07/C04 | Tail latency, fan-out and time budgets | [Primary draft](../book/volumes/v07/c04/tail-latency-fanout-and-deadline-budgets.md) | 2,155 | PENDING |
| V07/C05 | Overload protection and graceful degradation | [Primary draft](../book/volumes/v07/c05/overload-admission-control-and-graceful-degradation.md) | 1,712 | PENDING |
| V07/C06 | Horizontal/vertical scaling and autoscaling delay | [Primary draft](../book/volumes/v07/c06/autoscaling-lag-and-capacity-limits.md) | 1,794 | PENDING |
| V07/C07 | Capacity planning and cost/performance trade-offs | [Primary draft](../book/volumes/v07/c07/capacity-planning-and-cost-performance.md) | 1,408 | PENDING |
| V08/C01 | CI/CD architecture and artifact provenance | [Primary draft](../book/volumes/v08/c01/ci-cd-provenance-and-gitops.md) | 1,489 | PENDING |
| V08/C02 | Supply chain and release verification | [Primary draft](../book/volumes/v08/c02/sbom-attestation-and-release-verification.md) | 1,841 | PENDING |
| V08/C03 | VMs, containers, orchestration and serverless | [Primary draft](../book/volumes/v08/c03/runtime-placement-and-control-plane.md) | 1,783 | PENDING |
| V08/C04 | GitOps, rollout and progressive delivery | [Primary draft](../book/volumes/v08/c04/gitops-canary-and-progressive-rollout.md) | 1,045 | PENDING |
| V08/C05 | Backward-compatible database change | [Primary draft](../book/volumes/v08/c05/mixed-version-database-compatibility-and-online-ddl.md) | 1,239 | PENDING |
| V08/C06 | High availability and failure-domain placement | [Primary draft](../book/volumes/v08/c06/availability-zones-placement-and-failure-domains.md) | 1,099 | PENDING |
| V08/C07 | Multi-region recovery and data reconciliation | [Primary draft](../book/volumes/v08/c07/disaster-recovery-and-recovery-objectives.md) | 1,150 | PENDING |
| V09/C01 | SLIs, SLOs and error budgets | [Primary draft](../book/volumes/v09/c01/service-level-indicators-objectives-and-alerts.md) | 1,475 | PENDING |
| V09/C02 | Metrics ingestion, cardinality and time-series storage | [Primary draft](../book/volumes/v09/c02/metric-pipelines-cardinality-and-retention.md) | 1,548 | PENDING |
| V09/C03 | Distributed tracing and propagation | [Primary draft](../book/volumes/v09/c03/distributed-tracing-context-and-sampling.md) | 1,173 | PENDING |
| V09/C04 | Logging, audit and lineage | [Primary draft](../book/volumes/v09/c04/logs-audit-and-data-lineage.md) | 1,392 | PENDING |
| V09/C05 | Identity, authorization and threat modeling | [Primary draft](../book/volumes/v09/c05/identity-authorization-and-isolation.md) | 1,796 | PENDING |
| V09/C06 | Incident response and operational change | [Primary draft](../book/volumes/v09/c06/incident-response-and-operational-change.md) | 1,856 | PENDING |
| V09/C07 | Safety, isolation and privacy in agent-accessible services | [Primary draft](../book/volumes/v09/c07/safe-agent-access-and-knowledge-isolation.md) | 1,775 | PENDING |
| V10/C01 | Architecture requirement and workload profiles | [Primary draft](../book/volumes/v10/c01/requirements-and-workload-architecture-profiles.md) | 2,236 | PENDING |
| V10/C02 | Baseline analysis for existing software | [Primary draft](../book/volumes/v10/c02/legacy-baseline-and-modernization-evidence.md) | 2,453 | PENDING |
| V10/C03 | Pattern applicability and contraindications | [Primary draft](../book/volumes/v10/c03/pattern-applicability-and-contraindications.md) | 2,055 | PENDING |
| V10/C04 | Alternatives, experiments and ADRs | [Primary draft](../book/volumes/v10/c04/architecture-alternatives-experiments-and-adrs.md) | 1,617 | PENDING |
| V10/C05 | Target architecture versus transition states | [Primary draft](../book/volumes/v10/c05/target-and-transition-architecture-states.md) | 1,762 | PENDING |
| V10/C06 | Search and question routes for architecture agents | [Primary draft](../book/volumes/v10/c06/question-routes-for-architecture-analysis.md) | 1,985 | PENDING |
| V10/C07 | Cross-domain worked comparisons and unresolved cases | [Primary draft](../book/volumes/v10/c07/cross-domain-modernization-and-adr-examples.md) | 1,839 | PENDING |

## Required acceptance evidence (per chapter)

A chapter can change from `PENDING` only after all applicable gates have records of actual work and an accountable reviewer:

1. **Substantive and original content:** read whole chapter and relevant prior research; confirm the chapter answers its stated question, alternatives, contraindications, invariants, failure and recovery, with no unsupported choices or duplicated canonical mechanism.
2. **Claim-by-claim public evidence:** identify each material fact, the exact public source section/version/date and a license/reuse-admission outcome; classify source-documented behavior versus independent inference versus tested observation. Failed/unavailable sources are unresolved, not silently replaced.
3. **Examples, diagrams and maths:** check each example is synthetic or supported by reproducible evidence; validate arithmetic, message order, stated assumptions, negative/failure cases and diagram text alternatives. Render Mermaid, do not infer correctness from fences alone.
4. **Executable validation where relevant:** implement and run an isolated, permissible fixture for empirically testable claims (for instance isolation race, index plan, cache stale fill, rollback data compatibility); record exact environment/commands, actual outputs, limitations and reviewer. This is not a requirement to build production infrastructure.
5. **Editorial/navigation:** ensure one canonical owner for each mechanism, meaningful bounded sections, correct parent/adjacent links and link anchors, source versions, frontmatter/schema and routing metadata when edition identity has been designed. Preserve original source-research pages until they are fully remapped/reconciled.
6. **Independent-origin/security review:** confirm no disallowed private/domain-specific source or inferred architecture, ensure examples are independently invented and that safety/privacy/security claims are bounded.
7. **Final disposition:** mark one of `ACCEPTED`, `REVISION_REQUIRED`, `BLOCKED_EVIDENCE` with date, reviewer identity and exact checked evidence; do not mark accepted automatically from file existence, length or a passing static linter.

## Immediate editorial priorities from observed content

- Review all **eight previously overlapping original research groups** for claim preservation; the latest primary-file assignment fixes ownership, not completeness or duplication within actual prose.
- Start with cross-chapter interfaces whose misunderstood guarantees cause severe errors: V04/C04–C05 retries/outbox, V05/C01–C03 transaction isolation/planning, V06/C01–C02 cache invalidation, V08/C04–C07 rollback and recovery, and V09/C03–C04 trace versus audit.
- Pay extra attention to compact but high-consequence technical pages such as **V03/C01** (task cancellation), **V08/C04** (rollout gating), **V08/C06–C07** (HA/DR), and **V06/C06** (graph query semantics as a topic, not an infrastructure feature). Compactness is not a failure classification.
- Audit the **whole Git source tree** for manuscript content not listed as a primary target. This register verifies *assigned primary drafts only*. Do not delete or migrate old pages solely because a mapping exists.
- Defer final ten-volume/69-chapter/page packaging until chapters pass content/source/depth acceptance. Issue #214 is an edition build task, not a substitute for #213.

## Public-source spot check, independent of acceptance

[Eleven exact narrow source/claim comparisons across seven technical manuscript owners](CLAIM_VERIFICATION_SPOTCHECK_2026-10-19.md) were documented against published PostgreSQL 17, OASIS SOA, Kubernetes, Microservices.io and AWS references. The checked narrow assertions matched their bounded source sections; **the seven full chapters remain PENDING**, and no experiment, source-license audit or independent editorial sign-off was performed.

## Focused source verification and manuscript deepening — V05/C01

- Rechecked exact PostgreSQL **17** published sections for [transaction isolation](https://www.postgresql.org/docs/17/transaction-iso.html), [constraints](https://www.postgresql.org/docs/17/ddl-constraints.html), [range types and range constraints](https://www.postgresql.org/docs/17/rangetypes.html), and [`btree_gist` operator classes](https://www.postgresql.org/docs/17/btree-gist.html). Their documented behavior was used to add a **clearly unexecuted** example of an overlapping-booking exclusion constraint to [V05/C01](../book/volumes/v05/c01/relational-modeling-and-transaction-isolation.md). It now has **1,574** whitespace-separated Markdown terms at the new checkpoint (previously 1,224).
- Clarified a PostgreSQL-specific nuance: the Repeatable Read snapshot begins with the first non-transaction-control statement rather than simply at `BEGIN`; serialization anomaly limits and transaction retry requirements were checked against §13.2.
- **The SQL example was not run.** No `psql` or PostgreSQL server executable was detected in the working runtime (only `pg_config`), and a static Markdown/link check cannot establish SQL correctness. A real PostgreSQL 17 fixture and concurrent-write/restore experiment remain required for operational acceptance.
- This is a **partial evidence verification**, not comprehensive technical chapter sign-off. Its status remains PENDING. The recorded book-primary aggregate was updated by the measured 350-term difference.

## Reproducibility and open limitations

The primary mapping is derived from the verified 69-row [coverage audit](BOOK_COMPLETENESS_AUDIT.md); word-count values were recorded in five bounded GitHub file-read batches against the feature branch. No full local checkout, `scripts/premerge_check.py`, `scripts/check_boundary.py`, complete link-anchor validator, independent copyright/source-per-claim reviewer, executed performance/consistency experiment, generated final page index or edition build ran here. Exact measurements beyond the source-file existence and simple structural counts must not be implied.
