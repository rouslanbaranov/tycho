#!/usr/bin/env python3
"""Validate the finite edition and payload-preserving canonical migration.

Read-only by default. --write-inventory explicitly records the current content
membership; it must never be used to disguise a failed payload or identity gate.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

from assemble_edition import MARKER, external_urls, sha, split
from route_index import canonical_scan

ROOT = Path(__file__).resolve().parents[1]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_json(root, path):
    return json.loads((root/path).read_text())


def check_migration(root, outline, migration):
    chapters=outline['chapters'];volumes=outline['volumes']
    require(len(chapters)==69 and len(volumes)==10,'edition-count')
    require(len({c['code'] for c in chapters})==69,'duplicate-chapter-code')
    require(len({v['code'] for v in volumes})==10,'duplicate-volume-code')
    records=migration['documents']
    require(len(records)==69,'migration-count')
    require(len({r['old_path'] for r in records})==69,'duplicate-old-path')
    require(len({r['new_path'] for r in records})==69,'duplicate-new-path')
    require(len({r['id'] for r in records})==69,'duplicate-page-id')
    expected={c['code']:c for c in chapters}
    require({r['code'] for r in records}==set(expected),'migration-membership')
    word_counts=[]
    for r in records:
        c=expected[r['code']]
        require(r['old_path']==c['old_page_path'] and r['new_path']==c['page_path'],'migration-path')
        require(not (root/r['old_path']).exists(),'duplicate-canonical-old-path')
        path=root/r['new_path']
        require(path.is_file() and not path.is_symlink(),'missing-primary-page')
        meta,body=split(path.read_text())
        require(meta['id']==r['id'],'changed-page-id')
        require(meta['parent_id']==c['id']==r['new_parent_id'],'changed-page-parent')
        require(meta['canonical_path']==r['new_path'],'changed-page-path')
        # Only placement and edit date may differ from the accepted metadata.
        stable=lambda m:{k:v for k,v in m.items() if k not in ('canonical_path','parent_id','updated_at')}
        require(stable(meta)==stable(r['original_metadata']),'changed-evidence-metadata')
        require(body.count(MARKER)==1,'navigation-marker')
        payload=body.split(MARKER)[0]
        require(sha(payload)==r['migrated_payload_sha256'],'lost-or-altered-payload')
        require(external_urls(payload)==r['external_urls'],'changed-external-citations')
        require(len(re.findall(r'^# ',payload,re.M))==1,'primary-heading-count')
        words=len(payload.split())
        require(words<=3750,'oversized-primary-page')
        word_counts.append(words)
    # Structure is checked against the explicit outline, not just file counts.
    book_meta,_=split((root/'book/README.md').read_text())
    require(book_meta['kind']=='book','book-root-kind')
    for v in volumes:
        meta,body=split((root/v['path']).read_text())
        require(meta['id']==v['id'] and meta['kind']=='volume' and meta['parent_id']==book_meta['id'],'volume-identity')
        for section in ('## A worked cross-chapter synthesis','## Questions and chapters','## Counterexample and handoff','## Evidence and known limits'):
            require(section in body,'volume-synthesis-missing')
        require(v['scenario'] in body and v['synthesis'] in body and v['counterexample'] in body,'volume-synthesis-content')
    for c in chapters:
        meta,body=split((root/c['path']).read_text())
        volume=next(v for v in volumes if c['code'].startswith(v['code']+'/'))
        require(meta['kind']=='chapter' and meta['id']==c['id'] and meta['parent_id']==volume['id'],'chapter-identity')
        require(c['result'] in body and c['counterexample'] in body,'chapter-conclusion-missing')
        require('## Pages and reasoning route' in body and '## Navigation and prerequisites' in body,'chapter-route-missing')
    return {'migrated_pages':69,'primary_page_words_min':min(word_counts),'primary_page_words_max':max(word_counts)}


def inventory_members(root):
    result={}
    members=set()
    for folder in ('book','sources','schemas'):
        for p in (root/folder).rglob('*'):
            if p.is_file():
                require(not p.is_symlink(),'inventory-symlink')
                members.add(p.relative_to(root).as_posix())
    members.update(('generated/route-index.v1.json','edition/outline.json','edition/migration.json'))
    for path in sorted(members):
        result[path]=hashlib.sha256((root/path).read_bytes()).hexdigest()
    return result


def validate(root=ROOT,write_inventory=False):
    root=Path(root).resolve()
    outline=read_json(root,'edition/outline.json')
    migration=read_json(root,'edition/migration.json')
    require(outline['schema_version']==migration['schema_version']==1,'edition-schema-version')
    require(outline['baseline_commit']==migration['baseline_commit'],'migration-baseline')
    result=check_migration(root,outline,migration)
    index=canonical_scan(root)
    kinds=Counter(d['kind'] for d in index['documents'])
    require(kinds['volume']==10 and kinds['chapter']==69,'canonical-kind-counts')
    require(len(index['documents'])==215,'canonical-corpus-count')
    require(len({d['id'] for d in index['documents']})==215,'canonical-id-uniqueness')
    require(index==read_json(root,'generated/route-index.v1.json'),'edition-index-stale')
    identities=read_json(root,'sources/document-identities.json')['documents']
    require({(x['id'],x['canonical_path']) for x in identities}=={(x['id'],x['path']) for x in index['documents']},'edition-identity-registry')
    members=inventory_members(root)
    invpath=root/'edition/inventory.json'
    snapshot=hashlib.sha256(json.dumps(members,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    inventory={'schema_version':1,'version':outline['version'],'files':members,'content_snapshot_sha256':snapshot}
    if write_inventory:
        invpath.write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n')
    else:
        require(invpath.is_file(),'edition-inventory-missing')
        require(read_json(root,'edition/inventory.json')==inventory,'edition-inventory-drift')
    return {**result,'volumes':10,'chapters':69,'canonical_documents':215,
            'kinds':dict(kinds),'inventory_files':len(members),
            'content_snapshot_sha256':snapshot,'route_snapshot_sha256':index['snapshot_sha256'],
            'scope':'structure, preserved payload and frozen membership; not independent claim review or external URL availability'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=ROOT)
    p.add_argument('--write-inventory',action='store_true')
    args=p.parse_args()
    try:
        print(json.dumps(validate(args.root,args.write_inventory),indent=2))
    except (ValueError,OSError,KeyError) as error:
        print('FAIL:',error,file=sys.stderr);sys.exit(1)
