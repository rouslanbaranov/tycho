---
metadata_version: 1
id: "tycho.page.35c975574fa3b7088402ce5dd037c4f5"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/circuit-breaker.md"
title: "Circuit Breaker"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Circuit Breaker; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should calls to a failing dependency be rejected early until it recovers?
  prerequisites:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  related_ids:
    - "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "circuit breaker"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.resilience4j"
    - "src.microsoft-cloud-patterns"
    - "src.aws-backoff"
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.batch4-r4j-circuit.2026-10-21,
    read.microsoft-circuit-breaker.2026-10-31,
    read.aws-builders-timeouts-retries.2026-10-31 and the retained
    read.sre-overload.2026-10-21 record; owner section and limits are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Circuit Breaker

**Identity.** Circuit Breaker; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should calls to a failing dependency be rejected early until it
recovers?

**Good-fit conditions.** Failures are dependency-local and observable; the symptom may be an
error or a slow call (slow-call signal is Tycho); a bounded timeout and deadline exist; the
rolling window, minimum request volume and threshold comparison are defined; a half-open probe
is bounded and safe; the fallback or fail-fast contract is defined; rejected calls are measured
separately.

**Hard contraindications.** Reject when a circuit would hide a required dependency, when the
caller cannot bound the call duration, or when recovery probing would overload it. Prefer a retry
budget with jitter, a rate limit or a bounded timeout when failures are caller-specific or
caused by local saturation.

**Competing alternative.** For caller-specific or local failures, a retry budget with jitter,
rate limit or bounded timeout. AWS notes that breakers can add recovery time and limits retries
locally with a token bucket; Google SRE caps retries per request and per client. Reverse the
choice when state coordination and fallback complexity cost more than the calls they avoid.

**Failure and recovery.** Open is a hypothesis, not recovery; local saturation can masquerade
as a dependency failure, and a fallback can hide the outage. Probe with a bounded budget,
attribute rejections to the dependency only when dependency-local failures drove them, and do
not treat open as recovered.

**Technical owner.** [Circuit Breaker](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/dependency-isolation.md#circuit-breaker) — dependency isolation is bounded, not a full circuit-breaker library guide.

**Sources.** [src.resilience4j](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.batch4-r4j-circuit.2026-10-21`: Markdown alternate, 326 lines and
2,481 words. [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-circuit-breaker.2026-10-31`: sections "Context and problem",
"Solution", "Problems and considerations", "When to use this pattern" and "Workload design".
[src.aws-backoff](../../../../edition/patterns/reading-ledger.v1.json) read record
`read.aws-builders-timeouts-retries.2026-10-31`: sections "Introduction", "Failures Happen",
"Timeouts", "Retries and backoff", "Jitter" and "Conclusion". The retained
[src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json) record
`read.sre-overload.2026-10-21`: sections "Handling Overload", "Client-Side Throttling",
"Client request rejection probability", "Handling Overload Errors", "Deciding to Retry",
"Utilization Signals" and "Conclusions". The sources are public documentation and engineering
articles, not benchmarks; Tycho-labelled rules are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Bulkhead; Retry with Exponential Backoff; Timeout; Fallback.
