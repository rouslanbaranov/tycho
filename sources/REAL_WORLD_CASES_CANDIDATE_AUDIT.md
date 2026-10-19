# M9 / E16-01 — Complete Candidate Reachability & Admission-Gate Audit

**Review date:** 2026-10-19. **Scope:** all 43 original company-source candidates, no imported private material.  
**Procedure:** attempted to open each registered public URL in the source reader, followed the site's canonical redirects, and inspected accessible primary sections. This is a **link/provenance triage**, **not** verification of every factual claim, blanket content license, or a claim that all 43 entries meet final source-admission gates.

## Measured status

- **43** original candidates inspected in source registry.
- **38** accessible in this research reader, including U05 after a canonical locale URL fix. Accessibility does **not** imply completeness, reproducibility or license to mirror.
- **5** unresolved/failed primary URL accesses: N14, N15, SH04, SP02, SP03; **not admitted** pending retry and alternate first-party resolution.
- **5** Netflix entries already have detailed bounded claim/location evidence in [wave 01](REAL_WORLD_CASES_ADMISSION_WAVE_01.md): N01, N02, N05, N06, N07.
- Remaining accessible sources have title/producer and topic triage, but are **not yet claim-admitted** for arbitrary chapter assertions; a named original section/timestamp and author/date must accompany each assertion before authoring.
- **0** externally measured benchmarks and **0** reviewed case chapters. Only original links/paraphrase may be reused; no redistribution rights assumed.
- Primary first-party article availability is not equivalent to independently verified company outcomes.

## Per-candidate status and next claim-proof gate

