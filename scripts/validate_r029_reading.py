#!/usr/bin/env python3
"""R029 public-source/receipt audit; cannot inspect private novels in GitHub Actions."""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base=root/'cangjie/reading/R029'
with (root/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf-8',newline='') as fh: master={int(z['narrative_ordinal']):z for z in csv.DictReader(fh) if z['narrative_ordinal']}
with (base/'wanming_source_index.csv').open(encoding='utf-8',newline='') as fh: sources=list(csv.DictReader(fh))
records=[json.loads(s) for s in (base/'wanming_receipts.jsonl').read_text('utf-8').splitlines() if s.strip()]
focus={441,445,449,452,457,458,459,460,462,464,466,467,469,470,471,472,475,476,477,480}
errors=[]
def ck(cond,note):
 if not cond: errors.append(note)
def digest(strings):
 h=2166136261
 for s in strings:
  for ch in s:
   h=((h^ord(ch))*16777619)&0xffffffff
 return f'{h:08x}'
ck(len(records)==len(sources)==40,'require 40 actual R029 receipts and source records')
ck([r['narrative_ordinal'] for r in records]==list(range(441,481)),'R029 effective ordinals 361..400 incomplete')
ck([int(i['narrative_ordinal']) for i in sources]==list(range(441,481)),'source index ordinal drift')
nb=na=nc=0
sha_l=[]; member_l=[]; claims=[]; events=set()
for r,s in zip(records,sources):
 n=r['narrative_ordinal']; m=master.get(n)
 if not m:errors.append('unknown original ordinal '+str(n));continue
 ck(r['book_slug']=='wanming' and r['source_epub_sha256']=='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082',f'{n}: private original source identification')
 ck(r['spine_index']==int(m['spine_index'])==int(s['spine_index']),f'{n}: OPF spine mismatch')
 ck(r['epub_path']==m['epub_path']==s['epub_path'],f'{n}: original ZIP path mismatch')
 ck(r['chapter_sha256']==m['chapter_sha256']==s['chapter_sha256'],f'{n}: original member SHA mismatch')
 ck(r['body_paragraph_count']==r['observed_paragraph_count']==int(m['nonempty_paragraphs'])==int(s['nonempty_paragraphs']),f'{n}: original paragraph counts')
 close=n in focus
 ck(r['mode']==s['mode']==('CLOSE_READ' if close else 'FULL_TEXT_READ'),f'{n}: reading-mode mismatch')
 ck(r.get('fixture_only') is False and r.get('round_id')=='R029' and len(r.get('reader_session_id',''))>10,f'{n}: reader provenance missing')
 ck(r.get('paragraph_normalization')=='xhtml_visible_text_trim_whitespace_v1',f'{n}: paragraph algorithm changed')
 ck(len(r['event_chain'])==2 and all(isinstance(x,str) and len(x)>20 for x in r['event_chain']),f'{n}: independent scene/agency notes missing')
 ck(r['event_chain'][0] not in events,f'{n}: duplicate narrative note');events.add(r['event_chain'][0])
 ck(bool(r['open_questions']),f'{n}: no uncertainty declared')
 aa=r['anchors']; ck(len(aa)==(3 if close else 1),f'{n}: locator count')
 ck(all(0<a['paragraph_index']<=r['body_paragraph_count'] and re.fullmatch('[0-9a-f]{64}',a['paragraph_sha256']) for a in aa),f'{n}: invalid SHA or index')
 ck(';'.join(f"{a['paragraph_index']}:{a['paragraph_sha256']}" for a in aa)==s['paragraph_sha256_anchors'],f'{n}: recorded source and receipt anchors differ')
 if close:
  nc+=1; ck(len(r['mechanism_claims'])==1,f'{n}: missing close mechanism')
  for c in r['mechanism_claims']:
   claims.append(c)
   ck(c['verification_state']=='PROVISIONAL' and c['counterexample_status'] in ('SEARCHED_NONE','FOUND'),f'{n}: improperly certified mechanism')
   ck(set(c['support_anchor_ids'])<={a['anchor_id'] for a in aa} and c['support_anchor_ids'],f'{n}: unrelated anchor ID')
   ck(len(c['alternative_rendering_loss'])>=35 and len(c['failure_boundary'])>=35 and len(c['counterexample_search_note'])>=35,f'{n}: incomplete literary analysis')
   ck(c['counterexample_status']!='FOUND' or bool(c['counterexample_anchor_ids']),f'{n}: FOUND without real contrary anchor')
 else:ck(not r['mechanism_claims'],f'{n}: unexpected FULL_TEXT_READ claim')
 for a in aa:sha_l.append(f"{n}/{a['paragraph_index']}/{a['paragraph_sha256']}\n")
 member_l.append(f"{n}|{m['spine_index']}|{m['epub_path']}|{m['chapter_sha256']}|{m['nonempty_paragraphs']}\n")
 nb+=r['body_paragraph_count'];na+=len(aa)
ck((nb,nc,na)==(2050,20,80),'paragraph, close study and original locator totals changed')
ck(digest(sha_l)=='fa6c9f60','source paragraph SHA sequence FNV mismatch')
ck(digest(member_l)=='d05bdb81','40 original ZIP metadata SHA sequence FNV mismatch')
ck(len({c['claim_text'] for c in claims})==20 and len({c['failure_boundary'] for c in claims})==20,'reused generic mechanism/failure boundary')
ck(len({c['alternative_rendering_loss'] for c in claims})==20 and len({c['counterexample_search_note'] for c in claims})==20,'copied generic alternative or counterexample')
ck(len({c['aspect'] for c in claims})>=6,'insufficient independent literary dimensions')
for p in ['cangjie/reading/wanming_441_480.md','cangjie/reading/R029/wanming_close_analysis.md','cangjie/reading/R029/wanming_chapter_observations.jsonl','cangjie/reading/R029/wanming_continuity.md','cangjie/reading/R029/LOCAL_SOURCE_VERIFICATION.md','runs/R029.md']:
 ck((root/p).is_file(),'Missing R029 deliverable: '+p)
cursor=json.loads((root/'CURRENT_ROUND.json').read_text('utf-8'))
ordcur=int(cursor['current_round'][1:]);ck(ordcur>=29,'R029 has not been authorized')
if ordcur==29:
 ck(cursor['full_text_read_chapters']=={'wanming':440,'tiexuecanming':440},'R029 counted before formal PASS')
else:
 ck(cursor['full_text_read_chapters']['wanming']>=480 and cursor['full_text_read_chapters']['tiexuecanming']>=440,'R029 formally PASSED original count regressed')
for error in errors:print('FAIL:',error)
if errors:sys.exit(1)
print('PASS R029 PUBLIC SOURCE_STRUCTURE_ONLY: 40 original Wanming 441-480 narrative ordinals, 2050 XHTML paragraphs, 20 close, 80 authentic-source metadata hash locators, '+ 'fa6c9f60' + ' anchored FNV, member FNV d05bdb81; no literary mastery certified')
