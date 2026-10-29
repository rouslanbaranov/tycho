# 24x7 acceleration operating model — 2026-10-29

Status: active. Extends AGENTS rules 31-34.

## Topology

- 3 authoring lanes, each in its own git worktree and branch.
- 1 integrator in the main worktree; sole writer of shared metadata.
- 2 reviewers, read-only, packet groups, no tests.
- Batch size: 3-4 entries per lane wave.

## Lane rules

- Create from the frozen integration HEAD.
- Edit only the lane's owner/card pages and lane-local notes.
- Do not edit `owner-units`, `registry`, promotions, acceptance, manifests,
  directory migration, ids, semantic audit, qrels or generated artifacts.
- Do not run the full suite; lane-local validators only.
- Commit lane branch; do not merge or push main.

## Integrator rules

- Freeze a base HEAD before the wave.
- Merge/cherry-pick lanes sequentially into the integration worktree.
- Resolve shared metadata once; run refresh and full suite once.
- Reject overlapping files; a lane that touched another lane's page is redone.
- Commit the integrated wave and publish the new HEAD.

## Review wave

- Build 2 bounded packets from the integrated HEAD.
- Reviewers run in parallel, read-only, no tests.
- A pass with recorded minors permits promotion; majors go back to the owning lane.
- No rollback; fix forward (rule 33).

## Throughput assumption

- 3 lanes x 3-4 entries per wave.
- Integration + review + remediation per wave.
- Estimate 8-11 days wall clock for all remaining entries at 24x7.
