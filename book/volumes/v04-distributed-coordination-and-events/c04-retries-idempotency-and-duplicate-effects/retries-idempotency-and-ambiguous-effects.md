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
    - "src.ietf-idempotency-key"
  claim_ids: []
  status: "source-linked"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-31"
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

**Mechanism — key ownership, scope, fingerprint and retention (Tycho synthesis).** An
idempotency key belongs to the operation owner, who defines its scope, fingerprint inputs and
retention period. Callers choose a value only within that published contract.

The IETF draft makes the ownership boundary normative: "Uniqueness of the key MUST be defined
by the resource owner and MUST be implemented by the clients of the resource." It also states:
"The idempotency key MUST be unique and MUST NOT be reused with another request with a different
request payload." It recommends a UUID and asks the resource to define and publish an expiry
policy: "The resource SHOULD define such expiration policy and publish it in the documentation."
"An idempotency fingerprint MAY be used in conjunction with an idempotency key to determine the
uniqueness of a request"; it is generated by the resource from payload data. AWS describes the
same contract in API terms: "A unique caller-provided client request identifier for idempotent
operations meets this need." The service records an idempotent session keyed off the caller and
that identifier, and the identifier is "readily auditable" because it appears in logs. Stripe
puts key generation on the client, caps a key at 255 characters and says: "For API v1, you can
remove keys from the system automatically after they’re at least 24 hours old." Azure requires
a key that "must uniquely and consistently identify the logical message across every
redelivery" and, when consumers share a store, a composite of consumer identity and message
identity.

Tycho synthesis: scope, fingerprint inputs and retention are one published contract, not
independent settings. A key value alone does not define whose intent it is, and an unpinned
client-generated key is not tenant-safe. Retention is a product and compliance decision, not an
arbitrary cache timeout. State what happens after expiry and how an operator resolves a caller
that retries beyond it.

**Invariant — outcome record and business effect commit together (Tycho rule, source-bound
premise).** The outcome record and business effect must commit together; a later separate write
leaves a window for duplicate execution. AWS states the rule as an ACID requirement: "An
important consideration is that the process that combines recording the idempotent token and all
mutating operations related to servicing the request must meet the properties for an atomic,
consistent, isolated, and durable (ACID) operation." Azure states the consumer-side version:
"Avoid this failure window by writing the deduplication marker and the business side effects in
the same transaction."

The IETF draft does not require this atomic commit. In draft-08 a completed retry should return
a response "consistent with the request being completed according to the user's intent"; that
is weaker than an outcome record committed with the effect. Tycho rule: an effect without the
record, or a record without the effect, is not an idempotency contract. The owner treats a
changed fingerprint on a reused key as a new decision rather than a replay.

**Failure and recovery — conflict response and inspectable record (Tycho rule, source-bound
mechanics).** The owner also names the conflict response and the record a support engineer may
inspect. The IETF draft separates the responses: 400 when a required key is missing, 422 when a
key is reused with a different payload, and 409 while the original request is still being
processed. AWS says: "we return a validation error indicating a parameter mismatch between
idempotent requests." It also stores the initial parameters with the client request identifier;
the identifier is visible in logs and on the created resource. Stripe saves the status code and
body of the first request after endpoint execution begins: "Retries with the same key return the
saved response, including 500 errors." It also errors when the incoming parameters differ. Azure
records an in-progress state, updates it to completed with the outcome, and tells the consumer
to "reconcile stale records or route unresolved cases for intervention before acknowledging
redelivery."

Tycho rule: an inspectable record carries the key, caller scope, fingerprint inputs, outcome and
state. Expired, in-progress and fingerprint-mismatch states are distinct answers, not one generic
duplicate error.

**Alternative — uniqueness rule, compare-and-set or one writer (Tycho choice rule, source-bound
premise).** Some effects can rely on a uniqueness rule, a compare-and-set or one writer instead
of a key store. Azure makes the rule concrete: "Use a uniqueness constraint on the deduplication
key such that two transactions can attempt to insert a key, but only one can succeed." It also
says: "Use an atomic conditional write, such as an insert that fails on conflict or a
set-if-absent operation, to make claiming the key a single atomic step." The source says this
approach makes the database "the single arbiter of the conflict." The IETF draft separates
methods: "the methods OPTIONS, HEAD, GET, PUT and DELETE are idempotent while methods POST and
PATCH are not." Stripe says: "Don’t send idempotency keys in GET and DELETE requests because it
has no effect. These requests are idempotent by definition."

AWS describes a `ResourceAlreadyExists` response as side-effect free: "This meets the basic
tenets for idempotency because there is no side effect for retrying the call." It also notes
that the response leaves the caller unable to tell whether this request or an earlier one
created the resource. Tycho choice rule: prefer natural idempotency, a uniqueness constraint, a
compare-and-set or one writer when they express the effect without a separate key store. Reverse
the key choice when retention, storage or caller-scope complexity exceeds the duplicate-effect
risk, or when payload shape, caller population or retention cost changes. A key store without a
cleanup plan becomes an unbounded dependency.

**Source boundary.** Public units accessed 2026-10-31. Quotes are short excerpts; line breaks
inside a quote are editorial wrapping. Tycho-labelled rules are synthesis, not source claims.

- IETF, *The Idempotency-Key HTTP Header Field*,
  draft-ietf-httpapi-idempotency-key-header-08, 22 October 2026, sections 2.2-2.7: raw text
  SHA-256 `25dcfa45f2fcbe3d8bc00e2c8b2bf396dfe1bbcea991a535f2fedce3728ed4a3`; proposed record
  `read.ietf-idempotency-key-08.2026-10-31`. The retained draft-07 record
  `read.batch2-ietf.2026-10-21` remains historical.
- AWS Builders' Library, "Making retries safe with idempotent APIs", sections "Introduction",
  "Retrying and side effects", "Reducing client complexity", "Late arriving requests" and "Same
  client request ID, different intent": canonical text SHA-256
  `c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac`, raw HTML SHA-256
  `f1a8595955fe0900386eb9a1191184ee9e60fd117a2e7f7219ef6a5d1b2d8139`; Last-Modified
  2026-10-27; proposed record `read.aws-idempotency.2026-10-31`.
- Stripe, "Idempotent requests", section "Idempotent requests": canonical text SHA-256
  `fdda1f88aa51ec91f7655939cba5063dd8e256f20e00933209172fb3ef5d49ef`, raw HTML SHA-256
  `c1eb7968fc1fbecf85552f29f87b9dd1ec0648985e5ce42095172fd04f14d34d`; no page revision header,
  displays API version 2026-10-28; proposed record
  `read.stripe-idempotent-requests.2026-10-31`.
- Microsoft Azure Architecture Center, "Idempotent Consumer pattern", sections "Choose a stable
  deduplication key", "Commit the processed key and the side effects atomically", "Guard against
  concurrent duplicates", "Handle side effects that can't join the transaction" and "Problems
  and considerations": canonical text SHA-256
  `f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`; retained record
  `read.microsoft-idempotent-consumer.2026-10-30`; the 2026-10-31 refetch is byte-identical and
  the added key-stability, conditional-write and natural-idempotency claims are proposed for
  record `read.microsoft-idempotent-consumer.2026-10-31`.

The retained `src.ietf-idempotency-key` draft-07 record remains a historical reading; this
section binds the current draft-08 text.
