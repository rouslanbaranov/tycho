# Tycho — canonical chapter ownership and overlap remediation

**Status:** source-specific editorial desk review, 2026-10-19.  
**Purpose:** prevent a 69-row topical crosswalk from being mistaken for 69 **distinct, complete chapters**. This is an actionable content/ownership review for [Issue #213](https://github.com/rouslanbaranov/tycho/issues/213), and the input to the eventual ten-volume, 69-chapter publication conversion [#214](https://github.com/rouslanbaranov/tycho/issues/214).

## Verified scope and counts

The 69-row topic audit currently maps to **60 distinct primary Markdown target paths**. **Eight files** are assigned to more than one canonical chapter, accounting for **17 chapter-owner assignments** and **nine duplicate-target assignments** beyond the 60 unique paths.

These counts were derived from [the branch coverage audit](BOOK_COMPLETENESS_AUDIT.md) and checked against the headings and approximate word counts of **all eight shared manuscript files** through the GitHub branch file API. The 60 files are **not** an exhaustive Git-tree inventory; the crosswalk may omit adjacent, older or supplemental manuscript content. No final chapter landing, chapter/page metadata, semantic correctness review or rendered book edition is certified by this count.

**Key distinction:** One researched article can legitimately answer several chapter questions at a shallow level. This is useful draft coverage but **not** evidence that all intended owner chapters exist as coherent independent reading units. Conversely, blindly copying one research page into two chapters creates duplicated explanations that quickly diverge.

## Eight confirmed overlapping manuscript ownership groups

| Shared current article | Intended owners | Main existing conceptual sections | Required canonicalization |
|---|---|---|---|
| [Progressive delivery and schema evolution](../book/delivery/progressive-delivery-and-schema-evolution.md) (~1,769 words) | **V05/C06**, **V08/C04**, **V08/C05** | Rolling/blue-green/canary, N/N+1 matrix, expand/migrate/contract, online DDL | **Three separate owner chapters.** V05/C06 owns data/schema lifecycle and semantic migration; V08/C04 owns GitOps, rollout modes, canary/blue-green and traffic-safety controls; V08/C05 owns mixed-version storage compatibility, online DDL and rollback/no-return. Cross-link rather than duplicate mechanics; test which source version supports each claim |
| [Application styles and module boundaries](../book/application/architecture-styles-and-module-boundaries.md) (~2,556 words) | **V02/C01**, **V02/C04** | DDD/domain vs code/deployment axes, monolith, hexagonal ports/adapters, SOA vs microservices | V02/C01 owns layered/hexagonal and dependency direction; V02/C04 owns service-orientation and microservice selection/failure costs. Link to newly independent V02/C02 domain ownership and V02/C03 modular monolith rather than reproduce them |
| [Outbox and idempotent external effects](../book/distributed/transactional-outbox-and-idempotency.md) (~2,328 words) | **V04/C04**, **V04/C05** | Retry/effect identity, outbox atomicity boundary, replay, durable publication, inbox/saga pointers | V04/C04 owns client/request/consumer effect identity and duplicate/unknown acknowledgments; V04/C05 owns outbox/inbox/workflow mechanics and coordinating state transitions. Preserve the precise commit/publication failure matrix with a single canonical owner and cross-link |
| [PostgreSQL MVCC and query plans](../book/data/postgresql-mvcc-indexes-and-query-plans.md) (~1,742 words) | **V05/C01**, **V05/C03** | Relational constraints/MVCC visibility/isolation, indexes, query planner and EXPLAIN estimates | V05/C01 owns relational correctness, data model and snapshot isolation; V05/C03 owns indexing, statistics, query planning and access-path trade-offs. Do not equate cost estimate with measured latency; review PostgreSQL version-scoped evidence |
| [Local and distributed caching](../book/scaling/local-distributed-caching-and-invalidation.md) (~1,752 words) | **V06/C01**, **V06/C02** | Authority/freshness, local/distributed cache, invalidation races, stampede/hot keys | V06/C01 owns local/distributed cache design and freshness models; V06/C02 owns cache-stampede, hot-key, invalidation and overload failure mechanics. Retain one owner per exact race and link from the other chapter |
| [Multi-zone and multi-region recovery](../book/deployment/multi-region-disaster-recovery-contracts.md) (~1,912 words) | **V08/C06**, **V08/C07** | Placement/failure domains, RTO/RPO, active/active conflict, drills and data reconciliation | V08/C06 owns deployment/failure-domain placement and resilient topology; V08/C07 owns disaster-recovery plans, measured RTO/RPO, fencing and restore validation. Refer to V05/C07 for PostgreSQL backup/PITR mechanisms rather than restating DB-specific steps |
| [Metrics, SLOs and TSDBs](../book/observability/metrics-slo-timeseries-architecture.md) (~1,601 words) | **V09/C01**, **V09/C02** | Indicators/SLO, collection pipeline, temporal metrics, cardinality, storage/retention and alerting | V09/C01 owns user-level metrics, SLO and alert semantics; V09/C02 owns observability pipeline, cardinality, TSDB/retention and cost. This original page may be a research seed, but *neither* owner has a separate complete stand-alone chapter yet |
| [Tracing, logs, lineage and audit](../book/observability/trace-context-lineage-and-audit.md) (~1,767 words) | **V09/C03**, **V09/C04** | W3C trace propagation, async links, sampling, log contracts, OpenLineage and audit records | V09/C03 owns distributed tracing/context propagation/sampling; V09/C04 owns logs, authoritative audit, data lineage and integrity/retention. Critical distinction: sampled traces cannot serve as authoritative business audit |

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

**No owner in the eight overlap groups is declared accepted by this report.**

## Sequence for the publication pipeline

A. Verify the repository-wide source/page census and source revisions; reconcile unexpected extra pages.  
B. Deeply review eight overlap groups and author/adjust specific destination prose so each of the **17 affected chapters** answers its independent question without replicated mechanisms.  
C. Apply the same depth/evidence gates to the remaining 52 chapter questions, not just to these overlaps.  
D. Rebuild or validate strict frontmatter/schema and the deterministic page routing index against canonical volume/chapter/page IDs, with complete link/anchor checks.  
E. After content acceptance, create final 10-volume, 69-chapter first edition and bounded child pages under #214, with a reproducible inventory and source ledger; optionally render additional publication formats only when separately authorized.

## Explicit limitations

No full repository checkout, Git-tree inventory, automated boundary/premerge check, source-by-claim approval, Mermaid rendering, independent research assessment, or final edition was produced in this specific review. The inspected eight article headings and shared path assignments provide a **concrete duplication/ownership blocker**, not a release certificate.
