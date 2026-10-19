# Metrics architecture, SLOs, collection and time-series retention

> Tycho E14-11 [issue #89](https://github.com/rouslanbaranov/tycho/issues/89), original source-linked manuscript, 2026-10-19. No actual SLO measurements, telemetry pipeline, deployed collector, load test, audit or independent human review is asserted.

## Purpose and mission

Monitoring is an architecture with capacity, data quality, cost and failure modes of its own. A user-facing availability SLO cannot be established from CPU usage, and an exponentially large series space cannot be fixed merely by increasing storage retention.

**Question:** How should the system collect, aggregate, retain and alert on measurable user outcomes without making telemetry itself an unbounded workload?

Read with [workload measurements](../performance/workload-profiles-and-capacity-experiments.md) and [trace/lineage/audit boundaries](trace-context-lineage-and-audit.md).

## 1. Specify service-level meaning before signal collection

An SLI is a precisely counted and windowed property of user-relevant service behavior. An SLO is a selected target over that property and observation window; it is not a measured result unless actual events are recorded under the declared boundary.

For a fictional workshop registration system, a useful availability SLI could be:

successful eligible registration outcomes / eligible registration attempts

But the metric is undefined without specifying: whether duplicate idempotent retries count once, whether client cancellation counts, how admission rejection is classified, whether timeout after DB commit is success or uncertain, how malicious/invalid input is excluded, and how missing telemetry is treated.

A latency objective requires endpoint, time budget, observation point and outcome population. The p99 of a globally pooled histogram is **not** an average of per-instance p99 values. Retries may create several low-level requests per logical business attempt; do not confuse HTTP request metrics with operation outcomes.

For an availability target SLO = 99.9% over a defined window, permitted error fraction is 0.1% of eligible attempts. A theoretical monthly time-equivalent budget is not a measured downtime allowance for an event-count-based SLI. Specify whether the denominator is requests, service time, or user journeys.

## 2. Telemetry collection is a pipeline, not a database write

| Stage | Responsibility | Failure and scaling question |
|---|---|---|
| Instrumentation | Produce counters, gauges, histograms, spans and structured events at well-defined semantic boundaries | What is actually measured, what is dropped and at what cost? |
| Receiver / scrape | Obtain samples or accept pushed telemetry with identity and ingestion timing | Which actors can reach the endpoint? Is source timestamp trusted? |
| Processor | Enrich, transform, batch, filter, sample and limit memory | Can labels explode or privacy leak before controls apply? |
| Exporter / queue | Deliver telemetry to one or more stores; retry and backpressure | Can backlog, duplicate transport or outage exhaust resources? |
| Storage / query | Time-series blocks, indexes, retention and downsampling | How much disk, label index and query CPU are needed? |
| Alert/action | Evaluate user-impact conditions and route responsibility | Is there enough independent corroboration to automate recovery? |

OpenTelemetry Collector's official component description distinguishes receivers, processors, exporters, connectors and extensions. [E01] A pipeline may drop or transform signals, and it is not proof of end-to-end lossless delivery by default.

### Original topology

Application instances → local or remote telemetry receivers → bounded collector processors/batches → durable or best-effort transport according to declared policy → metrics/trace/log storage → queries and alerts.

This diagram does not imply all telemetry is durable. An incident may saturate the collector and remove exactly the samples needed to diagnose the incident; monitor collection queue depth, dropped points, exporter errors, scrape freshness and query availability as independent service health.

## 3. Pull, push and temporality

In a pull model such as a Prometheus scrape, the collector initiates periodic reads of target endpoints. Failure of discovery, reachability or scrape duration can produce gaps. In push telemetry, the producer/agent may buffer and export, but batching and retry can lead to duplicates, delays or loss depending on backpressure and storage guarantees.

The OpenTelemetry Metrics Data Model distinguishes delta and cumulative aggregation temporality, resource/instrument identity, sums, gauges and histograms. [E02] Converting between delta and cumulative can be lossy or require maintaining per-series state; a reset, change in start timestamp or temporality mismatch must not be misinterpreted as genuine negative work.

- **Counter / monotonic sum:** cumulative counts such as request attempts; calculate rates with reset handling and a valid window.
- **Gauge:** observed current value such as worker count; interpolation and missing samples matter.
- **Histogram:** bucket counts and total observations representing a distribution. Buckets determine possible quantile approximations, not actual individual request traces.
- **Summary and sketch algorithms:** client-side quantile estimates may not merge correctly across instances; prefer explicit models whose aggregation rules match desired fleet-wide questions.

For each metric document unit (seconds versus milliseconds, bytes), labels, monotonicity, reset semantics and observation start/end time. Labels are not free annotations: they create independent time series.

## 4. Cardinality and storage cost

For a metric family with independent label dimensions of sizes A, B and C, the **potential** number of series is A × B × C for every realized combination. This is an upper-bound approximation when combinations are sparse, but adding per-user or per-request IDs often makes series growth proportional to traffic.

Example, entirely synthetic: 8 endpoints × 5 methods × 6 status classes × 30 replicas creates up to 7,200 distinct series for one metric family, assuming every combination occurs. Adding a user ID with 100,000 values could produce hundreds of millions of combinations in principle. The number is an illustrative multiplication, not measured cardinality.

Official Prometheus instrumentation guidance warns against high-cardinality labels and recommends controlling unbounded dimensions. [E03] Put request ID, session ID or user ID in **appropriately protected logs/traces** rather than raw metrics labels. Use bounded route templates rather than raw paths, and explicitly define tenant aggregation/redaction policy.

Time-series storage costs include samples, series index entries, compression, WAL, retention, query working sets, remote-write bandwidth and compaction duplication. Prometheus TSDB documents block compaction, time/size retention and the need for temporary disk headroom during compaction. [E04] Retention time alone is not a safe index-size forecast.

A first budget should estimate:
- active series by metric family and bounded dimension,
- observed scrape/export interval and payload bytes,
- ingestion samples/second and burst ratio,
- raw and compressed storage separately,
- compaction and WAL headroom,
- remote-write egress, retries, duplicate/replay,
- query concurrency and long-range analytical cost,
- dropped/late sample policy.

## 5. Downsampling, recording rules and semantic loss

Rolling raw 10-second latency buckets into hourly averages may erase evidence of short-lived user-visible incidents. A recording rule computes a named transform and may reduce expensive query work, but its sampling window and cardinality requirements still matter.

An hourly mean of per-host means is not generally the fleet-wide mean unless correctly weighted by observation counts. A p99 computed from 5-minute buckets cannot be averaged to obtain the day's p99. If retaining coarse histograms, the chosen bucket schema constrains the precision of reconstituted percentiles.

Retention should reflect distinct questions:
- high-resolution operational diagnosis over short periods,
- user-SLO accountability and longer-range trends,
- capacity/performance regression comparison,
- audited business event reconstruction (which belongs in a separate authoritative audit store, not implicitly a metric backend).

Record what each retention tier *cannot* answer after downsampling. Log and trace correlation are separate tasks, not substitutes for lost metric samples.

## 6. Alert design and overload safety

Useful alerts connect a measurable user-impact or imminent irreversible resource risk to an actionable response. Examples: sustained eligible success-rate decline, rising high-percentile latency at stable offered demand, saturated pool with queue-age growth, stalled telemetry exporter with sample gaps, or exhausted TSDB disk headroom.

Avoid paging on every instantaneous CPU spike. Every alert needs:
1. eligible population and evaluation window,
2. enough observations / confidence to distinguish low traffic,
3. user outcome or concrete impending resource failure,
4. owner and escalation pathway,
5. runbook evidence and what will *falsify* the hypothesis,
6. explicit suppression/muting during controlled maintenance without hiding real incidents.

An exporter outage may look like a quiet service; missing metrics are themselves an observable incident. Red/green dashboard colors do not establish that instrumentation covers every path.

## 7. Synthetic operational failure and decision

Assume, for a fictional application, that a new release adds raw request identifiers as labels to several metrics. On a sustained traffic spike, series creation grows, memory/CPU pressure rises in collectors and storage. Samples drop, even as the business service's latency increases.

The first corrective action is to **stop unbounded cardinality at instrumentation/collector boundaries**, preserve allowed diagnostic trace/log detail elsewhere, inspect missing-sample markers, and measure telemetry cost under the same offered workload. Simply scaling the metrics store risks an expensive recurring failure.

**Architecture choice:** a single local scraper/TSDB may suffice for an initially bounded workload and retention objective; a remote-write and distributed query tier becomes plausible when retention, isolation, durability and query/ingestion demands justify its operating costs. Do not prescribe a cluster based on unverified endpoints-per-second.

## 8. Exact public evidence and missing checks

| ID | Source inspected 2026-10-19 | Scope and limitation |
|---|---|---|
| E01 | [OpenTelemetry Collector Components](https://opentelemetry.io/docs/collector/components/), receiver/processor/exporter/connector/extension types | Pipeline building blocks, not proof of durable end-to-end collection |
| E02 | [OpenTelemetry Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/), metrics types, identity and temporality sections | Semantic shape for data streams, not observed platform cost |
| E03 | [Prometheus Instrumentation Best Practices](https://prometheus.io/docs/practices/instrumentation/), cardinality guidance | Advisory label selection, not a universal numerical ceiling |
| E04 | [Prometheus Storage](https://prometheus.io/docs/prometheus/latest/storage/), block compaction, WAL, retention flags | Storage mechanics, not measured retention/cost for the synthetic example |

No real metric store, trace backend, remote-write test, compaction benchmark, user-level SLI, alert response or independent expert review was executed. The chapter gives a conditional architecture and explicit experiments, not guaranteed sizing or availability.
