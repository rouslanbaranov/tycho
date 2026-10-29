import json,math,random,sys
from pathlib import Path
sys.path.insert(0,'scripts')
import section_search
ROOT=Path('.')
q=json.load(open('evaluation/section-qrels.v3.json'))
rows=[]
for i in q['items']:
 a=set(i['accepted'])
 b=section_search.search(ROOT,i['question'],limit=5,abstain=False,section_rerank=False)
 try:
  r=section_search.search(ROOT,i['question'],limit=5,abstain=False,section_rerank=True)
 except section_search.SearchError:
  r=b
 bp=[x['section_key'] for x in b.get('results',[])]
 rp=[x['section_key'] for x in r.get('results',[])]
 rows.append((bool(set(bp[:1])&a),bool(set(rp[:1])&a)))
n=len(rows); b=sum(x[0] for x in rows); r=sum(x[1] for x in rows)
b01=sum(1 for x in rows if not x[0] and x[1]); b10=sum(1 for x in rows if x[0] and not x[1])
def pval(a,c):
 nn=a+c
 if not nn:return 1.0
 tail=sum(math.comb(nn,k) for k in range(0,min(a,c)+1))
 return min(1.0,2*tail/(2**nn))
rng=random.Random(20261029); diffs=[]
for _ in range(5000):
 s=[rows[rng.randrange(n)] for _ in range(n)]
 diffs.append(sum(x[1] for x in s)/n-sum(x[0] for x in s)/n)
diffs.sort()
print(json.dumps({'n':n,'base':round(b/n,4),'rerank':round(r/n,4),'diff':round((r-b)/n,4),'ci95':[round(diffs[125],4),round(diffs[4874],4)],'b01':b01,'b10':b10,'p':round(pval(b01,b10),6)}))
