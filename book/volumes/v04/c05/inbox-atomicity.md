---
metadata_version: 1
id: "tycho.page.eba0d0f0151c4044a71589c4d216b4b9"
kind: "page"
parent_id: "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
canonical_path: "book/volumes/v04/c05/inbox-atomicity.md"
title: "Inbox processing and atomic consumer effects"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "When can a receiver commit an effect and its deduplication record together?"
route_hints:
  questions:
    - "When can a receiver commit an effect and its deduplication record together?"
  prerequisites:
    - "tycho.page.9daa9ce90a5047fa849c637f24b063f7"
  related_ids:
    - "tycho.chapter.18aa94285a164b6f94530cebcfd87b8b"
    - "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
    - "tycho.page.71aea7bc58a6411ba7baf8a2ff40ffbd"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "inbox"
    - "atomicity"
evidence_scope:
  source_ids:
    - "src.idempotent-consumer-pattern"
  claim_ids: []
  status: "source-linked"
  notes: "Bounded question from tycho.page.aa810dd152884b35a84f0f4cbe4369e9; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-20"
  reviewer: "Codex editorial decomposition"
  proof_uri: null
authored_at: "2026-10-20"
updated_at: "2026-10-20"
source_inspection_date: "2026-10-20"
content_verified_at: null
---
# Inbox processing and atomic consumer effects

**Owning question:** When can a receiver commit an effect and its deduplication record together?

This page belongs to [V04/C05 — Outbox, inbox, sagas and durable workflows](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.aa810dd152884b35a84f0f4cbe4369e9:3 -->
## 3. Inbox and consumer-local atomicity

An inbox can persist a consumer's processed-event identity and business effect together in **one local transaction**. The [Idempotent Consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html) describes deduplication using a processed-message table or the business aggregate itself.

The identity must include the correct subscriber and event/effect scope; two different consumers legitimately process the same event into different local states. An in-memory set is not sufficient when the contract requires restart-safe deduplication.

**Fictional failure:** a notification consumer writes a processed marker then crashes before making an external non-idempotent send. On redelivery it may falsely skip the missing send. Reversing the order may send twice. Correctness may require a *second* durable send-intent record and cooperation or reconciliation with the downstream delivery provider. A transactional inbox does **not** guarantee exactly-once side effects outside its local authority.

<!-- /tycho-question-source -->

## A four-window consumer recovery trace

In an original fictional booking consumer, an incoming message carries a stable logical identity. The consumer's local transaction attempts to record that identity and change the authoritative booking state. The two writes belong to the same commit boundary; a separate acknowledgment to the broker follows the durable outcome.

There are four different crash windows. Before either write commits, retry must be able to attempt the operation. After an identity is recorded but before the business effect commits, a design using separate transactions can falsely suppress a missing effect. After the business effect commits but before the identity commits, the inverse design can apply the effect twice. When both records commit together but the acknowledgment is lost, redelivery should recognize the already recorded result.

Concurrent delivery adds a separate race. Two handlers checking for absence before either commits can both believe the message is new. A uniqueness or equivalent atomic authority rule must decide which transaction can record the identity, with failure handled as part of the intended protocol rather than as an unrelated unexpected error.

This boundary covers effects controlled by that transaction. It cannot include an independently committed email or remote API call merely because the local handler invokes it. That second boundary needs its own durable intent, idempotency or reconciliation contract. The [original idempotent-consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html) supplies the bounded recording pattern; this crash schedule is original reasoning and was not executed.

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](outbox-publication.md) |
| Next | [Continue the reasoning](saga-workflows.md) |
| Integrated question | [Original scenario and limits](outbox-inbox-sagas-and-durable-workflows.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
