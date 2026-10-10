#!/usr/bin/env python3
"""R051 counterexample source structural integrity; GitHub CI cannot certify novel literary semantics."""
from pathlib import Path
import re,csv,json,sys
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'books/tiexuecanming/candidates';errors=[]
def ck(a,msg):
 if not a:errors.append(msg)
def tsv(path):
 with path.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
text=(B/'counter-examples.md').read_text(encoding='utf8')
start=text.find('- id: ce01');end=text.find('## 反例不是负面情绪',start)
ck(start>=0 and end>start,'YAML start/end missing')
body=text[start:end] if start>=0 and end>start else ''
items=[t for t in re.split(r'(?=^- id: ce\d\d$)',body,flags=re.M) if t.lstrip().startswith('- id: ce')]
ids=[re.search(r'(?m)^- id: (ce\d\d)$',t).group(1) for t in items]
ck(ids==[f'ce{i:02}' for i in range(1,22)],'expected ce01—ce21')
locs=set();chunks=set();task=set();refs={}
required=['title','type','evidence_kind','source_chapter','source_quote','source_quote_status','source_loci','chunk_ids','summary','failure_mode','mechanism','warning_signs','bound_to','observed_status','counterpressure_or_limit','task_ids','tags','source_reality','status','verification_state']
for id,item in zip(ids,items):
 for field in required:ck(bool(re.search(r'(?m)^  '+field+':',item)),id+' missing '+field)
 ck('type: counter-example' in item,id+' extractor type')
 ck('source_quote: ""' in item and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in item,id+' copyright')
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in item and 'NOT_STARTED_STAGE1_5' in item,id+' fake certification')
 ck('FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE' in item,id+' source reality')
 L=set(re.findall(r'^    - "(n\d{3}/p\d+)"',item,re.M));C=set(re.findall(r'^    - "(ck-[a-f0-9]{12})"',item,re.M))
 ck(len(L)>=3 and len(C)>=1,id+' source scene incomplete')
 locs.update(L);chunks.update(C);refs[id]=(L,C)
 m=re.search(r'^  task_ids: \[([^]]+)\]',item,re.M)
 if m:task.update(x.strip() for x in m.group(1).split(','))
 ck(re.search(r'(?m)^  warning_signs:\n    - ',item) is not None,id+' warning_signs not list')
 ck(re.search(r'(?m)^  bound_to:\n    - ',item) is not None,id+' no limitation binding')
ck(task=={f'TX-{i:02}' for i in range(1,11)},'ten independent TX tasks not covered')
ev=tsv(B/'COUNTEREXAMPLE_EVIDENCE.tsv')
new=tsv(B/'R051_NEW_SOURCE_LOCI.tsv');cmanifest=tsv(B/'COUNTEREXAMPLE_CHUNKS.tsv')
ck(len(ev)==67 and len({x['source_locus'] for x in ev})==67,'67 distinct locators')
ck(len(new)==41 and len({x['source_locus'] for x in new})==41,'new hash sample count')
ck(len(cmanifest)==27 and len({(x['counterexample_id'],x['chunk_id']) for x in cmanifest})==27,'27 linked original chunks')
ck(locs=={x['source_locus'] for x in ev},'candidate/source inconsistent')
records={x['source_locus']:x for x in ev}
for x in new:ck(x['source_locus'] in records and x['paragraph_sha256']==records[x['source_locus']]['paragraph_sha256'],'new original hash mismatch')
with (ROOT/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf8',newline='') as f:meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(meta)==532,'frozen OPF count')
arcs=set(); chapters=set()
for x in ev:
 try:
  mt=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert mt
  n,p=map(int,mt.groups());chapters.add(n);m=meta[n]
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),'source coordinates')
  ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],'frozen chapter SHA')
  ck(1<=p<=int(m['nonempty_paragraphs']),'paragraph range')
  ck(bool(re.fullmatch('[a-f0-9]{64}',x['paragraph_sha256'])),'source paragraph SHA')
  ck(x['counterexample_id'] in refs and x['source_locus'] in refs[x['counterexample_id']][0],'wrong case owner')
  ck(x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','B/C not provisional')
  arcs.add(1 if n<=80 else 2 if n<=160 else 3 if n<=280 else 4 if n<=400 else 5 if n<=480 else 6)
 except Exception as e:errors.append('bad original source '+str(e))
ck(len(chapters)==24 and len(arcs)==6,'chapter/arc coverage')
for x in cmanifest:
 try:
  n=int(x['narrative_ordinal']);a=int(x['paragraph_start']);b=int(x['paragraph_end']);m=meta[n];id=x['counterexample_id']
  ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],'chunk source path')
  ck(1<=a<=b<=int(m['nonempty_paragraphs']),'chunk range')
  ck(id in refs and x['chunk_id'] in refs[id][1],'chunk owned by case')
  ck(any(int(y[1:4])==n and a<=int(y.split('/p')[1])<=b for y in refs[id][0]),'chunk has no linked original paragraph')
 except Exception as e:errors.append('bad chunk '+str(e))
legacy=tsv(ROOT/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(legacy)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in legacy),'old claims prematurely promoted')
audit=(B/'COUNTEREXAMPLE_AUDIT.md').read_text(encoding='utf8')
for tok in ['532','33,278','2,087,501','958','21条','67处','24个','27个','41处','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R052']:ck(tok in audit,'report '+tok)
cur=json.loads((ROOT/'CURRENT_ROUND.json').read_text(encoding='utf8'))
number=int(cur['current_round'][1:])
ck((cur["round_status"]=="NOT_STARTED" or (cur["current_round"]=="R057" and cur["round_status"]=="BLOCKED" and cur["rounds_completed"]==56 and cur["last_passed_round"]=="R056" and cur.get("cangjie_stage1_5_user_confirm")=="PENDING_R057_USER_APPROVAL")) and ((number==51 and cur['rounds_completed']==50) or (number>=52 and cur['rounds_completed']==number-1)),'cursor')
ck(cur['skill_certified_count']==0 and cur['heldout_bank_status']=='SEALED_NOT_RUN' and cur['original_output_test_status']=='NOT_RUN','false B/C/skill certification')
ck(cur['legacy_quality_debt_status']=='OPEN_QUARANTINED','old debt cleared without proof')
with (ROOT/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ld={x['id']:x for x in csv.DictReader(f)}
ck(ld['R050']['status']=='PASSED','R050 regression')
ck(ld['R051']['status']==('NOT_STARTED' if number==51 else 'PASSED'),'R051 ledger')
if number==52:ck(ld['R052']['status']=='NOT_STARTED','R052 started')
for e in errors:print('FAIL:',e)
print('R051','FAIL' if errors else 'PASS','21 RAW counterexamples / 67 original private SHA / 27 chunks / 24 chapters / 10 TX / SOURCE_STRUCTURE_ONLY B PROVISIONAL C NOT_RUN')
sys.exit(bool(errors))
