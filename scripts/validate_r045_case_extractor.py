#!/usr/bin/env python3
"""R045 private fiction case extractor: public structure and frozen state checks only."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1]
root=R/'books/wanming/candidates'
problems=[]
def ck(ok,msg):
 if not ok:problems.append(msg)
paths={k:root/k for k in ['cases.md','CASE_EVIDENCE.tsv','R045_NEW_SOURCE_LOCI.tsv','CASE_CHUNK_MANIFEST.tsv','CASE_RETRIEVAL_AUDIT.md']}
for p in paths.values():ck(p.is_file(),str(p)+' missing')
if problems:
 print('\n'.join(problems));sys.exit(1)
s=paths['cases.md'].read_text(encoding='utf8')
start=s.find('- id: c01');end=s.find('## 类型边界与覆盖缺口',start)
ck(start>=0 and end>start,'case candidate YAML delimiters missing')
chunks=re.split(r'(?=^- id: c\d{2}$)',s[start:end] if start>=0 and end>start else '',flags=re.M)
items=[x for x in chunks if x.strip() and x.lstrip().startswith('- id: c')]
ids=[re.match(r'^- id: (c\d{2})',x.lstrip()).group(1) for x in items]
ck(ids==[f'c{i:02}' for i in range(1,15)],'expected c01-c14, no missing/duplicates')
all_loci=set();all_chunks=set();tasks=set();case_map={}
required=['title','type','example_kind','source_reality','example_kind_extension_status','source_chapter','source_quote','source_quote_status','source_loci','chunk_ids','summary','bound_to','outcome','outcome_scope','counterpressure_or_limit','task_ids','tags','status','verification_state']
for item in items:
 ident=re.match(r'^- id: (c\d{2})',item.lstrip()).group(1)
 for key in required:ck(bool(re.search(r'^  '+key+r':',item,re.M)),ident+' missing '+key)
 ck(bool(re.search(r'^  type: case$',item,re.M)),ident+' wrong extractor category')
 ck('example_kind: fictional_narrative_case' in item and 'FICTIONAL_NOVEL_SCENE_NOT_HISTORICAL_EVIDENCE' in item,ident+' false real case claim')
 ck('REQUIRES_STAGE1_5_REVIEW' in item and 'NOT_STARTED_STAGE1_5' in item,ident+' original enum extension unreviewed')
 ck('source_quote: ""' in item and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in item,ident+' copyrighted text handling')
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in item,ident+' wrongly promoted')
 locus=re.findall(r'^    - "(n\d{3}/p\d+)"',item,re.M)
 chunkids=re.findall(r'^    - "(ck-[0-9a-f]{12})"',item,re.M)
 ck(len(locus)>=2 and len(chunkids)>=1,ident+' lacks scene evidence/chunk')
 all_loci.update(locus);all_chunks.update(chunkids);case_map[ident]=(set(locus),set(chunkids))
 task=re.search(r'^  task_ids: \[([^\]]+)\]',item,re.M)
 if task:tasks.update(q.strip() for q in task.group(1).split(','))
 summary=item.split('  summary: |-',1)[-1].split('  bound_to:',1)[0]
 ck(len([v for v in summary.splitlines() if v.startswith('    ')])>=5,ident+' insufficient outcome/limits')
 ck(re.search(r'^  bound_to:\n    - "',item,re.M) is not None,ident+' case not tied to method theme')
 outcome=re.search(r'^  outcome: (.+)',item,re.M)
 ck(outcome is not None and len(outcome.group(1))>15,ident+' cannot certify unexplained outcome')
ck(tasks=={f'WM-{i:02}' for i in range(1,10)},'all nine Stage0 independent tasks require raw case mapping')
with paths['CASE_EVIDENCE.tsv'].open(encoding='utf8',newline='') as f:ev=list(csv.DictReader(f,delimiter='\t'))
with paths['R045_NEW_SOURCE_LOCI.tsv'].open(encoding='utf8',newline='') as f:added=list(csv.DictReader(f,delimiter='\t'))
with paths['CASE_CHUNK_MANIFEST.tsv'].open(encoding='utf8',newline='') as f:manifest=list(csv.DictReader(f,delimiter='\t'))
ck(len(ev)==45 and len({x['source_locus'] for x in ev})==45,'45 distinct source SHA loci required')
ck(all_loci=={x['source_locus'] for x in ev},'case loci/evidence mismatch')
ck(len(added)==16 and len({x['source_locus'] for x in added})==16,'16 source rechecks required')
lookup={x['source_locus']:x for x in ev}
for row in added:ck(row['source_locus'] in lookup and lookup[row['source_locus']]['paragraph_sha256']==row['paragraph_sha256'],'private source SHA changed')
ck(len(manifest)==17 and len({x['chunk_id'] for x in manifest})==17,'17 source chunks expected')
ck({x['chunk_id'] for x in manifest}==all_chunks,'candidate chunks do not match indexed selection')
ck({x['case_id'] for x in manifest}==set(ids),'chunk/case association missing')
with (R/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:
 meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(meta)==571,'R002 original OPF drift')
arcs=set();chapters=set()
for x in ev:
 try:
  mt=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert mt
  n,p=map(int,mt.groups());m=meta[n];chapters.add(n)
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),x['source_locus']+' incorrect coordinate')
  ck(1<=p<=int(m['nonempty_paragraphs']),x['source_locus']+' paragraph out of bounds')
  ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],x['source_locus']+' original source path/sha changed')
  ck(bool(re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256'])),x['source_locus']+' invalid paragraph hash')
  ck(x['source_status']=='PRIVATE_SOURCE_SHA_WITH_PUBLIC_STRUCTURE_CHECK' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN',x['source_locus']+' incorrect A/B distinction')
  arcs.add(1 if n<=51 else 2 if n<=105 else 3 if n<=155 else 4 if n<=271 else 5 if n<=487 else 6)
 except (AssertionError,KeyError,ValueError,TypeError) as exc:problems.append('incorrect source locator '+str(exc))
ck(len(chapters)==16 and arcs==set(range(1,7)),'16 chapters across six arcs required')
for c in manifest:
 try:
  n=int(c['narrative_ordinal']);a=int(c['paragraph_start']);b=int(c['paragraph_end'])
  ck(n in meta and 1<=a<=b<=int(meta[n]['nonempty_paragraphs']),'chunk paragraph range invalid')
  ck(any(re.fullmatch(r'n(\d{3})/p(\d+)',loc) and int(loc[1:4])==n and a<=int(loc.split('/p')[1])<=b for loc in case_map[c['case_id']][0]),'chunk not actually supporting claimed paragraph')
  ck(c['chunk_id'] in case_map[c['case_id']][1],'chunk/case mismatch')
 except (KeyError,TypeError,ValueError):problems.append('incorrect chunk manifest record')
audit=paths['CASE_RETRIEVAL_AUDIT.md'].read_text(encoding='utf8')
for marker in ['848','571','30,221','2,245,824','45','16','14','worked_example','fictional_narrative_case','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R046']:
 ck(marker in audit,'provenance/exception note missing '+marker)
with (R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv').open(encoding='utf8',newline='') as f:old=list(csv.DictReader(f,delimiter='\t'))
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'old legacy literary debt must remain fenced')
cur=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
ck(int(cur['current_round'][1:])>=46 and int(cur['last_passed_round'][1:])>=45 and cur['rounds_completed']>=45,'R045 not formally completed')
if cur['current_round']=='R046':ck(cur['round_status']=='NOT_STARTED' and cur['rounds_completed']==45,'R046 started in R045 turn')
ck(cur['cangjie_stage0_gate']=='PASSED' and cur.get('legacy_quality_debt_status')=='OPEN_QUARANTINED','Stage0/legacy source gate not preserved')
ck(cur['skill_certified_count']==0 and cur['heldout_bank_status']=='SEALED_NOT_RUN' and cur['original_output_test_status']=='NOT_RUN','unjustified literary/creative certification')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R045']['status']=='PASSED','R045 ledger has not passed')
if cur['current_round']=='R046':ck(ledger['R046']['status']=='NOT_STARTED','R046 prematurely executed')
for error in problems:print('FAIL:',error)
print('R045', 'FAIL' if problems else 'PASS','14 fictional-case raw candidates / 45 original source positions / 17 private chunk IDs / WM01-09 raw coverage / six arcs; SOURCE_STRUCTURE_ONLY B PROVISIONAL C NOT_RUN')
sys.exit(bool(problems))
