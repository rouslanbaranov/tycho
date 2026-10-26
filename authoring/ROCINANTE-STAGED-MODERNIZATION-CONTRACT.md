# Staged modernization proposals for the shared Rocinante specialist

> Owner instruction, 2026-10-26, recorded for Tycho issue
> [#61](https://github.com/rouslanbaranov/tycho/issues/61), milestone M6.
> **Status:** proposed provider-behaviour contract.
> It is not an implemented agent behaviour, prompt, schema, fixture, tool,
> benchmark or evaluation. No Rocinante session produced the example below,
> and no stage outcome, cost, adoption or duration is claimed.

## Purpose and scope

The owner asked the shared specialist **Rocinante** to propose modernization
as a staged evolution instead of one target diagram with a migration
appendix: a proof-of-concept stage, a minimum-viable-product stage and a
product stage, optional sub-stages inside each, architecture that may change
from stage to stage, and an explicit justification at every stage that cites
Tycho as its evidence source.

This contract defines that behaviour at the Tycho provider boundary. It
applies when a question is modernization-shaped: an existing system, a
claimed or observed deficiency, and a proposed architectural change.

Out of scope:

- Rocinante's runtime, identity, general operating instructions and
  multi-provider routing, owned at the platform integration level.
- Tycho's retrieval envelope, decision outcomes and tool surface. Those keep
  [retrieval contracts](models/retrieval-contracts.md),
  [decision navigation](models/decision-navigation.md) and
  [the agent tool contract](MCP-AGENT-TOOL-CONTRACT.md) as canonical owners.
- The reader-facing explanation of target and transition states, which stays
  in the book: V10/C05, listed at
  [the decisions landing](../book/decisions/README.md).

This document adds only the staged proposal: its ladder, its evidence
obligations, its output shape and its refusal rules.

## What "provable" means here

Architectural fitness cannot be proved by a citation, a diagram or a
successful demonstration. [The authoring methodology](METHODOLOGY.md) already
separates published claims, reproduced observations, inference, proposals and
unknowns, and states that a test proves only the exercised scenario. The
contract therefore replaces "proof" with three checkable obligations:

1. **Support.** Every material claim names an exact Tycho page and section,
   or an explicit local observation class. Page IDs resolve in
   [the generated route index](../generated/route-index.v1.json).
2. **Falsification.** Every stage states, before it runs, the observation
   that would reject its own claim, including a negative case.
3. **Limits.** Every claim states applicability, version or workload scope
   and what remains unknown. An unsupported claim is deleted, not softened.

A proposal that cannot meet these obligations returns
`INSUFFICIENT_EVIDENCE` with a finite request. Confident architecture
language is not a substitute for the missing observation.

## Stage ladder

POC, MVP and Product follow the owner's instruction. They are Tycho working
labels with the definitions below, not a standardized taxonomy and not a
schedule. A stage ends when its pre-agreed evidence exists, not when a date
passes.

The labels come from product development, where they usually gate demand and
usability evidence. Here they gate architectural and operational evidence:
feasibility, one real journey under production constraints, then the full
operating envelope. Market, pricing and adoption claims are out of scope;
Rocinante must not import product-validation language into an architecture
gate.

| ID | Stage | Question the stage must answer |
|---|---|---|
| B0 | Baseline gate | Is the design adequate, and what exactly is deficient? |
| P0 | Proof of concept | Is the decisive technical claim true? |
| P1 | Minimum viable product | Does one real journey work in production? |
| P2 | Product | Does the agreed operating envelope hold at scope? |

`B0` is not a delivery stage. It may end the proposal with `RETAIN`,
`STABILIZE_FIRST` or `MEASURE_FIRST`; a target without a baseline is only a
hypothesis.

~~~mermaid
flowchart TD
  Q["Modernization objective"] --> B["B0 baseline and hard gates"]
  B -->|baseline adequate| R["RETAIN or STABILIZE_FIRST"]
  B -->|decisive unknown| MF["MEASURE_FIRST"]
  B -->|proceed| P01["P0.1 claim and falsifier"]
  P01 --> P02["P0.2 minimal slice"]
  P02 --> P03["P0.3 observe and decide"]
  P03 --> G0{"P0 exit gate"}
  G0 -->|inconclusive| MF2["Named measurement task"]
  G0 -->|hard gate fails| X["CONTRAINDICATED: exclude"]
  G0 -->|pass| P11["P1.1 journey and coexistence"]
  P11 --> P12["P1.2 first operating configuration"]
  P12 --> P13["P1.3 measured outcome"]
  P13 --> G1{"P1 exit gate"}
  G1 -->|unknown| HOLD["Hold: do not advance"]
  G1 -->|pass| P21["P2.1 broadening increments"]
  P21 --> P22["P2.2 envelope verification"]
  P22 --> P23["P2.3 contract and retire"]
  P23 --> DONE["Product: target operating envelope"]
  MF2 --> P01
  HOLD --> P13
~~~

Text alternative: a modernization objective first passes a baseline gate that
may end in retain, stabilize or measure. Otherwise the proposal enters a
proof of concept whose exit gate can be inconclusive, disqualifying or
passing. Only a passing proof of concept opens the minimum-viable-product
stage, and only its exit gate opens the product stage. An unknown P1 gate
holds the proposal where it is; the diagram does not show a schedule.

### P0 — proof of concept

Purpose: reduce the single highest-consequence uncertainty to one observed
result. P0 may be disposable, uses non-production data and makes no
user-visible commitment.

- **P0.1 Claim and falsifier.** State the claim, the exact observation that
  would reject it, the negative case and the reversal condition.
- **P0.2 Minimal slice.** Build the thinnest executable path across the
  boundary under test. No production consumer, authoritative write or
  irreversible effect.
- **P0.3 Observation and disposition.** Record supports, contradicts or
  inconclusive with the actual observation. A negative result is a valid P0
  outcome and must change or stop the proposal.

Exit gate: the pre-registered falsifier has been exercised. A P0 that only
reports that a technology runs has not answered its question.

### P1 — minimum viable product

Purpose: prove one real user journey end to end under production constraints,
for a bounded cohort, while remaining reversible by default. The P1
architecture must be a legitimate transition state of the intended target, or
the proposal must declare P1 as a second rewrite and justify the cost.

- **P1.1 Journey and coexistence contract.** One journey, one authoritative
  writer per invariant, a compatibility matrix, and rollback or
  forward-repair.
- **P1.2 First operating configuration.** Enter gate: compatibility,
  invariant, recovery and ownership evidence.
- **P1.3 Measured outcome and operational proof.** Pre-agreed user and
  operational thresholds measured under a recorded workload; named on-call,
  runbook and an exercised recovery.
- **P1.4 Continuation decision.** Continue, revise the target, return to P0
  or retain. Contracting transition machinery is a later gate, not a P1 exit.

### P2 — product

Purpose: reach the agreed operating envelope and retire transition machinery
on evidence.

- **P2.1 Broadening increments.** Each cohort, region or capability gets its
  own gate. There is no single "roll out everything" step.
- **P2.2 Envelope verification.** Measured capacity, latency, error budget,
  security, cost and recovery at the agreed workload.
- **P2.3 Contract and retirement.** Remove compatibility shims and the old
  authoritative path only with decommission evidence; record residual debt
  and revisit triggers.

Exit gate: the target state operates and the transition state is gone. Until
retirement, the proposal is not a product claim.

A proposal may omit a sub-stage that does not apply, but must state the
reason and must not omit the evidence class that sub-stage owns. Sub-stages
may merge only when the merged gate still records both observations. A
proposal may add a sub-stage when a stage needs a distinct observation; the
added sub-stage names its own gate.

A stage may be omitted when its question is already answered by cited
evidence, and the omission is recorded with that evidence. Omitting a stage
does not omit its evidence class. The ladder is a checklist for reasoning,
not a mandatory sequence of projects.

## Architecture evolution rules

Each stage declares its architecture as a transition state, not as a variant
of the final diagram. The [target/transition model](models/target-transition-architecture.md)
owns the state fields; the proposal inherits them per stage: live topology,
compatibility matrix, data path, deployment guard, exit guard, recovery and
provenance.

- **P0 may be thrown away.** Nothing from P0 enters production without a P1
  re-validation.
- **P1 must be a transition state of the target.** If it cannot be, the
  proposal declares P1 as a rewrite and states the cost of discarding it.
- **P2 retires the transition.** A target without a retirement stage is an
  unfinished migration, not a product.
- **One irreversible change per gate.** Parity work, migration and
  optimization are separate stages. Bundling them hides which change caused a
  failure; the [Airbnb build migration](../book/cases/airbnb-jvm-monorepo-bazel.md)
  records the parity-before-optimization lesson.
- **A stage justifies a choice among alternatives.** It names the rejected
  options, including retain, and the condition that would reverse the choice.
- **Architecture may shrink.** Retaining or simplifying a component is a valid
  evolution; additional components require a measured benefit.
- **A changed decision is superseded, not overwritten.** The
  [ADR model](models/candidate-comparison-adr.md) owns the record.
- **Temporary structure needs an owner and a removal gate.** Temporary does not
  exempt a component from operation, security or cost.
- **The old path stays authoritative until its gate.** A derived path may
  serve reads early; it may not own an invariant before the cutover gate.

## Evidence obligations

Every material claim receives an evidence row. A claim without a row is not
part of the proposal.

| Field | Content |
|---|---|
| Claim | One testable assertion, not a topic. |
| Class | Published fact, synthesis, inference, proposal or unknown. |
| Tycho anchor | Page ID, section heading and snapshot ID. |
| Source IDs | Source identities the page exposes, when present. |
| Relation | Supports, qualifies, contradicts or unavailable. |
| Scope | Applicability, version or workload limit. |
| Local check | Observation class that would satisfy a stage gate. |

Rules:

1. A Tycho page is evidence about the field: mechanisms, applicability and
   published experience. It is never evidence about the queried system.
2. A local claim needs a local observation class: measurement, test, review or
   named approval. A citation cannot substitute for it.
3. `unknown` is a result. It creates a finite request with an owner and a
   falsifier; it does not become an optimistic assumption.
4. Contradicting evidence is shown, not averaged. A page that qualifies or
   limits a mechanism is cited with that limit.
5. No invented numbers, dates, costs, adoption or review outcomes. A target
   threshold is a parameter to agree, not an observed value.
6. Gates are registered before the observation. Reopening a gate requires a
   new observation, not a re-reading of the same evidence.
7. Citations resolve at one snapshot. An unavailable source is reported as
   `source-unavailable`; the agent must not reconstruct unseen text.
8. A citation is not an approval. Approval requires the named decision owner.
9. Every stage carries at least one Tycho anchor for its method and at least
   one local check for its gate. A stage with anchors but no local check is
   not a gate; a stage with a local check but no anchor is an unexamined
   design.

## Proof obligations by stage

| Stage | Must show | Not sufficient |
|---|---|---|
| B0 | Deficiency, hard gates, retain alternative | A current-state diagram |
| P0 | Pre-registered falsifier and its observation | "The technology works" |
| P1 | Journey, compatibility, recovery, ownership | A successful deployment |
| P2 | Envelope measurements, decommission evidence | A rollout percentage |

An empty cell is an unknown, not a pass. A weighted score never overrides a
failed or unknown hard gate.

## Proposal envelope

This is a logical envelope, not a JSON Schema and not a tool response. It
extends the [decision-navigation envelope](models/decision-navigation.md);
fields not listed here keep that owner's meaning.

- `proposal_status`: `proposed`, `retain` or `insufficient-evidence`.
- `entry_route`: from the decision-navigation envelope.
- `baseline_gate`: deficiency, hard gates and alternatives including retain.
- `stages`: ordered stage objects.
- `recommended_stage`: one stage or null, never a vague "start anywhere".
- `citations`: snapshot ID, page ID, section and source IDs.
- `non_claims`: what this proposal does not establish.
- `review`: `not-assigned` until a named owner acts.

Each stage object carries `stage_id`, `question`, `architecture_delta`,
`transition_state`, `evidence_rows`, `enter_gate`, `exit_gate`,
`reversibility`, `stop_conditions`, `unknowns` and `next_evidence`.

`architecture_delta` names what changes in responsibilities, interfaces, state
authority, runtime or deployment, and operational ownership. A stage with no
delta still states that the architecture is unchanged and why that is enough.

The response must remain readable without the envelope: a prose or table
summary of stages, gates and unknowns is required. Structured fields are for
tooling and review, not a substitute for explanation.

## Stage gates and abstention

Stage outcomes reuse the
[decision-navigation outcome codes](models/decision-navigation.md):

- Missing baseline evidence: `MEASURE_FIRST`.
- P0 inconclusive: `INSUFFICIENT_EVIDENCE` with the next observation.
- P0 contradicts a hard gate: `CONTRAINDICATED`; exclude the candidate.
- P1 gate unknown: hold at P1; do not advance to P2.
- P2 without decommission evidence: `CONDITIONAL_CANDIDATE`, not product.
- Retain is a complete answer at any stage.

A stage gate is `pass`, `fail` or `unknown`. `unknown` blocks progression.
The proposal must name the missing observation, its owner and what result
would change the gate.

## Behaviours the contract rejects

- **Stage theatre.** POC, MVP and Product labels with the same exit evidence.
- **POC as product.** Carrying a throwaway P0 design into production.
- **Evidence laundering.** Citing a Tycho page as proof of local behaviour.
- **Hidden irreversibility.** A P1 step that removes rollback without an
  approved no-return gate.
- **Calendar fiction.** Promising durations, costs or adoption.
- **Single-option ladder.** No retain or materially different alternative.
- **Borrowed success.** "A published company did it" as local evidence.
- **Orphan temporary structure.** A shim without an owner or removal gate.
- **Unqualified proof language.** "Proven", "guaranteed" or "production-ready"
  without the exact observation and scope.

## Worked synthetic example

All names, constraints and observations below are invented for this contract.
The example is a proposal skeleton, not an executed migration; no measurement,
approval or production observation exists.

**Synthetic system:** a document-archive reading service. A relational store
is the authoritative writer and serves reads through a nightly denormalized
table. The proposed change is a projection-backed read path fed by change
events, with per-requester authorization filtering and an agreed freshness
window for deletions and revocations.

**B0 — baseline.** The reported deficiency is slow reads under an unrecorded
workload. Exit evidence: a recorded workload profile, the authorization and
retention hard gates, and a retain or tune alternative. Reversal: not
applicable.

**P0 — proof of concept.**

- *Claim:* an event-fed projection can serve authorized reads while exposing
  a deletion or revocation inside the agreed freshness window.
- *Falsifier:* a revoked record remains readable after that window in a
  shadow comparison, or the projection cannot be rebuilt from the change log
  without losing deletes.
- *Evidence row:* class proposal; anchors V10/C05 no-return gates and V02/C06
  coexistence; local check the shadow revoke comparison; limit the projection
  freshness depends on a change log whose delete behaviour is unverified.
- *Architecture delta:* a disposable capture table and a rebuild script; no
  production consumer.
- *Slice:* one synthetic collection, synthetic records, shadow reads only.
- *Illustrative disposition:* the legacy change log emits updates but not
  deletes, so the falsifier cannot be exercised. Gate: `INSUFFICIENT_EVIDENCE`
  with a named task to add delete events or an authorized full rebuild. The
  proposal does not advance on a partial success.

**P1 — minimum viable product.** Only if P0 passes.

- *Journey:* one internal cohort reads through the projection while the
  relational store remains the only authoritative writer.
- *Architecture delta:* the disposable capture table is replaced by a
  transactional outbox; a derived read path, an authorization filter, a
  rebuild procedure and a routing switch back to the old read table.
- *Enter gate:* unchanged read API, revocation test, source-to-projection
  reconciliation, named on-call owner.
- *Exit gate:* pre-agreed freshness and error thresholds measured under the
  recorded workload; an exercised rollback returns reads to the old table.

**P2 — product.** Broadening to all tenants.

- P2.1: one tenant group per increment with the same gate.
- P2.2: capacity, latency, cost, retention and authorization review at the
  agreed envelope.
- P2.3: remove the nightly table from the read path only after decommission
  evidence, then record residual debt and revisit triggers.

The example deliberately contains no latency, throughput, cost or duration
figures. Supplying one would be an invented measurement.

## Tycho evidence map

Each proposal reads these canonical owners instead of restating them. Page
IDs resolve in [the generated route index](../generated/route-index.v1.json).

- Target and transition states: `tycho.page.cf0ce38c73e44950aec5a9c2869bee63`
  (V10/C05, *Purpose and mission*).
- Migration mechanisms and no-return gates:
  `tycho.page.ea1c3ca31f974bcbb6a432c55e56bc03` (V10/C05, §6–§7).
- Rollback and reconciliation:
  `tycho.page.47b67ebf3dbf477e818e83f9e1683ffe` (V10/C05).
- State authority: `tycho.page.78d0f89ac4184b19bfef3a72e8b4f2cc` (V10/C05).
- Alternatives and ADRs:
  `tycho.page.f05854fcc406435bbf38a192bc7ab2f1` (V10/C04).
- Applicability and contraindications:
  `tycho.page.2176fe3dcdf24a199d1656cba602e8e1` (V10/C03).
- Baseline and modernization evidence:
  `tycho.page.b2d1285c1c1a4a698a2306c4e766a4f1` (V10/C02).
- Requirements and workload:
  `tycho.page.868027aee4884210bea1d8a6542fbfb0` (V10/C01).
- Overload and degradation: `tycho.page.c5d20ae7ef6445e5b23dd5fbac625060`
  (V07/C05, *Overload protection, admission control and graceful
  degradation*).
- Progressive delivery: `tycho.page.b938ff1a06264492a425f2eff555ae7d`
  (V08/C04, *GitOps, rolling, blue/green and canary release architecture*).
- Coexistence adapters: `tycho.page.31c8e450f78c451d90cb6090df330c5a`
  (V02/C06, *Anti-corruption adapters: semantic translation and safe
  coexistence*).
- Service levels: `tycho.page.c987c475cc5340bcb967f4b6f963b295`
  (V09/C01, *User-visible service indicators, objectives and error-budget
  decisions*).
- Published POC gate and negative POC result:
  [Airbnb build migration](../book/cases/airbnb-jvm-monorepo-bazel.md) and
  [Cloudflare object copy](../book/cases/cloudflare-super-slurper-queues.md).

These are method owners. None proves that a proposed stage will work in the
queried system; that requires the local gate.

The public sources behind these mechanics are recorded, with their limits, in
[the target/transition model](models/target-transition-architecture.md)
(arc42 runtime and deployment views, AWS strangler-fig and
branch-by-abstraction guidance, Martin Fowler's Parallel Change),
[decision navigation](models/decision-navigation.md) (arc42 §9 decision
records) and V10/C05 (Strangler Fig and Microsoft guidance). This contract
adds no new source inspection. The case pages above are publisher-reported
and time-scoped, with their own evidence limits; a POC result in one workload
does not transfer to another.

## Review and non-claims

- `human_review: not-performed`; `sufficient: 0`.
- No independent reviewer, owner acceptance, conformance fixture, benchmark
  or end-to-end evaluation of a Rocinante staged proposal exists.
- No Tycho MCP tool change is implied. The current tools are extractive and
  return no final recommendation; the staged proposal is composed by the
  calling agent or orchestrator from cited evidence.
- No book edition change is implied. Reader-facing explanation remains
  V10/C04 and V10/C05; promoting this method into a new book page would need
  edition, inventory and index work under the existing contracts.
- The Mermaid figure was reviewed manually; no Mermaid parser was available
  in the repository during authoring.

## Open questions

- Does the ladder belong in the versioned provider instruction module (#62),
  in Rocinante's shared package, or in both?
- Should stage objects become a versioned schema and compatibility fixtures
  (#62, #63), and what would a negative fixture prove?
- Does the MCP surface need a stage-planning tool, or should composition stay
  client-side? The current contract says client-side; changing that is an
  owner decision.
- Which evaluation measures proposal quality (#64, K28): falsifier coverage,
  citation precision, correct abstention, stage-gate discipline or cost?
- Who approves each stage gate in a real deployment? Tycho and Rocinante can
  supply method and evidence, not authority.

## Change control

Version 1, 2026-10-26. The owner's instruction is the authority for the
staged shape; every stage definition, evidence rule and refusal rule above is
Tycho's proposed implementation of it. Revise by superseding this document
and updating the links in
[the knowledge-platform plan](knowledge-platform-and-mcp-plan.md),
[decision navigation](models/decision-navigation.md) and
[the target/transition model](models/target-transition-architecture.md).
