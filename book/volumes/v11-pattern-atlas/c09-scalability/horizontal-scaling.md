---
metadata_version: 1
id: tycho.page.2405b393b0c69cc4c0cf307b2d06ddd1
kind: page
parent_id: tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
canonical_path: book/volumes/v11-pattern-atlas/c09-scalability/horizontal-scaling.md
title: Horizontal Scaling
topic_ids:
- scalability-and-load-distribution
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Horizontal Scaling.
route_hints:
  questions:
  - Should capacity be added by running more instances rather than a larger instance?
  prerequisites:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  related_ids:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - horizontal scaling
evidence_scope:
  source_ids:
  - src.k8s-hpa
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

# Horizontal Scaling

**Identity.** Horizontal Scaling; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should capacity be added by running more instances rather than a
larger instance?

**Good-fit conditions.** The workload can partition across instances; shared state is
removable; startup and coordination costs are bounded.

**Hard contraindications.** Reject when the bottleneck is a single shared resource, when
instances cannot be stateless, or when coordination cost grows faster than capacity.

**Competing alternative.** Vertical scaling or a larger partition. Reverse the choice when
shared-state contention dominates added instances.

**Failure and recovery.** Coordination and cold-start lag are common; verify ceiling in
the owner section.

**Technical owner.**
 [Horizontal
Scaling](../../v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md#horizontal-scaling)
— replica scaling and coordination cost are bounded; per-service capacity math is owner-specific.

**Sources.** [src.k8s-hpa](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-k8s-hpa.2026-10-21: all thirty served headings read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Vertical Scaling; Autoscaling; Load Balancing; Sharding.
