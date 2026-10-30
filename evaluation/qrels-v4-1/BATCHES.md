# Qrels v4.1 batches

Each Codex run expands exactly **10 queries** from the frozen v4 set.

| Batch | IDs |
|---|---|
| B01 | V4-A001–V4-A010 |
| B02 | V4-A011–V4-A020 |
| B03 | V4-A021–V4-A030 |
| B04 | V4-A031–V4-A040 |
| B05 | V4-A041–V4-A050 |
| B06 | V4-A051–V4-A060 |
| B07 | V4-A061–V4-A070 |
| B08 | V4-A071–V4-A080 |
| B09 | V4-A081–V4-A090 |
| B10 | V4-A091–V4-A100 |
| B11 | V4-A101–V4-A110 |
| B12 | V4-A111–V4-A120 |
| B13 | V4-A121–V4-A130 |
| B14 | V4-A131–V4-A140 |
| B15 | V4-A141–V4-A150 |

Output per batch:

- `evaluation/qrels-v4-1/batches/<BATCH>.page.json`
- `evaluation/qrels-v4-1/batches/<BATCH>.section.json`

Validate one batch:

```sh
python3 scripts/validate_qrels_v41_batch.py \
  --page evaluation/qrels-v4-1/batches/B01.page.json \
  --section evaluation/qrels-v4-1/batches/B01.section.json \
  --batch B01
```

After all 15:

```sh
python3 scripts/merge_qrels_v41_batches.py \
  --batch-dir evaluation/qrels-v4-1/batches
```
