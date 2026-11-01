---
metadata_version: 1
id: tycho.page.b244f2eabb0379ae6f08f0e358e532ae
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/fallback.md
title: Fallback
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Fallback.
route_hints:
  questions:
  - Should a failed primary path return a defined degraded result?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - fallback
evidence_scope:
  source_ids:
  - src.sre-cascading
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

# Fallback

**Identity.** Fallback; family Resilience and fault tolerance; kind resilience-pattern;
priority core.

**Decision question.** Should a failed primary path return a defined degraded result?

**Good-fit conditions.** The caller can act on a degraded result; fallback freshness,
authority and user-visible label are explicit; the fallback is cheaper and independently
safe.

**Hard contraindications.** Reject when no degraded result is meaningful, when fallback is
cached/fabricated without disclosure, or when the fallback depends on the same failed
resource.

**Competing alternative.** Fail fast with an explicit error. Reverse the choice when a
bounded degraded result is more useful than no result.

**Failure and recovery.** Fallback can mask failures and drift; a stale or partial result
must be labelled, and an explicit failure is safer than a plausible but wrong value.

**Technical owner.**
[Fallback](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#fallback)
— fallback selection is bounded to the overload path, not a universal degradation strategy.

**Sources.** [src.sre-cascading](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch4-sre-cascading.2026-10-21: all forty-four served
headings read. The section covers graceful degradation, not fallback; the fallback
freshness/authority/independence contract is synthetic owner guidance. The source is a public
pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Graceful Degradation; Circuit Breaker; Timeout; Load Shedding.
