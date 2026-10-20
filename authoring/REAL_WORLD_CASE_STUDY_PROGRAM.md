# Real-World Modernization Case Study Program (M9)

## Binding 2026-10-19 decision: full case-page coverage, no product knowledge graphs

**Primary delivery priority:** finish the substantive content of **every one of the 29 M9 case pages and six comparative decision pages** against the case-study authoring contract. Count completeness by independently checkable question/evidence coverage per page, not by pages present, word count, diagram count, closed authoring issues or source-discovery totals. A missing publisher detail is documented as **unknown** rather than filled with an invented answer. No case is declared 100% content-complete until its own before/decision/alternatives/transition/failures/outcomes/transfer/provenance checks pass; independent approval is a separate gate. The 29 existing pages remain drafts until verified.

**Graph work is STOPPED for M9**, consistently with [Tycho's accepted graph-retirement ADR](ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md). Do not implement, improve, validate, wire, version, serve, operate, or maintain a curated case graph, graph schema, graph shards, graph traversal, case-to-pattern graph edge pipeline, or graph-dependent MCP/search contracts. Explicit Markdown cross-links, stable IDs, frontmatter/indexable fields, claim-to-source provenance, ranked retrieval and bounded MCP evidence reads are the supported alternatives. This policy applies to both new M9 work and unfinished historical graph language below; the historical text is not authorization to resume graph work. Graph databases, GraphQL schemas, organization-reported relationship systems and native Mermaid illustrations can still be subjects of technical prose: they are not Tycho product graph infrastructure.

## Current execution state — 2026-10-19

**Latest 2026-10-19 draft PR #212 checkpoint:** substantive case-depth work now covers **29/29 case pages** and **6/6 decision guides**. This is complete *authoring-wave coverage*, **not 35 independently accepted documents**. GitHub-tree checks inspected stable case identities, balanced Mermaid fences, H2 duplicates and relative Markdown file targets; the reviewer, full pinned local validation, source-by-source semantic/license audit and real integrated MCP evaluation remain outstanding. See [latest matrix](cases/M9_REVIEW_ACCEPTANCE_MATRIX.md). Graph support remains fully retired. M9 and #121 must remain OPEN.

 (supersedes the historical start-readiness snapshot below)

**M9 remains OPEN**. GitHub source intake **#114** and authoring/draft contract deliverables **#115–#120** are closed, but these are writing and source-disposition checkpoints, not independent case acceptance. There are **29 source-bounded *draft* case pages** (12 Netflix, 17 across nine other organizations), **6 analytical decision playbooks**, **43 source dispositions** (41 bounded/scope-only and 2 deferred technical bodies, src.m9-n14/src.m9-st02), and **60 public-only answer/refusal/evidence fixtures** (21 answerable; 26 reject_false_claim; 13 insufficient_evidence). The M9 Epic #113 and independent acceptance issue [#121](https://github.com/rouslanbaranov/tycho/issues/121) remain open.

**Executed technical tests:** GitHub-tree/static link and case-ID checks; real Draft 2020-12 schema validation of **two manually transferred example records** (both valid, 10 corrupted variants rejected) with local Python/jsonschema; and a **29-document, 60-query offline lexical BM25 candidate-ranking diagnostic**. Its full-corpus candidate Hit@1 is **48/57 (84.2%)**, Hit@3 **55/57 (96.5%)**, with **89.6%** of all expected case IDs in top three. See [reproducibility/evidence](cases/M9_DRAFT202012_SAMPLE_VALIDATION_2026-10-19.md) and [offline baseline](cases/M9_BM25_CANDIDATE_BASELINE_2026-10-19.md). The BM25 result **does not** certify final AI answers, citation fidelity, production K18–K23 retrieval/MCP integration, semantic search or an independently reviewed gold set.

**Outstanding acceptance gates:** Independent human/authorized external technical review of historical claims, metrics, copyright reuse and contraindications; genuine repository-checkout execution of `scripts/validate_m9_cases.py` and `scripts/evaluate_m9_case_bm25.py` with pinned SHA/outputs; and real MCP/lexical/hybrid evaluation if owning core infrastructure is available, otherwise an **explicit authorized dependency disposition**, not an invented benchmark. Issue #121 was reopened after premature closure, and must not close without recorded evidence. No Scheduled Tasks are used for this execution.

The original `Status: planned` and `Start-readiness checkpoint` paragraphs below are **historical baseline statements dated 2026-10-19**, not today's delivery status.


**Status:** planned; initial 43-source discovery set and detailed Netflix dossier researched, **zero accepted case-study chapters**. Prepared 2026-10-19. This is an independent Tycho content wave, not a change to the autonomous E14 authoring run and not authorization to regenerate or re-enrich existing chapters.

## Why

The existing conceptual System Design corpus teaches architecture principles. Real enterprise modernization reports reveal **why choices changed over time**, what failed, what alternatives were considered, how an operational migration worked and which improvements were measured. A second evidence type—company-reported practice—will make Tycho's architecture decision guidance richer without turning any famous company's stack into a universal recommendation.

Focus: Netflix's changing Java/JVM, Spring Boot, RxJava, gRPC/GraphQL, Zuul, ZGC, virtual threads, data/platform migration and rollback lessons. Contrast with Uber, Shopify, Airbnb, Spotify, Stripe, Discord, Meta, LinkedIn and Cloudflare so readers see incompatible but defensible choices.

## Separation of work and independence

- All sources are public third-party practitioner articles, talks, repository docs and company reports. No employer/private-system content, sanitized reconstructions or sources from other collections.
- Tycho remains independently understandable; Rocinante is the one shared specialist; future Tycho MCP exposes evidence-bound case search, not a dedicated agent.
- This work **adds canonical case-specific pages and an indexed case layer**; existing foundational technical pages remain canonical for concepts. Cross-link, do not copy technical sections.
- Conduct research in bounded case slices using [case template](../templates/real-world-modernization-case.md), [source register](../sources/REAL_WORLD_ARCHITECTURE_CASES.md), and [Netflix dossier](../sources/NETFLIX_MODERNIZATION_DOSSIER.md).
- Public availability does not grant reproduction rights. Record access/copyright/reuse conditions; link source material, paraphrase with attribution; produce original diagrams and examples.
- Company measurements and promises must be explicitly identified as reported and observation-window-specific.
- Protect the current autonomous E14 run: this program uses its own feature branches and own file namespace (`book/cases/`, `authoring/cases/`, source case registers). Do not merge, rebase or edit concurrent E14 chapters implicitly. Concurrency/merge conflicts are resolved in later integration review.
- No extra GitHub Actions triggers: honor milestone-close-only CI and local premerge checks; never close M9 just to trigger CI while open work remains.

## GitHub milestone

**M9 — Real-World Architecture Modernization: Case Studies and Decision Transfer**

Created [native M9](https://github.com/rouslanbaranov/tycho/milestone/9) on 2026-10-19, separate from existing M1–M8 and E14/M8. Epic #113 and all nine tasks #114–#122 are assigned; no due date asserted. Its acceptance scope is evidence-backed case publication, comparative reasoning, evaluated retrieval readiness and traceable work, **not** deployment of MCP/semantic search (already owned by existing epics).

Gate M9-A (research intake): source links live, corporate authorship or speaker verified, rights noted, historical versions and source sections identified, contradictions recorded. Initial discovery register is only a candidate list.

Gate M9-B (Netflix depth): at least eight bounded, fully evidence-backed and cross-linked cases from the dossier, covering both successful and failed/rolled-back choices: legacy-to-cloud, framework and JDK fleet upgrades, Zuul/reactive evolution, VT locking, GC, DGS integration, data migration and workflow/operational transitions. Ensure 2023 vs 2026 versions are not combined.

Gate M9-C (cross-company breadth): at least twelve additional accepted cases across at least six companies, with contrasting modular monolith/microservices, zero-downtime database migration, CI/CD/build modernization, data partitioning, security/identity and service resilience. Prioritize **decision diversity**, not company popularity.

Gate M9-D (analytical transfer): at least six cross-company comparison/decision pages, explicit requirements/workload/legacy constraints, alternatives, contraindications, transition architecture and 'insufficient evidence' cases. Evidence-backed ADR examples use original hypothetical inputs.

Gate M9-E (agent readiness): deterministic case IDs, reviewed provenance, links, indexable tags and decision predicates; explicit case-to-pattern Markdown links and source-backed routing metadata now; actual schema/index/retrieval wiring only when existing metadata/search implementers provide stable contracts. **No curated graph design or implementation is in scope.** Query/evaluation fixture set of at least 30 case-oriented questions including counterfactual and unanswerable queries. Require clear cross-provider origin and temporal validity, no private corpus in Tycho.

Gate M9-F (acceptance): local source/license review; independent technical/semantic reviewer; tests and validation feasible at milestone stage; acceptance checkpoint with admitted source counts vs drafted vs verified; open known limitations. No claim of 'all patterns validated' or runtime measured.

## Work breakdown (new separate Epic E16)

| Task | Work package | Deliverable | Dependencies |
|---|---|---|---|
| E16-01 | Primary source verification/admission | Recheck every link and publisher, normalize citation metadata, license, date/version and type; reject unsupported/hype sources | This discovery baseline; existing source policy |
| E16-02 | Netflix Java platform fleet migration | Case chapters on JDK/Guice→Spring Boot, deprecating RxJava, Zuul/Netty and DGS/Spring GraphQL | E16-01 |
| E16-03 | Netflix concurrency / performance failures | VT locking, CPU-bound counterexample, ZGC, false sharing, production performance measurement caveats | E16-01 |
| E16-04 | Netflix cloud, data, orchestration and resilience | Cloud transformation, Cassandra connector replacement, sharding/time-series, Conductor and chaos/resilience | E16-01 |
| E16-05 | Other-company architectural transitions | Modular-monolith vs microservices, storage, streaming, traffic and deployment case chapters | E16-01 |
| E16-06 | Cross-company decision synthesis | ≥6 evidence-backed comparison/application/contraindication pages + transition/ADR exercises | E16-02..05 |
| E16-07 | Case identity/provenance/retrieval contract | Metadata mapping, typed relationships, searchable dimensions, stable citations, local routing/evaluation fixtures, later adapter points | E16-01 and stable K10–K20 contracts |
| E16-08 | Audit and milestone acceptance | 30+ hard questions, contradiction tests, independent technical review, source/version audit, M9 evidence report | E16-02..07 |
| E16-09 | Create the actual GitHub milestone | New native M9 milestone, associate E16-01..08 and epic, verify URL (GitHub connector currently cannot create milestones) | E16 epic |

Recommended milestones across work: 8 Netflix accepted cases; 12 cross-company accepted cases; 6 comparison pages; ≥30 evaluation questions. These are **targets**, not work already produced.

## Content integration, not a detached anthology

Proposed new navigation: `book/cases/README.md` for case routes; one company navigation node `book/cases/netflix/README.md` with bounded case pages; other-company navigation nodes only as authored (no empty placeholders). Case pages link to canonical Tycho owners in `book/application/`, `book/distributed/`, `book/execution/`, `book/data/`, `book/scaling/`, `book/search/`, `book/integration/`, `book/delivery/`, `book/performance/` and to the decision-model outputs as they exist.

New conceptual metadata (adapt to K10/K11 schema rather than inventing an incompatible committed schema):
- `document_kind: case-study`, stable `case_id`, `company`, `observation_period`, `source_ids`, `reported_vs_inferred`, `legacy_baseline`, `architecture_transitions`, `constraint_tags`, `workload_profile`, `failure_modes`, `patterns_applied`, `counterpatterns`, `result_metrics`, `migration_phases`, `confidence`, `verification_status`, `reviewed_at`.
- Case relationships are **ordinary typed metadata and reviewable Markdown links**, not edges of a graph. A page may explicitly link to related patterns, contrary evidence, source sections, and applicable decision guides with the conditions in prose. No graph schema/ownership/assembly/traversal is requested.
- Search routes by **problem first**, not company: e.g., 'high p99 JVM service with retry storms'; 'Cassandra hot partition'; 'complex microservice mesh ownership'; 'schema migration with no downtime'; 'Bazel vs Gradle build throughput'; 'migration agent with missing tests'.
- A Rocinante response must separate **what a source says happened** from **what might work for the queried legacy system**. Test with candidate evaluation sets; never present these as measured agent gains before running benchmarks.

## Core evaluations

At least one case question from each: exact historical fact, version-sensitive conflict, false 'Netflix uses X forever' assumption, rejected alternative, workload mismatch, unsuccessful rollback, production vs synthetic measurement, modernization compatibility, provenance lookup, query spanning two companies, and unanswerable 'what was p99?' where not published.

Comparative exemplars:
1. Netflix cloud service decomposition **vs** Shopify's chosen modular-monolith boundaries and Uber DOMA follow-up.
2. Netflix Zuul/RxJava-to-Java-platform evolution **vs** Netflix virtual-thread trial failure (not a false all-reactive/all-Loom binary).
3. Netflix ZGC benefits **vs** its non-generational ZGC costs/GC workload exceptions.
4. Netflix Cassandra Data Movement **vs** Uber Mezzanine, Stripe's online migration, and Discord's Cassandra→Scylla.
5. Netflix custom DGS→Spring GraphQL convergence **vs** platform OSS framework ownership.
6. Airbnb JVM Bazel migration **vs** Spotify fleet-wide automated upgrades and Uber CI/CD program.

## Existing roadmap relationship

- E14 continues independently writing foundation chapters; E16 cites only already accepted canonical owners and adds links later.
- E01/K30 decision rules consume cross-case applicability evidence but do not outsource correctness to company popularity.
- E03/K07 source register and provenance rules admit references; E04/K10–K13 provides metadata validation.
- K15–K16 curated graph work is **retired**; E07–E09/K17–K22 may index ordinary case metadata and provide source-bound retrieval through MCP **without graph infrastructure**.
- E13/K28 must benchmark case-oriented search quality, accurate provenance and insufficient-evidence responses. No duplicate search/MCP epics.
- E15/K29 maintains source freshness and change impact (publication updates are not automatic truth updates).

## Definition of completion

Do not close the milestone until the required **actual book case pages**, cross-company synthesis, tests, provenance/rights review, verification matrix and reviewer disposition are recorded. This planning document and source discovery are not a chapter corpus and should never close those issues by themselves.

## GitHub execution records (created 2026-10-19)

- [Epic E16 #113](https://github.com/rouslanbaranov/tycho/issues/113)
- [E16-01 #114](https://github.com/rouslanbaranov/tycho/issues/114) source verification
- [E16-02 #115](https://github.com/rouslanbaranov/tycho/issues/115) Netflix Java/Spring/reactive
- [E16-03 #116](https://github.com/rouslanbaranov/tycho/issues/116) Netflix JVM/performance failures
- [E16-04 #117](https://github.com/rouslanbaranov/tycho/issues/117) Netflix cloud/data/orchestration
- [E16-05 #118](https://github.com/rouslanbaranov/tycho/issues/118) additional-company cases
- [E16-06 #119](https://github.com/rouslanbaranov/tycho/issues/119) comparison and decision transfer
- [E16-07 #120](https://github.com/rouslanbaranov/tycho/issues/120) provenance/retrieval integration design
- [E16-08 #121](https://github.com/rouslanbaranov/tycho/issues/121) acceptance and review
- [E16-09 #122](https://github.com/rouslanbaranov/tycho/issues/122) native M9 setup and readiness verification

Native ownership: Program #1 → Epic #113 → tasks #114–#122. All ten E16 issues belong to [M9](https://github.com/rouslanbaranov/tycho/milestone/9). Closed duplicate issues #123–#130 are excluded.

## Start-readiness checkpoint — 2026-10-19

Ready to begin **source verification #114**, not accepted case publication. The program, 43-candidate register, Netflix dossier and case template are in main. No `book/cases/` pages exist yet. The 43 candidates are separate from the 169-record canonical source register; admission and exact claim verification remain #114 work.

Execution order: #114 → #115–#118 → #119; #120 can design portable contracts/fixtures after source admission; #121 audits completed content and records independent reviewer disposition. Do not wait for all M1–M8 completion to research cases. Actual schema/index/retrieval adapters wait for their stable owning contracts; **there are no M9 graph adapters**; record deferred integration explicitly rather than claiming deployment.

The Netflix task minima are three cases each (#115–#117), hence **at least nine distinct cases** if all three minima apply; this exceeds the eight-case milestone floor. Count unique case IDs once and satisfy both task and milestone criteria. #118 requires twelve additional cases across six other companies; #119 requires six comparisons; #120/#121 require at least thirty evaluation queries.

Before closure, name an independent technical reviewer and record the review event under #121; no reviewer has been asserted by this checkpoint. Start with bounded source admission, preserve missing metrics and historical contradictions, then author only admitted slices.

Local premerge validation against main `a31a0d86e0831e0c7a6701f84ca292cd6ca4c4fd`: boundary, 169 source records/references, generated catalogue, branch naming and all 50 regression tests passed. These checks do not validate the 43 new case sources or their claims. No GitHub Actions run was requested; M9 remains open.
