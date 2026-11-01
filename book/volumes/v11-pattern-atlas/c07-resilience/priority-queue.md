---
metadata_version: 1
id: "tycho.page.e89c1693f295dde2349c93019fcd8a7f"
kind: "page"
parent_id: "tycho.chapter.69085752a11c69305aa2a369b8ec9d29"
canonical_path: "book/volumes/v11-pattern-atlas/c07-resilience/priority-queue.md"
title: "Priority Queue"
topic_ids:
  - "performance-engineering"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "operations"
summary: >-
  Decision card for Priority Queue; all four dimensions source-bound;
  coverage remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should queued work be ordered by business priority rather than arrival?
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
    - "priority queue"
    - "resilience"
evidence_scope:
  source_ids:
    - "src.rabbitmq"
    - "src.microsoft-cloud-patterns"
    - "src.azure-service-bus-amqp"
    - "src.aws-sqs"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.rabbitmq-priority-queues.2026-10-31,
    read.microsoft-priority-queue-pattern.2026-10-31,
    read.azure-service-bus-amqp-message-mapping.2026-10-31,
    read.aws-sqs-queue-types.2026-10-31 and
    read.aws-sqs-fair-queues.2026-10-31; owner section and limits are bounded.
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
# Priority Queue

**Identity.** Priority Queue; family Resilience and fault tolerance; kind
resilience-pattern; priority core.

**Decision question.** Should queued work be ordered by business priority rather than
arrival?

**Good-fit conditions.** Priorities are meaningful and bounded; classes are
authenticated; the broker's actual support is verified (RabbitMQ classic or
quorum priority; the Service Bus AMQP guide maps no `priority` header, so the
pattern uses a custom property and SQL filters; or separate queues); a maximum wait
and aging policy bounds low-class starvation; tenant share is capped.
RabbitMQ states that "Classic and quorum queues in RabbitMQ support
priorities"; Azure's pattern assigns a "custom application property called
Priority".

**Hard contraindications.** Reject when all work is equal, when priorities can
starve low-priority work indefinitely without a wait bound, when producers can
self-assign priority unchecked, or when strict FIFO order within a group must
not be reordered.

**Competing alternative.** Admission-controlled FIFO, separate lanes per class,
or tenant-fair queues. SQS FIFO preserves order within a message group: "FIFO
queues ensure that you receive messages in the order they are sent within each
message group." SQS fair queues rebalance dwell time across tenants and do not
limit consumption per tenant. Reverse the choice when priority inversion or
starvation exceeds latency benefit.

**Failure and recovery.** Starvation, priority abuse and unauthenticated class
claims are common. RabbitMQ states that "only messages with higher priorities
are delivered, and lower-priority messages are never delivered" and that
strict quorum priority can delay lower priorities indefinitely; prefetch can
make a higher class wait behind lower-class in-flight work. Azure recommends
that teams "dynamically increase the priority of old messages" to ensure
low-priority work is eventually processed. Define max wait, aging/promotion,
tenant isolation and a starvation policy, and verify the class at each hop.
The max-wait/aging rule is Tycho synthesis; none of the selected broker units
supplies a universal bound.

**Technical owner.** [Priority Queue](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/admission-resource.md#priority-queue) — admission/queue policy is bounded, not a universal priority scheme.

**Sources.** [src.rabbitmq](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.rabbitmq-priority-queues.2026-10-31`, revision
`4ca982ad871d4c03eabc5545059ce945bade5ee5da444132361401119438dc45`;
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.microsoft-priority-queue-pattern.2026-10-31`, revision
`da8e65b90263acd29305315fdba36da3e6b4127e688532f1132ed681eb4c1fde`;
[src.azure-service-bus-amqp](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.azure-service-bus-amqp-message-mapping.2026-10-31`,
revision
`a1d6a361f205a21ff53f6323a87ad27dd9dd5efc15f136c8d829f896e16cbaab`;
[src.aws-sqs](../../../../edition/patterns/reading-ledger.v1.json) read
records `read.aws-sqs-queue-types.2026-10-31`, revision
`c9ccf72844c5180d80502042f9abf7766b8af7e194f217065ddf50a43f540609`,
and `read.aws-sqs-fair-queues.2026-10-31`, revision
`9d0821490fbdd48ed28c195c3b5bdc466d800d34383b1caf36dd802ec0e7ca5f`.
Units: RabbitMQ "Priority Support in Queues" version 4.4; Microsoft "Priority
Queue pattern" and "AMQP 1.0 in Azure Service Bus and Event Hubs"; AWS
"Amazon SQS queue types" and "Amazon SQS fair queues". Public documentation,
not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Queue-Based Load Leveling; Load Shedding; Rate Limiting; Bulkhead.
