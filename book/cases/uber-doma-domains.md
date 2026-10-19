# Uber — DOMA: governing service ownership after microservice explosion

**Case ID:** `case.uber.doma-domains` | **Milestone:** M9 E16-05 #118 | **Status:** evidence-bound original draft; technical review pending.  
**Source:** U01 — [original company engineering article](https://www.uber.com/us/en/blog/microservice-architecture/) (2020 engineering retrospective); primary evidence: Microservices at Uber; Domain-Oriented Microservice Architecture; Layer Design; Gateways; Extensions. Source reuse: original link and attributable paraphrase only; no copied diagrams or pages.

## Situation — the legacy architecture and constraint

A large microservice network became difficult to change safely because one user feature crossed many independently owned services and teams. Debugging a particular flow could involve about 50 services across 12 teams in an anecdote from the report; the number illustrates *this* incident, not normal service fan-out. Hidden coupling allowed networked-monolith behavior despite independent deployability.

## Chosen architectural change

Uber introduced domains as groups of related microservices, gateways as the externally facing contracts of a domain, and ordered dependency layers (infrastructure, business, product, presentation, edge). The aim was to reason about ownership, blast radius and who is allowed to depend on whom, not to eliminate the microservices themselves.

```mermaid
flowchart LR
  A[Cross-team service mesh / ad hoc RPC] --> B[Domain gateway and owned interfaces]
  B --> C[Layered domain implementations]
```

**Diagram alternative:** Cross-team service mesh / ad hoc RPC evolved through Domain gateway and owned interfaces toward Layered domain implementations. This is a deliberately simplified, original decision/transition sketch; it is not the original company's infrastructure map.

## Migration and validation

A domain boundary can first be modeled as an ownership and dependency inventory; introduce a gateway whose published API hides inner domain service churn. An extension mechanism can then serve explicit integrations without every external team editing the same microservices. This transition order is Tycho guidance: the article discusses architectural principles and experience, but does not give an atomic fleet-wide cutover runbook.

Suggested decision record for a different organization:

| Verification gate | Evidence needed before accepting change | Rollback or hold |
|---|---|---|
| Interface and ownership | Inventory of dependent clients, schema/contract/API compatibility and authorized owner | Preserve existing public contract |
| Representative workload | Actual traffic mix, failure modes and capacity baseline; no invented p99 | Roll back the cohort if its own SLO worsens |
| Correctness | Domain-specific business invariants, dual-state reconciliation if used, idempotent replays | Keep authoritative old representation until proven |
| Operability | Error budgets, runbooks, trace continuity, incident ownership and cost | Stop rollout without a clear incident response owner |

The gates in this table are Tycho's **analytical adaptation**, not an assertion that the source's engineers measured these same four things.

## Negative evidence, costs and alternatives

Services are not magically independent when gateways leak internal data models. Additional gateways can become central points of change; layer violations cannot be fixed by drawing boxes. This does not prove that a small monolith should be decomposed.

**Alternatives:** retain/tune the legacy architecture if capacity and correctness already meet requirements; incrementally constrain its internal dependency graph; adopt the described transition only if its own reported bottleneck exists; otherwise conclude **insufficient evidence** rather than copying the brand's solution. These are synthetic architecture alternatives and must not be presented as alternatives the company explicitly evaluated unless the source said so.

## Observed results and temporal validity

The company presented DOMA as an organizational and architectural response to tangled microservice dependencies; the post does not establish a controlled, transferable numerical productivity gain.

This is a company-reported historical result, not an independently reproduced benchmark. Precise current topology, total engineering effort, p99 and comparative cost must be regarded as **unknown** unless the named primary article supplies them. Do not extrapolate a dated deployment to October 2026 current practice.

## Applicability to legacy modernization

Favor domains and API ownership when a *preexisting* large distributed fleet suffers escalating coordination cost. For a small product that can change one deployable application cheaply, prefer module-level domain boundaries before adding network hops. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**Provenance:** [U01 primary](https://www.uber.com/us/en/blog/microservice-architecture/), sections Microservices at Uber; Domain-Oriented Microservice Architecture; Layer Design; Gateways; Extensions. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.
