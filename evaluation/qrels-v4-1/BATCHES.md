# Qrels v4.1 batches

Each Codex run expands exactly **10 queries** from the frozen v4 set.

| Batch | IDs |
|---|---|
| B01 | V4-A001–V4-A010 |
| B02 | V4-A011–V4-A020 |
| B03 | V4-A021–V4-A030 |
| B04 | V4-B001–V4-B010 |
| B05 | V4-B011–V4-B020 |
| B06 | V4-B021–V4-B030 |
| B07 | V4-B031–V4-B040 |
| B08 | V4-B041–V4-B050 |
| B09 | V4-B051–V4-B060 |
| B10 | V4-B061–V4-B070 |
| B11 | V4-B071–V4-B080 |
| B12 | V4-B081–V4-B090 |
| B13 | V4-V001–V4-V010 |
| B14 | V4-V011–V4-V020 |
| B15 | V4-V021–V4-V030 |

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
