---
metadata_version: 1
id: "tycho.page.33399db8d1574330951d9954801d6e71"
kind: "page"
parent_id: "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/retry-retention.md"
title: "Retry budgets, retention and adversarial tests"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "What prevents retries or delayed replay from violating capacity and effect guarantees?"
route_hints:
  questions:
    - "What prevents retries or delayed replay from violating capacity and effect guarantees?"
  prerequisites:
    - "tycho.page.69fe87997d804b3f9ee0f7b9e1655c73"
  related_ids:
    - "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
    - "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
  excludes:
    - "No independent technical approval, runtime experiment or universal applicability is implied."
  keywords:
    - "retry"
    - "retention"
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
# Retry budgets, retention and adversarial tests

**Owning question:** What prevents retries or delayed replay from violating capacity and effect guarantees?

This page belongs to [V04/C04 — Retries, idempotency and duplicate effects](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.

<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:6 -->
## 6. Retry policy must protect overload and deadlines

Retry only when an error class and the business contract permit it. Backoff/jitter, per-operation attempt budgets, total absolute deadline and cancellation are architectural controls, but no combination makes non-idempotent effects safe by itself.

Nested retries can multiply calls; a bounded outer retry policy may still overload a downstream service with its own retry layer. Degraded conditions need explicit rejection and **unknown outcome** states rather than suppressed failures. [Overload/admission](../../v07-performance-scale-and-resilience/c05-overload-protection-and-graceful-degradation/overload-admission-control-and-graceful-degradation.md) owns broader capacity policy.

A successful API response is not a guarantee that unrelated optional notification is completed. Use a durable accepted/pending contract when the business effect truly spans time.


### Worked race: two simultaneous first requests

**Original fictional scenario:** two requests A and B for the same tenant-scoped operation key K42 arrive concurrently. Both look up K42 before either commits. An implementation that checks for absence and then creates a booking without an atomic uniqueness/conditional-write rule can commit two different bookings despite sending the same key.

| Failure stage | Necessary authority rule |
|---|---|
| Concurrent first attempts | One atomic key-and-payload decision across all replicas; no local-only mutex |
| A commits R7 but its reply is lost | Retrying K42 resolves to R7, never creates R8 |
| B reuses K42 with changed booking parameters | Detect a parameter conflict; returning R7 would affirm the wrong intent |
| Old request replays after key expiry | A finite retention window cannot promise deduplication forever; reconcile by durable business identity |
| Downstream consumer repeats a side effect | Consumer-effect identity must be enforced at that effect's actual durability boundary |

**Alternative designs:** use a transactionally unique operation record, a queryable pending command or serialized per-key processing, provided their own failover/retention semantics are demonstrable. [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) describes HTTP idempotent method meaning, not a POST key contract. The [Idempotent Consumer pattern](https://microservices.io/patterns/communication-style/idempotent-consumer.html) describes duplicate-message protection, not universal external exactly-once effects.

**Proposed, not executed:** start A and B at a synchronization barrier, lose A's response after commit, restart the server, change K42's payload and replay it beyond the declared horizon. Count logical intents, durable outcomes and unresolved effects separately. Publication after commit belongs to the [outbox/workflow owner](../c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md).

<!-- /tycho-question-source -->
<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:7 -->
## 7. Negative and acceptance tests

An independent fixture would test two simultaneous requests with the same K/P, K reused with different payload, lost acknowledgment after commit, crash before/after the atomic outcome record, redelivered message to two consumers, delayed replay after key expiry and a downstream side effect without readback.

For each case count logical intents, transmitted attempts, accepted effects, duplicate observable side effects and unresolved outcomes **separately**. No such tests have been executed for this chapter.

<!-- /tycho-question-source -->

## Navigation, prerequisites and source scope

| Route | Destination |
|---|---|
| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |
| Previous / prerequisite | [Read preceding context](dedup-authority.md) |
| Next | [Continue the reasoning](README.md) |
| Integrated question | [Original scenario and limits](retries-idempotency-and-ambiguous-effects.md) |

The source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.
