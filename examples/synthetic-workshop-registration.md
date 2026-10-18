# Synthetic case study — community workshop registration

Status: **entirely fictional, unmeasured scenario**, authored for Tycho issue [#17](https://github.com/rouslanbaranov/tycho/issues/17), 2026-10-18. No public product, private system, deployment, load test, customer telemetry or architecture is described. Every number is invented for decision-method illustration.

Use the [requirements/workload model](../authoring/models/requirements-workload-profile.md) and [blank template](../templates/requirements-workload-profile.md) to develop alternative scenarios. This case is not a recommendation to adopt a particular architecture.

## A. Decision and boundaries

Profile: `synthetic.workshop-registration.v01`; revision v0.1; status **draft / scenario assumptions only**.

A hypothetical organization lists local workshops. Visitors discover upcoming sessions, check available seats and request one registration. The business needs a credible requirements and load profile before selecting a persistence model, consistency strategy, serving topology or scaling mechanism. The service boundary runs from client-visible API ingress through application processing to an abstract authoritative seat ledger; no technology stack is chosen.

**Actors:** visitor, workshop organizer, product owner, reliability operator, privacy reviewer. Names describe roles in a fictional organization, not evidence of real stakeholders.

**Non-goals:** evaluating payment processing, choosing microservices over a monolith, specifying a live deployment or claiming production performance. The future legacy baseline belongs to #18.

## B. Outcomes and decision criteria

| ID | Goal or constraint | Type | Proposed evidence / measure |
|---|---|---|---|
| BO-01 | Visitors can discover a workshop and get a correct availability indication | Business outcome | Completed discovery journeys / eligible discovery journeys; target agreed after user research |
| BO-02 | Accepted registrations issue one confirmation and never exceed the published seat capacity | Business outcome + correctness invariant | Exercise simultaneous reservation attempts and reconciliation; rejected capacity-full operations are a valid outcome |
| C-01 | Confirmed seats for a workshop never exceed its configured capacity | **HARD invariant** | Concurrent update/failure test and authoritative state audit; test coverage is not a mathematical proof |
| C-02 | Maximum total recurring infrastructure spend of EUR 3,000/month under the peak scenario | **HARD proposed constraint** | Independently priced capacity model; cost not yet established |
| C-03 | A demonstrable release candidate within 16 weeks | **HARD proposed constraint** | Delivery plan and staffing feasibility, currently unknown |
| C-04 | Retain completed registration records for 36 months | **HARD proposed constraint** | Data policy and deletion/restore exercise, subject to policy review |
| P-01 | Prefer EUR 1,800/month or less if equally viable | PREFERENCE | Comparable monthly bill-of-materials estimates with assumptions |
| P-02 | Prefer simpler operational ownership and fewer deployment units | PREFERENCE | Estimated maintenance/on-call tasks and failure surface; not scored yet |

The proposed hard/pref label describes the **hypothetical decision contract**, not approval by a real stakeholder.

## C. Quality scenarios and response criteria

| ID | Stimulus/environment | Expected response and scope | Proposed acceptance / measurement |
|---|---|---|---|
| Q-01 | Visitor browses during a hypothetical sustained 120 offered API RPS for 20 minutes | Discoverability and result freshness maintained for valid browse requests | At least 99% of eligible browse outcomes are successful within 500 ms measured at edge, in a declared 28-day window; acceptance under this load requires a representative test |
| Q-02 | A valid visitor attempts registration when capacity is nearly exhausted; concurrent attempts occur | Exactly one reservation outcome per idempotency key; no confirmed over-allocation | INV-01 zero confirmed over-allocation; test simultaneous requests, timeouts and retries; legitimate capacity-full responses do not count as state corruption |
| Q-03 | One application instance fails amid sustained nominal demand | User sees an explicit failure or a successful response; no silent duplicate booking | Restore service for nominal offered demand within proposed 10 minutes; RPO=0 for acknowledged registrations, both subject to separate feasibility review |
| Q-04 | Organizer adjusts workshop capacity while visitors read availability | Read responses respect a specified freshness bound, without claiming serializability by default | Propose freshness of ≤5 s for reads; define allowed lag and measurement later |
| Q-05 | A new version is rolled out during accepted registration attempts | Previously acknowledged outcomes remain retrievable and no migration skips required state | Test version coexistence, migration and rollback after architecture is chosen |

Q-01 has a defined performance denominator: eligible valid browse requests, **including** valid overload rejections/timeouts as not-good. Deliberately invalid inputs and automated health probes are excluded and counted separately. A proposed 28-day SLO window is a business convention here, not an observation from the 20-minute peak.

## D. Hypothetical demand scenarios

| Metric | Fictional premise | What it does *not* establish |
|---|---|---|
| Registered accounts | 200,000 | Daily use, load or in-flight requests |
| Daily active users | 12,000 | Simultaneous active load |
| Distinct users during busiest hour | 3,000 | Uniform arrivals or concurrency |
| Simultaneously active users (nominal) | 600 | 600 outstanding requests |
| Average API calls per active user, nominal | 3/minute, counting complete client actions as one API request | A measured or proven request rate |
| Peak scenario | Independent offered arrivals 120 requests/s for 20 minutes | That current infrastructure can process 120/s |
| Brief burst scenario | 240 offered requests/s for 30 seconds, with same illustrative mix | That queues, retries or dependencies handle the burst |
| Growth scenario | 2x nominal and peak offered arrival rates at 18 months | A validated forecast |
| Degraded scenario | Nominal 30 offered requests/s during loss of one application instance, plus recovery traffic | Surviving capacity or correctness |
| Rollout scenario | Nominal rates plus possible replay/retry amplification | Safe mixed-version operation |

**Nominal closed-session approximation:** `600 active users × 3 requests/minute ÷ 60 = 30 offered requests/s` under the assumed interaction and think-time model. It is **not** calculated from 200,000 registered users or 12,000 DAU. This simplified estimate assumes each action maps to one request; real fan-out, retries and background jobs must be measured. Offered peak (120/s) and burst (240/s) are independent **scenario assumptions** to be tested with an arrival-rate-oriented model, not a claim that concurrent-user growth automatically multiplies throughput.

### Peak operation mix

| API operation | Share of offered requests | Offered rate at 120/s | Illustrative mean response bytes (downstream direction) |
|---|---:|---:|---:|
| Browse/list workshops | 70% | 84.0/s | 4 KiB |
| Read seat availability | 29% | 34.8/s | 1 KiB |
| Attempt registration | 1% | 1.2/s | 2 KiB |
| **Total** | **100%** | **120.0/s** | Mixed |

Under these assumptions, mean **response payload** transfer alone is `84 × 4 + 34.8 × 1 + 1.2 × 2 = 373.2 KiB/s` at peak, excluding request bodies, headers, TLS, retries, compression and higher payload percentiles. Do not use this as a network provisioning figure. Arrival rates are averages within the declared 20-minute peak; minute-level burst distribution is unknown.

**Skew hypothesis:** one promoted workshop is responsible for 30% of seat-availability requests during peak (not of all API traffic). This may create hot-record or contention concerns, but does not prove a partitioning bottleneck. Unknown: concurrent allocation attempts to that workshop.

**Illustrative in-flight arithmetic only:** if a stable 120 completed requests/s throughput **and mean** request residence time of 0.20 s were actually observed at the same ingress-to-completion boundary, Little's Law gives `L = 120/s × 0.20 s = 24` *average* requests in that boundary. **Neither throughput nor mean latency is measured here.** 24 is not a p99 concurrency count, DB connection requirement or safe pool size. If offered > completed during overload, queues/backlog and boundary conditions change the interpretation.

### Data growth and resource unknowns

Assume 25,000 **new confirmed registration records/month**, with 2 KiB of base record payload each (purely invented). Raw record increment: `25,000 × 2 KiB = 48.8 MiB/month` (rounded), or about `586 MiB/year`, excluding indexes, metadata, backups, replicas, event logs and tombstones. This monthly assumption is **not derived** from peak registration attempts. Three-year retention is a proposed hard constraint but delete/restoration rules remain unresolved.

The workshop catalogue size, payload tails, browser cache hit ratio, connection usage, write amplification, disk IOPS, query plans, network/CPU per operation, dependency fan-out, event cardinality and actual working set are **unknown**. This profile must not invent a CPU/core count, thread pool, replica count or shard count.

## E. SLO definitions (proposed, not achieved)

| ID | Eligible events and vantage | Good criterion / target | Window and limitations |
|---|---|---|---|
| SLO-01 | Valid visitor browse requests at API edge, including valid timeouts and 429/5xx | ≥99% completed successfully within 500 ms | Proposed rolling 28 days; no instrument or measurement exists |
| SLO-02 | Valid registration attempts accepted for processing at edge | ≥99% receive **a definitive** accepted/full/error outcome within 1 s; do not mistake "full" for availability failure | Proposed rolling 28 days; idempotency retries and outcome classification must be specified |
| SLO-03 | Valid user operations at edge | ≥99.9% get an expected service response (including legitimate capacity-full) rather than infrastructure failure | Proposed rolling 28 days; exact eligible scope to confirm before approval |
| INV-01 | All authoritative confirmed registration states | Number of confirmed seats ≤ workshop capacity and acknowledgement is not silently lost | Hard correctness requirement, separate from SLO averages; no proof or test executed |
| DR-01 | Defined single-instance loss during nominal demand | Proposed RTO ≤10 minutes; acknowledged registration RPO=0 | Hypothesis needing failure tests and a storage/replication design |

SLO-03's hypothetical bad-event budget is `0.1%` of **eligible operations in the defined window**, not automatically minutes of downtime. Reporting p50/p95/p99 for investigation is planned; no percentile or availability figure has been observed.

## F. Critical unknowns and experiments

| Unknown | Why a decision depends on it | Evidence to obtain, independently and reproducibly |
|---|---|---|
| Whether 3 actions/min maps to actual API arrivals | 30/s nominal could be too high or too low | Ethical/synthetic session model, action telemetry specification and measurement plan |
| Peak/burst duration and traffic skew | Affects queues and overload behavior | Admission-controlled open-arrival load experiment at 120/s then 240/s with an independent traffic generator |
| Dependency cost and hot-seat contention | Could dominate latency and reservation correctness | Build isolated, original prototype; test concurrent allocations/retries at one key and measure throughput, conflicts and outcomes |
| Response-size tails / working-set distribution | May alter memory/network economics | Generate synthetic skewed samples and measure transfer/caching; capture confidence intervals |
| Ability to satisfy RPO=0, RTO and retention simultaneously | Hard constraints may conflict with budget | Failure-domain model, destructive test protocol and independent cost estimate |
| Monthly spending under specified load | EUR 3,000 cap is a gate | Versioned provider pricing and total resource/operational estimate with date |
| What constitutes a good reservation outcome after a lost response | Requires retriable confirmation/idempotency semantics | Draft protocol contract and explicit client retry test |
| SLO measurement coverage and denominators | Incorrect counting can hide user-visible failures | Compare synthetic client and edge instrumentation and document exclusions |

No candidate architecture can be accepted until the decisive hard constraints have feasible evidence. A sensible output at this stage is **measure first**, not "use microservices/sharding/queues once RPS exceeds X."

## G. Independent evidence and review state

This example is original synthetic material. The following public references informed only methodological conventions; they do not validate any scenario number:

- [Tycho inspected evidence inventory](../authoring/contracts/TYCHO-17-research-contract.md), including source IDs, exact sections and access limitations.
- [Reusable model](../authoring/models/requirements-workload-profile.md) describes why active users, arrivals, in-flight concurrency and tail latency remain distinct.

**Coverage:** profile/model and synthetic worked case drafted; no implementation or measured performance. **Human review:** none. **Approval:** none. **Architecture selected:** none. **Next task:** use #18 and #19 to build independent modernization and applicability inputs, then test candidate comparisons through #20.
