---
metadata_version: 1
id: tycho.page.398bb0c32955b8423801598db5feae25
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/retry-with-exponential-backoff.md
title: Retry with Exponential Backoff
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Retry with Exponential Backoff.
route_hints:
  questions:
  - Should a failed call be retried after increasing delays?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - retry with exponential backoff
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

# Retry with Exponential Backoff

**Identity.** Retry with Exponential Backoff; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should a failed call be retried after increasing delays?

**Good-fit conditions.** The failure is transient; the operation is idempotent or has an
effect identity; the attempt cap, backoff cap, jitter and remaining deadline are explicit;
a retry budget exists.

**Hard contraindications.** Reject when the operation is non-idempotent, when retries
amplify overload, or when the deadline cannot absorb the backoff.

**Competing alternative.** No retry or a single bounded retry. Reverse the choice when
retry latency and load exceed transient-failure benefit.

**Failure and recovery.** Retry storms, duplicate effects and synchronized clients are
common; jitter the delay, cap attempts and total delay, and stop on server pushback.

**Technical owner.** [Retry with Exponential Backoff](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md#retry-with-exponential-backoff) — retry budget and backoff are bounded; permanent-failure classification is caller-specific.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-retry.2026-10-21: all six served headings read. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Retry with Jitter; Timeout; Idempotency Key; Circuit Breaker.
