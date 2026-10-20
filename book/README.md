---
metadata_version: 1
id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
kind: "book"
parent_id: null
canonical_path: "book/README.md"
title: "Tycho — System Design"
topic_ids:
  - "system-design"
perspectives:
  - "architecture"
summary: "Reader entry for Tycho — System Design. Scope includes Reading contract; Integrated foundational and real-world casebook reading; Available researched entry points."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Tycho — System Design?"
  prerequisites: []
  related_ids:
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.43b3f0c107e34e5a800d6c1de65069e8"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
    - "tycho.landing.4348c76938fc4d41b239721b94338436"
    - "tycho.landing.73dff529d70048569efef74bffa88b00"
    - "tycho.landing.984c44f8dbd44d8e89105b4d31787636"
    - "tycho.landing.816c847b8daa4d67a3fe1e3a8cbe3830"
    - "tycho.landing.e181d96c75784f818a330bb0f266520c"
    - "tycho.landing.fe2eace7b2df4ae480adbdf844b68100"
    - "tycho.landing.6f58e5c00dea4f4086963169a2590bf5"
    - "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
    - "tycho.landing.3870e6370654489c949e098b9acd1840"
    - "tycho.landing.b656116463d9480f83199d8202b127a4"
  excludes:
    - "No final edition publication or runtime reproduction is implied."
  keywords:
    - "Tycho"
    - "System"
    - "Design"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-18"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# Tycho — System Design

## Purpose and mission

Help readers and AI agents reason about system design: identify constraints, compare alternatives, state assumptions, explain trade-offs, analyze failure, and choose verifiable next steps.

The book should develop engineering judgment rather than prescribe universal architectures. Explain the conditions under which a design works, when it fails, and what evidence could change the recommendation.

## Reading contract

A reader can understand each chapter using the explanations and local links in this repository. Public citations support further verification. No private system knowledge or companion corpus is required.

