# Unified Tycho book — M1–M8 foundational chapters + M9 applied cases

**Integration checkpoint:** 2026-10-19.  
**Branch:** `integration/tycho-m1-m9-unified-manuscript-20261019` — **DRAFT, not merged to main**.  
**Frozen parents:** core PR [#215](https://github.com/rouslanbaranov/tycho/pull/215) at `baaede83f09db3897965d07a7b0300dc3101da34`; M9 PR [#212](https://github.com/rouslanbaranov/tycho/pull/212) at `af83315ecf539caf5c95d1b9d944ce0d8d100903`. Both parent commit histories are preserved by the merge commit. Source PRs and M9 remain open/draft; [#121](https://github.com/rouslanbaranov/tycho/issues/121) and [#213](https://github.com/rouslanbaranov/tycho/issues/213) remain open.

## Editorial decision: ONE book, multiple complementary evidence types

Tycho stays a single standalone System Design book, not a foundational book competing with a separately accepted M9 product. The current planned canonical structure is **10 volumes / 69 technical and decision-oriented chapter questions**, supported by a **linked applied case-study collection (29 case pages and six synthetic comparative decision playbooks)**.

The case study collection is a **companion evidence/transfer layer**, not an automatically appended eleventh conceptual volume, a replacement for first-principles technical chapters, or 35 unreviewed "accepted chapters". This is a **proposed editorial placement**, to be finalized during [edition assembly #214](https://github.com/rouslanbaranov/tycho/issues/214). A case's vendor-reported historical results must never become a generic mechanism or Tycho recommendation unless independently justified. A decision playbook's synthetic ADR is not an historical decision of its case companies.

### Reading flow for engineers and external agents

1. **Requirements/question:** choose an exact Vxx/Cxx question in [the 69-question outline](../book/PROPOSED-STRUCTURE.md) and [unique owner audit](BOOK_COMPLETENESS_AUDIT.md).
2. **Canonical mechanism:** read the exact primary text from the [69-chapter editorial ledger](CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md), including assumptions, normal/failure/recovery, contraindications and source limits.
3. **Real-world evidence:** selectively retrieve a historical [case page](../book/cases/README.md) from this crosswalk, verify publication period, company-reported observations, direct public sources, unavailable claims and negative results. Cases do not override the technical chapter's explicit invariant.
4. **Architecture transfer:** use a relevant draft decision guide to form *conditional* alternatives, experiments, limits and an ADR. Treat requirements, existing legacy state and migration risks as inputs, not slogans.
5. **Evidence output:** return a bounded answer with source revisions, uncertainty, counterexamples, and precisely marked proposed experiments. No all-corpus dump, unsupported architecture selection, fabricated benchmark, or unauthorized action.

No manually curated concept graph, graph database, graph edges, graph traversal, graph maintenance, or graph-aware MCP requirement is included in Tycho infrastructure. **Graph data technology remains a valid theoretical V06/C06 chapter and historical case subject**, not a platform feature. Stable Markdown references, structured metadata, provenance, lexical/hybrid search methods and future read-only MCP remain the retrieval plan.

## Mapping 29 historical case pages into core concepts

**This is an editorial reading-route proposal derived from subject and case scope, not an independent assessment that every company's historical claim supports the mapped chapter.** The primary chapter is the most useful conceptual entry; the secondary helps challenge or qualify the result. Source-specific reviewers must confirm mapping after exact claim inspection.

| Existing case | Primary core concept | Secondary core concept | Proposed editorial relationship |
|---|---|---|---|
| [Netflix — Java platform convergence](../book/cases/netflix-java-platform-convergence.md) | [V03/C02](../book/execution/platform-threads-executors-and-virtual-threads.md) | [V08/C04](../book/delivery/gitops-canary-and-progressive-rollout.md) | Platform and runtime compatibility, staged adoption |
| [Netflix — Data Project identity](../book/cases/netflix-data-project-durable-workload-identity.md) | [V02/C07](../book/application/authorization-boundaries-and-multitenancy.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Durable ownership, authorization and transition |
| [Netflix — Zuul 2 nonblocking gateway](../book/cases/netflix-zuul2-nonblocking-gateway.md) | [V03/C03](../book/execution/reactor-webflux-r2dbc-and-backpressure.md) | [V07/C04](../book/performance/tail-latency-fanout-and-deadline-budgets.md) | Asynchronous demand, gateway/latency |
| [Netflix — DGS and Spring GraphQL](../book/cases/netflix-dgs-spring-graphql-convergence.md) | [V02/C05](../book/application/http-rpc-contracts-and-compatibility.md) | [V02/C06](../book/application/anti-corruption-adapters-and-coexistence.md) | Interface evolution, contract integration |
| [Netflix — Java 21 virtual-thread pinning](../book/cases/netflix-java21-virtual-thread-pinning.md) | [V03/C02](../book/execution/platform-threads-executors-and-virtual-threads.md) | [V03/C06](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | Thread behavior and runtime diagnosis |
| [Netflix — gRPC worker-pool regression](../book/cases/netflix-grpc-cpu-workerpool-virtual-thread-regression.md) | [V03/C01](../book/execution/threads-tasks-structured-coordination.md) | [V07/C02](../book/performance/contention-saturation-and-scaling-laws.md) | CPU work, resource contention, thread model |
| [Netflix — Generational ZGC workloads](../book/cases/netflix-generational-zgc-workloads.md) | [V03/C06](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | [V07/C04](../book/performance/tail-latency-fanout-and-deadline-budgets.md) | GC versus tail-latency workload fit |
| [Netflix — HotSpot sharing](../book/cases/netflix-hotspot-false-true-sharing.md) | [V07/C02](../book/performance/contention-saturation-and-scaling-laws.md) | [V03/C06](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | CPU contention, memory effects |
| [Netflix — Cloud rearchitecture](../book/cases/netflix-seven-year-cloud-rearchitecture.md) | [V10/C02](../book/decisions/legacy-baseline-and-modernization-evidence.md) | [V08/C06](../book/deployment/availability-zones-placement-and-failure-domains.md) | Longitudinal modernization and placement |
| [Netflix — Chaos Kong regional simulation](../book/cases/netflix-chaos-kong-regional-failover.md) | [V08/C07](../book/deployment/disaster-recovery-and-recovery-objectives.md) | [V09/C06](../book/observability/incident-response-and-operational-change.md) | Recovery, incident evidence |
| [Netflix — Casspactor shadow migration](../book/cases/netflix-casspactor-shadow-migration.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Shadow coexistence, migration gate |
| [Netflix — Cassandra time-series splits](../book/cases/netflix-cassandra-dynamic-time-series-splits.md) | [V05/C05](../book/scaling/shard-keys-hotspots-and-resharding.md) | [V07/C02](../book/performance/contention-saturation-and-scaling-laws.md) | Partitioning and hotspots |
| [Uber — DOMA](../book/cases/uber-doma-domains.md) | [V02/C02](../book/application/domain-boundaries-data-ownership-and-contracts.md) | [V02/C04](../book/application/service-orientation-microservices-and-distribution.md) | Domain ownership and service boundaries |
| [Uber — Mezzanine PostgreSQL migration](../book/cases/uber-mezzanine-pg-to-schemaless.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Data ownership transfer and compatibility |
| [Uber — MyRocks](../book/cases/uber-mysql-to-myrocks.md) | [V05/C04](../book/data/storage-model-alternatives-and-workload-fit.md) | [V05/C03](../book/data/postgresql-indexes-statistics-and-query-plans.md) | Engine choice and write/read trade-offs |
| [Uber — Cinnamon fairness](../book/cases/uber-cinnamon-admission-and-fairness.md) | [V07/C05](../book/performance/overload-admission-control-and-graceful-degradation.md) | [V07/C02](../book/performance/contention-saturation-and-scaling-laws.md) | Admission and overload conditions |
| [Shopify — Modular monolith](../book/cases/shopify-modular-monolith.md) | [V02/C03](../book/application/modular-monolith-and-internal-events.md) | [V02/C04](../book/application/service-orientation-microservices-and-distribution.md) | Monolith versus independently deployed services |
| [Shopify — Packwerk boundaries](../book/cases/shopify-packwerk-boundary-evolution.md) | [V02/C01](../book/application/layered-hexagonal-ports-and-adapters.md) | [V02/C03](../book/application/modular-monolith-and-internal-events.md) | Enforced module dependencies |
| [Shopify — Helix migration gates](../book/cases/shopify-helix-checkpoint-gated-native-migration.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | [V09/C07](../book/security/safe-agent-access-and-knowledge-isolation.md) | Modernization safety, AI claims and evidence |
| [Airbnb — Bazel JVM build migration](../book/cases/airbnb-jvm-monorepo-bazel.md) | [V08/C01](../book/delivery/ci-cd-provenance-and-gitops.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Build/release migration |
| [Stripe — Online subscriptions migration](../book/cases/stripe-online-subscriptions-migration.md) | [V08/C05](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | Online schema transition and compatibility |
| [Discord — Cassandra to ScyllaDB](../book/cases/discord-cassandra-scylladb-messages.md) | [V05/C04](../book/data/storage-model-alternatives-and-workload-fit.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Datastore transition and workload |
| [Discord — Search index cells](../book/cases/discord-search-index-cells.md) | [V06/C07](../book/search/retrieval-evaluation-and-index-lifecycle.md) | [V06/C03](../book/search/lexical-indexing-bm25-and-sql-fts.md) | Search index lifecycle and access paths |
| [Spotify — Long-tail platform migration](../book/cases/spotify-tech-migration-long-tail.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | [V10/C02](../book/decisions/legacy-baseline-and-modernization-evidence.md) | Legacy transition and residual callers |
| [Spotify — Honk data-consumer migration](../book/cases/spotify-honk-data-consumer-migration.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | [V08/C05](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | Versioned consumer state and cutover |
| [Cloudflare — Super Slurper queues](../book/cases/cloudflare-super-slurper-queues.md) | [V04/C06](../book/integration/messaging-families-and-durable-workflows.md) | [V07/C05](../book/performance/overload-admission-control-and-graceful-degradation.md) | Queue-backed work and overload |
| [Meta — TAO graph serving](../book/cases/meta-tao-social-graph-serving.md) | [V06/C06](../book/search/graph-data-models-and-traversal.md) | [V05/C04](../book/data/storage-model-alternatives-and-workload-fit.md) | Graph model as studied architecture, not Tycho graph infrastructure |
| [Meta — Ingestion shadow cutover](../book/cases/meta-ingestion-shadow-migration-lifecycle.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | Shadow verification and transition |
| [LinkedIn — Kafka tiers](../book/cases/linkedin-kafka-tiered-completeness.md) | [V04/C07](../book/integration/kafka-partitions-replication-and-contracts.md) | [V04/C08](../book/integration/stateful-stream-processing-and-cdc.md) | Kafka logs, processing state and completeness |

## Mapping six decision playbooks into the decision volume

These six pages are synthetic cross-case teaching guides. They supplement **V10's canonical decision method**, not replace its chapter owners.

| Existing draft playbook | Primary decision-method chapter | Specialized supporting chapter | Proposed reading route |
|---|---|---|---|
| [Monolith vs services](../book/cases/decisions/monolith-vs-services.md) | [V10/C03](../book/decisions/pattern-applicability-and-contraindications.md) | [V02/C04](../book/application/service-orientation-microservices-and-distribution.md) | Choice conditioned on service ownership and operating limits |
| [Reactive vs virtual threads](../book/cases/decisions/reactive-vs-virtual-threads.md) | [V10/C04](../book/decisions/architecture-alternatives-experiments-and-adrs.md) | [V03/C02](../book/execution/platform-threads-executors-and-virtual-threads.md) | Bounded execution-model comparison |
| [GC vs tail latency](../book/cases/decisions/gc-and-tail-latency.md) | [V10/C04](../book/decisions/architecture-alternatives-experiments-and-adrs.md) | [V03/C06](../book/execution/cpu-memory-gc-and-blocking-diagnostics.md) | Workload-conditional runtime decision |
| [Data migration correctness](../book/cases/decisions/data-migration-correctness.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | [V05/C06](../book/data/schema-lifecycle-and-semantic-migration.md) | Rollback/no-return and invariant-preserving migration |
| [Build and delivery migration](../book/cases/decisions/build-delivery-migration.md) | [V10/C05](../book/decisions/target-and-transition-architecture-states.md) | [V08/C01](../book/delivery/ci-cd-provenance-and-gitops.md) | Transition gates for build/platform changes |
| [Agent-assisted migration safety](../book/cases/decisions/agentic-migration-safety.md) | [V10/C07](../book/decisions/cross-domain-modernization-and-adr-examples.md) | [V09/C07](../book/security/safe-agent-access-and-knowledge-isolation.md) | Evidence, refusal and authorized automation boundaries |

## Verified integrated-branch mechanical QA — pinned snapshot

**Executed on the combined branch** after the Git merge and new book navigation, against Git tree `54bc35532419005becf6c8c32ef40f3a6fc03bec` (pre-QA-note commit). The Git tree was fetched recursively, contained **311 blobs**, and was **not truncated**.

- Re-fetched **all 35 M9 applied Markdown pages** in two batches (17 + 18) **from the merged branch**, checking duplicate exact H2 headings and paired fenced-code opening/closing boundaries. **35/35 passed those narrow structural checks**: no duplicate H2 headings and no odd fence counts detected. This does **not** render or syntax-validate Mermaid diagrams, and does not prove Markdown parser behavior, external URL access or source correctness.
- Counted the applied corpus in the merged Git tree: **29 case-study files** (excluding the casebook README) and **six decision-guide files**; all were present.
- Parsed *relative Markdown file links* in the [unified map](UNIFIED_BOOK_M1_M9_INTEGRATION.md), [main book README](../book/README.md), [casebook README](../book/cases/README.md) and [decision README](../book/decisions/README.md): **190/190 local file-link occurrences had existing target files** in this pinned Git tree; includes **109/109** integration-map references. Crosswalk contains **35 applied-page rows**, one per M9 case/guide. This is not anchor-fragment validation or claim-to-source verification.
- Direct Git history verified two merge parents; comparison against core parent returned **exactly 41 M9 path changes**, matching PR #212, and comparison against main returned **108 path changes** at the merge checkpoint before integration-only docs. No main commits were missing at that checkpoint.
- **No local `python` premerge/boundary/schema/M9 suite, rendered diagram, actual MCP evaluation, copyright clearance or independent human review was executed** in this QA. Do not translate these structural checks into any of the still-open acceptance gates.

## Continued source-review and whole-book structural checkpoint

The integrated manuscript has an additional [whole-book static scan](INTEGRATED_BOOK_STATIC_CHECKPOINT_2026-10-19.md) at pinned Git revision `ff88fe334050c6e429941cb514bdd02150fa6be2`: **136 of 136 book Markdown pages fetched**, **1,623 total Markdown link occurrences examined** for local file targets (none missing), exactly one H1 per file, and no odd triple-backtick fence counts. These are narrower GitHub-file/lexical checks, **not** a local Python premerge suite, complete anchor validation or source/diagram correctness review.

A new [Shopify first-party source comparison](cases/M9_SHOPIFY_SOURCE_SPOTCHECK_2026-10-19.md) evaluates **12 specific SH01 (2019) and SH02 (2020) historical assertions** across the modular-monolith and Packwerk cases. This found and corrected an overstatement implying full 2019 domain-boundary enforcement. Publisher-windowed facts (including ~6,000 Ruby classes in 2019 and 37 components / approximately one-third Packwerk adoption in 2020) were distinguished from Tycho's proposed architecture-transfer guidance. This source spot-check **does not count as independent copyright or technical acceptance**, and none of the 60 graph-free MCP evaluation fixtures ran.

Both core [#213](https://github.com/rouslanbaranov/tycho/issues/213) and M9 [#121](https://github.com/rouslanbaranov/tycho/issues/121) remain **OPEN**; the 69 core editorial statuses and 35 applied document statuses remain pending independent decisions.

## Integration and acceptance matrix — separate states

| Gate | Core M1–M8 and #213 | M9 and #121 | Combined branch / publication disposition |
|---|---|---|---|
| Files/corpus present | **69/69 unique primary Markdown files fetched** in core branch | **29/29 cases and 6/6 playbooks depth-pass**, 35 case docs, unchanged acceptance | Both history and content present in combined Git tree; **not accepted** |
| Case/doc H2/fence structure | Existing partial Markdown checks, not complete full-tree lint | 29 cases with no duplicated H2/unclosed fences, and 35 page structural checks reported in #212 | Re-run check on pinned **combined SHA**; no new generated claims |
| Provenance/reuse and rights | Claim spot-check 11 narrow points in seven chapter owners; whole corpus pending | Selected first-party reviews; all 35 pages still await independent technical/copyright review | **BLOCKED** for publication; retain publisher windows, exact revision and licenses |
| Source-to-owner and cross-links | 69 distinct primary targets; preserved older research | Stable case IDs and 35 original drafts | Crosswalk exists; verify 35 article ↔ 69 chapter routes and all anchors in a real checkout |
| Python validation | Full premerge/boundary/schema/editorial suite not run on combined branch | Full pinned local M9 scripts not executed | **BLOCKED**; run existing checks and record exact SHA/commands/output |
| Search/MCP 60-case evaluation | Hosted read-only MCP/search not implemented; book-first content priority | 60 specification queries (21 answerable, 26 false-claim rejections, 13 insufficient evidence), not integrated MCP results | **DEPENDENCY BLOCKED**; run real graph-free service after readiness, or obtain explicitly authorized formal dependency disposition. **Do not invent waiver or claim offline BM25 is MCP validation.** |
| Independent review | 69 owner drafts still PENDING | #121 open, M9 independent review incomplete | Separate reviewers/acceptance for 69 chapter owners + 35 applied pages, followed by integrated cross-chapter consistency review |
| Edition/release | #214 awaits #213 | M9 stays open until gates pass | **No final 10-volume/page publication or main merge** yet |

### Actual Git merge procedure and preservation guarantees

- PR #215 is up-to-date with `main` at `65ba643d1cab4a65eef148279c0d9adf84e5b2d9`; M9 branch PR #212 was **behind main by two commits**. The main additions are already present through core.
- PR file sets checked: **67 core file changes and 41 M9 file changes with zero overlapping paths**. All 41 modified M9 files were fetched at the **exact frozen PR #212 head**, then their Git blob SHA objects were overlaid onto the core head's tree. No shared content path was silently overwritten.
- A true two-parent Git merge commit `b710276de313ef9bd1c26a096a6e8583c9acf3ec` has parents `baaede8...` and `af83315...`. Its tree is `6baadce5446fe38681e0aae50e8024afb354a006`.
- Git comparison after branch update showed **41/41 M9 file changes relative to the core parent**, and **108 changed files relative to main**, with no behind-main commits at this snapshot. The audit is of tracked Git files/history, not semantic merge quality, source correctness or review.
- The integration-specific navigation and review files added after the merge are separate commits. If either source PR moves again, compare its new head and bring changes forward via another explicit reviewed integration commit, never overwrite the other branch or mark review complete by assumption.

### Remaining next steps

1. Perform content-level cross-links into canonical subject chapters only where evidence is genuinely relevant; this file supplies bounded, readable routing without a graph.
2. Run the existing full Python suites against a pinned local combined checkout; record exact output, negative cases and dependency issues, with milestone-only CI unchanged.
3. Independently accept **all** source-specific/company-specific case and rights claims and each core technical chapter; preserve counterexamples, historical shifts, original diagrams and uncertainty.
4. Reconcile inherited M9 metadata/provenance templates with book-first metadata without requiring a second knowledge graph or MCP server.
5. Only when both #121 and #213 are truly accepted, assemble and release the coherent ten-volume edition through #214. Evaluate future graph-free search/MCP according to its real dependency/readiness or a valid authorized disposition.

**Nonclaims:** no human sign-off, code/Python validation on combined branch, real search/MCP evaluation, legal clearance or edition publication has occurred by adding this crosswalk or combining Git histories.
