#!/usr/bin/env python3
"""Validate one section hard-negative batch."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--batch",required=True); ap.add_argument("--labeler",required=True); ap.add_argument("--labels",type=Path,required=True); ap.add_argument("--root",type=Path,default=ROOT); args=ap.parse_args(argv)
 c=json.loads((args.root/"evaluation/hard-negatives-section-v5/batches"/(args.batch+".candidates.json")).read_text()); l=json.loads(args.labels.read_text())
 errors=[]
 if l.get("batch")!=args.batch or l.get("labeler")!=args.labeler: errors.append("batch/labeler")
 if l.get("status")!="ai-adjudicated-not-human": errors.append("status")
 exp={i["id"]:{x["section_key"] for x in i["section_new"]} for i in c["items"]}; got={i["id"]:set(i.get("section_grades",{})) for i in l.get("items",[])}
 if set(exp)!=set(got): errors.append("query set")
 for q,keys in exp.items():
  if keys!=got.get(q,set()): errors.append(q+": keys")
  for i in l.get("items",[]):
   if i["id"]==q:
    for g in i.get("section_grades",{}).values():
     if g not in (0,1,2): errors.append(q+": grade")
 if errors:
  print("FAIL"); [print("-",e) for e in errors[:10]]; return 1
 print("PASS: section hard-negative labels are complete"); return 0
if __name__=="__main__": raise SystemExit(main())
