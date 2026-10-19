---
metadata_version: 1
id: "tycho.page.7419e7903c5549a6a9c7944f4214f7e1"
kind: "page"
parent_id: "tycho.landing.43b3f0c107e34e5a800d6c1de65069e8"
canonical_path: "book/cases/uber-doma-domains.md"
title: "Uber — DOMA: governing service ownership after microservice explosion"
topic_ids:
  - "architecture-case-studies"
perspectives:
  - "architecture"
  - "migration"
summary: "Reader entry for Uber — DOMA: governing service ownership after microservice explosion. Scope includes Situation — the legacy architecture and constraint; Chosen architectural change; Migration and validation."
route_hints:
  questions:
    - "What are the scope, mechanisms and limits of Uber — DOMA: governing service ownership after microservice explosion?"
  prerequisites: []
  related_ids:
    - "tycho.page.aed8b635f57f41dfa63c897a8d1caca8"
  excludes:
    - "No independent content acceptance or runtime reproduction is implied."
  keywords:
    - "Uber"
    - "DOMA"
    - "governing"
    - "service"
    - "ownership"
    - "after"
    - "microservice"
    - "explosion"
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

## Why domain boundaries were introduced after independent services

The dated [Uber Engineering account](https://www.uber.com/us/en/blog/microservice-architecture/) (U01, **Motivations**) separates two earlier architecture pressures: in approximately 2012–2013, large shared deployables impaired independent release and operational isolation; by 2018 the replacement service network had accumulated its own integration and debugging burden. A reported debugging investigation traversed roughly **50 services owned by 12 teams**; a different illustrative feature path needed **10 touchpoints** before DOMA. These examples identify coordination/coupling failure modes, not median trace length or a published p99.

The July 2020 proposal therefore **does not advocate collapsing 2,200 services back into one monolith**. It introduces a stable level of organizational and API ownership *above* individual implementations: one domain can contain a single service or many, and teams interact through a domain gateway, not through every implementation's changing RPC surface. The primary source reports that **2,200 critical microservices had been classified into 70 domains**, **roughly half implemented**, at that point in the rollout. Classification, implementation and full migration are separate denominators.

## Contract boundaries, allowed dependency directions and extensions

| DOMA mechanism | Source-bounded architecture role | Failure mode / migration responsibility |
|---|---|---|
| Domain grouping | Collection of related implementation services, sometimes within multiple organizational teams | Grouping by present reporting structure alone may split a coherent business capability |
| Five ordered layers | Infrastructure → general business → product → presentation → edge, from reusable lower layers to more consumer-specific upper layers | Higher layers may depend on lower ones; reversing that relationship embeds product logic in shared platform services |
| Domain gateway | A stable entry interface exposing RPC, event or query contracts and hiding internal services, tables and pipelines | Gateway bypass, over-broad shared DTOs or non-versioned response semantics recreate direct consumer coupling |
| Logic extension | Typed provider/plugin interface attached at a documented domain extension point | Unbounded plugins can change latency, fault isolation and safety behavior despite a stable API |
| Data extension | A domain accepts extensible context; the report describes Protocol Buffers **Any** as one option | Serialized payloads still require schema/version, authentication, size, privacy and retention controls |

**Publisher basis:** U01, sections **Domains**, **Layer Design**, **Gateways**, **Logic Extensions**, **Data Extensions**. The risk column is an original Tycho analysis: it should not be read as a record of every incident experienced by Uber. The paper explicitly allows domain size to vary; **80 microservices in the Maps organization behind three gateways** illustrate grouping, not a default gateway-to-service ratio.

For a hypothetical domain owner, the meaningful migration seam is external **contract identity**. The owner can replace, split or consolidate services behind a gateway while maintaining caller-visible semantics and a documented exception mechanism. In contrast, letting clients query implementation tables across domains would preserve the old source-of-truth coupling under a new name.

## Quantitative adoption evidence and its limits

| Publisher statement, July 2020 | Supported interpretation | Unsupported extrapolation |
|---|---|---|
| 2,200 critical services → 70 identified domains | Historical cataloguing scope at the author's observation date | All 70 domains were already migrated or have uniform size |
| Roughly 50% of domains implemented | Partial rollout, with other domains still planned | A 100% complete organization-wide DOMA transition |
| 25–50% shorter onboarding | Company-reported improvements for the described domain-gateway context | A transferable labor-cost reduction independent of task size |
| One platform integration from 3 days to 3 hours | Named experience with extensions, not a randomized comparison | Every change became ten times faster |
| Service half-life estimated at 1.5 years | Source-reported fleet churn estimate used to justify stable gateway interfaces | Every service expires exactly at 18 months or every domain changes at the same rate |

The post also reports **two large platform rewrites hidden behind gateways** instead of forcing all upstream consumers onto a new internal API. It does **not** provide reproducible control cohorts, an independently measured broad p99 or an invariant organizational velocity model. An agent should return the historical observation window, population and confidence caveats along with any quoted percentage. [U01, **Benefits**, **Reduced Complexity**, **Future Migrations**].

## Transfer: staged migration and reversal gates (Tycho original proposal)

A different distributed fleet can start with one operationally costly cross-team capability rather than decree universal gateways: (1) trace real consumers and domain data ownership, including cross-team failure/latency impact; (2) define a minimal public contract and a reversible adapter at the existing API; (3) add translation or routing behind that seam without changing the authoritative store; (4) replay consumer contracts and security context, compare request-level error/p99 and trace fan-out; (5) migrate one caller cohort; (6) retire direct implementation dependencies only after measured usage has ceased. Versioning and rollback of the gateway are part of the change; swapping a call graph picture for a functional contract is not.

**Contraindications:** few services and one team can redeploy cheaply, the cross-domain contract is less stable than internal implementations, independently owned data cannot be cleanly delimited, a new gateway adds a highly contended synchronous hop, or observability cannot attribute failures to domain owners. Compare the deliberately different [Shopify modular-monolith decision](shopify-modular-monolith.md); the two public reports have **different scale, chronology and business constraints**, not a controlled A/B. If domain ownership and caller measurements are missing, return **insufficient evidence** instead of recommending a gateway based on the company's reputation.

## Applicability to legacy modernization

Favor domains and API ownership when a *preexisting* large distributed fleet suffers escalating coordination cost. For a small product that can change one deployable application cheaply, prefer module-level domain boundaries before adding network hops. Before a roadmap is approved, require a baseline with data ownership and blast radius, a comparison to a smaller intervention, and measurable acceptance gates. An agent should retrieve this case as **evidence for conditions and counterconditions**, not as a universal preferred architecture.

**2026-10-19 publisher-source spot check:** [The dated U01 verification register](../../authoring/cases/M9_UBER_DOMA_SOURCE_SPOTCHECK_2026-10-19.md) matched 11 narrow source-specific statements and classified the Uber/Shopify comparison as Tycho's own inference. This does not establish a qualified independent review, copyright approval or reproduced benchmark.

**Provenance:** [U01 primary](https://www.uber.com/us/en/blog/microservice-architecture/), sections Microservices at Uber; Domain-Oriented Microservice Architecture; Layer Design; Gateways; Extensions. Cross-case comparisons must retain the original company's architecture and historical observation window. **Case review:** not yet independently approved under #121.
