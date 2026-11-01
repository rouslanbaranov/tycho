---
metadata_version: 1
id: tycho.page.ed90d20d04dc40f7c64357a07aff972f
kind: page
parent_id: tycho.chapter.69085752a11c69305aa2a369b8ec9d29
canonical_path: book/volumes/v11-pattern-atlas/c07-resilience/rate-limiting.md
title: Rate Limiting
topic_ids:
- resilience
perspectives:
- architecture
- operations
- evaluation
summary: Decision card for Rate Limiting.
route_hints:
  questions:
  - Should each client or tenant have an enforced request budget?
  prerequisites:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  related_ids:
  - tycho.chapter.69085752a11c69305aa2a369b8ec9d29
  excludes:
  - No owner acceptance is claimed for this card.
  keywords:
  - pattern atlas
  - rate limiting
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

# Rate Limiting

**Identity.** Rate Limiting; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should each client or tenant have an enforced request budget?

**Good-fit conditions.** Client identity is known; limits define window, burst and rejection
response; limits reflect capacity and fairness.

**Hard contraindications.** Reject when traffic is one internal caller, when limits would
block essential work, or when identity cannot be trusted.

**Competing alternative.** Global admission control or throttling. Reverse the choice when
per-client fairness is not required.

**Failure and recovery.** Bypass through many keys, burst doubling and unfair quotas are
common; bind limits to the scarce resource and declare retry guidance.

**Technical owner.**
[Rate
Limiting](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md#rate-limiting)
— rate limiting is bounded to request admission, not a universal overload policy.

**Sources.** [src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json)
read record read.sre-overload.2026-10-21: all eleven served headings read.
The source is a public pattern/documentation unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Throttling; Load Shedding; API Gateway; Gatekeeper.
