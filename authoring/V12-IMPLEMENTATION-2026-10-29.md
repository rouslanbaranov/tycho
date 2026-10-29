# V12 implementation record — 2026-10-29

Status: implemented in the issue-specific branch; independent review is a separate gate.
This record describes what was built, what was checked and what remains unmeasured. It is
not owner acceptance, CI, production validation or pattern promotion.

## Activation and branch

The owner activated issue #587 for one complete implementation pass on 2026-10-29. The work
is isolated in the worktree branch:

```text
feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume
```

The V12 volume lives at:

```text
book/volumes/v12-modeling-simulation-and-decision-validation/
```

The iron rule is unchanged: V12 references existing patterns; existing patterns do not
reference V12. The protected baseline is recorded in `edition/v12/protected-baseline.json`.

## Delivered artifacts

| Artifact | Count or path |
|---|---|
| V12 book pages | 31 Markdown pages: one volume, seven chapters, twenty-three question pages |
| Model contracts | 3 in `edition/v12/models/` |
| Scenario contracts | 9 in `edition/v12/scenarios/` |
| Run records | 9 in `edition/v12/runs/` |
| Decision records | 2 in `edition/v12/decisions/` |
| Source reading ledger | 10 records in `edition/v12/reading-ledger.v1.json` |
| Source plan | 8 topics and 16 bounded units in `edition/v12/source-plan.v1.json` |
| Registry | `edition/v12/registry.json` |
| Reverse index | `edition/v12/reverse-index.v1.json` |
| Search namespace | `generated/v12-index.v1.json` |
| Manifest | `edition/v12/manifest.json` |
| Engine | `scripts/v12_engine.py` |
| Validator | `scripts/validate_v12.py` |
| Index builder | `scripts/build_v12_index.py` |

## Source admissions

Nine public sources were admitted to `sources/register.json` and the catalogue was
regenerated: SimPy 4.1 documentation, Owen's Monte Carlo chapters, MIT ESD.00 system
dynamics lectures 2-4, Sargent's verification and validation paper, W3C PROV-O, MADR,
Nygard's decision-record article, the PLOS reproducibility rules and JCGM 100:2008. One
existing source, `src.little-law`, gained a bounded V12 reading record.

Each reading record stores the unit, revision, representation SHA-256, line and word counts,
sections read, omissions, claims supported and claims not supported. Registration is not
reading; reading is not independent review.

## Experiments

The comparative experiment uses one synthetic workload, one seed scheme and one metric set
for three checkout candidates. Candidate B is decision-supported under the declared
constraints: success 0.9996, p95 1.206 s, cost 1.60 per 1000 successes. Candidate C is
eliminated by the declared cost and latency constraints. The recommendation is conditional
on an unverified operability constraint and uncalibrated inputs.

The modernization experiment compares a staged cutover with a no-cutover baseline. The
staged path produces a maximum divergence of 10,102.8 records and does not complete rollback
within 2,400 seconds. The decision record returns `insufficient-evidence`.

The sensitivity screen reports first-order and total-order indices for arrival rate and
service mean. It is a quadratic response-surface screen, not a full pick-freeze Sobol
analysis, and its run is marked `insufficient-sample`.

## Validation evidence

Run from the worktree root:

```text
python3 scripts/validate_v12.py
PASS: V12 structure, hashes, reverse index and iron rule

python3 scripts/validate_edition.py
canonical_documents: 480
volumes: 12
chapters: 89
v12_documents: 31

python3 -m unittest discover -s tests -p 'test_tycho*.py'
Ran 622 tests in 39.974s
OK

node tools/mermaid/check.mjs --root .
242 diagrams checked; 242 passed
```

The V12 validator checks strict schemas, unique identifiers, referential integrity, model
and scenario hashes, run result hashes, the derived reverse index, source-plan links, the
V12 Markdown line limit and the protected baseline.

## Protected baseline

The baseline contains 449 existing book pages and four promotion/atlas records. The
validator reports:

```json
{"protected_pages": 449, "promotion_records": 4, "changed": 0, "missing": 0, "leaked": 0}
```

No existing page, card, owner page, promotion record or atlas manifest was edited. The only
new files under `book/` are the V12 volume pages.

## Derived artifacts refreshed

The route index, edition inventory, edition outline, V12 index and reverse index were
regenerated from the expanded corpus. The existing re-review packet record had one source
binding refreshed from the full route hash to the V1-V11 legacy route snapshot
(`0ba9ebd...`); no packet content, verdict template or reviewer field changed. The legacy
binding keeps the existing pattern evidence stable when V12 pages change.

## Pre-existing local check failures

Two checks fail at the branch base commit `4f111f25` as well as on this branch:

- `scripts/phase4_audit.py --check` reports `phase4-artifact-stale` because the committed
  Phase 4 artifact predates recent sufficient promotions in the pattern registry.
- `scripts/check_markdown_line_length.py` reports three V11 lines over 100 characters.

Neither failure is caused by V12. They are recorded here instead of being hidden or repaired
inside this issue. The V12 validator checks the V12 line limit independently.

## Limits

- Every V12 model is uncalibrated.
- All workloads and parameters are synthetic.
- The sensitivity screen is an approximation.
- Confidence intervals use a normal approximation across replications.
- No production, security, compliance or migration-safety claim is made.
- No existing pattern is promoted, demoted or re-reviewed.
- Independent review and owner acceptance remain separate decisions.

## Review gate

The independent read-only review is recorded under `authoring/ai-reviews/` when it runs.
Its verdict is evidence, not owner acceptance.
