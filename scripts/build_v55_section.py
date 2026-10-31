#!/usr/bin/env python3
"""Build v5.5 section qrels from full section top-5 audit."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--root",type=Path,default=ROOT); args=ap.parse_args(argv); root=args.root
 base=json.loads((root/"evaluation/section-qrels.v5-dense.json").read_text()); target={i["id"]:dict(i) for i in base["items"]}
 A={};B={}
 for f in (root/"evaluation/hard-negatives-section-v5/labels").glob("*.json"):
  if not (f.stem.startswith(("SN","SR")) and f.stem.endswith(("-A","-B"))): continue
  lab=f.stem[-1]; d=json.loads(f.read_text())
  for it in d["items"]:
   for k,v in it.get("section_grades",{}).items(): (A if lab=="A" else B)[(it["id"],k)]=int(v)
 third={}
 for f in (root/"evaluation/hard-negatives-section-v5").glob("adjudication-top5-*.json"):
  for i in json.loads(f.read_text())["items"]: third[(i["id"],i["section_key"])]=int(i["grade"])
 added=0; missing=set()
 for key,x in A.items():
  y=B.get(key)
  if y is None: continue
  if x==y: g=x
  elif key in third: g=third[key]
  else: missing.add(key); continue
  target[key[0]]["grades"][key[1]]=g; added+=1
 if missing: raise SystemExit("missing third: %d"%len(missing))
 for it in target.values():
  it["accepted"]=sorted(k for k,v in it["grades"].items() if v>=1); it["direct"]=sorted(k for k,v in it["grades"].items() if v==2)
 out=dict(base); out.update({"status":"ai-adjudicated-not-human","base":"qrels v5-dense","query_count":150,"items":sorted(target.values(),key=lambda i:i["id"]),"limits":"v5.5 section adds top-5 audited sections; not comparable to v5; AI-only."})
 (root/"evaluation/section-qrels.v5.5.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"added":added},indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
