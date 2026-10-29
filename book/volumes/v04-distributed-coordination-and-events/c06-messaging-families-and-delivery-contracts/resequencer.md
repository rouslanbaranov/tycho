---
metadata_version: 1
id: "tycho.page.2c928286b62944769a4b0cab9fad6139"
kind: "page"
parent_id: "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/resequencer.md"
title: "Resequencer"
topic_ids:
  - "integration-architecture"
perspectives:
  - "architecture"
summary: "Bounded Resequencer owner note; ordered release, bounded backlog, gap timeout and partitioned-ordering limits."
route_hints:
  questions:
    - "Should out-of-order messages be buffered and released in an acceptable order?"
  prerequisites:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  related_ids:
    - "tycho.chapter.23e79f6cb03b4206a5c82494bc5c2928"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "resequencer"
    - "owner note"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.camel"
    - "src.microsoft-cloud-patterns"
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
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Resequencer

> **Pattern atlas:**
> [Resequencer](../../v11-pattern-atlas/c03-messaging-integration/resequencer.md#resequencer) — decision conditions and contraindications.

This page owns the bounded technical note moved from the
[consumer requirements and messaging families page](message-selection.md#resequencer)
on 2026-10-29. The other ownership notes remain on the chapter page.

**Decision.** Use a resequencer only when the message contract declares a required order, a
reliable sequence domain, and a bounded buffer whose gap timeout and late-message disposition
have owners. Partition by key instead when global order is unnecessary or the buffer cannot be
bounded.

**Mechanism.** A resequencer holds messages and releases them in a specified order. The
Enterprise Integration Patterns page defines a "stateful filter" that collects and re-orders
messages before publishing them to the output channel. Camel's batch mode collects, sorts and
sends a batch; its stream mode sends a message as soon as the next expected sequence number
arrives, and requires integer sequence numbers ordered from 1 to N. A stream message must carry
a unique sequence number with a known predecessor and successor.

**Invariant.** The pending-message backlog is a bounded buffer: the default capacity is 1000
elements and can be configured. The source states that the capacity parameter prevents the
resequencer from running out of memory. Duplicate handling is a declared rule, not a broker
default: by default duplicates are not supported and only the last message is kept, while batch
mode can allow them. Tycho guidance: the sequence domain, buffer cap, duplicate rule and gap
timeout belong to the streaming contract.

**Failure and recovery.** The failure path is a missing sequence that blocks later messages. On
a timeout the resequencer disregards the current expected sequence number and moves to the next
expected number. Late messages need a declared disposition: with old-message rejection enabled
the implementation throws for an exchange older than the last delivered message, and invalid
exchanges can be skipped explicitly. Tycho guidance: release after a declared gap timeout, fail
the affected ordering scope when continuity is mandatory, and record dropped or rejected
sequence numbers.

**Alternative.** Partitioning messages by a category key and processing each category
sequentially, with different categories in parallel, is the alternative when global order is
unnecessary. The Sequential Convoy pattern partitions related messages that way; its
considerations add that competing consumers alone lose per-group ordering and that a poison
message blocks the rest of its session. Reverse the choice when ordering is global or the key
cannot be made stable.

**Limits.** Buffer memory, gap timeout and ordering scope are costs; a global resequencer can
become a throughput bottleneck. The source warns that the lower the timeout relative to the
out-of-sequence delay, the higher the probability of out-of-order delivery, and that large
timeouts need sufficiently high capacity.

**Evidence.** The Enterprise Integration Patterns Resequencer page
(read.batch2-resequencer.2026-10-21) states the collect-and-reorder mechanism. The Apache Camel
4.22.x LTS Resequence page (read.camel-resequence.2026-10-29, canonical text SHA-256
e14de4848c2405163b796e003cc751c1d70decc6f83b5e53d160db0f3b269a9e) states batch and stream
modes, the ordered integer sequence requirement, the default backlog capacity, duplicate
handling, timeout release, old-message rejection and invalid-message skipping. The Microsoft
Learn Sequential Convoy pattern page (read.microsoft-sequential-convoy.2026-10-29, canonical
text SHA-256 89cfb0fe140931f0addd23e85124b6fbfe430a9b743d5a1739052ca33fbcb43d) states
per-category partitioning with parallel categories and the per-group FIFO ordering boundary.
No source is a benchmark.

## Navigation

| Route | Destination |
|---|---|
| Parent chapter | [V04/C06 — Messaging families and delivery contracts](README.md) |
| Originating page | [Consumer requirements and messaging families](message-selection.md#resequencer) |
| Source ledger | [Chapter source ledger](README.md#chapter-source-ledger) |
