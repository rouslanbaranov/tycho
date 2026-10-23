---
metadata_version: 1
id: "tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f"
kind: "page"
parent_id: "tycho.chapter.a92541ba2fb44cf1a3afef1f9c021fe0"
canonical_path: "book/volumes/v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md"
title: "Retries, idempotency and ambiguous side effects"
topic_ids:
  - "distributed-systems"
perspectives:
  - "architecture"
summary: "Integrated question, original scenario and transfer limits for Retries, idempotency and duplicate effects. Detailed mechanisms have separate question owners."
route_hints:
  questions:
    - "Which side effects survive retries and ambiguous acknowledgements?"
  prerequisites: []
  related_ids:
    - "tycho.page.ace968ab1de8409383c6a9b22a00d006"
    - "tycho.page.aa810dd152884b35a84f0f4cbe4369e9"
    - "tycho.page.c5d20ae7ef6445e5b23dd5fbac625060"
    - "tycho.landing.1a9054fd18f64dfe911f34a4d17458c0"
    - "tycho.landing.ddbfbbbe1a85406faa2705102378beea"
    - "tycho.page.cccbd188936543a2aaf904f4002236d8"
    - "tycho.page.3c78e2b17ac74973b2ae658977843c2a"
    - "tycho.page.d20ce26599b442d2bc00a6e388ac2c35"
    - "tycho.page.69fe87997d804b3f9ee0f7b9e1655c73"
    - "tycho.page.33399db8d1574330951d9954801d6e71"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Retries"
    - "idempotency"
    - "and"
    - "ambiguous"
    - "side"
    - "effects"
evidence_scope:
  source_ids:
    - "src.http-semantics"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---
<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:-1 -->

# Retries, idempotency and ambiguous side effects

> **Tycho book manuscript — proposed V04/C04**, 2026-10-19. Original synthetic command and failure sequences. Independently inspected RFC 9110 §9.2.2 and public idempotent-consumer pattern references. No service, transaction, replay, production trace or independently reviewed contract test was executed. Previous combined [outbox/idempotency research](../../../distributed/transactional-outbox-and-idempotency.md) remains preserved for detailed source-claim reconciliation.

<!-- /tycho-question-source -->

> **Pattern atlas:**
> [Idempotency Key](../../v11-pattern-atlas/c04-consistency-events/README.md#idempotency-key) — decision conditions and contraindications.

<!-- tycho-question-source:tycho.page.8d28a6e14a1c49d6b67bf9cb5bfb242f:0 -->
## Purpose and mission

In distributed systems, a client can lose the response to a command **after** the server commits its effect. The client observes “no answer,” not necessarily “no commit.” Repeating a state-changing operation without identifying it as the same business intent can violate critical invariants.

**Idempotence is a property of the intended effect**, not a promise that HTTP status codes, logs or network attempts will look identical. The [RFC 9110, §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) defines idempotent method semantics; this is different from application-level idempotency keys for non-idempotent workflows. This chapter owns *request/effect identity and retry safety*. [Outbox, inbox, sagas and durable workflows](../c05-outbox-inbox-sagas-and-durable-workflows/outbox-inbox-sagas-and-durable-workflows.md) owns durable publication and multi-step state coordination.

<!-- /tycho-question-source -->

## Integrated decision and reading route

Bind retries to a stable logical intent, payload and retention policy with an authoritative recorded outcome.

After an acknowledgment is lost, a new identity can duplicate a committed effect; an expired key cannot guarantee historical deduplication.

**Idempotency-key contract.** The key binds one logical intent, caller/payload scope and
retention window to an authoritative outcome record. It must be stable across retries,
scoped so another caller cannot collide, and checked atomically with the effect. The
server returns the recorded outcome for a duplicate, rather than executing again.

**Invariant.** A key is only useful while its outcome record is retained; after expiry,
historical deduplication is no longer guaranteed. The key does not make a different payload
safe: a reused key with changed intent is a conflict, not idempotency.

**Alternative.** A naturally idempotent operation, a conditional/unique constraint, or a
single-writer serialization may be preferable when the effect can be expressed without a
key store. Reverse the key choice when retention, storage or caller-scope complexity
exceeds the duplicate-effect risk.

The detailed pages separate the mechanisms that make this decision conditional:

- [Logical intent and duplicate submission](intent-identity.md) — How are retry attempts bound to one payload and business intent?
- [Deduplication and consumer-local effects](dedup-authority.md) — Which atomic authority boundary makes an outcome record useful?
- [Retry budgets, retention and adversarial tests](retry-retention.md) — What prevents retries or delayed replay from violating capacity and effect guarantees?

[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.

## Bounded pattern ownership notes

### Idempotency Key

An idempotency key belongs to the operation owner, who defines its scope, fingerprint inputs and
retention period. Callers choose a value only within that published contract. The owner also
names the conflict response and the record a support engineer may inspect.

The outcome record and business effect must commit together; a later separate write leaves a
window for duplicate execution. The owner treats a changed fingerprint on a reused key as a new
decision rather than a replay.

Retention is a product and compliance decision, not an arbitrary cache timeout. State what
happens after expiry and how an operator resolves a caller that retries beyond it.

Some effects can rely on a uniqueness rule, a compare-and-set or one writer instead of a key
store. Review the contract when payload shape, caller population or retention cost changes. A
key store without a cleanup plan becomes an unbounded dependency.
