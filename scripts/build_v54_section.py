#!/usr/bin/env python3
"""Build v5.4 section qrels from section top-1 audit."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--root",type=Path,default=ROOT); args=ap.parse_args(argv); root=args.root
 base=json.loads((root/"evaluation/section-qrels.v5-dense.json").read_text()); target={i["id"]:dict(i) for i in base["items"]}
 third={}
 for f in (root/"evaluation/hard-negatives-section-v5").glob("adjudication*.json"):
  for i in json.loads(f.read_text())["items"]: third[(i["id"],i["section_key"])]=int(i["grade"])
 added=0
 for n in range(1,16):
  b="SN%02d"%n
  c=json.loads((root/"evaluation/hard-negatives-section-v5/batches"/(b+".candidates.json")).read_text())
  a=json.loads((root/"evaluation/hard-negatives-section-v5/labels"/(b+"-A.json")).read_text())
  bb=json.loads((root/"evaluation/hard-negatives-section-v5/labels"/(b+"-B.json")).read_text())
  am={i["id"]:i for i in a["items"]}; bm={i["id"]:i for i in bb["items"]}
  for it in c["items"]:
   q=it["id"]
   for e in it["section_new"]:
    k=e["section_key"]; x=am[q].get("section_grades",{}).get(k); y=bm[q].get("section_grades",{}).get(k)
    if x is None or y is None: continue
    g=int(x) if x==y else third[(q,k)]
    target[q]["grades"][k]=g; added+=1
 for it in target.values():
  it["accepted"]=sorted(k for k,v in it["grades"].items() if v>=1); it["direct"]=sorted(k for k,v in it["grades"].items() if v==2)
 out=dict(base); out.update({"status":"ai-adjudicated-not-human","base":"qrels v5-dense","query_count":150,"items":sorted(target.values(),key=lambda i:i["id"]),"limits":"v5.4 section adds one audited section per query; not comparable to v5; AI-only."})
 (root/"evaluation/section-qrels.v5.4.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"added":added},indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
