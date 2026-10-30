# Qrels v4 — final AI-adjudicated set

Status: **complete draft; B01–B03 coverage rework pending.** Not human review,
independent review, CI, owner acceptance or sufficient coverage.

The current files still contain the narrow B01–B03 batches. Re-merge after the
coverage rework.

## Files

- `evaluation/corpus-qrels.v4.json` — page level
- `evaluation/section-qrels.v4.json` — section level
- `evaluation/qrels-v4/validation.txt` — validator PASS

Both files contain 150 queries: 90 book, 30 atlas, 30 V12.

## Counts

| File | Queries | Candidates | Accepted | Direct |
|---|---:|---:|---:|---:|
| page | 150 | 628 | 455 | 203 |
| section | 150 | 628 | 454 | 203 |

Snapshot: `e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa`.  
Content commit: `7918391f`.

## Method

Ten Codex batches of 15 queries: B01–B06 book, A01–A02 atlas, V01–V02 V12.
Questions and candidates were built from read-only book pages, atlas cards and
V12 artifacts. Section keys came from the read-only sections DB. V3/v2/phase
labels, the quarantined partial draft and current search rankings were not read.

`validate_qrels_v4.py` checks schema, counts, IDs, paths, section identity,
grades, accepted/direct sets, page/section consistency and canonical content.

## Coverage limits

- **B01–B03 are coverage-narrow**: each is concentrated in one chapter/topic.
  They passed schema validation but are not representative of the whole book.
- B04–B06 span 5/5, 8/8 and 9/12 volumes/chapters.
- A01–A02 cover 15 distinct cards across 8 atlas chapters each.
- V01 spans 6 V12 chapters; V02 spans 5.
- Atlas cards use the broader `Entry inventory` section where no narrower H2
  exists.
- V12 judgments use V12 book pages, not individual artifact records.
- Candidate pools are 4–10 pages/sections, not exhaustive.
- Final merge normalizes `content_commit` to `7918391f`; book/edition/generated
  were verified unchanged to current HEAD.

## Limits

AI-adjudicated only. No human review, CI, owner acceptance or sufficient
coverage. Do not treat PASS as judgment-quality proof.
