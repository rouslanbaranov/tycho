# Qrels v4 batches

Each Codex run must produce exactly one batch: 15 queries at both page and
section levels.

| Batch | Split | IDs | Count |
|---|---|---|---:|
| B01 | book | V4-B001–V4-B015 | 15 |
| B02 | book | V4-B016–V4-B030 | 15 |
| B03 | book | V4-B031–V4-B045 | 15 |
| B04 | book | V4-B046–V4-B060 | 15 |
| B05 | book | V4-B061–V4-B075 | 15 |
| B06 | book | V4-B076–V4-B090 | 15 |
| A01 | atlas | V4-A001–V4-A015 | 15 |
| A02 | atlas | V4-A016–V4-A030 | 15 |
| V01 | v12 | V4-V001–V4-V015 | 15 |
| V02 | v12 | V4-V016–V4-V030 | 15 |

Output per batch:

- `evaluation/qrels-v4/batches/<batch>.page.json`
- `evaluation/qrels-v4/batches/<batch>.section.json`

Validate one batch:

```sh
python3 scripts/validate_qrels_v4.py \
  --page evaluation/qrels-v4/batches/B01.page.json \
  --section evaluation/qrels-v4/batches/B01.section.json \
  --book 15 --atlas 0 --v12 0
```

For A batches: `--book 0 --atlas 15 --v12 0`.
For V batches: `--book 0 --atlas 0 --v12 15`.

After all ten batches:

```sh
python3 scripts/merge_qrels_v4_batches.py \
  --batch-dir evaluation/qrels-v4/batches
```
