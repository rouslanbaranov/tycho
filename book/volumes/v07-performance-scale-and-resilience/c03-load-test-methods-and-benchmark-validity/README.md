---
metadata_version: 1
id: "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c03-load-test-methods-and-benchmark-validity/README.md"
title: "V07/C03 — Load-test methods and benchmark validity"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do open/closed arrivals, warmup and coordinated omission bias conclusions? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do open/closed arrivals, warmup and coordinated omission bias conclusions?"
  prerequisites:
    - "tycho.chapter.4cbc9e1582404965b696a63b79a66e93"
  related_ids:
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.page.bfa3a283746b42998825234aca63b101"
    - "tycho.page.180a25e8e7504ef4aa52257f76dbd1a8"
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

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](load-testing-and-benchmark-validity.md) | How do open/closed arrivals, warmup and coordinated omission bias conclusions? |
| [Experiment claims, arrival models and denominators](arrival-design.md) | Which offered workload must a load generator preserve while the system slows? |
| [Confounders, fault injection and acceptance](benchmark-controls.md) | Which invariant and distribution must remain comparable across benchmark variants? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C02 — Contention, saturation and scaling laws](../c02-contention-saturation-and-scaling-laws/README.md) |
| Next | [V07/C04 — Tail latency, fan-out and time budgets](../c04-tail-latency-fan-out-and-time-budgets/README.md) |
| Prerequisite | [V07/C02 — Contention, saturation and scaling laws](../c02-contention-saturation-and-scaling-laws/README.md) |
| Source reading | [Page-local evidence and versions](load-testing-and-benchmark-validity.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:7 -->
## 7. Public source ledger and limitations

| Independently reviewed public source | Exact applicable scope | Not established |
|---|---|---|
| [Grafana k6: open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) | Iterator/arrival coupling and executor distinctions | That a test with k6 sustained its configured rate |
| [Grafana k6: dropped iterations](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/) | Unsent iterations when VU capacity is insufficient and multiple causal interpretations | A universal correction or numerical service throughput ceiling |
| [HdrHistogram: AbstractHistogram correction API](https://github.com/HdrHistogram/HdrHistogram/blob/master/src/main/java/org/HdrHistogram/AbstractHistogram.java) | Modeling a missing-interval series with an explicit expected interval | Measured latency for requests not actually issued |
| [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/) | Capacity-aware overload and admission controls | Any particular project's safe request threshold |

The example reading-list system, arithmetic, diagrams, proposed experiments and matrix are all **original synthetic material**. These sources describe methods; they do not prove any Tycho benchmark occurred. Full link/anchor verification, dataset fixtures, rendering, repeatability exercises and independent technical/statistical acceptance remain open.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:8 -->
## Navigation

- Proposed V07/C03; current [performance topic landing](../../../performance/README.md).
- Prerequisite: [Workload and capacity experiment method](../../../performance/workload-profiles-and-capacity-experiments.md).
- Related: [Queueing and Little's Law](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md), [tail latency](../c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md), [autoscaling feedback](../c06-horizontal-vertical-scaling-and-autoscaling-delay/autoscaling-lag-and-capacity-limits.md), and [pattern selection](../../v10-decision-support-and-modernization/c03-pattern-applicability-and-contraindications/pattern-applicability-and-contraindications.md).
<!-- /tycho-question-source -->
