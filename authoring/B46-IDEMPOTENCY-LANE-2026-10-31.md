# B46 — Idempotency Key four-dimension lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 0/4 at the parent HEAD: mechanism, invariant, failure/recovery and
alternative were all partial. This lane binds all four to the exact IETF
Idempotency-Key draft-08, the AWS Builders' Library idempotency article, the
Stripe idempotent-requests reference and the Azure Architecture Center
Idempotent Consumer pattern, and labels the Tycho contract rules as synthesis.
The card remains inline in V11/C04.

## Lane coordinates

- Parent HEAD: 0604f3db50f0d9e09dbe9c1ded6acfe24d481175 (0604f3db).
- Branch: b46-idempotency; worktree:
  /Users/rbaranov/Projects/tycho-worktrees/b46-idempotency.
- Scope: the owner section "### Idempotency Key" in V04/C04 and the inline
  V11/C04 card "### Idempotency Key". Single-entry lane; no other entry,
  shared JSON, promotion or generated file is changed.
- Owner path (concatenate):

      book/volumes/v04-distributed-coordination-and-events/
      c04-retries-idempotency-and-duplicate-effects/
      retries-idempotency-and-ambiguous-effects.md

- Card path:
  book/volumes/v11-pattern-atlas/c04-consistency-events/README.md.
- Existing source ids: src.http-semantics and src.ietf-idempotency-key on the
  owner page; src.ietf-idempotency-key on the card. Added card ids:
  src.aws-idempotency and src.stripe-idempotency; src.microsoft-cloud-patterns
  was already declared.
- New ledger records: read.ietf-idempotency-key-08.2026-10-31,
  read.aws-idempotency.2026-10-31,
  read.stripe-idempotent-requests.2026-10-31 and
  read.microsoft-idempotent-consumer.2026-10-31.
- Retained historical records: read.batch2-ietf.2026-10-21 (draft-07) and
  read.microsoft-idempotent-consumer.2026-10-30 (same canonical digest as the
  2026-10-31 refetch).
- Final line-length and boundary checks pass.

## Baseline state

- At HEAD, all four dimensions were partial. The owner-unit reasons were:
  mechanism, the source states key uniqueness scope but not the full
  fingerprint/expiry mechanism; invariant, the source has no atomic
  outcome-record plus business-effect rule; failure/recovery, the source
  defines retry/concurrent outcomes but no support-visible record;
  alternative, the source varies key carrier but not the uniqueness-rule or
  single-writer choice.
- The owner page already carried the four owner-unit quotes verbatim. This
  lane keeps them unchanged and adds source bindings around them.
- The retained draft-07 record is historical evidence. It does not support the
  draft-08 retry wording or the draft-08 responsibility text.
- The Microsoft Idempotent Consumer record 2026-10-30 already binds atomic
  marker-plus-effect, uniqueness, conditional write and retention. The
  2026-10-31 refetch produced the same canonical digest; the new record adds
  the key-stability, conditional-write and natural-idempotency claims used by
  the card.

## Candidate evaluation

- IETF, "The Idempotency-Key HTTP Header Field" (selected, current draft-08).
  Draft-08 is dated 22 October 2026 and supersedes draft-07 (15 October
  2025); the source register still pins the older draft. It defines key
  uniqueness, ownership, expiry-policy publication, fingerprint input and
  lifecycle responsibility. It does not require the outcome record to commit
  atomically with the business effect and it does not define a
  support-inspection record. Its Retry text changed from
  "result of the previously completed operation" in draft-07 to a response
  "consistent with the request being completed according to the user's
  intent"; Appendix A says the Retry text is still open for discussion.
- AWS Builders' Library, "Making retries safe with idempotent APIs" (selected).
  It defines a unique caller-provided client request identifier, an idempotent
  session keyed off the caller and identifier, auditable logs, ACID recording
  of the token with all mutating operations, retention bounded by the resource
  lifetime plus a late-arrival interval, and a validation error on a changed
  parameter combination. It is narrative engineering guidance, not a tested
  implementation.
- Stripe, "Idempotent requests" (selected). It defines client-generated keys,
  a saved status/body returned on retry, parameter comparison, a 24-hour API
  v1 retention floor and natural method idempotence. It describes API v1
  behavior; API v2 retries differ and are described separately on the same
  page.
- Microsoft Azure Architecture Center, "Idempotent Consumer pattern"
  (selected). It defines a stable deduplication key, atomic marker-plus-effects
  commit, uniqueness/conditional-write concurrency control, an
  in-progress/completed record and retention longer than the redelivery
  window. It is consumer-side pattern guidance, not an HTTP Idempotency-Key
  specification. The page has no complete repair algorithm or post-expiry
  policy.
- The owner page's existing src.http-semantics citation remains a protocol
  idempotence boundary only; it does not bind application-level key scope,
  retention or conflict responses.

## Source binding

Quotes reproduce the served prose. Line breaks inside a quote are editorial
wrapping. The binding revision is the record content_sha256: raw text for the
plain-text IETF draft and canonical text for the HTML pages, extracted with
scripts/source_content_hash.py. Quoted fragments were checked as
whitespace-normalized substrings of the served representation. The
Tycho-labelled sentences are not presented as source quotes.

### IETF — The Idempotency-Key HTTP Header Field, draft-08

- Source id: src.ietf-idempotency-key (existing).
- New record: read.ietf-idempotency-key-08.2026-10-31.
- URL:
  https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-08.txt
