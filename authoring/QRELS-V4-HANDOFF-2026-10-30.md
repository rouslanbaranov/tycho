# Qrels v4 — independent Codex handoff

Status: handoff only. No qrels v4 labels exist yet.

## Mandatory working directory

Work only in the isolated clone:

```sh
cd ~/Projects/tycho-index-and-search
```

Absolute path: `/Users/rbaranov/Projects/tycho-index-and-search`. Do not use
`/Users/rbaranov/Projects/tycho` or any other checkout.

## Goal

Create an independent, AI-adjudicated qrels v4 from the book pages, atlas cards
and V12 artifacts. v4 must be suitable for evaluating the current search stack
without reusing v3 judgments.

This is AI-only evaluation. It is not human review, CI, owner acceptance or
sufficient coverage.

## Independence rules

The Codex session must not read or use:

- `evaluation/corpus-qrels.v3.json`
- `evaluation/section-qrels.v3.json`
- `evaluation/corpus-qrels.v3.pool.json`
- `evaluation/section-qrels.v3.pool.json`
- `evaluation/qrels-v3/`
- `evaluation/section-qrels-v3/`
- v2, phase2, phase3 or V12 qrels
- current search results, rankings, scores or hybrid/reranker outputs
- author conclusions, target metrics or desired labels

Do not try to reproduce v3. Do not optimize for the current retrieval stack.

Allowed read-only inputs:

- `book/**/*.md` — pages, cards, landings, V12 volume
- `edition/atlas-manifest.json`
- `edition/outline.json`
- `edition/patterns/registry.v1.json`
- other atlas metadata under `edition/`
- `generated/v12-index.v1.json`
- `generated/sections-fts-v5.sqlite` only for section identity lookup

Do not edit `book/**`, `edition/**`, `generated/**`, indexes or hashes.

## Query set

Target **150 fresh queries**:

| Split | Count | Scope |
|---|---:|---|
| `book` | 90 | conceptual and operational questions answered by book pages |
| `atlas` | 30 | pattern/card decisions from the atlas layer |
| `v12` | 30 | V12 model, scenario, validation, evidence and decision rules |

Requirements:

- fresh wording; no copied v3/v2/phase questions;
- one clear information need per query;
- answerable from the corpus at the recorded snapshot;
- no private, restricted or external-source-only questions;
- no question that requires editing or executing code;
- diversify across volumes, chapters and cards;
- for V12, cover contracts, scenario inputs, DES/queues, validation,
  provenance, uncertainty and decision use.

## Candidate pool

For every query, create **4–10 page candidates**:

- include the direct answer, partial/background pages and plausible distractors;
- choose them by reading headings/content and atlas metadata, not by current
  search ranking;
- do not include only accepted pages;
- at least one candidate must be grade 0 when a plausible distractor exists.

For every query, create **4–10 section candidates** from the same page pool.
Use exact H2 sections where possible. If a card has no H2, use its `overview`
section if the index exposes one.

Get `section_key` from the read-only sections DB:

```sh
sqlite3 -readonly generated/sections-fts-v5.sqlite \
  "SELECT section_key,path,section_id,heading,heading_level
   FROM sections WHERE path='book/...';"
```

Do not query FTS ranking tables for candidate selection.

## Labels

Use three grades:

- **2** — directly answers the query;
- **1** — partially relevant/background, not sufficient alone;
- **0** — not relevant.

For each query:

- every candidate must have a grade;
- at least one page must be grade 2;
- `accepted` = paths with grade >= 1;
- `direct` = paths with grade 2;
- page and section labels must agree: a grade-2 section implies its page is at
  least grade 1; a grade-0 page cannot have a grade-1/2 section.

Do not infer a label from a title alone. Read the page/section body.

## Output

Write exactly these files:

1. `evaluation/corpus-qrels.v4.json`
2. `evaluation/section-qrels.v4.json`
3. `evaluation/qrels-v4/REPORT.md`
4. `evaluation/qrels-v4/validation.txt`

Page file:

```json
{
  "schema_version": 4,
  "status": "ai-adjudicated-not-human",
  "level": "page",
  "snapshot": "<section index snapshot>",
  "content_commit": "<git HEAD>",
  "reviewer": "OpenAI Codex / model exposed by harness",
  "query_count": 150,
  "items": [
    {
      "id": "V4-B001",
      "split": "book",
      "question": "Fresh question",
      "grades": {"book/path.md": 2, "book/other.md": 0},
      "accepted": ["book/path.md"],
      "direct": ["book/path.md"]
    }
  ],
  "limits": "AI-adjudicated, not human review, not CI or sufficient coverage."
}
```

Section file: same shape with `"level": "section"` and `grades` keyed by
`section_key`; `accepted`/`direct` are section keys.

IDs:

- `V4-B001` … `V4-B090`
- `V4-A001` … `V4-A030`
- `V4-V001` … `V4-V030`

## Validation

Run:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/corpus-qrels.v4.json \
  --section evaluation/section-qrels.v4.json
```

The validator checks:

- schema, status and levels;
- unique IDs and splits;
- page and section queries match by ID;
- all paths exist;
- section keys map to an existing path;
- grades are 0/1/2;
- accepted/direct agree with grades;
- page/section consistency;
- counts and snapshot.

Do not edit the validator to accept invalid labels.

## Report

`REPORT.md` must state:

- reviewer harness/model and date;
- HEAD and snapshot;
- query counts by split;
- candidate and grade counts;
- method for question and candidate selection;
- confirmation that v3/v2/phase qrels and current rankings were not read;
- limitations and disagreements;
- no human/CI/owner acceptance claim.

## Stop conditions

Stop and report instead of inventing labels when:

- a path or section cannot be resolved;
- the book does not answer a planned question;
- a card has no readable section identity;
- the snapshot changes during the run;
- candidate selection would require current search rankings.

Do not modify book, atlas, indexes, qrels v2/v3 or production configuration.
