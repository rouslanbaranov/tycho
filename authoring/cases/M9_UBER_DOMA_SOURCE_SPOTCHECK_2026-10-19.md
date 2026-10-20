# M9 source-review spot check — Uber DOMA (2020)

**Date:** 2026-10-19.  
**Reviewer type:** bounded AI-assisted primary-source comparison, **not** an independent qualified technical reviewer or copyright/license acceptance.  
**Case:** [Uber DOMA](../../book/cases/uber-doma-domains.md), \`case.uber.doma-domains\`; source **src.m9-u01** from [the public case register](../../sources/REAL_WORLD_ARCHITECTURE_CASES.md). Related [monolith-versus-services playbook](../../book/cases/decisions/monolith-vs-services.md), [Shopify countercase source recheck](M9_SHOPIFY_SOURCE_SPOTCHECK_2026-10-19.md).

## Public first-party material and temporal boundary

[Adam Gluck, *Introducing Domain-Oriented Microservice Architecture*, Uber Engineering, 2020-07-23](https://www.uber.com/us/en/blog/microservice-architecture/). Sections: **Introduction**, **Motivations**, **Domain-Oriented Microservice Architecture**, **Uber's Implementation → Domains / Layer Design / Gateways / Extensions**, **Benefits → Products & Platforms / Reduced Complexity / Future Migrations**, **Practical Advice**.

The observed quantities represent Uber's own historic design/progress statements in **July 2020**; *none* describes October 2026 current production or an independently reproduced productivity experiment.

## Claim-specific check

| Claim | What the first-party article actually documents | Disposition / remaining uncertainty |
|---|---|---|
| Around 2,200 critical microservices, not one business component per process | **Introduction** describes a fleet around 2,200; **Reduced Complexity** says 2,200 services classified into 70 domains | **Matched 2020 scope**; one domain may hold one or many microservices |
| Historical debugging investigation covered about 50 services / 12 teams | **Motivations** contains this **example** | **Matched one reported incident**, not median call-graph path or general fan-out |
| Another feature integration before DOMA involved 10 touchpoints | **Motivations**, feature-example caption | **Matched example**, not universal pre-DOMA feature development cost |
| Five layer categories from infrastructure to edge | **Uber's Implementation → Layer Design** enumerates infrastructure, business, product, presentation and edge; higher application layers depend on lower general layers | **Matched source design**; not a mandatory industry layered topology |
| Domain gateway presents one public entry into underlying services | **Gateways** describes RPC, events and queries while hiding internal services/tables/pipelines | **Matched intent**; doesn't prove every consumer was migrated or that gateway failure domains were tested |
| Logic/data extension architecture | **Extensions → Logic Extensions / Data Extensions** describes plugins, Protobuf Any and alternatives | **Matched mechanism**; performance and authorization safeguards listed in Tycho are **original recommended tests**, not source-reported controls |
| 70 domains, roughly half implemented | **Benefits → Reduced Complexity** explicitly gives 70 classifications and about 50% implementation | **Matched with denominator**; classified ≠ implemented ≠ fully stable |
| Onboarding improvement 25–50% | **Benefits → Reduced Complexity** reports percentage improvement attributed to fewer touchpoints | **Matched publisher-reported result**, no control group, baseline population or portable causal estimate verified |
| Single early platform extension example: three days to three hours | **Benefits → Products & Platforms** reports a particular consumer experience | **Matched specific example**, not all integrations made 8× or 10× faster |
| Approximate service half-life of 1.5 years | **Benefits → Future Migrations** states Uber's estimate that half of services churn over 1.5 years | **Matched an estimate**, not empirical half-life for every service or a survival-law guarantee |
| Two large platform rewrites hidden behind domain gateways | **Benefits → Future Migrations** reports two historical rewrites | **Matched publisher report**; no detailed independently reproducible consumer migration log was inspected |
| Separate microservice vs modular-monolith recommendations | Uber advises contextual use of services and notes startup overhead; Shopify src.m9-sh01/src.m9-sh02 document a different choice | **Tycho comparison inference**, NOT controlled Uber vs Shopify A/B evidence or Uber's exact ADR |

## Findings and disposition

The case's existing [src.m9-u01 quantitative and domain-contract section](../../book/cases/uber-doma-domains.md) uses the major 2020 numbers with appropriately bounded interpretations. No factual contradiction was identified among the **eleven directly matched source-specific claims**, though their evidence is explicitly **company-reported**. The twelfth row is a **cross-company editorial interpretation**, not a first-party numeric assertion.

The case remains **DRAFT / PENDING independent review**. No copyright reuse or licensing sign-off, no technical runtime reproduction, no present-day source revalidation and no source-to-claim check of *every* line and diagram. The [M9 review acceptance matrix](M9_REVIEW_ACCEPTANCE_MATRIX.md) and issue [#121](https://github.com/rouslanbaranov/tycho/issues/121) remain OPEN.

**No curated Tycho knowledge graph or graph-aware search implementation is involved**. References to dependency and domains are the historical case *subject*, not additional platform scope.
