# Research log

## 2026-10-18 — Bootstrap

Established the project charter, source-admissibility boundary, authoring rules, and initial roadmap. No technical research, source admission, or chapter completion is claimed. General methodology was independently expressed; no companion corpus or implementation was imported.

## 2026-10-18 — Public-source discovery

Created a canonical inventory of 169 public research entries, with separate access, admission, reading and version states. Built coverage and implementation maps spanning the requested architecture, data, execution, delivery, workload and observability areas. Public source entry pages/abstracts were inspected; paid book contents and full linked documentation trees were not read. Direct JEP retrieval limits and further evidence gaps remain explicit.

Added a deterministic catalogue renderer and structural/reference validator. Removed coding-assistant-specific instructions; research and authoring continue in the ChatGPT project. Next action: bounded pilot contracts and chapter plan, with source version/section pinning and deeper reading.

## 2026-10-18 — Architecture decision layer added to plan

Added a bounded work plan connecting requirements, workload, existing-system constraints, pattern applicability, alternatives, evidence, ADRs, experiments and migration. Separated target architecture from interim coexistence and transition states. Added four navigation routes and pilot acceptance criteria, including insufficient-evidence outcomes. Updated the roadmap, methodology pointer and next action. This records planned work; no decision models, templates, graph, evaluated selection engine or real-system modernization were implemented.

## 2026-10-18 — Complete knowledge-platform and MCP scope recorded

Expanded the roadmap from book-first optional delivery to a mandatory self-contained book plus external-agent knowledge service. Added a 30-capability status/acceptance matrix covering authoring, metadata/schema/index validation, reproducible public code evidence, two graph layers, ranked retrieval, semantic/hybrid evaluation, read-only MCP, onboarding, shared Rocinante integration, snapshots, independent deployment, access controls, observability and quality/cost evaluation. Removed the prior deferred-until-justified wording for MCP delivery. Tool/engine choices remain evidence-based; development is not delegated. No platform implementation or deployment was performed in this planning update.

The shared external specialist remains Rocinante. Tycho supplies provider-specific MCP/onboarding guidance and integration tests; no separate book-specific expert is planned. Multi-provider reasoning occurs outside the corpus, with source attribution and isolation, and creates no dependency on or ingestion of another knowledge collection.


## 2026-10-18 — TYCHO-17 requirements and workload profile (feature branch)

Started on `feature/TYCHO-17-requirements-and-workload-profile` from `main`; one issue per branch is now explicit in repository instructions, with PR branch-name validation. This planning convention does not by itself configure GitHub branch protection.

Authored `authoring/models/requirements-workload-profile.md`, `templates/requirements-workload-profile.md`, `examples/synthetic-workshop-registration.md`, and `authoring/contracts/TYCHO-17-research-contract.md`. The first defines required business outcomes, hard constraints versus preferences, quality-attribute scenarios, arrival/concurrency/mix/skew/growth dimensions, SLI/SLO measurement contracts and evidence gates. The second offers a reusable input contract. The third illustrates assumptions and arithmetic using a wholly fictional registration portal, not a benchmark or current-system observation.

Bounded source inspection: public arc42 Section 1 (§1.1/§1.2), Google SRE Workbook Chapter 2 (SLIs and their implementation), Grafana k6 open/closed arrival models, each read from official public pages on 2026-10-18. Full works were not read. The registered Little's Law paper remains discovery-only for this slice; no claim is attributed to unread paper contents. Source register remains discovery-level until section-level read states are supported by its validator.

Quality scope: independent-origin review of authored content, checks of example calculations and branch-name parsing, repository boundary checks, source inventory checks and PR workflow. These are mechanical validations and a bounded self-review, **not** a human-approved architecture, measured capacity, proven invariant or production-validated SLO.

