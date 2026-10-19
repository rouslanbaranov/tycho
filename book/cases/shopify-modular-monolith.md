# Shopify — modular monolith instead of premature distributed extraction

**Case ID:** `case.shopify.modular-monolith` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-bound original draft; technical review pending.  
**Source:** SH01 — [original company engineering article](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) (2019-02-21, Shopify Engineering); primary evidence: Microservice Architecture; Modular Monoliths; Componentization. Source reuse: original link and attributable paraphrase only; no copied diagrams or pages.

## Situation — the legacy architecture and constraint

A large Rails monolith mixed commerce domains in one codebase. Cross-domain references and unclear ownership slowed changes, but a switch to microservices would multiply deployment infrastructure, remote failure modes and coordination on a business model whose boundaries were still evolving.

## Chosen architectural change

Shopify explicitly chose one deployable application with enforced domain components. A component has an allowed interface and dependency shape but need not own a separate process or network endpoint. The choice preserves cheap in-process refactors while forcing architects to control logical coupling.

```mermaid
flowchart LR
  A[Unbounded Rails models and shared data] --> B[Domain components / dependency rules]
  B --> C[One governed Rails deployment]
```

**Diagram alternative:** Unbounded Rails models and shared data evolved through Domain components / dependency rules toward One governed Rails deployment. This is a deliberately simplified, original decision/transition sketch; it is not the original company's infrastructure map.

## Migration and validation

The company describes incremental componentization; for a comparable monolith, inventory dependencies and data access before enforcing public component APIs. Introduce architectural tests and refuse new cross-boundary imports; fix cycles before attempting isolated deployments. This control order is Tycho's transfer, not proof of an identical internal automation.

Suggested decision record for a different organization:

| Verification gate | Evidence needed before accepting change | Rollback or hold |
|---|---|---|
| Interface and ownership | Inventory of dependent clients, schema/contract/API compatibility and authorized owner | Preserve existing public contract |
| Representative workload | Actual traffic mix, failure modes and capacity baseline; no invented p99 | Roll back the cohort if its own SLO worsens |
| Correctness | Domain-specific business invariants, dual-state reconciliation if used, idempotent replays | Keep authoritative old representation until proven |
| Operability | Error budgets, runbooks, trace continuity, incident ownership and cost | Stop rollout without a clear incident response owner |

The gates in this table are Tycho's **analytical adaptation**, not an assertion that the source's engineers measured these same four things.

## Negative evidence, costs and alternatives

A modular monolith is not 'microservices in one process': release, capacity and failure domains remain shared. Language/module tooling may allow boundary violations, so governance is critical. This approach cannot independently scale arbitrary modules unless later extraction is justified.

**Alternatives:** retain/tune the legacy architecture if capacity and correctness already meet requirements; incrementally constrain its internal dependency graph; adopt the described transition only if its own reported bottleneck exists; otherwise conclude **insufficient evidence** rather than copying the brand's solution. These are synthetic architecture alternatives and must not be presented as alternatives the company explicitly evaluated unless the source said so.

## Observed results and temporal validity

The article is a design rationale and implementation experience, not a guaranteed productivity delta. Its value lies in documenting a defensible opposite answer to Netflix's independently operated service fleet.

This is a company-reported historical result, not an independently reproduced benchmark. Precise current topology, total engineering effort, p99 and comparative cost must be regarded as **unknown** unless the named primary article supplies them. Do not extrapolate a dated deployment to October 2026 current practice.

## Applicability to legacy modernization

Choose modularity within one runtime when operational simplicity and many shared transactions outweigh independent deployment; extract services only at proven scale/team boundaries with clear data ownership. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [SH01 primary](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity), sections Microservice Architecture; Modular Monoliths; Componentization. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.
