# Requirements and workload profile — reusable template

> Template revision: 0.1. Origin: Tycho [model](../authoring/models/requirements-workload-profile.md), issue [#17](https://github.com/rouslanbaranov/tycho/issues/17). This is a Markdown authoring contract, **not** a JSON Schema. Replace all `TODO` fields. Unknown is an allowed and meaningful value; never invent observations to fill a slot.

## A. Identity, question and scope

| Field | Value / evidence |
|---|---|
| Profile ID / revision / status | TODO / v0.1 / draft |
| Product or synthetic system | TODO |
| Decision being supported | TODO; new system or existing-system change |
| Actors and decision owner | TODO |
| Primary and excluded journeys | TODO |
| Named client → service → dependency boundaries | TODO |
| Units, clock/time zone and reference window | TODO |
| Scenario evidence class | Observed / stakeholder requirement / scenario assumption / derived / unknown (select for each) |

**Research question:** TODO

**Explicit non-goals:** TODO

**Most consequential uncertainties:** TODO

## B. Business outcomes and requirements

| ID | Actor and capability / objective | Baseline and status | Target, units and window | Owner | Evidence or validation |
|---|---|---|---|---|---|
| BO-01 | TODO | Unknown | TODO | TODO | TODO |

| ID | Requirement | Type (HARD / PREFERENCE) | Rationale and priority | Test / rejection condition | Owner / evidence |
|---|---|---|---|---|---|
| C-01 | TODO | HARD | TODO | TODO | TODO |
| P-01 | TODO | PREFERENCE | TODO | Compare options, do not reject automatically | TODO |

Never confuse a high-value preference with a mandatory constraint. Name the decision-maker authorized to trade off preferences.

## C. Quality-attribute scenarios

| ID | Stimulus / actor | Environment, failure and workload conditions | Scope and expected response | Measure, eligible population, window | HARD/PREFERENCE | Validation |
|---|---|---|---|---|---|---|
| Q-01 | TODO | TODO | TODO | TODO | TODO | TODO |

Record required **state invariants** (for example, allocations cannot exceed capacity) separately from latency/success ratios. Define timeouts, duplicates, backpressure, recovery and degraded user behavior where relevant.

## D. Demand and workload by scenario

The following columns describe **offered arrivals**; completed throughput is measured separately. Define what a request/action/transaction means and whether arrivals are open or closed.

| Scenario | Time window and duration | Registered / DAU / simultaneously active | Arrival model and derivation | Offered RPS or events/s | Growth/seasonality | Evidence class |
|---|---|---|---|---|---|---|
| Nominal | TODO | TODO | TODO | TODO | TODO | TODO |
| Sustained peak | TODO | TODO | TODO | TODO | TODO | TODO |
| Brief burst | TODO | TODO | TODO | TODO | TODO | TODO |
| Dependency/zone failure | TODO | TODO | TODO | TODO | TODO | TODO |
| Growth horizon | TODO | TODO | TODO | TODO | TODO | TODO |
| Rollout/recovery | TODO | TODO | TODO | TODO | TODO | TODO |

**Workload detail:** think time; average and tail interarrival times; skew/hot-key fraction; read/write share; per-operation fan-out; retries; number of connected vs active vs in-flight users; queue boundaries; missing telemetry. TODO.

| Operation | Offered share (%) | Avg / tail payload (direction and units) | Dependencies and expected fan-out | User priority | Failure/correctness notes |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |
| **TOTAL** | **100%** | — | — | — | — |

**Peak operation rates and bytes/s** (show formula, units, assumptions and rounding): TODO.

**Concurrency:** In-flight at named boundary; queued; active sessions; open connections; background jobs. Distinguish these. If using `L = λW`, document stability, period, completed throughput and **mean** residence time; never use tail latency as `W`. TODO.

## E. Data, demand and limits

| Dimension | Nominal | Peak/growth | Source or unknown |
|---|---|---|---|
| Storage records/bytes and indexes | TODO | TODO | TODO |
| Write rate and retention | TODO | TODO | TODO |
| Working set/cacheable fraction | TODO | TODO | TODO |
| Skew/hot partitions/cardinality | TODO | TODO | TODO |
| CPU and memory demand | TODO | TODO | TODO |
| IOPS and network throughput | TODO | TODO | TODO |
| Connection pools and downstream quotas | TODO | TODO | TODO |
| Queue capacity, retry budget and overload policy | TODO | TODO | TODO |

## F. User-level objectives and recovery

| SLI / invariant ID | Eligibility denominator and measured vantage | Good-event numerator or rule | Target + window | Status / owner | Proof plan |
|---|---|---|---|---|---|
| SLO-01 | TODO | TODO | TODO | Proposed, not measured | TODO |
| INV-01 | Applicable state transitions | No invariant violation | HARD | Proposed, not proven | TODO |

Record: p50/p95/p99 latency **distributions** when available, error classifications, client/edge/server vantage, overload rejections and timeouts, RPO/RTO by failure class, data freshness, consistency, durability, and the difference between a proposed SLO and an achieved measurement.

## G. Delivery and economic constraints

| Constraint / preference | Type | Value, units, window | Owner and validation |
|---|---|---|---|
| Team capability/support capacity | TODO | TODO | TODO |
| Delivery deadline | TODO | TODO | TODO |
| Operational spend cap and preferred target | TODO | TODO | TODO |
| Security, privacy, retention and locality | TODO | TODO | TODO |
| Rollout, data migration and coexistence | TODO | TODO | TODO |

## H. Evidence and unknowns

| ID | Claim / assumption | Class (observed / required / synthetic / derived / unknown) | Public exact-source or reproducible measurement | Confidence limits | Validation action / owner |
|---|---|---|---|---|---|
| A-01 | TODO | unknown | Not available | TODO | TODO |

**Contradictions or disagreement:** TODO

**Evidence that could reverse an architecture option:** TODO

**Source versions, inspected sections and licensing:** TODO (do not claim documents were read solely because they are in the source register).

## I. Decision readiness gate

- [ ] Hard constraints and preferences classified, with named acceptance conditions.
- [ ] Business outcomes and quality scenarios measurable by stated owner and window.
- [ ] User, arrival, concurrency, mix, size, skew and growth figures have units and evidence classes.
- [ ] Operation shares total 100% within each modelled scenario.
- [ ] SLO numerator, denominator, exclusions, window, vantage and proposed/observed state explicit.
- [ ] Dependencies, queuing and degraded failure assumptions documented or flagged unknown.
- [ ] Material unknowns have experiments/owners and do not masquerade as facts.
- [ ] No architecture chosen from traffic/user thresholds alone.
- [ ] Exact independent sources or missing evidence are recorded.

**Gate decision:** ready for bounded candidate exploration / measure first / insufficient evidence. **Reason:** TODO.

**Next research task:** TODO. **Review status:** not human-reviewed unless an actual review event is documented.
