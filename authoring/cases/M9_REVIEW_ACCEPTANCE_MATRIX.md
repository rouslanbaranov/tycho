# M9 / E16-08 — Case Review Matrix and Acceptance Checkpoint

**Checkpoint:** 2026-10-19 · **Owner:** E16-08 #121 · **Status:** *mechanical/readability pre-review only*. This is NOT an independent technical review decision and NOT a certificate of complete M9. Data retrieved from Tycho `main` after source-intake #114; no CI, remote MCP queries, Java runtime or company production workloads executed.

## Scope frozen for this review preparation

- Source register: **43 unique candidates**, **41** with at least one bounded public claim or deliberately narrow publisher-scoped abstract/team-charter statement, **2 deferred** (N14 Conductor primary original not readable; ST02 Stripe TypeScript primary redirects to metadata). These two are **excluded from asserting technical outcomes**.
- Pages: **25** bounded original case drafts, including **10 Netflix** and **15 other-company** cases, indexed from `book/cases/README.md`.
- Comparisons: **6** case-backed synthetic decision playbooks, not company ADRs.
- Agent evaluation: **44** proposed retrieval test fixtures (14 answerable, 21 unsupported/false-claim rejection, 9 insufficient evidence) plus **2** example records and a Draft 2020-12 *proposed* JSON schema.
- Case-specific provenance: stable human-readable `case.*` IDs in all reviewed draft pages; first-party URL reference and Mermaid diagram present in each sampled path; no source article image imported.
- **No independent reviewer acceptance**, no production search/ranking/graph evaluation and no reproduced vendor metric are claimed.

## Mechanical pre-review results

| Check | Evidence / result | Status |
|---|---|---|
| Source register vs admission matrix | 43 registered source IDs correspond one-to-one with 43 audit rows, no duplicates; N14/ST02 explicitly deferred | **PASS** for identity/disposition |
| Case index | 25 pages individually fetched from `main`, stable `case.<company>.<slug>` IDs observed | **PASS** for presence/shape |
| Mermaid/Markdown structural check | In 25/25 case pages: ≥1 Mermaid block, paired backtick fences, first-party cited URL, review state clearly identified | **PASS** for observed text patterns; not a Mermaid renderer check |
| Decision corpus | Six linked comparison pages, each with synthetic constraints and at least two contrasting cases plus decision guardrails | **PASS** for existence, not substantive independent endorsement |
| Candidate-specific numeric evidence | Company 2013–2026 windows and negative results available in waves 01–08, including Netflix ZGC, Uber MyRocks, Discord, Airbnb, Shopify and Cloudflare | **PARTIAL**, high-risk numeric claims still require independent source-by-source review |
| Proposed schema/fixtures | 2 sample JSON records, 44 unique fixture IDs, 14/21/9 behavior groups; fixture source IDs from 43-source register | **STRUCTURAL PASS**, not full Python/schema engine run |
| Local Python validator | `scripts/validate_m9_cases.py` exists with negative tests and optional `jsonschema` | **NOT EXECUTED** against a full checked-out repository in this review |
| Source license and link reachability | URLs and reproduction warnings present; external URLs partly opened; publisher licensing beyond citation/paraphrase not granted | **LIMITED**; no bulk redistribution of vendor diagrams/text |
| Independent reviewer | No independent reviewer signoff or recorded source-specific verdict | **BLOCKED** |
| Live K10–K20 / MCP evaluation | Runtime ownership in core milestones, not available as integrated M9 transport | **DEFERRED**; 44 query fixtures are specifications, not measured hits |

## Case-by-case review matrix

