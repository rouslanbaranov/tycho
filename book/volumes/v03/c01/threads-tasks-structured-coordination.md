---
metadata_version: 1
id: "tycho.page.4e075e4ebc644f0e9b92c05294f62ca4"
kind: "page"
parent_id: "tycho.chapter.13ad4371e75b49dcb5e082ea62083ee3"
canonical_path: "book/volumes/v03/c01/threads-tasks-structured-coordination.md"
title: "Threads, tasks and coordination: cancellation and resource ownership"
topic_ids:
  - "execution-models"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Threads, tasks and coordination. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "What creates concurrency and which shared state creates contention?"
  prerequisites: []
  related_ids:
    - "tycho.page.02238832b395417bae63939cd96b9134"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.e181d96c75784f818a330bb0f266520c"
    - "tycho.page.114da51171c2474ebd56ee3bebad3bcb"
    - "tycho.page.b6cecfd7301b408db611228b4cec59c5"
    - "tycho.page.dc2470904e004a4aa733abcdb25517ed"
    - "tycho.page.2cdffb0fc6394a1596c8358c852a30e8"
    - "tycho.page.113050e25ec643da98578b98eba1c519"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Threads"
    - "tasks"
    - "and"
    - "coordination"
    - "cancellation"
    - "resource"
    - "ownership"
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
<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:-1 -->

# Threads, tasks and coordination: cancellation and resource ownership

> **Independent Tycho book draft V03/C01, 2026-10-19.** The public Java SE 25 and gRPC contracts cited below are independently published. The example and test plan are invented. No Java code was compiled or executed, no profiler ran, and no reviewer accepted an implementation. Structured concurrency in Java 25 is explicitly a **preview API**, not a permanent portability contract.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:0 -->
## Purpose and mission

A thread is an execution mechanism, not a unit of business demand. An executor schedules tasks, but architecture still must specify who owns each task, which result the parent requires, how long work may live, and what happens if the caller leaves or a sibling fails. Many logical tasks can wait without running on a CPU; increasing their number does not give the database more connection capacity.

The companion [platform and virtual threads](../c02/platform-threads-executors-and-virtual-threads.md) chapter owns detailed Java version/throughput trade-offs. This chapter owns task coordination, cancellation, locks and scarce resource budgets.

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.4e075e4ebc644f0e9b92c05294f62ca4:7 -->
## Applied M9 evidence: what transfers and what does not

These examples connect the chapter's conditional mechanism to published experiences or synthetic decision exercises. A historical company report is **first-party, time-scoped evidence**, not a controlled Tycho benchmark; an M9 decision playbook is **original synthetic analysis**, not a company decision.

**Case lens — [Netflix — gRPC worker-pool regression](../../../cases/netflix-grpc-cpu-workerpool-virtual-thread-regression.md)**. **Relevant mechanism or architectural contrast:** CPU-bound worker pool can regress with virtual threads despite a simpler-looking execution model. **Not established by this report/playbook:** A practitioner-reported few-percent regression without a disclosed benchmark is not a numeric forecast for another workload.

**Transfer test:** before applying the lesson to another legacy system, identify the exact workload, source date, relevant runtime/protocol versions, state authority, failure/recovery gate and the new observation that would reverse the choice. Follow the case's public evidence ledger rather than treating its link as independent proof.
<!-- /tycho-question-source -->

## Integrated decision and reading route

Give concurrent work a lifetime, result owner and cancellation policy rather than treating each thread as an independent business operation.

Cancelling a task requests termination; it cannot undo a downstream commit that already occurred.

The detailed pages separate the mechanisms that make this decision conditional:

- [Task ownership, lifetimes and cancellation](task-lifetime.md) — Who owns concurrent work and what happens when its parent leaves?
- [Shared invariants and irreversible effects](shared-state-effects.md) — Why do concurrency-safe classes and cancellation not establish a business invariant?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.
