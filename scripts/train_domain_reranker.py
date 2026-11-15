#!/usr/bin/env python3
"""Train a domain cross-encoder on v2 qrels and evaluate on v5-dense."""
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


def sections_for(root, path):
    target = Path(root) / "generated/sections-fts-v5.sqlite"
    with sqlite3.connect("file:" + target.resolve().as_posix() + "?mode=ro",
                         uri=True) as db:
        rows = db.execute(
            "select title,heading,content from sections"
            " where path=? and heading_level=2 limit 3", (path,)).fetchall()
    return [" ".join(str(x) for x in row)[:4000] for row in rows]


def pairs(root, items):
    out = []
    for item in items:
        rows = section_search.search(
            root, item["question"], limit=20, abstain=False)["results"]
        accepted = accepted_paths(item)
        positives = [row for row in rows if row["path"] in accepted]
        if not positives:
            for path in accepted:
                text = sections_for(root, path)[:1]
                if text:
                    out.append((item["question"], text[0], 1.0))
                    break
        else:
            out.append((item["question"],
                        " ".join(str(positives[0].get(k, ""))
                                for k in ("title", "heading", "content"))[:4000],
                        1.0))
        negatives = [row for row in rows if row["path"] not in accepted][:3]
        for row in negatives:
            text = " ".join(str(row.get(k, ""))
                            for k in ("title", "heading", "content"))[:4000]
            out.append((item["question"], text, 0.0))
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--epochs", type=int, default=2)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--output", type=Path,
                        default=Path.home() / ".cache/tycho/domain-reranker-v1")
    args = parser.parse_args(argv)
    import torch
    from sentence_transformers import CrossEncoder

    train = pairs(args.root, load(args.root / "evaluation/corpus-qrels.v2.json"))
    print(json.dumps({"training_pairs": len(train)}))
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    optimizer = torch.optim.AdamW(model.model.parameters(), lr=2e-5)
    loss_fn = torch.nn.BCEWithLogitsLoss()
    for epoch in range(args.epochs):
        model.model.train()
        order = torch.randperm(len(train)).tolist()
        for start in range(0, len(order), args.batch):
            batch = [train[i] for i in order[start:start + args.batch]]
            encoded = model.tokenizer(
                [x[0] for x in batch], [x[1] for x in batch],
                padding=True, truncation=True, max_length=512,
                return_tensors="pt")
            device = model.model.device
            encoded = {key: value.to(device) for key, value in encoded.items()}
            labels = torch.tensor([x[2] for x in batch], dtype=torch.float).to(device)
            optimizer.zero_grad()
            logits = model.model(**encoded).logits.squeeze(-1)
            loss = loss_fn(logits, labels)
            loss.backward()
            optimizer.step()
        print(json.dumps({"epoch": epoch + 1, "loss": round(float(loss), 4)}))
    args.output.mkdir(parents=True, exist_ok=True)
    model.save(str(args.output))
    page = load(args.root / "evaluation/corpus-qrels.v5-dense.json")
    section = {x["id"]: set(x["accepted"])
               for x in load(args.root / "evaluation/section-qrels.v5-dense.json")}
    values = []
    for item in page:
        rows = section_search.search(
            args.root, item["question"], limit=20, abstain=False)["results"]
        texts = [" ".join(str(row.get(k, ""))
                          for k in ("title", "heading", "content"))[:4000]
                 for row in rows]
        scores = model.predict([(item["question"], text) for text in texts],
                               show_progress_bar=False)
        order = sorted(range(len(rows)),
                       key=lambda i: (-float(scores[i]),
                                      rows[i]["section_key"]))
        page_rank = section_rank = None
        for rank, index in enumerate(order, 1):
            row = rows[index]
            if page_rank is None and row["path"] in accepted_paths(item):
                page_rank = rank
            if section_rank is None and row["section_key"] in section[item["id"]]:
                section_rank = rank
            if page_rank and section_rank:
                break
        values.append((page_rank, section_rank))
    n = len(values)
    result = {
        "page": {k: round(sum(1 for p, s in values if p and p <= k) / n, 3)
                 for k in (1, 3, 5)},
        "section": {k: round(sum(1 for p, s in values if s and s <= k) / n, 3)
                    for k in (1, 3, 5)},
        "mrr_page": round(sum(1 / p for p, s in values if p) / n, 3),
        "mrr_section": round(sum(1 / s for p, s in values if s) / n, 3),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
