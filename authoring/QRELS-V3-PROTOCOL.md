# Qrels v3 protocol — 2026-10-29

Status: pooled candidate set; independent adjudication pending.

## Why v3

Qrels v2 accepted sets are not exhaustive, phase3 labels are agent-adjudicated,
and V12 labels are author-labelled. Top-1 misses include valid unlabelled pages.
v3 is a new artifact; v2 and phase3 remain immutable historical evidence.

## Pool

- 188 answerable queries: 155 v2, 19 phase3, 14 V12.
- Candidate sources: BM25 top-10 and best-mode top-10.
- Deduplication: page path.
- 2,038 candidates; prior accepted pages are included as seed evidence.
- Snapshot: e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa.
- Level: page.

## Labels

- 0 = not relevant;
- 1 = partially relevant/background;
- 2 = directly answers.
- Prior qrels are context only, not final grades.
- Independent reviewer; not the authoring agent/session.

## Packets

Ten JSON packets, 20 queries each. A reviewed packet must grade every candidate
and must be stored under evaluation/qrels-v3/reviewed/.

## Merge

scripts/merge_qrels_v3_labels.py validates completeness and writes
evaluation/corpus-qrels.v3.json. The merge is diagnostic; it is not owner
acceptance, CI or sufficient coverage.

## Limits

- Page-level only.
- Candidate pool is not exhaustive beyond BM25/best top-10.
- No final labels yet.
