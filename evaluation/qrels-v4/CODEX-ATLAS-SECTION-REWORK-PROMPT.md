# Codex prompt — atlas A01–A02 section specificity rework

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Read `authoring/QRELS-V4-HANDOFF-2026-10-30.md` and
`evaluation/qrels-v4/BATCHES.md`.

Do not read v3/v2/phase qrels, current search rankings, author conclusions, or
the old A01/A02 labels. The old files are backed up under
`evaluation/qrels-v4/batches/provisional-entry-inventory-a01-a02/`; do not
reuse them.

## Problem

The current A01/A02 section judgments sometimes use the broad
`#entry-inventory` section from an atlas chapter README. That section lists
many cards; it is not specific to the card being judged.

## Task

Replace A01/A02 with reworked page+section batches under the same IDs:

| Batch | Split | IDs |
|---|---|---|
| A01 | atlas | V4-A001–V4-A015 |
| A02 | atlas | V4-A016–V4-A030 |

Overwrite only:

```text
evaluation/qrels-v4/batches/A01.page.json
evaluation/qrels-v4/batches/A01.section.json
evaluation/qrels-v4/batches/A02.page.json
evaluation/qrels-v4/batches/A02.section.json
```

Do not merge and do not touch B/V batches.

## Section specificity rule

- Prefer the dedicated atlas card page and its exact H2 section.
- If a card page has no H2, its `#overview` section is acceptable: it is the
  whole card, not a chapter inventory.
- **Do not use any section key ending in `#entry-inventory`.**
- If a query's only section support is a chapter README inventory, replace that
  candidate with a dedicated card page or replace the query with another atlas
  card that has a dedicated page. Do not keep the inventory anchor.
- Page and section labels must agree: a direct section implies its page is at
  least partial; a page with grade 0 cannot have an accepted section.

Target: **zero** `#entry-inventory` section keys across A01 and A02. If a
genuine exception exists, report it explicitly and do not silently relabel.

## Coverage and labels

Each batch:

- 15 fresh atlas queries;
- at least 10 distinct cards and 5 atlas chapters;
- no more than 2 queries from one card/chapter;
- 4–10 page and 4–10 section candidates per query;
- grades 0/1/2; at least one direct grade 2;
- exact accepted/direct sets.

Use section keys from the read-only `generated/sections-fts-v5.sqlite`
`sections` table. Read the card body; do not infer from titles.

## Validate

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/A01.page.json \
  --section evaluation/qrels-v4/batches/A01.section.json \
  --book 0 --atlas 15 --v12 0
```

Repeat for A02. Then run a check:

```sh
python3 - <<'PY'
import json
for b in ("A01","A02"):
 d=json.load(open(f"evaluation/qrels-v4/batches/{b}.section.json"))
 n=sum(1 for i in d["items"] for k in i["grades"] if k.endswith("#entry-inventory"))
 print(b,"entry-inventory",n)
PY
```

Both counts must be zero.

Append the A01–A02 rework to `evaluation/qrels-v4/BATCH-REPORT.md` with card,
chapter and inventory counts.

## Finish

Do not merge. Record HEAD, snapshot, coverage, candidate counts and limits.
State: AI-adjudicated only; not human review, CI, owner acceptance or sufficient
coverage.
