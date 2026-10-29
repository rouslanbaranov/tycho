---
metadata_version: 1
id: "tycho.page.6c54ed1288a4f0806889865916dc8ccf"
kind: "page"
parent_id: "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-limits/reproducibility-and-replay.md"
title: "Reproducibility and replay"
topic_ids:
  - "reproducibility"
  - "provenance"
perspectives:
  - "operations"
  - "evaluation"
summary: "Hashes, seeds, environment and replay limits for every stored V12 run."
route_hints:
  questions:
    - "What makes a V12 result replayable?"
    - "What does a successful replay not prove?"
  prerequisites: []
  related_ids:
    - "tycho.page.201248045fa3cd67e617ce04a1c56feb"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
    - "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "replay"
    - "hash"
    - "seed"
    - "environment"
    - "provenance"
evidence_scope:
  source_ids:
    - "src.plos-repro"
    - "src.w3c-prov-o"
    - "src.sargent-vv"
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

# Reproducibility and replay

**Question.** What makes a V12 result replayable, and what does a successful replay not prove?

**Short answer.** A replayable result has a versioned model, a versioned scenario, a stored
seed, a stored engine version, canonical hashes and a result hash. Replay recomputes the
result and fails on drift. It does not prove that the model is valid or that the decision is
correct.

## The reproducibility contract

The V12 run record stores:

- model and scenario SHA-256;
- engine name and version;
- seed base and replication count;
- an input hash over the model, scenario and engine version;
- Python and platform strings;
- the invocation;
- metrics, convergence, uncertainty and sensitivity;
- a result hash over the substantive fields.

The model and scenario files are the canonical inputs. The run record is derived. A change
to either input invalidates the run until it is regenerated.

## The replay command

From the repository root:

~~~text
python3 scripts/v12_engine.py replay \
  --run edition/v12/runs/checkout-b-queue.json \
  --model edition/v12/models/checkout-des.json \
  --scenario edition/v12/scenarios/checkout-b-queue.json
~~~

The command checks the stored model and scenario hashes, reruns the scenario and compares the
recomputed result hash. It fails if the model, scenario or output has drifted.

## What replay proves

Replay proves that the stored inputs, engine version and seed produce the stored metrics on
the same platform family. It does not prove:

- that the model is valid;
- that the inputs are measured;
- that the confidence interval covers a production value;
- that the decision is correct;
- that another platform will produce bit-identical floats.

The platform and Python strings make a cross-environment difference visible. They are not a
promise of bit-identical behavior.

## Ten rules mapping

The PLOS ten rules are guidance, not a certificate. V12 implements a bounded subset:

- track input data: model and scenario files are versioned and hashed;
- version scripts: the engine is a single versioned module;
- record parameters: the model and scenario contracts carry them;
- archive the environment: Python and platform are stored, but a full environment lock is
  not included;
- record seed and replication count: stored in the run;
- avoid manual steps: the engine runs from a command;
- record provenance: the run record links inputs to outputs;
- provide a result hash: stored and checked by replay.

V12 does not include a container image, a dependency lock or a full artifact archive. The
engine is dependency-free, which reduces the environment surface but does not eliminate the
platform difference.

## A replay flow

~~~mermaid
flowchart LR
    R["Stored run"] --> H["Check model hash"]
    R --> S["Check scenario hash"]
    H --> X["Rerun scenario"]
    S --> X
    X --> C["Compare result hash"]
    C --> P["Pass or fail"]
~~~

Text alternative: the replay loads a stored run, checks the model and scenario hashes, reruns
the scenario, recomputes the result hash and reports pass or fail.

## Failure modes

- **Hash drift.** A model or scenario is edited without regenerating its run.
- **Unrecorded seed.** The result cannot be reproduced.
- **Mutable dependency.** A library update changes the output and is not recorded.
- **Timestamp-only provenance.** A file says when it was created but not what it used.
- **Replay theater.** The command reruns the model but compares only the metric names, not
  the values or limitations.
- **Cross-platform overclaim.** A replay on one platform is presented as a guarantee for
  every platform.

## Evidence ledger

- [PLOS Ten Simple
  Rules](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
  supports tracked inputs, versioned scripts, recorded parameters and archived environments.
  It does not guarantee reproducibility on every platform.
- [PROV-O](https://www.w3.org/TR/prov-o/)
  supports entity, activity and derivation vocabulary.
  It does not establish V12 conformance.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports documentation as part of model verification and validation.
  It does not validate a replay result.

## Navigation

- Parent: [V12/C07 - Validation and limits](../README.md)
- Previous: [V12 validation gates](validation-gates.md)
- Parent volume: [V12 - Architecture modeling and decision validation](../README.md)
- Replay: scripts/v12_engine.py
