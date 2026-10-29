---
metadata_version: 1
id: "tycho.page.46865c9b53984280ac3a15e86f5ae50c"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/splitter.md"
title: "Splitter"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Bounded Splitter owner note; correlation identity, sequence position, completion rules, fan-out and aggregation alternatives."
route_hints:
  questions:
    - "Should a composite message be divided into independently processed parts?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "splitter"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.camel"
    - "src.spring-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Moved verbatim from the messaging families and durable workflows page; the bound source claims and limits remain in the owner unit."
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

# Splitter

> **Pattern atlas:**
> [Splitter](../../v11-pattern-atlas/c03-messaging-integration/splitter.md#splitter) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[messaging families and durable workflows page](messaging-families-and-durable-workflows.md#splitter)
on 2026-10-29. The other ownership notes remain on the chapter page.

**Decision.** Split a composite message only when its parts can make progress
independently and completion is observable. If the parts must succeed atomically, keep the
composite whole; if the work is to combine related messages, use an aggregator. Tycho
guidance, not a source claim: reject the split when ordering across parts is mandatory and
no sequencer reconstructs it, or when the split loses required context.

**Mechanism.** A splitter turns one input into several independently processable messages.
Apache Camel's splitter breaks a composite into one message per item and processes each part.
Camel states: "The Splitter will by default return the original input message. You can control
this by using a custom AggregationStrategy."

**Invariant.** Each part must carry a correlation identity, a sequence position and, when
known, the total size; completion is decidable only when the total count is known, or when a
custom release strategy or expiry closes the group. Spring Integration's base splitter
populates CORRELATION_ID, SEQUENCE_SIZE, and SEQUENCE_NUMBER on produced messages: "It is a
MessageHandler implementation that encapsulates features common to splitters, such as filling
in the appropriate message headers (CORRELATION_ID, SEQUENCE_SIZE, and SEQUENCE_NUMBER) on the
messages that are produced." For an iterator with no known size, Spring Integration's Iterators
section sets SEQUENCE_SIZE to zero and states that the aggregate group remains incomplete until
a custom release strategy or expiry closes it. Tycho guidance, not a source claim: a completion
or compensation rule must have an owner, and the fan-out is bounded; the source does not fix
per-part idempotency.

**Failure and recovery.** Apache Camel's value-based watermark is only updated when the split
completes successfully; an aborted split (for example, one that exceeds maxFailedRecords) does
not update the watermark, which allows the failed batch to be retried. Tycho guidance, not a
source claim: completed effects must remain idempotent or be deduplicated because a retry can
re-deliver parts. An unknown part count leaves the aggregate incomplete rather than silently
complete; Spring Integration requires a custom release strategy or expiry to close it.

**Alternative.** Aggregation is the mirror-image decision. Spring Integration describes the
aggregator as "Basically a mirror-image of the splitter, the aggregator is a type of message
handler that receives multiple messages and combines them into a single message." Use that
side when the work is to combine related messages, not to divide one composite; the source
states the relationship, while the decision framing is Tycho's synthesis.

**Limits.** The evidence boundary is provider documentation: Apache Camel's Split EIP page and
Spring Integration's Splitter and Aggregator pages are implementation-specific references, not
an independent evaluation and not a complete Splitter contract. The watermark is an Apache
Camel value-based resume feature, and the release-strategy and expiry behavior is Spring
Integration's aggregator mechanism; both are provider-specific and neither is a general
Splitter requirement. Completion and compensation ownership, bounded fan-out, ordering
rejection and compensation are Tycho guidance, not source claims. Fan-out multiplies message
volume, tracking state and partial-failure cleanup; a split with no completion marker leaks
orphaned work and needs an owner.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Messaging families and durable workflows](messaging-families-and-durable-workflows.md#splitter) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
