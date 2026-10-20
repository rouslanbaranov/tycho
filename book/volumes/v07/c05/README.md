---
metadata_version: 1
id: "tycho.chapter.0718556e0eb14d499adbbe67073327df"
kind: "chapter"
parent_id: "tycho.volume.f7679623ca274bff8a00389d409d68c6"
canonical_path: "book/volumes/v07/c05/README.md"
title: "V07/C05 — Overload protection and graceful degradation"
topic_ids:
  - "performance-engineering"
perspectives:
  - "architecture"
  - "evaluation"
summary: "How should admissions, queues, retries and shedding be bounded? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "How should admissions, queues, retries and shedding be bounded?"
  prerequisites:
    - "tycho.chapter.2ad010c2b29c4390b83bbdadeb346289"
  related_ids:
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.page.d9abd43bb7394c04a6bf77d4014f870d"
    - "tycho.page.80ab784dafed47a7baf31722fce5eabc"
    - "tycho.page.62ad1ae9e0d243d69b08be0ff32930a1"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.aws-backoff"
    - "src.sre-overload"
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

# V07/C05 — Overload protection and graceful degradation

## Purpose and mission

How should admissions, queues, retries and shedding be bounded? This chapter owns that question within performance, scale and resilience under load. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Bound admitted work, queue residence, retry amplification and degraded behavior around protected outcomes.

Accepting every request can postpone rejection until after resource exhaustion; useful service may require earlier explicit refusal. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](overload-admission-control-and-graceful-degradation.md) | How should admissions, queues, retries and shedding be bounded? |
| [Scarce resources, admission and queues](admission-resource.md) | Where must rejection occur to protect the expensive operation? |
| [Bulkheads, retries and optional dependencies](dependency-isolation.md) | How can failure in optional work starve core work? |
| [Recovery hysteresis and overload experiments](overload-recovery.md) | What prevents a recovering dependency from being overwhelmed immediately? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V07 — Performance, scale and resilience under load](../README.md) |
| Previous | [V07/C04 — Tail latency, fan-out and time budgets](../c04/README.md) |
| Next | [V07/C06 — Horizontal/vertical scaling and autoscaling delay](../c06/README.md) |
| Prerequisite | [V07/C04 — Tail latency, fan-out and time budgets](../c04/README.md) |
| Source reading | [Page-local evidence and versions](overload-admission-control-and-graceful-degradation.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.


## Further mechanism and recovery questions

- [Local limits, global quotas and fair admission](admission-resource.md#local-limits-global-quotas-and-fair-admission) — source-scoped enrichment; examples and proposed tests are not executed results.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:8 -->
## 8. Source-to-claim ledger and review limitations

| Public material inspected (2026-10-19) | Supported topic | Unverified |
|---|---|---|
| [Google SRE, Handling Overload](https://sre.google/sre-book/handling-overload/) | Resource-dependent overload costs, priorities, client throttle and retry concerns | Any universally correct rate or priority policy |
| [AWS Builders' Library, Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) | Shedding strategies and failure containment rationale | Measured benefit in the synthetic trail-guide scenario |
| [AWS Builders' Library, Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Retry multiplication and bounded backoff motivation | Real retry traffic or safe unconditional retry behavior |
| [Tycho capacity experiment chapter](../../../performance/workload-profiles-and-capacity-experiments.md) | Defined workload/queue and synthetic failure methodology | Completed independent experiment |

All example data, percentages, capacity statements and system behavior are hypothetical. No fault injection, cloud service, policy configuration, correctness exercise or independent review has been performed. Do not present this as an operational playbook without verifying actual target workload, authorizations, deadlines and state semantics.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.c5d20ae7ef6445e5b23dd5fbac625060:9 -->
## Navigation

- Proposed **V07/C05** in [planned TOC](../../../PROPOSED-STRUCTURE.md), current [Performance landing](../../../performance/README.md).
- Prerequisite: [Workload demand](../../v01/c02/workload-demand-and-arrival-models.md), [Queueing](../c01/queueing-littles-law.md).
- Related: [Autoscaling delay](../c06/autoscaling-lag-and-capacity-limits.md), [Tail latency](../c04/tail-latency-fanout-and-deadline-budgets.md), [Benchmark validity](../c03/load-testing-and-benchmark-validity.md), [Outbox/idempotency](../../../distributed/transactional-outbox-and-idempotency.md).

<!-- /tycho-question-source -->
