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
