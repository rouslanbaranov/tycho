---
metadata_version: 1
id: tycho.page.f7ddc06b59d38b5d75b0b1ab248505da
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/retry-with-jitter.md
title: Retry with Jitter
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Retry with Jitter.
route_hints:
  questions:
  - Should retry delays include randomness to avoid synchronized retries?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - retry with jitter
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

# Retry with Jitter

**Identity.** Retry with Jitter; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should retry delays include randomness to avoid synchronized
retries?

**Good-fit conditions.** Many clients retry after the same failure; the operation has stable
effect identity or is naturally idempotent; sampled delay is bounded by the backoff cap and
remaining deadline.

**Hard contraindications.** Reject when retry timing must be deterministic, when jitter
would violate a deadline, when the thundering herd is caused by something else, or when a
non-idempotent effect has no stable operation identity.

**Competing alternative.** Fixed backoff or no retry. Reverse the choice when randomized
delays complicate tracing more than they reduce synchronization.

**Failure and recovery.** Jitter spreads load but does not fix a persistent dependency failure
or make a non-idempotent retry safe; bound the sampled delay and total attempts, and verify the
retry budget.

**Technical owner.**
[Deadlines, cancellation and retry
budgets](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#retry-with-jitter)
— jitter and budget are bounded; PRNG quality is implementation-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-retry.2026-10-21: all six served headings read. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Exponential Backoff; Timeout; Load Shedding; Circuit
Breaker.
