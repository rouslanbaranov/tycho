---
metadata_version: 1
id: "tycho.page.a2cd4465792a4740aa5150ad248fd420"
kind: "page"
parent_id: "tycho.chapter.ee2cd95003ab4018a9d49e2ff0b6b2f4"
canonical_path: "book/volumes/v01/c04/architecture-evidence-hypotheses-and-experiments.md"
title: "Architecture evidence, competing hypotheses and decision experiments"
topic_ids:
  - "application-architecture"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Evidence, hypotheses and architecture experiments. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What do sources, estimates, simulations and measurements actually prove?"
  prerequisites: []
  related_ids:
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.be90d29e1bc04524b2ea41ee9beaab0f"
    - "tycho.page.4318e542ac7e445b9e8b3150effd2cff"
    - "tycho.page.06b70cb83d4f490ea9ef698a025e7684"
    - "tycho.page.f05854fcc406435bbf38a192bc7ab2f1"
    - "tycho.page.d8118d40313143e4ac47323274fbb594"
    - "tycho.page.3a5cdaf97d0b4e51ae5828507f033dd0"
    - "tycho.page.dff5d6affea243cca3c426d04d290802"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Architecture"
    - "evidence"
    - "competing"
    - "hypotheses"
    - "and"
    - "decision"
    - "experiments"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:-1 -->

# Architecture evidence, competing hypotheses and decision experiments

> **Tycho manuscript V01/C04 (2026-10-19).** Original experimental method and invented example; bounded public arc42 and SRE materials reviewed. No benchmark, controlled fault, actual source inspection of a target application, statistical acceptance or independent expert review has been executed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:0 -->
## Purpose and mission

A design opinion is often expressed as an empirical claim: “a cache will reduce latency,” “a queue prevents failure,” or “splitting a service improves availability.” Such claims are incomplete without a workload, a correctness definition, an alternative causal explanation and a way to falsify the benefit.

A **source-backed architectural assertion** can be grounded in a published specification, while a **system-specific architectural benefit** generally requires evidence at its own target boundary. Published PostgreSQL or Kubernetes documentation explains configurable mechanisms; it does not demonstrate that one configuration improves an invented application.

This chapter distinguishes a claim's source and scope from a testable engineering hypothesis, and establishes a small experiment lifecycle. The existing [capacity-experiment page](../../../performance/workload-profiles-and-capacity-experiments.md) supplies detailed load-test methods; [benchmark validity](../../v07/c03/load-testing-and-benchmark-validity.md) owns generator and measurement traps.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.a2cd4465792a4740aa5150ad248fd420:8 -->
## Engineering walkthrough — A falsifiable cache-versus-query experiment

**Original preregistered hypothetical study.** The symptom is a p99 increase on item-detail reads. Hypothesis H1 says repeated reads dominate and a bounded-freshness cache helps; rival H2 says PostgreSQL plan regression raises latency even for misses; H3 says connection acquisition—not SQL execution—is the bottleneck. The experiment must test *all three*, rather than select a cache before measuring.

Before any run, freeze the offered arrival trace, key skew, dataset snapshot, query/index definitions, pool size, application build, cache warm/cold state, permitted staleness and error deadline. Predeclare **correct completions**, p99 distribution with sample size, cache hit/miss split, DB plan and lock/pool wait, and changed/incorrect reads as acceptance observables.

| Controlled comparison | Expected discriminating result | Invalid inference |
|---|---|---|
| Baseline versus query/index repair | Lower DB execution time if H2 is true | A changed EXPLAIN cost alone proves user latency improved |
| Baseline versus cache-aside with write injection | Lower read load when H1 is true, bounded stale fraction | Cache hit rate proves authorization or freshness correctness |
| Baseline versus bounded pool admission | Lower queue delay if H3 is true | Higher accepted RPS proves more *correct* outcomes |

**Negative result example, invented:** a warm-cache run improves mean latency but violates the permitted stale-read window during concurrent updates. This **rejects that candidate** even if p99 looks attractive; it does not prove caches are inherently wrong. If plan repair achieves the requirement with lower operational complexity, prefer it until evidence reverses the decision. Mark official manuals as *specification*, any eventual run as *observed experiment*, this scenario as *synthetic*, and every unmeasured causal claim as *hypothesis*. No experiment was run.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Keep published semantics, synthetic arithmetic, hypotheses and observed experiments as distinct evidence classes with different permissible conclusions.

A cache experiment can improve latency while failing freshness; the result rejects that configuration rather than proving a universal claim about caching.

The detailed pages separate the mechanisms that make this decision conditional:

- [Evidence classes and competing hypotheses](evidence-hypotheses.md) — Which evidence class supports a claim and which alternative explanation remains possible?
- [Discriminating architecture experiments](experiment-contract.md) — What observation would distinguish cache benefit from query repair?
- [Negative evidence and stopping rules](negative-results.md) — When should an attractive candidate be rejected or research stop?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
