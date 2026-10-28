---
metadata_version: 1
id: "tycho.page.f213c7f6ef0741f18ea2e6f9d008f34f"
kind: "page"
parent_id: "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
canonical_path: "book/volumes/v11-pattern-atlas/c02-api-communication/async-request-reply.md"
title: "Asynchronous Request-Reply"
topic_ids:
  - "application-architecture"
  - "integration-architecture"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Asynchronous Request-Reply; bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should a client submit work and later fetch a result rather than hold a request open?"
  prerequisites:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  related_ids:
    - "tycho.chapter.9825cb82eb2142754c638aea1ba8d845"
  excludes:
    - "provider-specific operation handles"
  keywords:
    - "pattern atlas"
    - "asynchronous-request-reply"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-28"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-28"
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Asynchronous Request-Reply

**Identity.** Asynchronous Request-Reply; family API and service communication; kind
integration pattern; priority core.

**Decision question.** Should a client submit work and later fetch a result, rather than
hold one synchronous request open?

**Good-fit conditions.** Work does not fit a same-connection response; clients can poll a status
endpoint; operation identity is defined.

**Hard contraindications.** Reject when a same-connection synchronous response suffices or when
duplicate submission cannot be made idempotent.

**Competing alternative.** A same-connection synchronous response when most APIs respond
quickly enough.

**Failure and recovery.** A lost response is ambiguous; an idempotency key lets a retry return
the existing status resource.

**Technical owner.** [Asynchronous APIs and streaming: demand, deadlines and cancellation](../../v03-execution-concurrency-and-flow-control/c04-asynchronous-apis-and-streaming/asynchronous-apis-streaming-and-cancellation.md#asynchronous-request-reply) — async demand and cancellation; not a full request-reply implementation.

**Sources.**
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-async-request-reply.2026-10-21: all twelve served
headings read. Vendor pattern page, not a
benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** API Gateway; API Composition; Retry with Idempotency; Deadline
Propagation.
