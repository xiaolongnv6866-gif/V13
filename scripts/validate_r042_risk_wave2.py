#!/usr/bin/env python3
"""R042 second wave old-claim risk audit: public source-structure checks only."""
from pathlib import Path
from collections import Counter
import csv,json,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def ck(ok,why):
 if not ok:errors.append(why)
expected={'R009':('wanming',65,4),'R011':('wanming',99,4),'R012':('tiexuecanming',109,4),'R014':('tiexuecanming',153,4),'R016':('tiexuecanming',180,3),'R019':('wanming',265,4),'R020':('tiexuecanming',254,4),'R021':('wanming',305,4),'R022':('tiexuecanming',286,4)}
f=R/'cangjie/reading/R042_RISK_WAVE2_EVIDENCE.tsv'
with f.open(encoding='utf-8',newline='') as z:row=list(csv.DictReader(z,delimiter='\t'))
ck(len(row)==35,"not 35 checked XHTML anchors")
ck(Counter(x['batch'] for x in row)=={k:v[2] for k,v in expected.items()},"missing sample batch")
meta={}
for b in ['wanming','tiexuecanming']:
 with (R/f'sources/metadata/{b}_v13_spine.csv').open(encoding='utf-8',newline='') as fh:
  meta[b]={int(x['narrative_ordinal']):x for x in csv.DictReader(fh) if x['is_narrative_chapter']=='1'}
ck(len({(x['batch'],x['paragraph_index']) for x in row})==len(row),"duplicate anchor")
roles=set()
for x in row:
 b,n,_=expected[x['batch']];m=meta[b][n]
 ck(x['book_slug']==b and int(x['narrative_ordinal'])==n,"wrong source chapter")
 ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],"metadata SHA mismatch")
 ck(0<int(x['paragraph_index'])<=int(m['nonempty_paragraphs']) and len(x['paragraph_sha256'])==64,"invalid paragraph range/hash")
 ck(len(x['source_observation'])>=16 and len(x['boundary'])>=16,"uninformative source summary/boundary")
 ck(x['literary_status']!='VERIFIED',"B cannot be certified from source indices")
 roles.add(x['evidence_role'])
for k in ('PRIOR_WEAK','CORRECTIVE','CONTRARY_LIMIT','LATE_CORRECTIVE'):ck(k in roles,k+' missing')
audit=(R/'cangjie/reading/R042_RISK_WAVE2_AUDIT.md').read_text(encoding='utf8')
for k in [*expected,'LATE_CORRECTIVE','CONFIRMED_NARROW_PROVISIONAL','STAGE0','NOT_RUN','SOURCE_STRUCTURE_ONLY']:
 ck(k in audit,"missing explicit caveat / record: "+k)
cursor=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
pre_commit=cursor['current_round']=='R042' and cursor['round_status']=='BLOCKED' and cursor['last_passed_round']=='R041' and cursor['rounds_completed']==41 and cursor['cangjie_stage0_gate']=='NOT_PASSED'
accepted=cursor['current_round']=='R043' and cursor['round_status']=='NOT_STARTED' and cursor['last_passed_round']=='R042' and cursor['rounds_completed']==42 and cursor['cangjie_stage0_gate']=='PASSED'
ck(pre_commit or accepted,'Stage0 formal user confirmation state inconsistent')
ck(cursor['skill_certified_count']==0,'false SKILL certification')
print('R042 WAVE2',('FAIL' if errors else 'PASS'),'9 source-chapters and 35 anchored scene observations; SOURCE_STRUCTURE_ONLY / B PROVISIONAL / C NOT_RUN')
for x in errors:print('FAIL:',x)
sys.exit(bool(errors))
