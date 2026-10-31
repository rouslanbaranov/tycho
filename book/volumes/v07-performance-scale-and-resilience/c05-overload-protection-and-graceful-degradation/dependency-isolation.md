---
metadata_version: 1
id: "tycho.page.80ab784dafed47a7baf31722fce5eabc"
kind: "page"
parent_id: "tycho.chapter.0718556e0eb14d499adbbe67073327df"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md"
title: "Bulkheads, retries and optional dependencies"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How can failure in optional work starve core work?"
route_hints:
  questions:
    - "How can failure in optional work starve core work?"
  prerequisites:
    - "tycho.page.d9abd43bb7394c04a6bf77d4014f870d"
  related_ids:
    - "tycho.chapter.0718556e0eb14d499adbbe67073327df"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.62ad1ae9e0d243d69b08be0ff32930a1"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "dependency"
    - "isolation"
evidence_scope:
  source_ids:
    - "src.resilience4j"
    - "src.microsoft-cloud-patterns"
    - "src.aws-backoff"
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.c5d20ae7ef6445e5b23dd5fbac625060; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-31"
source_inspection_date: null
content_verified_at: null
---
# Bulkheads, retries and optional dependencies

**Owning question:** How can failure in optional work starve core work?

This page belongs to [V07/C05 — Overload protection and graceful degradation](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:4 -->
## 4. Bulkheads, circuit breakers and retries have different responsibilities

| Control | Primary purpose | Dangerous misuse |
|---|---|---|
| Admission/rate limit | Bound offered or admitted work before resource exhaustion | Hide rejected attempts from service-level outcomes |
| Queue limit/deadline | Bound waiting memory and usefulness | Queue accepted irreversible writes without durable tracking |
| Bulkhead | Reserve bounded workers/pools for independent classes/dependencies | Partition too tightly and waste capacity, or allow bypass |
| Circuit breaker | Avoid repeated costly calls to a failing dependency; probe recovery | Treat opening the breaker as permanent recovery or a substitute for backpressure |
| Retry budget + jitter | Spread bounded safe transient retries across time | Multiply load during outage or repeat non-idempotent effects |
| Load shedding | Discard lower-priority eligible work when explicitly permitted | Silently lose acknowledged business commands |
| Optional feature degradation | Preserve core outcome when nonessential enrichment fails | Present missing mandatory data as a complete result |

Across multiple layers, retries compound. If three independent layers make three attempts per incoming logical operation, a pathological path can create up to **27 downstream attempts** per logical intent (under a deliberately simplified fully nested retry model). No such amplification was observed here. [AWS Builders' Library retry and jitter discussion](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) explains why coordinated repeated retries can worsen overload. [Tycho's RPC and idempotency chapter](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md) owns effect-safe retry identity.

**Circuit-breaker alternative.** A retry budget with jitter, admission/rate limit, or a
bounded timeout may be preferable when failures are not fast, when the dependency recovers
quickly, or when an open breaker would hide a local resource problem. Reverse the breaker
choice when its state adds more coordination than the repeated-call cost it avoids.

**Bulkhead failure and alternative.** Bulkhead bypass, undersized partitions and a shared
hidden queue can defeat isolation; detect per-pool queue age, utilization and rejected
work, and rebalance or fail the isolated class explicitly. Admission/rate limiting may be
preferable when one global resource can be bounded directly; a circuit breaker may be
preferable when the failure is dependency-specific rather than capacity-specific.

The generic retry decision contract, including local-versus-broad overload and the
per-request, per-client and service-wide budgets, is owned by `V02/C05`
(`tycho.page.43414664520b4866929f7f006f27f59b`). This section owns the overload regime and
the isolation boundary; `V04/C04` (`tycho.page.33399db8d1574330951d9954801d6e71`) owns
effect identity and retention.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Circuit Breaker](../../v11-pattern-atlas/c07-resilience/README.md#circuit-breaker) — decision conditions and contraindications.
> [Bulkhead](../../v11-pattern-atlas/c07-resilience/README.md#bulkhead) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:5 -->
## 5. Original synthetic failure: one optional dependency poisons core work

A fictional public trail guide serves a **required** trail description and an **optional** community photo suggestion. Both initially use one shared worker pool. During a picture-service slowdown, photo calls hold most workers; required trail descriptions fail their deadlines even though authoritative trail records remain healthy.

**Candidate A:** enlarge the shared pool. It might only increase calls to the failing photo dependency and thread/buffer use. **Candidate B:** give optional images a separate small concurrency budget, deadline and circuit breaker; serve core trail information without the optional image when its deadline expires. **Candidate C:** queue user operations for minutes waiting on the photo service—contradicts the intended interactive contract.

A bounded test (not executed) would keep offered arrival schedule and resource ceiling equal, inject image-service slowness and observe correct core responses, missing-photo labelling, queue age, retry attempts, errors and recovery. A result where A appears faster only because it drops unknown user attempts is invalid.

The optional nature of photos is a **fictional stated requirement**. If actual user safety depends on a recent trail-closure update from another service, substituting stale information would be unacceptable; the safe response might need a clearly denied/unknown result.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](admission-resource.md) |
| Next | [Continue the reasoning](overload-recovery.md) |
| Integrated question | [Original scenario and limits](overload-admission-control-and-graceful-degradation.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

### Circuit Breaker

**Mechanism — a three-state proxy around one dependency (Tycho summary, source-bound).** A
circuit breaker is a state machine around one dependency: closed counts outcomes over a rolling
window, open rejects fast for a cooldown, half-open admits a bounded probe. Resilience4j says its
CircuitBreaker "is implemented via a finite state machine with three normal states: CLOSED, OPEN
and HALF_OPEN" and uses "a sliding window to store and aggregate the outcome of calls." Azure
says the proxy can be implemented "as a state machine that includes the following states": closed
routes the request and counts failures, open fails immediately, and half-open admits "a limited
number of requests." The state model is source-bound; one breaker per dependency, scoped to the
failure it can observe, is Tycho's rule.

**Invariant — a rate threshold needs a volume gate (Tycho rule, source-bound).** Threshold
semantics need both a rate and a minimum volume. Resilience4j says the failure rate "can only be
calculated, if a minimum number of calls were recorded"; with nine calls recorded and a minimum
of ten, "the CircuitBreaker will not trip open even if all 9 calls have failed." Its default
`minimumNumberOfCalls` is 100. Azure says "the failure threshold triggers the Open state only
when a specified number of failures occur during a specified interval." The sources disagree at
the boundary: Resilience4j trips when the rate is "equal or greater" than the threshold, while
Azure says the count "exceeds" it. Tycho's rule: declare and test the comparison, count only
calls recorded in the current window, and keep failed calls, slow calls, ignored exceptions and
rejected calls in separate counters. A rejected call is not a dependency failure.

**Failure and recovery — open is a hypothesis, half-open is a bounded probe (Tycho runbook,
source-bound mechanics).** The open state records why it opened and the cooldown; half-open
admits a bounded number of probes and closes only after consecutive successes. Resilience4j
says that after the wait duration it "permits a configurable number of calls" and rejects
further calls "until all permitted calls have completed"; Azure says a limited number of
requests pass and "if any request fails" the breaker reverts to open. Azure says "The Half-Open
state helps prevent a recovering service from suddenly being flooded with requests" and that
"System recovery is based on external operations," so open is not recovery. Tycho's warning:
an open caused by local resource exhaustion hides the real bottleneck. Azure scopes the pattern
to remote services and lists local private resources as a contraindication; SRE's utilization
signals are "based on the state local to the task." Attribute a rejection to the dependency only
when dependency-local failures, not local saturation, drove it. An open breaker still needs an
explicit fallback or fail-fast contract; a fallback that calls the same dependency or an
unbounded alternate path only hides the outage.

**Alternative — retry budget, rate limit or bounded timeout (Tycho choice rule, source-bound
trade-offs).** AWS says retries are "selfish" and that circuit breakers "can introduce
significant addition time to recovery"; it mitigates the risk "by limiting retries locally using
a token bucket." It also says jitter "adds some amount of randomness to the backoff to spread the
retries around in time." Google SRE caps retries with a per-request budget "of up to three
attempts" and a per-client ratio below 10%, and caps outgoing traffic so that "requests above the
cap fail locally without even reaching the network." SRE says that when a large subset of tasks is
overloaded, "requests should not be retried and errors should bubble up all the way to the caller
(e.g., returning an error to the end user)." AWS makes the timeout a budget too: "Setting a
timeout too high reduces its usefulness, because resources are still consumed while the client
waits for the timeout." Azure contrasts the breaker with retry and says waiting for a reset
"might introduce unacceptable delays"; it also warns that a breaker "might not fully protect
applications from failures in external services that have long time-out periods." Tycho's rule:
bound the timeout first, because a breaker cannot shorten a call that never returns. Use a
breaker when failures are dependency-local, observable and repeated calls amplify them, whether
the symptom is an error or a slow call. When failures are caller-specific or caused by local
saturation, prefer a retry budget with jitter, a rate limit or a bounded timeout. Reverse the
choice when state coordination and fallback complexity cost more than the calls they avoid.

**Source boundary.** Public sources accessed 2026-10-31; documentation and engineering articles,
not benchmarks or executed tests. Quotes are short excerpts. Markdown escapes, emphasis, curly
quotes and link-extraction spacing are normalized; Tycho-labelled sentences are synthesis, not
source claims. Proposed records (not yet in the shared ledger):

- Resilience4j, "CircuitBreaker" documentation, Markdown alternate, 326 lines and 2,481 words,
  SHA-256 `cad62135427cfee85f2c80095c3b823854aa36d4314a0fd829fa956022036e94`; the existing
  `read.batch4-r4j-circuit.2026-10-21` record has the same digest and is revalidated. The page is
  rolling documentation with no published version; the digest pins the representation.
- Microsoft Azure Architecture Center, "Circuit breaker pattern," `ms.date` 2025-02-05, pinned to
  `MicrosoftDocs/architecture-center` commit
  `9fdb775034a2faf6b2dcf699fb870d49fe50c992`; Markdown 187 lines and 3,744 words, SHA-256
  `29baeab9e19c54c9fdae01dfa4c431bae0c6811e0c5267a1d6c8c78267b8146e`; live raw HTML SHA-256
  `5b83f1575092478594cf049c4c4a0a8505b9bdc851f6db4fbee3d9dd979c1655`; canonical text SHA-256
  `29299b3b788328f0ec127c6f37b5f7bfb6ffc0d4a6bab37d4a0d81b5a4614274`; record
  `read.microsoft-circuit-breaker.2026-10-31` proposed.
- AWS Builders' Library, "Timeouts, retries, and backoff with jitter," published 2019-12-05;
  raw HTML SHA-256
  `d289c95d849b6d082f8b9aac64f1df92d7383d9b49ff3326d4d181ba8140f636`; canonical text SHA-256
  `c076aeb3beeb4766568d3cf85c5ffda79be9610be186159b925ceb882addfc94`; record
  `read.aws-builders-timeouts-retries.2026-10-31` proposed.
- Google SRE, "Handling Overload," 2017, CC BY-NC-ND 4.0; raw HTML SHA-256
  `945d15db67ad15a7f5e75833f8c0d014c8dc61d57909f7a3abd48459ad12cc9e`; canonical text SHA-256
  `8154963544456669d31fb2666db9f6a6a91ea0d4135d01d30e41922172a71bf2`; the existing
  `read.sre-overload.2026-10-21` record is revalidated.

### Bulkhead

A bulkhead reserves bounded workers or pools for independent classes or dependencies. The boundary
contains one class's saturation so it cannot consume every worker, but it does not create capacity.

Partition too tightly and waste capacity, or allow bypass. A bulkhead bypass, undersized partition
or shared hidden queue can defeat isolation; detect per-pool queue age, utilization and rejected
work, and rebalance or fail the isolated class explicitly. Measure the partition you actually
enforce, not the pool name.

Admission/rate limiting bounds a shared resource; a circuit breaker rejects calls to a failing
dependency; a bulkhead bounds concurrent capacity per class. Use a bulkhead when classes have
genuinely different latency and failure budgets and an owner. Capacity reservation must be
enforced by the admitting scheduler; a label on a shared pool is not a boundary.

