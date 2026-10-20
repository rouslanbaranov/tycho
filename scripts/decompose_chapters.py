#!/usr/bin/env python3
"""Apply reviewed, chapter-specific question boundaries; default is dry-run.

No automatic heading quota, source acquisition or acceptance promotion.
Input prose/additions and new IDs are explicit in the decomposition plan.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit

from assemble_edition import split, sha, MARKER, rel
from frontmatter_generate import render
from validate_book_navigation import slug_heading

ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'(!?\[[^\]\n]*\]\()([^\s)]+)([^)\n]*\))')
BLOCK_START=re.compile(r'^<!-- tycho-question-source:([^:]+):(-?\d+) -->$')
BLOCK_END='<!-- /tycho-question-source -->'


def source_sections(body):
    """Keep every original byte; recognize headings only outside code fences."""
    starts=[];offset=0;fence=None
    for line in body.splitlines(keepends=True):
        m=re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)',line)
        if m:
            marker=m.group(1)
            if fence is None:fence=(marker[0],len(marker))
            elif marker[0]==fence[0] and len(marker)>=fence[1] and not m.group(2).strip():fence=None
        elif fence is None and line.startswith('## '):
            starts.append(offset)
        offset+=len(line)
    boundaries=starts+[len(body)]
    result={-1:body[:starts[0]] if starts else body}
    result.update({i:body[a:boundaries[i+1]] for i,a in enumerate(starts)})
    return result


def headings(text):
    """Yield source heading labels using the navigation validator's convention."""
    fence=None
    for line in text.splitlines():
        m=re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)',line)
        if m:
            marker=m.group(1)
            if fence is None:fence=(marker[0],len(marker))
            elif marker[0]==fence[0] and len(marker)>=fence[1] and not m.group(2).strip():fence=None
        elif fence is None:
            h=re.match(r'^\s{0,3}(#{1,6})\s+(.+?)\s*$',line)
            if h:yield h.group(2)


def route_link(raw,source,routes):
    u=urlsplit(raw)
    if u.scheme or u.netloc or raw.startswith('/'):return None
    dest=posixpath.normpath(posixpath.join(posixpath.dirname(source),unquote(u.path))) if u.path else source
    fragment=unquote(u.fragment)
    dest,fragment=routes.get((dest,fragment),(dest,fragment))
    return dest,fragment,u.query


def rebase(text,source,dest,routes):
    def change(m):
        target=route_link(m.group(2),source,routes)
        if target is None:return m.group(0)
        path,fragment,query=target
        value=('#'+fragment if path==dest and fragment and not query else rel(dest,path)+('?' +query if query else '')+('#'+fragment if fragment else ''))
        return m.group(1)+value+m.group(3)
    return LINK.sub(change,text)


def normalized(text,source,routes):
    def change(m):
        target=route_link(m.group(2),source,routes)
        if target is None:return m.group(0)
        path,fragment,query=target
        return m.group(1)+'tycho-local:'+path+('?' +query if query else '')+('#'+fragment if fragment else '')+m.group(3)
    return LINK.sub(change,text)


def wrap(identity,index,body):
    return '<!-- tycho-question-source:'+identity+':'+str(index)+' -->\n'+body+BLOCK_END+'\n'


def extract_blocks(text):
    result={};active=None;lines=[]
    for line in text.splitlines(keepends=True):
        m=BLOCK_START.match(line.rstrip('\n'))
        if m:
            if active is not None:raise ValueError('nested source block')
            active=(m.group(1),int(m.group(2)));lines=[]
        elif line.rstrip('\n')==BLOCK_END:
            if active is None or active in result:raise ValueError('invalid or duplicate source block')
            result[active]=''.join(lines);active=None
        elif active is not None:lines.append(line)
    if active is not None:raise ValueError('unclosed source block')
    return result


