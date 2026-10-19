# Shopify — component governance is a migration, not a one-time refactor

**Case ID:** `case.shopify.component-governance` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-bound original draft; technical review pending.  
**Source:** SH02 — [original company engineering article](https://shopify.engineering/shopify-monolith) (2020 Shopify Engineering follow-up); primary evidence: Under Deconstruction; component boundaries and dependency enforcement. Source reuse: original link and attributable paraphrase only; no copied diagrams or pages.

## Situation — the legacy architecture and constraint

After selecting a modular monolith, residual shared models and Rails conventions still enabled accidental dependencies. A diagram naming components did not enforce their promises; changing historical references without breaking releases required gradual work.

## Chosen architectural change

Shopify's follow-up discusses an evolving codebase in which domain components and dependency checking are strengthened iteratively, while acknowledging remaining work. Packwerk and Rails packaging are tools in the larger migration; governance, ownership and exception reduction matter more than a magic static checker.

```mermaid
flowchart LR
  A[Implicit cross-package Rails references] --> B[Component API and exceptions register]
  B --> C[Gradually enforced package boundaries]
```

**Diagram alternative:** Implicit cross-package Rails references evolved through Component API and exceptions register toward Gradually enforced package boundaries. This is a deliberately simplified, original decision/transition sketch; it is not the original company's infrastructure map.

## Migration and validation

For another team, begin with observed dependency graph; classify cross-component edges by business requirement and ownership, introduce public API layers, grandfather known exceptions with explicit reduction targets, and add CI guardrails that reject new violations. These steps are Tycho's implementation proposal, not a claim of the company's exact per-week sequence.

Suggested decision record for a different organization:

| Verification gate | Evidence needed before accepting change | Rollback or hold |
|---|---|---|
| Interface and ownership | Inventory of dependent clients, schema/contract/API compatibility and authorized owner | Preserve existing public contract |
| Representative workload | Actual traffic mix, failure modes and capacity baseline; no invented p99 | Roll back the cohort if its own SLO worsens |
| Correctness | Domain-specific business invariants, dual-state reconciliation if used, idempotent replays | Keep authoritative old representation until proven |
| Operability | Error budgets, runbooks, trace continuity, incident ownership and cost | Stop rollout without a clear incident response owner |

The gates in this table are Tycho's **analytical adaptation**, not an assertion that the source's engineers measured these same four things.

## Negative evidence, costs and alternatives

A static dependency checker cannot ensure data contract ownership, transaction semantics or runtime isolation. Broad exceptions can preserve the dependency knot forever; enforcing every rule instantly can stall delivery. This is an incomplete-state case, not a falsely completed modernization.

**Alternatives:** retain/tune the legacy architecture if capacity and correctness already meet requirements; incrementally constrain its internal dependency graph; adopt the described transition only if its own reported bottleneck exists; otherwise conclude **insufficient evidence** rather than copying the brand's solution. These are synthetic architecture alternatives and must not be presented as alternatives the company explicitly evaluated unless the source said so.

## Observed results and temporal validity

The follow-up illustrates the continuing operational cost of architectural boundaries within a monorepo. It does not prove that all components became independent or that a specific tool solved every cycle.

This is a company-reported historical result, not an independently reproduced benchmark. Precise current topology, total engineering effort, p99 and comparative cost must be regarded as **unknown** unless the named primary article supplies them. Do not extrapolate a dated deployment to October 2026 current practice.

## Two successive detection approaches and why they differed

The [2019 first-party article](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) (SH01, **Isolating Dependencies**) described **Wedge**: a component-coupling feedback mechanism that combined runtime Ruby traces and static framework structure such as ActiveRecord associations. The [2020 follow-up](https://shopify.engineering/shopify-monolith) (SH02, **What We're Building Right Now** and **How We Enforce Boundaries**) explains why the team built **Packwerk** as a separate tool: analyzing explicit Ruby constant references was faster and more actionable in the pull-request workflow. It intentionally did **not** attempt to infer every possible runtime call. Both mechanisms concern **Shopify's source-code boundary enforcement**, not the knowledge graph excluded from the Tycho product.

| Historical stage | What the company was trying to observe | Principal limitation |
|---|---|---|
| Wedge (2019 account) | Runtime cross-component calls, ActiveRecord associations, inheritance and public-API violations, summarized into an isolation score | Instrumented execution covers the exercised paths; dynamic calls and long-term ownership are still hard |
| Packwerk (2020 account) | Static references to Ruby constants, component dependency declarations and privacy breaches, checked in PRs | A constant-reference checker does not prove runtime absence of cross-domain data access or business invariant preservation |
| Ownership and stewardship (2020) | Engineers own code grouped by commerce subdomain and negotiate API contracts | Organizational ownership alone is not equivalent to an isolated component |
| Enforced and declining exceptions (goal) | Refuse new violations while simplifying older dependencies | Complete acyclicity and strong isolation were a future objective, not the reported final state |

This is an observed evolution in **scope and enforcement**, not proof that Packwerk replaced every Wedge capability or that the original organization had solved all dynamic Ruby boundaries. Wedge and Packwerk should not be presented as interchangeable fully semantic dependency proofs.

## Why rigid rules were a failed modernization tactic

The 2020 retrospective names a social/technical failure: a centralized architecture team initially emphasized uniform public-interface patterns; some teams reshaped their problems just to fit the prescribed approach, and the rules added friction without addressing the actual blockers. The later effort placed more emphasis on **developer motivation, pairing, reducing tooling pain and letting component owners succeed incrementally**. [SH02, **What We Learned so Far**, **Foster the Grassroots**].

The same account distinguishes **two incomplete-state strategies**. Shopify's main monolith prioritized labeling a broad target set of subdomains and establishing file **stewardship**, even when their boundaries were still porous. Other applications experimented with extracting small fully isolated components, leaving a larger unstructured core behind. Each intermediate shape optimizes something different: discoverable ownership versus stronger isolation of selected code. Neither can be declared universally superior without knowing the primary failure mode.

## Reported progress and unresolved correctness boundaries

At the **September 2020** reporting point, the main monolith contained **37 components** and **about one third** used Packwerk to restrict dependencies. The writer explicitly described cycles, database model access and further isolation as still-in-progress work. Adoption percentage refers to components using Packwerk, **not** to verified zero-coupling or every Ruby constant covered. Architectural evolution cannot be marked 100% finished from this number alone.

The article also discusses partial **Rails Engine** packaging and selective service extraction (storefront rendering for separate read-heavy scaling and payment-vault separation for sensitive data). These are practical boundary cases: a modular-monolith strategy can be the *default* without forbidding independently operated components when workload or security justifies them. See the distinct [2019 modular-monolith decision](shopify-modular-monolith.md).

## A source-grounded adoption/reversal rubric (Tycho synthesis)

For a hypothetical Rails legacy system, baseline the number of implicit cross-component access paths, cycles, ownership gaps, runtime call failures and prior migration regressions. Choose an **ownership-first** organizational regrouping if individual developers cannot find or safely edit their domain; choose **isolation-first** for a critical component whose unexpected dependencies already cause incidents. Avoid announcing that dependency enforcement has been completed when a large exception set is still active.

Stage with read-only diagnostics, per-component owner decisions, a tiny contract test surface and nonblocking reports; tighten CI only for net-new violations after the team can resolve old debt. Independently test cross-component data authority, schema drift, retries and permission checks that a Ruby constant linter cannot observe. A safe rollback can restore the previous file/package boundary rule while preserving code behavior; full data-owner changes require their own reversal plan.

**Reject a tooling-first rollout** when static checks identify “violations” without a usable migration path, the service framework uses dynamic dispatch outside the analyzer's visibility, or a component's data ownership is unknown. Evidence insufficient to say whether a specific cycle can be removed? Escalate to the domain owner with a concrete scenario rather than invent a globally correct refactoring. The blog gives no reproducible 2026 production topology, independent productivity benchmark or completed-cycle count.

## Applicability to legacy modernization

Prefer incremental, observable dependency constraints over a big-bang module rewrite; measure new violations, removed exceptions and cross-boundary churn. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [SH02 primary](https://shopify.engineering/shopify-monolith), sections Under Deconstruction; component boundaries and dependency enforcement. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.
