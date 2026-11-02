---
metadata_version: 1
id: tycho.page.56c4660fc5d32ccffeb026513442b425
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/load-shedding.md
title: Load Shedding
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Load Shedding.
route_hints:
  questions:
  - Should the system reject some work to preserve useful throughput under overload?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - load shedding
evidence_scope:
  source_ids:
  - src.sre-overload
  - src.aws-load-shedding
  claim_ids: []
  status: source-linked
  notes: Source-level bindings remain in the owner unit.
content_review:
  status: self-checked
  reviewed_at: '2026-11-01'
  reviewer: Automated authoring agent
  proof_uri: null
authored_at: '2026-11-01'
updated_at: '2026-11-02'
source_inspection_date: '2026-11-02'
content_verified_at: null
---

# Load Shedding

**Identity.** Load Shedding; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should the system reject some work to preserve useful throughput
under overload?

**Good-fit conditions.** Load exceeds capacity; rejection is cheaper than queueing; a
bottleneck-specific signal, fair principal policy and retry guidance are defined.

**Hard contraindications.** Reject when all work is equally critical, when rejection would
violate a hard obligation, or when capacity is actually available.

**Competing alternative.** Queueing or autoscaling. Reverse the choice when queue delay is
acceptable and capacity can expand.

**Failure and recovery.** Shedding the wrong work, unfair tenant impact and synchronized
retry storms are common; declare quotas and retry hints, and protect essential outcomes.

**Technical owner.**
[Load
Shedding](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#load-shedding)
— load shedding is bounded to the overload path, not a universal admission policy.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Throttling; Rate Limiting; Graceful Degradation; Priority Queue.