| ID | Company | First-pass result | Primary source URL | Evidence boundary / admission action |
|---|---|---|---|---|
| N01 | Netflix | CITED — claim-ledger wave 01 | [original](https://about.netflix.com/en/news/completing-the-netflix-cloud-migration) | Already included in wave 01 claim audit. |
| N02 | Netflix | CITED — claim-ledger wave 01 | [original](https://www.infoq.com/presentations/netflix-java/) | Already included in wave 01 claim audit. |
| N03 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://dev.java/community/javaone-2026/sessions/lrn1058/) | JavaOne 2026 session abstract, 'Summary' (Paul Bakker, March 17, 2026). PROVES claimed talk scope (3000+ Java services) only; no adoption outcome or performance. |
| N04 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://sites.google.com/netflix.com/javaplatformnetflix/jif) | Netflix Java Integration Framework team homepage, 'Our work': Spring Boot starter/infrastructure scope, not benchmark; undated living page. |
| N05 | Netflix | CITED — claim-ledger wave 01 | [original](https://netflixtechblog.com/bending-pause-times-to-your-will-with-generational-zgc-256629c9386b) | Already included in wave 01 claim audit. |
| N06 | Netflix | CITED — claim-ledger wave 01 | [original](https://netflixtechblog.com/java-21-virtual-threads-dude-wheres-my-lock-3052540e231d) | Already included in wave 01 claim audit. |
| N07 | Netflix | CITED — claim-ledger wave 01 | [original](https://netflixtechblog.com/zuul-2-the-netflix-journey-to-asynchronous-non-blocking-systems-45947377fb5c) | Already included in wave 01 claim audit. |
| N08 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://github.com/Netflix/zuul/wiki/How-It-Works-2.0) | Netflix/zuul wiki 'How It Works 2.0': architecture diagram/process descriptions; Git wiki revision must be captured prior to code-level claims. |
| N09 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://netflixtechblog.com/a-tale-of-two-frameworks-the-domain-graph-service-framework-meets-spring-graphql-f8237f09c389) | Srinivasan & Bakker, 2024-04-08, sections 'Why not retire...', 'Framework Architecture', 'Performance', 'Going Forward'. Canary initially >50% CPU and 20% latency degradation; subsequent 10–20% CPU degradation resolved by disabling incidental async. |
| N10 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://netflix.github.io/dgs/announcements/) | DGS Framework 'New and Noteworthy': 8.5.0 released March 29 2024; 10.0.0 Dec 17 2024, legacy removal and Netflix fleet migration reported. |
| N11 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://netflixtechblog.com/the-evolution-of-cassandra-data-movement-at-netflix-6e13329c80a1) | Netflix tech blog 'Evolution of Cassandra Data Movement': migration approach; inspect backup, shadow, cutover sections before numeric assertion. |
| N12 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://medium.com/netflix-techblog/dynamically-splitting-wide-partitions-in-cassandra-for-time-series-workloads-0eded064f456) | Netflix dynamic repartitioning time-series article: article body accessible; section-level technical claim extraction pending. |
| N13 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://medium.com/netflix-techblog/scaling-time-series-data-storage-part-i-ec2b6d44ba39) | Netflix 'Scaling Time Series Data Storage Part I': historical article body accessible; separate from later Cassandra change. |
| N14 | Netflix | BLOCKED — cannot admit | [original](https://netflixtechblog.com/netflix-conductor-the-next-chapter-41ad21067649) | Source reader returned an internal error; search for a reliable rehost or direct primary transcript; no claim admission |
| N15 | Netflix | BLOCKED — cannot admit | [original](https://medium.com/netflix-techblog/chaos-engineering-upgraded-878d341f15fa) | Medium primary link fetch failed; locate alternate first-party archived copy |
| N16 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905) | Netflix 'Evolution of the Netflix Data Pipeline': original body accessible; 2016-era architecture. |
| N17 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://netflixtechblog.com/data-projects-managing-data-assets-at-netflix-scale-7ca25888591e) | Netflix 'Data Projects Managing Data Assets': original body accessible; 2026 source, claims need bounded scope. |
| N18 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://netflixtechblog.com/seeing-through-hardware-counters-a-journey-to-threefold-performance-increase-2721924a2822) | Netflix 'Seeing through hardware counters': original body accessible; numeric performance only for specified workload. |
| N19 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://medium.com/netflix-techblog/how-we-build-code-at-netflix-c5d9bd727f15) | Netflix 'How We Build Code': first-party archive accessible, 2016 era only. |
| N20 | Netflix | ACCESSIBLE — claim-level gate pending | [original](https://sites.google.com/netflix.com/javaplatformnetflix/jvm) | Netflix JVM Ecosystem team homepage accessible; undated operational scope, not deployment outcome. |
| U01 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/microservice-architecture/) | Uber 'Introducing Domain-Oriented Microservice Architecture'; inspect 'DOMA' domain/layer/extensibility trade-off, 2020. |
| U02 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/mezzanine-codebase-data-migration/) | Uber 'Project Mezzanine: The Great Migration'; project-level datastore migration; exact operational gates require per-claim sourcing. |
| U03 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/mysql-to-myrocks-migration-in-uber-distributed-datastores/) | Uber 'MySQL to MyRocks Migration': distinct read/write, compaction and storage costs, 2022 context. |
| U04 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/continuous-deployment/) | Uber 'Continuous deployment for large monorepos': monorepo/CD modernization; not a blanket claim of all Uber code. |
| U05 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/migrating-functionality-between-production-systems/) | Original locale path returned error; **canonical link repaired** to https://www.uber.com/us/en/blog/migrating-functionality-between-production-systems/ ; article accessible, migration safety sections. |
| U06 | Uber | ACCESSIBLE — claim-level gate pending | [original](https://www.uber.com/us/en/blog/from-static-rate-limiting-to-intelligent-load-management/) | Uber 'From Static Rate-Limiting to Intelligent Load Management': first-party 2026 article; system-specific overload. |
| A01 | Airbnb | ACCESSIBLE — claim-level gate pending | [original](https://airbnb.tech/infrastructure/migrating-airbnbs-jvm-monorepo-to-bazel/) | Airbnb 'Migrating Airbnb’s JVM Monorepo to Bazel': original article accessible; multi-year build migration. |
| SH01 | Shopify | ACCESSIBLE — claim-level gate pending | [original](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) | Shopify 'Deconstructing the Monolith': original 2019-era modular architecture account; do not mislabel as microservices. |
| SH02 | Shopify | ACCESSIBLE — claim-level gate pending | [original](https://shopify.engineering/shopify-monolith) | Shopify 'Under Deconstruction': actual ongoing modularity effort; not proof of completely isolated components. |
| SH03 | Shopify | ACCESSIBLE — claim-level gate pending | [original](https://shopify.engineering/cloud-load-modular-code-shopify-2022) | Shopify 'Cloud, Load, and Modular Code': 2022 status and renderer extraction. |
| SH04 | Shopify | BLOCKED — cannot admit | [original](https://shopify.engineering/helix) | Shopify link /helix returned internal error; verify canonical article and publication date |
| SP01 | Spotify | ACCESSIBLE — claim-level gate pending | [original](https://engineering.atspotify.com/2020/6/tech-migrations-the-spotify-way) | Spotify 'Tech Migrations, the Spotify Way': 2020-06-25 Chakrabarti and Lee; sections 'Ruthlessly prioritize', 'Product-ify', 'Automate'. Long-tail and Backstage coordination. |
| SP02 | Spotify | BLOCKED — cannot admit | [original](https://www.engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) | Spotify www-engineering address returned cache miss; retry canonical engineering.atspotify.com |
| SP03 | Spotify | BLOCKED — cannot admit | [original](https://www.engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4) | Spotify www-engineering address returned cache miss; retry canonical engineering.atspotify.com |
| ST01 | Stripe | ACCESSIBLE — claim-level gate pending | [original](https://stripe.com/blog/online-migrations) | Stripe 'Online migrations at scale': original article accessible, migration phases; guard correctness and dual-representation compatibility. |
| ST02 | Stripe | ACCESSIBLE — claim-level gate pending | [original](https://stripe.com/blog/migrating-to-typescript) | Stripe article redirects to stripe.dev/blog/migrating-to-typescript; author Andrew Lunny, published 2022-05-20. |
| DI01 | Discord | ACCESSIBLE — claim-level gate pending | [original](https://discord.com/blog/how-discord-stores-trillions-of-messages) | Discord 'How Discord Stores Trillions of Messages': original article accessible; workload- and epoch-bound Cassandra/Scylla numbers. |
| DI02 | Discord | ACCESSIBLE — claim-level gate pending | [original](https://discord.com/blog/how-discord-indexes-trillions-of-messages) | Discord 'How Discord Indexes Trillions of Messages': original accessible, distinguish text-search requirements from primary message storage. |
| ME01 | Meta | ACCESSIBLE — claim-level gate pending | [original](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/) | Meta/Facebook 'TAO: The Power of the Graph': 2013-06-25 historical graph-serving account. |
| ME02 | Meta | ACCESSIBLE — claim-level gate pending | [original](https://engineering.fb.com/2013/04/15/core-infra/scaling-memcache-at-facebook/) | Meta/Facebook 'Scaling memcache at Facebook': 2013-04-15 historical cache layers. |
| ME03 | Meta | ACCESSIBLE — claim-level gate pending | [original](https://engineering.fb.com/2026/05/12/data-infrastructure/migrating-data-ingestion-systems-at-meta-scale/) | Meta 'Migrating Data Ingestion Systems at Meta Scale': first-party 2026-05-12 ingestion account. |
| LI01 | LinkedIn | ACCESSIBLE — claim-level gate pending | [original](https://engineering.linkedin.com/kafka/running-kafka-scale) | LinkedIn 'Running Kafka At Scale': historical operations report, no current cluster capacity implied. |
| CF01 | Cloudflare | ACCESSIBLE — claim-level gate pending | [original](https://blog.cloudflare.com/making-super-slurper-five-times-faster/) | Cloudflare 'Making Super Slurper 5x faster': migration workload experiment, not blanket performance guarantee. |

## Corrections that materially affect M9

1. **Uber U05 URL:** the original localized `www.uber.com/do/en/...` source was not readable. The US-English first-party URL in the table above was accessible and contains the production migration narrative. Update the original source register before any case is cited.
2. **Netflix N03 2026:** The public JavaOne **session abstract** explicitly reports its intended coverage and service fleet scale, but is not evidence for all the technical results potentially discussed in the full talk. Do not infer deployment outcomes from a schedule.
3. **Netflix N09 → N10 actual chronology:** April 2024 engineering article proposed phased DGS/Spring GraphQL integration; December 17, 2024 DGS 10.0.0 release notes subsequently report removing legacy modules and migrating Netflix services. Distinguish proposal from completed vendor-reported adoption.
4. **Netflix N09 adverse canary:** early HTTP implementation measured >50% extra CPU and ~20% slower latency before incremental fixes; after fixes there was still ~10–20% CPU overhead until asynchronous handling was disabled. This performance regression is an essential negative case—not a marketing-only success narrative.
5. **Spotify SP01 migration governance:** distinguish platform migration coordination and team autonomy from changes to JVM execution models.
6. **Blocked publications:** source-fetch errors are *not* proof that the original URL is nonexistent. Try alternate verified primary domains, paper/repo links or temporarily exclude; do not silently invent conclusions from their titles.
7. **Licensing:** even for accessible primary publications, hyperlinks and metadata are reusable as citations, while copying text, diagrams, screenshots or publisher figures is outside authorization. Record original authors and article section in final case claim ledger.
8. **Source dates:** derive dates from publisher page, event agenda or release announcement, NOT the discovery date. Undated living documentation (team pages, wiki) requires a pinned snapshot or inspection date and may not establish historical deployments.

## Definition of done for issue #114

For every eventual admitted source: stable ID, primary creator/publisher, original publication/event date, observed URL and redirect, exact claim-specific section/timestamp, historical version and workload, explicit source-reported-vs-independent classification, license/reuse limitation, negative/counterclaims, and source disposition. The 5 unresolved URLs and claim-level work on the other accessible sources keep **#114 OPEN**. A deferred source may remain excluded with a recorded reason; it must not silently be called verified.

## Reproduction scope

The audit relied on read-only retrieval of the listed official sites (including normalized permanent redirects). No credentials, private material, live experiments, performance logs, graph rebuild, CI run or external company's data were accessed. The evidence rows are a research navigation index; readers must follow each linked original source and validate the cited section at publication time before making quantitative engineering decisions.
