# Queueing, workload boundaries, and Little's Law

> **Tycho technical page — V07/C01, pilot #38.** Evidence scope: public source sections inspected 2026-10-18. Status: researched draft; source-backed claims and original synthetic examples are distinguished below. No service was deployed or benchmarked. This chapter does **not** prescribe a system architecture or hardware size.

## Orientation — which number are we actually measuring?

An architect hears that a fictional service has 200,000 registered users, 12,000 daily active users and a peak of 120 requests per second. None of those numbers alone establishes its required thread count, connection-pool size, partition count, deployment topology or whether it should use a message queue.

The missing distinction is between **demand being offered to a boundary**, **work admitted**, **work completed**, and **requests still inside that boundary**. Users may produce many or few requests; arrivals may continue even when processing slows; retries can create further requests; and a downstream database may constrain throughput while request concurrency grows.

A useful workload profile names one boundary precisely:

```text
offered requests  →  ingress/admission  →  waiting queue  →  executing work  →  completed response
                          │                    │                   │
                          └→ rejected          └→ expired          └→ timed out / cancelled

Observability boundaries: offered, accepted, queued, in service, completed, rejected, timed out.
```

This picture is a **new Tycho illustration**, not an implementation architecture. Real services may have several queues and fan-out branches, in which case the diagram must be repeated per named boundary.

### Vocabulary with units

| Quantity | Meaning | Required distinction |
|---|---|---|
| Registered / DAU / simultaneously active users | Account population, distinct daily users and users currently performing actions | None directly counts in-flight requests. Client think time and action-to-request mapping are required to estimate traffic. |
| Offered arrival rate | New attempts sent toward the named ingress per second, whether or not admitted | May include retries; distinguish logical operations from transport requests. |
| Admitted arrival rate | Attempts accepted into the instrumented boundary | Less than offered under load shedding/admission control. |
| Completed throughput `λ` | Items **finishing** at the same boundary per second in the measured long-run accounting | Not interchangeable with offered traffic while backlog grows, or if failures/timeouts leave work accounted differently. |
| `L` | Long-run **mean** number of items inside the defined system, including queue and service when both are inside the boundary | Not simultaneous active users, a maximum in-flight count, or a server-count target. |
| `W` | Long-run **mean** time an item spends inside that boundary | Not p95 or p99. If only service time is measured, do not call it end-to-end queueing residence time. |
| SLO / tail latency | User-outcome target and distribution of observed durations | A tail percentile can matter for reliability even when the mean remains moderate; it cannot be substituted in `L = λW`. |

The fundamental law below is a **conditional relationship between compatible quantities**, not a universal sizing recommendation.

## Architecture — what Little's Law establishes

Kim and Whitt describe the familiar long-run relationship

```text
L = λ × W

L    average work in system                   [items]
λ    long-run throughput for the same items   [items/second]
W    mean residence time of those items       [seconds/item]
```

where the population, start/end boundary and averaging regime are consistent. The authors distinguish the well-developed long-run/stationary theory from real **finite-time measurements**, which can be biased by items already present at the start or remaining at the end. See *Statistical Analysis with Little's Law* (2013), Introduction §§1–1.2, and §2. <https://www.columbia.edu/~ww2040/LL_OR.pdf>.

### Why the formula is not a resource sizing rule

Imagine, explicitly as a **synthetic conditional example**, that one ingress-to-response boundary is stable over a sufficiently long observation, exactly 120 requests per second complete on average, and the **mean** residence time including queuing is 0.20 seconds. Then

```text
L = (120 completed requests / second) × (0.20 second / request)
  = 24 requests on average inside this boundary
```

This is arithmetic under assumptions. It is **not** measured Tycho performance. The result says nothing by itself about whether the work is CPU-bound, I/O-bound, multiplexed over event loops, waiting on locks, backed by a six-connection pool, or distributed across processes. Nor does it tell us the highest in-flight value in a burst or predict a latency percentile. Consequently, `L=24` is **not** an instruction to configure 24 threads, 24 DB connections or 24 worker instances.

For a closed interactive-user approximation, suppose 600 *simultaneously active* fictional users issue an average of three requests per minute, and one action corresponds to one API call. The modeled offered rate would be `600 × 3 / 60 = 30 requests/s`. It is neither observed nor inferable from registered users or DAU without those behavioral assumptions. This request arrival model and the prior completed-throughput example are different scenarios; do not combine them silently.