def apply(root=ROOT,write=False):
    root=Path(root)
    plan=json.loads((root/'edition/decomposition-plan.json').read_text())
    outline=json.loads((root/'edition/outline.json').read_text())
    if (root/'edition/decomposition-manifest.json').exists():raise ValueError('Decomposition already applied')
    owners={c['code']:c for c in outline['chapters']}
    files={};originals={};block_targets={};old_anchors={};records=[];new_metadata={}
    for c in plan['chapters']:
        owner=owners[c['code']]
        source=c['source_page']
        meta,body=split((root/source).read_text())
        body=body.split(MARKER)[0]
        sections=source_sections(body);originals[source]=(meta,body,sections)
        selected={}
        for page in c['pages']:
            for i in page['section_indices']:
                if i not in sections or i in selected:raise ValueError('Invalid/duplicate section in '+c['code'])
                selected[i]=page['path']
        # Source ledgers/old navigation are now chapter-owned shared evidence.
        # Applied cases and integrated walkthroughs remain in the original page.
        ledger=[]
        for i,text in sections.items():
            h=text.splitlines()[0].removeprefix('## ').lower() if i>=0 else ''
            if i not in selected and i>=0 and not h.startswith('applied') and re.search(r'(source|ledger|public|evidence|review|navigation|verification checklist)',h):
                ledger.append(i)
        for i in sections:
            block_targets[(meta['id'],i)]=selected.get(i,c['chapter_path'] if i in ledger else source)
        count=Counter()
        for i,text in sections.items():
            anchors=[]
            for label in headings(text):
                slug=slug_heading(label);n=count[slug];count[slug]+=1
                anchors.append(slug if not n else slug+'-'+str(n))
            old_anchors[(meta['id'],i)]=anchors
        inherited_meta=copy.deepcopy(meta)
        inherited_meta['route_hints']['questions']=[owner['question']]
        inherited_meta['route_hints']['related_ids']=list(dict.fromkeys(meta['route_hints']['related_ids']+[p['id'] for p in c['pages']]))
        inherited_meta['summary']='Integrated question, original scenario and transfer limits for '+owner['title']+'. Detailed mechanisms have separate question owners.'
        integrated=''.join(wrap(meta['id'],i,text) for i,text in sections.items() if block_targets[(meta['id'],i)]==source)
        integrated+='\n## Integrated decision and reading route\n\n'+owner['result']+'\n\n'+owner['counterexample']+'\n\n'
        integrated+='The detailed pages separate the mechanisms that make this decision conditional:\n\n'
        for page in c['pages']:
            integrated+='- ['+page['title']+']('+rel(source,page['path'])+') — '+page['question']+'\n'
        integrated+='\n[Chapter introduction, ordered pages and full source ledger](README.md). Original source labels retain their historical scope; this editorial decomposition does not turn proposed experiments into executed evidence.\n'
        files[source]=render(inherited_meta)+integrated
        for i,page in enumerate(c['pages']):
            dest=page['path'];m=copy.deepcopy(meta)
            m.update(id=page['id'],canonical_path=dest,title=page['title'],
                     summary=page['question'],authored_at='2026-10-20',updated_at='2026-10-20')
            m['route_hints']={'questions':[page['question']],
                'prerequisites':[meta['id']] if i==0 else [c['pages'][i-1]['id']],
                'related_ids':[owner['id'],meta['id']]+([c['pages'][i+1]['id']] if i+1<len(c['pages']) else []),
                'excludes':['No independent technical approval, runtime experiment or universal applicability is implied.'],
                'keywords':[x for x in Path(dest).stem.split('-') if len(x)>1]}
            m['evidence_scope']={'source_ids':page.get('fresh_source_ids',meta['evidence_scope']['source_ids']),
                'claim_ids':[],'status':'source-linked' if page.get('fresh_source_ids',meta['evidence_scope']['source_ids']) else 'unknown',
                'notes':'Bounded question from '+meta['id']+'; exact inherited citation rows and limits remain in the chapter source ledger. New synthetic additions are separately labelled.'}
            m['content_review']={'status':'self-checked','reviewed_at':'2026-10-20','reviewer':'Codex editorial decomposition','proof_uri':None}
            m['source_inspection_date']='2026-10-20' if page.get('fresh_source_ids') else None
            m['content_verified_at']=None
            body='# '+page['title']+'\n\n**Owning question:** '+page['question']+'\n\n'
            body+='This page belongs to ['+c['code']+' — '+owner['title']+'](README.md). Use the integrated walkthrough for the surrounding decision; the sections below own this narrower mechanism and its limits.\n\n'
            body+=''.join(wrap(meta['id'],idx,sections[idx]) for idx in page['section_indices'])
            if page.get('editorial_addition'):body+='\n'+page['editorial_addition']+'\n'
            body+='\n## Navigation, prerequisites and source scope\n\n| Route | Destination |\n|---|---|\n'
            body+='| Parent and source ledger | [Chapter introduction and exact source rows](README.md#chapter-source-ledger) |\n'
            prev=source if not i else c['pages'][i-1]['path']
            nxt=c['pages'][i+1]['path'] if i+1<len(c['pages']) else c['chapter_path']
            body+='| Previous / prerequisite | [Read preceding context]('+rel(dest,prev)+') |\n'
            body+='| Next | [Continue the reasoning]('+rel(dest,nxt)+') |\n'
            body+='| Integrated question | [Original scenario and limits]('+rel(dest,source)+') |\n'
            body+='\nThe source material keeps its original published/inferred/synthetic/unverified distinctions. Chapter-wide citations are shared reference context, not proof that every cited source supports every sentence on this page. Freshly inspected text is identified explicitly; absent dates and unknowns are retained.\n'
            files[dest]=render(m)+body;new_metadata[dest]=m
        cm,cb=split((root/c['chapter_path']).read_text())
        start=cb.index('## Pages and reasoning route');end=cb.index('## Boundaries and further reading')
        route='## Pages and reasoning route\n\n'
        route+='Begin with the integrated decision, then open the independent question that matches the missing mechanism or observed failure. Read source limits before applying the conclusion.\n\n'
        route+='| Page | Independent question and role |\n|---|---|\n'
        route+='| [Integrated decision and original walkthrough]('+rel(c['chapter_path'],source)+') | '+owner['question']+' |\n'
        for page in c['pages']:
            route+='| ['+page['title']+']('+rel(c['chapter_path'],page['path'])+') | '+page['question']+' |\n'
        cb=cb[:start]+route+'\n'+cb[end:]
        cb+='\n## Chapter source ledger\n\nThe following original citation rows, review limits and earlier topical routes are retained once for this chapter. Each question page points here and retains its inline citations. Evidence coverage must be judged at the actual claim and version, not inferred from source-list length.\n\n'
        cb+=''.join(wrap(meta['id'],i,sections[i]) for i in ledger)
        if not ledger:
            cb+='This source manuscript cites its public evidence inline in the detailed mechanism pages; it has no separate legacy reference table to transfer. Follow each inline source for its actual supported claim and version. The integrated walkthrough retains historical case transfers and their nonclaim boundaries.\n'
        cm['route_hints']['related_ids']=list(dict.fromkeys(cm['route_hints']['related_ids']+[meta['id']]+[p['id'] for p in c['pages']]))
        cm['summary']=owner['question']+' The reading route separates '+str(len(c['pages']))+' detailed questions from the integrated decision.'
        files[c['chapter_path']]=render(cm)+cb
        records.append({'code':c['code'],'source_path':source,'source_id':meta['id'],
            'baseline_body_sha256':sha(originals[source][1]),
            'original_metadata':meta,'sections':[],'new_pages':c['pages']})

    # Derive fragment routes from actual destination heading positions, including
    # duplicate heading suffixes. No guessed heading/filename mapping.
    routes={}
    source_by_id={meta['id']:source for source,(meta,_,_) in originals.items()}
    for dest,text in files.items():
        active=None;ordinal=0;seen=Counter();fence=None
        for line in text.splitlines():
            marker=BLOCK_START.match(line)
            if marker:active=(marker.group(1),int(marker.group(2)));ordinal=0;continue
            if line==BLOCK_END:active=None;continue
            fm=re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)',line)
            if fm:
                mark=fm.group(1)
                if fence is None:fence=(mark[0],len(mark))
                elif mark[0]==fence[0] and len(mark)>=fence[1] and not fm.group(2).strip():fence=None
                continue
            h=re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*$',line) if fence is None else None
            if h:
                slug=slug_heading(h.group(1));n=seen[slug];seen[slug]+=1;fragment=slug if not n else slug+'-'+str(n)
                if active:
                    old=old_anchors[active][ordinal];ordinal+=1
                    routes[(source_by_id[active[0]],old)]=(dest,fragment)
    # Rebase each preserved block from its original location, then rebase the
    # generated surrounding links from their already-correct destination.
    for dest,text in list(files.items()):
        parts=[];active=None;block=[]
        for line in text.splitlines(keepends=True):
            marker=BLOCK_START.match(line.rstrip('\n'))
            if marker:
                active=(marker.group(1),int(marker.group(2)));block=[];parts.append(line)
            elif line.rstrip('\n')==BLOCK_END:
                parts.append(rebase(''.join(block),source_by_id[active[0]],dest,routes));parts.append(line);active=None
            elif active is not None:block.append(line)
            else:parts.append(rebase(line,dest,dest,routes))
        files[dest]=''.join(parts)
    for file in root.rglob('*.md'):
        if any(x in ('.git','node_modules') for x in file.relative_to(root).parts):continue
        path=file.relative_to(root).as_posix()
        if path not in files:
            before=file.read_text();after=rebase(before,path,path,routes)
            if before!=after:files[path]=after
    for record in records:
        source=record['source_path'];meta,body,sections=originals[source]
        for i,text in sections.items():
            dest=block_targets[(meta['id'],i)]
            record['sections'].append({'index':i,'target':dest,'original_sha256':sha(text),
                'normalized_sha256':sha(normalized(text,source,routes)),
                'words':len(text.split()),'headings':old_anchors[(meta['id'],i)]})
    registry=json.loads((root/'sources/document-identities.json').read_text())
    retained_ids=sorted(r['id'] for r in registry['documents'])
    for path,m in new_metadata.items():
        registry['documents'].append({'id':m['id'],'kind':'page','canonical_path':path,
            'origin_commit':None,'authored_at':m['authored_at'],'migration_body_sha256':sha(split(files[path])[1])})
    registry['documents'].sort(key=lambda r:r['canonical_path'])
    for c in outline['chapters']:
        entry=next(x for x in plan['chapters'] if x['code']==c['code'])
        c['question_pages']=[{'id':p['id'],'path':p['path'],'question':p['question']} for p in entry['pages']]
    outline['version']='2026.10.1-rc.1'
    outline['edition']='Tycho — substantive decomposition candidate'
    manifest={'schema_version':1,'baseline_commit':plan['baseline_commit'],'status':'editorial candidate; #214 open',
        'source_bodies':records,'fragment_routes':[{'old_path':p,'old_fragment':f,'new_path':n,'new_fragment':a} for (p,f),(n,a) in sorted(routes.items())],
        'added_page_ids':[m['id'] for m in new_metadata.values()], 'retained_document_ids':retained_ids}
    files['edition/decomposition-manifest.json']=json.dumps(manifest,indent=2,ensure_ascii=False)+'\n'
    files['edition/outline.json']=json.dumps(outline,indent=2,ensure_ascii=False)+'\n'
    files['sources/document-identities.json']=json.dumps(registry,indent=2,ensure_ascii=False)+'\n'
    source_register=json.loads((root/'sources/register.json').read_text())
    for admitted in plan.get('admitted_source_additions',[]):
        existing=next((x for x in source_register['sources'] if x['id']==admitted['id']),None)
        if existing is not None and existing!=admitted: raise ValueError('Source admission differs from the explicit plan')
        if existing is None: source_register['sources'].append(admitted)
    files['sources/register.json']=json.dumps(source_register,indent=2,ensure_ascii=False)+'\n'
    if write:
        for path,text in files.items():
            p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    return {'chapters':len(records),'new_question_pages':len(new_metadata),'fragment_routes':len(routes),'writes':len(files),'applied':write}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--apply',action='store_true')
    a=p.parse_args();print(json.dumps(apply(a.root,a.apply),indent=2))
