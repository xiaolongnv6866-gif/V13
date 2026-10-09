#!/usr/bin/env python3
"""R054 V1 source sufficiency audit, GitHub SOURCE_STRUCTURE_ONLY; original EPUB private."""
from pathlib import Path
import csv,json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
fail=[]
def ck(cond,msg):
    if not cond:fail.append(msg)
def tsv(path):
    with path.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
books={
  'wanming':{'prefix':'WM','count':91,'pass':68,'review':23,'loci':145,'source':'a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082','digest':'a03ed960c5278df6b33578d19a8b8483cdba1cb88e9677ee8130117e3c280495'},
  'tiexuecanming':{'prefix':'TX','count':96,'pass':80,'review':16,'loci':177,'source':'9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf','digest':'990a8ade5c2e78174bc82b4e7f66d4c40995f9af2e715654c7fcec2634cf6548'}
}
tables=['FRAMEWORK_EVIDENCE.tsv','PRINCIPLE_EVIDENCE.tsv','CASE_EVIDENCE.tsv','COUNTEREXAMPLE_EVIDENCE.tsv','GLOSSARY_EVIDENCE.tsv']
allids=set()
for slug,conf in books.items():
    root=ROOT/'books'/slug
    source=tsv(root/'R053_CANDIDATE_MATRIX.tsv')
    v1=tsv(root/'validation/V1_EVIDENCE.tsv')
    ck(len(source)==len(v1)==conf['count'],slug+' missing candidates')
    scope_map={x['candidate_id']:x for x in source}
    ck(len(scope_map)==conf['count'],slug+' R053 unique IDs')
    original_hash={}
    with (ROOT/'sources/metadata'/(slug+'_v13_spine.csv')).open(encoding='utf-8',newline='') as f:
        meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
    ck(len(meta)==(571 if slug=='wanming' else 532),slug+' narrative OPF drift')
    for srcname in tables:
        for r in tsv(root/'candidates'/srcname):
            pos=r['source_locus'];sha=r['paragraph_sha256']
            ck(original_hash.get(pos,sha)==sha,slug+' contradictory original source SHA '+pos)
            original_hash[pos]=sha
            try:
                n,p=map(int,re.fullmatch(r'n(\d{3})/p(\d+)',pos).groups())
                ck(1<=p<=int(meta[n]['nonempty_paragraphs']),slug+' paragraph out-of-range '+pos)
                ck(meta[n]['chapter_sha256']==r['chapter_sha256'] and meta[n]['epub_path']==r['epub_path'],slug+' epub original path/sha mismatch '+pos)
            except Exception as e:fail.append(slug+' bad original n/p '+pos+': '+str(e))
    positions=sorted(original_hash,key=lambda x:tuple(map(int,re.findall(r'\d+',x))))
    fingerprint=hashlib.sha256('\n'.join(x+'='+original_hash[x] for x in positions).encode()).hexdigest()
    ck(len(positions)==conf['loci'] and fingerprint==conf['digest'],slug+' original private recheck manifest digest differs')
    rids=set()
    decision={'PASS':0,'REVIEW':0,'FAIL':0}
    for r in v1:
        rid=r['candidate_id'];rids.add(rid);allids.add(rid)
        ck(rid.startswith(conf['prefix']+'-') and rid in scope_map,slug+' extra V1 ID '+rid)
        if rid not in scope_map:continue
        before=scope_map[rid]
        ck(r['original_id']==before['original_id'] and r['title']==before['title'],slug+' changed original candidate title/ID '+rid)
        ck(r['extractor_type']==before['extractor_type'],slug+' modified extractor type '+rid)
        ck(r['source_candidate_file']==before['candidate_source_file'],slug+' original source file replaced '+rid)
        ck(r['source_loci']==before['original_source_loci'] and r['task_ids']==before['task_ids'],slug+' original n/p or task changed '+rid)
        ck(r['source_epub_sha256']==conf['source'],slug+' wrong EPUB edition '+rid)
        anchor=r['source_loci'].split(';')[0]
        ck(anchor in original_hash and r['primary_paragraph_sha256']==original_hash.get(anchor),slug+' first source SHA mismatched '+rid)
        verdict=r['V1']
        ck(verdict in decision,slug+' invalid V1 outcome '+rid)
        if verdict in decision:decision[verdict]+=1
        ck(len(r['source_observation'])>=12 and len(r['V1_reason'])>=28,slug+' no substantive source reading for '+rid)
        ck(len(r['source_scope'])>=16 and bool(r['evidence_class']),slug+' V1 overgeneralization boundary omitted '+rid)
        ck(r['V2']=='NOT_STARTED_R055' and r['V3']=='NOT_STARTED_R056',slug+' future step falsely certified '+rid)
        ck(r['copyright_status']=='ORIGINAL_NOT_PUBLISHED_SHA_ANCHORED',slug+' source copyright limit '+rid)
        ck(r['evidence_class'] in ('SOURCE_REFERENCE_ONLY','LIMITED_NARRATIVE_RECONSTRUCTION'),slug+' false method type '+rid)
        if r['extractor_type'] in ('case','counter-example','term'):ck(r['evidence_class']=='SOURCE_REFERENCE_ONLY',slug+' fictional event wrongly promoted to independent method '+rid)
    ck(rids==set(scope_map),slug+' candidate dropped in V1')
    ck(len(rids)==len(v1),slug+' duplicate V1 rows')
    ck(decision=={'PASS':conf['pass'],'REVIEW':conf['review'],'FAIL':0},slug+' unexpected decision numbers '+str(decision))
    document=(root/'validation/V1_SOURCE.md').read_text(encoding='utf-8')
    ids=re.findall(r'(?m)^### ('+conf['prefix']+r'-(?:ce|f|p|c|g)\d{2})｜',document)
    ck(len(ids)==conf['count'] and set(ids)==rids,slug+' Markdown individual review missing')
    ck(conf['digest'] in document and 'NOT_STARTED_R055' in document and 'PROVISIONAL' in document,slug+' report wrongly certified')