### Why finite measurement windows matter

A typical load test observes only `[t0, t1]`, not an infinite system history. Some work arrived before `t0`; some arrived before `t1` but remains inside afterwards. Kim and Whitt explicitly analyze **interval edge effects** and show a traditional finite-time equality under the special condition that the relevant system is empty at both observation edges (their §2.2, Theorem 1, pp. 1032–1033). The paper also discusses nonstationary and limited-data estimation concerns (Introduction §§1.1–1.2).

A small original counterexample makes the accounting problem visible:

- One request arrives at `t=-5s`, leaves at `t=5s`.
- A measurement observes `[0s,2s]`. There is **one item in the boundary throughout the observed interval**.
- The interval-average population is `L̄ = 1`, but **zero new items arrive inside the observed window**.
- Naively multiplying this window's `0 arrivals/s` by an average duration computed from only *new arrivals* cannot reproduce `L̄=1`. The relevant duration estimator is unavailable or changes definition.

The counterexample is Tycho's own deterministic illustration of an edge effect; it is not numerical data from the paper. The correct interpretation requires aligning eligible items, departures/arrivals and boundary conditions, or adopting a statistically justified estimator with explicit limitations. One finite traffic trace is not automatically a stationary dataset.

### A fictional overload scenario

Suppose a service can complete **at most an assumed 120/s** during a particular 30-second burst, while an independent generator attempts **180/s**. Ignore retries and assume for the arithmetic that each accepted request remains queued until processed, with no timeouts or backpressure:

```text
offered - completed = 180 - 120 = 60 requests/s
backlog after 30s = 60 × 30 = 1,800 additional outstanding requests
```

These numbers are invented, and the fixed 120/s capacity is *assumed*, not measured or derived from Little's Law. A real system might shed excess load, throttle clients, saturate queues and crash, so backlog growth need not follow this line. In particular, a transient 30-second burst cannot be treated as stationary with `L̄ = λW` using mismatched instantaneous figures.

If an otherwise identical hypothetical ingress admits only a bounded **600-request backlog**, that backlog would reach its limit in roughly `600/60 = 10s` under the simplified assumptions. Afterward it would need to reject, shed, slow or route excess attempts rather than continue increasing that same queue indefinitely. **This is not** a recommendation that 600 is a good production queue size.

Google SRE documents how exhausted CPU, memory, queues and retries can amplify load and produce cascading failures; it discusses bounded admission, load shedding and degradation as mechanisms with workload-dependent trade-offs, not default configurations: *Site Reliability Engineering*, Chapter 22, sections **Resource Exhaustion**, **Preventing Server Overload**, **Queue Management**, and **Load Shedding and Graceful Degradation**. <https://sre.google/sre-book/addressing-cascading-failures/>.

### How the load generator changes the question

Grafana k6's *Open and closed models* documentation (page displayed as **v2.2.x** at inspection, 2026-10-18) distinguishes:

- **Closed model:** virtual-user iteration start depends on completion of the previous iteration. As the system slows, iterations can begin less frequently, so an experiment intended to hold offered arrivals fixed can underload the stressed system.
- **Open model:** iteration starts are scheduled independently of previous iteration duration, subject to having sufficient load-generator resources. This is more suitable for exploring a specified offered-arrival process. Monitor whether the generator actually started the target iterations; the existence of an arrival-rate executor does not prove achieved test load.

The source explicitly explains the risk of **coordinated omission** in the closed model: <https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/>, sections **Closed Model**, **Drawbacks of using the closed model**, and **Open model**.

The open model is not inherently “more realistic” for every application: a finite number of humans who await a response before their next action may create completion-coupled sessions. The experiment must match the real workload assumption and separately measure offered versus completed traffic; neither generator model alone validates production capacity.

## Failure, recovery and measurement

