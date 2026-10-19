# Tycho — canonical chapter ownership and overlap remediation

**Status:** source-specific editorial desk review, 2026-10-19.  
**Purpose:** prevent a 69-row topical crosswalk from being mistaken for 69 **distinct, complete chapters**. This is an actionable content/ownership review for [Issue #213](https://github.com/rouslanbaranov/tycho/issues/213), and the input to the eventual ten-volume, 69-chapter publication conversion [#214](https://github.com/rouslanbaranov/tycho/issues/214).

## Verified scope and counts

At the **initial overlap audit**, the 69-row topic audit mapped to **60 distinct primary Markdown target paths**. **Eight files** were assigned to more than one canonical chapter, accounting for **17 chapter-owner assignments** and **nine duplicate-target assignments** beyond the 60 unique paths. **After the complete V02/V04/V05/V06/V08/V09 main-chapter draft separation, the latest crosswalk maps 69 chapter questions to 69 unique primary files; all 69/69 primary files were re-fetched successfully and eight original shared-article ownership conflicts are resolved at primary-file/path level. No chapter is independently accepted.**

These counts were derived from [the branch coverage audit](BOOK_COMPLETENESS_AUDIT.md) and checked against the headings and approximate word counts of **all eight shared manuscript files** through the GitHub branch file API. The original 60-target baseline and latest 69-target crosswalk are **not** an exhaustive Git-tree inventory; the crosswalk may omit adjacent, older or supplemental manuscript content. No final chapter landing, chapter/page metadata, semantic correctness review or rendered book edition is certified by this count.

**Key distinction:** One researched article can legitimately answer several chapter questions at a shallow level. This is useful draft coverage but **not** evidence that all intended owner chapters exist as coherent independent reading units. Conversely, blindly copying one research page into two chapters creates duplicated explanations that quickly diverge.

## Latest reconciliation and verification checkpoint — 2026-10-19

**Result: 69 unique primary Markdown targets for 69 proposed chapter owners; eight initial shared-primary-file groups all separated.** An unchanged older combined source can still share *mechanisms* with a new chapter; that duplication and the original evidence claims still require editorial comparison. The earlier 60 → 61 → 62 counts in historical sections below must be read as successive checkpoints, not as current status.

| Original shared-research group | New primary chapter owners and distinct files | File-owner separation | Claim-by-claim evidence review |
|---|---|---|---|
| Application styles | [V02/C01 layered/hexagonal](../book/application/layered-hexagonal-ports-and-adapters.md), [V02/C04 service orientation](../book/application/service-orientation-microservices-and-distribution.md) | Complete | **Pending** |
| Outbox and idempotency | [V04/C04 retries and ambiguous effects](../book/distributed/retries-idempotency-and-ambiguous-effects.md), [V04/C05 outbox/inbox/saga/workflows](../book/distributed/outbox-inbox-sagas-and-durable-workflows.md) | Complete | **Pending** |
| PostgreSQL MVCC and planning | [V05/C01 relational/isolation](../book/data/relational-modeling-and-transaction-isolation.md), [V05/C03 indexing/plans](../book/data/postgresql-indexes-statistics-and-query-plans.md) | Complete | **Pending** |
| Schema and rollout | [V05/C06 data lifecycle](../book/data/schema-lifecycle-and-semantic-migration.md), [V08/C04 progressive rollout](../book/delivery/gitops-canary-and-progressive-rollout.md), [V08/C05 DB compatibility](../book/delivery/mixed-version-database-compatibility-and-online-ddl.md) | Complete | **Pending** |
| Caching | [V06/C01 placement/freshness](../book/scaling/local-and-distributed-cache-design.md), [V06/C02 stampede/invalidation](../book/scaling/cache-invalidation-stampede-and-hot-keys.md) | Complete | **Pending** |
| HA and DR | [V08/C06 availability placement](../book/deployment/availability-zones-placement-and-failure-domains.md), [V08/C07 disaster recovery](../book/deployment/disaster-recovery-and-recovery-objectives.md) | Complete | **Pending** |
| SLI/SLO and metrics storage | [V09/C01 SLO decision](../book/observability/service-level-indicators-objectives-and-alerts.md), [V09/C02 telemetry pipeline](../book/observability/metric-pipelines-cardinality-and-retention.md) | Complete | **Pending** |
| Tracing versus audit | [V09/C03 tracing](../book/observability/distributed-tracing-context-and-sampling.md), [V09/C04 log/audit/lineage](../book/observability/logs-audit-and-data-lineage.md) | Complete | **Pending** |

**Actual verification:** the 69-row matrix had 69 distinct Vxx/Cxx IDs and 69 primary file paths with no duplicates, and **all 69 files existed on the feature branch** when individually fetched. The 13 most recently added shared-owner drafts were re-fetched and **44/44 unique locally referenced Markdown target files existed** on that branch. Read [the independent 69-row editorial acceptance ledger](CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md) for per-chapter file sizes and pending review status. An external check of selected OASIS, PostgreSQL, Kubernetes, public saga/consumer and AWS recovery documentation supported *narrow referenced mechanism descriptions*, not a comprehensive source provenance audit.

**Not established:** full Git-tree inventory, proof that every prior research claim survived migration, exact external citation stability, link fragments, required per-question depth, runtime/diagram tests, copyright admission per source, final book metadata, complete local CI or publication approval. All chapter content review states remain **pending**. Source research articles are **retained**; avoid deleting or silently retiring them until evidence reconciliation completes.

## Eight historically overlapping manuscript groups — all primary-file assignments separated; source claims not yet reconciled

| Shared current article | Intended owners | Main existing conceptual sections | Required canonicalization |
|---|---|---|---|
| [Progressive delivery and schema evolution](../book/delivery/progressive-delivery-and-schema-evolution.md) (~1,769 words) | **V05/C06**, **V08/C04**, **V08/C05** | Rolling/blue-green/canary, N/N+1 matrix, expand/migrate/contract, online DDL | **Three separate owner chapters.** V05/C06 owns data/schema lifecycle and semantic migration; V08/C04 owns GitOps, rollout modes, canary/blue-green and traffic-safety controls; V08/C05 owns mixed-version storage compatibility, online DDL and rollback/no-return. Cross-link rather than duplicate mechanics; test which source version supports each claim |
| [Application styles and module boundaries](../book/application/architecture-styles-and-module-boundaries.md) (~2,556 words) | **V02/C01**, **V02/C04** | DDD/domain vs code/deployment axes, monolith, hexagonal ports/adapters, SOA vs microservices | V02/C01 owns layered/hexagonal and dependency direction; V02/C04 owns service-orientation and microservice selection/failure costs. Link to newly independent V02/C02 domain ownership and V02/C03 modular monolith rather than reproduce them |
| [Outbox and idempotent external effects](../book/distributed/transactional-outbox-and-idempotency.md) (~2,328 words) | **V04/C04**, **V04/C05** | Retry/effect identity, outbox atomicity boundary, replay, durable publication, inbox/saga pointers | V04/C04 owns client/request/consumer effect identity and duplicate/unknown acknowledgments; V04/C05 owns outbox/inbox/workflow mechanics and coordinating state transitions. Preserve the precise commit/publication failure matrix with a single canonical owner and cross-link |
| [PostgreSQL MVCC and query plans](../book/data/postgresql-mvcc-indexes-and-query-plans.md) (~1,742 words) | **V05/C01**, **V05/C03** | Relational constraints/MVCC visibility/isolation, indexes, query planner and EXPLAIN estimates | V05/C01 owns relational correctness, data model and snapshot isolation; V05/C03 owns indexing, statistics, query planning and access-path trade-offs. Do not equate cost estimate with measured latency; review PostgreSQL version-scoped evidence |
| [Local and distributed caching](../book/scaling/local-distributed-caching-and-invalidation.md) (~1,752 words) | **V06/C01**, **V06/C02** | Authority/freshness, local/distributed cache, invalidation races, stampede/hot keys | V06/C01 owns local/distributed cache design and freshness models; V06/C02 owns cache-stampede, hot-key, invalidation and overload failure mechanics. Retain one owner per exact race and link from the other chapter |
| [Multi-zone and multi-region recovery](../book/deployment/multi-region-disaster-recovery-contracts.md) (~1,912 words) | **V08/C06**, **V08/C07** | Placement/failure domains, RTO/RPO, active/active conflict, drills and data reconciliation | V08/C06 owns deployment/failure-domain placement and resilient topology; V08/C07 owns disaster-recovery plans, measured RTO/RPO, fencing and restore validation. Refer to V05/C07 for PostgreSQL backup/PITR mechanisms rather than restating DB-specific steps |
| [Metrics, SLOs and TSDBs](../book/observability/metrics-slo-timeseries-architecture.md) (~1,601 words) | **V09/C01**, **V09/C02** | Indicators/SLO, collection pipeline, temporal metrics, cardinality, storage/retention and alerting | **Draft owner split implemented:** [V09/C01 SLI/SLO/error budgets](../book/observability/service-level-indicators-objectives-and-alerts.md) and [V09/C02 metric ingestion/cardinality/retention](../book/observability/metric-pipelines-cardinality-and-retention.md) now have distinct substantive primary article targets. Existing combined source retained for claim reconciliation. Neither new owner has independent editorial sign-off |
| [Tracing, logs, lineage and audit](../book/observability/trace-context-lineage-and-audit.md) (~1,767 words) | **V09/C03**, **V09/C04** | W3C trace propagation, async links, sampling, log contracts, OpenLineage and audit records | V09/C03 owns distributed tracing/context propagation/sampling; V09/C04 owns logs, authoritative audit, data lineage and integrity/retention. Critical distinction: sampled traces cannot serve as authoritative business audit |

## Progress since baseline — first two owners separated

On 2026-10-19, two original focused manuscript chapters were authored and linked under their own reader questions:

- **V09/C01:** [Service-level indicators, objectives and error-budget decisions](../book/observability/service-level-indicators-objectives-and-alerts.md), approximately 1,475 whitespace-separated Markdown words and one original Mermaid diagram. Owned subject: eligible user outcomes and denominators, SLO, error budgets, burn/alert interpretation and hard correctness constraints.
- **V09/C02:** [Metrics ingestion, cardinality and retention](../book/observability/metric-pipelines-cardinality-and-retention.md), approximately 1,548 words and one diagram. Owned subject: metric temporality and aggregation, counters/gauges/histograms, telemetry loss, TSDB cardinality, retention and costs.
- Prior combined research page [metrics/SLOs/TSDB](../book/observability/metrics-slo-timeseries-architecture.md) is preserved as a historical research input, **not** copied wholesale or removed. The [observability landing](../book/observability/README.md) now directs readers to the two separate manuscript owners.
- Both files were re-fetched from the feature branch and all **nine distinct local target file paths** extracted from their Markdown were fetched successfully (**9/9 exist**). External link permanence, Markdown anchor fragments, rendered Mermaid, exact claims, independently admissible revision provenance, semantic completeness and acceptance were **not tested**.
- Recomputed against the updated 69-row branch matrix: **61 unique primary targets; seven remaining shared legacy source files assigned to 15 planned owners; eight duplicate-owner assignments.** The eight groups in the table remain the historical baseline; two have now been resolved only at source-file ownership level, without semantic acceptance.

**This is an editorial ownership improvement, not a new volume/chapter/page edition, final content acceptance, or a semantic source-to-claim review.**

## Second owner separation — trace versus authoritative audit

The former single [trace/log/audit/lineage page](../book/observability/trace-context-lineage-and-audit.md) is now referenced by two independent main manuscript paths:

- **V09/C03:** [Distributed tracing, context propagation and sampling](../book/observability/distributed-tracing-context-and-sampling.md). Owns W3C traceparent/tracestate, trace-span relationship and links, sampling bias, trusted propagation and version scope. Does not claim trace completeness or an actual traced service.
- **V09/C04:** [Structured logging, authoritative audit and data lineage](../book/observability/logs-audit-and-data-lineage.md). Owns diagnostic logs versus committed business-audit effects, OpenTelemetry log semantics, OpenLineage job/run/dataset identity, integrity/access/retention and failure cases. Does not claim a running audit or a lineage system.
- The original common article is **not deleted**; it remains a source candidate for verifying that technical interpretations and citations were preserved. These are two unreviewed original independent chapters, not approved publication pages.

At the time of the second separation, the crosswalk had **62 distinct primary article paths** and six remaining shared groups. **Historical snapshot only:** the latest confirmed crosswalk is 69/69 unique primary targets. No claim of a complete Git-tree inventory or source-to-claim review is made.

## Canonical publication rule

1. **One stable chapter owner** per planned Vxx/Cxx question. A chapter must answer its title's complete question; merely linking to a paragraph is not sufficient for substantive acceptance.
2. **One owner per detailed technical mechanism**. Other chapters should introduce necessary context and link to its canonical page with exact applicability and limitation; avoid copying definitions/tables and creating contradictory versions.
3. **Content preservation by mapping.** The old topic article remains available in the branch until its sentences/figures/source claims have been remapped or verified redundant. Record old section → new chapter/page mapping before replacing or deleting anything.
4. **Depth expansion where missing.** Many of the eight shared pages are only 1,600–2,500 English words spread over two or three proposed chapters. Splitting them is **not content completion**; each destination may need research, original diagrams, negative examples, specific source links and chapter-level synthesis.
5. **Evidence and limitations carry with the claim.** Do not silently move a citation into a new chapter if its exact source section no longer supports the claim. Preserve version, source publisher and a tested/non-tested classification.
6. **Reader contract:** Volume purpose/mission → chapter question/criteria → bounded pages → synthesis, alternative/contraindication, failure/recovery and next reading. Chapter navigation is not proof of technical validation.
7. **Source independence:** only public independently admissible material and new synthetic examples; use generic methods from other projects, never import another book's implementation/content/schema wholesale.
8. **No graph-infrastructure expansion:** graph data modeling appears only as V06/C06 educational subject; no manually curated Tycho concept graph or worker/scheduler work.
9. **No premature merge/close:** each chapter requires an explicit completed content/evidence/editorial checklist before issue #213 can be accepted; structural edition #214 follows that checkpoint.

## Acceptance review per owner

Use an auditable chapter review card with:

| Check | Evidence to record | Failure state |
|---|---|---|
| Planned owner | Vxx/Cxx, volume mission, canonical source page(s) and exact reader question | Duplicate or missing canonical owner |
| Substantive coverage | Full set of question's mechanisms, criteria, normal + failure + recovery paths where material | One or more only mentioned in passing |
| Public source admission | Original independently published URL/revision, access date, exact section, claim mapping | Unreviewed/unverifiable or ineligible source |
| Distinctions | Observed fact vs published documentation vs original inference vs unknown | Synthetic example represented as measured behavior |
| Decision usefulness | Applicability, contraindications, alternatives, experiment/revisit | Prescriptive choice without requirements |
| Structural quality | Page bounds, unique IDs/frontmatter, stable links/anchors and reader navigation | Empty index, broken link or only a table |
| Originality/security | Scope neutrality, safe examples, boundary checks and human origin review | Contaminated or unauthorized material |
| Review outcome | Reviewer/date/checks run, accepted or unresolved specific reason | Automatic acceptance inferred from issue/PR count |

**No owner in the initial eight overlap groups is declared accepted by this report.**

## Sequence for the publication pipeline

A. Verify the repository-wide source/page census and source revisions; reconcile unexpected extra pages.  
B. **All eight groups now have separate primary chapter drafts.** Perform line/claim/source mapping from each preserved shared research article to its independently owned destination chapters; deepen or correct any missing content, without deleting originals prematurely.  
C. Apply the same depth/evidence/independence gates to **all 69 planned chapter questions** and track real acceptance in the [chapter editorial acceptance ledger](CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md).  
D. Rebuild or validate strict frontmatter/schema and the deterministic page routing index against canonical volume/chapter/page IDs, with complete link/anchor checks.  
E. After content acceptance, create final 10-volume, 69-chapter first edition and bounded child pages under #214, with a reproducible inventory and source ledger; optionally render additional publication formats only when separately authorized.

## Explicit limitations

No full repository checkout, Git-tree inventory, automated boundary/premerge check, source-by-claim approval, Mermaid rendering, independent research assessment, or final edition was produced in this specific review. The inspected shared articles and latest 69 unique destination paths document **resolved primary-file ownership only**; the unresolved blocker is complete *content/evidence/quality acceptance*, not merely duplicate file paths.
