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
summary: "Bounded Splitter owner note; part identity, completion rules, fan-out and aggregation alternatives."
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
Apache Camel's splitter breaks a composite into one message per item and processes each
part; the default output is the original input unless an aggregation strategy is supplied.

**Invariant.** Each part must carry a part identity and a position so completion is
decidable. Spring Integration's base splitter populates CORRELATION_ID, SEQUENCE_SIZE, and
SEQUENCE_NUMBER on produced messages; when the size is unknown, SEQUENCE_SIZE is zero and
the aggregate remains incomplete until a custom release strategy or expiry closes it. The
source states: "It is a MessageHandler implementation that encapsulates features common to
splitters, such as filling in the appropriate message headers (CORRELATION_ID, SEQUENCE_SIZE,
and SEQUENCE_NUMBER) on the messages that are produced." A completion or compensation rule
must have an owner; Tycho's design guidance adds a bounded fan-out and per-part idempotency,
which the source does not fix.

**Failure and recovery.** A split that aborts does not advance a successful-completion
watermark, so the failed batch can be retried. Tycho guidance, not a source claim:
completed effects must remain idempotent or be deduplicated because a retry can re-deliver
parts. An unknown part count leaves the aggregate incomplete rather than silently
complete.

**Alternative.** Aggregation is the mirror-image decision. Spring Integration describes the
aggregator as "Basically a mirror-image of the splitter, the aggregator is a type of message
handler that receives multiple messages and combines them into a single message." Use that
side when the work is to combine related messages, not to divide one composite; the source
states the relationship, while the decision framing is Tycho's synthesis.

**Limits.** Fan-out multiplies message volume, tracking state and partial-failure cleanup; a
split with no completion marker leaks orphaned work and needs an owner.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Messaging families and durable workflows](messaging-families-and-durable-workflows.md#splitter) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
