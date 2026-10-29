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

The branch was later merged with the current atlas-promotion branch head
`8649953f186d35b3191d35b9a925866fac87920d`; the V12 book pages are unchanged, while the
manifest, route index, inventory and review-packet source binding were regenerated for the
expanded corpus.

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
| Scenario contracts | 10 in `edition/v12/scenarios/` |
| Run records | 10 in `edition/v12/runs/` |
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
constraints: success 0.9996, p95 1.206 s, cost 1.34 per 1000 successes. Candidate C is
eliminated by the declared cost and p95 constraints. The recommendation
is conditional on an unverified operability constraint and uncalibrated inputs.

The modernization experiment compares a staged cutover with a no-cutover baseline. The
staged path produces a maximum divergence of 8,925.5 records and completes rollback within
2,400 seconds in only 10% of replications; non-completing rollback durations are censored
at 1,200 seconds after the trigger, with a mean censored duration of 1,080 seconds. The
decision record returns `insufficient-evidence`.

The sensitivity screen reports first-order and total-order indices for arrival rate and
service mean. It is a quadratic response-surface screen, not a full pick-freeze Sobol
analysis. The sensitivity run is converged; a separate two-replication
convergence-stress run is marked insufficient-sample.

## Validation evidence

Run from the worktree root:

```text
python3 scripts/validate_v12.py
PASS: V12 structure, hashes, reverse index and iron rule

python3 scripts/validate_edition.py
canonical_documents: 498
volumes: 12
chapters: 89
v12_documents: 31

python3 -m unittest discover -s tests -p 'test_tycho*.py'
Ran 709 tests in 81.3s
OK

node tools/mermaid/check.mjs --root .
242 diagrams checked; 242 passed
```

The V12 validator checks strict schemas, unique identifiers, referential integrity, model
and scenario hashes, run result hashes, the derived reverse index, source-plan links, the
V12 Markdown line limit and the protected baseline.

## Protected baseline

The baseline contains 467 existing book pages and five promotion/atlas/review records. The
validator reports:

```json
{"protected_pages": 467, "promotion_records": 5, "changed": 0, "missing": 0, "leaked": 0}
```

No existing page, card, owner page, sufficient-promotion record or atlas
manifest was edited. The only new files under book/ are the V12 volume pages.
One existing re-review packet had its route-source binding refreshed as
recorded below.

## Derived artifacts refreshed

The route index, edition inventory, edition outline, V12 index and reverse index were
regenerated from the expanded corpus. The existing re-review packet record had one source
binding refreshed from the full route hash to the V1-V11 legacy route snapshot
(`4903632b...`); no packet content, verdict template or reviewer field changed. The legacy
binding keeps the existing pattern evidence stable when V12 pages change. The Phase 4
artifact route hash was refreshed in the same way.

## Pre-existing local check failures

One check fails at the target branch head and on this branch:

- scripts/check_markdown_line_length.py reports two V11 lines over 100 characters.

The failure is not caused by V12. It is recorded here instead of being hidden or repaired
inside this issue. The V12 validator checks the V12 line limit independently. The Phase 4
artifact now passes after its legacy route-hash refresh. validate_book_navigation.py reports
four pre-existing anchor issues in two V11 pages at the target head; V12 pages add none.

## Independent review round 1

The first OpenAI Codex review (GPT-5-based; exact serving version not exposed; read-only,
pinned to the initial commit) returned
reject with three blocking findings: declared input correlations were not applied, stored B
and C runs were not reproducible from the pinned engine, and a stale completion event could
complete a later retry attempt. It also found two high, three medium and one low issue.

Corrections applied in this branch:

- Gaussian-copula sampling now applies the declared correlation matrix;
- every service and timeout event carries an attempt token, so a stale event cannot affect a
  later attempt;
- cost uses the measurement window rather than the full horizon;
- run records store the conservation invariant and the engine source hash;
- the run schema requires result_sha256 and invariants;
- source-register labels now match the bounded ledger coverage;
- model verification records name the actual test methods;
- the re-review packet is included in the protected baseline;
- regression tests cover correlation, stale-completion, cost window, invariants and replay
  of every committed run.

