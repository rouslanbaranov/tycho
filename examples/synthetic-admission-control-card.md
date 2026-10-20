# Conditional admission control under burst overload — synthetic applicability card

> Original Tycho illustrative case for [issue #19](https://github.com/rouslanbaranov/tycho/issues/19). Classification: resilience / backpressure mechanism. Card ID: `resilience.admission.boundary`, revision 0.1. All numbers below are invented. No service or load generator was benchmarked; no independent human approval is claimed.

**Canonical mechanism:** [Queueing, Little's Law and workload boundaries](../book/volumes/v07/c01/queueing-littles-law.md). Related: [requirements profile](../authoring/models/requirements-workload-profile.md), [pattern card contract](../authoring/models/pattern-applicability-card.md). This card guides a **decision**, rather than repeating the full mechanism chapter.

## The decision question

When offered bursts exceed a bounded dependency's sustainable throughput, should an application reject excess work **before** entering a costly queue, or should it allow buffering to grow? The answer depends on deadlines, prioritization, invariants and the actual accepted-demand contract.

Consider a completely fictional registration API. The client offers 200 logical operations per second for 30 seconds. Available workers are **assumed** to complete 150 successful operations/s under the stated conditions. Starting queue is empty, service demand is simplified as constant, and retries/cancellations are excluded. The hypothetical offered-completed imbalance accumulates `(200-150)*30=1500` outstanding operations if all are admitted. This arithmetic is NOT a queueing latency prediction or a benchmark.

## Applicability and required evidence

| Condition | Status in this fictional case | What evidence is needed in reality |
|---|---|---|
| External offered demand can temporarily exceed sustainably completed demand | Invented for illustration | Traffic and resource telemetry per operation and ingress boundary |
| An explicit max queue wait/deadline is part of the contract | Unknown; must be agreed | User journey timeouts, deadline propagation and SLO |
| Failure as a prompt, observable rejection is better than silent stale work | Conditional hypothesis | UX/API semantics, client retry policy, cost of rejection |
| Admission happens before expensive downstream calls | Proposed | Traces and exact allocation boundary |
| Correctness under retries/rejection can be specified | Unproven | Idempotency/transaction tests; rejected work cannot have partially committed |
| Fairness between tenants/classes is required | Unknown | Approved quota/priority contract and starvation tests |

A declared rejection is not successful throughput. It may be the least harmful option, but a service cannot claim availability by excluding rejected legitimate demand from its SLI without an explicit and defensible user-facing contract.

## Contraindications and counterexamples

- **Critical synchronous command with no safe retry and a possible durable side effect before admission:** Reject-before-work cannot be implemented safely at a late point; first move the admission boundary earlier or preserve request identity and outcome.
- **Short burst with sufficient bounded buffer under measured deadlines:** Additional rejection logic may be unnecessary. If all requests can complete in time, retaining a correctly bounded queue could be preferable.
- **Generator already suppressed arrivals:** A supposedly good rejection rate may only reflect a closed-loop client slowing down. Record scheduled and actually started work before claiming overload protection.
- **Per-tenant ordering, quotas and fairness not defined:** Global load shedding can starve a less active tenant; seek a workload-aware policy rather than assume uniform correctness.
- **Asynchronous durable workload that must not be lost:** Dropping requests or in-memory queue entries is an invalid substitute for an admitted durable task contract.

All these are **conditional engineering reasoning**. Which alternative wins cannot be decided from the constructed RPS number alone.

## Alternatives and explicit trade-offs

| Candidate | Potential benefit | Cost / failure mode | Validation |
|---|---|---|---|
| Retain existing bounded queue | Absorb short bursts within deadline | Tail latency and stale work when burst outlasts slack | Queue age, missed deadlines and correct completions |
| Reject early with capacity-limited admission | Prevent unbounded worker/downstream contention | Legitimate requests rejected; retry storm or unfairness | Offered/rejected/completed, p99, retry amplification and invariants |
| Rate limit per principal plus bounded queue | Fairness in mixed workloads | Complexity, potentially stranded capacity, misconfigured priorities | Starvation tests and workload mix sensitivity |
| Durable asynchronous acceptance | Protect accepted writes from volatile service overload | Persistence and reconciliation complexity, change of user semantics | Durable commit, replay, late/duplicate-effect experiments |
| Increase measured bottleneck capacity | Improve completion rate under sustained load | Scaling delay, downstream bottleneck and cost | Controlled load curve and resource/latency measurements |

## Original decision flow

~~~mermaid
flowchart TD
  Input["Measure offered arrivals and user contract"] --> Valid{"Deadline, correctness and identity clear?"}
  Valid -->|No| More["Insufficient evidence: inspect and test"]
  Valid -->|Yes| Queue{"Bounded buffer meets measured deadline?"}
  Queue -->|Yes| Keep["Consider retaining simple bounded queue"]
  Queue -->|No| Gate["Compare early admission, fairness and alternatives"]
  Gate --> Test["Measure rejection, latency, resource and invariants"]
  Test --> Result{"Meets hard gates and improves outcome?"}
  Result -->|No| More
  Result -->|Yes| Conditional["Conditionally applicable; staged rollout"]
~~~

Text alternative: first establish arrival and correctness evidence; if key contracts are unknown, investigate. If a bounded queue demonstrably meets deadlines, a simpler retained design can suffice. Otherwise compare admission/fairness alternatives using an equal-budget trial. Only measured outcomes and invariant preservation support conditional adoption.

## Falsifiable validation plan

**Hypothesis:** when sustained offered demand exceeds downstream capacity, a correctly placed, bounded admission controller may reduce worker queue age and p99 for **admitted** operations without violating business invariants, compared with uncontrolled queue growth. The hypothesis is **not** supported merely by lowering admitted throughput.

Prepare an open-model generator that tracks the intended schedule and actually issued operations. Reuse the same request mix, downstream resources, failure simulation and run duration across candidates. Count offered, accepted, rejected, failed and successful operations separately; record retries per logical command, downstream connection pressure, queue age, p50/p95/p99, correctness breaches and recovery after the burst. An operation must not be reported successful before its transaction contract says so. Repeat with a skewed high-priority tenant.

**Reject early admission as configured** if it violates any hard correctness/fairness constraint, increases client retry amplification, fails agreed user-facing good-event SLOs, or shows no net resource/latency benefit over a simpler bounded queue. Absence of a representative workload gives `insufficient-evidence`, not an assumed recommendation.

## Scoped evidence ledger

| ID | Evidence and inspected location | Supports / excludes |
|---|---|---|
| P01 | [Tycho canonical queueing chapter](../book/volumes/v07/c01/queueing-littles-law.md), *Partial failure, saturation and recovery* and its public-source ledger | Synthetic backlog arithmetic and the need to count rejected demand; no live workload |
| P02 | [Google SRE book, Handling Overload](https://sre.google/sre-book/handling-overload/), *Client-Side Throttling*, *Criticality* and *Deciding to Retry*; source inspected 2026-10-19 | Real-world motivation for overload protection, criticality and controlled retries; not proof for the hypothetical API |
| P03 | [Grafana k6, Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/), *Open Model* and *Closed Model*; living docs inspected 2026-10-19 | Load-generation model distinction; not a claim that a test actually ran |
| P04 | [Tycho synthetic capacity model](../book/volumes/v07/c01/queueing-littles-law.md), original bounded example | Conceptual method; not empirical verification of an admission policy |

**Acceptance boundary:** This card demonstrates classification, prerequisites, contraindications, alternatives, one scenario-local set of assumptions and falsifiability. The card's adoption result is **insufficient evidence pending workload and correctness measurements**. It does not implement rate limiting, modify a service, run a benchmark, approve a pattern library or validate a complete M1 decision engine.