| Review ID | Case file | Primary provenance IDs | Required semantic adversarial check | Acceptance |
|---|---|---|---|---|
| NF01 | [netflix-java-platform-convergence.md](../../book/cases/netflix-java-platform-convergence.md) | N02/N03/N04 | 2023 vs 2026 Java fleet; abstract not deployment | Draft; pending independent review |
| NF02 | [netflix-zuul2-nonblocking-gateway.md](../../book/cases/netflix-zuul2-nonblocking-gateway.md) | N07/N08 | CPU gain workload-specific; dynamic wiki revision unpinned | Draft; pending independent review |
| NF03 | [netflix-dgs-spring-graphql-convergence.md](../../book/cases/netflix-dgs-spring-graphql-convergence.md) | N09/N10 | 2024 initial CPU regression vs DGS10 later parity | Draft; pending independent review |
| NF04 | [netflix-java21-virtual-thread-pinning.md](../../book/cases/netflix-java21-virtual-thread-pinning.md) | N06 | Java21 only; 4 carriers, not permanent Loom ban | Draft; pending independent review |
| NF05 | [netflix-generational-zgc-workloads.md](../../book/cases/netflix-generational-zgc-workloads.md) | N05 | Generational vs non-generational ZGC, G1, Parallel distinct | Draft; pending independent review |
| NF06 | [netflix-hotspot-false-true-sharing.md](../../book/cases/netflix-hotspot-false-true-sharing.md) | N18 | 16→48 vCPU, false vs true sharing, fixed 55% CPU target | Draft; pending independent review |
| NF07 | [netflix-seven-year-cloud-rearchitecture.md](../../book/cases/netflix-seven-year-cloud-rearchitecture.md) | N01 | 2008 trigger to Jan 2016, company retrospective not A/B | Draft; pending independent review |
| NF08 | [netflix-chaos-kong-regional-failover.md](../../book/cases/netflix-chaos-kong-regional-failover.md) | N15 | Chaos Kong historical 2015; failover not availability guarantee | Draft; pending independent review |
| NF09 | [netflix-casspactor-shadow-migration.md](../../book/cases/netflix-casspactor-shadow-migration.md) | N11 | Two-sided set comparison, shadow and fallback | Draft; pending independent review |
| NF10 | [netflix-cassandra-dynamic-time-series-splits.md](../../book/cases/netflix-cassandra-dynamic-time-series-splits.md) | N12 | Partition split checksum and fallback vs future time slice | Draft; pending independent review |
| UB01 | [uber-doma-domains.md](../../book/cases/uber-doma-domains.md) | U01 | Historical service sprawl, domain gateway not arbitrary service split | Draft; pending independent review |
| UB02 | [uber-mezzanine-pg-to-schemaless.md](../../book/cases/uber-mezzanine-pg-to-schemaless.md) | U02 | 2014 trip storage, API/ID seam; not 2020 DOMA | Draft; pending independent review |
| UB03 | [uber-mysql-to-myrocks.md](../../book/cases/uber-mysql-to-myrocks.md) | U03 | MySQL 8 preparatory migration >1yr, read/space trade-off | Draft; pending independent review |
| SH01 | [shopify-modular-monolith.md](../../book/cases/shopify-modular-monolith.md) | SH01 | Modular monolith decision not proof zero services | Draft; pending independent review |
| SH02 | [shopify-packwerk-boundary-evolution.md](../../book/cases/shopify-packwerk-boundary-evolution.md) | SH02 | Component work incomplete by 2020; graph cycle exceptions | Draft; pending independent review |
| SH03 | [shopify-helix-checkpoint-gated-native-migration.md](../../book/cases/shopify-helix-checkpoint-gated-native-migration.md) | SH04 | Shop shipped vs Shopify App underway, default approval | Draft; pending independent review |
| AB01 | [airbnb-jvm-monorepo-bazel.md](../../book/cases/airbnb-jvm-monorepo-bazel.md) | A01 | Multi-year rollout, runtime parity, self-reported performance | Draft; pending independent review |
| ST01 | [stripe-online-subscriptions-migration.md](../../book/cases/stripe-online-subscriptions-migration.md) | ST01 | Read/write authority sequencing and online correctness | Draft; pending independent review |
| DI01 | [discord-cassandra-scylladb-messages.md](../../book/cases/discord-cassandra-scylladb-messages.md) | DI01 | Sample read equality vs full migration, tombstones | Draft; pending independent review |
| DI02 | [discord-search-index-cells.md](../../book/cases/discord-search-index-cells.md) | DI02 | Search indexing p99 cannot conflate with message DB p99 | Draft; pending independent review |
| SP01 | [spotify-tech-migration-long-tail.md](../../book/cases/spotify-tech-migration-long-tail.md) | SP01 | 2020 non-LLM process; 99% hidden migrations was aspiration | Draft; pending independent review |
| SP02 | [spotify-honk-data-consumer-migration.md](../../book/cases/spotify-honk-data-consumer-migration.md) | SP02/SP03 | 240 rolled-out PRs != merged; 1,800 are dependencies | Draft; pending independent review |
| CF01 | [cloudflare-super-slurper-queues.md](../../book/cases/cloudflare-super-slurper-queues.md) | CF01 | 5x benchmark 75k objects; queue duplicate/idempotency | Draft; pending independent review |
| ME01 | [meta-tao-social-graph-serving.md](../../book/cases/meta-tao-social-graph-serving.md) | ME01 | 2013 graph association serving, eventual consistency default | Draft; pending independent review |
| LI01 | [linkedin-kafka-tiered-completeness.md](../../book/cases/linkedin-kafka-tiered-completeness.md) | LI01 | 2015 cluster counts not current; audit totals not event equality | Draft; pending independent review |

