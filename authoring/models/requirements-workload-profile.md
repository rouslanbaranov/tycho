# Requirements and workload profile model

Status: design contract v0.1; issue [#17](https://github.com/rouslanbaranov/tycho/issues/17); prepared 2026-10-18.
Scope: technology-neutral requirements and workload characterization for new designs and modernization assessments. It is **not** a decision engine, final metadata schema, benchmark, architecture recommendation or approved workload forecast.

## Purpose and readers

A product decision-maker, architect, developer, or AI agent can use one bounded profile to identify what a design must accomplish, what is merely preferred, which operational loads it must sustain, and which unknowns require evidence before selecting patterns. An architecture option should be compared against the same workload and measurable outcomes, rather than chosen by a user-count threshold.

Canonical owner of this model: this file. Use the [reusable template](../../templates/requirements-workload-profile.md); see the [original synthetic example](../../examples/synthetic-workshop-registration.md). Modernization baseline analysis is a separate deliverable of [#18](https://github.com/rouslanbaranov/tycho/issues/18).

## 1. Profile identity, scope and evidence

Each profile must identify the following, even if a value is unknown:

| Field | Meaning / recording rule |
|---|---|
| `profile_id` and `revision` | Locally stable identity and revision of the profile; not a claimed JSON Schema ID |
| `status` | Draft, evidence-under-review or approved by a *named* reviewer; never infer approval from a merge |
| `system_boundary` | User journeys and technical ingress/egress measured; distinguish client, edge, application, downstream and storage boundaries |
| `decision_context` | New system, change to existing system, or exploratory comparison, with explicit non-goals |
| `owner_and_stakeholders` | Responsible roles, business users, operators, security and external consumers |
| `reference_period` | Measurement start/end in time zone, weekday/season and representative peak duration |
| `assumption_state` | Measured, stakeholder requirement, model-derived estimate, scenario assumption or unknown |
| `evidence_pointer` | Exact section/metric/query and time window or versioned public source; unrestricted internal data is not admissible for Tycho |

Use an assumption register with IDs, uncertainty, required validation, owner and revisit trigger. Do not turn a dated measurement into a timeless platform guarantee.

## 2. Business outcomes, drivers and constraints

Define each required capability as an observable user outcome with actor, trigger, expected result, exclusions and priority. For each business outcome record metric, baseline (or unknown), target, assessment window, data source and who may approve trade-offs. Separate business metrics (e.g., completed registrations) from service objectives (e.g., successful request ratio).

| Classification | Decision behavior | Examples of allowed profile wording |
|---|---|---|
| **Hard constraint** | Candidate that demonstrably violates it is rejected; uncertainty means validate before accepting. Give rationale, boundary, owner and acceptance test. | No double allocation of the same seat; specified data retention; deadline; maximum recurring spend |
| **Preference / trade-off** | Compare viable candidates using weights or ordinal priority; uncertain results must remain uncertain. | Fewer operational components, easier local development, lower median cost |
| **Measurable quality requirement** | Stimulus and environment must be paired with response criteria. May itself be a hard gate or preference. | At a stated arrival mix and duration, at least 99% of eligible requests complete within 500 ms |
| **Assumption / unknown** | Never silently substitute a fact; add an evidence task. | Peak burst multiplier has not been observed |

When a preference conflicts with a hard constraint, the hard constraint wins. A budget ceiling, compliance requirement, staffing capacity and externally imposed deadline need an owner and an explicit confidence/status, not implicit priority inferred by an agent.

## 3. Quality-attribute scenarios

Use this minimal scenario contract for performance, security, reliability, correctness, maintainability, deployability, recoverability, accessibility or cost as applicable:

1. **Stimulus and source:** user action, failure, deployment or data change.
2. **Environment:** nominal/peak/degraded, time window, affected failure domain, version and workload conditions.
3. **Scope:** API/feature/journey and user group; component/contract boundaries.
4. **Response:** expected system behavior, including partial failures, timeouts and user-visible outcomes.
5. **Measure:** units, acceptance threshold, percentile or ratio, sample definition, measurement vantage, observation window, exclusions and test method.
6. **Priority/evidence:** hard gate or preference, decision owner, hypothesis versus measured result, and verification gap.

State invariants (e.g., no duplicate successful allocations) separately from SLO percentages. A zero-failure requirement should be expressed as a correctness contract and verified with relevant tests and concurrency/failure experiments; a finite test is not a universal proof.

## 4. Load and growth dimensions

Every number has units, source/status and an observation window. Describe distributions and skew rather than replacing them with a global average.

| Dimension | Required distinctions and questions |
|---|---|
| Users and sessions | Registered accounts, DAU/MAU, users in busiest hour, **simultaneously active** users, authenticated sessions and idle connected clients are different counts |
| Arrival process | External requests/events/transactions per second; open (independent arrivals) versus closed (completion/think-time-coupled users); baseline, sustained peak, burst, duration, growth and seasonality |
| Concurrency | In-flight requests at named boundary, independent background jobs, connected sockets, workers, pending queue and admitted versus offered load |
| Operation mix | Shares **summing to 100%** per scenario and time window; read/write ratio alone hides cost; include retries, fan-out, cache hits and skew by route/key |
| Size and resource demand | Request/response payload distribution, batch size, CPU/service demand per operation, network bytes/s, storage IOPS, memory, connections and dependency quotas |
| Data and access patterns | Total bytes/records, new writes and retention, indexes/replicas/backups, working set, hot keys/shards, update frequency and freshness |
| Failure and recovery | Surviving load during loss of a dependency/zone, timeouts, retry amplification, queue bounds, rate limits, load shedding and RPO/RTO |
| Operational and economic | Team skills, support hours, deployment/incident capacity, delivery window, budget cap and cost-at-scenario target |

### Derived numbers and their boundaries

- A **hypothetical** closed-session approximation `offered_RPS ≈ simultaneously_active_users × actions_per_active_user_per_minute ÷ 60` requires defined action-to-request mapping and activity assumptions. It is not an observation and should not be used with an open arrival process without separate calibration.
- Operation arrival rate: `RPS_operation = total_offered_RPS × operation_share`. Follow through with each operation's amplification to downstream calls/transactions.
- Average bandwidth approximation: `bytes_per_second ≈ sum(RPS_operation × average_bytes_operation)`, with direction, protocol overhead, compression and tail sizes stated.
- For a stable boundary with a well-defined flow and compatible long-run averages, Little's Law is `L = λ × W`: average in-system work `L`, throughput `λ` in completed units/second, **mean** residence time `W` in seconds. Name the exact queue/boundary, consider finite-window/transient uncertainty, and never insert p95/p99 for `W`. It is not a maximum concurrency, thread count or pool-sizing formula.
- Capacity and latency are **not** derivable from user counts or Little's Law alone: demand, contention, queues, downstream resource limits, failure headroom and load-test evidence are required.
- Percentiles are distributions over eligible observations and defined time windows. A `p99` is not a mean; a low median cannot prove the tail objective. Separate offered traffic from completed throughput and count overload rejections/latency.

## 5. SLOs, integrity, recovery and measurement

Specify for every SLI/SLO: user-facing event, eligibility denominator, success/good numerator, threshold and target, rolling or calendar window, time zone, vantage (client/edge/server/synthetic), exclusions, sampling, instrument owner, missing-telemetry treatment and whether the target is approved or proposed. Keep high-priority journeys separate instead of hiding them in one system-wide mean.

Examples of *forms*, not recommended targets:

- Availability: `good_valid_requests / eligible_valid_requests ≥ objective` over a declared window. Count failures and valid overload rejections as bad events unless the contract explicitly and defensibly says otherwise.
- Latency: `valid_successful_user_operations_below_threshold / eligible_user_operations ≥ objective` with decision about failed operations documented; also report p50/p95/p99 for diagnosis, not as replacements for a good-event SLI.
- Freshness: fraction of user-visible reads whose underlying data age is within bound.
- Recovery: restore a defined service capability within RTO and tolerated lost data within RPO for a named failure class; demonstrate by exercise, not an assertion.
- Correctness/integrity: explicit state invariants with concurrent execution and failure-path evidence, not a promise that an SLO ratio alone prevents a violation.

For an event-based reliability objective `SLO = 99.9%`, the permitted bad-event fraction is `1 - 0.999 = 0.001` of eligible events in that same window; that **does not** specify minutes of downtime unless measurement and traffic distribution justify converting it.

## 6. Workload scenarios and evaluation gates

At minimum define: **nominal**, **sustained peak**, **brief burst**, **degraded/failure-domain**, **growth horizon** and **recovery/rollout**. For each: user activity and offered arrivals, mix, burst duration, key skew, payloads, queue/backpressure behavior, latency and correctness targets, capacity assumptions, measurement plan and missing evidence.

A profile is ready for candidate comparison only when:

- business outcome metrics, gate criteria and preferences are individually classified;
- all load units, operation shares, arrival-model assumptions and windows are internally consistent;
- each SLO has an eligible population, numerator/denominator, window and test/measurement plan;
- relevant saturation points and downstream budgets are either evidenced or flagged as unknown;
- missing decisive evidence has an explicit owner and experiment;
- no hard constraint is silently relaxed and no architecture is selected by universal RPS/DAU thresholds.

An honest valid result is **insufficient evidence / measure first**. The subsequent issues own baseline modernization (#18), applicability cards (#19), option comparison (#20), transition architecture (#21) and decision routes (#22). No technology choice or whole-book authoring is in this issue.

## Independent public reference scope

The **structure and field names above are Tycho's independently authored proposal**, not a copied standard. The following admitted public-source sections were inspected on 2026-10-18 for narrowly specified methodological points:

- `src.arc42` — [arc42, Section 1: Introduction and Goals](https://docs.arc42.org/section-1/), specifically §1.1 requirements overview and §1.2 quality goals: frame business drivers, stakeholders and quality scenarios; living site, no pinned release asserted.
- `src.sre-workbook` — [The Site Reliability Workbook, Chapter 2: Implementing SLOs](https://sre.google/workbook/implementing-slos/), sections **What to Measure: Using SLIs** and **Moving from SLI Specification to SLI Implementation**: distinguish SLI specification, measurement vantage, good/total event ratio and window; web chapter inspected, whole book not read.
- `src.k6` — [Grafana k6, Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/), sections **Closed Model**, **Drawbacks of using the closed model** and **Open model**: completion-coupled versus independent arrivals and coordinated-omission risk; inspected as the versioned documentation page labelled v2.2.x at access, exact behavior of a test installation not verified.
- `src.little-law` remains **discovery-only** in the public register: the model states the mathematical identity with explicit applicability caveats but makes no claim that its registered paper or any finite-window derivation was read for this issue. A later evidence/benchmark task must examine it before using numerical predictions as authoritative.

These references do not validate the synthetic assumptions, guarantee performance, or imply that any software has been tested.
