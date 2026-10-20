# #213 — actually executed synthetic technical examples, not substituted platform integration

> **Historical manuscript transition — 2026-10-20, before edition assembly:** The owner confirmed independent substantive/content acceptance of all 69 primary chapter manuscripts at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 merged into main at `f9834ef903fc5808f3a1edede208d82aac08f4e6`; #213 and E14 #15 are completed. #214 is open and ready for ten-volume/69-chapter edition assembly and named publication. The exact accepted-head 13/13 validation groups and 215/215 tests PASS are owner-reported in [PR #218](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915), not a new run on a later status commit. Earlier pending/0-of-69/review-open rows and pre-merge instructions below are historical and superseded for the manuscript acceptance gate. Their original observations and evidence limits are retained; no signed per-chapter reviewer records are manufactured. No finished physical edition or deployed service is claimed; visual rendering/live MCP remain owner-cancelled. See [current state](STATE.md) and [reconciliation](PROJECT_STATUS_RECONCILIATION_2026-10-20.md).

**Execution date:** 2026-10-20. **Environment:** Python 3.13.5; Python SQLite library 3.46.1; OpenJDK Java/Javac 21.0.12.1. No installed PostgreSQL server/psql, Kafka server, Neo4j server, PgBouncer, R2DBC, or JDK 24. Local Git cannot resolve `github.com`, hence **no full Tycho Python suite** could be executed from this environment. This is a standalone *original synthetic* reproduction of selected semantics; not a test of a deployed service.

**Reproducible user-facing source/log package:** `tycho-semantic-example-tests-20261020.zip` created in the ChatGPT conversation attachment on this date, containing exactly the two source files and command outputs. The package is not asserted to be hosted in the repository. Raw SHA-256 from the executed source artifacts:

- `test_semantic_examples.py` — `337239eded3a744c9ddbab5fe6efd4113daaaf7ec20340e17e43e819d6dd30f8`
- `VirtualThreadsBudget.java` — `7fe8dbb57124f84f3bc617cb973736d15537f0386a7432a6cab341e14a725892`

**Commands actually run:** `cd tycho_acceptance && python test_semantic_examples.py`, `javac VirtualThreadsBudget.java && java VirtualThreadsBudget`.

## Recorded results — genuinely run

```text
test_graph_recursive_sql_same_authorized_endpoints ... ok
test_idempotency_key_payload_conflict ... ok
test_open_vs_closed_trace_ledger ... ok
test_outbox_relay_crash_after_delivery ... ok
test_rrf_score_and_auth_exclusion ... ok
test_stale_cache_fill_fenced_by_generation ... ok

Ran 6 tests in 0.004s
OK

PASS Java 21: 30 virtual tasks share maximum 3 downstream slots; peak=3
NOT TESTED: Java 24 monitor-unmounting, JDBC or performance/p99.
```

| Book owner(s) | Actually exercised | Result and strict scope | **Never infer** |
|---|---|---|---|
| V06/C06 | Synthetic 6-node, 6-edge graph evaluated by **SQLite** recursive CTE and independent Python traversal; required authorized endpoints `U1,U2` | PASS same end-node set and per-tenant filter under fixed synthetic topology | Neo4j Cypher syntax/runtime, PostgreSQL array CTE syntax, index planner cost or storage ACL enforcement |
| V04/C05 | SQLite local atomic booking/outbox tables, simulated relay crash after consumer commit but before ack, replay + unique inbox | PASS one local row per logical effect and recovered sent marker | Kafka/Debezium interoperability, external email exactly once, PostgreSQL locking |
| V06/C02 | Generational cache invalidation v17→v18 and delayed stale value | PASS old v17 not reinstalled after v18 high-water mark | Redis CAS/Lua/cluster consistency or visibility across replicas |
| V06/C05 | Reciprocal Rank Fusion `k=60`; lexical and semantic lists `A,B,C` and `C,D,A`; distinct authorization exclusion | PASS A/C tie, forbidden A filtered independently and C selected | Actual Elasticsearch RRF scoring configuration or a production relevance/security audit |
| V01/C02 | Paired six-second synthetic open/closed arrivals and deterministic pair completions | PASS open 12 offers / 6 completions / 6 pending; closed 6 offers / 6 completions / 0 pending | k6 generator throughput, actual network arrival, response-time distribution or deployment capacity |
| V04/C04 | Scoped operation ID `K42` and payload fingerprint under SQLite | PASS same-payload retry returns R7; changed payload conflicts | Concurrent first-use race safety in PostgreSQL or expiry/replay horizon |
| V03/C02 / V03/C05 | Java 21 virtual-thread-per-task executor with a 3-permit downstream semaphore; 30 jobs | PASS max three admitted simulated workers; all 30 jobs completed | Throughput improvement, p99, JDK24 JEP491 pinning or actual JDBC connection pool behavior |

## Remain unexecuted — real platform acceptance targets

- **PostgreSQL 17**: exclusion-constraint concurrency, Serializable full-transaction retry, WAL replica lag and PITR restore, read-plan skew, actual recursive CTE with arrays, mixed-version DDL/online changes.
- **Neo4j 5/25**: Cypher variable-length path parsing, relationship versus node uniqueness, query index and tenant/object authorization over the full graph.
- **Kafka 4.1 / Debezium 3.6 / Flink 2.1**: leader replacement / eligible replicas, transactional Kafka topics versus external DB, outbox CDC/consumer effects, watermark-late-record checkpoint recovery.
- **PgBouncer 1.21+ / HikariCP / Java**: named protocol prepared statements versus SQL PREPARE/session state, JDBC pool saturation and failover, Reactor/R2DBC backpressure and native pinning.
- **Versioned verification engines**: Sigstore/SLSA attestation signature/identity policy, cross-tenant retrieval negative test on a real vector/index backend, full repository Python validation.
- No disruptive production systems or private data should be used as a shortcut. Synthetic integration stacks must have pinned versions and reproducible safe reset conditions.

**Editorial interpretation:** these six Python and one JVM runtime demonstrations provide useful falsifiable teaching oracles, but **zero Tycho chapters are independently ACCEPTED**, because the complete source/semantic test obligation is broader. In particular no one should label the tests `PostgreSQL 17 PASS`, `Neo4j PASS`, `Kafka PASS` or `JDK24 PASS`.

