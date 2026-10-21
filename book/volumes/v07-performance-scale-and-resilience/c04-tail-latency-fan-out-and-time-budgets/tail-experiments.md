---
metadata_version: 1
id: "tycho.page.c8b09f5ad28441ab89a6d9e06e0ff4c9"
kind: "page"
parent_id: "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/tail-experiments.md"
title: "Latency measurement and competing remedies"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Which observation would favor retaining, hedging or splitting a path?"
route_hints:
  questions:
    - "Which observation would favor retaining, hedging or splitting a path?"
  prerequisites:
    - "tycho.page.e229cbbcdc4a45bb9e368313f129b25b"
  related_ids:
    - "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "tail"
    - "experiments"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-cascading"
    - "src.tail-at-scale"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.eb130a7f820544a2ba0e0883c0ce587b; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
# Latency measurement and competing remedies

**Owning question:** Which observation would favor retaining, hedging or splitting a path?

This page belongs to [V07/C04 — Tail latency, fan-out and time budgets](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:5 -->
## 5. Why test-tool latency can be deceptively low

A closed workload generator that waits for a response before issuing the next request reduces offered load when the system stalls. A test can therefore hide the backlog users would create under externally timed arrivals. Observe the demand schedule and **offered/admitted/completed rates separately**, not only completed-response histograms. Latency under open arrivals, bounded connection pools, drops, timeouts and queue age gives a different service picture.

For a representative evaluation:

- Define user-visible start/end points, full journey and correctness assertions before choosing percentile targets.
- Preserve a repeatable arrival schedule (bursts, skew, coordinated operations, client geography) and record its clock semantics.
- Instrument queue wait, service time, dependency subcalls, failed requests, cancelled calls, retry counts and error/timeout outcomes.
- Include the failed or timed-out *intended* user operations when computing success and latency SLOs; do not silently omit requests that never entered the measured service.
- Compare baseline and treatment at equivalent **offered** demand, resource ceilings and logical outcomes, with confidence/variance limits.
- Inject one failure at a time (slow shard, unavailable replica, pool exhaustion, degraded network) and verify both parent latency and recovery correctness.
- Report resource cost and load on the underlying infrastructure, not solely a smaller parent percentile.

The original [queueing chapter](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) explains why finite measurement windows and completed-only sampling require careful interpretation; [workload experiment design](../../../performance/workload-profiles-and-capacity-experiments.md) extends this with reproducible arrival and evidence expectations.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:6 -->
## 6. Worked decision: retain, hedge, or split?

**Fictional case:** A read page queries eight independent views, but only five are required for the user's core operation. The three optional views may be absent with a visible explanation. Parent p99 is not yet measured, and it is unknown whether all views share one backend. A proposed "optimization" is to split the service and hedge every call.

**Baseline option:** retain the existing topology, trace the critical path, bound queue/admission, and measure the distribution of required versus optional views. This adds little operational complexity and is testable.

**Conditional improvement:** enforce a cutoff for optional views; render the core result once the five required views meet their correctness gates. If independently healthy replicas exist, test a narrowly budgeted hedge **only** on a selected required idempotent read after controlled tail evidence is collected.

**Rejected for now:** mandatory eight-result synchronization, blanket retry/hedge multiplication and service decomposition chosen solely because one parent's p99 is high. These options may increase latency variance, resource use or uncertainty without preserving core outcomes.

**Falsifiable claim:** at the same offered request mix and resource budget, limiting optional waits produces fewer user-visible deadline misses *without* suppressing mandatory content or worsening sustained backend overload. Measure p95/p99 and outcome ratio with a defined window; if not supported, revert the treatment.


### Original latency-budget counterexample: a retry consumes the same deadline

Suppose a fictional API has a **300 ms total caller deadline**, two parallel dependency reads and a 40 ms response/composition allowance. A proposal grants each dependency a 220 ms timeout plus one 220 ms retry. An attempt starting at T=20 expires at T=240; the retry then has only about 60 ms and cannot complete within the caller deadline.

| Hypothetical timeline | Budget principle |
|---|---|
| T=0–20 ms: admission/authentication | The downstream work inherits **remaining** deadline, not initial 300 ms |
| T=20–240 ms: first dependency attempts | Protect capacity with bounded per-hop work and cancellation propagation |
| T=240 ms: one dependency times out | Only about 60 ms remain; a full 220 ms retry cannot complete on time |
| T=240–300 ms: optional fallback | Return degraded/explicit failure if allowed, not fabricated fully successful data |
| After T=300 ms: late commit/reply arrives | User timeout means outcome **unknown**, not that a prior write did not occur |

A hedge to a second replica can sometimes improve a read tail, but it multiplies dependency work and may exacerbate shared saturation. Hedging **mutations** without a stable intent/effect identity can create duplicate user-visible effects. Retry eligibility must consider idempotency and the *remaining* deadline; retry storms should be bounded by admission budgets and backoff policy.

The [gRPC deadline guidance](https://grpc.io/docs/guides/deadlines/) supports propagation of time budgets and the [AWS Builders' Library retries analysis](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) discusses retry amplification. They are design references, not a tested latency prediction. **Proposed, not run:** inject a slow dependency and a shared overload condition under the same offered requests, compare deadline correctness, successful results, duplicate effects and additional backend calls with and without hedging.

**Reversal:** if correct partial responses are impossible, prefer a clear deadline error and reconciliation to a misleading success; if one dependency is optional, a bounded fallback may be preferable to a retry that cannot fit. Actual workload correlations and observed distributions—not independent p99 multiplication—must determine architecture choice.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](deadline-hedging.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](tail-latency-fanout-and-deadline-budgets.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
