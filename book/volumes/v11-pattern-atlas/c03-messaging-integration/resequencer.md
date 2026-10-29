---
metadata_version: 1
id: "tycho.page.19c9061504c7b1d7458d9697d8d55b3f"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/resequencer.md"
title: "Resequencer"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Resequencer; bounded owner evidence and limits."
route_hints:
  questions:
    - >-
      Should out-of-order messages be buffered and released in an acceptable
      order, or should the consumer partition by key instead?
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "broker-specific resequencer implementations"
  keywords:
    - "pattern atlas"
    - "resequencer"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.camel"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
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

**Decision.** Buffer and release out-of-order messages only when an ordering requirement, a
reliable sequence domain, and a bounded buffer with a gap timeout and a late-message disposition
have owners. Partition by key instead when global order is unnecessary.

**Identity.** Resequencer; family Messaging and event-driven integration; kind messaging-pattern;
priority advanced.

**Decision question.** Should out-of-order messages be buffered and released in an acceptable
order?

**Good-fit conditions.** The message contract declares which order is required. Sequence numbers
are reliable and scoped to the ordering domain, with known predecessors and successors. The
pending backlog is bounded, the gap timeout is declared, duplicates have a rule, and late or
invalid messages have a disposition. The consumer can tolerate buffering delay.

**Hard contraindications.** Reject when order is irrelevant, when the sequence domain is unstable,
when the buffer cannot be bounded, or when one missing message would block the stream beyond the
declared deadline. Reject when the producer can assign non-unique or non-monotonic sequence
values.

**Competing alternative.** Partitioning messages by a category key and processing each category
sequentially, with different categories in parallel. Reverse the choice when ordering is global or
the key cannot be made stable.

**Failure and recovery.** A missing sequence blocks later messages until a gap timeout releases
the buffer; the source states that a timeout makes the resequencer disregard the current expected
sequence number and move to the next expected number. Late messages need a declared disposition:
old-message rejection throws on an exchange older than the last delivered message, and invalid
messages can be discarded explicitly. At the buffer cap, reject or spill with evidence rather than
dropping silently.

**Technical owner.** [Resequencer](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/resequencer.md#resequencer) — sequence domain, buffer bound, gap timeout and late-message disposition are bounded; this is not a broker implementation guide.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-resequencer.2026-10-21: the public pattern page is publisher-abridged and
states the collect-and-reorder mechanism.
[src.camel](../../../../edition/patterns/reading-ledger.v1.json)
read record read.camel-resequence.2026-10-29: the Apache Camel 4.22.x LTS Resequence page states
batch and stream modes, the ordered integer sequence requirement, the default backlog capacity,
duplicate handling, timeout release, old-message rejection and invalid-message skipping. Canonical
text SHA-256: e14de4848c2405163b796e003cc751c1d70decc6f83b5e53d160db0f3b269a9e.
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-sequential-convoy.2026-10-29: the Sequential Convoy pattern page states
per-category partitioning, per-group FIFO ordering and parallel groups. Canonical text SHA-256:
89cfb0fe140931f0addd23e85124b6fbfe430a9b743d5a1739052ca33fbcb43d. The sources are public
documentation, not benchmarks.

**Decision state.** applicable-under-conditions.

**Related entries.** Competing Consumers; Aggregator; Correlation Identifier; Message Sequence;
Pipes and Filters.
