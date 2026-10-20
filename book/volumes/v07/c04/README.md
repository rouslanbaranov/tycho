---
metadata_version: 1
id: "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c04/README.md"
title: "V07/C04 — Tail latency, fan-out and time budgets"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Why can p99 degrade despite adequate mean capacity?"
route_hints:
  questions:
    - "Why can p99 degrade despite adequate mean capacity?"
  prerequisites:
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-cascading"
    - "src.tail-at-scale"
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

# V07/C04 — Tail latency, fan-out and time budgets

## Purpose and mission

Why can p99 degrade despite adequate mean capacity? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Allocate end-to-end time across critical paths, queues, fan-out and retries using distributions and explicit cancellation.

Adequate mean capacity does not guarantee a tail objective; parallel dependencies and correlated delays can dominate the slowest path. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Tail latency, fan-out and end-to-end deadline budgets](tail-latency-fanout-and-deadline-budgets.md) | Why can p99 degrade despite adequate mean capacity? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. One percentile cannot describe a distributed request](tail-latency-fanout-and-deadline-budgets.md#1-one-percentile-cannot-describe-a-distributed-request).
- [2. Draw the critical path and distinguish parallel from serial](tail-latency-fanout-and-deadline-budgets.md#2-draw-the-critical-path-and-distinguish-parallel-from-serial).
- [6. Worked decision: retain, hedge, or split?](tail-latency-fanout-and-deadline-budgets.md#6-worked-decision-retain-hedge-or-split).
- [7. Source-to-claim ledger and review boundary](tail-latency-fanout-and-deadline-budgets.md#7-source-to-claim-ledger-and-review-boundary).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C03 — Load-test methods and benchmark validity](../c03/README.md) |
| Next | [V07/C05 — Overload protection and graceful degradation](../c05/README.md) |
| Prerequisite | [V07/C03 — Load-test methods and benchmark validity](../c03/README.md) |
| Source reading | [Page-local evidence and versions](tail-latency-fanout-and-deadline-budgets.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
