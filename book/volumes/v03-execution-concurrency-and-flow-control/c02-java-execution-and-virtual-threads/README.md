---
metadata_version: 1
id: "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
kind: "chapter"
parent_id: "tycho.volume.c4854b444d7c480e9616c5bf06f4db08"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c02-java-execution-and-virtual-threads/README.md"
title: "V03/C02 — Java execution and virtual threads"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
  - "evaluation"
summary: "What improves concurrency without creating downstream capacity? The reading route separates 3 detailed questions from the integrated decision."
route_hints:
  questions:
    - "What improves concurrency without creating downstream capacity?"
  prerequisites:
    - "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
  related_ids:
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.c33e9e4b605a4aa3b073a9f91437fc26"
    - "tycho.page.c880ba1a0a594ad38d6713d198e46436"
    - "tycho.page.f5efc4fa96e242b59ddcd80a48c54af4"
  excludes:
    - "No new benchmark, source inspection or independent edition review is asserted."
  keywords:
    - "system-design"
    - "edition-navigation"
evidence_scope:
  source_ids:
    - "src.jep444"
    - "src.jep491"
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

# V03/C02 — Java execution and virtual threads

## Purpose and mission

What improves concurrency without creating downstream capacity? This chapter owns that question within execution models, concurrency and flow control. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.

## Decision and worked result

Choose execution resources with explicit downstream permits and release-specific blocking assumptions.

Cheaper waiting can increase demand on a saturated connection pool; replacing platform threads with virtual threads does not create database capacity. This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.

## Pages and reasoning route

Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.

| Page | Independent question and role |
|---|---|
| [Integrated decision and original walkthrough](platform-threads-executors-and-virtual-threads.md) | What improves concurrency without creating downstream capacity? |
| [Platform executors and queue budgets](platform-pools.md) | Which queue, deadline and resource assumptions govern a platform-thread executor? |
| [Virtual threads and release-specific pinning](virtual-threads.md) | What changes with virtual threads and which downstream limits stay finite? |
| [Context, cancellation and framework integration](context-cancellation.md) | How do execution choices propagate context and handle effects after a caller stops waiting? |

## Boundaries and further reading

The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.

## Navigation and prerequisites

| Route | Destination |
|---|---|
| Parent | [V03 — Execution models, concurrency and flow control](../README.md) |
| Previous | [V03/C01 — Threads, tasks and coordination](../c01-threads-tasks-and-coordination/README.md) |
| Next | [V03/C03 — Reactive streams, demand and cancellation](../c03-reactive-streams-demand-and-cancellation/README.md) |
| Prerequisite | [V03/C01 — Threads, tasks and coordination](../c01-threads-tasks-and-coordination/README.md) |
| Source reading | [Page-local evidence and versions](platform-threads-executors-and-virtual-threads.md) |

## Evidence and limits

The child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.

## Chapter source ledger

The following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.

<!-- tycho-question-source:tycho.page.02238832b395417bae63939cd96b9134:6 -->
## Evidence and status

- **[E01] Published primary specification, JDK 21:** [OpenJDK JEP 444](https://openjdk.org/jeps/444), *The thread-per-request style*, *Implications of virtual threads*, *Scheduling virtual threads*, *Executing virtual threads*, *JDK Flight Recorder*. Supports execution/pinning contracts, not local throughput.
- **[E02] Primary JDK 24 implementation review:** [OpenJDK core-libs-dev review, 2024-11-06](https://mail.openjdk.org/pipermail/core-libs-dev/2024-November/134177.html), *Summary of changes*, *Unmount virtual thread while holding monitors*. Does not prove application-level freedom from pinning.
- **[E03] Primary JDK 24 release target:** [inside.java notice, 2024-11-15](https://inside.java/2024/11/15/jep491-target-jdk24/). Only confirms the targeted JDK release.
- **[E04] Published Spring Boot 3.3.13 documentation:** [Task Execution and Scheduling](https://docs.spring.io/spring-boot/3.3/reference/features/task-execution-and-scheduling.html), *Task Execution* and *Task Scheduling*. Framework documentation, not a runtime test.

**Research state:** named primary sections inspected; diagrams and workload invented. **Not performed:** compilation, JFR capture, load testing, actual Spring configuration testing, full JEP 491 body inspection or independent human review.

<!-- /tycho-question-source -->
