---
metadata_version: 1
id: "tycho.chapter.03ec5acf85e043a5a6d552a036bf4659"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09-observability-security-and-operations/c03-distributed-tracing-and-propagation/README.md"
title: "V09/C03 — Distributed tracing and propagation"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which context, sampling and async boundaries determine trace usefulness? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Which context, sampling and async boundaries determine trace usefulness?"
  prerequisites:
    - "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
  related_ids:
    - "tycho.chapter.49cb8db3af4e406ea6988c8e5e852acf"
    - "tycho.page.f921597aae854c6996459fc025a9bca3"
    - "tycho.page.aac0f46189b74948bedfc30a81ec80e5"
    - "tycho.page.bc30179a9cda4c12b9deb383e8751d47"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.trace-context"
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

# V09/C03 — Distributed tracing and propagation

## Purpose and mission

Which context, sampling and async boundaries determine trace usefulness? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Interpret traces as sampled, propagated observations with explicit trust and asynchronous boundaries.

A missing span does not prove no effect occurred, and untrusted baggage must not become an authorization decision. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](distributed-tracing-context-and-sampling.md) | Which context, sampling and async boundaries determine trace usefulness? |
| [Trace identity and causal interpretation](trace-causality.md) | What execution relationship can a span and its timing establish? |
| [Propagation, sampling and untrusted context](sampling-trust.md) | What does a missing span or forged context prevent a trace from proving? |

## Boundaries and further reading

- [V09/C04 — Logging, audit and lineage](../c04-logging-audit-and-lineage/README.md) owns the adjacent question; compare assumptions before transferring the conclusion.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C02 — Metrics ingestion, cardinality and time-series storage](../c02-metrics-ingestion-cardinality-and-time-series-storage/README.md) |
| Next | [V09/C04 — Logging, audit and lineage](../c04-logging-audit-and-lineage/README.md) |
| Prerequisite | [V09/C02 — Metrics ingestion, cardinality and time-series storage](../c02-metrics-ingestion-cardinality-and-time-series-storage/README.md) |
| Source reading | [Page-local evidence and versions](distributed-tracing-context-and-sampling.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.f921597aae854c6996459fc025a9bca3:7 -->
## 7. Public source ledger and nonclaims

| Public source read | Narrow support | Not proven |
|---|---|---|
| [W3C Trace Context Recommendation, 23 Nov 2021](https://www.w3.org/TR/trace-context/) | traceparent/tracestate propagation and privacy/security context | Actual interop between fictional services |
| [OpenTelemetry sampling concepts](https://opentelemetry.io/docs/concepts/sampling/) | Sampling approaches, trace-data selection limits | Recorded trace completeness or analytical p99 validity |
| [Tycho earlier tracing/logging research](../../../observability/trace-context-lineage-and-audit.md) | Prior cross-domain conceptual distinctions | Separate owner acceptance or collected evidence |

All example events, diagrams and tracing behaviors are hypothetical educational work. No tracing backend, software build, distributed request, review or sampling evaluation was performed. Former combined tracing/logging research remains preserved for claim-level editorial reconciliation, not reproduced in full.

**Navigation:** proposed **V09/C03** in [book outline](../../../PROPOSED-STRUCTURE.md), current [observability landing](../../../observability/README.md). Related [Metrics and SLOs](../c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md), [Audit and lineage](../c04-logging-audit-and-lineage/logs-audit-and-data-lineage.md), [Tail latency](../../v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md).
<!-- /tycho-question-source -->
