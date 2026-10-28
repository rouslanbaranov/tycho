---
metadata_version: 1
id: "tycho.page.7082c6b84e0f4d04bec339b06fe600fc"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/pipes-and-filters.md"
title: "Pipes and Filters"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Pipes and Filters; bounded stage-contract evidence and limits."
route_hints:
  questions:
    - "Should processing be composed as independent stages connected by a message contract?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "provider-specific pipeline implementations"
  keywords:
    - "pattern atlas"
    - "pipes and filters"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-28"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-28"
source_inspection_date: "2026-10-28"
content_verified_at: null
---

# Pipes and Filters

**Decision.** Compose processing as ordered stages only when each stage has an independent
contract and the pipeline owns ordering, partial completion and recovery. Keep one cohesive
transformation when the work must be atomic or the stages cannot be operated independently.

**Identity.** Pipes and Filters; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should processing be composed as independent stages connected by a
message contract?

**Good-fit conditions.** Stages have distinct responsibilities and can fail or retry
independently; the message contract and ordering scope are explicit; per-stage lag and queue
depth are observable; a completion or checkpoint rule has an owner. Tycho guidance, not a
source claim: each stage carries an effect identity for deduplication, and the chain is
bounded.

**Hard contraindications.** Reject when one stage needs the whole transaction, when
intermediate latency or repeated message conversion exceeds the budget, when the pipeline
becomes an unowned distributed workflow, or when no one can recover a failed middle stage
from a declared checkpoint.

**Competing alternative.** One cohesive consumer with internal functions. Reverse the choice
when stage isolation and reuse no longer justify message hops.

**Failure and recovery.** A failed middle stage leaves earlier effects applied; record stage
identity and recover through a transactional client or a declared checkpoint. The source
states that the simple filter is not transactional, so an error before the output channel
loses the message; Tycho guidance adds per-stage idempotency and a replay boundary.

**Technical owner.** [Pipes and Filters](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#pipes-and-filters) — stage contract, ordering scope and non-transactional loss are bounded; backpressure, checkpoint and idempotency policy are Tycho guidance.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read records read.batch2-pipes.2026-10-21 and read.pipes-ch03.2026-10-28: the public
pattern page is publisher-abridged; Chapter 3, printed pp.70-77, supports mechanism, ordering,
non-transactional loss and the in-process alternative.
PDF revision SHA-256: c1e7125dcebfdd9a2b23a922dfbbc9694e5f8048e81e14dc95e2882043ac4f66.
The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Splitter; Aggregator; Content-Based Router; Process Manager.
