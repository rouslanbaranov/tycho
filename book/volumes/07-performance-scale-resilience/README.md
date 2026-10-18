# Volume 07 — Performance, scale and resilience under load

## Purpose and mission

Understand how explicitly defined demand, execution capacity, queueing and resource constraints change system behavior before considering scaling patterns or infrastructure changes. Distinguish observed evidence, conditional mathematical models and hypothesis-driven experiments. A headline RPS or user count does **not** select an architecture.

This is the first *partially researched* volume; its overall scope remains a [draft question-driven outline](../../PROPOSED-STRUCTURE.md). Unwritten chapters and missing primary-source evidence are not represented as published links.

## Available researched material

| Engineering question | Canonical chapter/page | Evidence coverage | Remaining limits |
|---|---|---|---|
| What can be inferred about average in-flight work from arrival, throughput and residence time? | [Queueing, workload boundaries, and Little's Law](01-queueing-and-workload.md) | Kim & Whitt §§1–2.2, Grafana k6 open/closed model docs, Google SRE overload/cascading failure sections inspected | No empirical service measurements or complete capacity model |

## Planned, not yet authored

- Contention, coordination and scaling laws (proposed V07/C02)
- Benchmark validity, warmup and coordinated omission (V07/C03)
- Tail latency and fan-out (V07/C04)
- Admission, retries, load shedding and graceful degradation (V07/C05)
- Autoscaling, headroom and deployment placement (V07/C06)
- Capacity planning and full lifecycle cost (V07/C07)

## Related material

- [Workload and requirements profile](../../../authoring/models/requirements-workload-profile.md) — completed requirement-gathering method, not a throughput benchmark.
- [Pilot 01 research contract](../../../authoring/contracts/PILOT-01-queueing.md) — bounded question and evidence scope.
- [Editorial contract](../../../authoring/EDITORIAL-CONTRACT.md) — canonical explanatory and review conventions.

**Review status:** this volume entry and its first page are research drafts until their issue-specific PR passes mechanical verification. No independent human review or production testing is claimed.
