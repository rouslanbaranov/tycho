---
metadata_version: 1
id: "tycho.page.8c596999929c47e48af6a7a2896bb9b9"
kind: "page"
parent_id: "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
canonical_path: "book/volumes/v09-observability-security-and-operations/c01-slis-slos-and-error-budgets/budget-actions.md"
title: "Error-budget decisions and revisions"
topic_ids:
  - "observability"
perspectives:
  - "architecture"
  - "operations"
summary: "What action should a budget trigger and when should the objective be reconsidered?"
route_hints:
  questions:
    - "What action should a budget trigger and when should the objective be reconsidered?"
  prerequisites:
    - "tycho.page.447ffb82d30f4a6999855c0a261e9a2a"
  related_ids:
    - "tycho.chapter.16f93a5e11e845d5b4c01a9e6a25f0c7"
    - "tycho.page.c987c475cc5340bcb967f4b6f963b295"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "budget"
    - "actions"
evidence_scope:
  source_ids:
    - "src.sre"
    - "src.prometheus"
    - "src.aws-cloudwatch-synthetics"
    - "src.azure-app-insights-availability"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Bounded question from tycho.page.c987c475cc5340bcb967f4b6f963b295; exact
    inherited citation rows and limits remain in the chapter source ledger.
    The Synthetic Monitoring section binds four public units inspected on
    2026-10-31; src.azure-app-insights-availability is registered, and no
    promotion, sufficient coverage or owner acceptance is claimed. Source
    registration does not change the bounded coverage state.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-31"
source_inspection_date: null
content_verified_at: null
---
# Error-budget decisions and revisions

**Owning question:** What action should a budget trigger and when should the objective be reconsidered?

