#!/usr/bin/env python3
"""R044 principles: source-structure CI, not semantic B or creative C certification."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1]
problems=[]
def check(ok,reason):
 if not ok:problems.append(reason)
paths=[R/'books/wanming/candidates'/x for x in ['principles.md','PRINCIPLE_EVIDENCE.tsv','R044_NEW_SOURCE_LOCI.tsv','PRINCIPLE_SCAN_REPORT.md']]
for f in paths:check(f.is_file(),str(f)+' absent')
if problems:print(problems);sys.exit(1)
s=paths[0].read_text(encoding='utf8')
start=s.find('- id: p01')
end=s.find('## 未形成数学公式',start)
check(start>=0 and end>start,'YAML block boundary')
blocks=re.split(r'(?=^- id: p\d\d\s*$)',s[start:end] if start>=0 and end>start else '',flags=re.M)
units=[v for v in blocks if v.strip() and v.lstrip().startswith('- id: p')]
ids=[re.match(r'^- id: (p\d\d)',x.lstrip()).group(1) for x in units]
check(ids==[f'p{i:02}' for i in range(1,24)],'23 principle IDs expected')
tasks=set();locs=set();kinds=set();origins=set()
for unit in units:
 id_=re.match(r'^- id: (p\d\d)',unit.lstrip()).group(1)
 for key in ['title','type','source_chapter','source_quote','source_quote_status','source_loci','summary','tags','task_ids','provenance','source_observation','rule_scope','counterexample_or_limit','missing_conditions','status','verification_state']:
  check(bool(re.search(r'^  '+key+r':',unit,re.M)),id_+' '+key+' missing')
 typ=re.search(r'^  type: (\S+)',unit,re.M)
 if typ:kinds.add(typ.group(1))
 prov=re.search(r'^  provenance: (\S+)',unit,re.M)
 if prov:origins.add(prov.group(1))
 check('source_quote: ""' in unit and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in unit,id_+' citation policy')
 check('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in unit and 'NOT_STARTED_STAGE1_5' in unit,id_+' prematurely certified')
 locs.update(re.findall(r'^    - "(n\d{3}/p\d+)"',unit,re.M))
 mt=re.search(r'^  task_ids: \[([^\]]+)\]',unit,re.M)
 if mt:tasks.update(x.strip() for x in mt.group(1).split(','))
 summary=unit.split('  summary: |-',1)[-1].split('  tags:',1)[0]
 check(len([x for x in summary.splitlines() if x.startswith('    ')])>=5,id_+' insufficient provenance summary')
check(kinds=={'principle','rule','checklist'},'wrong extractor classes')
check({'CHARACTER_NORMATIVE','NARRATIVE_INFERENCE','CHARACTER_LIST'} <= origins,'claim-origin missing')
check(tasks=={f'WM-{i:02}' for i in range(1,10)},'all WM tasks must be covered')
with paths[1].open(encoding='utf8',newline='') as f:ev=list(csv.DictReader(f,delimiter='\t'))
with paths[2].open(encoding='utf8',newline='') as f:extra=list(csv.DictReader(f,delimiter='\t'))
check(len(ev)==39 and len({x['source_locus'] for x in ev})==39,'39 distinct source locations')
check(len(extra)==14 and len({x['source_locus'] for x in extra})==14,'14 direct source rechecks')
check({x['source_locus'] for x in ev}==locs,'candidate locators differ from evidence')
known={x['source_locus']:x for x in ev}
for x in extra:check(x['source_locus'] in known and known[x['source_locus']]['paragraph_sha256']==x['paragraph_sha256'],'R044 extra source hash mismatch')
with (R/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:
 meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
check(len(meta)==571,'R002 source metadata drift')
arcs=set()
for x in ev:
 try:
  mt=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus'])
  assert mt is not None
  n,p=map(int,mt.groups());m=meta[n]
  check(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),'source coordinate mismatch')
  check(1<=p<=int(m['nonempty_paragraphs']),'paragraph range mismatch')
  check(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],'chapter source SHA mismatch')
  check(bool(re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256'])),'source paragraph SHA format')
  check(x['verification']=='PRIVATE_ORIGINAL_SHA_ANCHORED' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','false source or literary certification')
  arcs.add(1 if n<=51 else 2 if n<=105 else 3 if n<=155 else 4 if n<=271 else 5 if n<=487 else 6)
 except (AssertionError,KeyError,TypeError,ValueError) as e:problems.append('unreadable paragraph source '+str(e))
check(arcs==set(range(1,7)),'all six narratives must be represented')
report=paths[3].read_text(encoding='utf8')
for v in ['571','30,221','2,245,824','23条','39处','14个','PROVISIONAL','NOT_RUN','SOURCE_STRUCTURE_ONLY']:
 check(v in report,'scan report missing '+v)
with (R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv').open(encoding='utf8',newline='') as f:prior=list(csv.DictReader(f,delimiter='\t'))
check(len(prior)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in prior),'old claims no longer quarantined')
cur=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
check(int(cur['current_round'][1:])>=45 and int(cur['last_passed_round'][1:])>=44 and cur['rounds_completed']>=44,'R044 has not passed or cursor regressed')
if cur['current_round']=='R045':check(cur['round_status']=='NOT_STARTED' and cur['rounds_completed']==44,'R045 improperly started during R044')
check(cur['cangjie_stage0_gate']=='PASSED' and cur['legacy_quality_debt_status']=='OPEN_QUARANTINED','historic approval or quality debt corrupted')
check(cur['skill_certified_count']==0 and cur['original_output_test_status']=='NOT_RUN' and cur['heldout_bank_status']=='SEALED_NOT_RUN','skill/heldout prematurely certified')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
check(ledger['R044']['status']=='PASSED','R044 not PASSED in ledger')
if cur['current_round']=='R045':check(ledger['R045']['status']=='NOT_STARTED','R045 started during R044')
for x in problems:print('FAIL:',x)
print('R044', 'FAIL' if problems else 'PASS','23 raw principles / 39 source locations / 14 novel SHA / WM01-09 and six arcs; SOURCE_STRUCTURE_ONLY B PROVISIONAL C NOT_RUN')
sys.exit(bool(problems))
