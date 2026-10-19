# Architecture decision layer — implementation plan

Status: roadmap scope revised 2026-10-19. Originally drafted 2026-10-18.

## Purpose

Make Tycho useful for selecting and modernizing architectures under explicit requirements and constraints. Connect requirements, existing system characteristics, candidate patterns, trade-offs, implementation options, evidence, experiments and migration paths.

This layer is reusable knowledge and a decision method. It must not contain a description of a private system. All worked examples must be original synthetic scenarios or independently admissible public cases.

## 1. Requirements and workload profile

Define a reusable profile and authoring template covering:

- Business capabilities, change objectives, stakeholders and measurable outcomes.
- Quality-attribute scenarios: stimulus, operating conditions, affected scope, expected response and measurable acceptance conditions.
- Load: active users, arrival rate, concurrent work, operation mix, payload size, data growth, key skew, peaks and expected growth.
- Latency distributions/SLOs, availability, consistency, durability, freshness, security and cost.
- Budget, delivery time, team capabilities, operational capacity and external constraints.
- Hard constraints versus preferences, priorities, assumptions, unknowns and the evidence needed to resolve them.

Do not infer RPS from user count without behavior assumptions. Do not make an architectural recommendation solely from a user-count or RPS threshold. Missing evidence should produce a measurement or investigation task.

**Deliverable:** a documented profile model and reusable template with a synthetic example.

## 2. Legacy and modernization profile

Define a separate baseline profile:

- Current module and deployment boundaries; runtime, dependencies and contracts.
- Data ownership, shared databases, transaction boundaries and consistency assumptions.
- Versions, unsupported dependencies, coupling, tests, delivery process and operational limitations.
- Observed bottlenecks, incidents, cost drivers and change difficulties; distinguish observations from suspected causes.
- Required behavioral compatibility, allowable downtime, coexistence duration, data migration and rollback constraints.
- Modernization objectives, non-goals and measurable acceptance conditions.

Use observed properties, not the legacy label alone, to narrow candidates. New-system design can omit this profile; modernization must explicitly consider it.

**Deliverable:** a baseline/modernization template with evidence and unknown fields.

## 3. Pattern applicability card

Specify a common card for each architecture style or pattern:

- Stable ID, classification, canonical owner and problem addressed.
- Applicable requirements, workload conditions and prerequisites.
- Contraindications, disqualifying constraints and situations where simpler alternatives suffice.
- Alternatives and combinations; consequences for data, security, reliability, latency, operations, cost and delivery.
- New failure modes, organizational demands and lifecycle costs.
- Relevant implementations and their version-specific limits.
- Supporting source sections, scope of evidence, assumptions and confidence limitations.
- Validation experiment, expected observation, rejection conditions and conditions for revisiting the choice.
- Adoption path for an existing system, compatibility needs and reversibility limits.

Keep architectural styles, patterns, mechanisms and products distinct. A product name must not stand in for a complete architectural decision.

**Deliverable:** a card template and a bounded pilot set; no unsupported whole-catalogue backfill.

## 4. Candidate selection and decision record

Define the workflow:

1. Frame the problem and acceptance conditions.
2. Establish the workload/baseline and record material unknowns.
3. Generate several plausible options, including retaining or improving the current architecture when applicable.
4. Eliminate options violating hard constraints; record the reason and evidence.
5. Compare remaining options by relevant quality attributes, benefits, risks, cost, operational demands and migration effort.
6. Resolve decision-critical uncertainty with source investigation, measurements, prototypes or experiments.
7. Record the choice, alternatives, evidence, consequences and review triggers in an ADR.

Optional scoring must expose weights, uncertainty and sensitivity. It cannot override hard constraints or turn unsupported estimates into facts. The valid outcome can be: insufficient evidence, measure first, retain the existing design, or defer the decision.

Use a testable hypothesis: under conditions X, option Y is expected to improve outcome Z while preserving constraints A; experiment B supports or rejects that expectation.

**Deliverable:** a comparison template, ADR template and decision procedure.

## 5. Target architecture and transition architecture

Represent these separately:

- **Target:** desired responsibilities, data ownership, interfaces, runtime topology and quality outcomes.
- **Transition:** interim states, coexistence of old/new components, boundary interception, routing, compatibility and migration sequencing.
- For each transition step: prerequisites, changes, evidence/checks, measurable go/no-go conditions, observability, rollback or forward-recovery plan and irreversible actions.
- Include data reconciliation, mixed-version operation and externally visible failure behavior.
- Do not assume that choosing a final design establishes a safe route to it.

**Deliverable:** linked target/transition templates and one synthetic incremental-modernization example.

## 6. Navigation and knowledge relationships

Provide four entry routes:

- Requirement → diagnostic questions → candidate patterns.
- Symptom → hypotheses → evidence to gather → candidate remedies.
- Legacy constraint → excluded/viable options → transition choices.
- Modernization objective → measurable outcomes → target and migration alternatives.

Use the established requirement/legacy profiles, applicability cards, candidate comparisons, ADRs, target/transition documents and **existing typed claim-to-source provenance** as the authoritative relationships. Resolve stable document IDs, relevant sections and exact evidence through metadata and ranked retrieval. **Do not implement a curated knowledge graph or maintain a parallel hand-authored set of concept/pattern/decision edges.** The additional maintenance cost has no demonstrated Tycho-specific search/decision benefit.

**Deliverable:** route specification and original worked examples plus evidence-linked navigation through existing document/source IDs. A graph implementation is **not** a dependency.

## 7. Pilot and acceptance criteria

Reuse the three existing pilot categories rather than creating a parallel pilot program:

- One mechanism: assess applicability and limits under a bounded workload.
- One end-to-end process: compare options across data and interaction boundaries.
- One recovery scenario: assess failure behavior and safe transition/recovery.
- Across the pilot set, include both new-system and modernization reasoning and at least one genuinely unanswerable or evidence-insufficient case.

Evaluate whether a reader/agent can:

- Identify required inputs and material unknowns.
- Find applicable candidates, alternatives and contraindications.
- Explain the choice with exact evidence and explicit assumptions.
- Distinguish the target design from the transition plan.
- State how to validate or reject the recommendation and when to revisit it.
- Avoid unjustified migration, fake precision and universal load thresholds.

Record baseline findings and observed results; do not invent measurements or claim independent review. Broader rollout follows demonstrated pilot value.

## Sequencing and current boundary

Design the profiles, card, ADR and transition models first. Align the book structure and pilot contracts with them. Pin public evidence for pilot applicability claims. Implement agreed metadata, source/claim references and section retrieval, and validate the pilots before populating the wider book. A maintained curated concept graph is explicitly out of scope.

This document originated as a plan. Several profiles, templates and examples have since been implemented in scoped issues; do not reset their real GitHub status. The **curated decision graph is removed from scope** as of 2026-10-19. Broader evaluated decision workflows remain subject to actual tests and independent review; do not auto-execute merely because a plan exists.
