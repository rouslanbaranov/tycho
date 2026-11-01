---
metadata_version: 1
id: tycho.page.b72e7b4836432886f164484c6a05665c
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/timeout.md
title: Timeout
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Timeout.
route_hints:
  questions:
  - Should each call have a bounded wait before it is treated as failed?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - timeout
evidence_scope:
  source_ids:
  - src.resilience4j
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-01'
source_inspection_date: '2026-10-21'
content_verified_at: null
---

# Timeout

**Identity.** Timeout; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should each call have a bounded wait before it is treated as
failed?

**Good-fit conditions.** A local wait bound is known; cancellation is safe; late completion
is handled; the timeout is shorter than the caller's remaining budget.

**Hard contraindications.** Reject when work must complete regardless of time, when
cancellation leaves irreversible effects that cannot be reconciled, or when the timeout
is longer than the caller can wait.

**Competing alternative.** Long-running async request-reply. Reverse the choice when
synchronous waiting blocks capacity that could serve other work.

**Failure and recovery.** A timeout is an ambiguous outcome, not proof that the remote
effect stopped. Look up the durable outcome and clean up resources; do not blind-retry
non-idempotent work.

**Technical owner.**
[Timeout](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#timeout)
— timeout values and cancellation are bounded; transport timeout behavior is
implementation-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-timelimiter.2026-10-21: all four served headings read.
Cancellation semantics remain synthetic guidance. The source is
a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Deadline Propagation; Request-Reply; Circuit Breaker; Idempotency
Key.
