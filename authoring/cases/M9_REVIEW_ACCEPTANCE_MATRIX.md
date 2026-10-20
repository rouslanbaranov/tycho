# M9 / E16-08 — Case Review Matrix and Acceptance Checkpoint

> **Current-state overlay — 2026-10-20 (unmerged PR #218):** The older 'do not close #121/M9' and 'PR #212 Draft' statements are historical, from before owner-scoped integrated-draft acceptance and #216 merge. M9 #121 is now CLOSED. Do not invent a named external reviewer or a new independent claim-by-claim certificate. The 35 applied items remain 29 historical cases plus six synthetic decision playbooks. See [canonical project state](../STATE.md) and [reconciliation](../PROJECT_STATUS_RECONCILIATION_2026-10-20.md).


## Current M9 package disposition — 2026-10-20

Independent acceptance is **COMPLETED, owner-confirmed** for the integrated
manuscript including the 29 cases and six decision playbooks. Visual rendering
and live MCP checks are **CANCELLED by the owner**. See the binding
[acceptance disposition](../ACCEPTANCE_DISPOSITION_2026-10-20.md). The actual
M9 validator, self-test and all 17 M9 unit tests passed on the accepted pinned
revision. Earlier pending/blocked rows below are historical pre-review states,
not current blockers for these disposed gates. No live MCP run, external
reviewer identity or per-case inspection report is invented by this update.

**Checkpoint:** 2026-10-19 · **Owner:** E16-08 #121 · **Status:** *mechanical/readability pre-review only*. This is NOT an independent technical review decision and NOT a certificate of complete M9. Data retrieved from Tycho `main` after source-intake #114; no CI, remote MCP queries, Java runtime or company production workloads executed.

## Integrated-branch evidence checkpoint — 2026-10-19

**Scoped publisher comparison:** [M9 Shopify first-party source spot-check](M9_SHOPIFY_SOURCE_SPOTCHECK_2026-10-19.md) reopened src.m9-sh01 (2019-02-21) and src.m9-sh02 (2020-09-16) and checked **12 bounded historical assertions** represented in the [modular-monolith](../../book/cases/shopify-modular-monolith.md) and [Packwerk](../../book/cases/shopify-packwerk-boundary-evolution.md) drafts, also relevant to the [monolith-versus-services comparison](../../book/cases/decisions/monolith-vs-services.md). A misleading introductory suggestion that domain enforcement was already complete in 2019 was **corrected** to reflect the ongoing rollout and later incomplete 2020 component state. Other selected source statements matched publisher-scoped sections and periods; **no independent qualified human technical/copyright review, license clearance, controlled benchmark or 2026 topology was established**.

**Whole-book static cross-check:** [pinned integrated source scan](../INTEGRATED_BOOK_STATIC_CHECKPOINT_2026-10-19.md) fetched **136/136 Markdown files under book** at commit `ff88fe334050c6e429941cb514bdd02150fa6be2`; scanned 1,623 link occurrences with no missing local file targets and found no single-H1 or odd-backtick-fence anomalies. This did **not** run the Python premerge/M9 validators, resolve anchors, render Mermaid or verify external sources. Because Shopify content was edited after that pinned scan, rerun whole-tree validators on the eventual integration release candidate.

**Verdict:** progress in bounded source review, **not acceptance**. All 29 case studies and six decision guides still require actual reviewer verdicts. **#121 and M9 remain OPEN**, with **60 real end-to-end MCP scenarios or formally approved waiver** still outstanding; curated graph work remains excluded.

## Second bounded first-party check — Uber DOMA (2026-10-19)

[Eleven narrow Uber DOMA historical/quantitative assertions](M9_UBER_DOMA_SOURCE_SPOTCHECK_2026-10-19.md) were rechecked against the directly published [July 23, 2020 first-party article](https://www.uber.com/us/en/blog/microservice-architecture/): reported **~2,200 services organized into 70 domains, roughly half implemented**, cited 50-services/12-teams incident, one 10-touchpoint integration, five layers, gateway/extension mechanisms, reported 25–50% onboarding change, one three-day-to-three-hour consumer integration, 1.5-year fleet half-life estimate and two platform rewrites behind gateways. The source comparison found no contradiction in these specific publisher-qualified claims. The [Uber case](../../book/cases/uber-doma-domains.md) now links the source review. The Uber-versus-Shopify interpretation in Tycho's playbook remains **Tycho inference**, not a common A/B trial or a 2026 topology report.

**Acceptance unchanged:** source-specific AI-assisted spot checks are not qualified independent human review, copyright reuse/rights clearance or runtime experiment. No case marked independently accepted; 60 MCP evaluation scenarios and pinned full Python validators remain unexecuted; graph features remain excluded.

## Scope frozen for this review preparation

- Source register: **43 unique candidates**, **41** with at least one bounded public claim or deliberately narrow publisher-scoped abstract/team-charter statement, **2 deferred** (src.m9-n14 Conductor primary original not readable; src.m9-st02 Stripe TypeScript primary redirects to metadata). These two are **excluded from asserting technical outcomes**.
- Pages: **29** bounded original case drafts, including **12 Netflix** and **17 other-company** cases, indexed from `book/cases/README.md`.
- Comparisons: **6** case-backed synthetic decision playbooks, not company ADRs.
- Agent evaluation: **60** proposed retrieval test fixtures (21 answerable, 26 unsupported/false-claim rejection, 13 insufficient evidence) plus **2** example records and a Draft 2020-12 *proposed* JSON schema.
- Case-specific provenance: stable human-readable `case.*` IDs in all reviewed draft pages; first-party URL reference and Mermaid diagram present in each sampled path; no source article image imported.
- **No independent reviewer acceptance**, no production search/ranking/graph evaluation and no reproduced vendor metric are claimed.

## Mechanical pre-review results

| Check | Evidence / result | Status |
|---|---|---|
| Source register vs admission matrix | 43 registered source IDs correspond one-to-one with 43 audit rows, no duplicates; src.m9-n14/src.m9-st02 explicitly deferred | **PASS** for identity/disposition |
| Case index | 29 pages individually fetched from `main`, stable `case.<company>.<slug>` IDs observed | **PASS** for presence/shape |
| Mermaid/Markdown structural check | In 29/29 case pages: ≥1 Mermaid block, paired backtick fences, first-party cited URL, review state clearly identified | **PASS** for observed text patterns; not a Mermaid renderer check |
| Decision corpus | Six linked comparison pages, each with synthetic constraints and at least two contrasting cases plus decision guardrails | **PASS** for existence, not substantive independent endorsement |
| Candidate-specific numeric evidence | Company 2013–2026 windows and negative results available in waves 01–08, including Netflix ZGC, Uber MyRocks, Discord, Airbnb, Shopify and Cloudflare | **PARTIAL**, high-risk numeric claims still require independent source-by-source review |
| Proposed schema/fixtures | 2 sample JSON records, 60 unique fixture IDs, 21/26/13 behavior groups; fixture source IDs from 43-source register | **STRUCTURAL PASS**, not full Python/schema engine run |
| Local Python validator | `scripts/validate_m9_cases.py` exists with negative tests and optional `jsonschema` | **NOT EXECUTED** against a full checked-out repository in this review |
| Source license and link reachability | URLs and reproduction warnings present; external URLs partly opened; publisher licensing beyond citation/paraphrase not granted | **LIMITED**; no bulk redistribution of vendor diagrams/text |
| Independent reviewer | No independent reviewer signoff or recorded source-specific verdict | **BLOCKED** |
| Live K10–K20 / MCP evaluation | Runtime ownership in core milestones, not available as integrated M9 transport | **DEFERRED**; 60 query fixtures are specifications, not measured hits |

## Case-by-case review matrix

| Review ID | Case file | Primary provenance IDs | Required semantic adversarial check | Acceptance |
|---|---|---|---|---|
| NF01 | [netflix-java-platform-convergence.md](../../book/cases/netflix-java-platform-convergence.md) | src.m9-n02/src.m9-n03/src.m9-n04 | 2023 vs 2026 Java fleet; abstract not deployment | Draft; pending independent review |
| NF11 | [netflix-data-project-durable-workload-identity.md](../../book/cases/netflix-data-project-durable-workload-identity.md) | src.m9-n17 | Durable project identity vs overbroad grants; future rightsizing still planned | Draft; pending independent review |
| NF02 | [netflix-zuul2-nonblocking-gateway.md](../../book/cases/netflix-zuul2-nonblocking-gateway.md) | src.m9-n07/src.m9-n08 | CPU gain workload-specific; dynamic wiki revision unpinned | Draft; pending independent review |
| NF03 | [netflix-dgs-spring-graphql-convergence.md](../../book/cases/netflix-dgs-spring-graphql-convergence.md) | src.m9-n09/src.m9-n10 | 2024 initial CPU regression vs DGS10 later parity | Draft; pending independent review |
| NF04 | [netflix-java21-virtual-thread-pinning.md](../../book/cases/netflix-java21-virtual-thread-pinning.md) | src.m9-n06 | Java21 only; 4 carriers, not permanent Loom ban | Draft; pending independent review |
| NF12 | [netflix-grpc-cpu-workerpool-virtual-thread-regression.md](../../book/cases/netflix-grpc-cpu-workerpool-virtual-thread-regression.md) | src.m9-n02, QCon 2023 | CPU-bound outbound gRPC pool got a few percent slower on virtual threads; qualitative, not exact benchmark; distinct from 2024 tracing pinning | Draft; pending independent review |
| NF05 | [netflix-generational-zgc-workloads.md](../../book/cases/netflix-generational-zgc-workloads.md) | src.m9-n05 | Generational vs non-generational ZGC, G1, Parallel distinct | Draft; pending independent review |
| NF06 | [netflix-hotspot-false-true-sharing.md](../../book/cases/netflix-hotspot-false-true-sharing.md) | src.m9-n18 | 16→48 vCPU, false vs true sharing, fixed 55% CPU target | Draft; pending independent review |
| NF07 | [netflix-seven-year-cloud-rearchitecture.md](../../book/cases/netflix-seven-year-cloud-rearchitecture.md) | src.m9-n01 | 2008 trigger to Jan 2016, company retrospective not A/B | Draft; pending independent review |
| NF08 | [netflix-chaos-kong-regional-failover.md](../../book/cases/netflix-chaos-kong-regional-failover.md) | src.m9-n15 | Chaos Kong historical 2015; failover not availability guarantee | Draft; pending independent review |
| NF09 | [netflix-casspactor-shadow-migration.md](../../book/cases/netflix-casspactor-shadow-migration.md) | src.m9-n11 | Two-sided set comparison, shadow and fallback | Draft; pending independent review |
| NF10 | [netflix-cassandra-dynamic-time-series-splits.md](../../book/cases/netflix-cassandra-dynamic-time-series-splits.md) | src.m9-n12 | Partition split checksum and fallback vs future time slice | Draft; pending independent review |
| UB01 | [uber-doma-domains.md](../../book/cases/uber-doma-domains.md) | src.m9-u01 | Historical service sprawl, domain gateway not arbitrary service split | Draft; pending independent review |
| UB04 | [uber-cinnamon-admission-and-fairness.md](../../book/cases/uber-cinnamon-admission-and-fairness.md) | src.m9-u06 | Failed query-tier quotas vs PID/storage-local enforcement; 5,400/3,000 QPS context | Draft; pending independent review |
| UB02 | [uber-mezzanine-pg-to-schemaless.md](../../book/cases/uber-mezzanine-pg-to-schemaless.md) | src.m9-u02 | 2014 trip storage, API/ID seam; not 2020 DOMA | Draft; pending independent review |
| UB03 | [uber-mysql-to-myrocks.md](../../book/cases/uber-mysql-to-myrocks.md) | src.m9-u03 | MySQL 8 preparatory migration >1yr, read/space trade-off | Draft; pending independent review |
| src.m9-sh01 | [shopify-modular-monolith.md](../../book/cases/shopify-modular-monolith.md) | src.m9-sh01 | Modular monolith decision not proof zero services | Draft; pending independent review |
| src.m9-sh02 | [shopify-packwerk-boundary-evolution.md](../../book/cases/shopify-packwerk-boundary-evolution.md) | src.m9-sh02 | Component work incomplete by 2020; graph cycle exceptions | Draft; pending independent review |
| src.m9-sh03 | [shopify-helix-checkpoint-gated-native-migration.md](../../book/cases/shopify-helix-checkpoint-gated-native-migration.md) | src.m9-sh04 | Shop shipped vs Shopify App underway, default approval | Draft; pending independent review |
| AB01 | [airbnb-jvm-monorepo-bazel.md](../../book/cases/airbnb-jvm-monorepo-bazel.md) | src.m9-a01 | Multi-year rollout, runtime parity, self-reported performance | Draft; pending independent review |
| src.m9-st01 | [stripe-online-subscriptions-migration.md](../../book/cases/stripe-online-subscriptions-migration.md) | src.m9-st01 | Read/write authority sequencing and online correctness | Draft; pending independent review |
| src.m9-di01 | [discord-cassandra-scylladb-messages.md](../../book/cases/discord-cassandra-scylladb-messages.md) | src.m9-di01 | Sample read equality vs full migration, tombstones | Draft; pending independent review |
| src.m9-di02 | [discord-search-index-cells.md](../../book/cases/discord-search-index-cells.md) | src.m9-di02 | Search indexing p99 cannot conflate with message DB p99 | Draft; pending independent review |
| src.m9-sp01 | [spotify-tech-migration-long-tail.md](../../book/cases/spotify-tech-migration-long-tail.md) | src.m9-sp01 | 2020 non-LLM process; 99% hidden migrations was aspiration | Draft; pending independent review |
| src.m9-sp02 | [spotify-honk-data-consumer-migration.md](../../book/cases/spotify-honk-data-consumer-migration.md) | src.m9-sp02/src.m9-sp03 | 240 rolled-out PRs != merged; 1,800 are dependencies | Draft; pending independent review |
| src.m9-cf01 | [cloudflare-super-slurper-queues.md](../../book/cases/cloudflare-super-slurper-queues.md) | src.m9-cf01 | 5x benchmark 75k objects; queue duplicate/idempotency | Draft; pending independent review |
| src.m9-me02 | [meta-ingestion-shadow-migration-lifecycle.md](../../book/cases/meta-ingestion-shadow-migration-lifecycle.md) | src.m9-me03 | Shadow row counts/checksums vs business truth; 100% transition is company reported | Draft; pending independent review |
| src.m9-me01 | [meta-tao-social-graph-serving.md](../../book/cases/meta-tao-social-graph-serving.md) | src.m9-me01 | 2013 graph association serving, eventual consistency default | Draft; pending independent review |
| src.m9-li01 | [linkedin-kafka-tiered-completeness.md](../../book/cases/linkedin-kafka-tiered-completeness.md) | src.m9-li01 | 2015 cluster counts not current; audit totals not event equality | Draft; pending independent review |

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

## Proposed 60-query evaluation execution, when a real service is available

Evaluate all 60 fixture questions with answer **plus citation fidelity**, not just retrieval count. Record case hits, false-claim refusal, temporal contradiction handling, source URL and claim anchor, token/tool budget and p95 response time. Do not fabricate measured ranks or executed MCP results. Synthetic incorrect claims (e.g., 'Netflix removed all RxJava', 'Shopify completed all modularization', '240 Spotify PRs merged') **must be rejected**.

A reviewer should produce a signed/verifiable matrix with case file, claim ID, original-source section, observation period, correctness verdict, major/medium/minor severity, fix commit, numeric denominator verification, and explicit signoff. If any case lacks this evidence, leave it in draft and keep #121/M9 open.

## Decision as of this checkpoint

**Accepted mechanically:** existence of 29 well-scoped drafts, 6 guides, source ID mapping, 60 proposed fixtures.  
**Not accepted:** final external-source semantic review of all pages, complete production search evaluation, independently reproduced performance, external review signoff.  
**Milestone M9:** **OPEN — E16-08 independent review and live-evaluation gates not met**. This is an evidence-grounded delivery checkpoint, not a license to claim finished architecture modernization transfer.

## Addendum: October 19, 2026 — expanded coverage

Merged [case batch #168](https://github.com/rouslanbaranov/tycho/pull/168) added durable Netflix Data Projects identity, Uber Cinnamon overload control and Meta's shadow-validated ingestion transition. This checkpoint **mechanically inspected** each new page's case ID, original-source link and paired Mermaid fence, bringing observed presence checks to 29/29. It did **not** independently verify security-token semantics, Uber PID benchmarks or Meta checksum equivalence. A human reviewer should start from the new rows above and record evidence-specific verdicts separately.

## Evaluation checkpoint — public case retrieval 60-query set

After [PR #170](https://github.com/rouslanbaranov/tycho/pull/170) and [PR #176](https://github.com/rouslanbaranov/tycho/pull/176), the proposed decision-retrieval fixture set has **60 unique IDs**: **21 answerable, 26 reject unsupported/false claims, 13 return insufficient evidence**. Manual structural checks found no foreign-source ID or unknown case ID in the expected results; references resolve to the existing 43 registered public sources and 29 indexed case identities. **These checks are not a live retrieval/evidence benchmark:** no search results, ranking relevance, MCP answer citation fidelity, latency or token cost have been measured. K18–K23 implementation and runtime validation are separate dependencies; keep #121 open until a genuine reviewer and applicable execution proof exist.

## Second review checkpoint — 29 cases and 60 scenarios

[PR #174](https://github.com/rouslanbaranov/tycho/pull/174) added the 2023 Netflix CPU-intensive outgoing gRPC client worker-pool virtual-thread *negative result* as a separate src.m9-n02 case from the 2024 tracing pinning incident src.m9-n06. [PR #176](https://github.com/rouslanbaranov/tycho/pull/176) linked this evidence into the cross-company concurrency ADR and added four expectation fixtures (Q57–Q60). The current proposed set is **60**: **21** answerable, **26** false-claim rejection and **13** insufficient-evidence. Repository content was checked manually through connected GitHub for 29 case IDs, original diagrams/paired fences, source links and 60 distinct fixture IDs from the public source register. All current **authoring issues #115–#119 are marked complete**, while **#121 stays open** for independent technical, licensing and temporal verification and genuine retrieval runtime execution. The draft state of every page remains unchanged. No real MCP score or external benchmark can be inferred from these structural checks.

## Reopening #121 after unsupported closure — acceptance integrity

On **2026-10-19 at 12:35:18 UTC**, GitHub recorded issue #121 closed, but its two evidence comments and this matrix continued to identify absent independent reviewer signoff and absent actual 60-fixture search/MCP execution. No documented independent verdict or live evaluation artifacts accompanied that closure. The issue was reopened to preserve the acceptance gate. This does **not** invalidate completed authoring deliverables #114–#120; it separates drafted, structurally tested case knowledge from independently accepted knowledge.

**Completion requires evidence, not a closed GitHub status:** a named independent reviewer with case-by-case claim/source/date/copyright/contradiction verdicts (or an explicitly authorized independent evaluation process), correction of high-severity findings, executable offline checks with pinned revision and outputs, and a documented disposition for live integration tests depending on the K18–K23 runtime. If a prerequisite runtime does not exist, the exception/dependency must be transparently decided by the milestone owner rather than reporting imaginary MCP results. Count truth is **60 = 21 answerable + 26 false-claim refusals + 13 insufficient-evidence**. No Scheduled Tasks were enabled for this review.


## Offline search candidate baseline — executable diagnostic, not MCP acceptance

Merged [M9 BM25 pilot](M9_BM25_CANDIDATE_BASELINE_2026-10-19.md) used 29 Markdown case drafts as an offline document-level lexical corpus and the **existing 60** fixture questions as inputs. Of 57 questions with at least one expected case, **48** placed one gold candidate at rank 1 (**84.2%**) and **55** did so within top 3 (**96.5%**); gold-pair recall@3 was **89.6%**. For the **21 answerable questions**, 20 had at least one expected case at rank ≤3. The result is **not a retrieval-pipeline acceptance test**: it uses a self-authored relevance set, does not assess model answers, refusals, provenance citation fidelity, token/latency cost or K18–K23 MCP. Query `m9-q042` misses its two author-labelled cases at top 3 but retrieves other plausibly relevant migration evidence, which must be independently adjudicated rather than silently changing labels to improve scores.

Actual run: connected-tool JS, with a captured machine-readable [per-question result](M9_BM25_CANDIDATE_BASELINE_2026-10-19.json). Reproduction script: `scripts/evaluate_m9_case_bm25.py`, added to main but **not yet executed in a full local checkout**. The earlier schema sample verification was **executed** in isolated Python on two manually transferred GitHub JSON records and 10 negative variants; not a byte-verified checkout run. Keep #121 open while real independent technical review and runtime search evaluation are absent.

## Verified core retrieval/MCP dependency gate — 2026-10-19

The exact still-open original Tycho service dependencies and no-waiver acceptance boundary are documented in [M9 search/MCP dependencies](M9_SEARCH_MCP_DEPENDENCIES_2026-10-19.md). E07 index #49 / ranked search #50 / evidence resolution #51 and E09 MCP adapter #57 (and follow-on graph/onboarding/client issues) are not yet an available deployed M9 retrieval service. [Core PR #188](https://github.com/rouslanbaranov/tycho/pull/188) is a section-index **prototype**, not 60 live MCP question runs. The offline 29-case BM25 diagnostic is real but measures document-level candidate retrieval only. **No independent-review or full-toolchain success must be inferred from a prototype or a closed status.**

## Content-first completion policy — 2026-10-19

The user set **100% substantive case-page coverage as M9's highest priority**. The current 29 cases and six decision guides are **not** individually certified content-complete by the existing presence/shape checks. For each case, assess published baseline, workload and owners, trigger, considered alternatives (clearly separate historical from Tycho-analytical), migration and compatibility phases, failure/rollback and negative results, measured outcomes including date/unit/denominator, counterexamples, applicability prerequisites, source-section citations, and falsifiable independent review. For comparisons, require disqualifying conditions, reversible transition strategies, data quality/operational checks and an explicit insufficient-evidence outcome. Log unavailable facts as gaps instead of inventing content.

**Graph-related checks and deliverables are retired for all M9 acceptance.** No case graph, graph edge catalogue, graph-aware MCP API, graph freshness/version checks or graph infrastructure maintenance will be requested or accepted as new M9 work. Preserve stable IDs, canonical Markdown links, versioned source provenance and text/section search, per [accepted ADR](../ADR-RETIRE-CURATED-KNOWLEDGE-GRAPH.md). Native diagrams and published case studies about graph-based systems remain legitimate explanatory material. Historical graph references elsewhere in the milestone are superseded by this decision.

Do not equate “all 29 pages exist”, “all issues closed” or an approximate word count with 100% content. Independent acceptance of exact external claims remains a separate outstanding gate. No full-repository tests, complete case review or executed agent benchmark are asserted by this policy update.

## M9 page-depth checkpoint — content improvement wave, 2026-10-19

The linked [PR #212](https://github.com/rouslanbaranov/tycho/pull/212) improves seven previously existing case chapters and one existing decision guide while applying the graph-retirement requirement. It does not replace the prior **29-case/6-guide existence check** with independent acceptance. The chapter-level improvements below were authored from first-party public accounts and include additional observed historical phases, incompatibilities, negative outcomes, and separate synthetic migration controls:

| Expanded chapter | New substantive coverage | Remaining gate |
|---|---|---|
| Netflix Java convergence | Distinct JVM/framework/API-composition phases, Java 17 CPU context, cross-service compatibility and reversible fleet rollout | Independent primary metric/compatibility review |
| Netflix DGS/Spring GraphQL | 8.5.0 opt-in to 10.0.0, async-filter regressions, deleted modules and subscription migration concerns | Independent release-claim and numerical review |
| Netflix Generational ZGC | Collector comparisons, pause/retry amplification, native memory, reference handling and THP | Independent original blog figure/denominator review |
| Uber DOMA | 2,200 services/70 domains with partial adoption, layer/gateway/extension contracts and company-reported outcome limits | Independent historic benefit and timeline review |
| Shopify modular monolith | 2017 componentization, mechanical file move and history cost, contrasted 2020 partial ownership and service exceptions | Independent source/temporal review |
| Shopify component enforcement | Wedge-to-Packwerk differences, rigid-rule failure, ownership-first versus isolation-first and incomplete rollout | Independent technical and provenance review |
| LinkedIn Kafka tiers | Audit instrumentation across producer, mirrors, consumers; 2015 dated scale, counted-versus-identical-event caveat | Independent numeric/date and Kafka semantics review |
| Agent-assisted migration decision playbook | Correctness oracles, explicit stop states, staged code/data migration and human acceptance | Independent review of transferred applicability |

**Result of this wave:** **7 of 29** case pages and **1 of 6** decision pages substantively expanded; this ratio **does not represent the percentage of pages that are 100%-complete or independently accepted**. The other **22 case pages and 5 decision pages** were not depth-expanded in this wave. All 35 documents remain subject to full per-page completeness assessment and external independent approval. No independent reviewer or production MCP evaluation was performed in this checkpoint.

**Remote text-only mechanical check against PR head:** all 14 initially modified files, 102 relative Markdown links checked against a 248-file repository tree, balanced code fences, and the configured lexical boundary patterns of the edited files had **no detected issues**. This is not execution of the actual local Python checkers or proof of evidence correctness, and does not supersede them.

## Substantive page-depth work checkpoint — 2026-10-19

**This is an authoring-progress register, not an independent acceptance result.** Of the existing **29** case studies, **14** have received additional primary-source-bounded architecture depth in the current [M9 draft PR #212](https://github.com/rouslanbaranov/tycho/pull/212): Netflix **Java platform, DGS/Spring GraphQL, ZGC, Java 21 pinning, Zuul 2, 2008–2016 cloud rearchitecture**; Shopify **modular monolith and Packwerk**; Uber **DOMA**; LinkedIn **Kafka tier audit**; Airbnb **Bazel migration**; Discord **search cells**; Stripe **online subscriptions**; and Cloudflare **Super Slurper**. The [agentic migration decision guide](../../book/cases/decisions/agentic-migration-safety.md) has also been substantively deepened. Added content includes reported-vs-inferred chronology, system/failure boundaries, negative results, migration/rollback safeguards, workload-specific quantitative caveats and applicability contraexamples.

**Still without this dedicated depth pass in PR #212 — 15 case pages:** `netflix-data-project-durable-workload-identity.md`, `netflix-grpc-cpu-workerpool-virtual-thread-regression.md`, `netflix-hotspot-false-true-sharing.md`, `netflix-chaos-kong-regional-failover.md`, `netflix-casspactor-shadow-migration.md`, `netflix-cassandra-dynamic-time-series-splits.md`, `uber-mezzanine-pg-to-schemaless.md`, `uber-mysql-to-myrocks.md`, `uber-cinnamon-admission-and-fairness.md`, `shopify-helix-checkpoint-gated-native-migration.md`, `discord-cassandra-scylladb-messages.md`, `spotify-tech-migration-long-tail.md`, `spotify-honk-data-consumer-migration.md`, `meta-tao-social-graph-serving.md`, `meta-ingestion-shadow-migration-lifecycle.md`. This is **not a claim of their absence or poor quality**: each already exists as a bounded draft; each needs an explicit evidence-by-evidence completeness decision rather than a word-count target.

**Still without this wave's dedicated depth pass — 5 comparison guides:** `monolith-vs-services.md`, `reactive-vs-virtual-threads.md`, `gc-and-tail-latency.md`, `data-migration-correctness.md`, `build-delivery-migration.md`. They already contain synthetic ADRs but remain pending domain-specific falsification/counterevidence and independent review.

**Mechanical GitHub-only scan on the current wave:** reviewed the Markdown bodies on the feature branch against the `main` path inventory: 21 changed Markdown files at check time had balanced code fences, no repeated identical second-level headings and no missing relative Markdown file targets in the scanned subset. This does **not** verify anchors, external source reachability, diagram rendering, full repository checks, publisher claim accuracy, copyright or independence. Local `premerge_check.py` and `validate_m9_cases.py` were **not executed**: the execution container cannot resolve `github.com` for a full checkout. The feature branch was ahead of and behind current main; reconcile concurrent main changes before merge.

**Completion contract:** continue page-by-page research until every existing case/decision page meets the substantive checklist; then obtain named independent technical/copyright review and an authorized, evidence-backed search/MCP dependency disposition. Keep #121/E16/M9 open. Retired knowledge-graph features cannot be reintroduced as blockers or “missing coverage.”

## Latest full-corpus authoring checkpoint — 2026-10-19 (supersedes partial-wave counts above)

**Highest-priority case-content work reached the complete corpus at this draft checkpoint:** all **29/29 case pages**, including **12 Netflix and 17 other-company cases**, and all **6/6 comparative decision pages** have received substantive expansion in [draft PR #212](https://github.com/rouslanbaranov/tycho/pull/212). Earlier checkpoints in this file saying 7/29, 14/29 or 22 outstanding refer to intermediate commits of the same work and **are not the latest count**. Work covers historical baseline/transition and ownership, alternative hypotheses, failure/correctness/rollback boundaries, dated publisher-reported outcome limits, contraindications, and original reproducible *proposed* experiments where source measurements are absent. Authored analysis must remain distinguishable from published facts.

### Executed remote GitHub-tree checks for the 35-page current branch set

| Check | Observed result | Scope / caveat |
|---|---|---|
| Edited substantive corpus | **29/29 case files, 6/6 decision guides** occur in PR diff | Counts files with source-bounded depth passes, **not** independently signed-off pages |
| Source-backed case identity | **29/29** first-party URLs present and stable `case.*` identity labels visible | Not a human audit of URL accuracy or each claim against original section |
| Native illustration structure | **29/29** case pages have balanced Mermaid code fences | A syntactic check, not an actual GitHub/Mermaid renderer execution |
| Markdown file links | All 35 pages' **relative Markdown file targets** inspected against the GitHub `main` file inventory; **zero missing target files** | Target anchors, dynamic links and external HTTP reachability not certified |
| Repeated level-2 headings | No repeated identical H2 headings observed in 35 pages | Editorial coherency and duplication between differently named sections still require review |
| Decision guides | **6/6** have expanded domain-specific scenario, counterevidence, refusal and reversal discussions | No independent architecture decision fitness test or executing agent evidence |
| Provenance/runtime tests | Full pinned-checkout `validate_m9_cases.py`, `premerge_check.py`, local source and quality suites: **NOT EXECUTED** in this GitHub-only pass | Structural inspection **must not** be converted into a test-suite PASS |
| External human technical/copyright review | **NONE** supplied | No case is approved as `independent_reviewed` by this edit |
| Live K18–K23 lexical/hybrid/MCP evaluation | **NOT EXECUTED**; core service availability/authorized dependency decision still gates final M9 acceptance | Historic candidate BM25 data is not this production evaluation |
| Curated knowledge graphs | **EXCLUDED** from M9 by binding ADR | Not a missing implementation, coverage defect or release blocker |

**Content-depth coverage is 100% of the existing 35-page corpus; independently confirmed complete/accepted coverage is NOT 100%.** A “depth pass” certifies that extra content was authored and links were scanned, not that every claim is correct, fresh, license-cleared and externally reviewed. The 43 public source candidates have their previous scoped admission/disposition; two unavailable technical source bodies remain excluded from positive engineering claims.

**Next acceptance gate:** named qualified independent reviewer records a case-by-case source/section/date/metric/contraindication/rights verdict, amendments to every high-severity error, pinned repo-checkout execution with commands/output hashes, and authentic search/MCP evaluation or explicitly authorized exception. **Do not close #121, Epic #113 or M9** merely because 35/35 pages now have substantive drafts. Keep PR #212 **draft** until these controls and main-branch integration review pass. No renewed graph work is required or permitted.