| Situation | Internal consequence | External signal and risk | Measurement / mitigation hypothesis |
|---|---|---|---|
| Stable request mix | Completed and offered flow are compatible in a long-run sense | Mean latency may still hide tail effects | Observe arrival/finish counters, mean duration and separate tail distributions |
| Burst exceeds processing | Queue may grow until capped; deadlines may expire | Latency, timeouts and backlog; possible increasing retries | Record offered/admitted/completed/rejected rates, queue depth and age; test shedding |
| One dependency becomes slow | Service time and in-flight work rise; future arrivals may remain independent | End-to-end latency worsens even when own CPU is idle | Trace downstream duration, resource quotas, pool waits, timeout propagation |
| Partial instance/zone loss | Surviving processing capacity and queue conditions may change | More traffic shifts to remaining instances; retry amplification possible | Load-test degraded state, capacity headroom, recovery time and request outcome |
| Recovery after overload | Backlog, cancellations and retries may outlive the trigger | Old work can delay fresh useful work | Observe queue age, replay/retry budget, drain/shed policy and good-event ratio |

No row claims the proposed mitigation was tested. An availability number or p99 guarantee requires separately defined eligible requests, observation period and real measurements.

### A bounded, falsifiable validation protocol

Before choosing an architectural change, define:

1. **Boundary and counting unit:** logical operation ID versus per-attempt request ID; ingress, admission, queue, service, completion and cancellation timestamps. Ensure request retries are countable separately.
2. **Workload hypotheses:** closed user-interaction model versus independent offered-arrival model; nominal, peak, burst duration, operation mix, payload distributions, hot keys and think time.
3. **Metrics:** offered, admitted and completed arrivals/s; rejection and timeout counts; queue age/depth; **mean** residence time; p50/p95/p99 distributions over declared eligible observations; saturation signals for CPU/memory/pools/dependencies.
4. **Experiment:** warmup and a measurement window adequate to test a stable period, then controlled overload/dependency-loss phases; ensure load-generator capacity and report dropped iterations as experimental limitations.
5. **Decision:** distinguish the observed limiting resource from downstream symptoms, compare simplest viable remedies and repeat the experiment. More threads or shards are not justified merely because in-flight work rose.

If only user count, RPS and p99 are known, **there is insufficient evidence to choose a deployment architecture or size a pool**. The next action is to measure service demand, queueing, dependency limits and retry behavior within the same boundary.

## Evidence and provenance ledger

| Claim | Inspected independent public source | Supported scope and limitation |
|---|---|---|
| The `L = λW` identity relates long-run mean population, rate and residence time | `src.little-law`: Kim & Whitt (2013), **Introduction p.1030, §1.2 pp.1031–1032**, <https://www.columbia.edu/~ww2040/LL_OR.pdf> | Theoretical/estimation discussion; not a performance benchmark or sizing recommendation |
| Naive finite-window averages can disagree because of nonempty observation edges | `src.little-law`: **§§2.1–2.2, pp.1032–1033**, including Theorem 1 | Special exact equality is under declared start/end conditions; Tycho's one-request counterexample is original |
| Open and closed generators differ in completion coupling; coordinated omission can affect closed tests | `src.k6`: *Open and closed models*, **Closed Model / Drawbacks / Open model**, online documentation v2.2.x accessed 2026-10-18 | k6 documentation for executor behavior, not proof of a real generator's achieved rate |
| Unbounded queues, retries and resource exhaustion can reinforce system overload | `src.sre-cascading`: *Addressing Cascading Failures*, **Resource Exhaustion / Queue Management / Load Shedding and Graceful Degradation / Retries**, Chapter 22 | Public operational guidance; concrete policies must be load tested for a specific service |
| Hypothetical `120×0.2=24`, `600×3/60=30`, burst backlog and queue capacity | **Original synthetic assumptions and arithmetic in this page** | Illustrative derived values only; no independent measurements, throughput guarantee, source-backed capacity or production claim |

These page/section scopes were directly inspected. Other references in [the public source register](../../../sources/register.json) remain at their existing discovery status; the register's present validator does not implement a section-level reading state. Do not silently present all registered sources as researched.

## Next reading and review

- **Book owner:** first researched slice of proposed V07/C01. The [research contract](../../../authoring/contracts/PILOT-01-queueing.md) defines the bounded accepted question.
- **Related planned owners:** V03/C05 for resource pools; V07/C03 for benchmarking validity; V07/C05 for overload protection. These links remain planning references until actual pages exist.
- **Known limitations:** No original production trace, actual queueing experiment, workload distribution, empirical p99 or cost comparison. Confidence-interval and time-varying estimation algorithms beyond the inspected paper passages are deferred.
- **Review:** a source-aware AI authoring review and arithmetic check are possible; no named independent human technical review or production validation has occurred. Structural/link checks and CI results must be recorded when the PR runs.
