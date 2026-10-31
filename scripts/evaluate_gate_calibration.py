#!/usr/bin/env python3
"""Calibration audit for the agent answerability gate."""
import argparse, json, random
from pathlib import Path
import numpy as np
import section_search

ROOT = Path(__file__).resolve().parents[1]
OFFTOPIC = [
    "How do I bake sourdough bread at home?", "What is the best fertilizer for tomato plants?",
    "How do I change a bicycle tire?", "What causes earthquakes?",
    "How do I learn to play the piano?", "What is the capital of Australia?",
    "How do I train for a marathon?", "What is photosynthesis?",
    "How do I fix a leaking kitchen faucet?", "What is the history of the printing press?",
    "How do I make a good espresso?", "What is the best way to learn a language?",
    "How do I grow basil indoors?", "What is the water cycle?",
    "How do I tune a guitar?", "What is a healthy breakfast?",
    "How do I clean a cast iron pan?", "What causes the northern lights?",
    "How do I sew a button?", "What is the best way to store coffee?",
]

def auc(pos, neg):
    pos = np.asarray(pos); neg = np.asarray(neg)
    return float((np.sum(pos[:,None] > neg[None,:]) + .5*np.sum(pos[:,None] == neg[None,:]))/(len(pos)*len(neg)))

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--root",type=Path,default=ROOT); args=ap.parse_args(argv)
    page=json.loads((args.root/"evaluation/corpus-qrels.v5.3-page.json").read_text())
    rng=random.Random(17); by={"book":[],"atlas":[],"v12":[]}
    for i in page["items"]: by[i["split"]].append(i["id"])
    sample=rng.sample(by["book"],50)+rng.sample(by["atlas"],25)+rng.sample(by["v12"],25)
    qmap={i["id"]:i for i in page["items"]}; ans=[]
    for qid in sample:
        r=section_search.search(args.root,qmap[qid]["question"],limit=5,abstain=False)
        f=r["answerability"].get("features",{})
        ans.append({"id":qid,"current_abstain":bool(r["answerability"].get("no_confident_answer")),
                    "score":f.get("score"),"coverage":f.get("coverage"),
                    "margin":f.get("margin"),"prob":r["answerability"].get("probability_unanswerable")})
    off=[]
    for q in OFFTOPIC:
        r=section_search.search(args.root,q,limit=5,abstain=False)
        f=r["answerability"].get("features",{})
        off.append({"question":q,"current_abstain":bool(r["answerability"].get("no_confident_answer")),
                    "score":f.get("score"),"coverage":f.get("coverage"),
                    "margin":f.get("margin"),"prob":r["answerability"].get("probability_unanswerable")})
    features=[("score","high"),("coverage","high"),("margin","high"),("prob","low")]
    sweep={}
    for name,direction in features:
        pos=[x[name] for x in ans if x[name] is not None]; neg=[x[name] for x in off if x[name] is not None]
        vals=sorted(set(pos+neg)); best=None
        for t in vals:
            if direction=="high":
                tp=sum(v>=t for v in pos)/len(pos); fp=sum(v>=t for v in neg)/len(neg)
            else:
                tp=sum(v<=t for v in pos)/len(pos); fp=sum(v<=t for v in neg)/len(neg)
            # accept answerable = tp; reject off-topic = 1-fp
            score=tp+(1-fp)-1
            cand={"threshold":t,"accept_answerable":round(tp,3),"false_abstention":round(1-tp,3),
                  "reject_offtopic":round(1-fp,3),"youden":round(score,3)}
            if best is None or score>best["youden"]: best=cand
        sweep[name]={"auc_accept_answerable":round(auc(pos,neg),4),"best":best,
                     "current":{"answerable_abstain":sum(x["current_abstain"] for x in ans),
                                "offtopic_abstain":sum(x["current_abstain"] for x in off)}}
    out={"status":"ai-adjudicated-not-human","answerable":len(ans),"offtopic":len(off),
         "sweep":sweep,"answerable_rows":ans,"offtopic_rows":off,
         "limits":"in-sample threshold sweep; AI labels; not a fitted production gate."}
    (args.root/"evaluation/agent-retrieval-v5/gate-calibration.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(sweep,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
