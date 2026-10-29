import json,sys
from pathlib import Path
sys.path.insert(0,'scripts')
import section_search
ROOT=Path('.')
weights=",".join(f"{v:g}" for v in section_search.bm25_weights())
q=json.load(open('evaluation/section-qrels.v3.json'))
db,_=section_search.open_snapshot(ROOT)
rows=[]
for i in q['items']:
 a=set(i['accepted'])
 base=section_search.search(ROOT,i['question'],limit=5,abstain=False,section_rerank=False)
 pages=[(x['path'],x['section_key']) for x in base.get('results',[])]
 terms=section_search.normalize_terms(i['question']); expr=section_search.match_expression(terms)
 chosen=[]
 for page,base_key in pages:
  sql=("SELECT s.section_key,s.section_id,s.heading,s.content,bm25(fts,0.0,"+weights+") AS rank FROM fts JOIN sections s ON s.section_key=fts.section_key WHERE fts MATCH ? AND s.path=? ORDER BY rank LIMIT 100")
  rs=db.execute(sql,[expr,page]).fetchall()
  if not rs: chosen.append((page,base_key)); continue
  def feat(r):
   text=(r['heading']+' '+r['content']).casefold()
   return (sum(1 for t in set(terms) if t in text),sum(1 for t in set(terms) if t in r['heading'].casefold()),-r['rank'])
  best=max(rs,key=feat); chosen.append((page,best['section_key']))
 bp=[k for p,k in pages]
 ck=[k for p,k in chosen]
 rows.append(([bool(set(bp[:k])&a) for k in (1,3,5)],[bool(set(ck[:k])&a) for k in (1,3,5)]))
db.close(); n=len(rows)
for name,idx in [('base_section',0),('page_preserving_section',1)]:
 print(name,[round(sum(r[idx][j] for r in rows)/n,3) for j in range(3)])
