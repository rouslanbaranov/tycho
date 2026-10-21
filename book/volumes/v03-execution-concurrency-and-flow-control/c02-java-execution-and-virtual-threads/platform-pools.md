---
metadata_version: 1
id: "tycho.page.c33e9e4b605a4aa3b073a9f91437fc26"
kind: "page"
parent_id: "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
canonical_path: "book/volumes/v03-execution-concurrency-and-flow-control/c02-java-execution-and-virtual-threads/platform-pools.md"
title: "Platform executors and queue budgets"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Which queue, deadline and resource assumptions govern a platform-thread executor?"
route_hints:
  questions:
    - "Which queue, deadline and resource assumptions govern a platform-thread executor?"
  prerequisites:
    - "tycho.page.02238832b395417bae63939cd96b9134"
  related_ids:
    - "tycho.chapter.d5b789c9cd7e4cb693c22943423531c2"
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.page.c880ba1a0a594ad38d6713d198e46436"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "platform"
    - "pools"
evidence_scope:
  source_ids:
    - "src.jep444"
    - "src.jep491"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.02238832b395417bae63939cd96b9134; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
# Platform executors and queue budgets

**Owning question:** Which queue, deadline and resource assumptions govern a platform-thread executor?

This page belongs to [V03/C02 — Java execution and virtual threads](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.02238832b395417bae63939cd96b9134:1 -->
## Platform pools, queues and deadlines

A fixed platform pool bounds active blocking tasks but not waiting submissions unless its queue is also bounded. A queue can make latency worse even while the system reports few immediate errors. The deadline must include admission, executor queue wait, connection acquisition, execution and response transfer. Do not hold a database connection while waiting for unrelated network work. A rejection policy is part of the public service contract: retryable overload must be distinguished from uncertain committed effects.

Platform workers remain a simple choice for moderate concurrency and mature synchronous libraries. Neither fixed thread count nor CPU-core multiplier is universally correct: derive it from observed wait/compute fractions, heap, downstream budgets and load-test behavior.

<!-- /tycho-question-source -->

## Original decision model — a finite worker and waiting budget

Consider a fictional endpoint with four workers and room for eight waiting tasks. At an instant when all twelve slots are occupied, another attempt needs an explicit outcome: reject it, wait within a caller-owned budget, or defer it through a separately durable protocol. Merely calling the endpoint asynchronous does not answer that question. These numbers describe an invented state, not a Java default or a measured safe configuration.

Now let the downstream dependency pause. The relevant inventory includes active tasks waiting downstream, accepted tasks waiting locally, their remaining deadlines and work already committed beyond the process. A larger waiting queue postpones a capacity decision and retains more state; it does not make the dependency complete operations faster. If tasks continue after the callers abandon them, the system can consume scarce capacity on results nobody can use.

Before changing the pool, write the required behavior for a saturated queue, an expired caller, a failed worker and process shutdown. For each accepted operation, identify whether it is safe to discard, retry with the same logical identity, or query an authoritative outcome. Compare a smaller bounded pool plus explicit admission with a larger pool under the same offered workload and downstream permits. The discriminating result is correct completed work with bounded waiting and recoverable unknowns, not the number of tasks accepted into memory.

This model does not specify an executor implementation or claim a runtime test. The inherited JDK references explain the execution context; the queue arithmetic and failure schedule here are original synthetic reasoning.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](platform-threads-executors-and-virtual-threads.md) |
| Next | [Continue the reasoning](virtual-threads.md) |
| Integrated question | [Original scenario and limits](platform-threads-executors-and-virtual-threads.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