- Unit label: "The Idempotency-Key HTTP Header Field — IETF Internet-Draft
  08"; unit type specification; access date 2026-10-31.
- Representation: HTTP 200, 25,624 bytes, HTTP Date 2026-10-31T05:19:38Z,
  Last-Modified 2026-10-22T18:28:54Z, ETag "6ada55e6-6418"; raw text SHA-256
  25dcfa45f2fcbe3d8bc00e2c8b2bf396dfe1bbcea991a535f2fedce3728ed4a3;
  22,097 characters, 3,397 words; the draft expires 2027-04-25. A second
  fetch is byte-identical.
- Sections used: "Introduction", "Notational Conventions", "The
  Idempotency-Key HTTP Request Header Field", "Syntax", "Uniqueness of
  Idempotency Key", "Idempotency Key Validity and Expiry", "Idempotency
  Fingerprint", "Responsibilities", "Client", "Resource", "Idempotency
  Enforcement", "Error Handling".
- Exact quotes:

      An idempotency key is a unique value generated by the client which the
      resource uses to recognize subsequent retries of the same request.

      The idempotency key MUST be unique and MUST NOT be reused with another
      request with a different request payload.

      Uniqueness of the key MUST be defined by the resource owner and MUST be
      implemented by the clients of the resource.

      The resource SHOULD define such expiration policy and publish it in the
      documentation.

      An idempotency fingerprint MAY be used in conjunction with an
      idempotency key to determine the uniqueness of a request.

      A resource is responsible for managing the lifecycle of the idempotency
      key.

      The resource SHOULD respond with a response consistent with the request
      being completed according to the user's intent.

      The resource SHOULD respond with a resource conflict error.

      If there is an attempt to reuse an idempotency key with a different
      request payload, the resource SHOULD reply with an HTTP 422 status code
      with body containing a link pointing to relevant documentation.

      If the request is retried, while the original request is still being
      processed, the resource SHOULD reply with an HTTP 409 status code with
      body containing problem description.

      If the Idempotency-Key request header is missing for a documented
      idempotent operation requiring this header, the resource SHOULD reply
      with an HTTP 400 status code with body containing a link pointing to
      relevant documentation.

      the methods OPTIONS, HEAD, GET, PUT and DELETE are idempotent while
      methods POST and PATCH are not.

- Limits: one Internet-Draft, not an RFC; expires 2027-04-25. It does not
  require an atomic outcome-record plus effect commit, an inspectable support
  record, a tenant scope or a particular fingerprint algorithm. The Retry
  wording is weaker in draft-08 than in draft-07 and remains open for
  discussion. The draft's own examples are not reproduced.

### AWS — Making retries safe with idempotent APIs

- Source id: src.aws-idempotency (existing).
- New record: read.aws-idempotency.2026-10-31.
- URL:
  https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
- Unit label: "Making retries safe with idempotent APIs — Amazon Builders'
  Library"; unit type engineering-article; access date 2026-10-31.
- Representation: HTTP 200, 456,055 bytes, HTTP Date
  2026-10-31T05:19:39Z, Last-Modified 2026-10-27T00:27:38Z, no ETag; raw HTML
  SHA-256
  f1a8595955fe0900386eb9a1191184ee9e60fd117a2e7f7219ef6a5d1b2d8139;
  canonical text SHA-256
  c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac;
  20,123 characters, 3,115 words; no published version identifier. A second
  fetch returns the same canonical text, although the raw HTML differs.
- Sections used: "Introduction", "Retrying and side effects", "Reducing client
  complexity", "Late arriving requests" and "Same client request ID, different
  intent".
- Exact quotes:

      An idempotent operation is one where a request can be retransmitted or
      retried with no additional side effects, a property that is very
      beneficial in distributed systems.

      A unique caller-provided client request identifier for idempotent
      operations meets this need.

      It also has the benefit of making that intent readily auditable because
      the unique identifier is present in logs like AWS CloudTrail.

      An important consideration is that the process that combines recording
      the idempotent token and all mutating operations related to servicing
      the request must meet the properties for an atomic, consistent,
      isolated, and durable (ACID) operation.

      This ensures that we avoid situations where we could potentially record
      the idempotent token and fail to create some resources or,
      alternatively, create the resources and fail to record the idempotent
      token.

      However, it’s impractical to retain that knowledge indefinitely.

      We have found that, for EC2 instances, it works to limit the time period
      to the lifetime of the resource, plus an interval after which it is
      reasonable to assume that any late arriving requests would either have
      arrived or would no longer be valid.

      In response to this situation, we return a validation error indicating
      a parameter mismatch between idempotent requests.

      To support this deep validation, we also store the parameters used to
      make the initial request along with the client request identifier.

      One possible response to this request is to return a ResourceAlreadyExists
      return code.

      This meets the basic tenets for idempotency because there is no side
      effect for retrying the call.

      However, this leads to uncertainty from the perspective of the caller
      because it’s not clear whether the resource was created as a result of
      this request or the resource was created as the result of an earlier
      request.

- Limits: one living engineering article with no version identifier. It
  describes ACID token recording and a validation error but does not define a
  wire status code, a tenant key scope, a universal retention duration or a
  support-inspection record. No AWS service was exercised.

### Stripe — Idempotent requests

- Source id: src.stripe-idempotency (existing).
- New record: read.stripe-idempotent-requests.2026-10-31.
- URL: https://docs.stripe.com/api/idempotent_requests
- Unit label: "Idempotent requests — Stripe API Reference"; unit type
  api-reference; access date 2026-10-31.
