# Codex prompt — qrels v4, all batches in one run

You are the independent external AI evaluator for Tycho. Complete the full
qrels v4 set in this run by processing all ten batches sequentially. Do not stop
after one batch, do not return a plan instead of files, and do not ask for
confirmation between batches.

## Mandatory working directory

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Absolute path: `/Users/rbaranov/Projects/tycho-index-and-search`.

Do **not** use `/Users/rbaranov/Projects/tycho` or any other checkout.

Read:

- `authoring/QRELS-V4-HANDOFF-2026-10-30.md`
- `evaluation/qrels-v4/BATCHES.md`

Do **not** read v3/v2/phase qrels, v3 pools, reviewed packets, the quarantined
`evaluation/qrels-v4/partial/` draft, current search results/rankings, or author
conclusions. Create fresh questions and judgments from the book pages, atlas
cards and V12.

## Batch plan

Process in this exact order. Each batch has 15 queries and must produce both
page and section files before moving on.

| Batch | Split | IDs |
|---|---|---|
| B01 | book | V4-B001–V4-B015 |
| B02 | book | V4-B016–V4-B030 |
| B03 | book | V4-B031–V4-B045 |
| B04 | book | V4-B046–V4-B060 |
| B05 | book | V4-B061–V4-B075 |
| B06 | book | V4-B076–V4-B090 |
| A01 | atlas | V4-A001–V4-A015 |
| A02 | atlas | V4-A016–V4-A030 |
| V01 | v12 | V4-V001–V4-V015 |
| V02 | v12 | V4-V016–V4-V030 |

Outputs:

```text
evaluation/qrels-v4/batches/<BATCH>.page.json
evaluation/qrels-v4/batches/<BATCH>.section.json
```

Append one entry per batch to `evaluation/qrels-v4/BATCH-REPORT.md`.

## Per-batch procedure

For each batch:

1. Select 15 fresh questions from the assigned source area. Use the exact ID
   range and split.
2. For every query, create 4–10 page candidates. Include a direct answer,
   partial/background pages and plausible distractors. Read the page content;
   do not infer from titles.
3. Create 4–10 section candidates from the same pages. Use exact H2 sections
   where possible. Read `section_key` from the read-only
   `generated/sections-fts-v5.sqlite` `sections` table. Do not use FTS ranking
   tables for selection.
4. Grade every candidate: 0 not relevant, 1 partial/background, 2 direct.
   At least one page must be 2. `accepted` is exactly grade >=1; `direct` is
   exactly grade 2.
5. Enforce page/section consistency: a direct section implies its page is at
   least partial; a grade-0 page cannot have an accepted section.
6. Write the batch page and section JSON files. Do not write the final
   `corpus-qrels.v4.json` or `section-qrels.v4.json` yet.
7. Run the batch validator:
   - book: `--book 15 --atlas 0 --v12 0`
   - atlas: `--book 0 --atlas 15 --v12 0`
   - v12: `--book 0 --atlas 0 --v12 15`
8. If the validator fails, fix that batch and rerun it before starting the next
   batch. Do not continue with invalid files.
9. Record HEAD, snapshot, query/candidate counts, method and limitations in
   `BATCH-REPORT.md`.

Validator pattern for B01:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B01.page.json \
  --section evaluation/qrels-v4/batches/B01.section.json \
  --book 15 --atlas 0 --v12 0
```

## Finish

After all ten batches pass individually:

```sh
python3 scripts/merge_qrels_v4_batches.py \
  --batch-dir evaluation/qrels-v4/batches
```

The merge must create:

- `evaluation/corpus-qrels.v4.json`
- `evaluation/section-qrels.v4.json`

Then run the full validator with default counts (90/30/30) and save its output to
`evaluation/qrels-v4/validation.txt`. Write `evaluation/qrels-v4/REPORT.md`
with HEAD, snapshot, counts, method, limitations and confirmation that v3/partial
labels and current rankings were not read.

## Completion criteria

Do not finish until:

- all ten batch page files exist;
- all ten batch section files exist;
- every batch passed its validator;
- the merge script exited 0;
- `corpus-qrels.v4.json` has 150 queries;
- `section-qrels.v4.json` has 150 queries;
- the full validator passed;
- `REPORT.md` and `validation.txt` exist.

If a path or section cannot be resolved, choose a different resolvable question
for that slot. Do not invent an ID, path, section key or label. If the snapshot
changes, stop and report the exact mismatch.

## Hard rules

- Do not edit `book/**`, `edition/**`, `generated/**`, indexes, qrels v2/v3,
  source catalog or production configuration.
- Do not use current search rankings to choose candidates.
- Do not merge the quarantined partial draft.
- Do not claim human review, CI, owner acceptance or sufficient coverage.
- State clearly: AI-adjudicated only.

Do not return an intermediate summary as the final answer. Complete the batches
and the merge in this run.