## Comparative playbook review matrix

| Decision file | Contrasting companies | Adversarial assertion to reject | Acceptance |
|---|---|---|---|
| [monolith-vs-services.md](../../book/cases/decisions/monolith-vs-services.md) | Netflix / Shopify / Uber | Company decisions are not same-workload A/B | Draft; requires reviewer approval |
| [reactive-vs-virtual-threads.md](../../book/cases/decisions/reactive-vs-virtual-threads.md) | Netflix / Cloudflare | Scheduling mechanisms at different abstraction layers | Draft; requires reviewer approval |
| [gc-and-tail-latency.md](../../book/cases/decisions/gc-and-tail-latency.md) | Netflix / Discord | A latency SLO cannot be replaced by batch throughput | Draft; requires reviewer approval |
| [data-migration-correctness.md](../../book/cases/decisions/data-migration-correctness.md) | Stripe / Netflix / Uber / Discord | Two-sided diff != all business semantic correctness | Draft; requires reviewer approval |
| [build-delivery-migration.md](../../book/cases/decisions/build-delivery-migration.md) | Airbnb / Spotify / Uber | Build speed != fleet adoption | Draft; requires reviewer approval |
| [agentic-migration-safety.md](../../book/cases/decisions/agentic-migration-safety.md) | Shopify / Spotify / Stripe / Netflix | Generated/merged PR != verified defect-free change | Draft; requires reviewer approval |

## Independent reviewer checklist and non-negotiable gates

A qualified reviewer other than the author must independently examine **every** numerical assertion, version/date boundary, omitted contradictory result and performance denominator against the cited original document **section/talk timestamp**. Pay special attention to:

1. Netflix 2023 QCon Java report vs the **2026 JavaOne abstract**; neither should be interpreted as the other's production state.
2. Virtual-thread pinning with 4-core Java21 tracing/Brave locks vs a universal claim about newer JDKs; the source's incident does not establish a later runtime outcome.
3. DGS/Spring GraphQL early **>50% CPU / ~20% latency regression** and later documented change; avoid reporting only end-state success.
4. Discord Cassandra→Scylla **message store** vs separate Discord Elasticsearch **search-cell index**, each with its own denominators and product requirements.
5. Spotify 2025/2026 Honk: distinguish **>1,500 merged PRs** overall from **240 rolled-out dataset PRs**, 1,800 affected pipeline scope and excluded Scio class.
6. Shopify Helix **Shop app** shipped vs separate Shopify App incomplete; status not a 100%-fleet migration claim.
7. Shopify modular monolith strategy coexists with selected storefront service extraction; never say modular monolith means no standalone services.
8. Cloudflare bulk-copy **75,000 objects** speedup is one test, and Queues at-least-once semantics demand idempotency.
9. Uber MyRocks storage saving depends on disk/SQL compatibility and precedes a **MySQL 5.7→8.0 migration that took over a year**.
10. Any source with metadata-only admission or an undated living wiki may justify a chapter's *scope* but not detailed deployment/revision assertions.
11. All company diagrams are original Tycho simplifications, not copyright-reproduced original schematics; verify that no long article quotation slipped into case body.
12. No private Adro/employer sources or corpus cross-indexing; `tycho-public` collection boundary remains explicit.

## Proposed 44-query evaluation execution, when a real service is available

Evaluate all 44 fixture questions with answer **plus citation fidelity**, not just retrieval count. Record case hits, false-claim refusal, temporal contradiction handling, source URL and claim anchor, token/tool budget and p95 response time. Do not fabricate measured ranks or executed MCP results. Synthetic incorrect claims (e.g., 'Netflix removed all RxJava', 'Shopify completed all modularization', '240 Spotify PRs merged') **must be rejected**.

A reviewer should produce a signed/verifiable matrix with case file, claim ID, original-source section, observation period, correctness verdict, major/medium/minor severity, fix commit, numeric denominator verification, and explicit signoff. If any case lacks this evidence, leave it in draft and keep #121/M9 open.

## Decision as of this checkpoint

**Accepted mechanically:** existence of 25 well-scoped drafts, 6 guides, source ID mapping, 44 proposed fixtures.  
**Not accepted:** final external-source semantic review of all pages, complete production search evaluation, independently reproduced performance, external review signoff.  
**Milestone M9:** **OPEN — acceptance gate E16-08 not met**. This is an evidence-grounded delivery checkpoint, not a license to claim finished architecture modernization transfer.
