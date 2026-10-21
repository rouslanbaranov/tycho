---
metadata_version: 1
id: "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c02-contention-saturation-and-scaling-laws/README.md"
title: "V07/C02 — Contention, saturation and scaling laws"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When does coordination dominate additional capacity? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "When does coordination dominate additional capacity?"
  prerequisites:
    - "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
  related_ids:
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
    - "tycho.page.7ad835c06d5a4e3aabf6b14632f92c86"
    - "tycho.page.af6ce1d0b08a46bf908f851f77f7bb12"
    - "tycho.page.61c621bfa9a04a738e937416cec15e78"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---

# V07/C02 — Contention, saturation and scaling laws

## Purpose and mission

When does coordination dominate additional capacity? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Identify serial work, shared-state contention and resource saturation before extrapolating additional workers.

A scaling curve fitted outside the tested range can hide coordination cost; more workers may worsen useful throughput. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision](contention-saturation-and-scaling-laws.md) | When does coordination dominate additional capacity? |
| [Parallelism, serial work and scaling models](scaling-models.md) | Which model assumptions bound useful throughput as concurrency grows? |
| [Contended authority and discriminating scaling experiments](contention-response.md) | Which observation distinguishes resource saturation from coordination overhead? |

## Boundaries and further reading

- [V03/C05 — Thread, connection and buffer pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C01 — Queueing, Little's Law and measurement boundaries](../c01-queueing-littles-law-and-measurement-boundaries/README.md) |
| Next | [V07/C03 — Load-test methods and benchmark validity](../c03-load-test-methods-and-benchmark-validity/README.md) |
| Prerequisite | [V07/C01 — Queueing, Little's Law and measurement boundaries](../c01-queueing-littles-law-and-measurement-boundaries/README.md) |
| Source reading | [Page-local evidence and versions](contention-saturation-and-scaling-laws.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:8 -->
## 8. Evidence and limits

| Independently public source | Narrow statement supported | Unknown |
|---|---|---|
| [Gunther, *A General Theory of Computational Scalability Based on Rational Functions* (2008)](https://arxiv.org/abs/0808.1431) | Rational scale functions, queueing-bound relation and fit concept | Actual coefficient values or mechanism in a real service |
| [Little, *A Proof for the Queuing Formula*, 1961](https://doi.org/10.1287/opre.9.3.383) | Conditional mean occupancy/throughput/residence relation | Capacity or tail prediction |

All numerical values, diagrams, equations applied to imagined inputs and architecture conditions are
educational interpretations. No actual data was fitted, no benchmark performed, and no technical
review accepted any architecture for production. Full source-to-claim precision remains pending;
edition metadata is recorded.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.7ad835c06d5a4e3aabf6b14632f92c86:9 -->
Internal cross-reference: the Tycho capacity-experiment page is an original Tycho explanation, not
an independently inspected external source.

## Navigation

Canonical chapter in the current edition; start at the [volume landing](../README.md).
<!-- /tycho-question-source -->