- Representation: HTTP 200, 1,413,122 bytes, HTTP Date
  2026-10-31T05:19:39Z, no Last-Modified and no ETag; x-content-timestamp
  2026-10-31T05:19:38Z; raw HTML SHA-256
  c1eb7968fc1fbecf85552f29f87b9dd1ec0648985e5ce42095172fd04f14d34d;
  canonical text SHA-256
  fdda1f88aa51ec91f7655939cba5063dd8e256f20e00933209172fb3ef5d49ef;
  10,453 characters, 1,741 words; the page displays API version 2026-10-28
  and publishes no page revision header. A second fetch returns the same
  canonical text with a slightly different raw byte count.
- Sections used: "Idempotent requests". The extractor also captured the
  adjacent "Include-dependent response values (API v2)" and "Metadata"
  sections; they are in the digest but were not used.
- Exact quotes:

      The API supports idempotency for safely retrying requests without
      accidentally performing the same operation twice.

      For API v1, Stripe saves the status code and body of the first request
      made with a given idempotency key after endpoint execution begins.

      Retries with the same key return the saved response, including 500
      errors.

      A client generates an idempotency key, which is a unique key that the
      server uses to recognize subsequent retries of the same request.

      Idempotency keys are up to 255 characters long.

      For API v1, you can remove keys from the system automatically after
      they’re at least 24 hours old.

      We generate a new request if a key is reused after the original is
      pruned.

      The idempotency layer compares incoming parameters to those of the
      original request and errors if they’re not the same to prevent
      accidental misuse.

      Don’t send idempotency keys in GET and DELETE requests because it has no
      effect. These requests are idempotent by definition.

- Limits: one living API-reference page; no page revision header and no
  benchmark. The 24-hour retention statement is API v1 behavior and permits
  automatic pruning; API v2 retries differ. The page does not define a
  support-inspection record, an in-progress state or a tenant key scope.

### Microsoft — Idempotent Consumer pattern

- Source id: src.microsoft-cloud-patterns (existing).
- Retained record: read.microsoft-idempotent-consumer.2026-10-30, revision
  f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34.
- New record: read.microsoft-idempotent-consumer.2026-10-31, same canonical
  text revision.
- URL:
  https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer
- Unit label: "Idempotent Consumer pattern — Azure Architecture Center"; unit
  type pattern-page; access date 2026-10-31.
- Representation: HTTP 200, 68,421 bytes, HTTP Date 2026-10-31T05:19:39Z,
  Last-Modified 2026-10-23T05:05:51Z, ETag
  "FvRm8G7SwWJn7zIg7zOkjxLCYQU="; raw HTML SHA-256
  75f287667327aad7eb0d641195e7b5a05b1c0b3ddb0882c8b3dec8ef73fa9207;
  canonical text SHA-256
  f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34;
  18,747 characters, 2,820 words; no published version identifier. A second
  fetch is byte-identical.
- Sections used: "Choose a stable deduplication key", "Commit the processed
  key and the side effects atomically", "Guard against concurrent duplicates",
  "Handle side effects that can't join the transaction" and "Problems and
  considerations".
- Exact quotes:

      The deduplication key must uniquely and consistently identify the
      logical message across every redelivery.

      Use either a producer-assigned message identifier or a business-level
      idempotency key that identifies the specific logical operation, not a
      shared correlation context that several messages can carry.

      If the consumers share a deduplication store, key the records on a
      composite of the consumer identity and the message identity.

      Avoid this failure window by writing the deduplication marker and the
      business side effects in the same transaction.

      If a consumer commits both operations together or not at all, upon
      redelivery it either finds the marker and skips the message, or finds
      no marker because the transaction didn't complete and safely
      reprocesses the message.

      Use a uniqueness constraint on the deduplication key such that two
      transactions can attempt to insert a key, but only one can succeed.

      Use an atomic conditional write, such as an insert that fails on
      conflict or a set-if-absent operation, to make claiming the key a single
      atomic step.

      This approach makes the database the single arbiter of the conflict.

      Record the key with an in-progress state, and then perform the external
      action.

      Update the record to completed and store the outcome.

      An in-progress record signals that a previous attempt might be partially
      completed or is being processed by another consumer.

      The consumer should reconcile stale records or route unresolved cases
      for intervention before acknowledging redelivery.

      Retain each record at least as long as the broker can still redeliver
      the original message.

      Set a time-to-live on deduplication records that exceeds this window,
      so that a late redelivery still finds its marker.

      Deleting records too early reopens the window for duplicates.

      Deduplication removes duplicates, but doesn't guarantee order.

      Prefer naturally idempotent operations.

      Some operations are inherently idempotent and don't need deduplication
      bookkeeping.

      An upsert keyed on a business identifier, a write that sets an absolute
      value rather than an increment, or an HTTP PUT to a resource identifier
      produce the same results whether they run once or many times.

- Limits: one living Microsoft Learn pattern page with no published version
  identifier. It is consumer-side guidance; it does not define an HTTP
  Idempotency-Key header, a complete repair algorithm, a post-expiry policy,
  tenant scoping or a specific ordering protocol. No consumer, store or
  redelivery was exercised.

## Book edits

### Owner page

- Frontmatter: only updated_at moves from 2026-10-20 to 2026-10-31.
  evidence_scope, content_review, source_inspection_date and
  content_verified_at are unchanged. The new records are supporting
  bindings, not page-level evidence-scope ids.
- The section "### Idempotency Key" stays at line 104. The page grows from
  119 to 213 lines.
