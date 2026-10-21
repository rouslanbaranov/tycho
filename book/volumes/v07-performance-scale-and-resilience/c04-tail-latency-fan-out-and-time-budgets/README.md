---
metadata_version: 1
id: "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07-performance-scale-and-resilience/c04-tail-latency-fan-out-and-time-budgets/README.md"
title: "V07/C04 — Tail latency, fan-out and time budgets"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Why can p99 degrade despite adequate mean capacity? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "Why can p99 degrade despite adequate mean capacity?"
  prerequisites:
    - "tycho.chapter.a55ddaaa45a647e29b51d6b5c0adbe05"
  related_ids:
    - "tycho.page.eb130a7f820544a2ba0e0883c0ce587b"
    - "tycho.page.45935212b3b7476d8a163520f065b825"
    - "tycho.page.e229cbbcdc4a45bb9e368313f129b25b"
    - "tycho.page.c8b09f5ad28441ab89a6d9e06e0ff4c9"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-cascading"
    - "src.tail-at-scale"
  claim_ids: []
  status: "source-linked"
  notes: "Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial assembly"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# V07/C04 — Tail latency, fan-out and time budgets

## Purpose and mission

Why can p99 degrade despite adequate mean capacity? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Allocate end-to-end time across critical paths, queues, fan-out and retries using distributions and explicit cancellation.

Adequate mean capacity does not guarantee a tail objective; parallel dependencies and correlated delays can dominate the slowest path. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](tail-latency-fanout-and-deadline-budgets.md) | Why can p99 degrade despite adequate mean capacity? |
| [Percentiles, correlation and critical paths](tails-critical-path.md) | How do serial work and fan-out change end-to-end tail behavior? |
| [Deadlines, hedging and bounded degradation](deadline-hedging.md) | When can an extra attempt improve a tail without exhausting the protected resource? |
| [Latency measurement and competing remedies](tail-experiments.md) | Which observation would favor retaining, hedging or splitting a path? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C03 — Load-test methods and benchmark validity](../c03-load-test-methods-and-benchmark-validity/README.md) |
| Next | [V07/C05 — Overload protection and graceful degradation](../c05-overload-protection-and-graceful-degradation/README.md) |
| Prerequisite | [V07/C03 — Load-test methods and benchmark validity](../c03-load-test-methods-and-benchmark-validity/README.md) |
| Source reading | [Page-local evidence and versions](tail-latency-fanout-and-deadline-budgets.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:7 -->
## 7. Source-to-claim ledger and review boundary

| Public source inspected | Narrow supported role | Evidence boundary |
|---|---|---|
| [Dean and Barroso, *The Tail at Scale*, Communications of the ACM 56 (2013)](https://research.google/pubs/the-tail-at-scale/) | Parallel dependency tails and deferred hedging motivation | Paper case study ≠ performance result for fictional examples |
| [Google SRE Book, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) | Deadlines, overload and cascading work | Published production lessons, not portable numerical SLO thresholds |
| [gRPC Guides, Deadlines](https://grpc.io/docs/guides/deadlines/) | Propagated deadline and cancellation concepts | Language-specific implementations must be verified |
| [AWS Builders' Library, Timeouts/Retries/Backoff/Jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Overload amplification and retry-jitter design considerations | Vendor experience, not empirical evidence for this book's hypothetical topology |
| [Tycho queueing page](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md) | Original explanation of throughput versus mean and finite-window limits | Educational derivation; does not validate tail measurements |

**Author-owned inference:** the independent-max CDF and example calculations follow the stated probability model; the budget table, diagrams, choices and workload scenario are entirely fictional. Correlated latency distributions, real hedging effectiveness, throughput under overload, timeout-success ratios, latency sampling bias and third-party review remain **unverified**. No benchmark was run and no production recommendation is made. The page must be reconciled with the final V07 volume/section hierarchy before edition release.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.eb130a7f820544a2ba0e0883c0ce587b:8 -->
## Reading and navigation

- Current landing: [Performance, scaling and resilience](../../../performance/README.md); target V07/C04 in [proposed book contents](../../../PROPOSED-STRUCTURE.md).
- Background: [Queueing and Little's Law](../c01-queueing-littles-law-and-measurement-boundaries/queueing-littles-law.md); [Workload experiments](../../../performance/workload-profiles-and-capacity-experiments.md).
- Implementation boundaries: [Java concurrency](../../v03-execution-concurrency-and-flow-control/c02-java-execution-and-virtual-threads/platform-threads-executors-and-virtual-threads.md); [Connection pools](../../v03-execution-concurrency-and-flow-control/c05-thread-connection-and-buffer-pools/connection-pools-hikaricp-pgbouncer.md); [API deadlines and retries](../../v02-application-boundaries-and-contracts/c05-public-apis-http-rpc-and-compatibility/http-rpc-contracts-and-compatibility.md).
- Failure actions: [Safe rollout/recovery](../../../delivery/safe-rollout-and-recovery.md); [Distributed idempotency](../../../distributed/transactional-outbox-and-idempotency.md).
<!-- /tycho-question-source -->
