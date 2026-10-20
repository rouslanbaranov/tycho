# M9 E16-01 — Admission Wave 03: Numeric Claims Rechecked Against Original Engineers

**Read / reverified:** 2026-10-19. **Scope:** src.m9-a01, src.m9-di01, src.m9-di02, src.m9-cf01 and src.m9-li01, already represented in the 43-candidate register. Publisher-original blog pages were re-opened and their named authors, original dates and exact relevant sections inspected. **Admission:** primary statements and *company-reported* measurements only. Tycho did not reproduce any benchmark, gain access to internal metrics, check source-code revisions or acquire rights to republish graphics, tables or article body.

| ID | Publisher authors and publication date | Original public source | Bounded use |
|---|---|---|---|
| src.m9-a01 | Airbnb Engineering; Jack Dai, Howard Ho, Loc Dinh, Stepan Goncharov, Ted Tenedorio, Thomas Bao; **2025-09-17** | [Migrating Airbnb's JVM Monorepo to Bazel](https://airbnb.tech/infrastructure/migrating-airbnbs-jvm-monorepo-to-bazel/) | Adopted build system, migration stages, company-measured build changes; not universal savings |
| src.m9-di01 | Discord Engineering; Bo Ingram; **2023-03-06** | [How Discord Stores Trillions of Messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) | Cassandra→ScyllaDB historical migration and request-service behavior |
| src.m9-di02 | Discord Engineering; Vicki Niu; **2025-04-24** | [How Discord Indexes Trillions of Messages](https://discord.com/blog/how-discord-indexes-trillions-of-messages) | Search indexing/search-cell redesign, *not* message storage or universal index SLA |
| src.m9-cf01 | Cloudflare Blog; Connor Maddox, Siddhant Sinha, Prasanna Sai Puvvada; **2025-04-10** | [Making Super Slurper 5x faster](https://blog.cloudflare.com/making-super-slurper-five-times-faster/) | S3→R2 migration run, Workers/Queues/DO architecture, bounded test |
| src.m9-li01 | LinkedIn Engineering; Todd Palino; **2015-03-20** | [Running Kafka At Scale](https://engineering.linkedin.com/kafka/running-kafka-scale) | Dated Kafka broker and message counts and auditing; not modern Kafka limits |

## Numeric claim ledger, sections and caveats

| Claim | First-party section | Value that may be cited, with period and denominator | Limitation |
|---|---|---|---|
| A01.001 | 'How did we migrate?', introductory summary | **4.5 years** migration reported to completion | Duration spans coexistence, automated build graph, CI and deployments; not time for Bazel installation |
| A01.002 | 'Migration in numbers' / 'Conclusion' | Local builds/tests **3–5× faster**; IntelliJ sync and dev deploy **2–3× faster** | Publisher's measured program, not a general change to compile algorithms |
| A01.003 | 'Migration in numbers' | Build satisfaction **38% → 68%** | Self-reported internal CSAT, no external controlled cohort |
| A01.004 | 'How did we migrate? — Proof of concept' | Viaduct offered optional **Gradle/Bazel coexistence**; initial **2–4×** pilot build speed did **not** convince engineers until IDE/integration bugs were fixed | Evidence **against** assuming speed is sufficient adoption criterion |
| A01.005 | 'Migrating the deploys — Services' | Approximately **700** services tested and **100** startup/integration failures encountered in Bazel deployment parity checks | Tests uncovered reflection/classpath gaps, so successful compilation alone was inadequate |
| A01.006 | 'Migrating the deploys — Data pipelines' | ~450 data pipelines plus 50 other projects; about **3%** runtime issues for ~400 paved-path pipelines after CI tests | Specific paved path; do not apply 3% to all services/pipelines |
| DI01.001 | 'Our Cassandra Troubles' / 'Several Months Later' | **177 Cassandra nodes** (early 2022) → **72 ScyllaDB nodes** for message database | Different disk capacities/configuration: nodes are not directly interchangeable units |
| DI01.002 | 'Several Months Later' | Historical-read **p99 40–125ms → ~15ms**; message insert p99 **5–70ms → ~5ms** | Publisher-reported operational comparison, workload/snapshot-specific |
| DI01.003 | 'A Very Big Migration' | Rust migrator hit **up to 3.2 million messages/s**; final **99.9999%** blocked by Cassandra tombstones | Peak copy speed ≠ end-to-end completion speed; last ranges required manual compaction |
| DI01.004 | 'A Very Big Migration' | Automated validation sent **small percentage of reads to both DBs** and compared results | A **sample** is not proof of equality for all historical messages |
| DI02.001 | 'So... how are things going?' | Search median **500ms → below 100ms**; search p99 **~1s → below 500ms**; **2× indexing throughput** | Applies to Discord's 2025 *search indexing* redesign, not Cassandra/ScyllaDB message reads |
| DI02.002 | 'So... how are things going?' | **40 Elasticsearch clusters** with thousands of indices | 2025 reported architecture, not universal shard-count recommendation |
| CF01.001 | 'Results: Super Slurper now transfers data to R2 up to 5x faster' | **75,000 S3→R2 objects**, baseline **15m30s**, revised **3m25s** | One benchmark workload; size distribution/network not universal |
| CF01.002 | 'Challenges' | Cloudflare Queues delivers at least once, making **duplicates a first-class problem** | A successful bulk copy still requires idempotency and source/object verification |
| LI01.001 | 'How Big is Big?' | **Over 800B messages/day**, >175TB produced and >650TB consumed per day; peak **13M messages/sec** | **March 2015** LinkedIn fleet, not Kafka defaults or 2026 production inventory |
| LI01.002 | 'How Big is Big?' | **Over 1,100 brokers in more than 60 clusters** | LinkedIn's multi-tier setup, not a software sizing rule |
| LI01.003 | 'Auditing Completeness' | Per-stage producer/broker/consumer auditing described | The source's **count-based** evidence is vulnerable to a drop+duplicate cancellation; source does NOT claim perfect semantic event identity |

## Corrections / architecture applicability

1. **Bazel build parity:** the article names startup/integration and runtime reflection/library errors. Agentic migration checks must include *actual deploy artifacts*, not just syntax and tests. If Tycho claims the migration was effortless, mark that claim false.
2. **Discord's two migrations differ:** src.m9-di01 is message datastore and Rust demand shaping; src.m9-di02 is Elasticsearch/search-cell architecture, with its own p99 and indexing benchmarks. Their figures must **never** be pooled or compared as one test.
3. **Discord last 0.0001%:** progress count can hide unhandled tombstones, requiring special-case recovery. An unfinished migration is not success at 99.9999%.
4. **Cloudflare:** the '5×' title refers to a specific 75k-object S3→R2 test, while queues need idempotent consumers. Do not apply this factor to any arbitrary file size distribution.
5. **LinkedIn historical time:** the 2015 scale numbers do not establish current production capacity or justify choosing Kafka with no traffic baseline.
6. **Licensing:** only original summaries, URL/section pointers and independently drawn architecture graphs are retained in Tycho. No company figures, screenshots, proprietary code, slide decks or article passages are mirrored.

## Admission disposition

- Five additional IDs **source-reviewed for the bounded claims above**, not for every potentially relevant statement on their pages.
- Previously reviewed specific public references: wave 01 (src.m9-n01/src.m9-n02/src.m9-n05/src.m9-n06/src.m9-n07) and wave 02 (src.m9-sh04/src.m9-sp02/src.m9-sp03).
- Remaining registered candidate references still require full article-specific creator/date/claim gate or explicit rejected status. Do not declare all 43 admitted.
- Independent reviewer, production retrieval execution, source-code SHA pins and copyright rights beyond hyperlink/paraphrase remain pending.