- Mechanism: keeps the existing owner-unit sentence and adds IETF key
  ownership, uniqueness, expiry, fingerprint and lifecycle quotes; AWS
  client-request-identifier and audit quotes; the Stripe 24-hour retention
  sentence; and the Azure stable-key and composite-identity sentences. Tycho
  labels the one-contract rule, tenant-scope warning and retention-as-product
  decision as synthesis.
- Invariant: keeps the existing owner-unit sentence and adds the AWS ACID
  quote and the Azure same-transaction quote. It records that draft-08 does
  not require atomic commit and labels the effect/record rule and the
  changed-fingerprint rule as Tycho.
- Failure/recovery: keeps the existing owner-unit sentence and adds the IETF
  400/422/409 separation, the AWS parameter-mismatch validation error and
  parameter storage, the Stripe saved-response quote and the Azure
  in-progress/completed and reconcile sentences. Tycho labels the
  inspectable-record fields and the distinction among expired, in-progress
  and fingerprint-mismatch states.
- Alternative: keeps the existing owner-unit sentence and adds the Azure
  uniqueness-constraint, conditional-write and single-arbiter sentences; the
  IETF method-idempotence sentence; the Stripe GET/DELETE sentence; and the
  AWS ResourceAlreadyExists caveat. Tycho labels the choice and reversal rule.
- Source boundary lists the four units, the record revisions and the
  proposed records. It states that the retained draft-07 record is
  historical.
- Raw SHA-256:
  f16c7bbe42836d50d20943dd394c1af7b175e3e3b1dcfa66cf465b6116e5435b.
- Historical-view SHA-256:
  c4444edcaf755891989947dd25a97382133709e6ceb7affe04cfdf6a4d99cd2e.
- Base raw SHA-256:
  9619f8aa76d086e91dcc2b82f488813b13631ee30130167ec80293fea49c191b;
  base historical-view SHA-256:
  7d2db52b99c4e2cdd88ceec2eb5cb6df19ed042b88e750b52850595ae7def1f1.

### V11/C04 inline card

- evidence_scope.source_ids adds src.aws-idempotency and
  src.stripe-idempotency; src.ietf-idempotency-key and
  src.microsoft-cloud-patterns were already declared.
- content_review.reviewed_at, updated_at and source_inspection_date move to
  2026-10-31; the reviewer remains "Automated authoring agent". This is a
  self-check, not independent review. The notes field now says the card
  binds four public units.
- Good-fit conditions add a published key scope/fingerprint/retention
  contract, atomic outcome-record plus effect commit and a support-visible
  record.
- Hard contraindications add a key store with no expiry or cleanup owner.
- Competing alternative adds a compare-and-set and the reversal conditions on
  payload shape, caller population and retention cost. This intentionally
  changes the card text and forces the owner-units-alternative check until
  the metadata below is applied.
- Failure and recovery adds the IETF 400/422/409 separation, the Stripe
  saved response, the AWS parameter validation and the Azure
  in-progress/completed record with the reconcile quote; Tycho guidance
  distinguishes in-progress from expired and keeps the record for the retry
  window.
- Technical owner line now names source-bound key ownership, fingerprint,
  atomic commit, conflict response and retention; the four-part contract
  remains Tycho.
- Sources lists the IETF draft-07 historical record, the draft-08 proposed
  record, the AWS and Stripe proposed records and the Azure retained plus
  proposed records.
- "### Idempotency Key" moves from 296 to 298. The page grows from 458 to 478
  lines.
- Raw SHA-256:
  74ce752b5aa8baac0178dd6b7ba896db3ad8aee3bcff748b4227c762efc46c28.
- Historical-view SHA-256:
  18a9c4a7a1c811f2a27f88e35081b619e05aa15b395c6c35fd96d40d9ee8413d.
- Base raw SHA-256:
  cb23d5a0bb983c08f59c5bfd21b0f5cabd5159e6f04bec44e29e073a6e84f63b;
  base historical-view SHA-256:
  bb815eae6023478b0b8b8bc094de08f8224eda331796691f8e21d2191ece1fff.

No other book file is changed by this lane.

## Metadata needs (integrator)

The following changes are not in the lane commit. They were not applied to
any shared JSON file. They are the minimum metadata patch needed to make the
lane consistent; the counts and hashes below are derived from the worktree
state.

### Source register

Set updated to 2026-10-31; the source count stays 305.

- src.ietf-idempotency-key: change url and resolved_url to
  https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-08.txt;
  set version to "draft-ietf-httpapi-idempotency-key-header-08, 2026-10-22";
  set access_checked and content_verified to 2026-10-31; set reading_status to
  full-public-page-inspected; set verification_scope to "Complete public text
  accessed 2026-10-31; sections 1-2.7 read for this lane; sections 3-7 and
  the appendix were not read." Keep the IETF Internet-Draft license note.
- src.aws-idempotency: set version to "Living engineering article, accessed
  2026-10-31; 456,055-byte HTML; raw HTML SHA-256
  f1a8595955fe0900386eb9a1191184ee9e60fd117a2e7f7219ef6a5d1b2d8139;
  canonical text SHA-256
  c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac;
  HTTP Date 2026-10-31T05:19:39Z; Last-Modified 2026-10-27T00:27:38Z; no
  ETag; no published version identifier."; set access_checked and
  content_verified to 2026-10-31; set reading_status to
  full-public-page-inspected; set verification_scope to the five sections
  named above and exclude linked pages, code and images; set observed_title
  to "Making retries safe with idempotent APIs". Replace the placeholder
  license note with "Public AWS Builders' Library article; cite short
  excerpts and paraphrase; do not mirror."
