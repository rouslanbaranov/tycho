# External AI review outcome — #535

Status: review performed; verdict **reject**. No disposition was changed by this record.
The owner decides whether to apply the findings.

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

No claim, unit, acceptance or sufficient status was changed in response to this report.
The next step is owner direction: apply the findings and request a focused re-review, or
challenge specific findings with evidence.
