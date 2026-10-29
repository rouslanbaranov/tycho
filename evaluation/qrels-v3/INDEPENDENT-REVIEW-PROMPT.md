# Independent qrels v3 review handoff

Status: packets prepared, **no independent review performed**.

Use an independent reviewer (not the authoring agent) with read-only access to
`/Users/rbaranov/Projects/tycho-index-and-search` at content commit
`544ee40c`.

Review one packet per run. There are ten packets:
`evaluation/qrels-v3/packet-01.json` ... `packet-10.json`.

## Exact prompt

You are an independent relevance adjudicator for Tycho qrels v3. Work read-only:
do not write, commit, run tests or change configuration. Do not use the prior
labels as the answer; they are context only.

Review exactly one packet, specified below. For every query candidate:
1. read the query and candidate page;
2. grade the page:
   - 0 = not relevant;
   - 1 = partially relevant/background;
   - 2 = directly answers the query;
3. ignore which retriever returned it;
4. add a short note for every non-zero grade.

Return JSON:
```json
{
  "schema_version": 1,
  "packet": 1,
  "reviewer": "name / vendor / model or human",
  "reviewed_at": "2026-10-29",
  "head": "544ee40c",
  "grades": {"Q001": {"book/path.md": 2}},
  "notes": {"Q001": {"book/path.md": "why"}}
}
```

Every candidate path in the packet must have a grade. Do not add new candidates.
Do not claim owner acceptance, CI, human review or sufficient coverage unless
you are the named independent human reviewer.

Packet: <replace with packet path>.

## Merge

After all ten reviewed packets exist:
```sh
python3 scripts/merge_qrels_v3_labels.py --labels evaluation/qrels-v3/reviewed
```

## Limits

- Page-level pooling, not exhaustive beyond BM25/best top-10.
- Priors are stale author/agent labels.
- This is a handoff. No review has run.