- src.stripe-idempotency: set version to "Living API reference, accessed
  2026-10-31; 1,413,122-byte HTML; raw HTML SHA-256
  c1eb7968fc1fbecf85552f29f87b9dd1ec0648985e5ce42095172fd04f14d34d;
  canonical text SHA-256
  fdda1f88aa51ec91f7655939cba5063dd8e256f20e00933209172fb3ef5d49ef;
  HTTP Date 2026-10-31T05:19:39Z; no Last-Modified and no ETag; displays API
  version 2026-10-28; no page revision header."; set access_checked and
  content_verified to 2026-10-31; set reading_status to
  full-public-page-inspected; set verification_scope to the
  "Idempotent requests" section and exclude the adjacent API v2 and metadata
  sections, linked pages and code; set observed_title to "Idempotent
  requests | Stripe API Reference". Replace the placeholder license note with
  "Public Stripe API documentation; cite short excerpts and paraphrase; do
  not mirror."
- src.microsoft-cloud-patterns: append to version the 2026-10-31
  Idempotent Consumer facts: 68,421-byte HTML, raw HTML SHA-256
  75f287667327aad7eb0d641195e7b5a05b1c0b3ddb0882c8b3dec8ef73fa9207,
  canonical text SHA-256
  f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34,
  HTTP Date 2026-10-31T05:19:39Z, Last-Modified 2026-10-23T05:05:51Z, ETag
  "FvRm8G7SwWJn7zIg7zOkjxLCYQU=", no published version; a second fetch is
  byte-identical. Append to verification_scope that the Idempotent Consumer
  page was re-read on 2026-10-31 for key stability, conditional-write and
  natural-idempotency claims. Keep access_checked and content_verified at
  2026-10-31.
- Regenerate sources/CATALOG.md with scripts/source_catalog.py.

### Reading ledger

Add four records; records move from 214 to 218. Set each reviewer to
"Automated authoring agent" and status to read.

1. read.ietf-idempotency-key-08.2026-10-31 — source
   src.ietf-idempotency-key; label "The Idempotency-Key HTTP Header Field —
   IETF Internet-Draft 08"; type specification; URL the draft-08 URL;
   sections equal to the twelve sections listed in the source binding;
   content_sha256 25dcfa45f2fcbe3d8bc00e2c8b2bf396dfe1bbcea991a535f2fedce3728ed4a3;
   access method records 25,624 bytes, HTTP Date 2026-10-31T05:19:38Z,
   Last-Modified 2026-10-22T18:28:54Z, ETag "6ada55e6-6418", expiry
   2027-04-25 and a byte-identical second fetch. Claims are limited to key
   uniqueness, ownership, expiry, fingerprint, lifecycle, conflict statuses
   and the method-idempotence contrast. Limitations: Internet-Draft, not an
   RFC; no atomic outcome-record rule; no support-visible record; Retry text
   open for discussion.
2. read.aws-idempotency.2026-10-31 — source src.aws-idempotency; label
   "Making retries safe with idempotent APIs — Amazon Builders' Library";
   type engineering-article; URL the article URL; sections equal to the five
   named sections; content_sha256
   c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac;
   access method records the raw and canonical revisions, HTTP Date,
   Last-Modified, no ETag, and the canonical-identical second fetch. Claims
   are limited to caller-provided request identity, auditability, ACID
   token/effect recording, retention bounded by resource lifetime and
   late-arrival interval, parameter mismatch and the ResourceAlreadyExists
   trade-off. Limitations: no wire status code, universal retention duration
   or tested implementation.
3. read.stripe-idempotent-requests.2026-10-31 — source
   src.stripe-idempotency; label "Idempotent requests — Stripe API
   Reference"; type api-reference; URL the Stripe URL; sections ["Idempotent
   requests"]; content_sha256
   fdda1f88aa51ec91f7655939cba5063dd8e256f20e00933209172fb3ef5d49ef;
   access method records the raw and canonical revisions, HTTP Date,
   x-content-timestamp, no Last-Modified, no ETag, displayed API version
   2026-10-28 and the canonical-identical second fetch. Claims are limited
   to saved response on retry, client-generated key, 255-character limit,
   API v1 24-hour pruning, parameter comparison and natural method
   idempotence. Limitations: API v1 behavior, living page, no support record
   or in-progress state.
4. read.microsoft-idempotent-consumer.2026-10-31 — source
   src.microsoft-cloud-patterns; label "Idempotent Consumer pattern — Azure
   Architecture Center"; type pattern-page; URL the Microsoft URL; sections
   equal to the five named sections; content_sha256
   f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34;
   access method records the raw and canonical revisions, HTTP Date,
   Last-Modified, ETag and the byte-identical second fetch. Claims add stable
   key identity, producer/business key choice, composite consumer-plus-message
   key, conditional write, single arbiter and natural idempotency to the
   retained 2026-10-30 claims. Limitations: no complete repair algorithm,
   post-expiry policy, tenant scoping or ordering protocol.

Keep read.batch2-ietf.2026-10-21 and
read.microsoft-idempotent-consumer.2026-10-30 unchanged as historical
records.

### Source plan

Update the tycho.pattern.idempotency-key entry:

1. Replace the existing IETF unit URL with the draft-08 URL; change the unit
   label to "The Idempotency-Key HTTP Header Field — IETF Internet-Draft 08";
   set sections to the twelve sections above; set read_record_id to
   read.ietf-idempotency-key-08.2026-10-31; keep status read and
   blocked_reason null.
