#!/usr/bin/env python3
"""R042 targeted counterevidence: GitHub CI SOURCE_STRUCTURE_ONLY."""
from pathlib import Path
from collections import Counter
import csv,sys,json
R=Path(__file__).resolve().parents[1]
f=R/'cangjie/reading/R042_TARGETED_SOURCE_EVIDENCE.tsv'
with f.open(encoding='utf8',newline='') as h:rows=list(csv.DictReader(h,delimiter='\t'))
errors=[]
def ck(ok,msg):
 if not ok:errors.append(msg)
expected={'R008':8,'R013':6,'R017':5,'R018':5,'R023':7}
loc={'R008':('tiexuecanming',33),'R013':('wanming',143),'R017':('wanming',220),'R018':('tiexuecanming',226),'R023':('wanming',339)}
ck(len(rows)==31 and Counter(x['source_batch'] for x in rows)==expected,'31 locators from 5 batches required')
ck(len({(x['book_slug'],x['narrative_ordinal'],x['paragraph_index']) for x in rows})==len(rows),'duplicate original positions')
meta={}
for book in ('wanming','tiexuecanming'):
 with (R/f'sources/metadata/{book}_v13_spine.csv').open(encoding='utf8',newline='') as h:
  meta[book]={int(x['narrative_ordinal']):x for x in csv.DictReader(h) if x['is_narrative_chapter']=='1'}
for x in rows:
 b,n=loc[x['source_batch']];m=meta[b][n]
 ck(x['book_slug']==b and int(x['narrative_ordinal'])==n,'wrong narrative chapter')
 ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],'R002 source mismatch')
 ck(0<int(x['paragraph_index'])<=int(m['nonempty_paragraphs']) and len(x['paragraph_sha256'])==64,'invalid paragraph locator')
 ck(x['source_check']=='PRIVATE_ORIGINAL_SHA_PASS' and x['literary_status']=='PROVISIONAL_SCOPED','false certainty')
 ck(len(x['scene_observation'])>=12 and len(x['failure_boundary'])>=12,'weak source interpretation')
text=(R/'cangjie/reading/R042_TARGETED_REPAIR.md').read_text(encoding='utf8')
for k in [*expected,'SUPERSEDED_FOR_EXTRACTION','REVISED_PROVISIONAL','REJECTED_OVERCLAIM','NOT_RUN']:
 ck(k in text,'missing audit policy '+k)
cursor=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
ck((cursor['current_round']=='R042' and cursor['round_status']=='BLOCKED' and cursor['rounds_completed']==41) or (cursor['current_round']=='R043' and cursor['round_status']=='NOT_STARTED' and cursor['rounds_completed']==42 and cursor['cangjie_stage0_gate']=='PASSED'),'Stage0 approval cursor inconsistent')
print('R042_TARGETED', 'PASS' if not errors else 'FAIL',len(rows),'original-locator metadata; A SOURCE_STRUCTURE_ONLY / B PROVISIONAL / C NOT_RUN')
for e in errors:print('FAIL:',e)
sys.exit(bool(errors))
