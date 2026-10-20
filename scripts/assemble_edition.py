#!/usr/bin/env python3
"""Explicit one-time assembly of the accepted manuscript. Default: dry-run.

Use --apply only on the recorded baseline. IDs and editorial synthesis are
reviewed inputs in edition/outline.json, never inferred by an index refresh.
Rollback uses the recorded baseline commit and the reversible migration map.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit, unquote

from frontmatter_generate import render
from route_index import FENCE, engine

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'(!?\[[^\]\n]*\]\()([^\s)]+)([^)\n]*\))')
MARKER = '\n<!-- tycho-edition-navigation -->\n'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def split(text):
    match = FENCE.match(text)
    if not match:
        raise ValueError('Missing strict metadata')
    yaml, _, _ = engine()
    return yaml.safe_load(match.group(1)), text[match.end():]


def rel(source, target):
    return posixpath.relpath(target, posixpath.dirname(source))


def rewrite_links(text, old, new, moves):
    def change(m):
        raw = m.group(2)
        u = urlsplit(raw)
        if u.scheme or u.netloc or raw.startswith(('/', '#')):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(old), unquote(u.path)))
        if target not in moves and old == new:
            return m.group(0)
        target = moves.get(target, target)
        value = rel(new, target)
        if u.query:
            value += '?' + u.query
        if u.fragment:
            value += '#' + u.fragment
        return m.group(1) + value + m.group(3)
    return LINK.sub(change, text)


def external_urls(text):
    return sorted(set(re.findall(r'https?://[^\s)<>"]+', text)))


def metadata(path, identity, kind, parent, title, question, inherited, related, prerequisites):
    topics = sorted({x for m in inherited for x in m['topic_ids']})
    source_ids = sorted({x for m in inherited for x in m['evidence_scope']['source_ids']})
    return {
        'metadata_version': 1, 'id': identity, 'kind': kind, 'parent_id': parent,
        'canonical_path': path, 'title': title, 'topic_ids': topics,
        'perspectives': ['architecture', 'evaluation'], 'summary': question,
        'route_hints': {'questions': [question], 'prerequisites': prerequisites,
                        'related_ids': list(dict.fromkeys(related)),
                        'excludes': ['No new benchmark, source inspection or independent edition review is asserted.'],
                        'keywords': ['system-design', 'edition-navigation']},
        'evidence_scope': {'source_ids': source_ids, 'claim_ids': [],
                           'status': 'source-linked' if source_ids else 'unknown',
                           'notes': 'Editorial synthesis of the linked accepted manuscript; exact source versions and nonclaims remain in its page-local evidence ledger.'},
        'content_review': {'status': 'self-checked', 'reviewed_at': '2026-10-20',
                           'reviewer': 'Codex editorial assembly', 'proof_uri': None},
        'authored_at': '2026-10-20', 'updated_at': '2026-10-20',
        'source_inspection_date': None, 'content_verified_at': None,
    }


def assemble(root, apply=False):
    root = Path(root)
    outline = json.loads((root/'edition/outline.json').read_text())
    chapters, volumes = outline['chapters'], outline['volumes']
    if len(chapters) != 69 or len(volumes) != 10:
        raise ValueError('Expected the selected 10-volume/69-chapter outline')
    if (root/'edition/migration.json').exists():
        raise ValueError('Assembly already applied; validate, or restore the recorded baseline before reapplying')
    originals = {}
    for c in chapters:
        text = (root/c['old_page_path']).read_text()
        originals[c['code']] = (text, *split(text))
    root_meta, _ = split((root/'book/README.md').read_text())
    by_code = {c['code']: c for c in chapters}
    vol_by_code = {v['code']: v for v in volumes}
    moves = {c['old_page_path']: c['page_path'] for c in chapters}
    registry = json.loads((root/'sources/document-identities.json').read_text())
    entries = {r['id']: r for r in registry['documents']}
    new_files, records = {}, []
    for c in chapters:
        text, meta, body = originals[c['code']]
        rewritten = rewrite_links(body, c['old_page_path'], c['page_path'], moves)
        changed = copy.deepcopy(meta)
        changed['canonical_path'], changed['parent_id'] = c['page_path'], c['id']
        changed['updated_at'] = '2026-10-20'
        nav = MARKER + '\n## Edition navigation and evidence scope\n\n'
        nav += '| Route | Destination |\n|---|---|\n'
        nav += '| Parent chapter | [Question, conclusions and reading route](README.md) |\n'
        nav += '| Parent volume | [Volume synthesis](../README.md) |\n'
        nav += '| Book | [Authoritative contents]('+rel(c['page_path'],'book/README.md')+') |\n'
        nav += '| Source versions and access scope | [Registered sources]('+rel(c['page_path'],'sources/README.md')+') and the exact page-local citation ledger above |\n'
        nav += '\nThe original manuscript was accepted under #213 at the recorded baseline. Earlier draft/review labels describe historical authoring events. Source access, versions, unexecuted experiments and nonclaims retain their original scope; assembly does not assert a new source read or benchmark. The chapter landing adds editorial synthesis and navigation.\n'
        new_files[c['page_path']] = render(changed)+rewritten+nav
        records.append({
            'code': c['code'], 'id': meta['id'], 'old_path': c['old_page_path'],
            'new_path': c['page_path'], 'old_parent_id': meta['parent_id'],
            'new_parent_id': c['id'], 'original_metadata': meta,
            'baseline_document_sha256': sha(text), 'baseline_body_sha256': sha(body),
            'migrated_payload_sha256': sha(rewritten),
            'external_urls': external_urls(body),
            'reason': 'Move one accepted bounded question into its selected chapter; preserve identity and source payload.',
        })
        entries[meta['id']]['canonical_path'] = c['page_path']

    # Cross-owner boundaries from the selected outline; the wording stays in the
    # editorial report while the chapter route points to the corresponding owner.
    toc = (root/'authoring/FINAL_TOC_AND_OWNER_BOUNDARIES_2026-10-20.md').read_text()
    boundaries = {}
    for line in toc.splitlines():
        if line.startswith('| V') and ' vs ' in line:
            codes = re.findall(r'V\d{2}/C\d{2}', line)
            for code in codes:
                boundaries.setdefault(code, set()).update(x for x in codes if x != code)

    for i, c in enumerate(chapters):
        path = c['path']; vol = vol_by_code[c['code'].split('/')[0]]
        _, page_meta, page_body = originals[c['code']]
        prev = chapters[i-1] if i else None
        nxt = chapters[i+1] if i+1 < len(chapters) else None
        prerequisite_codes = vol['prerequisite_codes'] if c['code'].endswith('/C01') else [chapters[i-1]['code']]
        related_codes = sorted(boundaries.get(c['code'], set()))
        related_ids = [by_code[x]['id'] for x in related_codes]
        body = '# '+c['code']+' — '+c['title']+'\n\n'
        body += '## Purpose and mission\n\n'+c['question']+' This chapter owns that question within '+vol['title'].lower()+'. Read the mechanism together with its stated invariant, failure assumptions and evidence limits before applying the result to another system.\n\n'
        body += '## Decision and worked result\n\n'+c['result']+'\n\n'+c['counterexample']+' This is an editorial conclusion drawn from the linked manuscript and its original examples, not a newly executed experiment.\n\n'
        body += '## Pages and reasoning route\n\n'
        body += '| Page | Owning question |\n|---|---|\n'
        body += '| ['+page_meta['title']+']('+Path(c['page_path']).name+') | '+c['question']+' |\n\n'
        heads = re.findall(r'^## (.+)$', page_body, re.M)
        useful = [h for h in heads if not h.lower().startswith(('navigation','reading and navigation','purpose'))]
        chosen = []
        for h in useful[:2] + useful[-2:]:
            if h not in chosen:
                chosen.append(h)
        from validate_book_navigation import slug_heading
        body += 'The page is one bounded explanation. Its mechanism, failure analysis and evidence are kept together rather than split to meet a numerical page quota. Use these section entry points:\n\n'
        for h in chosen:
            body += '- ['+h+']('+Path(c['page_path']).name+'#'+slug_heading(h)+').\n'
        body += '\n## Boundaries and further reading\n\n'
        if related_codes:
            for code in related_codes:
                body += '- ['+code+' — '+by_code[code]['title']+']('+rel(path,by_code[code]['path'])+') owns the adjacent question; compare assumptions before transferring the conclusion.\n'
        else:
            body += 'The preceding and following chapters supply context; this landing does not replace their canonical mechanisms. Follow the exact source ledger on the child page when a claim depends on a product version or historical period.\n'
        body += '\n## Navigation and prerequisites\n\n| Route | Destination |\n|---|---|\n'
        body += '| Parent | ['+vol['code']+' — '+vol['title']+'](../README.md) |\n'
        for label,obj in [('Previous',prev),('Next',nxt)]:
            body += '| '+label+' | '+('['+obj['code']+' — '+obj['title']+']('+rel(path,obj['path'])+')' if obj else '[Book contents]('+rel(path,'book/README.md')+')')+' |\n'
        for code in prerequisite_codes:
            body += '| Prerequisite | ['+code+' — '+by_code[code]['title']+']('+rel(path,by_code[code]['path'])+') |\n'
        body += '| Source reading | [Page-local evidence and versions]('+Path(c['page_path']).name+') |\n'
        body += '\n## Evidence and limits\n\nThe child manuscript belongs to the owner-accepted #213 baseline. This new landing is editorially self-checked; it is not an independent technical review. Published behavior, original synthetic reasoning and unknowns remain distinguished in the child page. No new benchmark, runtime compatibility test or source-access date is implied.\n'
        meta = metadata(path,c['id'],'chapter',vol['id'],c['code']+' — '+c['title'],c['question'],[page_meta],related_ids,[by_code[x]['id'] for x in prerequisite_codes])
        new_files[path] = render(meta)+'\n'+body

    for i,v in enumerate(volumes):
        path=v['path'];own=[c for c in chapters if c['code'].startswith(v['code']+'/')]
        inherited=[originals[c['code']][1] for c in own]
        body='# '+v['code']+' — '+v['title']+'\n\n## Purpose and mission\n\n'+v['mission'].capitalize()+'\n\n'
        body+='The outcome of this volume is: '+v['synthesis_question']+'\n\n'
        body+='## A worked cross-chapter synthesis\n\n'+v['scenario']+'\n\n'+v['synthesis']+'\n\n'
        body+='## Questions and chapters\n\n| Chapter | Owning question |\n|---|---|\n'
        for c in own:
            body+='| ['+c['code']+' — '+c['title']+']('+rel(path,c['path'])+') | '+c['question']+' |\n'
        body+='\n## Choosing a reading route\n\n'
        body+='For a first reading, follow the chapter order. For diagnosis, connect the observed outcome to its authority and failure boundary using: '+', '.join('['+code+']('+rel(path,by_code[code]['path'])+')' for code in v['diagnostic_route'])+'. Return to the exact page-local source ledger before making a version-specific claim.\n\n'
        body+='Prerequisite context: '+v['prerequisite_description']+'\n\n'
        if v['prerequisite_codes']:
            body+='Read '+', '.join('['+x+']('+rel(path,by_code[x]['path'])+')' for x in v['prerequisite_codes'])+' for the named entry assumptions.\n\n'
        # A branching reasoning map, not an illustration of an observed system.
        labels=[v['diagnostic_route'][0]+' — '+by_code[v['diagnostic_route'][0]]['title'],
                v['diagnostic_route'][1]+' — '+by_code[v['diagnostic_route'][1]]['title'],
                v['diagnostic_route'][-1]+' — '+by_code[v['diagnostic_route'][-1]]['title']]
        body+='### Reasoning boundaries\n\nThis original conceptual map separates competing inputs rather than promising a universal solution.\n\n'
        body+='~~~mermaid\nflowchart TD\n    Q["'+labels[0]+'"] --> M["'+labels[1]+'"]\n    Q --> E["Evidence and unknown inputs"]\n    M --> D{"Meets the declared constraints?"}\n    E --> D\n    D -->|Supported| R["'+labels[2]+'"]\n    D -->|Unresolved| U["Measure, revise or retain the baseline"]\n~~~\n\n'
        body+='Text alternative: establish '+by_code[v['diagnostic_route'][0]]['title'].lower()+', compare '+by_code[v['diagnostic_route'][1]]['title'].lower()+' with the available evidence, and either carry a supported result forward or return to unresolved inputs. The figure describes a reasoning route, not observed runtime behavior.\n\n'
        body+='## Counterexample and handoff\n\n'+v['counterexample']+'\n\n'
        body+='## Navigation and source boundaries\n\n| Route | Destination |\n|---|---|\n| Parent | [Book contents](../../README.md) |\n'
        if i:body+='| Previous volume | ['+volumes[i-1]['code']+']('+rel(path,volumes[i-1]['path'])+') |\n'
        if i+1<len(volumes):body+='| Next volume | ['+volumes[i+1]['code']+']('+rel(path,volumes[i+1]['path'])+') |\n'
        body+='| Historical applications | [Casebook and synthetic playbooks]('+rel(path,'book/cases/README.md')+') |\n'
        body+='\n## Evidence and known limits\n\nThe scenario is original synthetic reasoning. The chapters contain the accepted manuscript and its published evidence; no synthetic number or historical result is a measured prediction for another system. This new synthesis is editorially self-checked, not independently certified. Source-access restrictions, unexecuted technology experiments and original case denominators remain explicit in their owning pages. Product-specific adoption still requires compatible versions and the target workload.\n'
        meta=metadata(path,v['id'],'volume',root_meta['id'],v['code']+' — '+v['title'],v['synthesis_question'],inherited,[c['id'] for c in own],[by_code[x]['id'] for x in v['prerequisite_codes']])
        if v['code']=='V10':
            meta['route_hints']['prerequisites']=[x['id'] for x in volumes[:-1]]
            body=body.replace('Read [V01/C01]', 'For the complete modernization route, read all earlier volume syntheses and mechanisms. Read [V01/C01]')
        new_files[path]=render(meta)+'\n'+body

    # Rewrite relative file links for both moved and stationary documents.
    for file in root.rglob('*.md'):
        if any(x in ('.git','node_modules') for x in file.relative_to(root).parts):
            continue
        path=file.relative_to(root).as_posix()
        if path in moves or path=='book/README.md':
            continue
        text=file.read_text()
        rewritten=rewrite_links(text,path,path,moves)
        if rewritten != text:
            new_files[path]=rewritten

    # The book landing is the single authoritative TOC; topic entries and
    # the casebook are explicitly supporting routes, not additional volumes.
    p='book/README.md'
    body='# Tycho — System Design\n\n## Purpose and mission\n\nReason about requirements, mechanisms, partial failure and safe modernization using independently published evidence and original synthetic examples. The book develops conditional engineering judgment: retain a simple design, measure first or state insufficient evidence whenever the facts require it.\n\n'
    body+='## '+outline['edition']+'\n\nThe reading edition comprises ten volumes and exactly 69 primary chapters. Each chapter links to one substantive bounded technical page; supporting essays and the historical casebook preserve earlier researched material without creating extra primary chapters. Source versions, access limits and nonclaims remain with their owning pages.\n\n'
    body+='## Contents\n\n| Volume | Chapters | Learning outcome |\n|---|---|---|\n'
    for v in volumes:
        own=[c for c in chapters if c['code'].startswith(v['code']+'/')]
        body+='| ['+v['code']+' — '+v['title']+']('+rel(p,v['path'])+') | '+str(len(own))+' | '+v['synthesis_question']+' |\n'
    body+='\n## How to read\n\nBegin with V01 to define outcomes, workload and evidence. Follow V02–V09 for mechanisms and their failure boundaries; V10 combines them into falsifiable modernization decisions. Each chapter provides previous/next, prerequisite, related-owner and source-reading links. Specialists may enter a chapter directly after checking its prerequisite contract.\n\n'
    body+='The [29 historical cases and six synthetic playbooks](cases/README.md) are a linked applied reading layer. The [historical topical entries](PROPOSED-STRUCTURE.md) and their supporting essays remain available; the volume/chapter contents above govern the edition order. Historical company outcomes do not promise benefits for another workload.\n\n'
    body+='## Evidence, acceptance and limitations\n\nThe 69 original manuscripts were substantively accepted by the owner under #213 at the recorded baseline. New volume/chapter syntheses are editorially self-checked. Page-local records distinguish published evidence, original inference, proposed tests and unknowns. No independent signatures, new benchmark or source-access date are manufactured.\n\n'
    body+='[Edition record and reproducible checks](../edition/README.md) describe the inventory, reversible migration, validation scope and publication state. The edition does not deploy a search service, MCP endpoint or specialist runtime. Visual rendering and live MCP remain owner-cancelled; later retrieval and deployment work follows the book release.\n'
    support = ['application','performance','distributed','search','scaling','data','integration','execution','delivery','deployment','observability','security','decisions']
    at = body.index('## Evidence, acceptance and limitations')
    section = '## Supporting topic routes\n\nThese retained topical entries provide secondary routes into the same canonical pages and supporting essays. The ten-volume contents above remain the primary reading order.\n\n'
    section += ' | '.join('['+f.replace('-',' ').title()+']('+f+'/README.md)' for f in support)+'\n\n'
    body = body[:at]+section+body[at:]
    changed=copy.deepcopy(root_meta)
    changed['title']='Tycho — System Design'
    changed['summary']='Ten-volume, 69-chapter System Design reading edition with canonical mechanisms, failure boundaries, evidence and modernization reasoning.'
    changed['route_hints']['related_ids']=[v['id'] for v in volumes]
    changed['updated_at']='2026-10-20'
    changed['route_hints']['excludes']=['No hosted service or runtime reproduction is implied.']
    changed['content_review']={'status':'self-checked','reviewed_at':'2026-10-20','reviewer':'Codex editorial assembly','proof_uri':None}
    new_files[p]=render(changed)+'\n'+body

    for path,text in list(new_files.items()):
        if path.startswith('book/'):
            meta,body=split(text)
            if meta['id'] not in entries:
                entries[meta['id']]={'id':meta['id'],'kind':meta['kind'],
                    'canonical_path':path,'origin_commit':None,'authored_at':meta['authored_at'],
                    'migration_body_sha256':sha(body)}
    registry['documents']=sorted(entries.values(),key=lambda x:x['canonical_path'])
    migration={'schema_version':1,'baseline_commit':outline['baseline_commit'],
               'from_contract_version':1,'to_contract_version':1,
               'policy':'Preserve all previous identities and evidence; only new volume/chapter entities receive new identities.',
               'documents':records}
    new_files['sources/document-identities.json']=json.dumps(registry,indent=2,ensure_ascii=False)+'\n'
    new_files['edition/migration.json']=json.dumps(migration,indent=2,ensure_ascii=False)+'\n'
    evaluation_path='evaluation/pilot-questions.json'
    evaluation=(root/evaluation_path).read_text()
    for old,new in moves.items():
        evaluation=evaluation.replace(old,new)
    new_files[evaluation_path]=evaluation
    summary={'moves':len(moves),'new_volume_landings':len(volumes),
             'new_chapter_landings':len(chapters),'writes':len(new_files),'applied':apply}
    if apply:
        for path,text in new_files.items():
            target=root/path;target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(text)
        for old in moves:
            (root/old).unlink()
    return summary


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=ROOT)
    p.add_argument('--apply',action='store_true')
    args=p.parse_args()
    print(json.dumps(assemble(args.root,args.apply),indent=2))
