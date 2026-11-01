---
metadata_version: 1
id: tycho.page.4caa1a3e2fc8f1e2b76783153858406d
kind: page
parent_id: tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
canonical_path: book/volumes/v11-pattern-atlas/c09-scalability/autoscaling.md
title: Autoscaling
topic_ids:
- scalability-and-load-distribution
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Autoscaling.
route_hints:
  questions:
  - Should capacity be adjusted automatically from observed or predicted demand?
  prerequisites:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  related_ids:
  - tycho.chapter.3b9ec227ed58b92c0004eb0d39099142
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - autoscaling
evidence_scope:
  source_ids:
  - src.keda
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

# Autoscaling

**Identity.** Autoscaling; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should capacity be adjusted automatically from observed or
predicted demand?

**Good-fit conditions.** Metrics reflect useful demand; scale-up/down delays are
acceptable; stabilization prevents oscillation.

**Hard contraindications.** Reject when demand is stable, when startup lag exceeds the
burst, or when the metric can be gamed.

**Competing alternative.** Static capacity or scheduled scaling. Reverse the choice when
autoscaling churn and cold starts dominate cost.

**Failure and recovery.** Lag and oscillation are common; verify stability in the owner
section.

**Technical owner.**
[Autoscaling](../../v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md#autoscaling)
— signal, lag and hysteresis are bounded; capacity forecast is service-specific.

**Sources.** [src.keda](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-keda.2026-10-21: the single served heading read.
The source is a public pattern/documentation
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Horizontal Scaling; Vertical Scaling; Load Balancing; Capacity
Planning.
