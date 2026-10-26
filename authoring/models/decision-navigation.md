# Decision navigation and insufficient-evidence behavior

> Tycho E01-06 [#22](https://github.com/rouslanbaranov/tycho/issues/22), original query-and-decision contract, 2026-10-19. **Method only.** No production index, curated decision graph, MCP tool, agent benchmark, private corpus or automatic selection engine is claimed.

## Mission and safety contract

Rocinante and human users must be able to begin with either a **requirement**, an **operational symptom**, an existing **legacy constraint**, or a **modernization objective**; reach only relevant architecture evidence; and receive a conclusion with actual validity conditions, alternatives and missing evidence. Search/navigation does not manufacture a recommendation. When hard-gate data are absent the correct outcome is **insufficient evidence / measure first / retain current design**, not a confident technology name.

Canonical owners are [requirements and workload](requirements-workload-profile.md), [legacy baseline](legacy-modernization-profile.md), [applicability/contraindication cards](pattern-applicability-card.md), [candidate comparison and ADR](candidate-comparison-adr.md), and [target/transition architecture](target-transition-architecture.md). The source-to-claim ledger of any technical book page remains the authority on mechanism facts; a route explanation is only a navigation summary, never a competing canonical chapter.

## Universal route envelope

| Field | Meaning | If absent |
|---|---|---|
| `entry_route` | requirement, symptom, legacy-constraint, modernization-objective | ask one question to identify the route |
| `question` | concrete user outcome / failed observable / hard constraint / proposed improvement | do not guess a problem |
| `system_boundary` | actor/journey, ingress, state and dependency limits | return evidence request for named boundaries |
| `workload_context` | offered/admitted/completed rates, operation mix, skew, burst, concurrency, data size, growth, window, SLO | qualify as unknown; do not choose a capacity threshold |
| `current_state` | versioned legacy baseline and symptom evidence, when applicable | separate documented fact from hypothesized cause |
| `hard_gates` | correctness, security, availability, compatible versions, data/downtime/RPO/RTO, budget | unknown gates veto unconditional adoption |
| `query_scope` | canonical page IDs, sources, version/revision, graph neighbor direction and specific section | use targeted lexical/manual navigation until indices exist |
| `decision_state` | candidate, conditionally applicable, contraindicated, not required, retained, insufficient evidence | never silently promote to accepted |
| `stage_ladder` | proposed stages, each with gate and evidence | no stage theatre |
| `support` | claim→source passage, assumption type, counterexample, falsifying test | state exactly what is missing |
| `next_step` | finite experiment/inventory/review task with accountable owner | output insufficient evidence without false certainty |

This is a *proposed logical envelope*, not a JSON Schema or MCP interface. Stable page/graph identities and serialization are owned by subsequent metadata and graph issues.

## Route R1: Requirement → measurable scenario → eligible mechanisms

1. Identify objective and **hard** versus preferred quality attributes.
2. Bind a scenario from the requirements/workload profile with operation mix, limits and observation window; require a valid numerator/denominator for SLOs where meaningful.
3. Identify canonical mechanisms that could satisfy that outcome, with an applicability card for each. Retrieve exact evidence and contraindications, not broad catalogue snippets alone.
4. Eliminate confirmed hard-constraint violations, set unknown gates to **needs validation**, and compare surviving alternatives including simple/retained design.
5. Return either a conditional ADR candidate with a falsifiable experiment, or insufficient evidence.

**Example:** “handle a larger burst” without burst duration, downstream capacity, deadline or source profile produces a measurement plan. It does **not** select Kubernetes, a queue, caching or microservices.

## Route R2: Symptom → competing hypotheses → evidence requests

1. Distinguish a user-observed failure from an inferred cause and collect first occurrence, time window, correlation key, data version and affected boundary.
2. Generate competing falsifiable hypotheses; e.g., slow response can arise from pool waiting, serialized data writes, a GC stall or a degraded downstream dependency.
3. Read the canonical mechanism/failure paths and retrieve telemetry or code evidence for the proposed boundary. Avoid using a latency percentile as a mean in Little's Law.
4. Only after diagnosis, apply pattern cards and hard constraints. If the root cause is unknown, prescribe measurement, not a migration.
5. Return one minimal discriminator per high-impact hypothesis, expected result, and what would falsify it.

**Example:** “p99 got worse” with no offered-versus-completed demand or queue position is **investigate**, not “add asynchronous messaging”.

## Route R3: Legacy constraint → excluded options / transition gates

1. Load old runtime/data/transaction/API ownership evidence from the baseline; classify each as observed, documented, hypothesized or unknown.
2. Identify constraints (shared database writer, compatibility overlap, immutable external consumer, no-downtime requirement) and link the specific prohibitions/prerequisites of candidate patterns.
3. Test whether a target option changes an enforceable invariant. Disqualify proven violations; unknown compatibility blocks cutover.
4. Link the target and transition architecture separately; include staged coexistence, schema/read compatibility, reconciliation and irreversible boundary.
5. Prefer retain or stabilize if there is no independently supported benefit.

**Example:** a caller that cannot be upgraded synchronously makes an unversioned breaking API change unsafe without a compatibility phase; it does not demand microservices.

## Route R4: Modernization objective → baseline gap → target and migration alternatives

1. Frame the measurable before/after goal (e.g., remove a support-risk runtime) and what must remain behaviorally equivalent.
2. Diagnose the baseline; collect a real supported-version/advisory citation for an outdated dependency rather than infer obsolescence from age.
3. Compare retain/upgrade-in-place, branch-by-abstraction, strangler and replacement options **only when** their prerequisites are met.
4. For any target, produce a separate transition with reversible states, observed go/no-go and rollback/forward-recovery limits.
5. Record the decision and **revisit trigger**; never invent a successful migration.
6. Express the transition as an evidence-gated stage ladder: proof of concept,
   minimum viable product and product. Each stage may change the architecture
   but must state its delta, its gate and its evidence; see
   [the staged contract](../ROCINANTE-STAGED-MODERNIZATION-CONTRACT.md).
7. Never present the target state as the first implementation step. If the
   lowest stage has no falsifier or gate evidence, return insufficient
   evidence with the next observation.

**Example:** if a runtime must be upgraded but public API continuity is mandatory, upgrade-in-place may be the viable first option. A service split is not a default modernization goal.

## Minimal agent retrieval behavior before index/MCP delivery

- Start from the most specific canonical owner related to the route and the exact question; optionally load two nearby pages and expand when a missing guarantee or comparison requires it. This is a **token-saving heuristic, not an evidence limit**.
- Preserve source titles, inspected sections, versions and original claim validity. Never take a broad generated summary or graph edge as proof.
- Use candidate applicability data as **conditional diagnostic material**, not a model ranking. If alternatives remain uncertain, return the particular missing primary source or experiment.
- No universal number of users, RPS, nodes or milliseconds selects a pattern.
- For modernization questions, propose staged evolution rather than one leap
  and keep each stage's Tycho anchor and local gate visible.
- Return a compact answer with: route, scoped facts, unknowns, excluded/possible options, reason and **next discriminating action**. Detailed provenance must be expandable.
- If the required source is inaccessible, state `source-unavailable` and prefer a separately inspected official companion under its own citation; do not reconstruct unseen text.

## One original route decision diagram

~~~mermaid
flowchart TD
  Entry{"Entry type?"} --> Req["Requirement"]
  Entry --> Sym["Symptom"]
  Entry --> Legacy["Legacy constraint"]
  Entry --> Goal["Modernization objective"]
  Req --> Frame["Define scope, scenario and hard gates"]
  Sym --> Frame
  Legacy --> Frame
  Goal --> Frame
  Frame --> Evidence{"Critical evidence available?"}
  Evidence -->|No| Missing["Insufficient evidence: specific measurement or source task"]
  Evidence -->|Yes| Card["Canonical mechanism and applicability checks"]
  Card --> Gate{"Hard gate satisfied?"}
  Gate -->|Fail| Reject["Exclude and explain"]
  Gate -->|Unknown| Missing
  Gate -->|Yes| Compare["Retain versus supported alternatives"]
  Compare --> Decision["Conditional ADR + test + revisit trigger"]
~~~

Text alternative: four entry routes converge on a problem scope and hard constraints; missing critical evidence creates an explicit investigation task. The model considers pattern applicability and rejects verified hard failures before comparing retaining the existing approach to other feasible options. A conditional decision needs acceptance tests.

## Outcome codes and proof obligations

| Code | Meaning | User/agent response |
|---|---|---|
| `RETAIN` | Existing design is adequate under validated objectives | Explain observed bounds and revisit triggers |
| `STABILIZE_FIRST` | Smallest corrective action supports objective without unneeded topology change | Provide tested root cause and regression/rollback |
| `MEASURE_FIRST` | A decisive workload or causal boundary remains unknown | Name precise instrumentation, control case and owner |
| `INSUFFICIENT_EVIDENCE` | Source, compatibility, hard-gate or empirical basis is absent | Distinguish inaccessible source from unresolved experiment |
| `CONTRAINDICATED` | Candidate demonstrably violates a hard constraint | Cite violated gate; seek alternatives |
| `CONDITIONAL_CANDIDATE` | No known hard violation; benefits need source/experiment or approval | Proposed ADR with falsification and failure conditions |

**Not an approval code:** `CONDITIONAL_CANDIDATE` does not mean “migrate now”. Accepted ADR requires actual named review and sufficient evidence in its stated scope.

## Evidence, review and limits

Public reasoning references inspected 2026-10-19: [arc42 §9 Architecture Decisions](https://docs.arc42.org/section-9/), *Content/Motivation/Form*, supports retraceable decision rationale; [AWS Branch by abstraction](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/branch-by-abstraction.html), implementation prerequisites, and [Fowler/Sato Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), expand/migrate/contract, support transition reasoning. The route taxonomy and outcome codes here are **Tycho's original proposed contract**, not an adopted standard. No independent domain review, real search-index evaluation, graph traversal, MCP server or automatic architecture-choice engine is asserted.
