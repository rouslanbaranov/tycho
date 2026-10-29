---
metadata_version: 1
id: "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
kind: "page"
parent_id: "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-limits/validation-gates.md"
title: "V12 validation gates"
topic_ids:
  - "model-validation"
  - "reproducibility"
perspectives:
  - "evaluation"
  - "architecture"
summary: "The V12-A to V12-F gate matrix, with local evidence and separate review."
route_hints:
  questions:
    - "Which validation gates does V12 pass?"
    - "What do the gates not establish?"
  prerequisites: []
  related_ids:
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
    - "tycho.page.b0c704c825b2faf15a1d118dc9a6b1cc"
    - "tycho.page.6c54ed1288a4f0806889865916dc8ccf"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "validation gates"
    - "structure"
    - "calibration"
    - "decision validity"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
    - "src.plos-repro"
    - "src.jcgm-100"
  claim_ids: []
  status: "source-linked"
  notes: "Page-local source records and limits; not independent review."
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

# V12 validation gates

**Question.** Which structural, model, statistical, calibration, decision and review gates
does V12 pass, and what evidence supports each one?

**Short answer.** V12-A through V12-E are implemented and checked locally. V12-F is an
independent review gate and is recorded separately. A passing local check is not independent
review, CI, owner acceptance or production validity.

## The gate matrix

| Gate | Scope | Status |
|---|---|---|
| V12-A | Structure, schemas, unique IDs, links, hashes | implemented |
| V12-B | Units, conservation, boundaries, event order | implemented |
| V12-C | Seeds, convergence, sensitivity, correlation | implemented |
| V12-D | Calibration status and validity limits | implemented |
| V12-E | Decision validity and insufficient evidence | implemented |
| V12-F | Independent read-only review | separate gate |

The validator scripts/validate_v12.py checks the structural gates. The engine tests check the
model and statistical gates. The model contracts and decision records carry the calibration
and decision evidence. The review gate is not claimed by the validator.

## V12-A: structural

The validator checks:

- every V12 document has valid strict frontmatter;
- volume, chapter and page identifiers are unique;
- model, scenario, run and decision identifiers are unique;
- every scenario model_id resolves;
- every run model_id and scenario_id resolve;
- every decision candidate run resolves;
- every pattern identifier and owner page resolves in the existing registry;
- every stored hash matches the current model or scenario file;
- the reverse index is derived from the records, not hand-edited;
- no protected existing page or card references V12.

The last check is the iron rule. It scans the existing book outside the V12 directory for V12
paths and V12-only identifiers. A violation fails the gate.

## V12-B: model correctness

The engine tests cover conservation, non-negativity, zero arrivals, zero capacity, queue
saturation, event ordering, timeout interaction, retry conservation and deterministic
replay. The model contracts record the cases and test paths. The tests do not prove
operational validity.

## V12-C: statistical validity

The run records report seeds, replications, standard errors, confidence intervals and a
convergence status. The sensitivity run reports a quadratic response-surface screen and is
marked insufficient-sample. The scenario declares correlated inputs and the run reports the
method. A run that fails the 0.02 relative-error threshold is not used as converged evidence.

## V12-D: calibration

Every model is uncalibrated. The model contracts list each parameter's evidence status and
the missing measurement. The decision records repeat the status. No production claim is made.

## V12-E: decision validity

The decision records declare:

- candidates and their runs;
- hard, soft and non-quantitative constraints;
- business-comparable metrics with units;
- evidence statuses for model verification, calibration and simulation;
- an explicit recommendation or a no-recommendation outcome;
- non-quantitative constraints kept separate;
- reversal triggers and limitations.

The checkout record is decision-supported under its declared constraints. The modernization
record is insufficient evidence. Both are valid outcomes.

## V12-F: independent review

The independent review gate requires a fresh read-only reviewer outside the authoring
session. It checks the V12 artifacts and does not rerun the test suite. Its report is stored
verbatim, indexed with a SHA-256 and linked from the review record. A pass is not owner
acceptance and does not promote a pattern.

The review status is recorded in the V12 review record, not inferred from this page.

## What the gates do not establish

- They do not establish that the source claims are true; the source ledger records what was
  read and what was not.
- They do not establish that the models match a real system.
- They do not establish that the decisions are accepted by the owner.
- They do not establish CI, deployment or production behavior.
- They do not promote any existing pattern.

## A gate flow

~~~mermaid
flowchart LR
    A["V12-A Structure"] --> B["V12-B Model"]
    B --> C["V12-C Statistical"]
    C --> D["V12-D Calibration"]
    D --> E["V12-E Decision"]
    E --> F["V12-F Review"]
~~~

Text alternative: structural checks precede model checks, statistical checks, calibration,
decision validity and independent review. A later gate cannot substitute for an earlier one.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports the verification and validation distinction and the data/conceptual/operational
  validity split.
  It does not certify the V12 gates.
- [PLOS Ten Simple
  Rules](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
  supports reproducible inputs, scripts, parameters and environments.
  It does not establish that the V12 artifacts are reproducible on every platform.
- JCGM 100:2008 (source src.jcgm-100; see the reading ledger)
  supports uncertainty vocabulary.
  It does not establish a V12 uncertainty budget.

## Navigation

- Parent: [V12/C07 - Validation and limits](../README.md)
- Previous: [Calibration and validity limits](calibration-and-validity-limits.md)
- Next: [Reproducibility and replay](reproducibility-and-replay.md)
- Validator: scripts/validate_v12.py
