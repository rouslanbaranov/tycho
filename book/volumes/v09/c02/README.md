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
summary: "How do scrape/push, temporality, labels, retention and scale interact?"
route_hints:
  questions:
    - "How do scrape/push, temporality, labels, retention and scale interact?"
  prerequisites:
    - "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
  related_ids: []
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

| Page | Owning question |
|---|---|
| [Metrics ingestion, cardinality and time-series retention architecture](metric-pipelines-cardinality-and-retention.md) | How do scrape/push, temporality, labels, retention and scale interact? |

The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:

- [1. Separate measurement generation from retrieval](metric-pipelines-cardinality-and-retention.md#1-separate-measurement-generation-from-retrieval).
- [2. Measurement types and aggregation limitations](metric-pipelines-cardinality-and-retention.md#2-measurement-types-and-aggregation-limitations).
- [Engineering walkthrough — How one unbounded metric label multiplies storage](metric-pipelines-cardinality-and-retention.md#engineering-walkthrough-how-one-unbounded-metric-label-multiplies-storage).
- [8. Public evidence, caveats and navigation](metric-pipelines-cardinality-and-retention.md#8-public-evidence-caveats-and-navigation).

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
