---
metadata_version: 1
id: tycho.page.6387b385f9816863166546ac2699995c
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/bulkhead.md
title: Bulkhead
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Bulkhead.
route_hints:
  questions:
  - Should concurrency or resources for one dependency be isolated from the rest of
    the workload?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - bulkhead
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

# Bulkhead

**Identity.** Bulkhead; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should concurrency or resources for one dependency be isolated from
the rest of the workload?

**Good-fit conditions.** One dependency can exhaust shared pools; isolation limits blast
radius; per-pool queue age/utilization are observable; rejection behavior is defined.

**Hard contraindications.** Reject when isolation would strand capacity, when the
dependency is essential to all work, or when pool sizing cannot be observed.

**Competing alternative.** Shared pool with admission control. Reverse the choice when
isolation overhead and stranded capacity exceed containment benefit.

**Failure and recovery.** Bypass, undersized partitions, a shared hidden queue and
starvation are common; detect per-pool metrics and fail the isolated class explicitly.

**Technical owner.** [Bulkhead](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md#bulkhead) — bulkhead isolation is bounded, not a full resilience-library guide.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-r4j-bulkhead.2026-10-21: all eight served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Circuit Breaker; Timeout; Load Shedding; Priority Queue.
