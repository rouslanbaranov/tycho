---
metadata_version: 1
id: "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c03/README.md"
title: "V07/C03 — Load-test methods and benchmark validity"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do open/closed arrivals, warmup and coordinated omission bias conclusions?"
route_hints:
  questions:
    - "How do open/closed arrivals, warmup and coordinated omission bias conclusions?"
  prerequisites:
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
  related_ids: []
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.sre-overload"
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

# V07/C03 — Load-test methods and benchmark validity

## Purpose and mission

How do open/closed arrivals, warmup and coordinated omission bias conclusions? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Choose an arrival model, warm-up policy and outcome accounting that preserve the workload being tested.

A closed-loop generator can reduce offered demand when the system slows, masking the backlog an external arrival stream would create. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

| Page | Owning question |
|---|---|
| [Load-test methodology, generator validity and defensible benchmark evidence](load-testing-and-benchmark-validity.md) | How do open/closed arrivals, warmup and coordinated omission bias conclusions? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Write the experiment claim before starting a load generator](load-testing-and-benchmark-validity.md#1-write-the-experiment-claim-before-starting-a-load-generator).
- [2. Open versus closed arrivals: the generator can hide degradation](load-testing-and-benchmark-validity.md#2-open-versus-closed-arrivals-the-generator-can-hide-degradation).
- [6. Decide from distributions, invariants and cost together](load-testing-and-benchmark-validity.md#6-decide-from-distributions-invariants-and-cost-together).
- [7. Public source ledger and limitations](load-testing-and-benchmark-validity.md#7-public-source-ledger-and-limitations).

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C02 — Contention, saturation and scaling laws](../c02/README.md) |
| Next | [V07/C04 — Tail latency, fan-out and time budgets](../c04/README.md) |
| Prerequisite | [V07/C02 — Contention, saturation and scaling laws](../c02/README.md) |
| Source reading | [Page-local evidence and versions](load-testing-and-benchmark-validity.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.
