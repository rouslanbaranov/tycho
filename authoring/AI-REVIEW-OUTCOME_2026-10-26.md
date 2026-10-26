# External AI review outcome — #535

Status: review performed; verdict **reject**. Remediation was applied after the review;
a focused re-review is still required. The owner decides whether to accept the remediation.

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

R-04, R-06 and R-07 remain non-blocking open items. The review verdict remains `reject`
for the reviewed snapshot; the post-remediation state needs a focused external re-review.

Post-remediation claim counts: 15 partially-supported, 5 unconfirmed, 2 contradicted,
1 resolved, total 23.
