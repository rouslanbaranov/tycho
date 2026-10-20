---
metadata_version: 1
id: "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c02/README.md"
title: "V07/C02 — Contention, saturation and scaling laws"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "When does coordination dominate additional capacity?"
route_hints:
  questions:
    - "When does coordination dominate additional capacity?"
  prerequisites:
    - "tycho.chapter.e365b78505784c20a4f3d72fe7904d9b"
  related_ids:
    - "tycho.chapter.e436af815dc442f694deb55966077d9e"
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
updated_at: "2026-10-20"
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

| Page | Owning question |
|---|---|
| [Contention, saturation and scalability laws: distinguishing capacity limits](contention-saturation-and-scaling-laws.md) | When does coordination dominate additional capacity? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Concurrency, parallel execution and completed throughput differ](contention-saturation-and-scaling-laws.md#1-concurrency-parallel-execution-and-completed-throughput-differ).
- [2. Amdahl's conditional bound](contention-saturation-and-scaling-laws.md#2-amdahls-conditional-bound).
- [8. Evidence and limits](contention-saturation-and-scaling-laws.md#8-evidence-and-limits).
- [Applied M9 evidence: what transfers and what does not](contention-saturation-and-scaling-laws.md#applied-m9-evidence-what-transfers-and-what-does-not).

## Boundaries and further reading

- [V03/C05 — Thread, connection and buffer pools](../../v03/c05/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C01 — Queueing, Little's Law and measurement boundaries](../c01/README.md) |
| Next | [V07/C03 — Load-test methods and benchmark validity](../c03/README.md) |
| Prerequisite | [V07/C01 — Queueing, Little's Law and measurement boundaries](../c01/README.md) |
| Source reading | [Page-local evidence and versions](contention-saturation-and-scaling-laws.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
