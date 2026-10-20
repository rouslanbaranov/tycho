# E16-01 — Source Admission Wave 07: Storage-Engine Economics, JVM Cache Contention and Selective Extraction

**Checked:** 2026-10-19 against four original company engineering publications (src.m9-u03, src.m9-n18, src.m9-sh03, src.m9-me01). Source disposition: **admit only the individually listed, historically bounded claims**, not a complete endorsement of either technology, copyright reuse or independent benchmark verification. All quotations/graphics remain at the external publishers; Tycho uses original paraphrase and source-section pointers.

## Identity and original sections

| ID | Publisher, authors and date | Primary evidence / exact sections | Admission |
|---|---|---|---|
| src.m9-u03 | Uber Engineering; Shenglin Du, Hao Xu, Shriniket Kale; **2022-09-01** | [MySQL → MyRocks Migration](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/); 'Introduction', 'Motivation', 'Challenges', 'Upgrade and Migration', 'MySQL 8.0 Upgrade', 'MyRocks Migration' | First-party technical narrative with source-reported relative disk benchmark |
| src.m9-n18 | Netflix TechBlog; Vadim Filanovsky and Harshad Sane; **2022-11-09** | [Seeing through hardware counters](https://netflixtechblog.com/seeing-through-hardware-counters-a-journey-to-threefold-performance-increase-2721924a2822); 'The problem', 'False Sharing', 'True Sharing', 'Future work' | First-party one-service CPU performance investigation, not general JVM gain |
| src.m9-sh03 | Shopify Engineering; Allan Leinwand; **2022-01-20** | [Cloud, Load, and Modular Code](https://shopify.engineering/cloud-load-modular-code-shopify-2022); introduction and 'We are building more modular code' | First-party 2021/BFCM traffic and renderer-extraction report; no universal extraction target |
| src.m9-me01 | Meta Engineering; author attributed to first-party engineering publication **2013-06-25** | [TAO: The power of the graph](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/); 'Memcache and MySQL', 'Objects and associations', 'TAO data model and API', 'Implementation', 'Consistency' | Original historical graph-serving architecture and described trade-offs; no modern adoption claim |

## Per-claim provenance and alternatives

| Claim ID | Exact location / published observation | Scope / contradiction |
|---|---|---|
| evidence.m9-u03.001 | 'Introduction': all Schemaless instances and **some** Docstore instances had migrated to MyRocks since **2019** | **Not all** Docstore migrated as of September 2022 |
| evidence.m9-u03.002 | 'Challenges': InnoDB table compression yielded ~**5% disk saving**; publisher's MyRocks benchmark yielded **over 30%** with acceptable latency | Different interventions and benchmarks; 30% is not a portable guaranteed reduction |
| evidence.m9-u03.003 | 'MySQL 8.0 Upgrade': needed MySQL **5.7→8.0** before MyRocks for XtraBackup compatibility; process took **over a year**, with higher memory, optimizer changes and corruption risks | Actual migration precondition and adverse work, not 'drop-in engine switch without operations' |
| evidence.m9-u03.004 | 'Upgrade and Migration': followers then leader, partition then region order; validate data integrity, latency/error and parity before expanding | Reported staged path; no full source-private deployment manifest available |
| evidence.m9-n18.001 | 'The problem': **16-vCPU m5.4xl → 48-vCPU m5.12xl** GS2 CPU-bound workload; at ~55% CPU target initially **~25% throughput improvement** and >**50% mean-latency worsening** | One service; bigger instance did **not** deliver expected 3× performance |
| evidence.m9-n18.002 | 'False Sharing': CPU counters and VTune found HotSpot adjacent `_secondary_super_cache` / `_secondary_supers` cache-line interactions, fast node band ~**12%** | 1-in-8 memory alignment evidence, JVM and instance-specific |
| evidence.m9-n18.003 | 'True Sharing': after padding, throughput remained ~**150 RPS/node** vs **250 target**; bypass of secondary-superclass-cache writes under a VM flag reported ~**350 RPS/node**, **3.5×** the initial large-node throughput | **Two sequential fixes**, not one generic option or free JVM update |
| evidence.m9-sh03.001 | 2021 BFCM retrospective: Shopify reported **32 million app-server requests/minute** and **>34 million load-balancer requests/minute** | Peak period BFCM 2021, not 2026 sustained traffic |
| evidence.m9-sh03.002 | 'We are building more modular code': extracting storefront renderer from monolith and refactoring yielded **4× faster cache fills** and **5× faster page rendering** | Publisher-reported combined extraction/**refactoring** result, cannot attribute entire gain to network/service separation |
| evidence.m9-sh03.003 | Same section: renderer could deploy regionally without moving complete Rails monolith | *Selective extraction* is consistent with a modular-monolith strategy; reject 'Shopify never used independent services' |
| evidence.m9-me01.001 | 'Memcache and MySQL': early MySQL + memcache direct application access created complex cache and data-model responsibilities | Architectural motivation, not proof every relational cache invalid |
| evidence.m9-me01.002 | 'TAO data model and API': typed graph object/association model supports point, ordered range and count queries but deliberately not complex graph traversals/pattern matching | **Workload-specialized serving API**, not replacement for arbitrary graph database |
| evidence.m9-me01.003 | 'Implementation', 'Consistency': follower/leader cache tiers with MySQL per shard; *eventual consistency by default*, stronger override trades cost/availability | Financial/identity invariants may require a different choice; 2013 state not present-day topology |
| evidence.m9-me01.004 | Introduction / implementation: Meta reported **>1 billion reads/sec and millions of writes/sec** within 2013 historical workload | Publisher-report scale, not contemporary sizing benchmark |

## Modernization cross-checks

- **Uber storage engineering (src.m9-u03)** and **Netflix JVM tuning (src.m9-n18)** both refute simplistic 'more CPU/storage nodes solves it': physical resource bottleneck must be measured, and the migration may require a costly preparatory compatibility upgrade or JDK patch.
- **Shopify (src.m9-sh03)** is a decisive counterexample to a false binary between modular monolith and microservices. It kept a modular monolith while extracting high-volume storefront rendering to independent locations. Do not infer all modules were extracted.
- **Meta TAO (src.m9-me01)** optimized a defined graph-serving operation profile with eventual consistency and typed associations; do not turn it into a generic recommendation to replace ACID transaction workloads with a cache.
- **Measurements are different types**: Netflix GS2 per-node RPS with fixed autoscaling target, Uber disk-space benchmarks, Shopify storefront latency/cache fill and Meta aggregate 2013 operations/s are **not comparable test populations**. Agent output must retain original denominator, time window and workload.
- **Reuse boundary:** URLs, metadata, source-section pointers and independently authored explanations only. Copyright-protected figures, source articles and diagrams were not imported; no private employer data was used.

## Coverage / completion status

Previous original-source waves 01–06 documented **32 of 43 candidate IDs** with at least one bounded claim or explicitly restricted source status. This wave adds **src.m9-u03, src.m9-n18, src.m9-sh03, src.m9-me01** (all distinct from those 32), bringing the running minimum to **36/43**. The other **7** require bounded first-party section claims or an explicit exclusion decision. This is claim-source scope coverage, not independently accepted cases. This number is **claim-grounded source coverage**, not 27 independently reproduced company benchmarks or approved case-study chapters. Issue #114 stays open pending the remaining source decisions. Independent review #121 is still required.
