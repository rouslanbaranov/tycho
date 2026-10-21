---
metadata_version: 1
id: "tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53"
kind: "page"
parent_id: "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
canonical_path: "book/volumes/v09-observability-security-and-operations/c02-metrics-ingestion-cardinality-and-time-series-storage/metric-pipelines-cardinality-and-retention.md"
title: "Metrics ingestion, cardinality and time-series retention architecture"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Integrated question, original scenario and transfer limits for Metrics ingestion, cardinality and time-series storage. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do scrape/push, temporality, labels, retention and scale interact?"
  prerequisites: []
  related_ids:
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.1c7350e3bc17483ba18f201d02727aea"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
    - "tycho.page.5ae9f2c4b45842c7975fd32c252dc4d8"
    - "tycho.page.ecb28b2c14af4100b2d31e8f2aafcf56"
    - "tycho.page.03bdffc1632345f390c2e845b52a3eb0"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Metrics"
    - "ingestion"
    - "cardinality"
    - "and"
    - "time-series"
    - "retention"
    - "architecture"
evidence_scope:
  source_ids:
    - "src.otel-metrics-model"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:-1 -->

# Metrics ingestion, cardinality and time-series retention architecture

> **Tycho source-grounded System Design draft V09/C02, 2026-10-19.** OpenTelemetry and Prometheus public specifications support the narrow instrumentation and data-model descriptions. All pipelines, rate/budget figures and failure tests here are original hypothetical examples. No collector, database, remote-write service or runtime metric stream was deployed or exercised.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:0 -->
## Purpose and mission

A useful service-level indicator needs telemetry that preserves the intended meaning. Transport and storage choices determine what information survives collection, aggregation, label filtering, retention and backend failure. Even perfect dashboards cannot correct instrumentation that uses the wrong event denominator, while unbounded metric labels can consume substantial resources and expose sensitive identifiers.

This chapter owns **how signals are represented, transferred, stored and operated**. [SLIs, SLOs and error budgets](../c01-slis-slos-and-error-budgets/service-level-indicators-objectives-and-alerts.md) owns the user-visible definition and alert decision. [Tracing/log/audit](../../../observability/trace-context-lineage-and-audit.md) owns different evidence types.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:8 -->
## Engineering walkthrough — How one unbounded metric label multiplies storage

**Original synthetic metric:** a request-duration series records `route` (40 values), `status_class` (5), `zone` (3) and `tenant_id` (2,000). Ignoring labels added by instrumentation, the potential Cartesian product is `40 × 5 × 3 × 2,000 = 1,200,000` separate time series. Removing `tenant_id` reduces that theoretical combination count to `600`. These are *upper-bound dimensionality arithmetic*, not observed active series or a vendor price estimate.

At a purely hypothetical one sample per series every 15 seconds, a full million-plus active series would produce up to 80,000 samples/s; actual active combinations can be far lower and per-sample storage depends on compression, retention, replication and index layout. High-cardinality labels may leak tenant identity and consume query resources even when an app remains healthy.

| Pipeline boundary | Normal contract | Failure interpretation to reject |
|---|---|---|
| SDK/exporter | Counter/histogram semantics and bounded attributes | Missing samples imply no user traffic |
| Collector | Backpressure, aggregation, resource budgets | Dropped telemetry means errors disappeared |
| Time-series store | Retention and label query budget | A downsampled p99 equals p99 of original raw durations |
| Dashboard/alert | Distinguish reset, cumulative/delta and missing windows | Counter reset interpreted as negative successful requests |

The existing OpenTelemetry metric data model and Prometheus metric-type references define terminology; they do not certify a given collector's actual temporality conversion or cardinality footprint. A missing histogram bucket or restarted counter can make apparent rates nonsensical without explicit reset/missing-data handling.

**Proposed, unexecuted:** replay the same traffic with bounded route templates versus unbounded tenant/path labels; measure active series, ingestion memory, missing points, query time and retained bytes. Keep high-cardinality user IDs in access-controlled audit or trace context when justified, not automatically in globally aggregatable metric labels. A cheaper dashboard is not sufficient if it hides severe tail errors.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Make telemetry temporality, aggregation, cardinality, retention and loss visible in the metric contract.

An unbounded label can multiply storage and disclose identifiers; aggregation cannot reconstruct distinctions already discarded.

The detailed pages separate the mechanisms that make this decision conditional:

- [Metric transport, types and temporality](metric-semantics.md) — Which reset and aggregation semantics survive collection and storage?
- [Cardinality, retention and lost information](cardinality-retention.md) — Which labels and aggregation choices change cost, privacy and diagnostic meaning?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
