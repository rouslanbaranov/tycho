# M9 E16-01 — Netflix Primary Claim Admission Wave 05: GraphQL and Cassandra

**Date of direct source inspection:** 2026-10-19. **Admitted IDs:** N09, N10, N11, N12, each restricted to the historical source-specific claims below. Company-authored articles/release notes; figures remain *publisher reports*, not Tycho-reproduced measurements. Copyright allows linked citations/original paraphrase, not copied charts or bulk reproductions.

| ID | Verified source identity | Original URL and date | Temporal boundary |
|---|---|---|---|
| N09 | Kavitha Srinivasan and Paul Bakker; Netflix TechBlog | [A Tale of Two Frameworks](https://netflixtechblog.medium.com/a-tale-of-two-frameworks-the-domain-graph-service-framework-meets-spring-graphql-f8237f09c389), **2024-04-08** | Integration/opt-in phase and plans, not a proof every service already migrated |
| N10 | Netflix DGS Framework maintainers, official release notes | [New and Noteworthy: DGS 8.5.0 and 10.0.0](https://netflix.github.io/dgs/announcements/), **2024-03-29** and **2024-12-17** | Versioned release-owner evidence subsequent to N09 |
| N11 | Guil Pires, Jennifer Prince, Jose Camacho, Ken Kurzweil, Phanindra Chunduru; Netflix TechBlog | [Evolution of Cassandra Data Movement](https://netflixtechblog.medium.com/the-evolution-of-cassandra-data-movement-at-netflix-6e13329c80a1), **2026-05-18** | Reported production migration and company assertions, not audited savings |
| N12 | Rajiv Shringi, Kaidan Fullerton, Oleksii Tkachuk, Kartik Sathyanarayanan; Netflix TechBlog | [Dynamic Repartitioning for Time Series Workloads](https://medium.com/netflix-techblog/dynamically-splitting-wide-partitions-in-cassandra-for-time-series-workloads-0eded064f456), **2026-06-03** | Cassandra 4.x workload- and date-bound implementation |

## Evidence locations, numbers and failure/negative controls

| Claim | Exact source section | Supported statement | Limit |
|---|---|---|---|
| N09.001 | 'Framework Architecture with Spring GraphQL' | DGS schema provider and programming model persisted; QueryExecutor delegated to Spring GraphQL execution, transport moved to Spring MVC/WebFlux handlers | Application API compatibility ≠ identical filter/async semantics |
| N09.002 | 'Performance' | Initial production-canary comparison: **>50% CPU degradation** and **~20% request latency degradation**; intermediate **10–20% CPU degradation** | Dated 2024 large Netflix service canaries; no generic Spring GraphQL regression |
| N09.003 | 'Performance' | Implicit async request dispatch repeatedly ran non-async-aware filters; **disabling async processing** restored reported baseline parity | Explicit counterexample to 'async everywhere' without lifecycle awareness |
| N09.004 | 'Going Forward' | Fleet adoption plan in April for Q2/Q3 2024 and removing legacy before year-end | At that time it was a **plan**, not proof of completion |
| N10.001 | 'DGS Framework 8.5.0 with Spring GraphQL released!' | **2024-03-29** integration release and opt-in starter | Do not conflate first opt-in and later default |
| N10.002 | 'DGS Framework 10.0.0 released!' | **2024-12-17** removal of legacy modules; maintainers say they migrated Netflix services and see prior-level performance | **Release-owner assertion**, not independent per-service production audit |
| N10.003 | 'Detailed list of changes' | Earlier DGS starter and selected websocket/subscription modules were removed/replaced, some API tests needed adaptation | Calling DGS10 a perfectly backward-compatible zero-change update for all clients is false |
| N11.001 | 'Casspactor: The Engine We Outgrew' | Legacy engine reportedly handled **~1,200 movements/day** totaling **~3 PB/day** | Legacy throughput scoped by source, not new system's measured speed |
| N11.002 | 'Fragile Metadata Dependencies' / 'The New Stack: A Layered Architecture' | Old metadata was assembled from inconsistent systems; new design derives schema/topology/data from authoritative S3 backups into Cassandra Analytics / model-aware DataFrames | No full runbook/source code revision available |
| N11.003 | 'Pillar 1: Validation' | Source defines **C** as old Casspactor output, **M** as new; compare **both C−M and M−C**. Any nonzero difference prompted investigation; target exact equivalence | A schema/multiset/time-window-aware equality definition is required in another architecture; row counts alone insufficient |
| N11.004 | 'Uncovering and Resolving Disparities' | Differences included TTL/reference timestamps, consistency levels, backup choices and connector business logic | Cases of difference cannot simply be dismissed as noise |
| N11.005 | 'Pillar 3: Safety' / 'Leveraging Abstraction: The Decider Pattern' | Maestro Decider/Connector Controller selects connector per cohort/job; failed new connector conditionally invokes Casspactor | The source calls it transparent; **do not infer zero additional runtime on fallback** |
| N11.006 | 'Conclusion' and 'The New Stack' | Netflix claims notable performance improvements and savings **in the order of USD millions** | No independent audited dollar amount, TCO baseline or transferability |
| N12.001 | 'Impact of Wide Partitions' | Some TimeSeries dataset averages were single-digit milliseconds, wide partition outliers ran into seconds and timeouts | Different dataset populations; not one universal p99 |
| N12.002 | 'Solution 1: Time Slice Re-Partitioning' | A histogram-based worker adjusts **future** slice configurations, targeting configurable **2–10 MiB** density | Does not rewrite all old wide partitions; density not a universal database tuning constant |
| N12.003 | 'Solution 2: Dynamic Partitioning per ID' / 'Immutability' / 'Checkpointing' | Kafka read-path detection and checkpointed planner initially focus on **immutable** partitions | Mutable split remains a future proposal |
| N12.004 | 'Validating Splits' / 'Serving Reads' / 'Fallbacks' | Pre/post split checksums, Bloom-based routing, and retention of the original wide row provide staged safety | Bloom filter false positives require metadata check; checksum alone is not full semantic proof |
| N12.005 | 'Building Additional Confidence' | Offline Data Bridge verification and staged shadow old/new read comparison were used before the final routing switch | Do not attribute exact stage percentages unless independently stated |
| N12.006 | 'Results' | Authors report improved wide-partition average reads from **seconds to low-double-digit ms**, tails to **~200ms or better** for specific workloads | Source graph/metric windows not replicated; not a service-wide guaranteed 200ms SLO |

## Correct historical decision transfer

1. **N09→N10:** An April roadmap must be read together with a December release announcement, not rewritten as a one-date migration.
2. **N11:** Data movement correctness requires both set differences and transactional/temporal comparability; job-interface stability and fallback matter as much as peak throughput.
3. **N12:** The two repartitioning levers address different skews. A future time-slice adjustment is not an existing partition split. Netflix intentionally reduced initial scope to immutable rows and maintained original storage to avoid irreversible failure.
4. **Original sources / rights:** all documentation is Tycho-authored summaries and independently designed diagrams; the original graphs, logs, private connectors and specific source snapshots are not mirrored.
5. **Cross-company unknown:** a method that worked in one Netflix Cassandra 4.x cluster does not decide if a different company should choose Cassandra, DynamoDB, ScyllaDB or a lake storage layer.

**Admission summary:** four additional bounded original sources now have explicit first-party proof. Historical-source claim coverage becomes **23/43**, but other 20 candidates remain partially read, blocked or without strict author/section review. This ledger does **not** claim that #114 or M9 passed independent review. The static-retrieval/readiness gates remain separately owned by K10–K20 and #120/#121.
