# Pilot research 2 — local transaction to downstream event

- **Contract ID:** TYCHO-PILOT-END-TO-END-v0.1
- **Issue / owner:** [#39](https://github.com/rouslanbaranov/tycho/issues/39); proposed canonical chapters V04/C04–C05.
- **Status:** research contract and synthetic scenario only; not an implemented transactional system or publication guarantee.
- **Audience:** architects and developers who must make a local durable state change observable to another component without claiming an impossible single atomic transaction across arbitrary endpoints.
- **Primary question:** If a local database transaction and a broker publication cannot share an assumed atomic commit, how do a transactional outbox, change-data capture or polling relay, consumer deduplication, retry/recovery and ordering choices affect observable correctness?
- **Connection to first pilot:** the workloads, retries and load conditions are explicit, not technology-choice thresholds. Review the already-authored material from #38 for load/measurement terminology rather than repeat it.

## Original synthetic story and boundaries

A fictional workshop organizer accepts a registration, writes a reservation record to a relational database and wants a notification service to learn about that committed change. There is no real platform, business database, internal schema, measured load or proprietary behavior behind the example.

**Hard invariant proposed for the story:** no notification is treated as authoritative proof of a committed registration; a successfully acknowledged registration must be recoverably discoverable. An outbound notification may arrive more than once and consumers must express their idempotency contract. Treat desired outcome, assumed atomic boundaries and implementation guarantee separately.

**Normal sequence to research:** validate command → commit registration and outbox entry locally → connector/relay observes outbox record → broker accepts event → consumer processes/deduplicates → user sees an outcome. Each step needs a named transactional boundary and evidence.

## Research scope and primary public sources

These are precise reading **targets**, not a statement that all material has already been reviewed.

| ID | Version and exact reading target | Specific question and caveat |
|---|---|---|
| `src.debezium-outbox` | [Debezium Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), exact doc release/page revision captured at time of #39 writing: **Basic outbox table**, **Basic configuration**, event key/ID columns, and connector options | How an outbox row becomes a routed event, and what the SMT actually controls. Outbox CDC alone is not a global exactly-once business-effect guarantee. |
| `src.postgresql` | [PostgreSQL version-pinned manual](https://www.postgresql.org/docs/current/), then select concrete major-version URLs for **Transactions**, **Transaction Isolation**, **WAL** or **Logical Decoding** if claimed | Exactly what a local commit/durable WAL/logical change represents; a generic current-doc link does not prove a versioned implementation detail. |
| `src.http-semantics` | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), §§9.2.2 **Idempotent Methods** and 9.2.3 **Methods and Caching** as applicable | Distinguish protocol idempotence from an application-level idempotency-key contract, not all POST retries are automatically safe. |
| `src.aws-idempotency` | [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), carefully scoped headings and revision/access date | Idempotency tokens, ambiguous responses, duplicate requests and same-token/different-intent concerns, if verified from the actual passage. |
| `src.kafka` | [Apache Kafka official documentation](https://kafka.apache.org/documentation/), pin explicit version + sections on producer idempotence and transactions before writing | Constrain broker-level semantics. Do **not** assume consumer database effects are enclosed in a Kafka producer transaction. |

Only cite the exact sections inspected in the #39 chapter. Public product documentation is evidence of its specified behavior in declared versions, not independent proof of an end-to-end deployment.

## Required timelines and failure matrix

| Interruption or operation | Question to answer |
|---|---|
| Failure before the local commit | Do both registration and outbox rollback within one database transaction? |
| Local commit succeeds, process dies before response | How can a retry recover the existing outcome without creating a new authoritative registration? |
| Commit succeeds, relay not yet publishes | Which durable record remains, how is delay detected and what are liveness limits? |
| Broker accepts, relay crashes before recording progress | Can publication repeat? How does consumer deduplication work and how long is its key retained? |
| Consumer applies effect, acknowledgement fails | Which idempotency invariant limits repeated side effects? |
| Two events for same aggregate and partition changes | Which ordering scope and key selection matter, and where is ordering *not* guaranteed? |
| Schema/consumer versions coexist | How are event format and compatibility validated and rolled back? |

Analyze at least **two** alternatives (e.g. database outbox with CDC vs polling relay, plus single-service/synchronous option when acceptable). Explain operational cost, latency, failure points, consumer state, data retention, and cases where the pattern is unwarranted.

## Completion and evidence gates for #39

- One coherent event/data-flow explanation showing exactly where atomicity stops.
- Precise public-source passage IDs/links, release applicability and a claim-to-evidence ledger.
- Annotated **original synthetic** normal/retry/duplicate/recovery diagrams or tables; no copied production system.
- Testable invariants and a minimal validation plan (concurrent/repeated request, duplicate broker delivery, restart and replay).
- Distinguish theoretical guarantee, official specification, synthetic scenario expectation and **measured** result (none until a test is actually run).
- Reuse canonical previous-page explanations by link, not long duplicated queueing content.
- Acceptance may legitimately record **insufficient evidence** for a product/version-specific guarantee and an exact follow-up source/test action.
