---
metadata_version: 1
id: "tycho.page.ee435fc3b8bf4b6ba35d9e6b1ee4b69c"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/saga.md"
title: "Saga"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Saga with bounded owner evidence."
route_hints:
  questions:
    - >-
      Should a multi-service business process be coordinated through local
      transactions and compensations?
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "saga"
    - "compensating transaction"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---

# Saga

**Identity.** Saga; family Data consistency, transactions and event sourcing; kind
transaction-pattern; priority core.

**Decision question.** Should a multi-service business process be coordinated through
local transactions and compensations?

**Good-fit conditions.** Steps cross service boundaries; intermediate states are
acceptable; compensation is a business decision; progress is durable.

**Hard contraindications.** Reject when one local transaction can preserve the invariant,
when no compensation is possible, or when intermediate visibility is unacceptable.

**Competing alternative.** Single local transaction or two-phase commit. Reverse when steps do
not genuinely cross independent owners or compensation is
unsafe.

**Failure and recovery.** Compensating transactions can fail and leave an inconsistent state;
transient failures and idempotence must be handled, and monitoring/tracking is required. Tycho
guidance, not a source claim: treat a lost acknowledgment as unknown and a failed compensation as
a repair item; verify the saga protocol in the owner section.

**Technical owner.** [Saga](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/saga-workflows.md#saga) — saga recovery is the bounded owner, not a full saga engine.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-saga.2026-10-21: all eleven served headings read.
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-saga-azure.2026-10-30: sections "Solution", "Key concepts in the
Saga pattern" and "Problems and considerations"; exact quotes "If a step fails, a series of
compensating transactions undoes the changes that the completed steps made" and "Compensating
transactions might not always succeed, which can leave the system in an inconsistent state";
revision 84fba1653e842f2af72959d9ac6c3d88821c179804049849e09431b5132069ca.
Both sources are public pattern/specification units, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Saga Choreography; Saga Orchestration; Compensating Transaction;
Transactional Outbox.
