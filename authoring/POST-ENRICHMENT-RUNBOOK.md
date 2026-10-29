# Post-enrichment search runbook

Status: planned procedure for the next content change. Quality claims remain
suspended until the steps complete.

## 1. Freeze

- Confirm the enrichment branch is at the reviewed content commit.
- Run search_reindex.py snapshot on a clean checkout.
- Preserve the previous pre-enrichment manifest as historical evidence.
- Do not overwrite the pre-enrichment manifest.

## 2. Rebuild and diff

- Run search_reindex.py rebuild.
- Run search_reindex.py diff against the pre-enrichment manifest.
- Review changed/added/removed pages and qrels changes.
- Run check; qrels-stale is expected until re-adjudication.

## 3. Re-adjudicate evidence

- Rebind qrels v2 accepted answers to changed pages/sections.
- Re-check all 29 excluded phase-3 items; enrichment may make some answerable.
- Rebuild the phase-3 human sample; human review remains pending until done.
- Do not tune BM25 or the refusal gate before labels are stable.

## 4. Review and merge

- External different-vendor AI review is required because book content changes.
- Save raw report under authoring/ai-reviews/ with SHA-256.
- Merge only after findings are resolved and premerge passes.

## 5. Quality work

- Recalibrate only after the new labels are frozen.
- Publish separate pre/post metrics; never mix snapshots.
- State sufficient: 0 unless separate evidence exists.

## Rollback

Keep the previous manifest and index version. Rebuild from the prior content
commit; do not hand-edit qrels or the index.

## One-command diagnostic gate

```sh
python3 scripts/post_enrichment_check.py --regression
```

It runs manifest check, section diff, deep index verify and optional retrieval
fingerprints. Exit code 0 means deep verification passed; changed pages/qrels
are expected and are not quality acceptance.

