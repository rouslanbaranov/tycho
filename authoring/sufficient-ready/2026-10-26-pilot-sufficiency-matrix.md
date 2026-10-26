# Pilot sufficiency matrix

Date: 2026-10-26. Refs #532. This is not sufficient coverage and not human review.

## Criteria used

An entry is `sufficient-ready` for this pilot when:

1. a dedicated admitted source record exists;
2. all four owner-unit technical dimensions are `supported`;
3. the atlas card has its decision question, fit conditions, contraindications,
   competing alternative and failure/recovery;
4. an independent Reviewer pass covers the current card/owner/source binding;
5. remaining gaps are named as synthetic or operational limits.

`sufficient-ready` does not mean `sufficient`: decision coverage is still
`partial-bounded`, no independent human review of sufficiency exists, and no
per-entry promotion to `sufficient` has been recorded.

## Result

| Entry | Technical dimensions | Status | Remaining limit |
|---|---|---|---|
| Workload Identity / mTLS | failure/recovery partial | not ready | revocation and rotation-failure impact synthetic |
| Dark Launching / Shadow Traffic | invariant, failure, alternative partial | not ready | measurement, side-effect suppression and capacity bounds synthetic |
| RBAC/ABAC | all four supported | **sufficient-ready** | revocation, role explosion and attribute freshness synthetic |
| Federated Identity | all four supported | **sufficient-ready** | federation revocation and replay synthetic |
| Controlled Cutover | all four supported | **sufficient-ready** | general no-return, fallback and RTO synthetic; Spanner is bounded |
| Parallel Run | all four supported | **sufficient-ready** | mismatch threshold, sampling and cost bounds synthetic |

## Limits

- `sufficient-ready` is a pilot label, not a registry coverage promotion.
- Decision coverage remains `partial-bounded` for all six.
- No human review, CI, owner acceptance or sufficient coverage is claimed.
