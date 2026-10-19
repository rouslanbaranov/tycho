# M9 — Historical Architecture Modernization Case Studies

**Evidence state:** original author-reviewed **drafts**, not independent-reviewed/accepted Tycho cases. As of 2026-10-19 this collection contains **28** case pages: **11 Netflix** and **17 from 9 other organizations**. A publisher's architectural write-up is evidence of its historical account, not independent validation of an experiment. Do not represent the case counts as finished milestone acceptance until E16-01 and E16-08 gates pass.

## Netflix — Java and runtime (#115/#116/#117)

- [Java service platform convergence](netflix-java-platform-convergence.md)
- [Durable identity and project-based data governance](netflix-data-project-durable-workload-identity.md)
- [Zuul 2 async gateway](netflix-zuul2-nonblocking-gateway.md)
- [DGS and Spring GraphQL](netflix-dgs-spring-graphql-convergence.md)
- [Java 21 virtual-thread pinning](netflix-java21-virtual-thread-pinning.md)
- [Generational ZGC workload choice](netflix-generational-zgc-workloads.md)
- [HotSpot false/true sharing](netflix-hotspot-false-true-sharing.md)
- [Seven-year cloud rearchitecture](netflix-seven-year-cloud-rearchitecture.md)
- [Chaos Kong region-failure simulation and resilience](netflix-chaos-kong-regional-failover.md)
- [Casspactor shadow migration](netflix-casspactor-shadow-migration.md)
- [Cassandra TimeSeries dynamic split](netflix-cassandra-dynamic-time-series-splits.md)

## Other companies (#118)

- [Uber DOMA](uber-doma-domains.md)
- [Uber Mezzanine trip migration](uber-mezzanine-pg-to-schemaless.md)
- [Uber MyRocks](uber-mysql-to-myrocks.md)
- [Uber Cinnamon dynamic overload protection and fairness](uber-cinnamon-admission-and-fairness.md)
- [Shopify modular monolith](shopify-modular-monolith.md)
- [Shopify component governance](shopify-packwerk-boundary-evolution.md)
- [Shopify Helix gate-driven AI native migration](shopify-helix-checkpoint-gated-native-migration.md)
- [Airbnb Bazel JVM build migration](airbnb-jvm-monorepo-bazel.md)
- [Stripe online data migration](stripe-online-subscriptions-migration.md)
- [Discord ScyllaDB messages](discord-cassandra-scylladb-messages.md)
- [Discord search index cells](discord-search-index-cells.md)
- [Spotify long-tail platform migrations](spotify-tech-migration-long-tail.md)
- [Spotify Honk dataset-consumer migration and negative evidence](spotify-honk-data-consumer-migration.md)
- [Cloudflare queue-backed Super Slurper](cloudflare-super-slurper-queues.md)
- [Meta TAO graph serving](meta-tao-social-graph-serving.md)
- [Meta ingestion shadow lifecycle and cutover](meta-ingestion-shadow-migration-lifecycle.md)
- [LinkedIn audited Kafka tiers](linkedin-kafka-tiered-completeness.md)

## Reading and agent retrieval policy

Every document should be read with its original publication period, exact first-party article sections, claim uncertainty and counter-architectures. The cases contrast incompatible answers: Netflix's microservice/cloud move and Shopify's modular-monolith choice; Zuul 2 async connection scale and Java 21 virtual-thread incident; ZGC tail latency and Parallel GC batch throughput; storage engine swaps and incremental schema changes.

- Sources and access status: [initial company register](../../sources/REAL_WORLD_ARCHITECTURE_CASES.md), [43-source audit](../../sources/REAL_WORLD_CASES_CANDIDATE_AUDIT.md), [first Netflix claim ledger](../../sources/REAL_WORLD_CASES_ADMISSION_WAVE_01.md).
- Program and acceptance: [M9 case-study program](../../authoring/REAL_WORLD_CASE_STUDY_PROGRAM.md), [E16-01 #114](https://github.com/rouslanbaranov/tycho/issues/114), [E16-08 #121](https://github.com/rouslanbaranov/tycho/issues/121).
- The later first-party audit confirmed SH04/SP02/SP03; their bounded evidence is [admitted](../../sources/REAL_WORLD_CASES_PRIMARY_AGENT_MIGRATION_EVIDENCE.md). N14 still lacks direct-original article access (publisher-attributed syndication exists), and N15 remains unreadable. Never claim all original articles are verified. The Stripe TypeScript redirect currently exposes insufficient article body for substantive technical assertions; it is also excluded from case authoring.
- All Mermaid diagrams are newly authored conceptual schematics. Any reported performance numbers are explicitly scoped by source and period. No independent technical peer review or system benchmarks have yet been completed.

## Evidence-based architecture decision playbooks (E16-06)

Six cross-company, synthetic-decision guides are published as **drafts**; their ADRs are Tycho analyses, not historical decisions taken by the named companies.

- [Modular monolith vs microservices](decisions/monolith-vs-services.md) — Netflix / Shopify / Uber
- [Reactive, virtual threads and queue-based I/O](decisions/reactive-vs-virtual-threads.md) — Netflix / Cloudflare
- [JVM collector and tail-latency choice](decisions/gc-and-tail-latency.md) — Netflix / Discord
- [Correctness-first online data migration](decisions/data-migration-correctness.md) — Stripe / Netflix / Uber / Discord
- [Build platform and fleet adoption](decisions/build-delivery-migration.md) — Airbnb / Spotify / Uber
- [Agent-assisted modernization safety](decisions/agentic-migration-safety.md) — Spotify / Shopify / Stripe / Airbnb / Netflix; source-reported AI migrations and their explicit test gaps, no independent AI-agent defect-rate claim

Each decision guide has a synthetic starting state, evidence for contrasting real-world mechanisms, contraindications, an original ADR, rollback/insufficient-evidence branch, and a proposed transition.
