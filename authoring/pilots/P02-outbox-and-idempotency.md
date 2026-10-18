# Pilot P02 — Local transactions, outbox publication and duplicate effects

**Status:** research contract ready; technical deep reading and writing **not performed**. **Execution owner:** [#39](https://github.com/rouslanbaranov/tycho/issues/39). **Draft book owner:** V04/C04–C05 with pointers to V05/C01 and V04/C07. **Pilot class:** end-to-end across data and message boundaries.

## Question and fictional context

A wholly fictional workshop registration service must persist one accepted registration and arrange downstream notification. A database commit and external message delivery are independently failure-prone. Under what exact assumptions can local atomicity be combined with **at-least-once** publication and idempotent consumer effects without pretending the remote handler belongs to one atomic transaction?

Use the requirements model from #17, but do not reuse any employer architecture or production observation.

## Required independently public evidence to inspect

- `src.postgresql`, official [PostgreSQL documentation](https://www.postgresql.org/docs/current/), exact relevant **transaction / isolation / WAL** sections to identify and pin to a concrete major release during execution; no guarantee is attributed yet to the rolling current page.
- `src.debezium-outbox`, official [Debezium Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), review event-table conventions, key/payload routing, transaction boundary and connector behavior; pin exact release and caveats when reading.
- `src.kafka-design`, Apache Kafka 4.1 [design documentation](https://kafka.apache.org/41/design/design/), verify its actual delivery/idempotence/transactions guarantee boundaries; do not claim cross-system exactly-once without supported evidence.
- `src.stripe-idempotency`, official [idempotent requests](https://docs.stripe.com/api/idempotent_requests), as a **reference example of an independent public HTTP API policy**, not an assumed specification for the fictional system. Distinguish operation idempotency from infrastructure de-duplication.

No paid-book content or copied reference implementation is allowed.

## Required explanation and experiments to propose

1. Sketch the client's intent key, local transaction/uniqueness decision, outbox row and publication/consumer boundaries.
2. Walk through successful commit and downstream processing with distinct acknowledgement locations and data owners.
3. Show at least four failure points: pre-commit crash, post-commit/pre-publication crash, publication acknowledged but local marker not updated, consumer applies effect then acknowledgement is lost.
4. Compare at-least-once + idempotent effects, transactional outbox, direct synchronous call and distributed transaction proposals (where warranted). Record tradeoffs rather than technology rankings.
5. Describe what remains unknowable until message ordering, consumer side-effect target and key expiry are specified; include an **insufficient evidence** outcome if durable deduplication scope is missing.
6. Show how version/retention/partition constraints may reverse a candidate design. Leave any cross-region/mixed-version recovery to P03 when appropriate.

**Exclusions:** platform-specific code, measured throughput, exhaustively documenting Kafka, provisioning brokers, promising end-to-end exactly-once or final modernization verdict.

## Delivery and quality

Write coherent **real pages** about event-publication and duplicate-effect mechanisms, not an implementation list. Give exact source sections/versions and a claim evidence table, synthetic step-by-step state transitions, alternatives, failure/retry matrix and bounded validation tests. Describe observed/published/inferred/proposed status for each guarantee. Existing CI + manual source and diagram validation; no human review presumed.
