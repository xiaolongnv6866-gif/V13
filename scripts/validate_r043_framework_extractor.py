#!/usr/bin/env python3
"""R043 Cangjie framework extractor: original-task coverage & source-only GitHub check.

Public CI cannot certify private EPUB semantics or independent creative-task benefit.
"""
from pathlib import Path
import csv,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
errs=[]
def check(ok,msg):
 if not ok:errs.append(msg)
src=ROOT/'books/wanming/candidates/frameworks.md'
evid=ROOT/'books/wanming/candidates/FRAMEWORK_EVIDENCE.tsv'
report=ROOT/'books/wanming/candidates/FRAMEWORK_SCAN_REPORT.md'
check(src.is_file() and evid.is_file() and report.is_file(),'Stage1 framework outputs missing')
if not (src.is_file() and evid.is_file() and report.is_file()):
 print('FAIL: R043 artifacts missing');sys.exit(1)
text=src.read_text(encoding='utf8')
match=re.search(r'```yaml\n(.*?)\n```',text,re.S)
check(match is not None,'YAML candidate block missing')
yaml=match.group(1) if match else ''
blocks=re.split(r'(?=^- id: f\d+\s*$)',yaml,flags=re.M)
units=[x for x in blocks if x.strip() and re.match(r'^- id: f\d+\s*$',x.splitlines()[0])]
ids=[re.match(r'^- id: (f\d+)',x).group(1) for x in units]
check(len(units)==17,'Original 17 documented frameworks missing')
check(ids==[f'f{i:02}' for i in range(1,18)],'IDs unstable or duplicate')
tasklinks=set(); locs=set(); all_loci=set(); arc_seen=set()
for block in units:
 id_=re.match(r'^- id: (f\d+)',block).group(1)
 for key in ('title','type','source_chapter','source_quote','source_quote_status','source_loci','summary','tags','task_ids','inputs','outputs','steps','missing_conditions','counterexample_or_limit','status','verification_state'):
  check(bool(re.search(r'^  '+key+r':\s*(?:.|$)',block,re.M)),f'{id_} missing field {key}')
 check(re.search(r'^  type: (framework|procedure|troubleshooting)$',block,re.M) is not None,f'{id_} incorrect framework extractor scope')
 check('source_quote: ""' in block and 'COPYRIGHT_OMITTED_PRIVATE_SOURCE_SHA' in block,f'{id_} copyrighted original must be redacted with hash')
 check('RAW_CANDIDATE_B_PROVISIONAL_C_NOT_RUN' in block and 'NOT_STARTED_STAGE1_5' in block,f'{id_} incorrect verification state')
 l=[x for x in re.findall(r'    - "(n\d{3}/p\d+)"',block)]
 check(len(l)>=2,f'{id_} insufficient cited scenes')
 for x in l:
  locs.add(x)
  n=int(x[1:4])
  if n<=51:arc_seen.add('S1')
  elif n<=105:arc_seen.add('S2')
  elif n<=155:arc_seen.add('S3')
  elif n<=271:arc_seen.add('S4')
  elif n<=487:arc_seen.add('S5')
  else:arc_seen.add('S6')
 y=re.search(r'  task_ids: \[([^\]]+)\]',block)
 if y:tasklinks.update(z.strip() for z in y.group(1).split(','))
 steps=block.split('  steps:',1)[-1].split('  missing_conditions:',1)[0]
 check(len(re.findall(r'^    - "',steps,re.M))>=3,f'{id_} procedure lacks three stated writing decisions')
check(tasklinks=={f'WM-{i:02}' for i in range(1,10)},'BOOK_OVERVIEW task coverage not all 9')
check(arc_seen=={f'S{i}' for i in range(1,7)},'One of six OPF narrative arcs missing')
with evid.open(encoding='utf8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
check(len(rows)==57 and len({x['source_locus'] for x in rows})==57,'57 unique original paragraph anchor rows needed')
check({x['source_locus'] for x in rows}==locs,'candidate source references do not match evidence')
with (ROOT/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:
 meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
check(len(meta)==571,'R002 chapter index drift')
for x in rows:
 try:
  ref=x['source_locus']; n,p=(int(v) for v in re.fullmatch(r'n(\d{3})/p(\d+)',ref).groups())
  m=meta[n]
  check(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),ref+' locator mismatch')
  check(1<=p<=int(m['nonempty_paragraphs']),ref+' paragraph out of range')
  check(m['epub_path']==x['epub_path'] and m['chapter_sha256']==x['chapter_sha256'],ref+' source path/chapter hash mismatch')
  check(re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256']) is not None,ref+' invalid paragraph SHA')
  check(x['verification']=='PRIVATE_SHA_VERIFIED_PREVIOUS_OR_R043' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN',ref+' false evidence-certification status')
 except (KeyError,ValueError,AttributeError,TypeError) as e:errs.append('Malformed original locator '+str(e))
scan=report.read_text(encoding='utf8')
for key in ['30,221','2,245,824','571','17个','57个','adabf437c83ffe27b9775e1d787a211c07e31eb3cd3a856030802820f82d4749','模型','PROVISIONAL','NOT_RUN','R044']:
 check(key in scan,'scan execution report missing '+key)
ov=(ROOT/'books/wanming/BOOK_OVERVIEW.md').read_text(encoding='utf8')
check('STAGE0_FRAMEWORK_USER_APPROVED_WITH_LEGACY_DEBT' in ov,'User did not approve Stage0 frame')
for i in range(1,10):check(bool(re.search(r'^\|WM-'+str(i).zfill(2)+r'\|',ov,re.M)),'Book-independent task missing')
q=ROOT/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv'
check(q.is_file(),'R042 legacy gate not available')
if q.is_file():
 with q.open(encoding='utf8',newline='') as f:old=list(csv.DictReader(f,delimiter='\t'))
 check(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'legacy quarantine was removed')
cur=json.loads((ROOT/'CURRENT_ROUND.json').read_text(encoding='utf8'))
check(int(cur['current_round'][1:])>=44 and int(cur['last_passed_round'][1:])>=43 and cur['rounds_completed']>=43,'R043 not formally completed or R044 not entered')
check(cur['cangjie_stage0_gate']=='PASSED' and cur.get('legacy_quality_debt_status')=='OPEN_QUARANTINED','Adler Stage0 or legacy debt state invalid')
if cur['current_round']=='R044':
 check(cur['round_status']=='NOT_STARTED','R044 must not start during R043 run')
 check(cur['skill_certified_count']==0 and cur['heldout_bank_status']=='SEALED_NOT_RUN','Unjustified skill or heldout advancement')
with (ROOT/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
check(ledger['R043']['status']=='PASSED','R043 ledger not PASSED')
if cur['current_round']=='R044':check(ledger['R044']['status']=='NOT_STARTED','R044 prematurely executed')
for x in errs:print('FAIL:',x)
print('R043',('FAIL' if errs else 'PASS'),'17 unverified independent framework candidates / 57 source locators / nine book tasks / six narrative arcs; public SOURCE_STRUCTURE_ONLY, B PROVISIONAL C NOT_RUN')
sys.exit(bool(errs))
