---
metadata_version: 1
id: "tycho.landing.b7ea8fb13ebb4079af2333e475f97106"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/observability/README.md"
title: "Observability, tracing, lineage and audit"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "Reader entry for Observability, tracing, lineage and audit. Scope includes Canonical chapters; Question-driven reading; Completeness boundary."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Observability, tracing, lineage and audit?"
  prerequisites: []
  related_ids:
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
    - "tycho.page.61b76bbbef8b42de8cc8603a5bc9bf53"
    - "tycho.page.1c7350e3bc17483ba18f201d02727aea"
    - "tycho.page.f921597aae854c6996459fc025a9bca3"
    - "tycho.page.436c2b22dc9e47acaaca7d18fadb511c"
    - "tycho.page.6b9a3f5c7bae455ab4f56f151f17b406"
    - "tycho.page.d87f9ba3852b49ee8188d150bb679716"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.a2c47a0850154eaa95e1eb97e23f9c71"
    - "tycho.page.2536d18422944e27abe4ea8549beb9ab"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Observability"
    - "tracing"
    - "lineage"
    - "and"
    - "audit"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
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

# Observability, tracing, lineage and audit

## Purpose and mission

This area explains how to measure user-visible service behavior, understand distributed execution and preserve distinct kinds of operational and data evidence. **Telemetry collection is not proof of business correctness**, and an audit record is not automatically interchangeable with a sampled trace or log.

## Canonical chapters

1. [Service-level indicators, objectives and error-budget decisions](../volumes/v09/c01/service-level-indicators-objectives-and-alerts.md) — **V09/C01** user-visible eligible populations, SLI/SLO contracts, budgets, action/alert decisions and failure examples.
2. [Metrics ingestion, cardinality and time-series retention](../volumes/v09/c02/metric-pipelines-cardinality-and-retention.md) — **V09/C02** telemetry representations, delta/cumulative temporality, ingestion/data-loss risks, TSDB cardinality/retention and original budget reasoning.
3. [Earlier combined SLO/metrics/TSDB research](metrics-slo-timeseries-architecture.md) — preserved **legacy research input**, no longer the exclusive primary chapter owner for either V09/C01 or V09/C02.
4. [Distributed tracing, context propagation and sampling](../volumes/v09/c03/distributed-tracing-context-and-sampling.md) — **V09/C03** W3C trace context, parent/link semantics, sampling and trust-boundary limitations.
5. [Structured logs, authoritative audit and data lineage](../volumes/v09/c04/logs-audit-and-data-lineage.md) — **V09/C04** OpenTelemetry log records, committed business audit versus sampled telemetry and OpenLineage flow concepts.
6. [Earlier combined tracing/log/audit research](trace-context-lineage-and-audit.md) — preserved historical manuscript for claim-by-claim reconciliation; not now the primary chapter owner.
7. [Incident response, containment and operational change](../volumes/v09/c06/incident-response-and-operational-change.md) — V09/C06 original incident state machine, operator responsibilities, recovery and postmortem gates, with wholly synthetic scenarios.

## Question-driven reading

| Architecture question | Start here | Continue with |
|---|---|---|
| How do we define success and error budget for a user journey? | [SLIs, SLOs and budgets](../volumes/v09/c01/service-level-indicators-objectives-and-alerts.md) | [Workload measurement](../performance/workload-profiles-and-capacity-experiments.md) |
| Why did metric-store cost increase unexpectedly? | [Metric pipelines and retention](../volumes/v09/c02/metric-pipelines-cardinality-and-retention.md) | [Capacity controls](../performance/workload-profiles-and-capacity-experiments.md) |
| How can we link asynchronous jobs to original requests? | [Trace context and links](../volumes/v09/c03/distributed-tracing-context-and-sampling.md) | [Durable outbox/events](../distributed/transactional-outbox-and-idempotency.md) |
| Is a sampled trace enough to prove an authorized state change? | [Trace versus audit](../volumes/v09/c04/logs-audit-and-data-lineage.md) | [Transaction ownership](../volumes/v04/c03/transaction-isolation-and-sagas.md) |
| What input datasets produced this derived report? | [Data lineage](../volumes/v09/c04/logs-audit-and-data-lineage.md) | [Stateful streams and CDC](../volumes/v04/c08/stateful-stream-processing-and-cdc.md) |
| How do we contain an incident, verify recovery and avoid unsafe concurrent changes? | [Incident response](../volumes/v09/c06/incident-response-and-operational-change.md) | [Disaster recovery](../deployment/multi-region-disaster-recovery-contracts.md) |

## Completeness boundary

The original combined telemetry and tracing chapters are preserved as research source material from [E14-11 #89](https://github.com/rouslanbaranov/tycho/issues/89). The examples and decision controls are educational proposals, not measured production behavior, installed collectors, executed traces, retained audit evidence or independent review. Security and authorization mechanisms are developed separately under the subsequent security/synthesis chapter work.


**Canonical ownership note:** the two new V09/C01 and V09/C02 chapter drafts deliberately split *user-experience/SLO decision semantics* from *measurement processing/retention*. Their former shared source remains available for exact claim reconciliation. Neither new chapter is independently accepted or runtime-tested.

The V09/C03 and V09/C04 owners now have different primary manuscript files. The original combined page is retained to verify that technical facts/citations survive a proper editorial migration. **Neither new chapter has independent expert review or runtime validation.**
