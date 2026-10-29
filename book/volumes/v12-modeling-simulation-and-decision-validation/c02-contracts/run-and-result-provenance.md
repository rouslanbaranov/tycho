---
metadata_version: 1
id: "tycho.page.201248045fa3cd67e617ce04a1c56feb"
kind: "page"
parent_id: "tycho.chapter.3a47e8385cccb8a2ce764bfa765cc740"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c02-contracts/run-and-result-provenance.md"
title: "Run and result provenance contract"
topic_ids:
  - "provenance"
  - "reproducibility"
perspectives:
  - "architecture"
  - "operations"
summary: "A run record binds model, scenario, engine, seeds, metrics and limits by hash."
route_hints:
  questions:
    - "Which fields make a run replayable?"
    - "What does a matching replay prove?"
  prerequisites: []
  related_ids:
    - "tycho.page.dedc5f2d31912a9ba5f562a86009fda0"
    - "tycho.page.c7a43944f1d41e810eec0d17ec33b85a"
    - "tycho.page.6c54ed1288a4f0806889865916dc8ccf"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "provenance"
    - "hash"
    - "replay"
    - "seed"
    - "convergence"
evidence_scope:
  source_ids:
    - "src.w3c-prov-o"
    - "src.plos-repro"
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

# Run and result provenance contract

**Question.** What must a run record preserve so that another reader can replay it and see
what the run did not establish?

**Short answer.** A run record binds the model and scenario by SHA-256, records the engine
version, seed base, replication count, input hash, Python and platform, invocation, metrics,
convergence, uncertainty, sensitivity and limitations. It also stores a result hash over the
record's substantive fields.

## Provenance is not a log line

A timestamp and a filename do not explain a result. Provenance answers:

- which model and scenario produced the result;
- which engine version executed it;
- which seed and how many replications;
- which inputs were combined into the run;
- which output metrics and convergence diagnostics were produced;
- which limitations apply.

PROV-O describes entities, activities and agents, with relations such as generation, use and
derivation. V12 borrows that shape without claiming ontology conformance. The model and
scenario are entities; the engine run is an activity; the run record is a generated entity
that used the inputs. A replay is a new activity that should generate the same result hash.

## Required fields

The run contract contains:

- id, version, model_id and scenario_id;
- engine: name, version and deterministic flag;
- provenance: model hash, scenario hash, seed base, replications, input hash, Python,
  platform and invocation;
- metrics: value, unit, replication count, standard error and confidence interval;
- convergence: status, metric, relative error, threshold and replications;
- uncertainty: method, draws, correlated-input flag and notes;
- sensitivity: parameter, first-order and total-order indices, method and replications;
- limitations and result_sha256.

The result hash is computed over the record without the hash field. Replay recomputes it and
fails if the model, scenario or engine output has drifted.

## What replay proves

Replay proves that the stored inputs, engine version and seed produce the stored metrics on
the same platform family. It does not prove that the model is valid, that the inputs are
measured or that the decision is correct. A replay that matches is a reproducibility check,
not a truth check.

Platform strings can differ across operating systems and Python builds. V12 stores the
platform string and the Python version so a mismatch is visible. The engine's metrics are
deterministic for the same inputs and seeds; the environment string is evidence, not a
guarantee of bit-identical behavior on every platform.

## Example: candidate B run

The candidate B run has 30 replications, a success rate of 0.9996 with a 95% CI of
0.9995-0.9996, a p95 latency of 1.206 seconds, and a relative error of 0.00004. The
convergence status is converged against a 0.02 threshold. The uncertainty method is
replication; there are no correlated inputs. The limitations say the workload is synthetic
and the confidence intervals use a normal approximation.

The run's model hash is the SHA-256 of checkout-des.json; the scenario hash is the SHA-256
of checkout-b-queue.json. If either file changes, replay fails before producing a new
number.

## A provenance chain

~~~mermaid
flowchart LR
    M["Model entity"] --> A["Engine run activity"]
    S["Scenario entity"] --> A
    A --> R["Run record entity"]
    R --> D["Decision record"]
    R --> P["Replay activity"]
    P --> R2["Recomputed result hash"]
~~~

Text alternative: model and scenario entities feed an engine run. The run generates a record
that feeds a decision and a replay. The replay recomputes the result hash and compares it
with the stored record.

## Failure modes

- **Hash drift.** A model or scenario is edited without regenerating its run. Replay fails;
  the old result is stale.
- **Unrecorded seed.** The result cannot be reproduced because the seed was chosen in a
  notebook and not stored.
- **Timestamp-only provenance.** A file says when it was created but not which inputs it
  used.
- **Environment omission.** A result depends on a library version that is not recorded.
- **Hash over the wrong fields.** The result hash covers only the metrics, so a changed
  limitation or convergence status is invisible.

V12 hashes the substantive record, not the file bytes, so formatting changes do not
invalidate a result. A changed metric, limitation or convergence status does.

## Evidence ledger

- [PROV-O](https://www.w3.org/TR/prov-o/)
  supports entity, activity, agent, generation and use vocabulary.
  It does not establish V12 conformance or reproducibility.
- [PLOS Ten Simple
  Rules](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
  supports tracked inputs, versioned scripts, recorded parameters and archived environments.
  It does not guarantee that a replay will match on every platform.

## Navigation

- Parent: [V12/C02 - Contracts](../README.md)
- Previous: [Scenario specification contract](scenario-specification.md)
- Next: [Decision record contract](decision-record.md)
- Schema: [run-result.v1.schema.json](../../../../schemas/v12/run-result.v1.schema.json)
