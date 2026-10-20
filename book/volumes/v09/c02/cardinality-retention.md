---
metadata_version: 1
id: "tycho.page.03bdffc1632345f390c2e845b52a3eb0"
kind: "page"
parent_id: "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
canonical_path: "book/volumes/v09/c02/cardinality-retention.md"
title: "Cardinality, retention and lost information"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Which labels and aggregation choices change cost, privacy and diagnostic meaning?"
route_hints:
  questions:
    - "Which labels and aggregation choices change cost, privacy and diagnostic meaning?"
  prerequisites:
    - "tycho.page.ecb28b2c14af4100b2d31e8f2aafcf56"
  related_ids:
    - "tycho.chapter.ef166b5f7d76454ca4c8a685c6ce033e"
    - "tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "cardinality"
    - "retention"
evidence_scope:
  source_ids:
    - "src.otel-metrics-model"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Cardinality, retention and lost information

**Owning question:** Which labels and aggregation choices change cost, privacy and diagnostic meaning?

This page belongs to [V09/C02 — Metrics ingestion, cardinality and time-series storage](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:4 -->
## 4. Cardinality is multiplicative and architectural

Metric series identity commonly combines name and distinct label/attribute value sets. A convenient label such as a unique request ID, customer ID, trace ID or rapidly rotating ephemeral resource ID can create very many series with expensive indexing and retention and may leak sensitive data.

**Fully hypothetical arithmetic:** suppose one metric has 12 routes, 5 method/outcome groupings, 3 regions, and 40 independently emitting application instances, with all combinations present. Then its *illustrative* upper product is 12 × 5 × 3 × 40 = **7,200 series** before considering per-instance process recycling, per-tenant/URL labels or histogram buckets. With 20 classic histogram buckets per series, additional cumulative buckets, counts and sums increase the number of Prometheus float time series further. This calculation is a **model**; it is not a measured TSDB footprint or actual sample rate.

Cardinality is not the same as volume: 7,200 series scraped every 15 seconds generate different ingest/storage costs from the same series sampled every minute. Metrics type, compression, retention, index overhead, query fan-out and multi-region replication change resource costs.

**Design guidance:**
- Prefer bounded route templates and explicit status classes to raw URLs.
- Never publish secrets, unique tokens or personal identifiers as metric labels.
- Make label cardinality a reviewable instrumentation constraint with known worst cases.
- Use logs or traces with access controls for high-detail correlation rather than making one metric series per user.
- Bound per-tenant metrics and index privileges; separate access scopes.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:5 -->
## 5. Aggregation loses information by design

Rollups and downsampling can reduce storage while preserving some statistics. But averaging percentiles across groups is generally invalid; deleting buckets removes resolution for later quantile estimation; aggregating tenants can hide fairness and authorization failures. A sum and count can reconstruct the mean under compatible populations; they cannot reconstruct an arbitrary high-percentile distribution.

Choose retention from the question to answer: real-time alert, incident diagnosis, historical capacity trend or audit need. **An audit obligation cannot be satisfied simply by retaining sampled telemetry**, particularly when legal/business effects require complete durable event records.

The pipeline must record where transform loss occurs. For example, a daily series average can hide a 10-minute queue crisis; a histogram aggregated without compatible bucket boundaries can misrepresent the merged distribution.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:6 -->
## 6. Failure modes and operational economics

| Failure | Potential false conclusion | Required observability/repair |
|---|---|---|
| Scrape/export failure | Zero errors in an empty time series means full availability | Track sample freshness, target health and explicit unknown data |
| Duplicate cumulative stream | Throughput inexplicably doubled | Source/writer identity and temporality-aware deduplication |
| Cardinality explosion | Ingestion/TSDB saturation and dropped samples | Series growth and attribute-budget guard |
| Expired retention | Past incident looks clean because data vanished | Record known retention and separate long-lived source/audit evidence |
| Misconfigured downsampling | p99 appears improved | Verify histogram/quantile mathematics and preserved boundary |
| Storage unavailability | Alerts silently not evaluated | Independent monitor for pipeline health and fail-safe response policy |
| Cross-scope metric disclosure | Tenant/resource metadata leaks | Authorization over queries, labels and dashboards |

Metrics ingestion cost also includes collector resources, compression, scrape network, hot storage, query concurrency, replication, archive and operational on-call. A vendor's advertised storage price alone is not the full budget. Cost should be compared against how much a metric actually improves user-level decisions rather than retaining every raw label indefinitely.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53:7 -->
## 7. Original synthetic architectural choice

A fictional public library catalogue needs request-success and latency metrics plus a 30-day capacity trend. Two candidates:
- **A:** bounded route/status histograms and counters plus a small set of resource/queue gauges, retained at appropriate short/long resolutions.
- **B:** raw URL + arbitrary client ID as labels on every metric, with full-resolution indefinite retention.

B may seem richer but can create unbounded series and sensitive metadata. A is a **conditionally better starting design**, provided the selected labels support needed error budget and tenant/service diagnosis. If detailed per-entity investigations are required, use controlled logs/traces with separate access/retention rather than unlimited metrics labels.

**Falsifiable test (not run):** generate known bounded route/status combinations, inject random client IDs, restart a producer, duplicate exports, drop one collection interval and replay timestamps. Compare series count, ingest resource budget, SLI numerical semantics, query correctness and exposure controls. There is no test data or result in this chapter.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](metric-semantics.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](metric-pipelines-cardinality-and-retention.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
