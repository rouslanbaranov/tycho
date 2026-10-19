# Evidence-backed Architecture Decision Record (ADR) template

> Use alongside the [Tycho candidate-comparison method](../authoring/models/candidate-comparison-adr.md). An ADR is a record of a decision and its evidence, not a substitute for a benchmark. Never auto-set status to accepted from a repository merge.

## ADR identity and governance

- ADR ID, version, date, author and required approval authority:
- Status: **proposed / accepted / rejected / superseded**, with actual decision date and link to successor:
- Context: named business scenario, capabilities, [requirements/workload profile](../authoring/models/requirements-workload-profile.md), and [legacy baseline](../authoring/models/legacy-modernization-profile.md) where applicable:
- Decision boundary: owner of state/transactions, affected interfaces, versions, users and neighboring systems:
- Non-goals and excluded domains:
- Evidence snapshot, provenance and review timestamp:

## Objective and quality gates

| Requirement ID | Hard constraint or preference | Unit, environment, window and evidence | Named gate test | State: pass, fail, unknown |
|---|---|---|---|---|
| REQ-1 | | | | |

An unknown *hard* gate must not be silently approved. Record a required experiment and owner. A failed hard gate vetoes the option regardless of any weighted ranking.

## Options: always include the baseline

| Option ID | Description and status | Benefits under stated workload | Risks and failure effects | Operations, migration, reversibility |
|---|---|---|---|---|
| A | Retain, stabilize or incrementally improve the existing design (greenfield: simplest adequate design) | | | |
| B | Candidate with explicit pattern applicability card | | | |
| C | Distinct alternative or explicit no-change | | | |

## Evidence, comparison and counterexamples

| Claim ID | Option and falsifiable hypothesis | Exact public section / measurement window | Fact, assumption or inference | Confidence limits | Rejection observation |
|---|---|---|---|---|---|
| E1 | | | | | |

If using weighted preferences, show the weight-sum check, the observed-or-subjective nature of ratings, and a sensitivity test where preferences or unknown scores change. Do not combine hard gates into a weighted sum. Explicitly record alternatives rejected and *why*.

## Decision and consequences

**Decision:** candidate / retain / measure first / no feasible option / accepted by actual authority.

**Rationale:** why this option dominates *at the stated boundary*, despite its costs, unknowns and alternative explanations.

**Positive consequences:**

**Negative and neutral consequences:**

**Version/compatibility consequences:** including new attack surfaces, schema/client overlap, upgrade conditions.

**Operational commitments:** monitoring, on-call burden, cost ceilings, failure tests, acceptance, permissions.

## Validation and transition contract

- Controlled experiment(s), success/rejection metrics, data, baseline and reproducible configuration:
- Rollout stages and interim topology, with owners and client/data compatibility:
- Go/no-go checks, hold points and rollback or forward-recovery boundary:
- Irreversible effects, backfill/reconciliation and failure recovery:
- Decision expiry/revisit triggers: new load, new version, incident, lost evidence or new constraint:
- Independent approver and actual review outcome; if unavailable, remain **proposed**:

## Verification

- Relative links actually checked:
- Source/rights bounds and exact sections actually inspected:
- Numeric/scenario sanity checks actually performed:
- Tests executed versus proposed:
- Remaining decision-critical unknowns:

Example: [fictional workshop registration decision](../examples/synthetic-workshop-adr.md).