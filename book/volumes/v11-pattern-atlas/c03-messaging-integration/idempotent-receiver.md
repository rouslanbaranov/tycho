---
metadata_version: 1
id: "tycho.page.8d1dbd92ef5042739736443d1f5a3d81"
kind: "page"
parent_id: "tycho.chapter.a4b31346a691566550633efe0cf2693e"
canonical_path: "book/volumes/v11-pattern-atlas/c03-messaging-integration/idempotent-receiver.md"
title: "Idempotent Receiver"
topic_ids:
  - "integration-architecture"
  - "architecture-decisions"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Decision card for Idempotent Receiver with bounded owner evidence."
route_hints:
  questions:
    - "Should the receiver detect duplicate deliveries and avoid duplicate effects?"
  prerequisites:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  related_ids:
    - "tycho.chapter.a4b31346a691566550633efe0cf2693e"
  excludes:
    - "No sufficient coverage, promotion or owner acceptance is claimed for this moved page."
  keywords:
    - "pattern atlas"
    - "idempotent-receiver"
    - "duplicate detection"
evidence_scope:
  source_ids:
    - "src.enterprise-integration"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Dedicated card page; source bindings remain in the owner unit."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-30"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---

# Idempotent Receiver

**Identity.** Idempotent Receiver; family Messaging and event-driven integration; kind
messaging-pattern; priority core.

**Decision question.** Should the receiver detect duplicate deliveries and avoid duplicate
effects?

**Good-fit conditions.** Messages carry stable identity; effect and identity are recorded
atomically; retention covers the redelivery window; concurrent duplicates are handled.

**Hard contraindications.** Reject when the effect is naturally idempotent, when identity
is unstable, or when deduplication state cannot be retained.

**Competing alternative.** Natural idempotency or a transactional inbox. Reverse the
choice when identity retention and lookup cost exceed duplicate risk.

**Failure and recovery.** A crash after a separate external effect but before its
marker can duplicate the effect; a marker written before the effect can leave an
in-progress record that needs reconciliation. The Microsoft Learn Idempotent
Consumer page supplies the check-then-process window, the in-progress/completed
marker pair and the reconcile-stale-records rule. Cleanup ownership, post-expiry
routing and the order/version policy beyond the page's caveat are Tycho guidance.

**Technical owner.** [Idempotent Receiver](../../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/dedup-authority.md#idempotent-receiver) — deduplication authority is bounded, not a complete idempotent-receiver recipe.

**Sources.**
[src.enterprise-integration](../../../../edition/patterns/reading-ledger.v1.json)
read record read.batch2-idempotent.2026-10-21: served problem/solution; publisher-abridged.
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json)
read record read.microsoft-idempotent-consumer.2026-10-30: sections "Commit the
processed key and the side effects atomically", "Guard against concurrent
duplicates", "Choose a stable deduplication key", "Handle side effects that can't
join the transaction" and "Problems and considerations". Exact quotes: "Avoid this
failure window by writing the deduplication marker and the business side effects in
the same transaction."; "Use a uniqueness constraint on the deduplication key such
that two transactions can attempt to insert a key, but only one can succeed.";
"Record the key with an in-progress state, and then perform the external action.";
"The consumer should reconcile stale records or route unresolved cases for
intervention before acknowledging redelivery." Revision
`f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`. The source is
public documentation, not a benchmark.

**Decision state.** applicable-under-conditions.

**Related entries.** Point-to-Point Queue; Transactional Inbox; Idempotency Key; Retry
with Exponential Backoff.