audit=(ROOT/'books/R054_V1_AUDIT.md').read_text(encoding='utf-8')
for token in ('187','148','39','322','V1','R055','R056','R057','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','n526','n532'):
    ck(token in audit,'audit missing '+token)
ck(len(allids)==187,'crossbook ID collision')
old=tsv(ROOT/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'legacy literary debt improperly certified')
state=json.loads((ROOT/'CURRENT_ROUND.json').read_text(encoding='utf-8'))
n=int(state['current_round'][1:])
ck(state['round_status']=='NOT_STARTED' and ((n==54 and state['last_passed_round']=='R053' and state['rounds_completed']==53) or (n>=55 and state['rounds_completed']==n-1 and int(state['last_passed_round'][1:])>=54)),'formal R054 status guard')
ck(state['skill_certified_count']==0 and state['original_output_test_status']=='NOT_RUN' and state['literary_interpretation_status']=='PROVISIONAL','false skill/B/C upgrading')
ck(state['legacy_quality_debt_status']=='OPEN_QUARANTINED' and state['heldout_bank_status']=='SEALED_NOT_RUN','old debt/heldout altered')
with (ROOT/'ROUND_LEDGER.csv').open(encoding='utf-8',newline='') as f:
    ledger={r['id']:r for r in csv.DictReader(f)}
ck(ledger['R053']['status']=='PASSED','R053 predecessor not complete')
ck(ledger['R054']['status']==('NOT_STARTED' if n==54 else 'PASSED'),'R054 ledger mismatch')
if n==55:ck(ledger['R055']['status']=='NOT_STARTED','R055 must remain not started')
for x in fail:print('FAIL:',x)
print('R054 V1', 'FAIL' if fail else 'PASS','187 individually adjudicated; 148 limited source-pass, 39 requires-review, 0 source-contradicted; 322 private original source SHA; public CI SOURCE_STRUCTURE_ONLY; V2/V3 NOT_STARTED, Skill0')
sys.exit(bool(fail))
