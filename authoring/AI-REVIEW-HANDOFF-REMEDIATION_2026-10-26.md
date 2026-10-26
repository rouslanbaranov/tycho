# Focused AI re-review hand-off — #535 remediation

Status: prepared for a focused independent AI re-review. This is not a review,
acceptance, CI result or sufficient-coverage claim.

- Issue: #535
- Branch: `feature/TYCHO-535-read-the-155-pattern-source-plan-units-in-full`
- Reviewed snapshot: `0531e9ce`
- Remediation commits: `5f05ad7d`, `bbe1c0c6`, `e11839d2`
- Original review: `ai-reviews/2026-10-26-full-unit-reading-codex.md`
- Original report SHA-256: `4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90`
- Original verdict: **reject**
- Outcome: [AI-REVIEW-OUTCOME_2026-10-26.md](AI-REVIEW-OUTCOME_2026-10-26.md)

## 1. What changed

- **R-01:** FS-21 is `partially-supported`; case-study clauses are supported and the
  definition/design rule remains unconfirmed.
- **R-02:** FS-10 is `partially-supported`; universal every-stage wording is unsupported,
  while buffering, reordering risk and non-transactional loss are recorded.
- **R-03:** eleven EIP claims are `partially-supported`; each has `supported_clauses` and
  `unconfirmed_clauses`; original conjunctions are not fully supported.
- **R-04:** 130 reading-plan section lists aligned to `source-plan.v1.json`;
  `planned_sections` preserves the original scope; zero diffs remain.
- **R-05:** ACCEPTED, RESOLUTIONS and ALTERNATIVES agree on EIP clause-level support and
  blocked units.
- **R-06:** FS-01/02/03/19 `full_source` narrowed to the complete pattern page; linked
  material is `not-read`.
- **R-07:** FS-18 records the per-message mechanism; `variants`/encoding remain
  unconfirmed and literal-word absence is not negative evidence.
- **R-08:** Workbook coverage corrected from chapters 1-20 to 1-21.

Current claims: 15 partially-supported, 5 unconfirmed, 2 contradicted, 1 resolved.
Current units: 129 full, 14 exact reuse, 1 partial, 11 blocked.

## 2. Scope of this re-review

Review the remediation delta only:

- R-01 through R-08;
- the changed claim records and result entries;
- the reconciled section lists;
- the corrected acceptance prose.

Do not re-read all 155 units. Sample at least the changed claims and 5 changed units.
The original report remains a `reject` verdict for its snapshot; this review decides whether
the remediation resolves its findings. It is not a fresh full-atlas review.

## 3. Required checks

1. Derive the counts from artifacts; do not copy them from this hand-off.
2. FS-21: confirm the Workbook clauses and the remaining unconfirmed definition/design rule.
3. FS-10: confirm the chapter supports the clauses but not the universal wording.
4. EIP: confirm every one of the eleven claims has both supported and unconfirmed clauses.
5. R-04: confirm zero section diffs between the two plans.
6. R-06: confirm the four narrowed `full_source` values and `linked_sources: not-read`.
7. R-07: confirm FS-18 no longer uses literal-word absence as negative evidence.
8. R-08: confirm chapters 1-21.
9. Run the validators and record exact exit statuses.

## 4. Exact prompt for the external reviewer

```text
You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Perform a focused read-only re-review of Tycho #535
remediation. Do not edit, commit, open a PR or change configuration.

Repository: /Users/rbaranov/Projects/tycho
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Reviewed snapshot: 0531e9ce.
Remediation HEAD: current branch HEAD (record it).
Original report: authoring/ai-reviews/2026-10-26-full-unit-reading-codex.md
Original report SHA-256: 4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90
Hand-off: authoring/AI-REVIEW-HANDOFF-REMEDIATION_2026-10-26.md
Claims: research/full-source-confirmation/claims.v1.json
Results: research/full-source-confirmation/results.v1.json
Reading plan: edition/patterns/full-unit-reading-plan.v1.json
Source plan: edition/patterns/source-plan.v1.json

Verify the remediation of R-01 through R-08, not the whole 155-unit reading.
Derive counts from artifacts. Use public sources only. Do not trust this prompt.

Required checks:
1. Counts: 15 partially-supported, 5 unconfirmed, 2 contradicted, 1 resolved, total 23.
2. FS-21: supported Workbook clauses and remaining unconfirmed definition/design rule.
3. FS-10: clause-level support exists; universal every-stage wording is unconfirmed.
4. Eleven EIP claims: each has supported_clauses and unconfirmed_clauses.
5. R-04: zero section diffs between the reading plan and source plan.
6. R-06: four narrowed full_source values and linked_sources: not-read.
7. R-07: FS-18 mechanism is supported; variants/encoding remain unconfirmed.
8. R-08: Workbook chapters 1-21.
9. Run the validators in the hand-off and record exact exit statuses.

Return one Markdown report with: harness/vendor, model/version, session id, timestamp,
repository path, review HEAD, reviewed snapshot, exact scope, verdict
(pass / pass-with-findings / reject), findings by severity with paths and evidence,
limits, and `ai_review: performed` only if the checks ran. State `sufficient: 0`.
Do not claim owner acceptance, CI or merge permission.
```

The author saves the returned report verbatim under `authoring/ai-reviews/` and records
its SHA-256 in the index. A review without a saved report is not complete.
