#!/usr/bin/env python3
"""Build v5.3 page qrels from full top-5 page audit."""
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root",type=Path,default=ROOT)
    args=ap.parse_args(argv); root=args.root
    page=json.loads((root/"evaluation/corpus-qrels.v5-dense.json").read_text())
    target={i["id"]:dict(i) for i in page["items"]}
    a={}; b={}
    for f in (root/"evaluation/hard-negatives-page-v5/labels").glob("*.json"):
        if not (f.stem.startswith(("PG","RB")) and f.stem.endswith(("-A","-B"))): continue
        lab=f.stem[-1]; d=json.loads(f.read_text())
        for it in d["items"]:
            for k,v in it.get("page_grades",{}).items():
                (a if lab=="A" else b)[(it["id"],k)]=int(v)
    third={}
    for f in (root/"evaluation/hard-negatives-page-v5").glob("adjudication-third-*.json"):
        for it in json.loads(f.read_text())["items"]:
            third[(it["id"],it["path"])]=int(it["grade"])
    added=0; missing=set()
    for key,x in a.items():
        y=b.get(key)
        if y is None: continue
        if x==y: grade=x
        elif key in third: grade=third[key]
        else: missing.add(key); continue
        target[key[0]]["grades"][key[1]]=grade; added+=1
    if missing:
        raise SystemExit("missing third labels: %d" % len(missing))
    for item in target.values():
        item["accepted"]=sorted(k for k,v in item["grades"].items() if v>=1)
        item["direct"]=sorted(k for k,v in item["grades"].items() if v==2)
    out=dict(page); out.update({"status":"ai-adjudicated-not-human",
        "base":"qrels v5-dense","query_count":150,
        "items":sorted(target.values(),key=lambda i:i["id"]),
        "limits":("v5.3 page adds all top-5 audited pages; not comparable "
                  "to v5; AI-only.")})
    (root/"evaluation/corpus-qrels.v5.3-page.json").write_text(
        json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"added":added},indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
