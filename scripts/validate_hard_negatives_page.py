#!/usr/bin/env python3
"""Validate one page hard-negative batch."""
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch",required=True)
    ap.add_argument("--labeler",required=True)
    ap.add_argument("--labels",type=Path,required=True)
    ap.add_argument("--root",type=Path,default=ROOT)
    args=ap.parse_args(argv)
    c=json.loads((args.root/"evaluation/hard-negatives-page-v5/batches"/(args.batch+".candidates.json")).read_text())
    l=json.loads(args.labels.read_text())
    errors=[]
    if l.get("batch")!=args.batch or l.get("labeler")!=args.labeler: errors.append("batch/labeler")
    if l.get("status")!="ai-adjudicated-not-human": errors.append("status")
    exp={i["id"]:{x["path"] for x in i["page_new"]} for i in c["items"]}
    got={i["id"]:set(i.get("page_grades",{})) for i in l.get("items",[])}
    if set(exp)!=set(got): errors.append("query set")
    for qid,keys in exp.items():
        if keys!=got.get(qid,set()): errors.append(qid+": key set")
        for v in l.get("items",[]):
            if v["id"]==qid:
                for g in v.get("page_grades",{}).values():
                    if g not in (0,1,2): errors.append(qid+": grade")
    if errors:
        print("FAIL"); [print("-",e) for e in errors[:10]]; return 1
    print("PASS: page hard-negative labels are complete"); return 0

if __name__=="__main__": raise SystemExit(main())
