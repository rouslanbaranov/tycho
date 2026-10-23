# Phase 3 human review sample

Status: **human review pending**. No human review has been performed.

Sample: 9 of 43 items (20.9%).

Full paths and quotes are in evaluation/phase3-human-sample.json.

For each item: check the adjudicated label, support section and answer key.
Record agree/disagree, corrected label and notes. Do not edit frozen qrels.

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

## 9. T5-U01 — T5

**Question.** What exact per-gigabyte price will a named cloud provider charge this organization
for cross-region replication traffic in its next contract year?

**Phase-3 label.** unanswerable
**Adjudicated label.** unanswerable

**Human verdict.** [ ] agree  [ ] disagree  [ ] relabel

**Corrected label / notes.**

---

