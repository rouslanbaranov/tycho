---
metadata_version: 1
id: "tycho.page.1a7b78e63a294313b93d56eed8cc06c7"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/message-filter.md"
title: "Message Filter"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Message Filter; bounded owner evidence and limits."
route_hints:
  questions:
    - "Should messages be discarded when they do not match explicit criteria?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "provider-specific filter expressions"
  keywords:
    - "pattern atlas"
    - "message-filter"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
  claim_ids: []
  status: "source-linked"
  notes: "Moved card page; failure/recovery binding and revision in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-28"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Message Filter

**Identity.** Message Filter; family Messaging and event-driven integration; kind
integration-pattern; priority core.

**Decision question.** Should messages be discarded when they do not match explicit criteria?

**Good-fit conditions.** The filter has a single output channel; the predicate is testable;
filtering is cheaper than downstream handling.

**Hard contraindications.** Reject when messages need multiple destinations or every message has a
required effect.

**Competing alternative.** A content-based router sends each message to a different channel based on
content. Prefer the router when messages require different destinations or routing must choose
among channels; the filter fits only a single-output pass-or-discard decision.

**Failure and recovery.** A non-matching message is discarded and produces no downstream
output. The served page states: "If the message content does not match the criteria, the message
is discarded." It states no rejected-message disposition, audit record, retention or recovery
path; those remain unknown and out of scope for this card. A recovery design would need a
separate retained source, replay or dead-letter path, which is Tycho synthesis, not a claim from
this source.

**Technical owner.** [Message selection: filters and routing](../../v04-distributed-coordination-and-events/c06-messaging-families-and-delivery-contracts/message-selection.md#message-filter) — bounded to predicate filtering, not every router.

**Sources.** [src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read records read.batch2-filter.2026-10-21 and read.batch2-content-router.2026-10-28.
read.batch2-filter.2026-10-21 serves the Message Filter and RabbitMQ example sections at
revision `899fcd8bbb8d91b9a0985314998a4707c1b4e0b34aa79a2821149c861d53db2c`; it is
publisher-abridged and states no rejected-message disposition, audit record, retention or
recovery path. The source is public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Content-Based Router; Selective Consumer; Publish-Subscribe.
