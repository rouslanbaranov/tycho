---
metadata_version: 1
id: "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
kind: "chapter"
parent_id: "tycho.volume.4a94b1e6f8234841afaa51af14330627"
canonical_path: "book/volumes/v09/c02/README.md"
title: "V09/C02 — Metrics ingestion, cardinality and time-series storage"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How do scrape/push, temporality, labels, retention and scale interact? The reading route separates 2 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How do scrape/push, temporality, labels, retention and scale interact?"
  prerequisites:
    - "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
  related_ids:
    - "tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53"
    - "tycho.page.ecb28b2c14af4100b2d31e8f2aafcf56"
    - "tycho.page.03bdffc1632345f390c2e845b52a3eb0"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.otel-metrics-model"
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

# V09/C02 — Metrics ingestion, cardinality and time-series storage

## Purpose and mission

How do scrape/push, temporality, labels, retention and scale interact? This chapter owns that question within observability, security and operational architecture. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Make telemetry temporality, aggregation, cardinality, retention and loss visible in the metric contract.

An unbounded label can multiply storage and disclose identifiers; aggregation cannot reconstruct distinctions already discarded. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](metric-pipelines-cardinality-and-retention.md) | How do scrape/push, temporality, labels, retention and scale interact? |
| [Metric transport, types and temporality](metric-semantics.md) | Which reset and aggregation semantics survive collection and storage? |
| [Cardinality, retention and lost information](cardinality-retention.md) | Which labels and aggregation choices change cost, privacy and diagnostic meaning? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V09 — Observability, security and operational architecture](../README.md) |
| Previous | [V09/C01 — SLIs, SLOs and error budgets](../c01/README.md) |
| Next | [V09/C03 — Distributed tracing and propagation](../c03/README.md) |
| Prerequisite | [V09/C01 — SLIs, SLOs and error budgets](../c01/README.md) |
| Source reading | [Page-local evidence and versions](metric-pipelines-cardinality-and-retention.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:9 -->
## 8. Public evidence, caveats and navigation

| Independently inspected public source | Narrow support | What remains unproven |
|---|---|---|
| [OpenTelemetry Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/) | Sums/gauges/histograms, delta/cumulative temporality, timestamps and translation constraints | Conformance of invented collector deployment |
| [Prometheus Metric Types](https://prometheus.io/docs/concepts/metric_types/) | Counters, gauges, classic/native histograms, summaries and version-related aggregation cautions | Observed TSDB cost or configured instance behavior |
| [Tycho original metrics/SLO research](../../../observability/metrics-slo-timeseries-architecture.md) | Earlier combined researched mechanisms and hypothetical alert controls | Independently accepted canonical split |

Everything here is original general System Design prose and wholly fictional examples. No data, measured cost, series count, alerts, collector or metric backend was actually generated. The old combined research article is **preserved** as supporting source while the V09/C01 and V09/C02 chapter ownership is separated. Further claim-level source and editorial review is required before release.

**Navigation:** proposed **V09/C02** in [planned contents](../../../PROPOSED-STRUCTURE.md), [observability landing](../../../observability/README.md); related [SLIs and error budgets](../c01/service-level-indicators-objectives-and-alerts.md), [tracing and audit](../../../observability/trace-context-lineage-and-audit.md), [capacity planning](../../v07/c07/capacity-planning-and-cost-performance.md).
<!-- /tycho-question-source -->
