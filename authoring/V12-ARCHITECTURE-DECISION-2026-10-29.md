# V12 architecture decision — 2026-10-29

Status: implemented 2026-10-29 under explicit owner activation of #587. Independent review,
owner acceptance and pattern promotion remain separate decisions. See the
[implementation record](V12-IMPLEMENTATION-2026-10-29.md).

## Decision

Architecture Modeling, Simulation & Decision Validation lives in a separate volume:

```text
book/volumes/v12-modeling-simulation-and-decision-validation/
```

**Iron rule:** V12 references existing patterns. Existing patterns do not reference V12.

## Protected baseline

Existing V11 cards, owner pages, frontmatter, page IDs, paths, source/evidence ledgers,
review packets, promotion records and the current 21 sufficient entries are protected.
V12 must not edit them to add fields, links or reverse references.

## Evidence layers

Pattern source evidence, model verification, calibration, simulation evidence and
decision evidence are separate. Simulation never promotes a pattern to sufficient.

## Discovery

V12 links one way to `tycho.pattern.*`. A derived reverse index
`pattern_id -> [model, scenario, run, decision]` supplies cross-volume discovery without
write-back. Search adds `artifact_type`, `volume`, `pattern_id` and `evidence_status`
facets; canonical pattern pages rank first for pattern queries.

## Issue map

- #587 — parent plan and iron rule;
- #588 — V12 foundations;
- #589 — V12 contracts;
- #590 — V12 reference engine;
- #591 — V12 experiments;
- #592 — V12 decision records and derived reverse index;
- #593 — optional external interoperability.

## Gate

Activation requires explicit owner instruction, a pinned baseline, a read-only impact
manifest and a bounded phase plan. No global schema/frontmatter migration is part of
this decision.
