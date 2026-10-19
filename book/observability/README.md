# Observability, tracing, lineage and audit

## Purpose and mission

This area explains how to measure user-visible service behavior, understand distributed execution and preserve distinct kinds of operational and data evidence. **Telemetry collection is not proof of business correctness**, and an audit record is not automatically interchangeable with a sampled trace or log.

## Canonical chapters

1. [Metrics architecture, SLOs, collection and time-series retention](metrics-slo-timeseries-architecture.md) — user-level indicators, metric data types/temporality, OpenTelemetry collection, Prometheus, TSDB retention, cardinality cost and alert/action gates.
2. [Distributed tracing, structured logs, data lineage and trustworthy audit](trace-context-lineage-and-audit.md) — W3C context propagation, sampling and async links, OTel log model, OpenLineage jobs/datasets/facets and the distinct durability/access assumptions of authoritative audit events.
3. [Incident response, containment and operational change](incident-response-and-operational-change.md) — V09/C06 original incident state machine, operator responsibilities, recovery and postmortem gates, with wholly synthetic scenarios.

## Question-driven reading

| Architecture question | Start here | Continue with |
|---|---|---|
| How do we define success and error budget for a user journey? | [Metrics and SLOs](metrics-slo-timeseries-architecture.md) | [Workload measurement](../performance/workload-profiles-and-capacity-experiments.md) |
| Why did metric-store cost increase unexpectedly? | [Cardinality and TSDB retention](metrics-slo-timeseries-architecture.md) | [Capacity controls](../performance/workload-profiles-and-capacity-experiments.md) |
| How can we link asynchronous jobs to original requests? | [Trace context and links](trace-context-lineage-and-audit.md) | [Durable outbox/events](../distributed/transactional-outbox-and-idempotency.md) |
| Is a sampled trace enough to prove an authorized state change? | [Trace versus audit](trace-context-lineage-and-audit.md) | [Transaction ownership](../distributed/transaction-isolation-and-sagas.md) |
| What input datasets produced this derived report? | [Data lineage](trace-context-lineage-and-audit.md) | [Stateful streams and CDC](../integration/stateful-stream-processing-and-cdc.md) |
| How do we contain an incident, verify recovery and avoid unsafe concurrent changes? | [Incident response](incident-response-and-operational-change.md) | [Disaster recovery](../deployment/multi-region-disaster-recovery-contracts.md) |

## Completeness boundary

The initial telemetry chapters are original manuscript for [E14-11 #89](https://github.com/rouslanbaranov/tycho/issues/89). The examples and decision controls are educational proposals, not measured production behavior, installed collectors, executed traces, retained audit evidence or independent review. Security and authorization mechanisms are developed separately under the subsequent security/synthesis chapter work.
