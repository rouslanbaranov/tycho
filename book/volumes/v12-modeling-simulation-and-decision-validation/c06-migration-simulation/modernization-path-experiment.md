---
metadata_version: 1
id: "tycho.page.7732cad079d3148dd26b24cc1fdef318"
kind: "page"
parent_id: "tycho.chapter.26ddd5ca6c1bea39738561c3bdb1cf23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c06-migration-simulation/modernization-path-experiment.md"
title: "Modernization-path experiment"
topic_ids:
  - "modernization-simulation"
  - "monte-carlo"
perspectives:
  - "migration"
  - "evaluation"
summary: "A staged cutover compared with a no-cutover baseline; insufficient evidence for cutover."
route_hints:
  questions:
    - "How does the staged path compare with no cutover?"
    - "What measurement would change the outcome?"
  prerequisites: []
  related_ids:
    - "tycho.page.ea00bb677b242deed4a1ff3fa91f948a"
    - "tycho.page.3cfd08ee56330be9b7a2d37975c3fe26"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "modernization"
    - "experiment"
    - "divergence"
    - "rollback"
evidence_scope:
  source_ids:
    - "src.sargent-vv"
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

# Modernization-path experiment

**Question.** How does the staged modernization scenario compare with a no-cutover baseline,
and what does the comparison establish?

**Short answer.** The experiment fixes the workload and seed scheme, varies the stage
schedule and rollback trigger, and compares the staged path with a no-cutover baseline. The
staged path serves the traffic but produces a large synthetic divergence and does not
complete rollback within the horizon. The comparison establishes a measurement agenda, not a
cutover decision.

## Experiment design

The staged scenario:

- offers 10 requests per second for 2,400 seconds;
- shifts target traffic to 0.2 at t=0, 0.5 at t=300 and 1.0 at t=600;
- uses a 1.5-second dual-write lag and a 4-record-per-second reconciliation capacity;
- triggers a rollback at t=1,200;
- draws lag from 0.5-2.5 seconds and reconciliation capacity from 2-8 records per second,
  with a -0.4 correlation;
- uses 20 replications and the seed base 20261029.

The no-cutover baseline uses the same workload and model but keeps target share at zero and
never triggers a rollback. It uses 10 replications.

The comparison is not an A/B test of two production systems. It is a synthetic check of how
the declared inputs move the modeled divergence and rollback time.

## Results

The staged run reports:

- success rate 1.0;
- throughput 10 requests per second;
- mean dual-write backlog 4,242.0 records;
- maximum divergence 8,925.5 records (95% CI 5,561.6-12,289.3);
- rollback completed 0.1;
- rollback seconds mean 2,160, with non-completions censored at 2,400.

The baseline reports:

- success rate 1.0;
- throughput 10 requests per second;
- zero divergence and zero backlog;
- no rollback requirement.

The baseline is not a recommendation to remain on the legacy path forever. It is a reference
for the modeled cost of not shifting traffic. The staged path adds divergence risk and a
rollback requirement; it does not add modeled throughput because both paths have enough
capacity for the synthetic load.

## What the experiment establishes

It establishes that, under the declared inputs:

- the target path can serve the synthetic traffic;
- the dual-write backlog grows when lag times throughput exceeds reconciliation capacity;
- the rollback completes in only 10% of replications inside the 2,400-second window;
- the divergence range is wide enough to cross plausible business thresholds.

It does not establish that the target path is correct, that records reconcile, that the
rollback is operationally executable or that the real divergence is inside the modeled range.

## Why the decision is insufficient evidence

The decision record compares the staged path with the baseline. The staged path has a
non-zero divergence and an incomplete rollback. The baseline has neither. A decision to cut
over would need to show that the divergence is acceptable and the rollback is achievable.
The model cannot show either because the inputs are assumed over wide ranges.

The correct next step is measurement:

1. Instrument dual-write lag in a bounded environment.
2. Measure reconciliation throughput under target load.
3. Rehearse a rollback and record its duration.
4. Measure divergence over a sustained shadow period.
5. Re-run the scenario with measured inputs.

## A comparison diagram

~~~mermaid
flowchart LR
    W["Same synthetic workload"] --> S["Staged cutover"]
    W --> B["No-cutover baseline"]
    S --> D["Divergence and rollback"]
    B --> Z["No divergence"]
    D --> I["Insufficient evidence"]
    Z --> I
    I --> M["Measure lag, capacity, rollback"]
~~~

Text alternative: the same workload feeds a staged cutover and a no-cutover baseline. The
staged path produces divergence and an incomplete rollback; the baseline does not. Both point
to an insufficient-evidence outcome and a measurement agenda.

## Failure modes

- **Baseline as winner.** The no-cutover path is treated as the recommended architecture
  because it has zero modeled divergence. The baseline does not achieve modernization.
- **Single-input optimism.** The staged path is run with the best-case lag and capacity only.
  The decision ignores the upper tail.
- **Correlation omission.** Lag and capacity are drawn independently, producing an
  unrealistically narrow divergence range.
- **Horizon censorship.** A rollback that exceeds the horizon is reported as zero seconds
  rather than censored.
- **Throughput equivalence.** Both paths serve the synthetic load, so the experiment is
  treated as evidence that the target path adds no value. The model does not include the
  business reason for modernization.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports data validity and operational validity as separate concerns.
  It does not validate the staged scenario.
- JCGM 100:2008 (source src.jcgm-100; see the reading ledger)
  supports reporting a value with uncertainty and coverage.
  It does not create a measured lag or capacity.

## Navigation

- Parent: [V12/C06 - Migration simulation](../README.md)
- Previous: [Coexistence and rollback](coexistence-and-rollback.md)
- Next: [V12/C07 - Validation and limits](../c07-validation-and-limits/README.md)
- Run: edition/v12/runs/modernization-staged.json
