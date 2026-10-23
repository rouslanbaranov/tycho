# Phase 3 human review sample

Status: **human review pending**. No human review has been performed.

Sample: 15 of 72 items (20.8%).

Full paths, quotes and machine-readable fields are in
evaluation/phase3-human-sample.json. This packet omits long paths to keep
Markdown lines within 100 characters.

For each item: check the adjudicated label, support section and answer key.
Record agree/disagree, corrected label and notes. Do not edit the frozen qrels.

## 1. T1-A01 — T1

**Question.** In the cache-aside pattern, what does an application do on a cache hit and on a
cache miss, and how does this differ from read-through caching?

**Phase-3 label.** answerable
**Adjudicated label.** answerable

**Answer key.** The application reads the cache first; a hit returns the cached item directly.
On a miss it loads the item from the data store, writes it into the cache, and returns it to the
caller. Read-through caching differs because the cache itself performs the load on a miss, while
cache-aside keeps that logic in the application.

**Proposed support.**

- section: 4-cache-aside-is-a-sequence-not-a-consistency-theorem
  > A cache-aside sequence reads the cache first, fetches the origin on a miss

- section: bounded-pattern-ownership-notes
  > A read-through cache loads a miss from the source on behalf of the caller

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 2. T2-A01 — T2

**Question.** A service handles a long-run average of 250 requests per second, and each request
spends an average of 120 ms in the system. Using Little's law, what is the average number of
requests in the system, and what condition must hold for the law to apply?

**Phase-3 label.** answerable
**Adjudicated label.** answerable

**Answer key.** Convert the dwell time to seconds and multiply: L = 250 x 0.12 = 30 requests on
average. The law is an average-case identity for a stationary (ergodic) system; apart from that,
it does not depend on the arrival distribution, the service-time distribution or the queue
discipline.

**Proposed support.**

- section: page-level
  > For a stable system with a consistent customer/work definition and well-defined steady-state

- section: page-level
  > L = λ × W

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 3. T3-A01 — T3

**Question.** A five-server Raft cluster uses majority quorums. How many server failures can it
tolerate while still electing a leader and committing new entries, and what property of
majorities keeps two partitions from both making progress?

**Phase-3 label.** answerable
**Adjudicated label.** answerable

**Answer key.** Five servers require a majority of three, so the cluster can lose two servers
and still elect a leader and commit entries; with three failures only two remain, below quorum.
Quorums are counted over all configured servers rather than only the reachable ones, and any two
majorities share at least one server. That shared server can vote in only one term and can sit
on only one side of a partition, so at most one partition can assemble a quorum and split brain
is avoided.

**Proposed support.**

- section: 2-majority-quorum-arithmetic-and-the-failure-envelope
  > A **5-voter** cluster requires 3.

- section: 2-majority-quorum-arithmetic-and-the-failure-envelope
  > a minority partition cannot commit authoritatively

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 4. T4-A01 — T4

**Question.** Under RFC 9110, which request methods are idempotent, and when may a client
automatically retry a request whose method is not idempotent?

**Phase-3 label.** answerable
**Adjudicated label.** answerable

**Answer key.** RFC 9110 defines idempotence in terms of the intended effect on the server:
several identical requests must have the same effect as one. PUT, DELETE, and every safe method
(GET, HEAD, OPTIONS, and TRACE) are idempotent. A client should not automatically retry a
non-idempotent request unless it knows the request semantics are actually idempotent or can
detect that the original request was never applied; a proxy must not automatically retry
non-idempotent requests at all.

**Proposed support.**

- section: 2-http-method-semantics-are-not-business-effect-deduplication
  > PUT, DELETE and safe methods are idempotent by their specified semantics.

- section: 2-http-method-semantics-are-not-business-effect-deduplication
  > POST has no general automatic-retry guarantee.

- section: 3-end-to-end-deadlines-cancellation-and-retry-budgets
  > semantically idempotent, or protected by an application effect key

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 5. T6-A06 — T6

**Question.** What distinguishes head-based from tail-based trace sampling, and why can head
sampling alone fail to retain every trace that contains an error?

**Phase-3 label.** answerable
**Adjudicated label.** answerable

**Answer key.** Head sampling decides early, often from the trace ID and a target percentage,
without inspecting the finished trace; this keeps whole traces at a consistent rate but cannot
condition on errors or total latency. Tail sampling waits until all or most spans are available
and can sample by error presence, overall latency, span attributes, or attributes that identify
a newly deployed service. That is why a team wanting every error trace may need tail sampling,
possibly after an initial head-sampling stage.

