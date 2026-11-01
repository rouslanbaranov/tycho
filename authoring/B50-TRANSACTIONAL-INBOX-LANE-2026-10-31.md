# B50 - Transactional Inbox four-dimension source binding lane

Status: lane-local book edit, self-checked on 2026-10-31. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry was 1/4 at the parent HEAD: invariant was supported; mechanism,
failure/recovery and alternative were partial. This lane binds all four
dimensions to public Microsoft, Kafka, PostgreSQL and Debezium units and
upgrades the entry to partial-bounded. Preflight still requires the metadata
patch and card registration below. The lane commit edits only the two book
files and this note.

## Lane coordinates

- Parent HEAD: `a888c887` ("docs: pin hand-off to Expand-and-Contract
  promotion").
- Branch: `b50-inbox`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b50-inbox`.
- Scope: the V04/C05 owner section `## 3. Inbox and consumer-local atomicity`
  and the inline V11/C04 card `### Transactional Inbox`.
- The card remains inline in the V11/C04 `README.md`; the integrator owns the
  split decision and the `card_path` registration.
- Single-entry lane; no other entry, shared owner page, promotion or generated
  file is changed.

## Candidate evaluation

- Microsoft Idempotent Consumer:
  `https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer`.
  Existing record `read.microsoft-idempotent-consumer.2026-10-31`
  (`src.microsoft-cloud-patterns`), canonical
  `f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`. It states
  the Inbox name, the atomic marker-plus-effect rule, store-level uniqueness,
  the consumer-scoped composite key, both crash-window directions, the
  in-progress/completed repair route, retention/TTL and the natural-idempotency
  preference. Primary source for mechanism, invariant and failure/recovery.
- Microsoft transactional-outbox guide:
  https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos
  New unit on the same admitted source. It states the producer-side
  same-transaction rule, the outbox table, change-feed reprocessing duplicates,
  duplicate detection and TTL retention. It is a Cosmos DB implementation
  article, not a generic inbox pattern.
- Apache Kafka 4.1 Design: `https://kafka.apache.org/41/design/design/`.
  Source `src.kafka-design` is admitted. The existing
  `read.kafka-design.2026-10-30` record covers replication and consumer position
  but not the delivery-semantics sections, so a new record is required. The page
  states the exactly-once definition and scope, the consumer position stored as
  a message in the same transaction as output records, and the at-least-once
  default.
- PostgreSQL 18 SELECT:
  `https://www.postgresql.org/docs/current/sql-select.html`. Source
  `src.postgresql` is admitted. New unit for "The Locking Clause": SKIP LOCKED
  skips rows that cannot be locked immediately, and the page warns that this
  gives an inconsistent view and is only suitable for queue-like contention.
  It is not a deduplication mechanism.
- Debezium Outbox Event Router:
  `https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html`.
  Source `src.debezium-outbox` is admitted. The existing
  `read.debezium-outbox.2026-10-31` record covers routing and the event ID but
  not the opening claim that an outbox avoids state/event inconsistency, so a
  new binding record is required.
- Rejected or bounded: the Azure Architecture Center
  `/patterns/transactional-outbox` path returned 404 on 2026-10-31; no AWS
  replacement was used. No new source admission is requested.

## Source units and revisions

All fetches were public HTTPS GETs on 2026-10-31. Canonical text was extracted
with `scripts/source_content_hash.py`; raw HTML SHA-256 is also recorded.

- `src.microsoft-cloud-patterns` - Idempotent Consumer pattern - Azure
  Architecture Center. Canonical
  `f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34`; current
  raw HTML
  `f335c4291771cc0421741e45761ca7810c11c980ddf9c163ae2fa91586e7594a`; HTTP
  Date 2026-10-31T14:38:37Z; Last-Modified 2026-10-23T05:05:51Z; ETag
  `"FvRm8G7SwWJn7zIg7zOkjxLCYQU="`. Canonical text is unchanged from the
  existing 2026-10-31 record; only the page shell differs.
- `src.microsoft-cloud-patterns` - Implement the Transactional Outbox pattern
  by using Azure Cosmos DB. Canonical
  `6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e`; raw
  HTML `7d2b0299a683239c95f44571f862484035c71c89aa6375627a1c5f768298a048`;
  84,527 bytes; HTTP Date 2026-10-31T14:38:37Z; Last-Modified
  2026-10-15T17:37:26Z; ETag `"w6OVhWKvL9oyg8jLkO69fLwvTMY="`. Sections read:
  "Solution" and "Error handling".
- `src.kafka-design` - Design - Apache Kafka 4.1 documentation (exactly-once
  and offsets). Canonical
  `674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b`; raw
  HTML `d01981797402d75cada10599d586b753d02f8a9deb08d658a0e07758dedadfb7`;
  143,123 bytes; HTTP Date 2026-10-31T14:38:37Z; Last-Modified
  2026-10-28T19:19:52Z; ETag `"22f13-65eeb7291ff35"`. Sections read: "Consumer
  Position", "Message Delivery Semantics" and "Using Transactions".
- `src.postgresql` - SELECT - The Locking Clause (PostgreSQL 18
  documentation). Canonical
  `464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94`; raw
  HTML `876b2978f26650506af5fb36cf99135a15c8c68b4d979c3a784ee44f84d1e6fc`;
  118,042 bytes; HTTP Date 2026-10-31T12:36:44Z; no Last-Modified or ETag
  served. Section read: "The Locking Clause".
- `src.debezium-outbox` - Outbox Event Router - Debezium documentation
  (2026-10-31 binding). Canonical
  `26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e`; raw
  HTML `382f0bd0cd99f5c8206f9ba0381f3ec71f12ffe373154d351baa8823fd11ad53`;
  90,537 bytes; HTTP Date 2026-10-31T14:38:38Z; Last-Modified
  2026-10-31T04:20:50Z. Sections read: "Outbox Event Router" and "Basic outbox
  table".

## Dimension mapping

- **Mechanism.** Primary: Microsoft Inbox, "Commit the processed key and the
  side effects atomically" (Q1). Supporting: the same section names the
  transactional variant the Inbox pattern (Q2); the Microsoft outbox guide
  applies the same transaction to the business object and its events (Q3).
- **Invariant.** Primary: the existing microservices.io record
  `read.batch2-idempotent-consumer.2026-10-21`, section "Solution". Supporting:
  Microsoft uniqueness (Q4) and consumer-scoped composite key (Q5); Kafka
  position-as-message and offset transaction (Q6), the exactly-once definition
  (Q7) and the external-system cooperation limit (Q9).
- **Failure and recovery.** Primary: Microsoft Inbox check-then-process crash
  window (Q10). Supporting: the in-progress/completed route (Q11),
  reconciliation before acknowledgement (Q12), retention (Q13), the Microsoft
  outbox reprocessing duplicate (Q14) and Kafka's at-least-once default (Q8).
- **Alternative.** Primary: Debezium's producer-side outbox (Q15). Supporting:
  the Debezium event ID for duplicate removal (Q16), PostgreSQL SKIP LOCKED and
  its inconsistent-view warning (Q17), Microsoft's natural-idempotency
  preference (Q18) and the Microsoft outbox-table mechanism (Q19).

## Selected exact quotes

- Q1, Microsoft Inbox, "Commit the processed key and the side effects
  atomically": "Avoid this failure window by writing the deduplication marker
  and the business side effects in the same transaction."
- Q2, Microsoft Inbox, "Commit the processed key and the side effects
  atomically": "This transactional variant is the Inbox pattern".
- Q3, Microsoft outbox guide, "Solution": "When you save the business object
  and its events within the same database transaction, the system guarantees no
  data loss."
- Q4, Microsoft Inbox, "Guard against concurrent duplicates": "Use a
  uniqueness constraint on the deduplication key such that two transactions can
  attempt to insert a key, but only one can succeed."
- Q5, Microsoft Inbox, "Choose a stable deduplication key": "If the consumers
  share a deduplication store, key the records on a composite of the consumer
  identity and the message identity."
- Q6, Kafka Design, "Message Delivery Semantics": "The consumer's position is
  stored as a message in an internal topic, so we can write the offset to Kafka
  in the same transaction as the output topics receiving the processed data."
- Q7, Kafka Design, "Message Delivery Semantics": "Exactly once -Each message
  is processed once and only once."
- Q8, Kafka Design, "Message Delivery Semantics": "Otherwise, Kafka guarantees
  at-least-once delivery by default, and allows the user to implement
  at-most-once delivery by disabling retries on the producer and committing
  offsets in the consumer prior to processing a batch of messages."
- Q9, Kafka Design, "Message Delivery Semantics": "Exactly-once delivery for
  other destination systems generally requires cooperation with such systems".
- Q10, Microsoft Inbox, "Commit the processed key and the side effects
  atomically": "A check-then-process flow has a failure window. If a consumer
  processes a message and then records the key in a separate step, a crash
  between the two operations leaves the side effects applied but the key
  unrecorded, so the consumer reprocesses the next redelivery."
- Q11, Microsoft Inbox, "Handle side effects that can't join the transaction":
  "Record the key with an in-progress state, and then perform the external
  action. Update the record to completed and store the outcome."
- Q12, Microsoft Inbox, "Handle side effects that can't join the transaction":
  "The consumer should reconcile stale records or route unresolved cases for
  intervention before acknowledging redelivery."
- Q13, Microsoft Inbox, "Problems and considerations": "Retain each record at
  least as long as the broker can still redeliver the original message."
- Q14, Microsoft outbox guide, "Error handling": "When reprocessing occurs, the
  application might have already sent some messages to Service Bus, which
  normally creates duplicate message processing."
- Q15, Debezium Outbox Event Router, "Outbox Event Router": "The outbox pattern
  is a way to safely and reliably exchange data between multiple (micro)
  services."
- Q16, Debezium Outbox Event Router, "Basic outbox table": "Contains the unique
  ID of the event. In an outbox message, this value is a header. You can use
  this ID, for example, to remove duplicate messages."
- Q17, PostgreSQL SELECT, "The Locking Clause": "Skipping locked rows provides
  an inconsistent view of the data, so this is not suitable for general purpose
  work, but can be used to avoid lock contention with multiple consumers
  accessing a queue-like table."
- Q18, Microsoft Inbox, "Problems and considerations": "Prefer naturally
  idempotent operations."
- Q19, Microsoft outbox guide, "Solution": "This pattern saves events in a data
  store that's typically in an outbox table in your database before it pushes
  them to a message broker."

Typography: the sources use a curly apostrophe in "consumer's" and "service's",
and an en dash in the Kafka exactly-once line. The owner page and machine
bindings preserve those codepoints; the Q6/Q7 renderings above are ASCII
transcriptions for this note only.

## Book edits

- V04/C05 owner `inbox-atomicity.md`:
  - Frontmatter adds `src.microsoft-cloud-patterns`, `src.kafka-design`,
    `src.postgresql` and `src.debezium-outbox`; advances `reviewed_at`,
    `updated_at` and `source_inspection_date` to 2026-10-31; reviewer becomes
    "Automated authoring agent".
  - Adds source-check, invariant, failure/recovery and alternative paragraphs
    inside section 3, without a new heading, so the owner section remains
    contiguous for preflight. The local-authority reading, at-most-one-effect
    invariant, retry/reconcile/acknowledgement schedule and SKIP LOCKED limit
    are labelled Tycho.
  - Heading line 54; page 134 lines.
  - SHA-256: `3cc15e807db3cbf2290876e3e13d0155affda18c7cdae59162f8693d3bb413b5`.
- V11/C04 inline card `README.md`:
  - Frontmatter adds `src.kafka-design` and updates the evidence note.
  - "Failure and recovery" names the marker/effect crash window, the
    in-progress/completed record and reconciliation before acknowledgement, and
    labels retention/replay and separate-acknowledgement guidance Tycho.
  - "Sources" names the Microsoft Inbox and outbox records, the Kafka 4.1
    Design record, the PostgreSQL SELECT record and the Debezium record, with
    revisions; the four-dimension mapping and the SKIP LOCKED
    duplicate-suppression limit are labelled Tycho.
  - Card heading line 264; chapter 452 lines.
  - SHA-256: `43ececcb5a54063053e2477af06b4744d5b5e69a58aea563f09cc24585f0de6e`.
- No other book file, edition JSON, promotion or generated file is changed.

## Full ledger records (integrator)

The Microsoft Inbox record `read.microsoft-idempotent-consumer.2026-10-31`
already exists and is reused unchanged. Append these four records:

```json
[
  {
    "id": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
    "source_id": "src.microsoft-cloud-patterns",
    "unit_url": "https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos",
    "unit_label": "Implement the Transactional Outbox pattern by using Azure Cosmos DB",
    "unit_type": "article",
    "access_date": "2026-10-31",
    "access_method": "public HTTP fetch on 2026-10-31; served text/html 84,527 bytes; raw HTML SHA-256 7d2b0299a683239c95f44571f862484035c71c89aa6375627a1c5f768298a048; canonical text SHA-256 6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e; HTTP Date 2026-10-31T14:38:37Z; Last-Modified 2026-10-15T17:37:26Z; ETag \"w6OVhWKvL9oyg8jLkO69fLwvTMY=\"",
    "sections_read": [
      "Solution",
      "Error handling"
    ],
    "sections_not_read": [
      "Overview",
      "Implementation in Azure Cosmos DB",
      "Transactional batches",
      "Context, repositories, and UnitOfWork",
      "Event handling: Creation and publication",
      "Persistence",
      "Change feed processing",
      "Cleanup and maintenance",
      "Summary",
      "Considerations",
      "Deploy this scenario",
      "Contributors",
      "Next steps",
      "Related resources",
      "linked pages, sample code and images"
    ],
    "tables_figures": [
      "tables and figures in the inspected sections were read in text form; not reproduced"
    ],
    "license_notes": "Public Microsoft Learn documentation; cite short excerpts and paraphrase; do not mirror.",
    "claims_supported": [
      "This pattern saves events in a data store that's typically in an outbox table in your database before it pushes them to a message broker.",
      "When you save the business object and its events within the same database transaction, the system guarantees no data loss.",
      "You must preserve event order so that the system publishes an OrderCreated event before an OrderUpdated event.",
      "When reprocessing occurs, the application might have already sent some messages to Service Bus, which normally creates duplicate message processing.",
      "To prevent this scenario, you can turn on duplicate message detection in Service Bus.",
      "The primary consideration is to set a suitable TTL value on the DomainEvent documents when the background worker (change feed processor) or the service bus are unavailable."
    ],
    "claims_not_supported": [
      "a consumer inbox implementation",
      "exactly-once delivery to arbitrary external systems",
      "a benchmark, failure drill or production observation",
      "linked pages, sample code and images"
    ],
    "limitations": "One living Microsoft Learn guide with no published version identifier; it describes a Cosmos DB implementation of the producer-side outbox. It does not define a consumer inbox, a repair algorithm or a delivery guarantee for arbitrary external systems.",
    "content_sha256": "6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e",
    "read_scope": "Solution and Error handling sections of the served page, excluding navigation and linked pages",
    "reviewer": "Automated authoring agent",
    "status": "read"
  },
  {
    "id": "read.kafka41-design-exactly-once.2026-10-31",
    "source_id": "src.kafka-design",
    "unit_url": "https://kafka.apache.org/41/design/design/",
    "unit_label": "Design — Apache Kafka 4.1 documentation (exactly-once and offsets)",
    "unit_type": "documentation-page",
    "access_date": "2026-10-31",
    "access_method": "public HTTP fetch on 2026-10-31; served text/html 143,123 bytes; raw HTML SHA-256 d01981797402d75cada10599d586b753d02f8a9deb08d658a0e07758dedadfb7; canonical text SHA-256 674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b; HTTP Date 2026-10-31T14:38:37Z; Last-Modified 2026-10-28T19:19:52Z; ETag \"22f13-65eeb7291ff35\"",
    "sections_read": [
      "Consumer Position",
      "Message Delivery Semantics",
      "Using Transactions"
    ],
    "sections_not_read": [
      "Motivation",
      "Persistence",
      "Efficiency",
      "The Producer",
      "The Consumer",
      "Offline Data Load",
      "Static Membership",
      "Share groups",
      "Replication",
      "Log Compaction",
      "Quotas",
      "linked pages and implementation code"
    ],
    "tables_figures": [
      "tables and figures in the inspected sections were read in text form; not reproduced"
    ],
    "license_notes": "Public Apache Kafka documentation; cite short excerpts and paraphrase; do not mirror.",
    "claims_supported": [
      "The consumer controls its position in this log.",
      "The consumer’s position is stored as a message in an internal topic, so we can write the offset to Kafka in the same transaction as the output topics receiving the processed data.",
      "Exactly once –Each message is processed once and only once.",
      "Otherwise, Kafka guarantees at-least-once delivery by default, and allows the user to implement at-most-once delivery by disabling retries on the producer and committing offsets in the consumer prior to processing a batch of messages.",
      "When writing to an external system, the limitation is in the need to coordinate the consumer’s position with what is actually stored as output.",
      "Exactly-once delivery for other destination systems generally requires cooperation with such systems",
      "The consumer uses partition assignment to ensure that it is the only consumer in the consumer group currently processing each partition.",
      "The producer uses transactions so that all the records it produces, and any offsets it updates on behalf of the consumer, are performed atomically."
    ],
    "claims_not_supported": [
      "an application inbox implementation",
      "exactly-once effects in an external destination system",
      "a benchmark, failure drill or production observation",
      "linked pages and implementation code"
    ],
    "limitations": "One public Apache Kafka 4.1 design page; it states documented delivery semantics and the offset-transaction design, not an application inbox, an external-system implementation, a benchmark or a production observation.",
    "content_sha256": "674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b",
    "read_scope": "Consumer Position, Message Delivery Semantics and Using Transactions sections of the served page",
    "reviewer": "Automated authoring agent",
    "status": "read"
  },
  {
    "id": "read.postgresql-select-locking.2026-10-31",
    "source_id": "src.postgresql",
    "unit_url": "https://www.postgresql.org/docs/current/sql-select.html",
    "unit_label": "SELECT — The Locking Clause (PostgreSQL 18 documentation)",
    "unit_type": "documentation-page",
    "access_date": "2026-10-31",
    "access_method": "public HTTP fetch on 2026-10-31; served text/html 118,042 bytes; raw HTML SHA-256 876b2978f26650506af5fb36cf99135a15c8c68b4d979c3a784ee44f84d1e6fc; canonical text SHA-256 464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94; HTTP Date 2026-10-31T12:36:44Z; no Last-Modified or ETag served",
    "sections_read": [
      "The Locking Clause"
    ],
    "sections_not_read": [
      "Synopsis",
      "Description",
      "Parameters",
      "Examples",
      "Compatibility",
      "linked pages"
    ],
    "tables_figures": [
      "tables and figures in the inspected section were read in text form; not reproduced"
    ],
    "license_notes": "Public PostgreSQL documentation; cite short excerpts and paraphrase; do not mirror.",
    "claims_supported": [
      "With SKIP LOCKED , any selected rows that cannot be immediately locked are skipped.",
      "Skipping locked rows provides an inconsistent view of the data, so this is not suitable for general purpose work, but can be used to avoid lock contention with multiple consumers accessing a queue-like table.",
      "To prevent the operation from waiting for other transactions to commit, use either the NOWAIT or SKIP LOCKED option."
    ],
    "claims_not_supported": [
      "duplicate suppression or transactional-inbox semantics",
      "a durable queue implementation",
      "a benchmark, lock experiment or production observation",
      "linked pages"
    ],
    "limitations": "One living PostgreSQL 18 SELECT page; SKIP LOCKED is a row-locking option for queue-like access, not a message-deduplication mechanism. No query, lock, queue or failure drill was executed.",
    "content_sha256": "464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94",
    "read_scope": "The Locking Clause section of the served page",
    "reviewer": "Automated authoring agent",
    "status": "read"
  },
  {
    "id": "read.debezium-outbox-binding.2026-10-31",
    "source_id": "src.debezium-outbox",
    "unit_url": "https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html",
    "unit_label": "Outbox Event Router — Debezium documentation (2026-10-31 binding)",
    "unit_type": "documentation-page",
    "access_date": "2026-10-31",
    "access_method": "public HTTP fetch on 2026-10-31; served text/html 90,537 bytes; raw HTML SHA-256 382f0bd0cd99f5c8206f9ba0381f3ec71f12ffe373154d351baa8823fd11ad53; canonical text SHA-256 26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e; HTTP Date 2026-10-31T14:38:38Z; Last-Modified 2026-10-31T04:20:50Z",
    "sections_read": [
      "Outbox Event Router",
      "Basic outbox table"
    ],
    "sections_not_read": [
      "Example outbox message",
      "Basic configuration",
      "Options for applying the transformation selectively",
      "Payload serialization format",
      "Emitting messages with additional fields",
      "Configuration options",
      "Distributed tracing",
      "linked pages and examples"
    ],
    "tables_figures": [
      "tables and figures in the inspected sections were read in text form; not reproduced"
    ],
    "license_notes": "Public Debezium documentation; cite short excerpts and paraphrase; do not mirror.",
    "claims_supported": [
      "The outbox pattern is a way to safely and reliably exchange data between multiple (micro) services.",
      "An outbox pattern implementation avoids inconsistencies between a service’s internal state (as typically persisted in its database) and state in events consumed by services that need the same data.",
      "A Debezium connector that is configured to apply the outbox SMT should capture changes that occur in an outbox table only.",
      "Contains the unique ID of the event. In an outbox message, this value is a header. You can use this ID, for example, to remove duplicate messages.",
      "Contains the event key, which provides an ID for the payload. The SMT uses this value as the key in the emitted outbox message. This is important for maintaining correct order in Kafka partitions."
    ],
    "claims_not_supported": [
      "a consumer inbox implementation",
      "exactly-once delivery or a delivery guarantee",
      "a benchmark, failure drill or production observation",
      "linked pages and examples"
    ],
    "limitations": "One living Debezium 3.7 documentation page; it describes the outbox table, event ID and routing configuration, not a consumer implementation, a delivery guarantee or a failure drill.",
    "content_sha256": "26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e",
    "read_scope": "Outbox Event Router and Basic outbox table sections of the served page",
    "reviewer": "Automated authoring agent",
    "status": "read"
  }
]
```

## Source-plan units (integrator)

In `edition/patterns/source-plan.v1.json`, entry
`tycho.pattern.transactional-inbox`, append these five units after the existing
microservices.io unit. Keep this order; the registry unit list must match it.

```json
[
  {
    "source_id": "src.microsoft-cloud-patterns",
    "unit": "Idempotent Consumer pattern — Azure Architecture Center",
    "unit_type": "pattern-page",
    "url": "https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer",
    "sections": [
      "Choose a stable deduplication key",
      "Commit the processed key and the side effects atomically",
      "Guard against concurrent duplicates",
      "Handle side effects that can't join the transaction",
      "Problems and considerations"
    ],
    "status": "read",
    "read_record_id": "read.microsoft-idempotent-consumer.2026-10-31",
    "blocked_reason": null
  },
  {
    "source_id": "src.microsoft-cloud-patterns",
    "unit": "Implement the Transactional Outbox pattern by using Azure Cosmos DB",
    "unit_type": "article",
    "url": "https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos",
    "sections": [
      "Solution",
      "Error handling"
    ],
    "status": "read",
    "read_record_id": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
    "blocked_reason": null
  },
  {
    "source_id": "src.kafka-design",
    "unit": "Design — Apache Kafka 4.1 documentation (exactly-once and offsets)",
    "unit_type": "documentation-page",
    "url": "https://kafka.apache.org/41/design/design/",
    "sections": [
      "Consumer Position",
      "Message Delivery Semantics",
      "Using Transactions"
    ],
    "status": "read",
    "read_record_id": "read.kafka41-design-exactly-once.2026-10-31",
    "blocked_reason": null
  },
  {
    "source_id": "src.postgresql",
    "unit": "SELECT — The Locking Clause (PostgreSQL 18 documentation)",
    "unit_type": "documentation-page",
    "url": "https://www.postgresql.org/docs/current/sql-select.html",
    "sections": [
      "The Locking Clause"
    ],
    "status": "read",
    "read_record_id": "read.postgresql-select-locking.2026-10-31",
    "blocked_reason": null
  },
  {
    "source_id": "src.debezium-outbox",
    "unit": "Outbox Event Router — Debezium documentation (2026-10-31 binding)",
    "unit_type": "documentation-page",
    "url": "https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html",
    "sections": [
      "Outbox Event Router",
      "Basic outbox table"
    ],
    "status": "read",
    "read_record_id": "read.debezium-outbox-binding.2026-10-31",
    "blocked_reason": null
  }
]
```

Update the entry notes to: "Batch 2 public unit read; four additional units read
on 2026-10-31 for mechanism, invariant, failure/recovery and alternative."

Summary changes: `required_units` 278 -> 283; `read_units` 277 -> 282;
`ledger_records` 231 -> 235; `blocked_units` 1 unchanged; `updated`
2026-10-31. Recompute `registry_sha256` after saving the registry. A scratch
application with two-space indentation produced
`0fe34f28e79d4d6c1613209659c5334d41f630de2dc96dc80fd63d203508c606`; do not
copy it without checking the saved bytes.

## Registry patch (integrator)

In `edition/patterns/registry.v1.json`, entry
`tycho.pattern.transactional-inbox`:

- Set `technical_owner.state` to `partial-bounded`.
- Set `coverage.technical` and `coverage.overall` to `partial-bounded`;
  `coverage.decision` and `atlas_owner.state` stay `partial-bounded`.
- Append the six source units below in this order.
- Set `notes` to: "Phase 3 C04 card; bounded owner section and backlink are
  self-checked, not independent-reviewed or sufficient. All four technical
  dimensions bound 2026-10-31 to Microsoft Inbox/outbox, Kafka 4.1 Design,
  PostgreSQL SELECT and Debezium Outbox Event Router; coverage partial-bounded."
- Set `updated_at` to 2026-10-31.

```json
[
  {
    "source_id": "src.microservices-patterns",
    "unit": "Idempotent Consumer — pattern page",
    "status": "read"
  },
  {
    "source_id": "src.microsoft-cloud-patterns",
    "unit": "Idempotent Consumer pattern — Azure Architecture Center",
    "status": "read"
  },
  {
    "source_id": "src.microsoft-cloud-patterns",
    "unit": "Implement the Transactional Outbox pattern by using Azure Cosmos DB",
    "status": "read"
  },
  {
    "source_id": "src.kafka-design",
    "unit": "Design — Apache Kafka 4.1 documentation (exactly-once and offsets)",
    "status": "read"
  },
  {
    "source_id": "src.postgresql",
    "unit": "SELECT — The Locking Clause (PostgreSQL 18 documentation)",
    "status": "read"
  },
  {
    "source_id": "src.debezium-outbox",
    "unit": "Outbox Event Router — Debezium documentation (2026-10-31 binding)",
    "status": "read"
  }
]
```

## Owner-units patch (integrator)

In `edition/patterns/owner-units.v1.json`, entry
`tycho.pattern.transactional-inbox`:

- Set `owner.line` to 54.
- Replace `technical_evidence` with the object below; the existing
  microservices.io binding remains the invariant primary.
- Replace `source_support.auxiliary` with the objects below.
- Set `technical_coverage` to `partial-bounded`.
- Set `notes` to: "All four technical dimensions bound 2026-10-31 to Microsoft
  Inbox/outbox, Kafka 4.1 Design, PostgreSQL SELECT and Debezium Outbox Event
  Router; the invariant, recovery schedule, queue/outbox comparison and
  reversal conditions remain Tycho. Coverage partial-bounded; no promotion or
  acceptance."
- Update the summary: `mechanism_supported` 116 -> 117,
  `failure_recovery_supported` 75 -> 76, `alternative_supported` 80 -> 81,
  `technical_partial_bounded` 15 -> 16, `technical_partial` 67 -> 66. No other
  counter changes; `technical_sufficient` stays 63.

```json
{
  "mechanism": {
    "state": "supported",
    "quote": "An inbox can persist a consumer's processed-event identity and business effect together in **one local transaction**.",
    "reason": "Microsoft names the transactional variant the Inbox pattern and requires the deduplication marker and business side effects in one transaction; its outbox guide applies the same transaction to the business object and its events. The local-authority reading and the external-send boundary are Tycho synthesis.",
    "binding": {
      "source_id": "src.microsoft-cloud-patterns",
      "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
      "section": "Commit the processed key and the side effects atomically",
      "quote": "Avoid this failure window by writing the deduplication marker and the business side effects in the same transaction.",
      "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
    },
    "supporting_bindings": [
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Commit the processed key and the side effects atomically",
        "quote": "This transactional variant is the Inbox pattern",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
        "section": "Solution",
        "quote": "When you save the business object and its events within the same database transaction, the system guarantees no data loss.",
        "revision": "6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e"
      }
    ]
  },
  "invariant": {
    "state": "supported",
    "quote": "The identity must include the correct subscriber and event/effect scope; two different consumers legitimately process the same event into different local states.",
    "reason": "Microsoft requires a store-level uniqueness constraint and a consumer-scoped composite key; Kafka stores the consumer position as a message in the same transaction as the output records. The at-most-one committed effect rule and the retention window are Tycho.",
    "binding": {
      "source_id": "src.microservices-patterns",
      "ledger_record": "read.batch2-idempotent-consumer.2026-10-21",
      "section": "Solution",
      "quote": "Since the (subscriberId, messageID) is the PROCESSED_MESSAGE table’s primary key the INSERT will fail if the message has been already processed successfully.",
      "revision": "3edddaa1959c70dbd9953648e54759b5a2bc167cd121805124e5faafa0eca40f"
    },
    "supporting_bindings": [
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Guard against concurrent duplicates",
        "quote": "Use a uniqueness constraint on the deduplication key such that two transactions can attempt to insert a key, but only one can succeed.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Choose a stable deduplication key",
        "quote": "If the consumers share a deduplication store, key the records on a composite of the consumer identity and the message identity.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.kafka-design",
        "ledger_record": "read.kafka41-design-exactly-once.2026-10-31",
        "section": "Message Delivery Semantics",
        "quote": "The consumer’s position is stored as a message in an internal topic, so we can write the offset to Kafka in the same transaction as the output topics receiving the processed data.",
        "revision": "674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b"
      },
      {
        "source_id": "src.kafka-design",
        "ledger_record": "read.kafka41-design-exactly-once.2026-10-31",
        "section": "Message Delivery Semantics",
        "quote": "Exactly-once delivery for other destination systems generally requires cooperation with such systems",
        "revision": "674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b"
      }
    ]
  },
  "failure_recovery": {
    "state": "supported",
    "quote": "a notification consumer writes a processed marker then crashes before making an external non-idempotent send. On redelivery it may falsely skip the missing send. Reversing the order may send twice.",
    "reason": "Microsoft describes both crash-window directions and the in-progress/completed repair for external effects; Kafka defaults to at-least-once delivery and replays from a consumer position; the outbox relay can duplicate on reprocessing. The retry, reconcile and separate-acknowledgement schedule and the retention owner are Tycho.",
    "binding": {
      "source_id": "src.microsoft-cloud-patterns",
      "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
      "section": "Commit the processed key and the side effects atomically",
      "quote": "A check-then-process flow has a failure window. If a consumer processes a message and then records the key in a separate step, a crash between the two operations leaves the side effects applied but the key unrecorded, so the consumer reprocesses the next redelivery.",
      "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
    },
    "supporting_bindings": [
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Handle side effects that can't join the transaction",
        "quote": "Record the key with an in-progress state, and then perform the external action. Update the record to completed and store the outcome.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Handle side effects that can't join the transaction",
        "quote": "The consumer should reconcile stale records or route unresolved cases for intervention before acknowledging redelivery.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Problems and considerations",
        "quote": "Retain each record at least as long as the broker can still redeliver the original message.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
        "section": "Error handling",
        "quote": "When reprocessing occurs, the application might have already sent some messages to Service Bus, which normally creates duplicate message processing.",
        "revision": "6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e"
      },
      {
        "source_id": "src.kafka-design",
        "ledger_record": "read.kafka41-design-exactly-once.2026-10-31",
        "section": "Message Delivery Semantics",
        "quote": "Otherwise, Kafka guarantees at-least-once delivery by default, and allows the user to implement at-most-once delivery by disabling retries on the producer and committing offsets in the consumer prior to processing a batch of messages.",
        "revision": "674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b"
      }
    ]
  },
  "alternative": {
    "state": "supported",
    "quote": "A unique constraint or conditional insert on effect identity, a producer outbox, or an idempotent downstream API may be preferable when the inbox table and retention cost exceed the duplicate-impact risk.",
    "reason": "Debezium describes a producer-side outbox that avoids state/event inconsistency and carries an event ID for duplicate removal; PostgreSQL supports SKIP LOCKED for queue-like claim but warns of an inconsistent view; Microsoft prefers naturally idempotent operations. The inbox-versus-queue/outbox comparison and reversal conditions are Tycho.",
    "binding": {
      "source_id": "src.debezium-outbox",
      "ledger_record": "read.debezium-outbox-binding.2026-10-31",
      "section": "Outbox Event Router",
      "quote": "The outbox pattern is a way to safely and reliably exchange data between multiple (micro) services.",
      "revision": "26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e"
    },
    "supporting_bindings": [
      {
        "source_id": "src.debezium-outbox",
        "ledger_record": "read.debezium-outbox-binding.2026-10-31",
        "section": "Basic outbox table",
        "quote": "Contains the unique ID of the event. In an outbox message, this value is a header. You can use this ID, for example, to remove duplicate messages.",
        "revision": "26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e"
      },
      {
        "source_id": "src.postgresql",
        "ledger_record": "read.postgresql-select-locking.2026-10-31",
        "section": "The Locking Clause",
        "quote": "Skipping locked rows provides an inconsistent view of the data, so this is not suitable for general purpose work, but can be used to avoid lock contention with multiple consumers accessing a queue-like table.",
        "revision": "464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
        "section": "Problems and considerations",
        "quote": "Prefer naturally idempotent operations.",
        "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
      },
      {
        "source_id": "src.microsoft-cloud-patterns",
        "ledger_record": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
        "section": "Solution",
        "quote": "This pattern saves events in a data store that's typically in an outbox table in your database before it pushes them to a message broker.",
        "revision": "6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e"
      }
    ]
  }
}
```

Auxiliary records:

```json
[
  {
    "source_id": "src.microsoft-cloud-patterns",
    "ledger_record": "read.microsoft-idempotent-consumer.2026-10-31",
    "revision": "f50de2c478e15c5ef148791316beeda854c6d9bfe386ed47f68b679b51f78a34"
  },
  {
    "source_id": "src.microsoft-cloud-patterns",
    "ledger_record": "read.microsoft-transactional-outbox-cosmos.2026-10-31",
    "revision": "6a7b566c0b088e3d95bc3fac1c4f884a9008f0258c72e07aac788499770e143e"
  },
  {
    "source_id": "src.kafka-design",
    "ledger_record": "read.kafka41-design-exactly-once.2026-10-31",
    "revision": "674d7c7e0516cd1f511f8692a720b3b03123e6d9567b191f181eb8cdf165503b"
  },
  {
    "source_id": "src.postgresql",
    "ledger_record": "read.postgresql-select-locking.2026-10-31",
    "revision": "464470632f55ed1f7b662b71e2d1b42351a0adcff0d742df245cf1d18d48dc94"
  },
  {
    "source_id": "src.debezium-outbox",
    "ledger_record": "read.debezium-outbox-binding.2026-10-31",
    "revision": "26c1b278b6e7bd2a85787fa38064b0e9651836ca1bf1e7830df46781d9b6872e"
  }
]
```

## Card registration (integrator)

`edition/patterns/card-batches.v1.json` has no `card_path` for this entry, so
preflight reports `card_path missing or absent`. Add:

```json
"card_path": "book/volumes/v11-pattern-atlas/c04-consistency-events/README.md"
```

The card remains inline; no split is required. `evidence_scope.source_ids`
already names Microsoft, Debezium and PostgreSQL; this lane adds Kafka. The
card `ledger_record` remains `read.batch2-idempotent-consumer.2026-10-21`.

## Content revisions (integrator)

Add one entry to `edition/content-revisions.json`:

- `issue`: 540.
- `authorized_at`: 2026-10-31.
- `authorization`: "B50 transactional inbox source binding".
- `directory_documents`:
  - Owner path, `previous_sha256`
    `423804d92fcb99e86a3e0d9a1b63f99aebf6fe259ee68c655a5793b12363a917`
    (migration baseline), `current_sha256`
    `3cc15e807db3cbf2290876e3e13d0155affda18c7cdae59162f8693d3bb413b5`.
  - Card path, `previous_sha256`
    `4b78177af1e1f2bf96c7488ebf4e0a0512e0bb2a1f35a1e52408720fba3df22d`
    (migration baseline), `current_sha256`
    `43ececcb5a54063053e2477af06b4744d5b5e69a58aea563f09cc24585f0de6e`.
- Empty `source_blocks`, `enrichment_documents`, `enrichment_additions` and
  `enrichment_baselines`.

## Source register (integrator)

`sources/register.json` already admits all four source ids. Update the records:

- `src.microsoft-cloud-patterns`: add the Cosmos outbox page to `version` with
  its 84,527-byte representation, raw hash, canonical hash, HTTP Date,
  Last-Modified and ETag; set `access_checked` and `content_verified` to
  2026-10-31; extend `verification_scope` with the "Solution" and "Error
  handling" sections and the unchanged Idempotent Consumer canonical hash.
- `src.kafka-design`: add the canonical hash and the "Consumer Position",
  "Message Delivery Semantics" and "Using Transactions" sections; set
  `access_checked` and `content_verified` to 2026-10-31.
- `src.postgresql`: add the SELECT page canonical hash, raw hash, HTTP Date,
  absent Last-Modified/ETag and the "The Locking Clause" section; set
  `access_checked` and `content_verified` to 2026-10-31.
- `src.debezium-outbox`: add the 2026-10-31 Last-Modified value and the "Outbox
  Event Router" and "Basic outbox table" sections; set `access_checked` and
  `content_verified` to 2026-10-31. Canonical hash unchanged.

## Validation

In the lane worktree:

    PASS: configured lexical boundary checks; independent-origin review still required.
    PASS: V11 prose <=100; 145 exact owner-link exceptions

A scratch copy at `/tmp/b50-verify` with the book edits, the shared metadata
patches and the temporary card path reported:

    PASS: source plan 145 entries; 282 read; 235 ledger records
    PASS: owner units 145 entries, 145 units, 30 shared pages
    PASS: pattern registry 145 entries, 11 families
    PASS: pattern cards 11 batch(es), 145 entries
    PASS: tycho.pattern.transactional-inbox
    1/1 entries preflight clean

At the lane HEAD without shared metadata, preflight still reports the three
partial dimensions and the missing card path. The lane does not edit shared
JSON, so those failures are expected until the integrator applies this patch.
The full test suite is deferred to the batch end under the batch rule; no test
results are claimed here.

## Limits

The binding covers living public documentation at the 2026-10-31
representations. Microsoft publishes no version identifier for these pages;
Kafka is pinned to the 4.1 Design page; PostgreSQL is the current 18
documentation; Debezium is the living "stable" 3.7 page. The Microsoft outbox
article is a Cosmos DB implementation, not a generic outbox proof. Kafka's
exactly-once discussion is scoped to Kafka read-process-write and says external
destinations generally require their own cooperation. PostgreSQL SKIP LOCKED is
a row-locking option for queue-like access and is not duplicate suppression.
The Debezium page gives no delivery guarantee. No broker, database, crash,
replay, queue, reconciliation or concurrency test was executed. Coverage is
`partial-bounded`; independent review, promotion and owner acceptance are not
claimed.

## Commit scope

The lane commit contains this note and the two book files only:

- The V04/C05 owner page `inbox-atomicity.md`.
- The V11/C04 inline card `README.md`.
- `authoring/B50-TRANSACTIONAL-INBOX-LANE-2026-10-31.md`.

Exact repository paths appear in the lane diff. No shared JSON, promotion or
generated file is in the lane commit.
