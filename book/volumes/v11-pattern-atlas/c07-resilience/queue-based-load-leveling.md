---
metadata_version: 1
id: "tycho.page.6a5f799a46729ab3e2fcdf168692b50a"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/queue-based-load-leveling.md"
title: "Queue-Based Load Leveling"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Queue-Based Load Leveling; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should work be buffered in a queue so producers and consumers can run at
      different rates?
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
    - "queue-based load leveling"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.microsoft-cloud-patterns"
    - "src.aws-sqs"
    - "src.sre-overload"
    - "src.rabbitmq"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.microsoft-queue-based-load-leveling.2026-10-31,
    read.aws-sqs-welcome.2026-10-31 and the retained
    read.sre-overload.2026-10-21 and read.batch4-rabbit-reliability.2026-10-21
    records; owner section and limits are bounded.
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
# Queue-Based Load Leveling

**Identity.** Queue-Based Load Leveling; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should work be buffered in a queue so producers and consumers can
run at different rates?

**Good-fit conditions.** Bursts exceed consumer capacity; queue durability, a backlog
age/retention bound and idempotent consumers are owned; the caller can defer the result;
latency is acceptable.

**Hard contraindications.** Reject when the caller needs a synchronous result, when
backlog would violate a deadline, when the broker does not persist accepted messages, or
when the queue becomes an unbounded hiding place.

**Competing alternative.** Direct synchronous calls or admission control, including
shedding when work cannot be deferred. Reverse the choice when queue delay and backlog risk
exceed smoothing benefit; shedding is the alternative when deferral has no value.

**Failure and recovery.** Unbounded backlog, expired work and duplicate effects after
ambiguous acknowledgment are possible; bound age, reject early and drain. Azure says
"Monitor queue depth and scale consumers within safe limits, or shed work at the producer";
AWS says that messages beyond the maximum retention period are deleted automatically;
Google SRE says requests above a cap fail locally. Tycho's rule is to reject before enqueue
when backlog age crosses its bound, not to let memory or retention expire the work.

**Technical owner.** [Queue-Based Load Leveling](../../v07-performance-scale-and-resilience/c01-queueing-littles-law-and-measurement-boundaries/queue-recovery.md#queue-based-load-leveling) — mechanism, durability and retention are source-bound; the four-part admission rule and shedding choice remain Tycho.

**Sources.** [src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-queue-based-load-leveling.2026-10-31`: sections "Solution",
"Problems and considerations" and "When to use this pattern".
[src.aws-sqs](../../../../edition/patterns/reading-ledger.v1.json) read record
`read.aws-sqs-welcome.2026-10-31`: sections "Benefits of using Amazon SQS",
"Basic Amazon SQS architecture" and "Message lifecycle".
[src.sre-overload](../../../../edition/patterns/reading-ledger.v1.json) retained record
`read.sre-overload.2026-10-21`: sections "Handling Overload", "Per-Customer Limits" and
"Client-Side Throttling". The retained
[src.rabbitmq](../../../../edition/patterns/reading-ledger.v1.json) record
`read.batch4-rabbit-reliability.2026-10-21` remains a supporting reliability citation only.
The sources are public documentation, not benchmarks; Tycho-labelled rules are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Priority Queue; Load Shedding; Dead Letter Channel; Competing
Consumers.
