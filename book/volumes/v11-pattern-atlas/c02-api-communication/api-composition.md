---
metadata_version: 1
id: "tycho.page.ade9759a19a0402594773756d097c11c"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/api-composition.md"
title: "API Composition"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for API Composition; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - >-
      Should an in-memory composition layer assemble a response from several
      service owners, rather than forcing one owner to duplicate all data?
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "api composition"
    - "api and service communication"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
    - "src.microsoft-api-design"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.microservices-api-composition.2026-10-21,
    read.microsoft-gateway-aggregation.2026-11-01 and
    read.microsoft-api-design.2026-11-01; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-11-01"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-11-01"
updated_at: "2026-11-01"
source_inspection_date: "2026-11-01"
content_verified_at: null
---
# API Composition

**Identity.** API Composition; family API and service communication; kind integration
pattern; priority core.

**Decision question.** Should an in-memory composition layer assemble a response from
several service owners, rather than forcing one owner to duplicate all data?

**Good-fit conditions.** The query is read-mostly; per-owner calls have bounded
deadlines; partial results and their declared failure behavior can be represented;
composition logic is owned and tested; the response does not require a distributed
transaction.

**Hard contraindications.** Reject the claim when strong consistency is required; when
fan-out latency exceeds the client budget; when composition needs writes across owners;
when one service can answer the query directly without duplicating authority.

**Competing alternative.** A maintained read model or a client-specific backend for frontend.
Reverse the choice when composition latency and partial-failure complexity exceed the
duplication alternative.

**Failure and recovery.** Slow dependencies and partial results are common. Azure's Gateway
Aggregation pattern recommends per-request timeouts, conditional error handling and a choice
between a partial response and failing the entire request. Tycho synthesis, not a source
claim: declare that choice in the composition contract and verify it in the owner section.

**Technical owner.** [API Composition](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md#api-composition) — composition is a dedicated bounded section, not a full composition platform.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microservices-api-composition.2026-10-21: all nine served
headings read.
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-gateway-aggregation.2026-11-01: Gateway Aggregation sections
read; pattern page, not a benchmark.
[src.microsoft-api-design](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-api-design.2026-11-01: versioning and tracing sections read;
API design guidance, not a composition test.

**Decision state.** applicable-under-conditions.

**Related entries.** Backend for Frontend; Gateway Aggregation; CQRS; Self-Contained
Service.