Validation outcome: [PR #95](https://github.com/rouslanbaranov/tycho/pull/95) opened as draft; [branch convention CI](https://github.com/rouslanbaranov/tycho/actions/runs/39153497864) and [source boundary CI](https://github.com/rouslanbaranov/tycho/actions/runs/39153497829) both completed successfully. Local source-boundary scans also passed on the feature commits. No human approval or merge is claimed. Next: independent review and merge; issue remains open. Subsequent #18/#19 work is not implemented here.


## 2026-10-18 — Book-first delivery reprioritization and TYCHO-23 draft

Following completion of #17, reconsidered the order of work: comprehensive legacy-modernization and pattern applicability contracts would be mostly hypothetical before any evidence-backed technical chapters existed. The requirements/workload model is sufficient to define the initial questions; it is not a substitute for researched architecture knowledge.

Drafted `book/PROPOSED-STRUCTURE.md`: audience, independent question-driven topic ownership, provisional 10-volume outline, bounded chapter/page responsibilities, mandatory coverage mapping and retrieval entry routes. This is a *proposal*, not an approved table of contents, written chapter, source deep-reading, technical finding or implementation claim.

Planned the revised dependency chain: #23 (after completed #17) → #24 → #25 → #26 → #38–#40. Specific blockers for #18/#19 are moved downstream of evidence-backed pilot content; final accepted case-study methods will be reworked from those findings. #37 remains required validation infrastructure, developed in parallel, but it will not prevent writing the first material under manual source/claim and existing mechanical checks.

The `scripts/apply_book_first_order.py` workflow is intentionally limited to five known Issues and will run after the #23 PR merges. Update the checkpoint after **verified** GitHub execution. This planning update does not execute source reading, publication of the book or generation of technical pages.


## 2026-10-18 — TYCHO-26 pilot scope

Selected three tightly bounded and complementary public-evidence research tasks: queueing and finite-window Little's Law (#38), transaction-to-event/outbox and duplicate effects (#39), and progressive release/compatibility/recovery (#40). Added three detailed research contracts and one authoring wave checklist. Each records source IDs, exact intended sections, uncertainty, negative cases, and acceptance; writing these contracts does **not** imply full reading of sources, empirical tests or completed technical chapters. Continue in issue-specific branches, verify exact public sources while authoring, and do not expand the whole corpus automatically.


## 2026-10-18 — TYCHO-38 first researched technical page (feature branch)

Wrote the first bounded technical chapter, `book/performance/queueing-littles-law.md`, with `book/performance/README.md` as its navigable landing. This is original prose, diagrams and entirely synthetic examples, not copied source text, measured live capacity or a completed volume. The chapter covers unit/boundary definitions; Little's Law for steady means; a finite-window edge counterexample; mean-versus-p99; closed/open workload generation; admission/backlog dynamics; overload and recovery; alternatives, applicability and an explicit insufficient-evidence outcome.

Actually inspected these independent public passages for this slice on 2026-10-18:
- `src.little-law`: Kim & Whitt (2013), DOI 10.1287/opre.2013.1193, author PDF, Abstract, §§1, 1.1–1.2, §2.1 definitions and §2.2 finite-window edge effects.
- `src.k6`: Grafana k6 official *Open and closed models*, online docs labelled v2.2.x; Closed Model, Drawbacks, Open model.
- `src.sre-overload`: SRE public 2017 *Handling Overload*, Client-Side Throttling and closing remarks on per-task protection.

The source register remains at its existing discovery-level status; this chapter's narrow claim ledger is the evidence location. No entire book, source repo or complete external documentation tree was read. No real workload was generated or benchmark recorded. Mechanical unit tests check the article's synthetic arithmetic and explicit counterexample. A green CI is not equivalent to a technical expert/human review, which remains unrecorded.

Subsequent work belongs to independently researched end-to-end (#39) and recovery (#40) pilot branches, not an automatic full-book enrichment.


## 2026-10-18 — TYCHO-39 distributed outbox and idempotency chapter

Authored `book/distributed/transactional-outbox-and-idempotency.md` plus its volume landing and deterministic textual checks. This is original architectural explanation with four Mermaid diagrams, synthetic workshop registration scenario, local transaction boundary, three distinct identities (request, entity, event), failure/replay matrix, consumer-side deduplication design and exact independent-source ledger.

Actually examined public sections: Debezium **3.6 Outbox Event Router**, Basic outbox table/configuration, event key/ID/payload and SMT predicate details; PostgreSQL **17** Transaction Isolation, BEGIN and WAL introduction; **RFC 9110 §9.2.2** Idempotent Methods; AWS Builders' Library *Making retries safe with idempotent APIs* on side effects, semantic retries, late arrivals and same-token/different-intent. Specific product behaviors were not independently reproduced. No broker/database stack, benchmark, consumer replay or global exactly-once proof was executed. Tests assert presence, structure and source paths only; no integration-level correctness is claimed.

Manuscript is under branch review; retain the separate K30 and book completion gates. The next independent chapter is #40 for deployment and recovery, not generic pattern-catalog generation.


## 2026-10-18 — TYCHO-40 rollout, schema compatibility and recovery

Authored `book/delivery/safe-rollout-and-recovery.md` plus accessible Mermaid navigation and deterministic document/arithmetic tests. This is original technical prose about target vs transition states, rolling/canary/blue-green, new/old schema coexistence, failed release behavior, restoration evidence, RPO/RTO and failure-domain load. Includes four Mermaid diagrams, synthetic N/N+1 compatibility matrix, and explicit cases in which binary rollback cannot reverse a new-format persisted record. No production deployment or recovery test was performed.

Actually inspected bounded public sections: Kubernetes online Deployments documentation in the v1.37 family (rolling strategy, status, failed deployment), Argo Rollouts stable Canary and BlueGreen concepts (precise operational version **not pinned**), AWS DR official whitepaper Introduction/DR options, and Google SRE Addressing Cascading Failures on overload and recovery. Version-specific claims must be narrowed in a future actual installed environment. The tests assert sample arithmetic and document scope only. No measured RTO/RPO, claimed rollback guarantee, certification or independent human approval.

Pilot-wave content exists as three bounded, separately owned chapters; this does not equate to all proposed volume chapters, metadata, indexed retrieval or MCP completeness. Further book authoring requires independent admitted public-source reading.


## 2026-10-18 — TYCHO-41 pilot quality gate

Compiled 25 evidence-linked evaluation questions across fact, synthesis, trade-off, failure, change impact, contradiction and unanswerable categories. Ran a deterministic **author-created in-sample** lexical smoke on only the three pilot pages, observing 25/25 top-1 correct topic routes, not verified end-to-end answers or general ranking quality. Recorded an ADOPT/REVISE/REJECT author assessment; major gaps include independent human review, strict metadata/provenance, version-pinned sources, fuller corpus and actual agent/tool cost evaluation. No full-book acceptance implied.


## 2026-10-18 — TYCHO-79 application architecture research

Authored three source-grounded pages under `book/application/`: architecture quality drivers and views; modular monolith, bounded context, ports/adapters, SOA and microservices; and architecture evolution/service extraction. Added a Mermaid-based landing and mechanical document tests. Diagrams and scenario examples are independently authored and explicitly synthetic.

Public passages inspected: Lewis/Fowler *Microservices* (2014), componentization, capabilities, decentralized data and SOA comparison; Fowler *Monolith First* (2015) with stated evidentiary caveats; Fowler *Bounded Context* (2014), model/language boundaries; Cockburn *Hexagonal Architecture* (2005), intent/solution/structure; OASIS SOA Reference Model 1.0 §§2.1, 3.2–3.3; public Spring Modulith 2.1.0 overview and 1.3.12 verification rules; arc42 Section 1 §§1.1–1.3; official C4 Introduction; public SRE Workbook Chapter 2, initial SLO process. The Evans DDD Reference PDF and comprehensive technical implementation sources were **not** read for this slice.

This is partial original book content with bounded publication references, not empirical architecture research or proof of a deployable system. No executable domain service, load test, completed modernization or independent technical review is claimed. GitHub-hosted CI runs only at accepted milestone closure per #104; no issue-level pipeline should be reported as passed.


## 2026-10-18 — TYCHO-80 causal and transactional research

Authored three self-contained technical pages in `book/distributed`, each with original Mermaid diagrams, failure conditions and public-source ledgers, plus updated navigation. Specifically inspected: Lamport's 1978 **publication record/abstract only** (full PDF not inspected), Ongaro/Ousterhout's 2014 extended Raft report §§2, 5.1–5.4, PostgreSQL 17 §§13.2/13.5, Richardson's public Saga pattern and 2019 semantic-lock discussion, Fowler's 2005 *Event Sourcing* draft, Fowler's 2011 CQRS and 2017 event-driven taxonomy, Richardson's public CQRS pattern. The pre-existing outbox evidence page was reused by a canonical link rather than duplicated.

No original research paper PDF, full commercial book, deployed consensus cluster, database isolation integration test, saga processor, event-sourced store, LLM answer-quality benchmark or independent human review has been performed for these pages. Material claims are bounded to the sources cited and synthetic illustrations. Full GitHub regression CI is deferred until the accepted milestone closes, pursuant to #104.


## 2026-10-18 — TYCHO-81 integration and stream processing

Authored three synthetic, version-bounded technical pages in `book/integration/`: Kafka 4.1 partitions/replication/producer/consumer offsets and transaction limits; RabbitMQ 4.3 queue publisher/consumer acknowledgements, NATS JetStream durable state, Pulsar 4.1 BookKeeper roles, abstract durable workflow state; and Kafka Streams 4.1 state stores, archived Flink 2.1 checkpoints/savepoints, PostgreSQL 17 logical replication and Debezium 3.6 outbox/CDC integration. Sources inspected from official public docs on 2026-10-18 with exact section scopes on each page. Mermaid diagrams and failure stories are original; no product ranking from measurements is claimed.

No broker, stream processor, CDC connector or durable workflow instance was installed, no cross-system exactly-once proof or failover benchmark was run, and no independent human technical review is recorded. GitHub Actions remain milestone-only; do not claim an issue-level CI pass.

## 2026-10-18 — TYCHO-82 Java execution research

Selected issue #82 after confirming #79 closed and no open PR or existing #82 branch. Inspected versioned public primary sections: OpenJDK JEP 444; OpenJDK JEP 491 implementation review and JDK 24 targeting notice (canonical JEP body inaccessible); Spring Boot 3.3.13; Spring Framework 6.2; Reactor 3.7.0; R2DBC SPI 1.0.0.RELEASE; Netty 4.x rolling guide; Vert.x 4.4.9; Quarkus 3.27; SmallRye Mutiny 2.9.0; RxJava v3.1.9 tagged README. Wrote three original research chapters and execution landing with Mermaid/text alternatives, failure/selection criteria and claim-level evidence ledgers. Synthetic arithmetic is explicitly not measured.

Added a structural test module and navigation/checkpoint updates. This execution environment cannot clone the repository or run its local Python test suite; the standard premerge check was **not executed**. Connector-side static checks, if performed, are not equivalent to Python unit tests or technical correctness review. No Java compilation, load tests, JFR, human review, GitHub Actions runs or milestone acceptance is claimed.


## 2026-10-19 — TYCHO-83 database models and recovery research

Authored three new source-grounded documents plus navigation and structural tests under `book/data/`. Inspected PostgreSQL **17** MVCC §13.1, transaction isolation §13.2, serialization handling §13.5, planner/EXPLAIN §14.1, indexes chapter 11, WAL §28.3, physical streaming replication §26.2, logical replication chapter 31, and backup/PITR chapter 25. Broader model reading: official SQLite architecture (2025-05-31), CockroachDB **v24.3** architecture, FoundationDB **8.0** architecture, Apache Cassandra **5.0** overview, MongoDB official embedding/referencing docs, official ClickHouse MergeTree docs and Neo4j graph concepts. All diagrams, schema/SQL examples, business constraints and calculations are original and hypothetical. No live PostgreSQL EXPLAIN, failover/restore, engine comparison benchmark, schema migration or independent technical review was performed. GitHub Actions reserved for milestone acceptance.


## 2026-10-19 — TYCHO-84 scale-out, pool and cache mechanisms

Authored three original evidence-scoped technical pages in `book/scaling/` and an editable Mermaid landing. Inspected official public Vitess 24.0 Resharding guide, public VSchema reference, PostgreSQL 17 declarative partitioning and server connections, HikariCP README configuration, PgBouncer pool_mode/max_client_conn/default_pool_size, Caffeine Eviction/Refresh wiki, and Redis cache-aside and EXPIRE docs. Source provenance is exact at named public sections on each page. Synthetic hot-key, connection-count/hold-time and cache-fill race examples are not benchmarks. No Vitess resharding, production DB load measurement, pool compatibility test, or cache failover was run. Independent technical review and milestone-wide regression CI remain separate gates.


## 2026-10-19 — TYCHO-85 lexical, vector, hybrid and graph retrieval

Authored three original research chapters and Mermaid navigation in `book/search/`. Inspected PostgreSQL **17** full-text search §12.3 and text indexes, selected Apache Lucene **10.3.0** BM25Similarity API and core overview, official pgvector README (exact search, HNSW/IVFFlat, selective filtering, iterative scans), Faiss official index-family and index-factory wikis, Elasticsearch official reciprocal-rank-fusion score/reference, and Neo4j public graph concepts. Exact URL/section scopes and rolling-reference limitations are recorded in chapter evidence ledgers. Original RRF arithmetic and raw-FP32 vector size examples are not measured application performance.

**No** Tycho lexical index, embeddings, ANN service, knowledge graph traversal runtime, MCP server, independent human judgments, answer correctness benchmark or token cost benchmark was built by this issue. These are future implementation/evaluation phases, and the content explicitly distinguishes them. GitHub Actions remains milestone-only; no per-PR CI pass asserted.


## 2026-10-20 — Authorized content enrichment and critical topic additions

Following explicit owner authorization, wrote two new chapters (network request paths; object storage), seven new technical pages and twelve source-scoped additions to existing owners. All earlier page identities and baseline text are preserved. Recorded 25 selected public-document inspections, 22 new source admissions and three reused IDs; no full documentation-tree read or runtime execution is asserted.

[Scope](ENRICHMENT_SCOPE_2026-10-20.md) records every bounded question and acceptance case. The new conservation manifest keeps the original 69-manuscript split baseline separate from two new chapters. Index and inventory are reconciled as a reviewable candidate. The execution environment is unavailable: Python, adversarial test execution and Mermaid parsing remain pending. The change must remain draft and #214 open until required checks and substantive acceptance.

## 2026-10-20 — Second enrichment pass for #214

The owner authorized all five newly proposed mechanisms and three complete worked projects. The [bounded contract](SECOND_ENRICHMENT_CONTRACT_2026-10-20.md) maps each to an existing chapter. Ten selected primary-source scopes were read; nine sources are new to the register and the TLA+ overview reuses its existing ID. The [inspection register](../sources/enrichment-inspections-2026-10-20.json) retains the first 25 readings and appends these ten.

FoundationDB's documentation site did not return usable content in the available retrieval path. Its public testing documentation was instead read from the exact GitHub revision recorded in the source entry. The replicated-data-types paper was read only in the declared introductory sections; later proofs were not checked. No implementation or experiment was run.

Eight original pages include explicit assumptions, counterexamples, failure/recovery, alternatives and proposed oracles. The projects contain synthetic workloads and arithmetic, with no measured production results or price claims. See [validation and unresolved gates](SECOND_ENRICHMENT_VALIDATION_2026-10-20.md). #214 remains open and PR #222 draft.

## 2026-10-20 — Recovered Python and Mermaid execution

The environment recovered and the exact PR #222 snapshot was checked locally: 16/16 Python groups, 233/233 tests with zero skips, and 221/221 Mermaid syntax parses passed. Python reproduced the 406-document candidate index byte for byte. [The executed report](PYTHON_MERMAID_VALIDATION_2026-10-20.md) pins the commit/tree and archives actual logs. No technical defect needed repair. Documentation status is reconciled; substantive acceptance remains pending and #214 stays open.

## 2026-10-20 — Readable volume and chapter directories

The owner authorized physical directory migration after the naming requirements were merged. The explicit map covers ten volumes, 71 chapters and all 406 canonical IDs; 339 files move. Only local path segments and current path metadata change. Every canonical file reconstructs the exact baseline bytes through inverse path transformation; external URLs and fragments retain their spelling. Four historical migration/decomposition/enrichment records retain their original bytes. New validation and nine negative/coverage tests preserve those boundaries. [Migration and validation record](DIRECTORY_MIGRATION_2026-10-20.md). #214 remains open.

## 2026-10-26 — Rocinante staged modernization contract (#61)

Following the owner's instruction, recorded a proposed provider-behaviour
contract for the shared specialist: POC → MVP → Product stages with optional
sub-stages, an architecture delta per stage, and per-stage evidence gates that
cite Tycho pages and sections as the evidence source. The contract defines
stage definitions, evidence rules, a logical envelope, refusal rules and a
synthetic example with no measurements. It is linked from the knowledge
platform plan, decision navigation and the target/transition model. No agent
implementation, tool change, fixture, benchmark, evaluation or human review is
claimed. See [the contract](ROCINANTE-STAGED-MODERNIZATION-CONTRACT.md).
