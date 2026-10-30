---
metadata_version: 1
id: "tycho.page.69fe87997d804b3f9ee0f7b9e1655c73"
kind: "page"
parent_id: "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/dedup-authority.md"
title: "Deduplication and consumer-local effects"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Which atomic authority boundary makes an outcome record useful?"
route_hints:
  questions:
    - "Which atomic authority boundary makes an outcome record useful?"
  prerequisites:
    - "tycho.page.d20ce26599b442d2bc00a6e388ac2c35"
  related_ids:
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
    - "tycho.page.33399db8d1574330951d9954801d6e71"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "dedup"
    - "authority"
evidence_scope:
  source_ids:
    - "src.http-semantics"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-30"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-30"
source_inspection_date: "2026-10-30"
content_verified_at: null
---
# Deduplication and consumer-local effects

**Owning question:** Which atomic authority boundary makes an outcome record useful?

This page belongs to [V04/C04 — Retries, idempotency and duplicate effects](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:4 -->
## 4. Deduplication is only as strong as its authority boundary

An in-memory set can deduplicate within one live process but fails across replicas, restarts and retained events. A durable database uniqueness constraint or state-machine conditional write can enforce one logical-effect record when scoped to the correct business domain.

A minimal conceptual contract is:
1. Authenticate and authorize each request.
2. Derive the normalized identity/semantic parameters and check them against any retained prior operation.
3. In one suitable durable authority boundary, decide **new, in-progress, committed, rejected, or incompatible duplicate**.
4. Commit the business effect and durable outcome correspondence with required atomicity.
5. Reply with an observation consistent with persisted truth.
6. Expose status lookup/reconciliation where an acknowledgment may be lost.
7. Define retention and what happens after keys expire.

If a downstream system can commit independently without supporting a stable effect key or readback, the caller may be unable to give an exactly-once **business** guarantee. Say **unknown** and design recovery rather than promising idempotence through an interface wrapper.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Idempotent Receiver](../../v11-pattern-atlas/c03-messaging-integration/README.md#idempotent-receiver) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:5 -->
## 5. Message redelivery and consumer effects

[Microservices.io's Idempotent Consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html) describes recording processed message IDs under a consumer identity in the same database transaction as the business update, so redelivery cannot apply it twice under that local model.

However, marking an event processed **before** making a separate external effect can lose the effect if the process crashes; marking it processed **after** can duplicate that external effect. The consumer must reason about the external capability's own idempotency/reconciliation boundary.

| Failure | Required evidence of safety |
|---|---|
| Duplicate message delivered concurrently to two workers | Atomic (consumer, event/effect ID) uniqueness with business update |
| Crash after DB commit, before ack | Redelivery resolves previously recorded outcome |
| Crash before DB commit | Retry may safely make first valid commit |
| Crash between DB and external delivery | External idempotency or durable reconciliation; local DB cannot make remote effect atomic |
| Event older than current entity state | Version/order/retention policy protects from stale effect |
| Wrong tenant/owner scope | Deduplication must not bypass authorization or cross tenant state |

The event ID is not necessarily the business command ID, nor the notification-delivery effect ID. Choosing all three to be equal can be legitimate only if their intended semantic scopes really coincide.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](intent-identity.md) |
| Next | [Continue the reasoning](retry-retention.md) |
| Integrated question | [Original scenario and limits](retries-idempotency-and-ambiguous-effects.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.

## Bounded pattern ownership notes

### Idempotent Receiver

An idempotent receiver makes redelivery safe for one consumer's local effects. The mechanism
describes recording processed message IDs under a consumer identity in the same database transaction
as the business update, so redelivery cannot apply it twice under that local model.

The Microsoft Azure Architecture Center Idempotent Consumer page states the atomic form directly:
"Avoid this failure window by writing the deduplication marker and the business side effects in
the same transaction." It also requires the data store, not application logic, to arbitrate a
concurrent claim: "Use a uniqueness constraint on the deduplication key such that two
transactions can attempt to insert a key, but only one can succeed." When independent consumers
share a store, it scopes the key to the consumer: "If the consumers share a deduplication store,
key the records on a composite of the consumer identity and the message identity." The page ties
that atomicity to recovery: "If a consumer commits both operations together or not at all, upon
redelivery it either finds the marker and skips the message, or finds no marker because the
transaction didn't complete and safely reprocesses the message."

Those sentences support the invariant: atomic (consumer, event/effect ID) uniqueness with the
business update under one local transactional authority. Deriving the key from consumer identity,
event identity and effect scope, validating that all three are present and well formed, and
rejecting a same-key/different-payload collision are Tycho guidance; the page supports the
transactional marker, the store-level uniqueness constraint and the consumer-scoped composite key,
not a complete key-derivation or collision-response procedure.

For an effect that cannot join the local transaction, the page identifies the crash window on the
marker-after side: "A check-then-process flow has a failure window. If a consumer processes a
message and then records the key in a separate step, a crash between the two operations leaves
the side effects applied but the key unrecorded, so the consumer reprocesses the next
redelivery." Its marker-before repair is a two-phase record: "Record the key with an in-progress
state, and then perform the external action. Update the record to completed and store the
outcome. On redelivery, a completed record tells the consumer to skip repeating the call. An
in-progress record signals that a previous attempt might be partially completed or is being
processed by another consumer. The consumer should reconcile stale records or route unresolved
cases for intervention before acknowledging redelivery." On retention and order, the page adds:
"Retain each record at least as long as the broker can still redeliver the original message."
"Set a time-to-live on deduplication records that exceeds this window, so that a late redelivery
still finds its marker." "Deduplication removes duplicates, but doesn't guarantee order."

The marker-before/marker-after comparison, the cleanup owner, the post-expiry rejection or
reconciliation route, and the tenant/owner-scope rule are Tycho guidance. The page supports the
in-progress/completed record pair, reconciliation of stale in-progress records, the retention
window, the TTL warning and the order caveat; it does not prescribe a complete repair algorithm,
a post-expiry policy or an ordering protocol.

A business-key upsert, a conditional write or the downstream API's idempotency key may be preferable
when no local processed-message table is available. An idempotent receiver is a fit when the
consumer owns a local transaction and can retain the dedup record for the redelivery horizon.

**Source boundary.** The Microsoft Learn page was read on 2026-10-30; its canonical text
SHA-256 is `f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`. The exact
sentences above are verbatim from "Commit the processed key and the side effects atomically",
"Guard against concurrent duplicates", "Choose a stable deduplication key", "Handle side effects
that can't join the transaction" and "Problems and considerations". The page is living
documentation with no published version identifier; the hash pins this representation. It does
not define a complete repair algorithm, a post-expiry policy, tenant scoping or a specific
ordering protocol.