**Proposed support.**

- section: 4-sampling-limits-what-the-trace-can-support
  > | Head sampling | Can limit collection near request start | Later severe error may be missed
  > |

- section: 4-sampling-limits-what-the-trace-can-support
  > | Tail sampling | Can prefer slow/error traces using fuller context | Requires buffered
  > state and collector resources; decisions can be late |

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 6. T1-U01 — T1

**Question.** Which internal data structure and coordination protocol does a named commercial
managed cache use to coalesce concurrent misses across its nodes?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 7. T2-U02 — T2

**Question.** Which cloud queue service currently charges the least per million messages at list
price?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 8. T3-U03 — T3

**Question.** Which consensus protocol and quorum sizes does a particular proprietary managed
database service use internally for leader election?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 9. T4-U04 — T4

**Question.** What CPU and memory allocation should an outbox relay use to sustain 20,000 events
per second?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 10. T5-U01 — T5

**Question.** What exact per-gigabyte price will a named cloud provider charge this organization
for cross-region replication traffic in its next contract year?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 11. T1-A06 — T1

**Question.** How does probabilistic early expiration (XFetch) reduce stampedes without a lock?

**Phase-3 label.** answerable
**Adjudicated label.** unanswerable

**Answer key.** Each request independently decides whether to refresh the cached value before
its nominal expiry, with a probability that rises as expiry approaches. A common test refreshes
when current time minus delta times beta times the logarithm of a random value has reached the
expiry, where delta is the observed regeneration time and beta is typically 1.0. One request
refreshes slightly early while the others keep serving the cached value, smoothing the spike.
The cache item must also store delta and, when expiry is not readable, the expiry time.

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 12. T2-A03 — T2

**Question.** For an M/M/1 server whose mean service time is fixed, by what factors do the mean
sojourn time and the mean number of jobs in the system increase when utilization rises from 0.5
to 0.9?

**Phase-3 label.** answerable
**Adjudicated label.** unanswerable

**Answer key.** Mean sojourn time is tau/(1 - rho), so it rises from 2 tau at rho = 0.5 to 10
tau at rho = 0.9, a fivefold increase. Mean system size is rho/(1 - rho), which rises from 1 to
9, a ninefold increase. This divergence as rho approaches 1 is why modest utilization changes
near saturation produce much larger latency and backlog changes.

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 13. T3-A05 — T3

**Question.** What does Flexible Paxos relax about quorum intersection, and what does that
relaxation permit in a six-acceptor deployment?

**Phase-3 label.** answerable
**Adjudicated label.** unanswerable

**Answer key.** Flexible Paxos shows that Paxos needs intersection only between phase-1 and
phase-2 quorums, not majority quorums in both phases, and phase-2 quorums may even be disjoint
from each other. With six acceptors, where a strict majority is four, a deployment may use
phase-1 quorums of four and phase-2 quorums of three because 4 + 3 exceeds 6. For an even number
of acceptors this can shrink the second-phase quorum by one and improve steady-state
availability.

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 14. T5-A03 — T5

**Question.** With a replication factor of three, how does Apache Cassandra choose the replicas
for a key, and what benefit and what risk come from giving each physical node many tokens?

**Phase-3 label.** answerable
**Adjudicated label.** unanswerable

**Answer key.** A coordinator hashes the partition key to a position on the token ring and walks
clockwise until it has met three distinct nodes, which become the replicas. Giving each physical
node multiple tokens, called virtual nodes, makes a small cluster behave like a larger one, so a
new or decommissioned node exchanges roughly equal data with many neighbours. The trade-off is
that every token adds up to 2*(RF-1) neighbours, increasing the number of failure combinations
that can make part of the ring unavailable and adding repair work.

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

## 15. T6-A03 — T6

**Question.** For a 99.9% SLO, what long and short windows, burn rates, and error-budget
percentages does the Google SRE Workbook recommend for page and ticket alerts?

**Phase-3 label.** answerable
**Adjudicated label.** unanswerable

**Answer key.** It recommends two page-level rules: a 14.4 burn rate over a one-hour long window
and a five-minute short window, consuming 2% of the budget, and a 6 burn rate over a six-hour
long window and a 30-minute short window, consuming 5%. A ticket-level rule uses a burn rate of
1 over a three-day long window and a six-hour short window, consuming 10% of the budget. The
short window is one-twelfth the long window.

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

