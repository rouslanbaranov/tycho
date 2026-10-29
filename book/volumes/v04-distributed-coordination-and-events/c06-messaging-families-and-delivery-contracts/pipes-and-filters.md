---
metadata_version: 1
id: "tycho.page.5f7a647e94fb4e7cbce5dab08b1d3414"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/pipes-and-filters.md"
title: "Pipes and Filters"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Bounded Pipes and Filters owner note; ordered stage contracts, non-transactional loss and pipeline limits."
route_hints:
  questions:
    - "Should processing be composed as independent stages connected by a message contract?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "pipes and filters"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the consumer requirements and messaging families page; the bound source claims and limits remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-28"
content_verified_at: null
---

# Pipes and Filters

> **Pattern atlas:**
> [Pipes and Filters](../../v11-pattern-atlas/c03-messaging-integration/pipes-and-filters.md#pipes-and-filters) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[consumer requirements and messaging families page](message-selection.md#pipes-and-filters)
on 2026-10-29. The other ownership notes remain on the chapter page.

**Decision.** Compose processing as ordered stages only when each stage has an independent
contract and the pipeline owns ordering, partial completion and recovery. If one stage needs
the whole transaction, or per-stage latency and coordination exceed the value of isolation,
keep one cohesive transformation.

**Mechanism.** Pipes and filters decompose processing into ordered, replaceable stages
connected by a message contract. The source defines the style as dividing "a larger
processing task into a sequence of smaller, independent processing steps (filters) that are
connected by channels (pipes)." The pipe carries one filter's output to the next; a filter
receives on its inbound pipe, processes the message, and publishes the result to its
outbound pipe. The source states: "Each filter exposes a very simple interface: It receives
messages on the inbound pipe, processes the message, and publishes the results to the
outbound pipe."

**Invariant.** Each stage has one inbound and one outbound port in the basic form, and a
parallel or multi-instance stage can reorder messages unless the pipeline declares an
ordering scope and a resequencer. The source states: "If the sequence of messages is
critical, we can run only one instance of each component or we must use a Resequencer
(283)." Tycho guidance, not a source claim: give each stage an effect identity for
deduplication, expose per-stage lag or queue depth, and define backpressure and a
partial-completion rule before adding a stage.

**Failure and recovery.** A failed middle stage leaves earlier effects applied; record stage
identity and recover through a transactional client or a declared checkpoint. The source is
explicit about the simple case: "This simple filter example is not transactional. If an
error occurs while processing the message (before it is sent to the output channel), the
message is lost. This is generally not desirable in a production environment. See
Transactional Client (484) for a solution to this problem." Tycho guidance: retries and
replays must be idempotent per stage, and the operator needs the failed stage, its input
identity and the last completed stage.

**Alternative.** A single in-process transformation is the alternative when the stages are
small and cannot be operated independently. The source names a comprehensive "incoming
message massaging module" as the alternative and calls that approach "inflexible and
difficult to test"; an in-memory queue is a lighter pipe when all components share one
machine. Use the pipeline when independent development, scaling or replacement pays for the
message contract and partial-failure states.

**Limits.** Channels consume memory and CPU cycles for buffering, and repeated message
conversion lowers throughput on long chains; the slowest stage bounds pipeline throughput,
and stateful filters are poor parallel candidates.

**Evidence.** The 2003 Chapter 3 section, printed pp.70-77, supports the mechanism, ordering,
non-transactional loss and the in-process alternative; the public pattern page is
publisher-abridged. Backpressure, checkpoint and idempotency guidance is Tycho synthesis,
not a source claim.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Consumer requirements and messaging families](message-selection.md#pipes-and-filters) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
