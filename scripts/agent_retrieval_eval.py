#!/usr/bin/env python3
"""Bounded retrieval audit for external-agent use."""
import argparse, json, random, statistics, time
from pathlib import Path
import section_search

ROOT = Path(__file__).resolve().parents[1]
OFFTOPIC = [
    "How do I bake sourdough bread at home?",
    "What is the best fertilizer for tomato plants?",
    "How do I change a bicycle tire?",
    "What causes earthquakes?",
    "How do I learn to play the piano?",
    "What is the capital of Australia?",
    "How do I train for a marathon?",
    "What is photosynthesis?",
    "How do I fix a leaking kitchen faucet?",
    "What is the history of the printing press?",
    "How do I make a good espresso?",
    "What is the best way to learn a language?",
    "How do I grow basil indoors?",
    "What is the water cycle?",
    "How do I tune a guitar?",
    "What is a healthy breakfast?",
    "How do I clean a cast iron pan?",
    "What causes the northern lights?",
    "How do I sew a button?",
    "What is the best way to store coffee?",
]

def pct(values, p):
    values = sorted(values)
    return values[min(len(values)-1, int(len(values)*p))]

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--abstain", action="store_true")
    ap.add_argument("--all-sections", action="store_true")
    ap.add_argument("--out", type=Path, default=ROOT/"evaluation/agent-retrieval-v5/agent-eval.json")
    args = ap.parse_args(argv)
    page_q = json.loads((args.root/"evaluation/corpus-qrels.v5.3-page.json").read_text())
    sec_q = json.loads((args.root/"evaluation/section-qrels.v5.5.json").read_text())
    sec = {i["id"]: i for i in sec_q["items"]}
    page = {i["id"]: i for i in page_q["items"]}
    rng = random.Random(17)
    by_split = {"book": [], "atlas": [], "v12": []}
    for item in page_q["items"]:
        by_split[item["split"]].append(item["id"])
    sample = (rng.sample(by_split["book"], 50) + rng.sample(by_split["atlas"], 25)
              + rng.sample(by_split["v12"], 25))
    rows = []
    for qid in sample:
        item = next(i for i in page_q["items"] if i["id"] == qid)
        t0 = time.perf_counter()
        r = section_search.search(args.root, item["question"], limit=args.limit,
                                  abstain=args.abstain, all_sections=args.all_sections)
        latency = (time.perf_counter()-t0)*1000
        res = r.get("results", [])
        keys = [x["section_key"] for x in res]
        paths = [x["path"] for x in res]
        sec_acc = set(sec[qid]["accepted"])
        page_acc = set(page[qid]["accepted"])
        sec_hit = len(set(keys) & sec_acc)
        page_hit = len(set(paths) & page_acc)
        chars = sum(len(x.get("excerpt","")) for x in res)
        rows.append({
            "id": qid, "split": item["split"], "question": item["question"],
            "returned": len(res), "section_hit": sec_hit,
            "section_accepted": len(sec_acc), "page_hit": page_hit,
            "page_accepted": len(page_acc),
            "section_recall": round(sec_hit/len(sec_acc),4) if sec_acc else 0.0,
            "page_recall": round(page_hit/len(page_acc),4) if page_acc else 0.0,
            "citation_precision": round(sec_hit/len(res),4) if res else 0.0,
            "unique_paths": len(set(paths)), "unique_volumes": len({x.get("volume") for x in res if x.get("volume")}),
            "excerpt_bytes": chars, "approx_tokens": round(chars/4),
            "latency_ms": round(latency,3),
            "abstained": bool(r.get("answerability",{}).get("no_confident_answer")),
            "snapshot": r.get("snapshot"), "ranker": r.get("ranker_version"),
        })
    # abstention probes
    probes = []
    for q in OFFTOPIC:
        r = section_search.search(args.root, q, limit=5, abstain=args.abstain)
        a = r.get("answerability", {})
        probes.append({"question": q, "no_confident_answer": bool(a.get("no_confident_answer")),
                       "answerable": a.get("answerable"), "state": a.get("state"),
                       "returned": len(r.get("results", []))})
    metrics = {
        "tasks": len(rows),
        "section_recall@k": round(sum(x["section_recall"] for x in rows)/len(rows),4),
        "page_recall@k": round(sum(x["page_recall"] for x in rows)/len(rows),4),
        "citation_precision@k": round(sum(x["citation_precision"] for x in rows)/len(rows),4),
        "mean_unique_paths": round(statistics.mean(x["unique_paths"] for x in rows),3),
        "mean_unique_paths_nonempty": round(statistics.mean(x["unique_paths"] for x in rows if x["returned"]),3),
        "mean_unique_volumes_nonempty": round(statistics.mean(x["unique_volumes"] for x in rows if x["returned"]),3),
        "zero_result_tasks": sum(x["returned"] == 0 for x in rows),
        "answerable_zero_result_tasks": sum(x["returned"] == 0 for x in rows if x["page_accepted"]),
        "mean_approx_tokens": round(statistics.mean(x["approx_tokens"] for x in rows),1),
        "latency_p50_ms": round(pct([x["latency_ms"] for x in rows], .5),2),
        "latency_p95_ms": round(pct([x["latency_ms"] for x in rows], .95),2),
        "abstention_probes": len(probes),
        "abstention_rate": round(sum(p["no_confident_answer"] for p in probes)/len(probes),4),
        "answerability_note": "off-topic abstention probes only; not answer correctness",
    }
    out = {"status":"ai-adjudicated-not-human","mode":("abstain" if args.abstain else "return-candidates") + ("+all-sections" if args.all_sections else ""),"snapshot":rows[0]["snapshot"] if rows else None,
           "ranker":rows[0]["ranker"] if rows else None,"limit":args.limit,
           "metrics":metrics,"rows":rows,"abstention_probes":probes,
           "limits":("Retrieval-only; no answer support or citation correctness by a reader. "
                     "Latency includes cache effects. AI labels only.")}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(metrics,indent=2)); return 0

if __name__=="__main__":
    raise SystemExit(main())
