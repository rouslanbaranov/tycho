---
metadata_version: 1
id: "tycho.page.d9c13bc73d3060017a13776ac9dec4b9"
kind: "page"
parent_id: "tycho.chapter.e9c650012060143639af44b0cfdc4236"
canonical_path: "book/volumes/v11-pattern-atlas/c04-consistency-events/idempotency-key.md"
title: "Idempotency Key"
topic_ids:
  - "data-architecture"
  - "distributed-systems"
perspectives:
  - "architecture"
  - "evaluation"
summary: >-
  Decision card for Idempotency Key; all four dimensions source-bound; coverage
  remains partial-bounded, no promotion.
route_hints:
  questions:
    - >-
      Should a client-supplied key let the server recognize retries of one logical
      request?
  prerequisites:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  related_ids:
    - "tycho.chapter.e9c650012060143639af44b0cfdc4236"
  excludes:
    - >-
      No sufficient coverage, promotion or owner acceptance is claimed for this
      moved page.
  keywords:
    - "pattern atlas"
    - "idempotency key"
    - "data consistency"
evidence_scope:
  source_ids:
    - "src.ietf-idempotency-key"
    - "src.aws-idempotency"
    - "src.stripe-idempotency"
    - "src.microsoft-cloud-patterns"
  claim_ids: []
  status: "source-linked"
  notes: >-
    Card cites read.ietf-idempotency-key-08.2026-10-31,
    read.aws-idempotency.2026-10-31, read.stripe-idempotent-requests.2026-10-31
    and read.microsoft-idempotent-consumer.2026-10-31; owner section and limits
    are bounded.
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-31"
  reviewer: "Automated authoring agent"
  proof_uri: null
authored_at: "2026-10-31"
updated_at: "2026-10-31"
source_inspection_date: "2026-10-31"
content_verified_at: null
---
# Idempotency Key

**Identity.** Idempotency Key; family Data consistency, transactions and event sourcing;
kind api-pattern; priority core.

**Decision question.** Should a client-supplied key let the server recognize retries of
one logical request?

**Good-fit conditions.** Retries are expected; the operation owner publishes key scope,
fingerprint inputs and retention; the outcome record and effect commit together; a
support-visible record survives the retry window.

**Hard contraindications.** Reject when operations are naturally idempotent, when keys can
collide across tenants, when retention cannot cover the retry window, or when the key store
has no expiry and cleanup owner.

**Competing alternative.** Natural idempotency, a uniqueness constraint, a compare-and-set
or one writer. Reverse when key storage and fingerprinting cost exceed retry risk, or when
payload shape, caller population or retention cost changes.

**Failure and recovery.** Expiry ends historical deduplication; a reused key with changed
intent is a conflict, not idempotency. The IETF draft separates 400 (missing key), 422
(different payload) and 409 (original request still in progress); Stripe returns the saved
response, including 500 errors; AWS stores the initial parameters and returns a validation
error on mismatch; Azure keeps an in-progress/completed record and says to "reconcile stale
records or route unresolved cases for intervention before acknowledging redelivery." Tycho:
reject mismatched fingerprints, distinguish in-progress from expired, and keep the record for
the retry window.

**Technical owner.** [Idempotency Key](../../v04-distributed-coordination-and-events/c04-retries-idempotency-and-duplicate-effects/retries-idempotency-and-ambiguous-effects.md#idempotency-key) — key ownership, fingerprint, atomic commit, conflict response and retention are source-bound; the four-part contract remains Tycho.

**Sources.** [src.ietf-idempotency-key](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.batch2-ietf.2026-10-21` (draft-07, historical) and read record
`read.ietf-idempotency-key-08.2026-10-31` (draft-08, current): sections 2.2-2.7.
[src.aws-idempotency](../../../../edition/patterns/reading-ledger.v1.json) read record
`read.aws-idempotency.2026-10-31`: sections "Introduction", "Retrying and side effects",
"Reducing client complexity", "Late arriving requests" and "Same client request ID,
different intent". [src.stripe-idempotency](../../../../edition/patterns/reading-ledger.v1.json)
read record `read.stripe-idempotent-requests.2026-10-31`: section "Idempotent requests".
[src.microsoft-cloud-patterns](../../../../edition/patterns/reading-ledger.v1.json) read
record `read.microsoft-idempotent-consumer.2026-10-30` and read record
`read.microsoft-idempotent-consumer.2026-10-31`: sections "Choose a stable deduplication
key", "Commit the processed key and the side effects atomically", "Guard against concurrent
duplicates", "Handle side effects that can't join the transaction" and "Problems and
considerations". The sources are public documentation, not benchmarks; Tycho-labelled rules
are synthesis.

**Decision state.** applicable-under-conditions.

**Related entries.** Idempotent Receiver; Transactional Inbox; Retry with Exponential
Backoff; Correlation Identifier.
