import json, pathlib, re, hashlib, sys
ROOT=pathlib.Path('.')
V12=ROOT/'edition/v12'
route=json.loads((ROOT/'generated/route-index.v1.json').read_text())
registry=json.loads((V12/'registry.json').read_text())
patterns=json.loads((ROOT/'edition/patterns/registry.v1.json').read_text())['patterns']
pattern_by_id={p['id']:p for p in patterns}

def tokenize(text):
    return set(re.findall(r'[a-z0-9]+', text.lower()))

# page -> pattern ids from registry artifacts
page_patterns={}
for collection in registry['artifacts'].values():
    for art in collection:
        page_patterns.setdefault(art['page_path'], set()).update(art.get('pattern_ids', []))

documents=[]
for d in route['documents']:
    if not d['path'].startswith('book/volumes/v12-modeling-simulation-and-decision-validation/'):
        continue
    documents.append({
        'id': d['id'], 'path': d['path'], 'title': d['title'], 'kind': d['kind'],
        'artifact_type': 'document', 'volume': 'v12',
        'pattern_ids': sorted(page_patterns.get(d['path'], [])),
        'evidence_status': d['evidence_status'],
        'summary': d['summary'], 'questions': d['questions'], 'keywords': d['keywords'],
        'topics': d['topics'],
    })
page_by_path={d['path']:d for d in route['documents']}
for collection in registry['artifacts'].values():
    for art in collection:
        page=page_by_path.get(art.get('page_path',''), {})
        documents.append({
            'id': art['id'], 'path': art['path'], 'title': page.get('title', art['id']),
            'kind': 'artifact', 'artifact_type': art['artifact_type'], 'volume': 'v12',
            'pattern_ids': sorted(art.get('pattern_ids', [])),
            'evidence_status': art.get('evidence_status'),
            'summary': page.get('summary',''), 'questions': page.get('questions',[]),
            'keywords': page.get('keywords',[]), 'topics': page.get('topics',[]),
        })
documents.sort(key=lambda d: (d['artifact_type'], d['id']))

pattern_catalog={pid: {'name': p['catalog_name'], 'owner_page': p['technical_owner']['path']}
                 for pid,p in pattern_by_id.items()}

index={
 'schema_version':1,
 'volume':'v12',
 'generated_from':['generated/route-index.v1.json','edition/v12/registry.json','edition/patterns/registry.v1.json'],
 'documents':documents,
 'reverse_index':registry['reverse_index'],
 'pattern_catalog':pattern_catalog,
 'ranking_policy':'Canonical pattern owner pages rank first for pattern queries. V12 documents rank for modeling, simulation and decision queries. No existing corpus document is re-embedded or rewritten.',
 'scope':'Derived V12 retrieval namespace and reverse lookup. Not a semantic graph, not a source of claim truth.'
}

def query(text, limit=5, artifact_type=None):
    terms=tokenize(text)
    canonical=[]
    for pid,name in pattern_by_id.items():
        if name['catalog_name'].lower() in text.lower():
            canonical.append({'id':name['technical_owner']['document_id'],
                              'path':name['technical_owner']['path'],
                              'title':name['catalog_name'],'kind':'pattern-owner',
                              'artifact_type':'pattern','score':100,'reason':'canonical pattern owner'})
    scored=[]
    for d in documents:
        if artifact_type and d['artifact_type']!=artifact_type: continue
        blob=' '.join([d['title'],d.get('summary',''),' '.join(d.get('questions',[])),
                       ' '.join(d.get('keywords',[])),' '.join(d.get('topics',[])),
                       ' '.join(d.get('pattern_ids',[]))]).lower()
        score=sum(3 for t in terms if t in blob)
        if score: scored.append((score,d))
    scored.sort(key=lambda x:(-x[0],x[1]['id']))
    results=canonical[:limit]
    for score,d in scored:
        if len(results)>=limit: break
        if any(r['id']==d['id'] for r in results): continue
        results.append({'id':d['id'],'path':d['path'],'title':d['title'],
                        'kind':d['kind'],'artifact_type':d['artifact_type'],
                        'score':score,'reason':'V12 facet match'})
    return {'query':text,'returned':len(results),'results':results,
            'policy':'Canonical pattern owners first; V12 artifacts for modeling queries.'}

def render_reverse():
    reverse={'schema_version':1,'volume':'v12','patterns':index['reverse_index'],
             'scope':'Derived pattern-to-artifact lookup. It is regenerated from V12 records and never written back to existing cards or owner pages.'}
    return json.dumps(reverse,indent=2,ensure_ascii=False)+chr(10)

def render():
    return json.dumps(index,indent=2,ensure_ascii=False)+chr(10)

if __name__=='__main__':
    target=ROOT/'generated/v12-index.v1.json'
    reverse_target=ROOT/'edition/v12/reverse-index.v1.json'
    content=render(); reverse_content=render_reverse()
    if '--check' in sys.argv:
        if not target.is_file() or target.read_text()!=content:
            raise SystemExit('V12 index is stale; run python3 scripts/build_v12_index.py')
        if not reverse_target.is_file() or reverse_target.read_text()!=reverse_content:
            raise SystemExit('V12 reverse index is stale; run python3 scripts/build_v12_index.py')
        print('V12 index and reverse index match derived artifacts')
    else:
        target.write_text(content); reverse_target.write_text(reverse_content)
        print('Built',len(documents),'V12 index documents; reverse patterns',len(index['reverse_index']))
