---
metadata_version: 1
id: "tycho.page.43414664520b4866929f7f006f27f59b"
kind: "page"
parent_id: "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
canonical_path: "book/volumes/v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/deadlines-retries.md"
title: "Deadlines, cancellation and retry budgets"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "How should one end-to-end time budget bound nested calls and retries?"
route_hints:
  questions:
    - "How should one end-to-end time budget bound nested calls and retries?"
  prerequisites:
    - "tycho.page.e7e65b602c5a41fb80fa4a1e88a33298"
  related_ids:
    - "tycho.chapter.53b6bb88a00549e491949aeb426b83f2"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.de9c5bc478ba44718fcb731e69109dce"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "deadlines"
    - "retries"
evidence_scope:
  source_ids:
    - "src.http-semantics"
    - "src.sre-overload"
    - "src.sre-cascading"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.cccbd188936543a2aaf904f4002236d8; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-30"
source_inspection_date: null
content_verified_at: null
---
# Deadlines, cancellation and retry budgets

**Owning question:** How should one end-to-end time budget bound nested calls and retries?

This page belongs to [V02/C05 — Public APIs, HTTP/RPC and compatibility](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.cccbd188936543a2aaf904f4002236d8:3 -->
## 3. End-to-end deadlines, cancellation and retry budgets

A timeout on one socket is not a complete request deadline. The caller has an end-to-end business time budget; proxies, authentication, queueing, internal RPCs and durable state can consume it. An API must define which result is still meaningful after the caller stops waiting, and what resource cleanup follows.

The [gRPC deadlines guide](https://grpc.io/docs/guides/deadlines/) explains that an RPC deadline is the latest point at which the client is willing to wait; propagation between calls can subtract elapsed time and thereby limit an internal call to the remaining budget. Language-specific defaults and propagation configuration differ. The [gRPC cancellation guide](https://grpc.io/docs/guides/cancellation/) makes clear that cancellation of a call should stop initiated work where possible; user code may need to check and propagate the signal. **Cancellation is not proof that a previously committed effect was undone.**

A **hypothetical** 900-ms request budget could be partitioned into 50 ms of edge/auth overhead, 100 ms in queueing, 450 ms downstream work, 100 ms durable write, and 200 ms network/margin. These numbers are invented for illustration, not a target for any product. Per-hop independent 900-ms timeouts would allow the aggregate to vastly exceed the caller's deadline. At each hop the effective budget is at most the remaining time, subject to clock and propagation behavior. Critical cleanup and reconciliation may need to continue after the synchronous response budget expires, using an explicitly durable workflow rather than an unbounded request task.

The [gRPC retry guide](https://grpc.io/docs/guides/retry/) distinguishes transparent retries from configured retry policies; configurable retries are limited by status, attempts, backoff and commitment boundaries. A service configuration can also set per-method timeouts and retry/hedging behavior. These client mechanisms cannot infer application effect identity: an RPC retry is safe only when the underlying operation semantics and downstream effects allow it.

**Exponential backoff.** A retry delay should grow with each failed attempt, be capped, and be
randomized with jitter so clients do not retry in lockstep. The attempt cap, total delay and
remaining deadline bound the policy; server pushback/backpressure should reduce or stop
retries. Backoff does not make a non-idempotent effect safe.

**Timeout and deadline.** A timeout is a local wait bound on one operation; the request
deadline is the caller's end-to-end budget. Each hop should use at most the remaining
deadline, minus its own processing and margin, and propagate the remainder. Cancellation
stops work where possible but does not roll back a committed effect; an ambiguous timeout
requires outcome lookup.

**Alternatives.** Do not retry when the failure is permanent, the operation has no effect
identity, or the remaining deadline cannot fit the attempt; fail fast or queue. A shorter
local timeout with explicit cancellation may protect capacity better than a long caller
deadline. Propagate a deadline when the caller has a real end-to-end budget; use
independent timeouts only when each hop is genuinely independent.

**Retry decision contract:**

- First ask whether the operation is read-only, semantically idempotent, or protected by an application effect key.
- Retry only a documented retryable failure class, with a bounded total deadline and bounded attempt/backoff budget; observe server pushback/backpressure.
- Prefer explicit outcome lookup for an ambiguous durable command, rather than treating every timeout as “nothing happened”.
- Avoid retry amplification across proxy, API and downstream clients; designate where retries are owned and instrument actual attempt counts.
- Reject the assumption that a cancelled response retracts committed state or emitted events.

### Local overload versus broad overload

An error response does not by itself justify a retry. The decision also depends on how much
of the fleet is failing and on which layer observed the failure.

- **A small overloaded subset.** If one backend or a small fraction of instances is
  overloaded while other eligible instances have capacity, an immediate retry on another
  instance can redistribute work. The operation must still be safe to repeat, the remaining
  deadline must allow it, and the retry must consume the same budget.
- **Broad overload.** If a large fraction of instances is overloaded, another attempt is
  likely to meet the same condition. Return an explicit overload result and let the caller
  decide. A backend should propagate a specific "overloaded; do not retry" signal rather
  than a generic error that every layer retries.
- **Retry at one layer.** Retry only at the layer immediately above the layer that rejected
  the request. Lower layers should return a classified result, not independently retry work
  that the caller has already judged non-retryable. This avoids a combinatorial retry
  explosion across proxy, API, service and client layers.

### Three retry budgets

A per-request attempt cap bounds one logical operation. It does not bound the aggregate work
created by many clients. Use complementary budgets:

- **Per-request attempt cap.** Bounds attempts for one logical operation and consumes the
  remaining deadline. It does not bound aggregate retry load.
- **Per-client retry ratio.** Bounds retries relative to a client's recent original
  requests. Sparse clients may lack enough history for a stable ratio; do not treat the
  ratio as a guarantee or as a substitute for a deadline.
- **Process- or service-wide retry budget.** Caps total retry work across clients and
  operations. This is the one budget that directly protects a shared dependency from a
  retry storm.

The source's example thresholds are contextual. Use measured failure rates, deadlines and
dependency capacity; record the chosen budgets and the observations that would change them.
Count original attempts and retries separately, and measure retry amplification by layer.

[Handling Overload](https://sre.google/sre-book/handling-overload/) and
[Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
describe the local-versus-broad distinction and complementary retry budgets. Their numeric
thresholds are examples, not defaults.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Retry with Exponential Backoff](../../v11-pattern-atlas/c07-resilience/README.md#retry-with-exponential-backoff) — decision conditions and contraindications.
> [Retry with Jitter](../../v11-pattern-atlas/c07-resilience/README.md#retry-with-jitter) — decision conditions and contraindications.
> [Timeout](../../v11-pattern-atlas/c07-resilience/README.md#timeout) — decision conditions and contraindications.
> [Deadline Propagation](../../v11-pattern-atlas/c07-resilience/README.md#deadline-propagation) — decision conditions and contraindications.


## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](effect-identity.md) |
| Next | [Continue the reasoning](version-compatibility.md) |
| Integrated question | [Original scenario and limits](http-rpc-contracts-and-compatibility.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

These notes define the decision boundary for atlas cards whose mechanism is not the main subject of
this page. They are synthetic design guidance, not measured evidence, and they do not create a new
source claim.

### Retry with Jitter

Jitter randomizes each retry delay so independent clients do not retry in lockstep, spreading
attempts across a window or adding a random offset to an exponential base. Every attempt must
consume the same end-to-end deadline and attempt budget, so added delay cannot extend the caller's
useful completion window.

Synchronized retries convert a brief failure into a sustained overload; compare actual attempt
counts and retry arrivals with the planned budget and stop the retry policy when pushback persists.
Retry without jitter at a single layer, or do not retry at all when the failure is non-retryable;
add jitter when many clients share the same dependency and retry signal.

**Limits.** Jitter reduces synchronization but does not bound aggregate load; a retry storm can
still overload a shared dependency, and the policy must respect the deadline and cancel
remaining attempts.

**Jitter bound.** Sample the delay inside `[0, min(backoff_cap, remaining_deadline)]`;
a spread narrower than the client population still synchronizes, while a wider one spends the
caller's budget. Retry only when the operation has a stable effect identity or is naturally
idempotent; jitter cannot make a non-idempotent effect safe.

### Retry with Exponential Backoff

Grow the delay after each failure, cap it and add jitter so clients do not synchronize. State the
attempt count, base, multiplier and aggregate budget across calls; the curve alone is not a policy.
The cap and the caller's remaining deadline bound the useful window, not a fixed attempt count.
For retry n (n=1 is the first retry), sleep a jittered value in
[0, min(cap, remaining_deadline, base * multiplier^(n-1))].

Budget retries per dependency and caller class in addition to a service-wide cap; a single global
counter alone can let one failing dependency starve unrelated calls. Emit attempt and
terminal-outcome labels, and reset the budget only after a healthy window. When the budget is
exhausted, return the overload result and let the caller choose fail-fast or queue; do not retry a
permanent failure or an operation without effect identity. Stop when the server signals pushback;
the budget is not permission to ignore backpressure.

The policy needs an owner and a visible attempt metric; an exponential curve without a deadline
check can spend the caller's budget after the result stopped being useful.

### Timeout

A timeout is a local wait bound on one operation; the request deadline is the caller's end-to-end
budget. Each hop should use at most the remaining deadline, minus its own processing and margin,
and propagate the remainder.

Timeout expiry does not mean the effect did not commit. Prefer explicit outcome lookup for an
ambiguous durable command, rather than treating every timeout as "nothing happened". A shorter
local timeout with explicit cancellation may protect capacity better than a long caller deadline,
provided the cancellation path is tested and the caller can reconcile.

Name the timeout owner, the unit (connect, read, total) and the retry interaction; a timeout that
silently becomes a retry can multiply load. The timeout value must be observable.

### Deadline Propagation

Deadline propagation carries the caller's remaining budget as a relative duration. gRPC
converts the caller's absolute deadline to a timeout with the elapsed time already deducted
before propagating it, so hosts do not need synchronized wall clocks. Google SRE describes
the same request tree as sharing one absolute deadline, then gives each hop the remaining
seconds after its own processing. The accounts agree only when the absolute deadline is
fixed at ingress and every hop transmits the remainder; that reconciliation is a Tycho
reading, not a source instruction.

The relative duration is measured against a local elapsed-time source. Use monotonic clocks
so wall-clock adjustments cannot move the boundary; the guides do not require this, so it
is Tycho guidance. The ingress sets the budget and each hop checks expiry before starting
work. Enforcement is split: a gRPC server automatically cancels a call once the client
deadline passes, and the client fails with `DEADLINE_EXCEEDED`; the application must still
stop any work it spawned and check cancellation. Google SRE says each stage should check the
deadline before doing more work. A propagated value without such an enforcement point is
only a hint.

If a hop sends an absolute timestamp instead of a relative value, define a bounded skew and
reject or clamp values outside it. The selected sources do not specify a tolerance, so the
bound is Tycho guidance. Detached asynchronous work gets its own durable deadline rather
than inheriting the request's remaining time.

Clock skew, a lost timeout header and a hop that ignores expiry are the common failures.
gRPC's conversion removes the clock-synchronization dependency, but the protocol defines
an omitted `grpc-timeout` header as an infinite timeout, so a lost header silently removes
the bound. A hop that ignores expiry keeps working for a caller that has already given up.
On expiry, cancel the work and record the outcome; cleanup or reconciliation runs in an
explicitly durable workflow. Requiring a deadline at ingress, rejecting a missing
propagated deadline on bounded paths, and moving cleanup to durable work are Tycho
guidance; cancellation itself is source-supported.

Use propagation when the caller has a real end-to-end budget; independent per-hop timeouts
fit only when the hops are genuinely independent.

**Source boundary.**

- gRPC, "Deadlines", `read.grpc-deadlines.2026-10-30`, source Markdown
  `e310a0e5a4bdc8f353ef04a641336d9a51176ffaa0ba0ee8b8b1aad98263a900`:
  "Deadline Propagation" (conversion to an elapsed-adjusted timeout), "Deadlines on the
  Server" (automatic cancellation and application responsibility) and "Deadlines on the
  Client" (`DEADLINE_EXCEEDED`).
- Google SRE, "Addressing Cascading Failures", `read.batch4-sre-cascading.2026-10-21`,
  revision `d67024d52d72a1254c830d3c29e6d1b2afade88e133ffcff64b94711c2aaa11a`:
  "Latency and Deadlines" (per-stage deadline checks, the absolute-deadline description
  and the remaining-seconds example).
- gRPC, "gRPC over HTTP2", `read.grpc-protocol.2026-10-30`, source Markdown
  `b51ea1b8cee67ad3477e73152bb60ac3ebf6e164962b46ba79434e980739256f`:
  "Requests" (`grpc-timeout` relative units; an omitted timeout means an infinite
  timeout).
- Limits: the sources specify protocol and operational guidance, not a tested
  implementation or a numeric clock-skew bound.
