---
metadata_version: 1
id: "tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e"
kind: "page"
parent_id: "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c03-load-test-methods-and-benchmark-validity/load-testing-and-benchmark-validity.md"
title: "Load-test methodology, generator validity and defensible benchmark evidence"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated decision and bounded source limits for Load-test methods and benchmark validity. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "How do open/closed arrivals, warmup and coordinated omission bias conclusions?"
  prerequisites: []
  related_ids:
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.page.49d9df04c0b4488e936b02e580a62271"
    - "tycho.page.35d5be6a4e074758afff95bf3ec68bc5"
    - "tycho.page.bfa3a283746b42998825234aca63b101"
    - "tycho.page.180a25e8e7504ef4aa52257f76dbd1a8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Load-test"
    - "methodology"
    - "generator"
    - "validity"
    - "and"
    - "defensible"
    - "benchmark"
    - "evidence"
evidence_scope:
  source_ids:
    - "src.sre-overload"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-21"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:-1 -->

# Load-test methodology, generator validity and defensible benchmark evidence

> **Tycho V07/C03 integrated decision (2026-10-19).** Original method and fictional examples. Primary public k6, HdrHistogram and SRE documentation is cited at limited scope. No test run, recorded benchmark, independent statistical review, or hardware comparison was performed. This page does not claim that a threshold or test tool creates an architecture decision automatically. The content_review field retains the decomposition-era draft state; no independent acceptance is asserted.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.1cfb9cfdf1604fada0f508c123fe8b2e:0 -->
## Purpose and mission

A performance benchmark can produce precise-looking numbers while measuring the wrong population. A system that slows its *load generator* may appear more responsive than one that actually serves its intended traffic. A synthetic workload whose key distribution, user decisions or failure mix does not resemble the stated engineering problem may yield impeccable charts and still choose an unsuitable architecture.

The objective is to design a test whose **demand, observation, correctness and resource boundaries are reproducible and honestly limited**. The [workload and capacity-experiment chapter](../../../performance/workload-profiles-and-capacity-experiments.md) describes what demand variables to model; [queueing](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) gives mean mathematical boundaries; [tail latency](../c04-tail-latency-fan-out-and-time-budgets/tail-latency-fanout-and-deadline-budgets.md) explains why parent latency is not a simple addition of per-hop percentiles. This chapter owns the **validity protocol**.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Choose an arrival model, warm-up policy and outcome accounting that preserve the workload being tested.

A closed-loop generator can reduce offered demand when the system slows, masking the backlog an external arrival stream would create.

The detailed pages separate the mechanisms that make this decision conditional:

- [Experiment claims, arrival models and denominators](arrival-design.md) — Which offered workload must a load generator preserve while the system slows?
- [Confounders, fault injection and acceptance](benchmark-controls.md) — Which invariant and distribution must remain comparable across benchmark variants?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
