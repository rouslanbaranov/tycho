---
metadata_version: 1
id: "tycho.page.71f864d85c3e4213ad053e42e2976add"
kind: "page"
parent_id: "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
canonical_path: "book/volumes/v11-pattern-atlas/c09-scalability/vertical-scaling.md"
title: "Vertical Scaling"
topic_ids:
  - "scaling-mechanisms"
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Vertical Scaling with bounded owner evidence and explicit limits."
route_hints:
  questions:
    - "Should capacity be added by increasing CPU/memory/IO on one instance?"
  prerequisites:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  related_ids:
    - "tycho.chapter.3b9ec227ed58b92c0004eb0d39099142"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "vertical scaling"
    - "capacity"
evidence_scope:
  source_ids:
    - "src.kubernetes"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; source binding remains in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Vertical Scaling

**Identity.** Vertical Scaling; family Scalability and load distribution; kind
scalability-pattern; priority core.

**Decision question.** Should capacity be added by increasing CPU/memory/IO on one
instance?

**Good-fit conditions.** The workload fits one node; the provider allows a larger size;
restart/downtime is acceptable only when in-place resize is unavailable.

**Hard contraindications.** Reject when a single-node ceiling is near, when failover
requires multiple nodes, or when cost grows superlinearly.

**Competing alternative.** Horizontal scaling by adding replicas. The Kubernetes
page frames the choice as either changing the replica count (horizontal scaling) or
adjusting resources in place (vertical scaling); it does not state when either is
preferable. Reverse the choice when the larger node no longer meets availability or cost
constraints; those conditions are Tycho synthesis.

**Failure and recovery.** Resource ceilings are bounded; restart or migration risk is conditional
on in-place resize being unavailable. Verify limits in the owner
section.

**Technical owner.** [Vertical Scaling](../../v07-performance-scale-and-resilience/c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md#vertical-scaling) — resource ceiling and restart cost are bounded; instance sizing is platform-specific.

**Sources.** [src.kubernetes](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch5-k8s-resources.2026-10-21: all thirty-three served
headings read. The source is a public pattern/documentation
unit, not a benchmark. The competing alternative is bound to the same source's
Autoscaling Workloads page, read record read.autoscaling-workloads-vertical.2026-10-29,
section "Autoscaling Workloads", revision
f653ca7cce9cb752cd41e1fc2d10b335acd8033a186aa324eb499897bb7219ab: "When you scale a
workload, you can either increase or decrease the number of replicas managed by the
workload, or adjust the resources available to the replicas in-place. The first approach
is referred to as horizontal scaling, while the second is referred to as vertical
scaling." The page defines both approaches but not when either is preferable; the
reversal conditions remain Tycho synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Horizontal Scaling; Autoscaling; Capacity Planning; Contention.
