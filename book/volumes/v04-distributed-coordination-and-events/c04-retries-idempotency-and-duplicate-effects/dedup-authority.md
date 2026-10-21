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
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: null
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
