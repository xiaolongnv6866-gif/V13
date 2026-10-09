#!/usr/bin/env python3
"""V13 R046 counter-example extractor: source and candidacy gate, NOT literary B or output C."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1]
BASE=R/'books/wanming/candidates'
err=[]
def ck(condition,reason):
 if not condition:err.append(reason)
def tsv(path):
 with path.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
paths={x:BASE/x for x in ['counter-examples.md','COUNTEREXAMPLE_EVIDENCE.tsv','R046_PRIVATE_SOURCE_SHA.tsv','COUNTEREXAMPLE_CHUNKS.tsv','COUNTEREXAMPLE_AUDIT.md']}
for x in paths.values():ck(x.is_file(),f'missing {x}')
if err:
 print('\n'.join('FAIL '+x for x in err));sys.exit(1)
s=paths['counter-examples.md'].read_text(encoding='utf8')
begin=s.find('- id: ce01');end=s.find('## 原版方法与小说体裁',begin)
ck(begin>=0 and end>begin,'counterexample candidate block missing')
blocks=re.split(r'(?=^- id: ce\d{2}$)',s[begin:end] if begin>=0 and end>begin else '',flags=re.M)
units=[x for x in blocks if x.strip() and x.lstrip().startswith('- id: ce')]
ids=[re.match(r'^- id: (ce\d{2})',x.lstrip()).group(1) for x in units]
ck(ids==[f'ce{i:02}' for i in range(1,20)],'candidate count/ID/order changed')
loci=set(); tasks=set(); chunks=set(); case_sources={}; case_chunks={}; kinds=set()
keys=['title','type','source_chapter','source_quote','source_quote_status','evidence_kind','source_loci','chunk_ids','summary','failure_mode','mechanism','warning_signs','bound_to','task_ids','missing_conditions','status','verification_state','tags']
for unit in units:
 id_=re.match(r'^- id: (ce\d{2})',unit.lstrip()).group(1)
 for key in keys:ck(bool(re.search(r'^  '+key+r':',unit,re.M)),id_+' lacks '+key)
 ck('  type: counter-example' in unit,id_+' outside extractor scope')
 ck('source_quote: ""' in unit and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in unit,id_+' source-quotation provenance not explicit')
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in unit and 'NOT_STARTED_STAGE1_5' in unit,id_+' falsely admitted as verified skill')
 k=re.search(r'^  evidence_kind: (\w+)',unit,re.M)
 if k:kinds.add(k.group(1))
 loc=set(re.findall(r'^    - "(n\d{3}/p\d+)"',unit,re.M))
 ch=set(re.findall(r'^    - "(ck-[0-9a-f]{12})"',unit,re.M))
 ck(len(loc)>=2 and len(ch)>=1,id_+' insufficient original scene or chunk trace')
 loci|=loc;chunks|=ch;case_sources[id_]=loc;case_chunks[id_]=ch
 part=re.search(r'^  task_ids: \[([^\]]+)\]',unit,re.M)
 if part:tasks|={v.strip() for v in part.group(1).split(',')}
 signs=unit.split('  warning_signs:',1)[-1].split('  bound_to:',1)[0]
 ck(len(re.findall(r'^    - "',signs,re.M))>=2,id_+' insufficient specific warning signs')
 ck(len(re.findall(r'^  summary: \|-$',unit,re.M))==1,id_+' missing prose context')
 ck(re.search(r'^  bound_to:\n    - "',unit,re.M) is not None,id_+' missing bounded task')
ck(tasks=={f'WM-{i:02}' for i in range(1,10)},'nine independent Stage0 tasks do not all have raw counterexample candidates')
ck('NARRATOR_HISTORICAL_CLAIM_UNVERIFIED' in kinds and 'CHARACTER_PREDICTED_RISK' in kinds and 'OBSERVED_DISPUTE' in kinds,'observed/projected/narrator evidence kinds not distinguished')
anchor=tsv(paths['COUNTEREXAMPLE_EVIDENCE.tsv'])
hashes=tsv(paths['R046_PRIVATE_SOURCE_SHA.tsv'])
ch_manifest=tsv(paths['COUNTEREXAMPLE_CHUNKS.tsv'])
ck(len(anchor)==62 and len({x['source_locus'] for x in anchor})==62,'62 distinct source lines required')
ck(len(hashes)==62 and len({x['source_locus'] for x in hashes})==62,'62 actual local source SHA receipts required')
ck({x['source_locus'] for x in anchor}==loci,'source citations do not match manuscript')
hmap={x['source_locus']:x['paragraph_sha256'] for x in hashes}
with (R/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:
 spine={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(spine)==571,'narrative spine must remain 571')
chapters=set(); arcs=set()
for x in anchor:
 ref=x['source_locus']
 try:
  m=re.fullmatch(r'n(\d{3})/p(\d+)',ref);assert m
  n,p=map(int,m.groups());source=spine[n];chapters.add(n)
  ck(1<=p<=int(source['nonempty_paragraphs']),'paragraph index out of range: '+ref)
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']), 'reference disagreement '+ref)
  ck(x['epub_path']==source['epub_path'] and x['chapter_sha256']==source['chapter_sha256'],'frozen source chapter mismatch '+ref)
  ck(re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256']) is not None and x['paragraph_sha256']==hmap[ref],'private paragraph hash mismatch '+ref)
  ck(x['source_status']=='PRIVATE_EPUB_SHA_RECHECK' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','B/C certification drift '+ref)
  arcs.add(1 if n<=51 else 2 if n<=105 else 3 if n<=155 else 4 if n<=271 else 5 if n<=487 else 6)
 except (KeyError,ValueError,AssertionError,TypeError) as e:err.append('invalid source '+ref+' '+str(e))
ck(len(chapters)==20 and arcs==set(range(1,7)),'20 actual source chapters across all six arcs required')
ck(len(ch_manifest)==21 and len({x['chunk_id'] for x in ch_manifest})==21,'21 source chunks required')
ck({x['chunk_id'] for x in ch_manifest}==chunks,'selected-source chunk list mismatch')
for x in ch_manifest:
 try:
  cid=x['counterexample_id'];n=int(x['narrative_ordinal']);st=int(x['paragraph_start']);en=int(x['paragraph_end'])
  ck(cid in case_sources and x['chunk_id'] in case_chunks[cid],'chunk referenced by wrong candidate')
  ck(n in spine and 1<=st<=en<=int(spine[n]['nonempty_paragraphs']),'chunk bounds invalid')
  ck(any(int(ref[1:4])==n and st<=int(ref.split('/p')[1])<=en for ref in case_sources[cid]),'chunk lacks cited source position')
 except (KeyError,ValueError,TypeError):err.append('unparseable chunk manifest')
audit=paths['COUNTEREXAMPLE_AUDIT.md'].read_text(encoding='utf8')
for marker in ['571','30,221','2,245,824','848','19','62','21','20','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R047']:
 ck(marker in audit,'audit report missing '+marker)
with (R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv').open(encoding='utf8',newline='') as f:old=list(csv.DictReader(f,delimiter='\t'))
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'14 inherited source failures no longer fenced')
cur=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
ck(int(cur['current_round'][1:])>=47 and int(cur['last_passed_round'][1:])>=46 and cur['rounds_completed']>=46,'R046 formally uncompleted')
if cur['current_round']=='R047':ck(cur['round_status']=='NOT_STARTED' and cur['rounds_completed']==46,'R047 prematurely executed')
ck(cur['cangjie_stage0_gate']=='PASSED' and cur.get('legacy_quality_debt_status')=='OPEN_QUARANTINED','Stage0 or legacy debt falsely cleared')
ck(cur['skill_certified_count']==0 and cur['heldout_bank_status']=='SEALED_NOT_RUN' and cur['original_output_test_status']=='NOT_RUN','unearned Skill or C-test advancement')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R046']['status']=='PASSED','round R046 not in passed ledger')
if cur['current_round']=='R047':ck(ledger['R047']['status']=='NOT_STARTED','R047 ledger advanced early')
for z in err:print('FAIL:',z)
print('R046', 'FAIL' if err else 'PASS','19 raw counterexamples / 62 actual paragraph hashes / 21 indexed source chunks / 20 chapters / six arcs / nine Stage0 tasks; PUBLIC SOURCE_STRUCTURE_ONLY, B PROVISIONAL C NOT_RUN')
sys.exit(bool(err))
