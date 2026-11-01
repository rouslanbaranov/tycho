---
metadata_version: 1
id: tycho.page.f600c061ee0320ee72708eaa838d2eb5
kind: page
parent_id: tycho.chapter.87e52392e206a451ea5c79a4194c384b
canonical_path: book/volumes/v11-pattern-atlas/c05-caching-retrieval/single-flight-request-coalescing.md
title: Single Flight / Request Coalescing
topic_ids:
- caching
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Single Flight / Request Coalescing.
route_hints:
  questions:
  - Should duplicate in-flight requests for the same key share one source call?
  prerequisites:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  related_ids:
  - tycho.chapter.87e52392e206a451ea5c79a4194c384b
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - single flight request coalescing
evidence_scope:
  source_ids:
  - src.microsoft-caching-guidance
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

# Single Flight / Request Coalescing

**Identity.** Single Flight / Request Coalescing; family Caching and retrieval; kind
caching-pattern; priority core.

**Decision question.** Should duplicate in-flight requests for the same key share one
source call?

**Good-fit conditions.** Requests are read-mostly; the key is stable; waiters can tolerate
shared failure; the coalescing scope is bounded.

**Hard contraindications.** Reject when requests carry different authorization or
parameters, when one slow call would block unrelated callers, or when cancellation must be
independent.

**Competing alternative.** Independent calls with stampede protection at the source.
Reverse the choice when shared latency/failure outweighs duplicate-call reduction.

**Failure and recovery.** One failure fans out to all waiters; verify scope and
cancellation in the owner section.

**Technical owner.**
 [Single Flight / Request
Coalescing](../../v06-caching-indexing-and-retrieval/c02-hot-keys-cache-stampedes-and-read-amplification/stampede-protection.md#single-flight-request-coalescing)
— coalescing window and leader election are bounded; library semantics are implementation-specific.

**Sources.**
[src.microsoft-caching-guidance](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch3-ms-caching.2026-10-21: section "Manage concurrency in a cache". The
record covers cache concurrency, not request coalescing; coalescing and leader election are
synthetic owner guidance. The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Cache Stampede Protection; Cache-Aside; Distributed Cache; Timeout.
