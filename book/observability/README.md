# Observability, tracing, lineage and audit

## Purpose and mission

This area explains how to measure user-visible service behavior, understand distributed execution and preserve distinct kinds of operational and data evidence. **Telemetry collection is not proof of business correctness**, and an audit record is not automatically interchangeable with a sampled trace or log.

## Canonical chapters

1. [Service-level indicators, objectives and error-budget decisions](service-level-indicators-objectives-and-alerts.md) — **V09/C01** user-visible eligible populations, SLI/SLO contracts, budgets, action/alert decisions and failure examples.
2. [Metrics ingestion, cardinality and time-series retention](metric-pipelines-cardinality-and-retention.md) — **V09/C02** telemetry representations, delta/cumulative temporality, ingestion/data-loss risks, TSDB cardinality/retention and original budget reasoning.
3. [Earlier combined SLO/metrics/TSDB research](metrics-slo-timeseries-architecture.md) — preserved **legacy research input**, no longer the exclusive primary chapter owner for either V09/C01 or V09/C02.
4. [Distributed tracing, context propagation and sampling](distributed-tracing-context-and-sampling.md) — **V09/C03** W3C trace context, parent/link semantics, sampling and trust-boundary limitations.
5. [Structured logs, authoritative audit and data lineage](logs-audit-and-data-lineage.md) — **V09/C04** OpenTelemetry log records, committed business audit versus sampled telemetry and OpenLineage flow concepts.
6. [Earlier combined tracing/log/audit research](trace-context-lineage-and-audit.md) — preserved historical manuscript for claim-by-claim reconciliation; not now the primary chapter owner.
7. [Incident response, containment and operational change](incident-response-and-operational-change.md) — V09/C06 original incident state machine, operator responsibilities, recovery and postmortem gates, with wholly synthetic scenarios.

## Question-driven reading

| Architecture question | Start here | Continue with |
|---|---|---|
| How do we define success and error budget for a user journey? | [SLIs, SLOs and budgets](service-level-indicators-objectives-and-alerts.md) | [Workload measurement](../performance/workload-profiles-and-capacity-experiments.md) |
| Why did metric-store cost increase unexpectedly? | [Metric pipelines and retention](metric-pipelines-cardinality-and-retention.md) | [Capacity controls](../performance/workload-profiles-and-capacity-experiments.md) |
| How can we link asynchronous jobs to original requests? | [Trace context and links](distributed-tracing-context-and-sampling.md) | [Durable outbox/events](../distributed/transactional-outbox-and-idempotency.md) |
| Is a sampled trace enough to prove an authorized state change? | [Trace versus audit](logs-audit-and-data-lineage.md) | [Transaction ownership](../distributed/transaction-isolation-and-sagas.md) |
| What input datasets produced this derived report? | [Data lineage](logs-audit-and-data-lineage.md) | [Stateful streams and CDC](../integration/stateful-stream-processing-and-cdc.md) |
| How do we contain an incident, verify recovery and avoid unsafe concurrent changes? | [Incident response](incident-response-and-operational-change.md) | [Disaster recovery](../deployment/multi-region-disaster-recovery-contracts.md) |

## Completeness boundary

The original combined telemetry and tracing chapters are preserved as research source material from [E14-11 #89](https://github.com/rouslanbaranov/tycho/issues/89). The examples and decision controls are educational proposals, not measured production behavior, installed collectors, executed traces, retained audit evidence or independent review. Security and authorization mechanisms are developed separately under the subsequent security/synthesis chapter work.


**Canonical ownership note:** the two new V09/C01 and V09/C02 chapter drafts deliberately split *user-experience/SLO decision semantics* from *measurement processing/retention*. Their former shared source remains available for exact claim reconciliation. Neither new chapter is independently accepted or runtime-tested.

The V09/C03 and V09/C04 owners now have different primary manuscript files. The original combined page is retained to verify that technical facts/citations survive a proper editorial migration. **Neither new chapter has independent expert review or runtime validation.**
