#!/usr/bin/env python3
"""R050: public structural source provenance only; no semantic or creativity certification."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1];B=R/'books/tiexuecanming/candidates';err=[]
def ck(ok,msg):
 if not ok:err.append(msg)
def tsv(p):
 with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
candidate=(B/'cases.md').read_text(encoding='utf-8')
start=candidate.find('- id: c01');end=candidate.find('## 类型边界',start)
ck(start>=0 and end>start,'missing c case block')
units=[x for x in re.split(r'(?=^- id: c\d\d$)',candidate[start:end],flags=re.M) if x.lstrip().startswith('- id: c')]
ids=[re.search(r'(?m)^- id: (c\d\d)$',x).group(1) for x in units]
ck(ids==[f'c{i:02d}' for i in range(1,17)],'expected 16 c01-c16')
loc=set();chunk=set();tasks=set();links={}
required=['title','type','example_kind','source_reality','example_kind_extension_status','source_chapter','source_quote','source_quote_status','source_loci','chunk_ids','summary','bound_to','outcome','outcome_scope','counterpressure_or_limit','task_ids','tags','status','verification_state']
for id,item in zip(ids,units):
 for f in required:ck(bool(re.search(r'(?m)^  '+f+r':',item)),id+' missing '+f)
 ck('type: case' in item and 'example_kind: fictional_narrative_case' in item and 'REQUIRES_STAGE1_5_REVIEW' in item,id+' invalid literary category')
 ck('source_quote: ""' in item and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in item,id+' copyright')
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in item and 'NOT_STARTED_STAGE1_5' in item,id+' unearned certification')
 L=set(re.findall(r'^    - "(n\d{3}/p\d+)"',item,re.M));K=set(re.findall(r'^    - "(ck-[0-9a-f]{12})"',item,re.M))
 ck(len(L)>=3 and len(K)>=1,id+' source or chunk shortage')
 loc.update(L);chunk.update(K);links[id]=(L,K)
 m=re.search(r'(?m)^  task_ids: \[([^]]+)\]',item)
 if m:tasks.update(t.strip() for t in m.group(1).split(','))
 ck('  bound_to:\n    - "' in item,id+' no bound_to')
 ck(len(re.findall(r'^    [^\n]+',item.split('  summary: |-')[1].split('  bound_to:')[0],re.M))>=6,id+' insufficient explanation')
ck(tasks==set(f'TX-{i:02d}' for i in range(1,11)),'ten Stage0 tasks raw mapped')
ev=tsv(B/'CASE_EVIDENCE.tsv');extra=tsv(B/'R050_NEW_SOURCE_LOCI.tsv');manifest=tsv(B/'CASE_CHUNK_MANIFEST.tsv')
ck(len(ev)==54 and len({x['source_locus'] for x in ev})==54,'evidence count')
ck(len(extra)==33,'new evidence count')
ck(len(manifest)==17 and len({x['chunk_id'] for x in manifest})==17,'chunk count')
ck(loc=={x['source_locus'] for x in ev},'candidate-locus mismatch')
ck(chunk=={x['chunk_id'] for x in manifest},'candidate-chunk mismatch')
evmap={x['source_locus']:x for x in ev}
for x in extra:ck(x['source_locus'] in evmap and x['paragraph_sha256']==evmap[x['source_locus']]['paragraph_sha256'],'new hash mismatch')
with (R/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(meta)==532,'frozen 532 chapters')
arcs=set();seen=set()
for x in ev:
 try:
  m=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert m
  n,p=map(int,m.groups());ref=meta[n];seen.add(n)
  ck(x['epub_path']==ref['epub_path'] and x['chapter_sha256']==ref['chapter_sha256'],'chapter sha/path mismatch')
  ck(1<=p<=int(ref['nonempty_paragraphs']),'paragraph out of range')
  ck(bool(re.fullmatch('[a-f0-9]{64}',x['paragraph_sha256'])),'bad paragraph sha')
  ck(x['case_id'] in links and x['source_locus'] in links[x['case_id']][0],'wrong case ref')
  ck(x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','unexpected B/C')
  arcs.add(1 if n<=80 else 2 if n<=160 else 3 if n<=280 else 4 if n<=400 else 5 if n<=480 else 6)
 except Exception as ex:err.append('bad evidence '+str(ex))
ck(len(seen)==16 and len(arcs)==6,'16 chapters across 6 research arcs')
for x in manifest:
 try:
  n=int(x['narrative_ordinal']);a=int(x['paragraph_start']);b=int(x['paragraph_end']);ref=meta[n];id=x['case_id']
  ck(x['epub_path']==ref['epub_path'] and x['chapter_sha256']==ref['chapter_sha256'],'chunk orig ref')
  ck(1<=a<=b<=int(ref['nonempty_paragraphs']),'bad chunk range')
  ck(id in links and x['chunk_id'] in links[id][1],'chunk ownership')
  ck(any(int(l[1:4])==n and a<=int(l.split('/p')[1])<=b for l in links[id][0]),'chunk has no source anchor')
 except Exception as ex:err.append('chunk error '+str(ex))
report=(B/'CASE_RETRIEVAL_AUDIT.md').read_text(encoding='utf-8')
for token in ['958','532','33,278','2,087,501','16个','54处','17处','33处','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R051','fictional_narrative_case']:
 ck(token in report,'missing audit token '+token)
legacy=tsv(R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(legacy)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in legacy),'quarantine regressed')
c=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf-8'))
number=int(c['current_round'][1:])
ck((c["round_status"]=="NOT_STARTED" or (c["current_round"]=="R057" and c["round_status"]=="BLOCKED" and c["rounds_completed"]==56 and c["last_passed_round"]=="R056" and c.get("cangjie_stage1_5_user_confirm")=="PENDING_R057_USER_APPROVAL")) and ((number==50 and c['rounds_completed']==49) or (number>=51 and c['rounds_completed']==number-1)),'cursor mismatched')
ck((number==50 and c['last_passed_round']=='R049') or (number>=51 and int(c['last_passed_round'][1:])>=50),'R050 not completed before later rounds')
ck(c['cangjie_stage0_gate']=='PASSED' and c['legacy_quality_debt_status']=='OPEN_QUARANTINED','quality gate drift')
ck(c['skill_certified_count']==0 and c['heldout_bank_status']=='SEALED_NOT_RUN' and c['original_output_test_status']=='NOT_RUN','C false promotion')
with (R/'ROUND_LEDGER.csv').open(encoding='utf-8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R050']['status']==('NOT_STARTED' if c['current_round']=='R050' else 'PASSED'),'R050 ledger inconsistency')
if c['current_round']=='R051':ck(ledger['R051']['status']=='NOT_STARTED','R051 started without trigger')
for e in err:print('FAIL:',e)
print('R050','FAIL' if err else 'PASS','SOURCE_STRUCTURE_ONLY 16 fictional RAW cases / 54 local SHA / 17 chunks / six arcs / 10 tasks B_PROVISIONAL C_NOT_RUN')
sys.exit(bool(err))