This page belongs to [V09/C01 — SLIs, SLOs and error budgets](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:4 -->
## 4. Burn rate and alerts are actions, not decorations

An error-budget burn rate compares observed bad-event consumption with the budget's expected consumption rate. A fast burn may need immediate intervention, but short windows can be noisy and long windows slow to detect severe faults.

The [Google SRE Workbook on alerting based on SLOs](https://sre.google/workbook/alerting-on-slos/) describes alert design around error-budget burn rates and time windows. This method does not imply universal thresholds, especially for services with intermittent traffic or where one incorrect operation is intolerable.

| Signal | Useful operational decision | Trap |
|---|---|---|
| Fast error-budget burn | Investigate impact and consider protecting capacity/halting rollout | Alert threshold selected without enough valid event samples |
| Sustained slow burn | Review problem history and release/quality trade-offs | Ignoring long-term harm because there is no loud incident |
| High p99 for one journey | Trace critical-path, queue and dependency wait | Inferring whole-product failure from one selected operation |
| Zero observed errors at idle time | Insufficient demand to validate reliability | Reporting “100% available” with no eligible operations |
| High CPU or pool occupancy | Supporting diagnosis and capacity control | Substituting resource usage for user correctness |
| Trace sampling dropped | Telemetry gap and reduced debugging confidence | Treating missing spans as proof no failures occurred |

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Synthetic Monitoring](../../v11-pattern-atlas/c11-security-operations/synthetic-monitoring.md#synthetic-monitoring) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:5 -->
## 5. An original synthetic error-budget decision

A hypothetical project owner set a 99.9% good-event target for a defined booking operation during a month. A release increases timeouts, and an operator proposes an automatic rollout pause.

A safe rule would:
1. Check that the event population is correct and the target window sufficiently sampled.
2. Compare logical operation outcomes, not simply network attempts.
3. Stop rollout if a mandatory correctness gate fails, **even with budget remaining**.
4. Use confirmed burn and impact to decide between mitigation, investigation or reversible rollback.
5. Verify that any recovery restores correct booked state rather than merely reducing HTTP errors.
6. Record the signal, source/alert version, decision and follow-up owner.

The action thresholds remain hypothetical. No PromQL query, SLO policy or alert was executed for this chapter.

```mermaid
flowchart TD
    U["Eligible user journey"] --> I["Outcome + duration SLI"]
    I --> O["Selected SLO / error-budget window"]
    O --> B{"Burn or hard correctness gate?"}
    B -->|Hard correctness fail| S["Contain / stop release regardless of budget"]
    B -->|Budget concern| R["Validate sampling + trigger named response"]
    B -->|Within target| C["Continue observation and validate data quality"]
    R --> V["Post-change user + state correctness check"]
```

**Text alternative:** a user journey produces an indicator, compared with a stated objective. A correctness failure always triggers its own mitigation; a budget alert must account for the event sample and leads to a verified response, not a purely cosmetic dashboard change.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c987c475cc5340bcb967f4b6f963b295:6 -->
## 6. SLOs need revision and contradiction handling

An old SLO may cease to represent user experience if a new API version changes which outcomes count as good, if retries are introduced or if the monitoring boundary shifts. Keep the numerator, denominator, units, target, data-source revision and effective date together.

A release can legitimately improve average response time while degrading the worst users. An unrelated region may hide under aggregate metrics; disaggregate by meaningful route/workload where needed without creating dangerous high-cardinality labels or data leakage. The [metrics ingestion/storage chapter](../c02-metrics-ingestion-cardinality-and-time-series-storage/metric-pipelines-cardinality-and-retention.md) owns the telemetry cost and cardinality mechanics.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](sli-population.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](service-level-indicators-objectives-and-alerts.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is
not the main subject of this page. They are synthetic design guidance, not
measured evidence, and they do not create a new source claim.

### Synthetic Monitoring

**Mechanism.** Synthetic monitoring exercises a representative user journey from outside
the service. Google SRE, "Monitoring Distributed Systems", defines black-box monitoring as
"Testing externally visible behavior as a user would see it" and notes that "only end-to-end
system tests can detect that you’re serving the wrong content." The Prometheus blackbox
exporter "allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP, ICMP and gRPC";
AWS CloudWatch Synthetics canaries "follow the same routes and perform the same actions as
a customer"; and Azure availability tests "send web requests to your application at regular
intervals". **Tycho reading:** a probe is a measurement contract over a named journey, not
a liveness shortcut, and a shallow endpoint ping is not evidence for a complete journey.

**Invariant.** It needs a safe identity, a journey definition, location and frequency
choices and a rule that separates probe failure from product failure. Prometheus "needs to
be passed the target as a parameter", resolves "the target hostname on every probe and
does not cache the result" and exposes `probe_success`; Azure applies its retry rule
"independently at each test location" and warns that availability tests use "shared IP
addresses", so a firewall must not rely on IP filtering alone. Add an origin header with a
safe identity and treat credential expiry as a configuration event. AWS runs canaries "on a
schedule". **Tycho rule:** bind who probes what, from where, how often, with which
identity, and what counts as success before the check is trusted.

**Failure and recovery.** The failure path is a probe that cannot authenticate or that
tests only a trivial path; rotate credentials, cover the critical journey and triage probe
noise separately. Azure retries a failed test and reports "only if three successive
attempts fail", yet notes that "about 80% of failures disappear on retry"; alerts are
enabled by default. AWS says canaries let you "discover issues before your customers do".
Prometheus exposes `probe_success` and debug output, and its security note says the
exporter "makes requests to any target it is given". **Tycho runbook:** page on
product-visible failure, keep credential-expiry alerts distinct from product alerts, and
re-run with debug before declaring an outage.

**Alternative.** Real-user monitoring is the alternative when actual traffic provides
enough coverage without synthetic load. Google SRE contrasts black-box with white-box
monitoring, which "depends on the ability to inspect the innards of the system, such as
logs or HTTP endpoints, with instrumentation." Azure tells operators that for nonpublic
endpoints they should "monitor an internal health signal from inside the network and
create log or metric alerts on that signal." **Tycho choice rule:** prefer a synthetic
probe only when no real traffic exercises the journey; prefer internal or real-user
signals when the probe cannot reach or safely authenticate to the path; reverse when probe
maintenance and noise exceed the detection benefit.

**Bound source limits.** Four public units were inspected on 2026-10-31: Google SRE,
"Monitoring Distributed Systems"; Prometheus, "Blackbox exporter"; AWS, "Synthetic
monitoring (canaries)"; and Azure, "Application Insights availability tests". The exact
units are:
<https://sre.google/sre-book/monitoring-distributed-systems/>,
<https://github.com/prometheus/blackbox_exporter>,
<https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html>
and
<https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability>.
The bound or retained records are `read.sre-book-blackbox-monitoring.2026-10-31`,
`read.prometheus-blackbox-exporter.2026-10-31`,
`read.aws-synthetics-canaries.2026-10-30`, and
`read.azure-app-insights-availability.2026-10-31`. They are living book, repository,
service-guide and how-to pages, not benchmarks, measurement standards or production
observations. The SRE chapter has no published version identifier; the Prometheus README
is pinned to commit `f9c2f47d4f7785652ed66e391618c2f7cea1b3c9`; the Azure page records a
source commit; the AWS page is a service overview. No probe, canary or availability test
was created or run. The real-user comparison, choice rule and runbook remain Tycho
guidance, not source claims.
