#!/usr/bin/env python3
"""Fine-tune a domain bi-encoder on v2 query/positive-section pairs."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_search


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))["items"]


def accepted_paths(item):
    return {a["path"] if isinstance(a, dict) else a
            for a in item.get("accepted", [])}


def positive_text(root, item):
    rows = section_search.search(
        root, item["question"], limit=20, abstain=False)["results"]
    accepted = accepted_paths(item)
    for row in rows:
        if row["path"] in accepted:
            return " ".join(str(row.get(k, ""))
                            for k in ("title", "heading", "content"))[:4000]
    target = Path(root) / "generated/sections-fts-v5.sqlite"
    for path in accepted:
        with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                             uri=True) as db:
            row = db.execute(
                "select title,heading,content from sections"
                " where path=? and heading_level=2 limit 1", (path,)).fetchone()
        if row:
            return " ".join(str(x) for x in row)[:4000]
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--output", type=Path,
                        default=Path.home() / ".cache/tycho/domain-minilm-v1")
    args = parser.parse_args(argv)
    from sentence_transformers import InputExample, SentenceTransformer, losses
    from torch.utils.data import DataLoader

    examples = []
    for item in load(args.root / "evaluation/corpus-qrels.v2.json"):
        text = positive_text(args.root, item)
        if text:
            examples.append(InputExample(texts=[item["question"], text]))
    print(json.dumps({"training_pairs": len(examples)}))
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    loader = DataLoader(examples, shuffle=True, batch_size=args.batch)
    loss = losses.MultipleNegativesRankingLoss(model)
    model.fit(train_objectives=[(loader, loss)], epochs=args.epochs,
              warmup_steps=10, output_path=str(args.output),
              show_progress_bar=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