The initial review report is saved verbatim as
\`authoring/ai-reviews/2026-10-29-v12-isolated-volume-codex.md\` and indexed with verdict
reject. A delta review of the corrected artifacts is the next gate.

## Independent review round 2

A delta review of the correction commit returned reject with one blocking, one high and two
medium findings:

- N1: queue wait was no longer included in the per-attempt deadline, and a queued timeout did
  not consume the attempt budget;
- N2: correlated inputs were passed to an independent-input response-surface decomposition;
- N3: rollback duration aggregation silently dropped failed rollbacks;
- N4: correction metadata contained stale run counts and unsupported model-version claims.

Corrections applied:

- the attempt starts at arrival or retry, the deadline covers queue wait, and a queued
  timeout consumes the attempt budget;
- the sensitivity scenario is independent and the engine rejects a correlated screen; the
  correlated-input run remains a separate Monte Carlo propagation;
- non-completing rollback durations are censored at the elapsed time from the trigger to the
  horizon and the limitation is stored;
- the decision, review index, implementation record and decision constraint evidence were
  corrected, and the packet baseline limitation is recorded.

The delta review report is saved verbatim as
\`authoring/ai-reviews/2026-10-29-v12-isolated-volume-delta-codex.md\` and indexed with
verdict reject. A second delta review of the corrected artifacts is the next gate.

## Independent review round 3

A second delta review returned pass-with-findings. N1 and N2 were resolved. N3 remained
partially resolved because a non-completing rollback used the full scenario duration instead
of elapsed time since the trigger; N4 remained partially resolved because corrected prose
retained stale overload percentages and an outdated pick-freeze engine description. The low
finding noted missing direct assertions for the attempt budget, censoring and correlated-screen
rejection.

Corrections applied:

- unfinished rollback durations are censored at duration minus rollback trigger time;
- overload prose uses the corrected timeout and rejection rates;
- the engine docstring describes the quadratic response-surface screen;
- modernization failure bullets are marked as hypothetical failure cases;
- regression tests assert the attempt budget, elapsed censoring and correlated-screen
  rejection.

The pass-with-findings report is saved verbatim as
\`authoring/ai-reviews/2026-10-29-v12-isolated-volume-delta2-codex.md\` and indexed. A final
delta review of these corrections is the last review gate.

## Independent review round 4

The third delta review returned pass-with-findings. N3, N4 and the test-gap finding were
resolved. The only remaining finding was low severity: the newly added review-index table row
exceeded the 100-character Markdown line limit.

The V12 review records were moved from long table rows to wrapped bullet records, and the AI
review validator now parses that form. The report is saved verbatim as
\`authoring/ai-reviews/2026-10-29-v12-isolated-volume-delta3-codex.md\` and indexed. A focused
final delta review of this editorial correction is the last review gate.

## Independent review round 5

The focused final review returned pass-with-findings. The prior index-row finding was
resolved. The only remaining finding was low severity: the saved raw reviewer report contains
two lines over 100 characters because the report is preserved verbatim.

That finding is recorded as a preservation exception, not edited away: raw external reviewer
output must remain verbatim, while authored Markdown remains within the line limit. There are
no blocking, high or medium findings in the final review.

## Limits

- Every V12 model is uncalibrated.
- All workloads and parameters are synthetic.
- The sensitivity screen is an approximation.
- Confidence intervals use a normal approximation across replications.
- No production, security, compliance or migration-safety claim is made.
- No existing pattern is promoted, demoted or re-reviewed.
- Independent review and owner acceptance remain separate decisions.

## Review gate

Five independent read-only reviews are saved under `authoring/ai-reviews/` and indexed with
their SHA-256 values. The final focused review is pass-with-findings, with one recorded
raw-report line-length exception and no blocking, high or medium finding. A review verdict is
evidence, not owner acceptance.

## Owner acceptance

Ruslan Baranov accepted the V12 delivery on 2026-10-29 at 15:34 Europe/Zurich. The record is
`authoring/V12-OWNER-ACCEPTANCE-2026-10-29.md`; it binds the accepted content commit
`6c60ffabe1e5a3ab7158612691cca47bd89aff3a`, artifact hashes, review hashes, scope and limits.
The acceptance covers V12 content only and does not assert production, security, compliance
or migration safety. The pull request remains stacked on the atlas-promotion branch and must
be retargeted to main after that branch merges.
