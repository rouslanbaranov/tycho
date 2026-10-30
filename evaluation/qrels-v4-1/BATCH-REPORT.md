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
