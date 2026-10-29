---
metadata_version: 1
id: "tycho.page.5eda4c047acb44699a8e444b66ea5ec2"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/transactional-outbox.md"
title: "Transactional Outbox"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Transactional Outbox with bounded owner evidence."
route_hints:
  questions:
    - "Should publication intent be stored in the same local transaction as the state change?"
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "transactional outbox"
    - "outbox"
evidence_scope:
  source_ids:
    - "src.microservices-patterns"
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
source_inspection_date: "2026-10-21"
content_verified_at: null
---

# Transactional Outbox

**Identity.** Transactional Outbox; family Data consistency, transactions and event
sourcing; kind data-pattern; priority core.

**Decision question.** Should publication intent be stored in the same local transaction
as the state change?

**Good-fit conditions.** The database supports a local transaction; a relay can publish
later within a bounded age; duplicate publication is deduplicated; relay ownership and
retention are explicit.

**Hard contraindications.** Reject when the state store cannot share a transaction with an
outbox, when publication latency is unacceptable, or when no relay is operated.

**Competing alternative.** Event sourcing is an alternative solution.

**Failure and recovery.** A crash after publish/before checkpoint duplicates; a crash after
commit/before publish retries; a poison row can block progress. Bound attempts/age and keep
repair evidence.

**Technical owner.** [Transactional Outbox](../../v04-distributed-coordination-and-events/c05-outbox-inbox-sagas-and-durable-workflows/transactional-outbox.md#transactional-outbox) — outbox coordination is bounded, not a
connector manual.

**Sources.**
[src.microservices-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-outbox.2026-10-21: all nine served headings read.
The source is a public pattern/specification
unit, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Transactional Inbox; Domain Events; CDC; Idempotent Receiver.
