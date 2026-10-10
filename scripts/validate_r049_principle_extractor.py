#!/usr/bin/env python3
"""R049 public CI: SOURCE_STRUCTURE_ONLY; no copyrighted source or B/C certification."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1];B=R/'books/tiexuecanming/candidates';errors=[]
def ck(b,msg):
 if not b:errors.append(msg)
def readtsv(f):
 with f.open(encoding='utf8',newline='') as z:return list(csv.DictReader(z,delimiter='\t'))
s=(B/'principles.md').read_text(encoding='utf8')
blocks=re.findall(r'(?ms)^- id: (p\d\d)\n(.*?)(?=^- id: p\d\d\n|^## |\Z)',s)
ck([i for i,_ in blocks]==['p%02d'%i for i in range(1,23)],'22 ordered principle candidates')
loc=set();tasks=set();types=set();orig=set()
for id,body in blocks:
 for key in ['title','type','source_chapter','source_quote','source_quote_status','source_loci','summary','tags','task_ids','provenance','source_observation','rule_scope','counterexample_or_limit','missing_conditions','status','verification_state']:
  ck(bool(re.search(r'^  '+key+r':',body,re.M)),id+' missing '+key)
 loc.update(re.findall(r'^    - "(n\d{3}/p\d+)"',body,re.M))
 match=re.search(r'^  task_ids: \[([^]]+)\]',body,re.M)
 if match:tasks.update(t.strip() for t in match.group(1).split(','))
 match=re.search(r'^  type: (\w+)',body,re.M)
 if match:types.add(match.group(1))
 match=re.search(r'^  provenance: (\w+)',body,re.M)
 if match:orig.add(match.group(1))
 ck('source_quote: ""' in body and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in body,id+' copyright locator')
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in body and 'NOT_STARTED_STAGE1_5' in body,id+' false promotion')
ck(types=={'principle','rule','checklist'},'extractor kinds')
ck({'NARRATIVE_INFERENCE','CHARACTER_NORMATIVE','CHARACTER_LIST'} <= orig,'provenance kinds')
ck(tasks=={'TX-%02d'%i for i in range(1,11)},'ten independent TX tasks')
ev=readtsv(B/'PRINCIPLE_EVIDENCE.tsv');fresh=readtsv(B/'R049_NEW_SOURCE_LOCI.tsv')
ck(len(ev)==51 and len({x['source_locus'] for x in ev})==51,'distinct original evidence')
ck(len(fresh)==15,'new source evidence count')
ck({x['source_locus'] for x in ev}==loc,'source and candidate locus matching')
by={x['source_locus']:x for x in ev}
for x in fresh:ck(x['source_locus'] in by and by[x['source_locus']]['paragraph_sha256']==x['paragraph_sha256'],'new source SHA mismatch')
with (R/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf8',newline='') as f:meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(meta)==532,'frozen 532 narrative chapters')
arcs=set()
for x in ev:
 try:
  z=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert z
  n,p=map(int,z.groups());m=meta[n]
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),'source coordinates')
  ck(m['epub_path']==x['epub_path'] and m['chapter_sha256']==x['chapter_sha256'],'chapter hashes')
  ck(1<=p<=int(m['nonempty_paragraphs']),'paragraph range')
  ck(bool(re.fullmatch('[a-f0-9]{64}',x['paragraph_sha256'])),'paragraph sha format')
  ck(x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','invalid literary status')
  arcs.add(1 if n<=80 else 2 if n<=160 else 3 if n<=280 else 4 if n<=400 else 5 if n<=480 else 6)
 except Exception as e:errors.append('source '+str(e))
ck(arcs==set(range(1,7)),'six source arcs')
report=(B/'PRINCIPLE_SCAN_REPORT.md').read_text(encoding='utf8')
for token in ['532','33,278','2,087,500','22条','51处','15个','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R050']:ck(token in report,'audit token '+token)
old=readtsv(R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'old claim quarantine')
c=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
number=int(c['current_round'][1:])
ck((c["round_status"]=="NOT_STARTED" or (c["current_round"]=="R057" and c["round_status"]=="BLOCKED" and c["rounds_completed"]==56 and c["last_passed_round"]=="R056" and c.get("cangjie_stage1_5_user_confirm") in ("PENDING_R057_USER_APPROVAL","USER_APPROVED_R057_TRIAGE_SCHEME_A_EXECUTION_SCOPE_PENDING"))) and ((number==49 and c['rounds_completed']==48) or (number>=50 and c['rounds_completed']==number-1)),'cursor/round status')
ck((number==49 and c['last_passed_round']=='R048') or (number>=50 and int(c['last_passed_round'][1:])>=49),'R049 never completed before newer rounds')
ck(c['cangjie_stage0_gate']=='PASSED' and c['legacy_quality_debt_status']=='OPEN_QUARANTINED','historical debt')
ck(c['skill_certified_count']==0 and c['original_output_test_status']=='NOT_RUN' and c['heldout_bank_status']=='SEALED_NOT_RUN','C/skills premature')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ld={x['id']:x for x in csv.DictReader(f)}
ck(ld['R049']['status']==('NOT_STARTED' if c['current_round']=='R049' else 'PASSED'),'R049 ledger drift')
if c['current_round']=='R050':ck(ld['R050']['status']=='NOT_STARTED','R050 started')
for x in errors:print('FAIL:',x)
print('R049','FAIL' if errors else 'PASS','SOURCE_STRUCTURE_ONLY: 22 raw candidates 51 SHA loci 15 new across six arcs and 10 tasks B_PROVISIONAL C_NOT_RUN')
sys.exit(bool(errors))