The [selected ten-volume/69-chapter outline](../authoring/FINAL_TOC_AND_OWNER_BOUNDARIES_2026-10-20.md) assigns the engineering questions to canonical owners and records cross-topic boundaries and volume synthesis. The manuscript remains in topical folders; final Volume → Chapter → Page assembly is tracked in [#214](https://github.com/rouslanbaranov/tycho/issues/214). The [editorial contract](../authoring/EDITORIAL-CONTRACT.md) and [research workflow](../authoring/RESEARCH-WORKFLOW.md) govern sources, original prose, diagrams and validation.

## Current manuscript and publication status — 2026-10-20

The owner confirmed successful independent substantive/content acceptance of **all 69 primary chapter manuscripts** at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. [PR #218](https://github.com/rouslanbaranov/tycho/pull/218) is merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. The old 0/69 and pending-review statements in [dated review records](../authoring/CHAPTER_EDITORIAL_ACCEPTANCE_LEDGER.md) are historical.

The [accepted-head verification](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915) is an owner-reported **13/13 Python groups and 215/215 tests PASS**, zero skips, with a fresh complete 136-document index. That result belongs to the accepted SHA. This status edit requires a rebuilt index and separate local checks; it does not fabricate fresh source inspection or page-specific reviewer metadata.

**[#214](https://github.com/rouslanbaranov/tycho/issues/214) is ready:** create substantive volume/chapter landings and bounded pages, preserve identities and sources through reversible migration, finish reading paths and synthesis, validate the final frozen tree and publish a named edition. There is no finished physical ten-volume edition or deployed MCP service yet. Visual rendering and live MCP remain owner-cancelled.

See [current project state](../authoring/STATE.md), [post-merge reconciliation](../authoring/PROJECT_STATUS_RECONCILIATION_2026-10-20.md) and [roadmap](../authoring/ROADMAP.md).

## Integrated foundational and real-world casebook reading

The **M1–M8 architectural foundation and M9 real-world case studies were merged to `main` in [PR #216](https://github.com/rouslanbaranov/tycho/pull/216)**. Their integration checkpoint remains useful history, not the current branch or a final book edition. They are complementary parts of **one Tycho book**, not two separately finished products: **10 planned volumes and 69 unique primary foundational/decision chapter drafts**, plus an integrated [historical casebook](cases/README.md) with **29 evidence-scoped case studies and six synthetic decision playbooks**.

The [unified reading and editorial integration map](../authoring/UNIFIED_BOOK_M1_M9_INTEGRATION.md) links **all 35 applied pages** to their most relevant existing Vxx/Cxx chapter owners, without copying technical explanations or introducing a curated concept graph. Start with a concept/requirement, follow selected historical cases and contrast with draft decision playbooks, always checking source date, authorship, uncertainty and falsification conditions.

**Acceptance and edition delivery:** M9 [#121](https://github.com/rouslanbaranov/tycho/issues/121) remains closed under its scoped owner disposition; subsequent owner acceptance of all 69 primary manuscripts and PR #218 merge completed #213/E14. [#214](https://github.com/rouslanbaranov/tycho/issues/214) now owns final assembly and named publication. The [M9 transfer register](../authoring/M9_CHAPTER_TRANSFER_AND_NONCLAIMS_2026-10-20.md) preserves support/nonclaim boundaries. Curated graph infrastructure remains excluded.

## Available researched entry points

- [Real-world architecture modernization cases and decision playbooks](cases/README.md) — 29 public-source historical case drafts and six synthetic comparisons, linked to the canonical technical explanations.
- [Application architecture, evidence and quality foundations](application/README.md) — context and views, hypothesis/evidence discipline, domain/module boundaries, SOA/microservices, ports/adapters and safe modernization.
- [Performance, workload and queueing](performance/README.md) — arrival models, queueing, scaling laws, cost/capacity, tail latency, load-test validity and overload contracts.
- [Distributed coordination](distributed/README.md) — causal ordering, quorum and leader-change failure modes, transactions, sagas, outbox, CQRS and projections.
- [Search and retrieval architecture](search/README.md) — inverted indices, SQL FTS, vector/ANN, hybrid ranking, graph data models as educational material, and retrieval evaluation.
- [Scaling mechanisms](scaling/README.md) — sharding, connection pooling, cache freshness and overload controls.
- [Data storage and database engines](data/README.md) — PostgreSQL 17 transactions, WAL, replication, query/index choices and comparison of alternative storage models.
- [Messaging and stream processing](integration/README.md) — Kafka, RabbitMQ, Pulsar, NATS, stateful stream processing and CDC, with versioned evidence.
- [Java concurrency and execution](execution/README.md) — platform and virtual threads, Reactor/WebFlux/R2DBC, Netty/Vert.x/Quarkus/Mutiny/RxJava.
- [Deployment and recovery](delivery/README.md) — rollout, compatibility and restoration constraints.
- [Runtime topology and disaster recovery](deployment/README.md) — control-plane/data-plane limits, failure domains and region recovery decisions.
- [Observability and incident response](observability/README.md) — SLOs, metrics, traces, lineage, audit and original incident response model.
- [Security and safe agent-accessible knowledge](security/README.md) — identity, object authorization, untrusted source boundaries and data privacy as System Design topics.
- [Architecture decision and modernization guidance](decisions/README.md) — source-grounded requirements, legacy baseline, pattern applicability and progressive evidence-first question routes.

These are the current topical reading entries for the accepted manuscript. Final volume/chapter navigation and the published edition remain #214. The [coverage audit](../authoring/BOOK_COMPLETENESS_AUDIT.md) and editorial reports preserve historical observations and evidence limits; their pending statuses are superseded by owner-confirmed manuscript acceptance.

## Machine-readable knowledge product

The book is also the canonical content for a planned read-only MCP knowledge service. External agents will discover its structure through onboarding, retrieve ranked sections, verify source-to-claim provenance and browse typed metadata/navigation using versioned snapshots. A shared Rocinante integration package will carry the operating guidance. These are required roadmap outcomes; see the [knowledge-platform plan](../authoring/knowledge-platform-and-mcp-plan.md). The hosted service and full evaluation are not implemented; foundational schemas and some deterministic routing/validation tooling already exist, with current coverage and test limits recorded separately. A manually curated concept graph is not in Tycho's delivery scope. The book remains self-contained and locally navigable without MCP.
