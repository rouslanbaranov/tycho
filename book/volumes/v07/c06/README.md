---
metadata_version: 1
id: "tycho.chapter.1d8d87e683bc428e8dbed087106f37fd"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c06/README.md"
title: "V07/C06 — Horizontal/vertical scaling and autoscaling delay"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which headroom, statefulness and failure assumptions shape capacity?"
route_hints:
  questions:
    - "Which headroom, statefulness and failure assumptions shape capacity?"
  prerequisites:
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.k8s-hpa"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V07/C06 — Horizontal/vertical scaling and autoscaling delay

## Purpose and mission

Which headroom, statefulness and failure assumptions shape capacity? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Compare demand timescale with detection, provisioning, readiness and warm-up delay before relying on autoscaling.

Capacity that arrives after a short burst cannot prevent its initial overload; reserved headroom or admission control may still be needed. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Horizontal and vertical scaling: autoscaling lag, resource ceilings and stability](autoscaling-lag-and-capacity-limits.md) | Which headroom, statefulness and failure assumptions shape capacity? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Decompose the actual scale-out response time](autoscaling-lag-and-capacity-limits.md#1-decompose-the-actual-scale-out-response-time).
- [2. Feedback signals and the hot-key trap](autoscaling-lag-and-capacity-limits.md#2-feedback-signals-and-the-hot-key-trap).
- [7. Public evidence and review limits](autoscaling-lag-and-capacity-limits.md#7-public-evidence-and-review-limits).
- [Engineering walkthrough — A burst ends before new replicas become useful](autoscaling-lag-and-capacity-limits.md#engineering-walkthrough-a-burst-ends-before-new-replicas-become-useful).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C05 — Overload protection and graceful degradation](../c05/README.md) |
| Next | [V07/C07 — Capacity planning and cost/performance trade-offs](../c07/README.md) |
| Prerequisite | [V07/C05 — Overload protection and graceful degradation](../c05/README.md) |
| Source reading | [Page-local evidence and versions](autoscaling-lag-and-capacity-limits.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
