# Pooled qrels v3 — review packets

Status: **unreviewed**. No final v3 labels exist.

## What this is

A page-level candidate pool for 188 answerable queries from qrels v2, phase3
and V12. Candidates come from BM25 top-10 and best-mode top-10, deduplicated by
page. Prior qrels are recorded as seed evidence, not as final grades.

- Pool: ../corpus-qrels.v3.pool.json
- Packets: packet-01.json ... packet-10.json
- Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa
- Level: page

## Independent review only

The authoring agent must not provide the final grades. Use a reviewer that is
independent of this session and has read-only access.

For each packet:

1. Read the query, prior paths, and every candidate page.
2. Grade every candidate page:
   - 0 = not relevant;
   - 1 = partially relevant/background;
   - 2 = directly answers the query.
3. Do not use the prior label as the answer; it is only context.
4. Do not consider whether BM25 or best mode returned the page.
5. Record a short note for each non-zero grade.

Return JSON:

```json
{
  "schema_version": 1,
  "packet": 1,
  "reviewer": "name/vendor/model",
  "reviewed_at": "2026-10-29",
  "head": "544ee40c",
  "grades": {
    "Q001": {"book/path.md": 2},
    "Q002": {"book/path.md": 1}
  }
}
```

Every candidate in the packet must have a grade. Do not add new candidates
without recording them separately.

## Merge

After all ten reviewed packets exist:

```sh
python3 scripts/merge_qrels_v3_labels.py --labels evaluation/qrels-v3/reviewed
```

The merge writes `evaluation/corpus-qrels.v3.json` only when every query and
candidate is graded. It is diagnostic evidence, not owner acceptance.

## Limits

- Priors are author/agent labels; not independent.
- Page-level grades; section-level precision is a separate future task.
- No human review, CI, owner acceptance or sufficient coverage is claimed until
  the independent reports exist.
