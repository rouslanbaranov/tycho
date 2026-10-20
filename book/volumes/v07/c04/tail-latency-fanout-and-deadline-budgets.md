---
metadata_version: 1
id: "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
kind: "page"
parent_id: "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
canonical_path: "book/volumes/v07/c04/tail-latency-fanout-and-deadline-budgets.md"
title: "Tail latency, fan-out and end-to-end deadline budgets"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Integrated question, original scenario and transfer limits for Tail latency, fan-out and time budgets. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Why can p99 degrade despite adequate mean capacity?"
  prerequisites: []
  related_ids:
    - "tycho.page.a9a28aaa4d1e4e9cb0accd2fc2c5ba9b"
    - "tycho.page.f784d6ef723c4c0e8836ff9085bf7dcc"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.landing.b08f16ced4a142a785c37b43eb340260"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.1e89567050974052b13ba62b3b44484f"
    - "tycho.page.45935212b3b7476d8a163520f065b825"
    - "tycho.page.e229cbbcdc4a45bb9e368313f129b25b"
    - "tycho.page.c8b09f5ad28441ab89a6d9e06e0ff4c9"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Tail"
    - "latency"
    - "fan-out"
    - "and"
    - "end-to-end"
    - "deadline"
    - "budgets"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-cascading"
    - "src.tail-at-scale"
  claim_ids: []
  status: "source-linked"
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
<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:-1 -->

# Tail latency, fan-out and end-to-end deadline budgets

> **Tycho chapter draft:** intended canonical topic V07/C04 of the provisional 69-chapter table of contents. Source scope reviewed 2026-10-19. This page is original explanatory material with synthetic numbers; no live trace, experiment, performance benchmark, independent reviewer acceptance or production SLO is claimed.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:0 -->
## Purpose and mission

A system can have fast median service times and still miss a user-visible latency objective. The architecture question is not merely "how fast is each component?" but **how waiting, parallel dependency calls, retry fan-out, queueing and uncertainty combine along the user's critical path**. The tail of a service-time distribution is not an implementation nuisance: if a request needs many dependent results, a slow outlier can determine whether the entire result meets its deadline.

This chapter teaches the distinction between a measured percentile and an illustrative probability model, how to budget latency and cancellation end to end, and when mitigation patterns decrease *user-visible* tail latency without creating more load. Queueing and throughput conservation have their own canonical explanation in [queueing and Little's Law](../c01/queueing-littles-law.md); falsifiable workload experiments are covered in [workload profiles and capacity experiments](../../../performance/workload-profiles-and-capacity-experiments.md); [API/RPC contracts](../../v02/c05/http-rpc-contracts-and-compatibility.md) own exact retry identity and protocol semantics.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Allocate end-to-end time across critical paths, queues, fan-out and retries using distributions and explicit cancellation.

Adequate mean capacity does not guarantee a tail objective; parallel dependencies and correlated delays can dominate the slowest path.

The detailed pages separate the mechanisms that make this decision conditional:

- [Percentiles, correlation and critical paths](tails-critical-path.md) — How do serial work and fan-out change end-to-end tail behavior?
- [Deadlines, hedging and bounded degradation](deadline-hedging.md) — When can an extra attempt improve a tail without exhausting the protected resource?
- [Latency measurement and competing remedies](tail-experiments.md) — Which observation would favor retaining, hedging or splitting a path?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
