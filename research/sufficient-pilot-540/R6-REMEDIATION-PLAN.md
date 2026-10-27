# R6 remediation plan

Date: 2026-10-27. Owner decision: admit new public sources that support the claims; where no
such source is found, rewrite the claims in the book and owner units to the exact wording of
admitted sources. No promotion before a fresh external review and owner acceptance.

## Current state

- external reviews rejected the 25 review-ready candidates;
- 0 review-ready, 0 `sufficient`, 0 promotions;
- 103 `partial`, 42 `partial-bounded`, 145 rejected;
- every batch result is generated from owner units.

## Rules

1. Source-first: search for a public, admitted unit whose exact text supports the whole
   claim. Add the unit, ledger record and binding; do not stretch a nearby quote.
2. Rewrite fallback: narrow the book sentence, atlas card, owner claim and binding together.
   A claim that is not in the book cannot be an owner claim.
3. One bounded entry per change set. Do not mix unrelated entries.
4. A book edit requires the full change pipeline: content revision, atlas manifest,
   semantic audit, route index, census, coverage and phase4 refresh.
5. External review follows each completed change set. A review rejection reopens the entry.
6. Owner acceptance remains a separate record; an external pass is not acceptance.

## Pilot sequence

- **Static Content Hosting.** The failure claim combines purge loss, cold-cache storms and
  origin failover. First find a CDN/origin source for the full failure claim; otherwise
  narrow to purge propagation and browser-cache persistence.
- **Transactional Outbox.** The alternative names direct publication, while the binding only
  says event sourcing is an alternative. Find a source for direct publication with
  reconciliation; otherwise narrow to event sourcing as the competing approach.
- **Valet Key.** Audience binding and over-scoping exceed the Microsoft unit. Find an
  OAuth/RFC unit covering audience and revocation; otherwise narrow to scoped, time-limited,
  revocable access.

Each pilot must end in one of: `review-ready`, `remediation` with a recorded source gap, or
`rejected`. It must never end in an unrecorded `supported` state.

## Book-edit checklist

1. Edit the owner page and the atlas card; keep lines at or below 100 characters.
2. Record the authorized page hashes in `edition/content-revisions.json`.
3. Update `edition/atlas-manifest.json` document hashes and re-review V11 pages.
4. Update `edition/patterns/semantic-audit.v1.json` for changed pages.
5. Rebuild route index, section FTS, census, coverage, phase4 and inventory.
6. Regenerate owner units, registry, delivery evidence and the batch result.
7. Run tests, `check_boundary`, `validate_*` and `premerge_check`.
8. Save the external report and index it by SHA-256 before any promotion.

## Acceptance gate

- technical: every dimension binding names a read section and a revision, and the exact
  quote supports the full claim;
- decision: four dimensions justify the card question without circularity;
- external: verdict `pass`, no blocking finding;
- owner: explicit acceptance record.

Until all four hold, `sufficient: 0` and no promotion record is written.

## Parallelization

Parallel work is allowed only where evidence cannot race.

- Lane A: read-only subagents audit one entry each. They return exact claims, quotes,
  bindings and gaps; they do not write, classify support or issue verdicts.
- Lane B: the parent applies book and owner-unit changes serially. Entries sharing an
  owner page stay in one change set.
- Lane C: shared artifacts are rebuilt once after the serial edits.
- Lane D: external reviewers run at one frozen HEAD, one bounded scope per run. Do not
  edit the repository while a review is running.

A subagent report is never review evidence. The parent recomputes every quote, section,
revision and hash before use. External review remains the only independent gate.
