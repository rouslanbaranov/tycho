---
metadata_version: 1
id: "tycho.volume.fd0c1a798f9968eed4a679b048deea14"
kind: "volume"
parent_id: "tycho.book.37c50125355948f1b52ec66229ef59bd"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/README.md"
title: "V12 - Architecture modeling, simulation and decision validation"
topic_ids:
  - "simulation"
  - "model-validation"
  - "decision-records"
perspectives:
  - "architecture"
  - "evaluation"
  - "operations"
  - "migration"
summary: "Isolated V12 volume: simulation evidence, decision records and limits."
route_hints:
  questions:
    - "Which alternative is defensible, and what would reverse it?"
    - "How are verification, calibration and decision evidence kept apart?"
  prerequisites: []
  related_ids:
    - "tycho.chapter.6006603befaacfc1baadc486a0f7007a"
    - "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
    - "tycho.chapter.ad6455916f994c0e22e0df7881857f23"
    - "tycho.chapter.9548ac72fafbee8773ad7309a51d512b"
    - "tycho.chapter.2147ec1471d027ef256437a345f9c1e7"
    - "tycho.chapter.26ddd5ca6c1bea39738561c3bdb1cf23"
    - "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
  excludes:
    - "No production measurement, independent review or pattern promotion is asserted."
  keywords:
    - "simulation"
    - "system dynamics"
    - "discrete-event simulation"
    - "Monte Carlo"
    - "decision record"
    - "model validation"
evidence_scope:
  source_ids:
    - "src.simpy"
    - "src.owen-monte-carlo"
    - "src.sargent-vv"
    - "src.jcgm-100"
    - "src.madr"
    - "src.nygard-adr"
    - "src.little-law"
  claim_ids: []
  status: "source-linked"
  notes: "Volume navigation only; page-local ledgers are authoritative for limits."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# V12 - Architecture modeling, simulation and decision validation

**Status:** self-checked V12 candidate, 2026-10-29. The volume, contracts, reference
engine, experiments, decision records and validators are present in this tree. No
production measurement, independent review, owner acceptance or pattern promotion is
asserted. The independent review gate is recorded separately when it runs.

## Purpose and mission

V12 helps a reader evaluate architecture alternatives before costly implementation. It
combines stock-and-flow reasoning, discrete-event simulation, Monte Carlo uncertainty,
comparative decision records and staged modernization-path simulation. The result is
quantitative decision evidence with explicit assumptions, not a proof that a design is
correct, secure, compliant or safe to migrate.

The volume is deliberately isolated:

> **V12 references existing patterns. Existing patterns do not reference V12.**

V12 pages may link to existing `tycho.pattern.*` identifiers and canonical owner pages.
Existing cards, owner pages, frontmatter, page identifiers, source ledgers, review records
and promotion hashes are not edited. Reverse discoverability comes from a derived index,
not from writing back into the existing corpus.

## What this volume does and does not do

It does:

- state a model boundary, state variables, units, parameters and validity limits;
- execute deterministic reference cases and seeded discrete-event simulations;
- report uncertainty, convergence and sensitivity rather than one number;
- compare candidates on identical workloads and business-comparable metrics;
- record a recommendation, a no-recommendation outcome or an explicit
  `insufficient-evidence` outcome;
- preserve hashes, seeds and replay instructions for every stored run.

It does not:

- promote, demote or re-review an existing pattern;
- claim that a simulation proves production behavior;
- treat a source claim as a calibrated parameter;
- replace security, compliance, legal or operational review;
- hide a hard constraint inside a weighted score.

## Five evidence layers

| Layer | Question | Owner |
|---|---|---|
| Source and claim | Does a source support the method? | Ledger and page citations |
| Verification | Is the model implemented as specified? | Model spec and tests |
| Calibration | Do parameters match measured reality? | Calibration record |
| Simulation | What happens under the assumptions? | Scenario and run records |
| Decision | Does it follow from model and constraints? | Decision record |

The layers are separate. A `model-verified` label does not imply calibration. A
`decision-supported` record may coexist with an `uncalibrated` model when the decision is
explicitly conditional. Simulation results never promote a pattern to `sufficient`.

## Volume map

- [C01 - Foundations](c01-foundations/README.md): stock and flow, scope, evidence.
- [C02 - Contracts](c02-contracts/README.md): model, scenario, run, decision.
- [C03 - Deterministic and DES](c03-deterministic-and-des/README.md): queues and retries.
- [C04 - Monte Carlo](c04-monte-carlo/README.md): sensitivity and convergence.
- [C05 - Decision integration](c05-decision-integration/README.md): links and outcomes.
- [C06 - Migration simulation](c06-migration-simulation/README.md): coexistence and rollback.
- [C07 - Validation and limits](c07-validation-and-limits/README.md): gates and replay.

