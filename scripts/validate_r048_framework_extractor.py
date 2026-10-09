#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,sys
P=Path(__file__).resolve().parents[1]
base=P/'books/tiexuecanming/candidates'
issues=[]
def ck(ok,msg):
 if not ok: issues.append(msg)
def read(path):
 with open(path,encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
candidate=(base/'frameworks.md').read_text()
items=re.findall(r'^- id: (f[0-9][0-9])$',candidate,re.M)
ck(items==[f'f{i:02}' for i in range(1,18)],'framework IDs')
required=['title','type','source_chapter','source_quote','summary','tags','task_ids','inputs','outputs','steps','missing_conditions','counterexample_or_limit','source_loci']
task=set();loci=set()
for match in re.finditer(r'^- id: f[0-9][0-9]$',candidate,re.M):
 block=candidate[match.start():]
 end=re.search(r'(?m)^- id: f[0-9][0-9]$|^## 覆盖审计',block[8:])
 if end:block=block[:end.start()+8]
 for key in required:ck(bool(re.search(r'^  '+key+r':',block,re.M)),items[0]+' missing '+key)
 ck('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in block,'uncertified status missing')
 loci.update(re.findall(r'^    - "(n[0-9]{3}/p[0-9]+)"',block,re.M))
 x=re.search(r'^  task_ids: \[([^\]]+)\]',block,re.M)
 if x:task.update(z.strip() for z in x.group(1).split(','))
ck(task=={f'TX-{i:02}' for i in range(1,11)},'TX task coverage')
records=read(base/'FRAMEWORK_EVIDENCE.tsv')
ck(len(records)==52 and len({x['source_locus'] for x in records})==52,'52 distinct source locators')
ck(loci=={x['source_locus'] for x in records},'source locator consistency')
with (P/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:
 meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(meta)==532,'frozen 532 chapters')
seen=set(); arcs=set()
for x in records:
 try:
  n,p=map(int,x['source_locus'][1:].split('/p'));m=meta[n];seen.add(n)
  ck(m['epub_path']==x['epub_path'] and m['chapter_sha256']==x['chapter_sha256'],'source sha/path')
  ck(1<=p<=int(m['nonempty_paragraphs']),'paragraph boundary')
  ck(bool(re.fullmatch('[a-f0-9]{64}',x['paragraph_sha256'])),'paragraph sha')
  ck(x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','evidence quality status')
  arcs.add(1 if n<=80 else 2 if n<=160 else 3 if n<=280 else 4 if n<=400 else 5 if n<=480 else 6)
 except Exception:issues.append('malformed original source')
ck(len(seen)==35 and len(arcs)==6,'chapter/arc spread')
report=(base/'FRAMEWORK_SCAN_REPORT.md').read_text()
for marker in ['532','33,278','2,087,501','17个','52处','35个','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R049']:
 ck(marker in report,'report '+marker)
legacy=read(P/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(legacy)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in legacy),'legacy debt')
c=json.loads((P/'CURRENT_ROUND.json').read_text())
ck(int(c['current_round'][1:])>=49 and c['rounds_completed']>=48 and int(c['last_passed_round'][1:])>=48,'R048 cursor')
ck(c['cangjie_stage0_gate']=='PASSED' and c['legacy_quality_debt_status']=='OPEN_QUARANTINED','quality gate')
ck(c['skill_certified_count']==0 and c['original_output_test_status']=='NOT_RUN','no premature certification')
with (P/'ROUND_LEDGER.csv').open(encoding='utf-8',newline='') as f: ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R048']['status']=='PASSED','R048 ledger')
if c['current_round']=='R049':ck(c['round_status']=='NOT_STARTED' and ledger['R049']['status']=='NOT_STARTED','R049 not started')
for x in issues: print('FAIL:',x)
print('R048', 'FAIL' if issues else 'PASS','SOURCE_STRUCTURE_ONLY')
sys.exit(bool(issues))
