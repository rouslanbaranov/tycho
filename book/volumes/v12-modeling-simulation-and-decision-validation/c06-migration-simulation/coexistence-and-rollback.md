---
metadata_version: 1
id: "tycho.page.ea00bb677b242deed4a1ff3fa91f948a"
kind: "page"
parent_id: "tycho.chapter.26ddd5ca6c1bea39738561c3bdb1cf23"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c06-migration-simulation/coexistence-and-rollback.md"
title: "Coexistence and rollback"
topic_ids:
  - "modernization-simulation"
  - "model-validation"
perspectives:
  - "migration"
  - "architecture"
summary: "Traffic shares, dual-write backlog, reconciliation and rollback drain in a staged path."
route_hints:
  questions:
    - "Which states must a modernization model expose?"
    - "What makes a rollback finding actionable?"
  prerequisites: []
  related_ids:
    - "tycho.page.7732cad079d3148dd26b24cc1fdef318"
    - "tycho.page.ea9adae8cf8a3196a3515d383b075f53"
    - "tycho.page.d8d9d15b402d8f65928ca0e3f3e5b939"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "coexistence"
    - "dual write"
    - "reconciliation"
    - "rollback"
    - "divergence"
evidence_scope:
  source_ids:
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

# Coexistence and rollback

**Question.** Which coexistence, reconciliation and rollback states must a modernization model
expose before a cutover can be called supported?

**Short answer.** A staged model must show the traffic share on each path, the dual-write
backlog, the reconciliation capacity, the accumulated divergence and the rollback drain. A
cutover is supported only when those states stay inside declared limits and the rollback
completes within the observation window.

## Coexistence is a state, not a date

A modernization path usually has several states:

- legacy only;
- dual write: both paths receive writes, with a reconciliation process;
- shadow: the target receives traffic but does not own the authoritative response;
- cutover: the target owns the authoritative response;
- rollback: traffic returns to the legacy path while the target drains.

Each state has different failure modes. A dual-write state can diverge silently. A shadow
state can look healthy while the target's write path is untested. A cutover state can expose
a reconciliation backlog that was hidden by legacy ownership.

The V12 modernization model represents the states as a stage schedule and a set of stocks:

- dual_write_backlog: records awaiting reconciliation;
- divergence: accumulated observed difference between paths;
- legacy_share and target_share: traffic allocation;
- rollback timer: time since the rollback trigger.

The model is a fluid approximation. It does not represent individual records, schema
compatibility or deployment orchestration. Those omissions are part of the validity limit.

## The accounting

At each step, the offered traffic is split between legacy and target. The model serves up to
each path's capacity:

    target_served = min(arrival * target_share * dt, target_capacity * dt)
    legacy_served = min(arrival * (1 - target_share) * dt, legacy_capacity * dt)
    rejected = offered - target_served - legacy_served

The dual-write backlog grows with target throughput times the declared lag and drains at the
reconciliation capacity:

    backlog += target_served * dual_write_lag
    backlog -= min(backlog, reconciliation_capacity * dt)

Divergence accumulates when the backlog exceeds the drain capacity. It is a synthetic proxy,
not a measured data-quality metric.

## Rollback

A rollback trigger sets the target share to zero. The legacy path must absorb the traffic,
and the target must drain its backlog and divergence. The model records:

- whether the rollback completed within the horizon;
- the time from trigger to drain, or a censored value at the horizon;
- the maximum divergence observed before the trigger.

A rollback that does not complete is not a failed model. It is a finding: the declared
reconciliation capacity is insufficient for the declared lag and observation window.

## The staged result

The staged scenario uses a three-stage shift (0.2, 0.5, 1.0) over 2,400 seconds, a 1.5-second
dual-write lag, a reconciliation capacity of 4 records per second, and a rollback at 1,200
seconds. The input ranges are 0.5-2.5 seconds for lag and 2-8 records per second for
reconciliation, with a -0.4 correlation.

The run reports:

- success rate 1.0 (the modeled traffic is served);
- maximum divergence 8,925.5 records (95% CI 5,561.6-12,289.3);
- rollback completed 0.1: it finishes in only 10% of replications;
- rollback seconds 0 for the 10% that completed; non-completions are censored at 2,400.

The no-cutover baseline reports zero divergence and no rollback requirement. The staged
candidate does not produce a decision-supported cutover because rollback completes in
only 10% of replications and the divergence is far outside any plausible business threshold.
The decision record returns insufficient evidence.

## A state diagram

~~~mermaid
stateDiagram-v2
    [*] --> Legacy
    Legacy --> DualWrite: stage 1
    DualWrite --> Shadow: stage 2
    Shadow --> Cutover: stage 3
    Cutover --> Rollback: divergence trigger
    Rollback --> Legacy: drain complete
    Cutover --> [*]: accepted
~~~

Text alternative: the path moves from legacy to dual write, shadow and cutover. A divergence
trigger moves cutover to rollback; rollback returns to legacy only after the drain completes.

## Failure modes

- **Dual-write divergence.** The two paths accept writes that cannot be reconciled. The
  backlog grows faster than the reconciliation capacity.
- **Reconciliation starvation.** The reconciliation process competes with the target for the
  same resources and slows down under load.
- **Rollback that cannot drain.** The target keeps receiving work after the trigger, or the
  backlog is too large to drain in the window.
- **False cutover signal.** A 100% traffic share is treated as success while divergence is
  still growing.
- **Schema incompatibility.** A record cannot be represented on one path. The fluid model
  does not see it.
- **Business continuity gap.** The rollback is technically possible but the operating team
  cannot execute it.

## What would support a cutover

A cutover record could be decision-supported only with:

- a measured dual-write lag with a bounded upper confidence limit;
- a measured reconciliation capacity in the target environment;
- a rehearsed rollback that completes inside the observation window;
- a measured divergence below the business threshold across a sustained period;
- a confirmed continuity and reconciliation runbook.

Those are measurements and operational evidence, not model parameters. The model can show
what to measure and how the decision depends on it; it cannot create the measurement.

## Evidence ledger

- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports data validity, conceptual validity and operational validity as separate concerns.
  It does not validate the modernization model.
- Existing V10 transition and cutover owner pages (read-only links from the decision record)
  support the pattern vocabulary.
  They do not establish a migration result.

## Navigation

- Parent: [V12/C06 - Migration simulation](../README.md)
- Next: [Modernization-path experiment](modernization-path-experiment.md)
- Decision record: edition/v12/decisions/modernization-cutover.json
