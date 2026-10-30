# Qrels v4.1 batch report

Codex appends one entry per batch:

```text
Batch:
IDs:
HEAD:
Snapshot:
Page candidates:
Section candidates:
Outcome:
Limitations:
```

Do not claim human review, CI, owner acceptance or sufficient coverage.

## B01

Batch: B01
IDs: V4-A001–V4-A010
HEAD: 457f90ad982cada07ccccf001249d6cbd6d1250a
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B01`.
Limitations: AI-adjudicated only; structural neighbors came from the original candidate pool,
without current rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B05

Batch: B05
IDs: V4-B011–V4-B020
HEAD: 457f90ad982cada07ccccf001249d6cbd6d1250a
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B05`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B12

Scope: `V4-B081`–`V4-B090` (10 book queries).

HEAD: `43502ff9c4316b822b81719304cca1e4954dc10b`.
Snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`.

Counts: 107 page candidates and 107 section candidates; 67 new candidates at each level;
10–11 candidates per query. The additions include 31 new grade-0 page candidates and 31 new
grade-0 section candidates, with at least two new grade-0 candidates for every query.

Method: structural neighbors only—same or adjacent chapters and chapter overview pages. No
current search results, rankings or v3 labels were read or used.

ai_review: `not-required`; this batch changes neither book nor atlas content or structure.

Validation: `validate_qrels_v41_batch.py --batch B12` passed. Every frozen v4 candidate and
grade is preserved, page/section judgments are consistent and every query retains a direct
grade-2 answer. AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.

## B10 — V4-B061–V4-B070

- HEAD: `43502ff9c4316b822b81719304cca1e4954dc10b`.
- Content commit: `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`.
- Snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`.
- Scope: 10 queries, 100 page labels and 100 section labels.
- Expansion: 60 new page candidates and 60 new section candidates; 10 candidates per query.
- New grade-0 labels: 29 page and 29 section labels; 2–5 new grade-0 labels per query.
- Candidate selection used only same or adjacent chapters and chapter overviews. Current search
  rankings, v3 labels and prior adjudication conclusions were not used.
- Validation: the required B10 validator passed. The targeted page/section consistency validator
  also passed for 10 book queries.
- Limitations: AI-adjudicated only; not human review, CI, owner acceptance or sufficient coverage.

## B02

Batch: B02
IDs: V4-A011–V4-A020
HEAD: 457f90ad982cada07ccccf001249d6cbd6d1250a
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B02`.
Limitations: AI-adjudicated only; structural neighbors only, without current rankings. This is
not human review, CI, owner acceptance or sufficient coverage.

## B03

Batch: B03
IDs: V4-A021–V4-A030
HEAD: 457f90ad982cada07ccccf001249d6cbd6d1250a
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B03`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B04

Batch: B04
IDs: V4-B001–V4-B010
HEAD: 457f90ad982cada07ccccf001249d6cbd6d1250a
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B04`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B06
Parent audit: 10 queries V4-B021–V4-B030; 10 page/section candidates per query;
validator PASS. Codex turn ended on the account usage limit after writing both
files; Codex did not append this entry. HEAD 457f90ad; snapshot e7496a66.

## B07
Parent audit: 10 queries V4-B031–V4-B040; 10 page/section candidates per query;
validator PASS. Codex turn ended on the account usage limit after writing both
files; Codex did not append this entry. HEAD 457f90ad; snapshot e7496a66.

## B09

Batch: B09
IDs: V4-B051–V4-B060
HEAD: 43502ff9c4316b822b81719304cca1e4954dc10b
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 46 preserved and 54 new; 10 per query.
Section candidates: 100 total; 46 preserved and 54 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B09`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B08

Batch: B08
IDs: V4-B041–V4-B050
HEAD: 43502ff9c4316b822b81719304cca1e4954dc10b
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 44 preserved and 56 new; 10 per query.
Section candidates: 100 total; 44 preserved and 56 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B08`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B11

Batch: B11
IDs: V4-B071–V4-B080
HEAD: 43502ff9c4316b822b81719304cca1e4954dc10b
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 102 total; 40 preserved and 62 new; 10–11 per query.
Section candidates: 102 total; 40 preserved and 62 new; 10–11 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B11`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B13

Batch: B13
IDs: V4-V001–V4-V010
HEAD: 43502ff9c4316b822b81719304cca1e4954dc10b
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B13`.
Limitations: AI-adjudicated only; candidates came from structural neighbors without current
rankings. This is not human review, CI, owner acceptance or sufficient coverage.

## B15

Batch: B15
IDs: V4-V021–V4-V030
HEAD: 43502ff9c4316b822b81719304cca1e4954dc10b
Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
Page candidates: 100 total; 40 preserved and 60 new; 44 new grade-0; 10 per query.
Section candidates: 100 total; 40 preserved and 60 new; 44 new grade-0; 10 per query.
Outcome: PASS from `validate_qrels_v41_batch.py --batch B15`.
AI review: not-required; this batch does not change book content or atlas structure.
Limitations: AI-adjudicated only; candidates came from same or adjacent V12 chapters,
linked V12 pages and overview pages. Current rankings, v3 labels and prior author
conclusions were not used. This is not human review, CI, owner acceptance or sufficient
coverage.

## B14: V4-V011-V4-V020

- Date: 2026-10-30.
- HEAD: `43502ff9c4316b822b81719304cca1e4954dc10b`.
- Content commit: `7918391fe10bc3c2f91e8358b3ee768cf70fbea2`.
- Snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`.
- Scope: 10 V12 queries, V4-V011 through V4-V020.
- Page qrels: 100 candidates total; 60 new; exactly 6 new per query.
- Section qrels: 100 candidates total; 60 new; exactly 6 new per query.
- New grade-0 labels: 33 page and 33 section; minimum 2 at each level per query.
- Baseline preservation: every existing v4 candidate and grade is unchanged.
- Candidate basis: same or adjacent chapters and chapter overview pages only.
- Current search rankings and v3 labels were not consulted.
- Page SHA-256: `eb8b18aa001cc8cf0f6ca8c43ff71af33ad615ef9030952f00d7cf051cc76177`.
- Section SHA-256: `9fbb6867c08342690b15cf48154fd35294e3948024c76d700d20d35fd99b8296`.
- Validation: `validate_qrels_v41_batch.py --batch B14` passed locally.
- External AI review: not required because no book or atlas content changed.
- Limitations: AI-adjudicated only; not human review, CI, owner acceptance or sufficient
  coverage. The qrels remain pool-relative, and the structural-neighbor restriction may
  omit relevant pages outside the permitted neighborhood.