2. Append AWS, label "Making retries safe with idempotent APIs — Amazon
   Builders' Library", type engineering-article, URL the article URL, record
   read.aws-idempotency.2026-10-31, sections equal to that record's
   sections_read.
3. Append Stripe, label "Idempotent requests — Stripe API Reference", type
   api-reference, URL the Stripe URL, record
   read.stripe-idempotent-requests.2026-10-31, sections ["Idempotent
   requests"].
4. Append Microsoft, label "Idempotent Consumer pattern — Azure Architecture
   Center", type pattern-page, URL the Microsoft URL, record
   read.microsoft-idempotent-consumer.2026-10-31, sections equal to that
   record's sections_read.

Set every unit status to read and blocked_reason to null. Replace the entry
notes with "All four technical dimensions bound 2026-10-31 to IETF draft-08,
AWS Builders' Library, Stripe and Azure Architecture Center; the key
ownership, atomic-commit, conflict-response and alternative rules remain
Tycho."

Summary: required_units 260 -> 263; read_units 259 -> 262; planned_units
stays 0; blocked_units stays 1; ledger_records 214 -> 218. Recompute
registry_sha256 after saving the registry and refresh route_index_snapshot
from the rebuilt route index.

### Pattern registry

For tycho.pattern.idempotency-key:

- Set technical_owner.state to partial-bounded (from partial). Keep
  atlas_owner.state at partial-bounded.
- Set coverage.technical and coverage.overall to partial-bounded; keep
  coverage.decision at partial-bounded.
- Replace the single IETF source unit with the four units above, all with
  status read; unit labels must equal the source-plan labels.
- Replace notes with "All four technical dimensions bound 2026-10-31 to IETF
  draft-08, AWS Builders' Library, Stripe and Azure Architecture Center; the
  key ownership, atomic-commit, conflict-response and alternative rules
  remain Tycho. Coverage partial-bounded; no promotion or acceptance."
- Keep review_status self-checked. Set the registry updated_at to 2026-10-31.

### Owner units

Entry tycho.pattern.idempotency-key:

- Keep owner.line at 104, the heading, document id, unit kind and unit terms
  unchanged. The terms remain present in the body.
- Mechanism: set state supported; keep the existing quote ("An idempotency
  key belongs to the operation owner, who defines its scope, fingerprint
  inputs and retention period."). Reason: IETF draft-08 defines uniqueness
  ownership, non-reuse, expiry publication, fingerprint input and lifecycle
  responsibility; AWS, Stripe and Azure give API-level key scope and
  retention examples; the one-contract and tenant-scope rules are Tycho.
  Primary binding src.ietf-idempotency-key, record
  read.ietf-idempotency-key-08.2026-10-31, section "Uniqueness of Idempotency
  Key", quote "Uniqueness of the key MUST be defined by the resource owner
  and MUST be implemented by the clients of the resource.", revision
  25dcfa45f2fcbe3d8bc00e2c8b2bf396dfe1bbcea991a535f2fedce3728ed4a3.
  Supporting bindings:
  - IETF, same record, section "Idempotency Key Validity and Expiry", quote
    "The resource SHOULD define such expiration policy and publish it in the
    documentation.", same revision.
  - AWS, record read.aws-idempotency.2026-10-31, section "Reducing client
    complexity", quote "A unique caller-provided client request identifier
    for idempotent operations meets this need.", revision
    c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac.
  - Stripe, record read.stripe-idempotent-requests.2026-10-31, section
    "Idempotent requests", quote "For API v1, you can remove keys from the
    system automatically after they’re at least 24 hours old.", revision
    fdda1f88aa51ec91f7655939cba5063dd8e256f20e00933209172fb3ef5d49ef.
  - Microsoft, record read.microsoft-idempotent-consumer.2026-10-31, section
    "Choose a stable deduplication key", quote "The deduplication key must
    uniquely and consistently identify the logical message across every
    redelivery.", revision
    f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34.
- Invariant: set state supported; keep the existing quote ("The outcome
  record and business effect must commit together; a later separate write
  leaves a window for duplicate execution."). Reason: AWS requires ACID
  recording of the idempotent token with all mutating operations; Azure
  requires the deduplication marker and business side effects in one
  transaction; IETF draft-08 states a weaker response-consistency rule but
  not atomic commit; the full rule is Tycho. Primary binding
  src.aws-idempotency, record read.aws-idempotency.2026-10-31, section
  "Reducing client complexity", quote "An important consideration is that
  the process that combines recording the idempotent token and all mutating
  operations related to servicing the request must meet the properties for
  an atomic, consistent, isolated, and durable (ACID) operation.", revision
  c18401ac35cb5d8e7e97a4d53ff3f5a7280a53097e000d50bc525a758fbbcdac.
  Supporting bindings:
  - Microsoft, record read.microsoft-idempotent-consumer.2026-10-31, section
    "Commit the processed key and the side effects atomically", quote "Avoid
    this failure window by writing the deduplication marker and the business
    side effects in the same transaction.", revision f50de2c4....
  - IETF, record read.ietf-idempotency-key-08.2026-10-31, section
    "Idempotency Enforcement", quote "The resource SHOULD respond with a
    response consistent with the request being completed according to the
    user's intent.", revision 25dcfa45....
- Failure/recovery: set state supported; keep the existing quote ("The owner
  also names the conflict response and the record a support engineer may
  inspect."). Reason: IETF draft-08 separates 400, 422 and 409 and requires a
  problem description; AWS stores the initial parameters and returns a
  validation error on mismatch; Stripe returns the saved response; Azure
  keeps in-progress/completed records and says to reconcile stale records;
  the inspectable-record fields are Tycho. Primary binding
  src.ietf-idempotency-key, record read.ietf-idempotency-key-08.2026-10-31,
  section "Error Handling", quote "If the request is retried, while the
  original request is still being processed, the resource SHOULD reply with
  an HTTP 409 status code with body containing problem description.",
  revision 25dcfa45....
  Supporting bindings:
  - IETF, same record and section, quote "If there is an attempt to reuse an
    idempotency key with a different request payload, the resource SHOULD
    reply with an HTTP 422 status code with body containing a link pointing
    to relevant documentation.", revision 25dcfa45....
  - AWS, record read.aws-idempotency.2026-10-31, section "Same client
    request ID, different intent", quote "In response to this situation, we
    return a validation error indicating a parameter mismatch between
    idempotent requests.", revision c18401ac....
  - Stripe, record read.stripe-idempotent-requests.2026-10-31, section
    "Idempotent requests", quote "Retries with the same key return the saved
    response, including 500 errors.", revision fdda1f88....
  - Microsoft, record read.microsoft-idempotent-consumer.2026-10-31, section
    "Handle side effects that can't join the transaction", quote "Record the
    key with an in-progress state, and then perform the external action.
    Update the record to completed and store the outcome.", revision
    f50de2c4....
- Alternative: set state supported; keep the existing quote ("Some effects
  can rely on a uniqueness rule, a compare-and-set or one writer instead of a
  key store."). Reason: Azure binds a uniqueness constraint, an atomic
  conditional write and a single database arbiter; IETF draft-08 separates
  naturally idempotent methods; Stripe says GET and DELETE are idempotent by
  definition; AWS shows the ResourceAlreadyExists trade-off; the choice and
  reversal rule is Tycho. Primary binding src.microsoft-cloud-patterns,
  record read.microsoft-idempotent-consumer.2026-10-31, section "Guard
  against concurrent duplicates", quote "Use a uniqueness constraint on the
  deduplication key such that two transactions can attempt to insert a key,
  but only one can succeed.", revision f50de2c4....
  Supporting bindings:
  - Microsoft, same record and section, quote "Use an atomic conditional
    write, such as an insert that fails on conflict or a set-if-absent
    operation, to make claiming the key a single atomic step.", revision
    f50de2c4....
  - Microsoft, same record and section, quote "This approach makes the
    database the single arbiter of the conflict.", revision f50de2c4....
  - IETF, record read.ietf-idempotency-key-08.2026-10-31, section
    "Introduction", quote "the methods OPTIONS, HEAD, GET, PUT and DELETE
    are idempotent while methods POST and PATCH are not.", revision
    25dcfa45....
  - Stripe, record read.stripe-idempotent-requests.2026-10-31, section
    "Idempotent requests", quote "Don’t send idempotency keys in GET and
    DELETE requests because it has no effect. These requests are idempotent
    by definition.", revision fdda1f88....
- Set technical_coverage to partial-bounded. Set notes to the registry notes
  above.
- Set decision_evidence.competing_alternative to the new card text: "Natural
  idempotency, a uniqueness constraint, a compare-and-set or one writer.
  Reverse when key storage and fingerprinting cost exceed retry risk, or
  when payload shape, caller population or retention cost changes."
- source_support: primary source src.ietf-idempotency-key, record
  read.ietf-idempotency-key-08.2026-10-31, unit_type specification, status
  read, card_citation true. Auxiliary entries for src.aws-idempotency
  (read.aws-idempotency.2026-10-31, c18401ac...), src.stripe-idempotency
  (read.stripe-idempotent-requests.2026-10-31, fdda1f88...) and
  src.microsoft-cloud-patterns
  (read.microsoft-idempotent-consumer.2026-10-31, f50de2c4...).
- Summary counters: mechanism_supported 112 -> 113; invariant_supported
  77 -> 78; failure_recovery_supported 71 -> 72; alternative_supported
  76 -> 77; technical_partial_bounded 15 -> 16; technical_partial 71 -> 70.
  No decision counter changes.

### Card batches

For tycho.pattern.idempotency-key, change ledger_record to
read.ietf-idempotency-key-08.2026-10-31. Keep owner_state linked and the
owner path and anchor unchanged. The card remains inline; do not add a
card_path.

### Content revisions

Add one issue-540 revision with authorized_at 2026-10-31 and authorization
"B46 Idempotency Key four-dimension source binding; no promotion or owner
acceptance." Use these historical-view hashes:

- Owner path, previous (baseline):
  7d2db52b99c4e2cdd88ceec2eb5cb6df19ed042b88e750b52850595ae7def1f1;
  current:
  c4444edcaf755891989947dd25a97382133709e6ceb7affe04cfdf6a4d99cd2e.
- Card path, previous (baseline):
  bb815eae6023478b0b8b8bc094de08f8224eda331796691f8e21d2191ece1fff;
  current:
  18a9c4a7a1c811f2a27f88e35081b619e05aa15b395c6c35fd96d40d9ee8413d.
- Leave source_blocks, enrichment_documents, enrichment_additions and
  enrichment_baselines empty.

Raw file hashes for reference:
f16c7bbe42836d50d20943dd394c1af7b175e3e3b1dcfa66cf465b6116e5435b
(owner) and
74ce752b5aa8baac0178dd6b7ba896db3ad8aee3bcff748b4227c762efc46c28
(card).

### Atlas manifest, inventory and derived artifacts

- edition/atlas-manifest.json: set the V11/C04 document sha256 to
  74ce752b5aa8baac0178dd6b7ba896db3ad8aee3bcff748b4227c762efc46c28 and
  registry_sha256 to the new registry file hash after the registry edit. No
  atlas route changes.
- edition/inventory.json: regenerate so the owner page hash is f16c7bbe...
  and the card hash is 74ce752b...; use
  python3 scripts/validate_edition.py --write-inventory before validating.
- Refresh route index, page census, coverage/reverse map, phase 4,
  delivery-evidence counts, semantic audit, edition inventory and the source
  catalogue once at batch end. Reconcile the sufficient-candidate and
  sufficient-ready-plan files from the new 4/4 state. The 2026-10-22
  sufficient review record carries the old owner page hash; do not update
  that record without a fresh review.
- No promotion hash binds either changed page, so no promotion rebind is
  required.

### Preflight

The preflight checks cannot pass in this lane for two structural reasons: the
owner-unit dimensions are still recorded as partial because no shared JSON is
in the lane, and the card remains inline so it has no card_path. After the
metadata above is applied, only the inline-card card_path check should
remain. Do not convert the card to a dedicated page in this lane.

## Validation

Checker output in the lane worktree after the two book edits:

    PASS: V11 prose <=100; 145 exact owner-link exceptions
    PASS: configured lexical boundary checks; independent-origin review still
    required.

Quote audit: 52 quoted fragments across four public units were checked as
whitespace-normalized substrings of the fetched representations. Zero
missing. The audit used the canonical text extraction for HTML pages and the
raw text for the IETF draft, not a search result.

Targeted validator results with the book edits only, in the lane worktree:

- python3 scripts/validate_pattern_cards.py — PASS; 145 entries.
- python3 scripts/validate_book_metadata.py — exit 0; 500 documents.
- python3 scripts/validate_pattern_sources.py — PASS; source plan 145
  entries, 259 read, 214 ledger records.
- python3 scripts/validate_pattern_registry.py — PASS; 145 entries.
- python3 scripts/validate_pattern_coverage.py — PASS; 145 entries.
- python3 scripts/validate_decomposition.py — exit 0.
- python3 scripts/validate_enrichment.py — exit 0.
- python3 scripts/validate_pattern_owner_units.py — FAIL
  owner-units-alternative because the existing metadata still carries the old
  card alternative. This is metadata work, not a content defect.
- python3 scripts/validate_pattern_atlas.py — FAIL atlas-document-sha;
  expected until the atlas manifest is updated.
- python3 scripts/validate_directory_migration.py — FAIL
  directory-baseline-payload-drift; expected until the content revision is
  applied.
- python3 scripts/validate_edition.py — FAIL
  directory-baseline-payload-drift; expected for the same reason.
- python3 scripts/preflight_sufficient.py --pattern
  tycho.pattern.idempotency-key — FAIL on the four partial states and the
  missing inline card_path; expected until the metadata patch above.
- Full unit suite was not run; batch-end tests remain with the integrator.

## Limits

The binding uses four public units. They describe key ownership, uniqueness,
fingerprint input, expiry publication, atomic marker-plus-effect commit,
saved-response replay, conflict statuses, parameter validation, uniqueness
and conditional-write alternatives, in-progress/completed records and
retention. None observes this page's service, executes a retry race,
reproduces a lost response, measures a retention window or proves that one
implementation is correct.

The four dimensions are marked supported because the page separates the
source-supported statements from the Tycho synthesis: the one-contract rule,
tenant-scope warning, retention-as-product decision, effect/record rule,
changed-fingerprint rule, inspectable-record fields, state distinction,
alternative choice and reversal rule are Tycho. A reviewer that requires
every word of a dimension quote to be source-quoted should treat the
dimensions as partial.

Draft-08 is an Internet-Draft, not an RFC, and expires on 2027-04-25. Its
Retry text is weaker than draft-07 and Appendix A says it is still open for
discussion. The Stripe page is living API v1 documentation with no page
revision header. The AWS article is narrative guidance with no published
version. The Azure page is consumer-side pattern guidance with no complete
repair algorithm, post-expiry policy, tenant scoping or ordering protocol.

The Microsoft canonical digest includes served navigation chrome because the
repository extractor falls back to the full page text. The Stripe digest
includes two adjacent API-reference sections that were not used. These are
binding revisions for the 2026-10-31 representation, not published editions.

No promotion, owner acceptance, CI, independent review or merge permission is
claimed. The book/atlas independent review gate applies.

## Review needs

- Request a fresh external review under the book/atlas gate. The reviewer
  should check quote-to-claim fit for all four dimensions, the Tycho labels
  for the ownership, commit, record and choice rules, the four revisions, the
  card wording, the shifted heading lines and the metadata patch.
- The reviewer must use read-only repository access and must not write,
  commit, open a pull request or change configuration, and must not run
  tests.
- No existing promotion binds either changed page; confirm that before
  integration.

## Commit scope

The lane commit contains this note and the two book files only:

- book/volumes/v04-distributed-coordination-and-events/
  c04-retries-idempotency-and-duplicate-effects/
  retries-idempotency-and-ambiguous-effects.md;
- book/volumes/v11-pattern-atlas/c04-consistency-events/README.md.

No shared JSON, promotion, test or generated file is in the lane commit.
