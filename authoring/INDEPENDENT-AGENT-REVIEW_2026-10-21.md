# Independent agent review — 2026-10-21

Status: independent review agent (non-human), assigned by the owner in
[issue #288](https://github.com/rouslanbaranov/tycho/issues/288). This is not human
review, owner acceptance or claim-by-claim source verification.

- Reviewer: **Reviewer**
- Reviewed tree: PR #289, commit `a0b0b95`, base `300c63b`.
- Review mode: read-only; no repository file edited by the reviewer.
- Relationship to Tycho: did not author the change and did not retrieve external
  sources.

## Scope

The review covered the semantic-audit artifact, schema, validator, builder and tests;
the V11 atlas volume; delivery evidence and status documents; the Phase 4/5 pattern
artifacts; and the pages carrying findings.

The reviewer read all pages that were then classified `needs-remediation` and all
48 pages with a medium finding; under the corrected taxonomy 47 pages are
`needs-remediation`, and all are covered by that reading. It also sampled low findings,
did not read all 118 low findings line by line and did not reopen external sources.

## Commands run by the reviewer

All Python commands used `.venv/bin/python3` (Python 3.9.6, jsonschema 4.25.1).

- `.venv/bin/python3 scripts/validate_pattern_semantic_audit.py` — PASS, 419 pages,
  166 findings, 7 gates.
- The eight pattern validators, `phase4_audit.py --check`,
  `validate_delivery_evidence.py`, source and edition checks, directory migration,
  markdown line length, pattern census and boundary check — all PASS.
- `-m unittest discover -s tests -p 'test_tycho*.py' -v` — 333 tests in the first
  pass and 342 in the focused re-review, both OK; the final suite has 348 tests.
- Independent probes recomputed coverage, IDs, kinds, tiers, Phase 4 dispositions,
  SHA-256 values, anchors, disposition rules and summary counts; checked 380 local links
  across the V11 files and the audit report with 0 broken; normalized the 40 related
  labels; and checked the five V11 content-revision hashes.
- `premerge_check.py` was not run by the reviewer because the review packet did not
  include the exact issue title; its constituent validators and the full suite were
  run separately.

## Verdict

**ACCEPT-WITH-FINDINGS.**

The core audit invariants held: 419/419 records; zero ID/path/kind/tier/Phase 4
mismatches; zero SHA-256 mismatches; 166/166 anchors resolved; all disposition rules
satisfied; exact summary counts; all required gates present; and no claim of human
independent review, sufficient coverage or owner acceptance. The V11 corrections were
consistent with the tree, the 40 labels were genuine non-routes, the three reads were
intentionally unused and the three splits were properly deferred.

The reviewer recorded 17 findings (4 technical, 5 editorial, 8 audit-logic or
evidence-integrity). A focused re-review found 7 residual findings (2 medium, 5 low).
All 24 were addressed in the working tree before this record was added.

## Findings and disposition

### Technical

- **T1, medium, substring anchors.** The validator accepted a word contained in a
  heading rather than an exact heading or slug. Fixed: exact heading/slug matching and a
  substring-anchor regression test.
- **T2, low, missing branch tests.** Several validator branches had no adversarial test.
  Fixed: tests added for substring anchors, blocked without a gate, needs-remediation
  without a medium finding, duplicate IDs, tier mismatch, non-ancestor source commit and
  open-gate summary mismatch.
- **T3, low, queue heading mismatch.** The builder exposed only level-2/3 headings and
  truncated the list. Fixed: the builder now uses the validator's full heading
  extraction.
- **T4, low, source-commit provenance.** `source_commit` predates the artifact. Fixed:
  both evidence artifacts now state that it is the branch base and that page hashes bind
  the reviewed content.

### Editorial

- **E1, low, V11 status.** The landing still called the atlas Phase 5 and the audit
  open. Fixed: Phase 6/recorded-audit wording; the human review and owner gates remain
  open.
- **E2, low, C01 owner note.** The note overstated what the anchored section states.
  Fixed: the note now names only hidden shared state and orchestration/BFF alternatives.
- **E3, low, correction notes.** The audit notes did not identify the corrected defects.
  Fixed: the five corrected pages now carry precise correction notes.
- **E4, low, reproduction block.** The block used placeholders and the wrong interpreter.
  Fixed: exact branch and issue title, `.venv/bin/python3` and the dependency note.
- **E5, low, unnamed cards.** The report did not name the four corrected cards. Fixed:
  C01, C02, C03 and C08 are listed with their defect categories.

### Audit logic and evidence integrity

- **A1, medium, taxonomy.** The disposition rules did not determine the 100/40 split.
  Fixed: `sound-with-findings` is now low-only; `needs-remediation` requires a
  medium/high finding with a remediation on that finding. Eleven pages were
  reclassified; counts are now 278 sound, 93 sound-with-findings, 47 needs-remediation
  and 1 blocked.
- **A2, medium, no severity rubric.** Fixed: the artifact now defines low, medium and
  high. The "0 high" count is reproducible under that rubric.
- **A3, medium, stale delivery limit.** Fixed: the structural-disposition limit now says
  the semantic audit is self-checked and not independent human review.
- **A4, medium, stale non-route limit.** Fixed: the delivery evidence now says the 40
  labels are deliberate non-routes and no unresolved label remains.
- **A5, medium, over-characterized gRPC duplicate.** Fixed: the finding now names the
  repeated measurement terms and keeps the four sections distinct.
- **A6, low, workflow-failure ownership claim.** Fixed: the finding now covers only the
  duplicated launch/timer material and records that V04/C05 does not own poison-work.
- **A7, low, stale test and premerge evidence.** Fixed: the final 348 tests and the
  #288 branch are recorded.
- **A8, low, provenance fields.** Addressed with the same source-commit note as T4.

## Focused re-review

The re-review confirmed the core invariants, the 278/93/47/1 dispositions, all 419
current page hashes, the exact-anchor control, the 19 semantic tests then present, 342
full-suite tests and local premerge. It recorded seven residual findings:

- **RR1, medium.** The audit gates and summary lacked a human/agent qualifier while a
  named agent review existed. Fixed: the gates now say "human", a `review_events` record
  names Reviewer, and `agent_reviews` is 1 while `independent_reviews` stays 0 for
  humans.
- **RR2, medium.** Delivery evidence and the source contract disagreed on whether an
  independent editorial review exists. Fixed: every status now says "independent human"
  where a human gate is meant, and the agent review is recorded separately.
- **RR3, low.** `needs-remediation` did not require remediation on the medium/high
  finding. Fixed: the validator now requires that pairing, with a test.
- **RR4, low.** The review record's A7 still said 333 tests. Fixed: final count is 348.
- **RR5, low.** Test coverage gaps remained. Fixed: tests now cover partial checks,
  kind/ID/Phase-4 mismatches, medium-in-bounded and medium-remediation pairing.
- **RR6, low.** The review record was untracked and had imprecise provenance. Fixed:
  it is tracked, links issue #288, and names the local-link scope.
- **RR7, low.** The report overclaimed that all findings were addressed. Fixed: the
  report and status now distinguish the 17 review findings and the 7 re-review residuals.

## Remaining limits

- This is agent review, not human review or owner acceptance. Those gates remain open.
- The review did not reopen external sources or verify every claim.
- The 118 low findings were checked structurally; 8 were sampled for prose, including 4
  read against page text.
- The audit remains a bounded page reading, not a claim-by-claim source verification.
