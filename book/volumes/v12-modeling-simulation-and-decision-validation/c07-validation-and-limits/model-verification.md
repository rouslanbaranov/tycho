---
metadata_version: 1
id: "tycho.page.621e495fcadc4849d2f21d55be4c52e4"
kind: "page"
parent_id: "tycho.chapter.77831d9a57067de6faa1da630a83f49b"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c07-validation-and-limits/model-verification.md"
title: "Model verification"
topic_ids:
  - "model-validation"
  - "simulation"
perspectives:
  - "evaluation"
  - "implementation"
summary: "Conservation, boundary, event-order and replay checks, with an explicit list of gaps."
route_hints:
  questions:
    - "Which checks show the engine implements its models?"
    - "What remains unverified?"
  prerequisites: []
  related_ids:
    - "tycho.page.b0c704c825b2faf15a1d118dc9a6b1cc"
    - "tycho.page.6fd0d561e3e2900dc8b59a3011071cd2"
    - "tycho.page.4e13fd6ac1103a15c800e939b13bd2f9"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "verification"
    - "conservation"
    - "boundary"
    - "event order"
    - "replay"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
    - "src.simpy"
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

# Model verification

**Question.** Which checks show that the V12 engine implements its models as specified, and
which checks are still missing?

**Short answer.** Verification covers units, conservation, non-negativity, boundary cases,
event ordering, timeout interaction, retry conservation and deterministic replay. It does not
cover operational validity, calibration or a production trace. The test matrix records what
passed and what remains unverified.

## Verification versus validation

Sargent defines model verification as ensuring that the computer program of the model is
correct. Validation asks whether the model is adequate for its intended purpose. A model can
be verified and still be invalid for a decision because its structure or data are wrong.

V12 uses the same distinction. The verification section names the tests and the observed
results. The calibration and validity sections name the missing measurements. A verified
engine is not a validated system.

## The test matrix

| Check | Test | Result |
|---|---|---|
| Stock-flow conservation | test_conservation_below_capacity | pass |
| Stock-flow non-negativity | test_saturation_rejects_and_conserves | pass |
| Zero-arrival boundary | test_zero_boundary | pass |
| Saturation and rejection | test_saturation_rejects_and_conserves | pass |
| Event order at equal time | test_ties_use_priority_then_insertion | pass |
| Timeout before completion | test_timeout_before_completion | pass |
| Completion before timeout | test_completion_before_timeout | pass |
| Retry conservation | test_conservation_under_retries | pass |
| Zero queue capacity | test_zero_capacity_boundary | pass |
| Deterministic replay | test_deterministic_replay | pass |
| Modernization zero lag | test_zero_lag_has_no_divergence | pass |
| Modernization rollback | test_rollback_completes_with_high_reconciliation | pass |
| Modernization capacity | test_modernization_capacity | pass |
| Sensitivity coherence | test_indices_are_coherent | pass |

The table names the intended tests; the actual test file is tests/test_tycho_v12_engine.py.
A test that is renamed must update the model contract's verification case path.

## Conservation

The stock-flow model checks:

    offered = completed + rejected + backlog

The discrete-event model checks:

    offered = completed + rejected + failed + in_system

The check runs after every replication. A conservation failure aborts the run; the engine does
not write a partial record. The test exercises a below-capacity case, a saturation case and a
retry-heavy case.

Conservation is necessary but not sufficient. A model can conserve requests while assigning
them to the wrong outcome. The timeout and retry tests check the outcome path separately.

## Boundary cases

The boundary tests are:

- zero arrivals: no requests, no completions, no fabricated success;
- zero servers: no service; requests are rejected or remain in backlog according to the
  model;
- zero queue capacity: a request that cannot start service immediately is rejected;
- full bulkhead: explicit rejection;
- one attempt: no retry;
- maximum attempts: terminal failure after the last timeout.

A boundary case often exposes a division by zero, a negative stock or an unbounded loop. The
tests assert the outcome, not merely that the run terminates.

## Event ordering

The event-order test schedules three events at the same time with different priorities and
checks the processing order. The timeout tests check that:

- a timeout before completion cancels the attempt and may retry;
- a completion before timeout succeeds and the later timeout is ignored;
- a stale completion after a timeout does not free a second server.

The tests do not prove that the chosen priority order matches a production scheduler. They
prove that the implemented order is deterministic and that the timeout state machine is
self-consistent.

## Replay

The replay test runs the same model, scenario and seed twice and compares the result hash. It
also checks the stored run against the current model and scenario hashes. A change in either
file fails replay before a new number is produced.

Replay is a verification check for the engine's determinism. It is not a validation check for
the model's assumptions.

## What is not verified

- The service-time distribution is not fitted to a real sample.
- The arrival process is not tested against a production trace.
- The queue discipline is FIFO only; priority and preemption are not implemented.
- The model does not represent dependency calls, network transport or storage.
- The sensitivity screen is not a full Sobol' estimator.
- The confidence-interval coverage is not tested over many synthetic samples.

These are recorded as limits, not as completed checks. A reader who needs one of them must
commission the corresponding evidence, not infer it from the passing matrix.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports computerized-model verification, degenerate tests, extreme-condition tests and
  traces.
  It does not validate the V12 engine.
- [SimPy 4.1 documentation](https://simpy.readthedocs.io/en/latest/)
  supports event, resource and timeout semantics.
  It does not establish the V12 implementation.

## Navigation

- Parent: [V12/C07 - Validation and limits](../README.md)
- Next: [Calibration and validity limits](calibration-and-validity-limits.md)
- Tests: tests/test_tycho_v12_engine.py
