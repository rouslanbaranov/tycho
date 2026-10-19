---
metadata_version: 1
id: "tycho.landing.43b3f0c107e34e5a800d6c1de65069e8"
kind: "landing"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/cases/README.md"
title: "M9 — Historical Architecture Modernization Case Studies"
topic_ids:
  - "architecture-case-studies"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for M9 — Historical Architecture Modernization Case Studies. Scope includes Position inside the single Tycho book (M1–M9 integration); Netflix — Java and runtime (#115/#116/#117); Other companies (#118)."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of M9 — Historical Architecture Modernization Case Studies?"
  prerequisites: []
  related_ids:
    - "tycho.book.37c50125355948f1b52ec66229ef59bd"
    - "tycho.page.b95df0f6a3ee4355939f65193b11d8c9"
    - "tycho.page.ca73432e255443ca808b30f9587f20cb"
    - "tycho.page.8982b044f7ee4305a2330a6ff989bb77"
    - "tycho.page.5a4108bc167f4e2387dbf019eac7881e"
    - "tycho.page.8ece705ef365401395fd06585173b1f1"
    - "tycho.page.36d83a4c7ecb4d12b60fb814d605646a"
    - "tycho.page.a486e061c9564587b1e39a4e83024fca"
    - "tycho.page.6cdc8b405be542f29528e4cfd7454bc9"
    - "tycho.page.db99bd9dbe5c4058a286afaeb129f156"
    - "tycho.page.b256d263efff488c8cf549e116be9683"
    - "tycho.page.50b3410cae7d4032babb15542e748cac"
    - "tycho.page.cd9c135dbdad45e5937a41c6f70ec3d3"
    - "tycho.page.7419e7903c5549a6a9c7944f4214f7e1"
    - "tycho.page.b369cf77ebee40c6a35f45effefe473d"
    - "tycho.page.689c7d51faf1441caa7edfcb6152345e"
    - "tycho.page.3fb5e995d5c04cc4aa78b0bd95fcbfe6"
    - "tycho.page.aed8b635f57f41dfa63c897a8d1caca8"
    - "tycho.page.09cb313598ad41bbafd7b10d9b4e8018"
    - "tycho.page.5b4cd43052b647abb7cb161381ebdcc5"
    - "tycho.page.c766e3289b95429bb158fb168f7bd0b9"
    - "tycho.page.f0337e16699d4cd1be934cbbcfb5fa87"
    - "tycho.page.b55f5bf29d7946c78454a769980c476e"
    - "tycho.page.95bf2e08c056472f92faf870de8f1357"
    - "tycho.page.b9bdcfd7c9a84e2ba3dd446bae8e63c2"
    - "tycho.page.acfab58bfa6b470ca28010ac561dfeef"
    - "tycho.page.9fba18919c6c44cdbd6ba07b4825f1e2"
    - "tycho.page.1e37e65ac62345da9b836a32cc4eb6b9"
    - "tycho.page.0c8a001625a545c1bbfa56bcb89accc4"
    - "tycho.page.9f1f71a670f345e9898fe78167b48cda"
    - "tycho.decision.1c768ea76c334e82b00e98b955dcf7e9"
    - "tycho.decision.cb09e574f2a64060a6f46120394e398d"
    - "tycho.decision.054f312b9e744575ac80632f4acf72fa"
    - "tycho.decision.c089ea2f22f54b0ebbe9ebc3804a7e14"
    - "tycho.decision.54dff384ace3468490c46b1d00b0dcf6"
    - "tycho.decision.73ab83b8148a4061a1effab218d47b0b"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Historical"
    - "Architecture"
    - "Modernization"
    - "Case"
    - "Studies"
evidence_scope:
  source_ids: []
  claim_ids: []
  status: "unknown"
  notes: "Only exact URL matches to the global source register are normalized here. Page-local case and evidence ledger IDs remain in the body; no claim-level mapping or source inspection is inferred."
content_review:
  status: "draft"
  reviewed_at: null
  reviewer: null
  proof_uri: null
authored_at: "2026-10-19"
updated_at: "2026-10-20"
source_inspection_date: null
content_verified_at: null
---

# M9 — Historical Architecture Modernization Case Studies

## Purpose and mission

Use dated, first-party accounts to understand why a modernization approach fit
its original constraints, how its transition and failure boundaries worked,
and which evidence would justify or reject transferring it to a new system.
Start with the case families below, then compare their mechanisms through the
decision playbooks. Published outcomes remain source-reported historical
observations; the playbooks provide explicitly synthetic decision reasoning.

**Evidence state:** original author-reviewed **drafts**, not independent-reviewed/accepted Tycho cases. As of 2026-10-19 this collection contains **29** case pages: **12 Netflix** and **17 from 9 other organizations**. A publisher's architectural write-up is evidence of its historical account, not independent validation of an experiment. Do not represent the case counts as finished milestone acceptance until E16-01 and E16-08 gates pass.

## Position inside the single Tycho book (M1–M9 integration)

This existing M9 collection is now linked to the **69 canonical draft chapter owners** across Tycho's ten proposed volumes. It is an **applied casebook/reference layer of the same book**, not an eleventh conceptual volume, an independent book requiring another agent, or proof of publication acceptance. The [complete 29-case + six-playbook mapping](../../authoring/UNIFIED_BOOK_M1_M9_INTEGRATION.md) supplies proposed concept-to-case reading routes; readers can enter from [the main book](../README.md).

The foundational chapters explain **mechanisms and invariant conditions**; a historical case reports a **particular company's published experience** within a stated period; the decision playbooks are **Tycho's synthetic transfer reasoning**. Do not convert source-reported outcomes into universal benchmark claims. Both #213 and #121 stay open pending independent review, real validators and the graph-free MCP dependency disposition.

## Netflix — Java and runtime (#115/#116/#117)

- [Java service platform convergence](netflix-java-platform-convergence.md)
- [Durable identity and project-based data governance](netflix-data-project-durable-workload-identity.md)
- [Zuul 2 async gateway](netflix-zuul2-nonblocking-gateway.md)
- [DGS and Spring GraphQL](netflix-dgs-spring-graphql-convergence.md)
- [Java 21 virtual-thread pinning](netflix-java21-virtual-thread-pinning.md)
- [CPU-heavy gRPC worker-pool virtual-thread regression](netflix-grpc-cpu-workerpool-virtual-thread-regression.md)
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

**M9 implementation boundary:** Graph development and maintenance are stopped. Navigate these cases through stable document IDs, human-readable links, indexed metadata, source citations and bounded text retrieval; no graph schema, edge database or graph-aware MCP feature is required. Original Mermaid illustrations and historical case subjects such as GraphQL or Meta TAO do not constitute Tycho product graph support.

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
