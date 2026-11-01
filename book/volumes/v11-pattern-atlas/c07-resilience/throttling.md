---
metadata_version: 1
id: tycho.page.ddfcdbdae287ddb5947c1adc9fa714b0
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/throttling.md
title: Throttling
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Throttling.
route_hints:
  questions:
  - Should request rate be limited to protect a dependency or budget?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - throttling
evidence_scope:
  source_ids:
  - src.sre-overload
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

# Throttling

**Identity.** Throttling; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should request rate be limited to protect a dependency or budget?

**Good-fit conditions.** A measurable bottleneck rate is known; throttling is observable;
callers can back off; queue age and per-class latency are measured.

**Hard contraindications.** Reject when the limit is arbitrary, when clients cannot react,
or when throttling would drop mandatory work.

**Competing alternative.** Rate limiting at the edge or admission control. Reverse the
choice when per-client fairness matters more than aggregate rate.

**Failure and recovery.** When capacity is exhausted, reject requests quickly rather than
processing them; callers may retry when appropriate.

**Technical owner.** [Throttling](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#throttling) — throttling is bounded to already-admitted work, not a universal rate-limit algorithm.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The record covers client-side adaptive rejection, not server-side
pacing; server-side pacing is synthetic owner guidance. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Rate Limiting; Load Shedding; Retry with Jitter; Priority Queue.
