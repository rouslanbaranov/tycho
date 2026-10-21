#!/usr/bin/env python3
"""Read-only conservation and ownership checks for the editorial decomposition."""
import json
from pathlib import Path
from collections import Counter

from assemble_edition import split,sha
from content_revisions import authorized
from decompose_chapters import extract_blocks,normalized
from directory_paths import HistoricalView

ROOT=Path(__file__).resolve().parents[1]


def require(ok,message):
    if not ok:raise ValueError(message)


def validate(root=ROOT):
    root=Path(root)
    view=HistoricalView(root)
    plan=json.loads((root/'edition/decomposition-plan.json').read_text())
    manifest=json.loads((root/'edition/decomposition-manifest.json').read_text())
    migration=json.loads((root/'edition/migration.json').read_text())
    require(plan['baseline_commit']==manifest['baseline_commit'],'decomposition-baseline')
    require(len(plan['chapters'])==len(manifest['source_bodies'])==69,'decomposition-chapter-count')
    require(len({x['code'] for x in plan['chapters']})==69,'duplicate-chapter-code')
    routes={(r['old_path'],r['old_fragment']):(r['new_path'],r['new_fragment']) for r in manifest['fragment_routes']}
    atlas_path=root/'edition/atlas-manifest.json'
    atlas_ids={d['id'] for d in json.loads(atlas_path.read_text())['documents']} if atlas_path.is_file() else set()
    all_blocks={};metadata={};texts={}
    for path in (root/'book').rglob('*.md'):
        relative=view.original(path.relative_to(root).as_posix());text=view.read_text(relative)
        meta,_=split(text)
        if meta['id'] in atlas_ids:
            continue
        metadata[relative]=meta;texts[relative]=text
        for key,value in extract_blocks(text).items():
            require(key not in all_blocks,'duplicate-source-payload')
            all_blocks[key]=(relative,value)
    require(set(manifest['retained_document_ids']) <= {m['id'] for m in metadata.values()},'lost-earlier-document-identity')
    expected=set();word_counts=[];new_ids=[]
    old_migrations={r['id']:r for r in migration['documents']}
    require(not any((root/r['old_path']).exists() for r in migration['documents']),'duplicate-retired-canonical-path')
    protected=('id','kind','parent_id','canonical_path','evidence_scope','content_review','authored_at','source_inspection_date','content_verified_at')
    for record in manifest['source_bodies']:
        original_id=record['source_id']
        require(record['baseline_body_sha256']==old_migrations[original_id]['migrated_payload_sha256'],'accepted-baseline-payload')
        require(record['source_path'] in metadata,'missing-integrated-page')
        current=metadata[record['source_path']]
        require(all(current[k]==record['original_metadata'][k] for k in protected),'altered-original-provenance')
        require(len({r['index'] for r in record['sections']})==len(record['sections']),'duplicate-source-section')
        for section in record['sections']:
            key=(original_id,section['index']);expected.add(key)
            require(key in all_blocks,'missing-source-payload')
            target,payload=all_blocks[key]
            require(target==section['target'],'source-owner-mismatch')
            current_sha=sha(normalized(payload,target,routes))
            require(current_sha==section['normalized_sha256']
                    or authorized(root,'source_blocks',f'{original_id}:{section["index"]}',
                                  section['normalized_sha256'],current_sha),
                    'altered-source-payload')
    require(set(all_blocks)==expected,'unregistered-source-payload')
    for chapter in plan['chapters']:
        require(chapter['chapter_path'] in metadata,'missing-chapter-introduction')
        cm=metadata[chapter['chapter_path']]
        require(cm['id']==chapter['chapter_id'] and cm['kind']=='chapter','chapter-identity')
        require('## Chapter source ledger' in texts[chapter['chapter_path']],'missing-chapter-ledger')
        require(texts[chapter['chapter_path']].split('## Chapter source ledger',1)[1].strip(),'empty-chapter-ledger')
        for page in chapter['pages']:
            path=page['path'];new_ids.append(page['id'])
            require(path in metadata,'missing-question-page')
            m=metadata[path];text=texts[path]
            require(m['id']==page['id'] and m['parent_id']==chapter['chapter_id'],'question-identity-parent')
            require(m['kind']=='page' and m['canonical_path']==path,'question-kind-path')
            require(m['route_hints']['questions']==[page['question']],'question-route-drift')
            require(page['question'] in text,'question-context-missing')
            require('README.md#chapter-source-ledger' in text,'question-source-route')
            if page.get('editorial_addition'):
                require(page['editorial_addition'] in text,'missing-editorial-deepening')
            require(page['section_indices'] or page.get('editorial_addition'),'empty-question-page')
            for idx in page['section_indices']:
                source_record=next(r for r in manifest['source_bodies'] if r['code']==chapter['code'])
                require(all_blocks[(source_record['source_id'],idx)][0]==path,'planned-question-owner')
            if page.get('fresh_source_ids'):
                require(m['source_inspection_date']=='2026-10-20','missing-fresh-inspection-date')
                require(m['evidence_scope']['source_ids']==page['fresh_source_ids'],'fresh-source-binding')
            else:
                require(m['source_inspection_date'] is None and m['content_verified_at'] is None,'fabricated-question-verification')
            word_counts.append(len(split(text)[1].split()))
    require(len(set(new_ids))==len(new_ids),'duplicate-question-id')
    require(set(new_ids)==set(manifest['added_page_ids']),'added-question-membership')
    return {'reviewed_chapters':69,'preserved_original_manuscripts':69,
            'preserved_source_blocks':len(expected),'new_question_pages':len(new_ids),
            'fragment_routes':len(routes),'question_page_words_min':min(word_counts),
            'question_page_words_max':max(word_counts),
            'scope':'conserved text, provenance and explicit question ownership; not independent editorial acceptance'}


if __name__=='__main__':
    import sys
    try:print(json.dumps(validate(),indent=2))
    except (ValueError,OSError,KeyError) as e:print('FAIL:',e,file=sys.stderr);sys.exit(1)