~~~mermaid
flowchart LR
    Q["Bounded architecture question"] --> M["Model contract"]
    M --> S["Scenario contract"]
    S --> R["Seeded run"]
    R --> U["Uncertainty and sensitivity"]
    U --> D["Decision record"]
    D --> P["Existing pattern owner, read-only"]
    D --> X["Explicit limits or insufficient evidence"]
~~~

Text alternative: a bounded question becomes a model contract and a scenario contract.
A seeded run produces metrics, uncertainty and sensitivity. Those feed a decision record
that links one way to existing pattern owners and states either a conditional
recommendation or an insufficient-evidence outcome.

## A worked cross-chapter synthesis

A synthetic checkout service receives 20 requests per second for 30 minutes after a
five-minute warmup. Three candidates use the same arrivals, duration, seed scheme and
metrics:

- A: direct capacity with a one-second deadline and no retry budget;
- B: a bounded queue, a two-second deadline and a small retry budget;
- C: more servers, a slower mean service time and a higher unit cost.

Under the declared assumptions, B succeeds on 0.9996 of offered requests with a
1.206-second p95 latency and 1.34 relative cost units per 1000 successes. A succeeds on
0.9218 with a 0.870-second p95 and 1.81 cost units. C succeeds on 0.9679 but exceeds the
declared 3.0 cost and 1.5-second p95 constraints. The decision
record recommends B for the synthetic workload, records the non-quantitative operability
constraint as unverified and lists the measurements that would reverse the choice.

A second experiment compares a staged modernization cutover with a no-cutover baseline.
The staged model's maximum divergence is 8,925.5 records (95% CI 5,561.6-12,289.3), and
rollback completes in only 10% of replications within the 2,400-second horizon. Because
dual-write lag and reconciliation capacity are assumed rather than measured, the decision
record returns `insufficient-evidence`, not a recommendation.

## Machine artifacts

The volume is not only prose. The following artifacts are part of the deliverable:

| Artifact | Path | Purpose |
|---|---|---|
| Model contracts | `edition/v12/models/` | State, parameters, invariants and verification |
| Scenario contracts | `edition/v12/scenarios/` | Workload, configuration, seeds and metrics |
| Run records | `edition/v12/runs/` | Metrics, convergence, hashes and limits |
| Decision records | `edition/v12/decisions/` | Candidates, constraints and outcome |
| Source ledger | `edition/v12/reading-ledger.v1.json` | Read units, hashes and omissions |
| Reverse index | `edition/v12/reverse-index.v1.json` | Derived pattern-to-artifact lookup |

Reproduce a stored run from the repository root:

~~~text
python3 scripts/v12_engine.py run \
  --model edition/v12/models/checkout-des.json \
  --scenario edition/v12/scenarios/checkout-b-queue.json \
  --out /tmp/checkout-b.json
python3 scripts/v12_engine.py replay \
  --run edition/v12/runs/checkout-b-queue.json \
  --model edition/v12/models/checkout-des.json \
  --scenario edition/v12/scenarios/checkout-b-queue.json
~~~

The replay command recomputes the result hash and fails if the model, scenario or engine
output has drifted. It proves deterministic replay for the exercised inputs, not model
validity.

## Evidence and limits

The source ledger records the exact unit, representation hash, sections read, omissions
and limits for each admitted source. The engine tests exercise conservation, boundary
cases, event ordering, retries, convergence and sensitivity ranking. Those tests prove the
implemented reference cases; they do not validate a real system.

All numeric workloads in this volume are synthetic. The confidence intervals use a normal
approximation across replications. The sensitivity screen uses a quadratic response-surface
decomposition, not a full pick-freeze Sobol analysis. Calibration is `uncalibrated` for
every model. Independent review and owner acceptance remain separate decisions.

## Navigation and boundaries

| Route | Destination |
|---|---|
| Foundations | [C01 - Foundations](c01-foundations/README.md) |
| Contracts | [C02 - Contracts](c02-contracts/README.md) |
| Deterministic and DES | [C03 - Deterministic and DES](c03-deterministic-and-des/README.md) |
| Monte Carlo | [C04 - Monte Carlo](c04-monte-carlo/README.md) |
| Decision integration | [C05 - Decision integration](c05-decision-integration/README.md) |
| Migration simulation | [C06 - Migration simulation](c06-migration-simulation/README.md) |
| Validation and limits | [C07 - Validation and limits](c07-validation-and-limits/README.md) |
| Existing patterns | [V11 Pattern atlas](../v11-pattern-atlas/README.md) |

The volume does not replace the technical owner of any pattern. Read the linked owner page
before treating a mechanism claim as established. When the model and the owner disagree,
the disagreement is evidence to record, not a reason to edit the owner.
