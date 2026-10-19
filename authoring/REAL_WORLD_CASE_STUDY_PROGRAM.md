# Real-World Modernization Case Study Program (Proposed M9)

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

## Proposed new GitHub milestone

**M9 — Real-World Architecture Modernization: Case Studies and Decision Transfer**

Proposed **new milestone**, separate from existing M1–M8 and existing E14/M8 coverage wave. **Native GitHub milestone not yet created** if unavailable through the connected repository tool; no due date fabricated. Its acceptance scope is evidence-backed case publication, comparative reasoning, evaluated retrieval readiness and traceable work, **not** deployment of MCP/semantic search (already owned by existing epics).

Gate M9-A (research intake): source links live, corporate authorship or speaker verified, rights noted, historical versions and source sections identified, contradictions recorded. Initial discovery register is only a candidate list.

Gate M9-B (Netflix depth): at least eight bounded, fully evidence-backed and cross-linked cases from the dossier, covering both successful and failed/rolled-back choices: legacy-to-cloud, framework and JDK fleet upgrades, Zuul/reactive evolution, VT locking, GC, DGS integration, data migration and workflow/operational transitions. Ensure 2023 vs 2026 versions are not combined.

Gate M9-C (cross-company breadth): at least twelve additional accepted cases across at least six companies, with contrasting modular monolith/microservices, zero-downtime database migration, CI/CD/build modernization, data partitioning, security/identity and service resilience. Prioritize **decision diversity**, not company popularity.

Gate M9-D (analytical transfer): at least six cross-company comparison/decision pages, explicit requirements/workload/legacy constraints, alternatives, contraindications, transition architecture and 'insufficient evidence' cases. Evidence-backed ADR examples use original hypothetical inputs.

Gate M9-E (agent readiness): deterministic case IDs, reviewed provenance, links, indexable tags and decision predicates; case graph relationship *specification* now, actual schema/index/graph wiring only when existing K10–K20 implementers provide the stable infrastructure. Query/evaluation fixture set of at least 30 case-oriented questions including counterfactual and unanswerable queries. Require clear cross-provider origin and temporal validity, no private corpus in Tycho.

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
- Graph relations: `case → observed_use_of → pattern`; `case → contradicts_universal_claim → claim`; `case → was_motivated_by → constraint`; `case → migrated_from/to → architecture-state`; `case → reports → evidence`. Every edge requires an evidence pointer and validity window. Do not infer global 'recommended' from a single observed use.
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
- E06/K15–K16 eventually indexes curated case relationships; E07–E09/K17–K22 makes them retrievable by future MCP.
- E13/K28 must benchmark case-oriented search quality, accurate provenance and insufficient-evidence responses. No duplicate search/MCP epics.
- E15/K29 maintains source freshness and change impact (publication updates are not automatic truth updates).

## Definition of completion

Do not close the proposed milestone until the required **actual book case pages**, cross-company synthesis, tests, provenance/rights review, verification matrix and reviewer disposition are recorded. This planning document and source discovery are not a chapter corpus and should never close those issues by themselves.

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
- [E16-09 #122](https://github.com/rouslanbaranov/tycho/issues/122) **native M9 milestone creation and issue assignment still required**

These are linked GitHub issues. Native GitHub sub-issue parenting and M9 milestone assignments have **not** been applied by this plan; references in descriptions carry ownership until those metadata operations are available.
