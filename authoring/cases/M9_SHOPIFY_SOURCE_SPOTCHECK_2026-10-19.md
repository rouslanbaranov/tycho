# M9 first-party source spot-check — Shopify modular monolith and Packwerk

**Date:** 2026-10-19  
**Review scope:** Narrow AI-assisted claim-to-publisher comparison using directly reopened **public first-party** articles. This is **not** an independent qualified human review, copyright/license acceptance, empirical replication, or closing evidence for issue [#121](https://github.com/rouslanbaranov/tycho/issues/121).

## Exact sources and observation windows

| ID | First-party source and section identifiers | Historical observation |
|---|---|---|
| SH01 | [Kirsten Westeinde, *Deconstructing the Monolith*, Shopify Engineering, 2019-02-21](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity); **Microservice Architecture**, **Modular Monoliths**, **Shopify’s Implementation of the Modular Monolith: Componentization**, **Code Organization**, **Isolating Dependencies**, **Enforcing Boundaries** | Developer surveys and reorganization following constraints noticed in 2016; team assembled in early 2017; new module APIs and full enforcement were **work in progress** at publication |
| SH02 | [Philip Müller, *Under Deconstruction: The State of Shopify’s Monolith*, Shopify Engineering, 2020-09-16](https://shopify.engineering/shopify-monolith); **Apply Tooling Deliberately**, **Use Rails Engines**, **Define and Enforce Contracts**, **Perform Static Dependency Analysis**, **Decide to Prioritize Ownership or Boundaries**, **What We’re Building Right Now** | Later, distinct partial-adoption snapshot; must not be treated as 2019 state or a verified 2026 topology |

## Selected matched assertions (bounded checks, not whole-case approval)

| ID | Claim represented in current Tycho case pages | First-party observation | Outcome and required caution |
|---|---|---|---|
| SH-01 | Shopify chose incremental **modularity within one deployable** rather than blanket microservice extraction | SH01 **Microservice Architecture** and **Modular Monoliths** explicitly contrast deployment, network/coordination and data costs | **MATCHED as a historical decision direction**; not proof a monolith is optimal for other workloads |
| SH-02 | The early componentization team formed in **2017** | SH01 **Shopify’s Implementation ... Componentization** describes the early-2017 team and preceding developer survey | **MATCHED**; the survey is company self-report, not independently designed experiment |
| SH-03 | Around **6,000 Ruby classes** were classified for a large code organization move | SH01 **Code Organization** describes a spreadsheet of about 6,000 classes and one mechanically generated big-bang file-move PR | **MATCHED with approximate denominator**; this mechanical move must not be confused with big-bang independently deployed services |
| SH-04 | Large mechanical move damaged GitHub's displayed file history, though git-follow-style tracing was possible | SH01 **Code Organization** explicitly describes renames perceived by GitHub as delete/new and historical traceability costs | **MATCHED as publisher report**; do not imply actual Git history objects were deleted |
| SH-05 | Wedge used instrumented Ruby calls plus ActiveRecord relations/inheritance to surface cross-component violations | SH01 **Isolating Dependencies** describes runtime TracePoint methods, associations and inherited classes | **MATCHED as described mechanism**; this is historical Ruby dependency tooling, **not a Tycho knowledge-graph implementation** |
| SH-06 | Full API isolation and **enforcement were not complete in 2019** | SH01 **Isolating Dependencies** acknowledges partial adoption; **Enforcing Boundaries** describes desired stronger enforcement as future work | **CORRECTION MADE** in [Shopify modular-monolith case](../../book/cases/shopify-modular-monolith.md): changed opening from “with enforced domain components” to an explicitly staged target |
| SH-07 | In **September 2020**, Shopify reported **37 components** and **Packwerk adopted by about one third** of those components | SH02 **What We’re Building Right Now** | **MATCHED exact observation window**; **not** proof all component boundaries were strong, every component ran Packwerk, or 2026 state |
| SH-08 | For a particular publishing window, Wedge's instrumented full test pass took **over an hour**, Packwerk static constant-reference scan **a few minutes** | SH02 **Perform Static Dependency Analysis** | **MATCHED company-reported engineering experience**, **not** a controlled equivalent-workload throughput benchmark; the detection techniques have different coverage |
| SH-09 | Rails Engines adopted as a favored modular packaging mechanism, with caveats | SH02 **Use Rails Engines** describes one-process composable engines and gem/tooling issues | **MATCHED as then-current stated direction**, not universal Rails or microservice prescription |
| SH-10 | Sorbet became Shopify's component input/output contract preference after custom hash-schema limits | SH02 **Define and Enforce Contracts** reports component-schema runtime/maintenance concerns and Sorbet | **MATCHED a company tool choice**; doesn't prove all entrypoints were statically safe |
| SH-11 | The modular monolith was **not** a rule forbidding all extracted services | SH02 **What We’re Building Right Now** explicitly names separately scaled storefront rendering and separate payment-card vaulting for data-sensitivity | **MATCHED**; “Shopify used no microservices” is incorrect |
| SH-12 | Ownership-first versus isolation-first boundary strategies can leave different incomplete intermediate states | SH02 **Decide to Prioritize Ownership or Boundaries** describes both, with main monolith adopting ownership-first | **MATCHED conceptual report**, with trade-off table in Tycho being **new synthesis**, not a company A/B trial |

## Case-level crosswalk and negative review

- [Shopify modular monolith](../../book/cases/shopify-modular-monolith.md) owns SH01 decision rationale, 2017/2019 history, expected economic trade-offs and later SH02 qualifications. Its previous summary was **overstated**: the presence of tooling and intentions does **not** imply all boundaries already strictly enforced in 2019. The case is corrected in the integration PR.
- [Shopify Packwerk boundary evolution](../../book/cases/shopify-packwerk-boundary-evolution.md) owns SH02's technical follow-up: static versus instrumented coverage, tooling lag, social adoption, 37/third numbers and ongoing Rails/ActiveRecord limitations. The existing draft distinguishes these mechanisms and partial states, but has not received complete independent source and copyright review.
- [Monolith-versus-services decision playbook](../../book/cases/decisions/monolith-vs-services.md) may cite Shopify as a real *counterexample* to treating distributed deployment as inevitable. Its suggested migration steps and ADR **belong to Tycho**, not Shopify's documented choice or a head-to-head controlled experiment against Netflix.
- **Source-level disagreement was not found within the twelve selected, specifically scoped historical claims after correcting SH-06's wording.** This conclusion does not cover every sentence, diagram, attribution, numerical claim or external link in these case pages.

## Still unverified (do NOT close #121 or M9)

- Exact legal rights/terms of reusable quotations, figures and code; public read access only permits safe references/original paraphrases, **not** wholesale republication. No external diagram is copied.
- Independent subject-matter/copyright reviewer, detailed historical source-to-claim mapping for every sentence, numeric denominator audit across all 35 pages, accessibility/diagram rendering, exact GitHub anchor validation and future-source stability.
- No fresh evidence of Shopify's 2026 application topology, architecture productivity causality, p99 or full adoption of domain isolation. All such conclusions must remain **unknown**.
- No actual boundary checker run, codebase checkout, design experiment, production metrics, benchmark, legal review or consent of a qualified independent reviewer.
- All **29 case studies + six playbooks** remain draft; [M9 review matrix](M9_REVIEW_ACCEPTANCE_MATRIX.md) stays open. The pinned combined Git tree structural scan is separately documented in [the M1–M9 integration report](../UNIFIED_BOOK_M1_M9_INTEGRATION.md).

## Editorial process recommendation

For other M9 cases, reuse this narrow approach: name the real first-party article and publication window, check each historical statement under its specific section, keep company-reported results separate from Tycho synthetic decision advice, **correct ambiguous temporal/implementation claims**, and leave the independent acceptance field open until the qualified review plus full checks are actually complete.

**No curated knowledge-graph build or validation task is proposed or implied.**
