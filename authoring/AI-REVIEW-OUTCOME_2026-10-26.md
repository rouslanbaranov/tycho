# External AI review outcome — #535

Status: three review rounds performed. Round 3 returned **pass** for the bounded remediation
scope. The independent AI review gate for #535 is satisfied; earlier reject verdicts remain
historical for their snapshots.

## Review identity

- Reviewer: Codex desktop app / OpenAI.
- Model: GPT-6 family; exact deployed version not exposed.
- Session: `01a17a03-0b7c-7513-87fe-1f3994862b1d`.
- Original review date: 2026-10-26; exact time not recorded.
- Correction timestamp: 2026-10-26T22:28:08+01:00.
- Reviewed handoff: `authoring/AI-REVIEW-HANDOFF_2026-10-26.md` at
  `ec9289ae7dd9a1f179133c46ca9991a59e86055a`.
- Reviewed handoff SHA-256: `13fc97f5ae933787c434fbbaabebe53749adbfa47ffdc0da8c716bba73a156d0`.
- Report: [2026-10-26-full-unit-reading-codex.md](ai-reviews/2026-10-26-full-unit-reading-codex.md).
- Report SHA-256: `4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90`.

## Verdict

**reject**, with three blocking and five non-blocking findings. This is a partial,
targeted review: 22 units and all 23 claims were sampled; the full 155 units were not
re-read and the unavailable EIP/DDIA books were not obtained.

## Blocking findings

### R-01 — FS-21 overlooks Workbook support

The reviewer finds that the complete Workbook contains artificial user activity, browser
probes, probe placement and geographically separate confirmation. The current
`FS-21` disposition is `unconfirmed` with an accepted final status. Reopen and assess at
least `partially-supported`.

### R-02 — FS-10 contradiction is not demonstrated

The reviewer accepts that Chapter 3 discusses channel buffering, conditional reordering
and non-transactional message loss, but argues these do not establish the opposite of the
universal "each stage adds buffering, ordering and failure behaviour" claim. The
`contradicted` disposition needs narrowing or reclassification.

### R-03 — Grouped EIP closure obscures supported clauses

The reviewer finds clause-level support on the public pages for FS-06, FS-11, FS-12,
FS-14, FS-15 and FS-16. The grouped `source-unavailable` closure must separate supported
clauses from the unconfirmed remainder; it must not promote the original conjunctions.

## Non-blocking findings

- R-04: 127 section lists differ between the full-reading plan and source plan.
- R-05: UNSOLVED/ACCEPTED/ALTERNATIVES prose has incompatible EIP acceptance statements.
- R-06: FS-01/02/03/19 registry scope names linked material not exhaustively checked.
- R-07: absence of the literal words "encode" and "path" does not weaken FS-18's
  supported mechanism.
- R-08: Workbook coverage metadata says chapters 1-20; the contents list 21 chapters.

## Current disposition

At the time the review was recorded, no disposition was changed. Remediation was applied
afterward; see the section below. A focused re-review is required before treating the
reject verdict as resolved.


## Remediation applied

- **R-01 applied:** FS-21 reclassified to `partially-supported`. Supported case-study
  clauses are recorded; the exact definition and design rule remain unconfirmed.
- **R-02 applied:** FS-10 reclassified to `partially-supported`. The chapter supports
  buffering, reordering risk and non-transactional loss, not every-stage wording.
- **R-03 applied:** eleven EIP claims split into `supported_clauses` and
  `unconfirmed_clauses`; original conjunctions are not fully supported.
- **R-05 applied:** ACCEPTED, RESOLUTIONS and ALTERNATIVES now agree on EIP clause-level
  support and blocked units.
- **R-08 applied:** Workbook coverage corrected from chapters 1-20 to 1-21.
- **R-04 applied:** 130 full-reading-plan section lists aligned to `source-plan.v1.json`;
  `planned_sections` preserves the original reading scope.
- **R-06 applied:** FS-01, FS-02, FS-03 and FS-19 `full_source` narrowed to the complete
  pattern page; linked material is explicitly `not-read`.
- **R-07 applied:** FS-18 records the supported per-message mechanism and separates the
  unconfirmed `variants`/encoding detail; literal-word absence is not negative evidence.

The review verdict remains `reject` for the reviewed snapshot; the post-remediation state
needs a focused external re-review.

Post-remediation claim counts: 15 partially-supported, 5 unconfirmed, 2 contradicted,
1 resolved, total 23.


## Second focused re-review — 2026-10-26

Report: `authoring/ai-reviews/2026-10-26-remediation-rereview-codex.md`.
SHA-256: `430d30bbb689e5ad15127f7790eb2a0e0cc4b39fd663602ccde854cc7bfbb2f7`.

Verdict: **reject**.

- R-01, R-02, R-06, R-07 and R-08 were resolved in the reviewed scope.
- R-04 regressed: sections were bound by `pattern_id` only, producing ten sibling-source
  misbindings. Corrected by `(pattern_id, source_id, unit)`; 155 entries matched and zero
  differences remain.
- R-03a: the Aggregator ledger limitation still denied incomplete-set handling. Corrected.
- R-05a: the RESOLUTIONS range included FS-10. FS-10 is now listed separately.

No claim disposition changed in this round. The third focused re-review returned pass; see below.


## Third focused re-review — 2026-10-26

Report: `authoring/ai-reviews/2026-10-26-round3-rereview-codex.md`.
SHA-256: `b4ecbb26a1eaf395df439d82a98a21c819ea3d4c428818a6338076955c34dbe1`.

Verdict: **pass**. No blocking or non-blocking finding remains in the round-3 scope.
R-04, R-03a and R-05a are resolved; R-01, R-02, R-06, R-07 and R-08 show no regression.

Verified counts: 155 units (129 full, 14 exact, 1 partial, 11 blocked); 23 claims
(15 partially-supported, 5 unconfirmed, 2 contradicted, 1 resolved). All eight validators
and `check_boundary` exited 0 on an isolated copy.

This pass covers the remediation delta and the #535 evidence package, not a fresh
full-atlas review, EIP Chapter 4+, DDIA, sufficient coverage or CI.
