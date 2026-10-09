#!/usr/bin/env python3
"""R035 final 11 original Wanming narrative chapters; private EPUB required to prove actual text SHA.
CI validates structure and R002 source metadata ONLY. A=SOURCE_STRUCTURE_ONLY on CI, B=PROVISIONAL, C=NOT_RUN.
"""
import argparse,csv,hashlib,json,re,sys,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1]; BASE=R/'cangjie/reading/R035'
EPUB='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
with (R/'sources/metadata/wanming_v13_spine.csv').open(newline='',encoding='utf-8') as f:
 master={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['narrative_ordinal']}
with (BASE/'wanming_source_index.csv').open(newline='',encoding='utf-8') as f:index=list(csv.DictReader(f))
receipts=[json.loads(s) for s in (BASE/'wanming_receipts.jsonl').read_text('utf8').splitlines() if s.strip()]
notes=[json.loads(s) for s in (BASE/'wanming_chapter_observations.jsonl').read_text('utf8').splitlines() if s.strip()]
stat=json.loads((BASE/'STUDY_STATS.json').read_text('utf8'))
errors=[]
def ck(x,msg):
 if not x:errors.append(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def fnv(ss):
 h=2166136261
 for s in ss:
  for char in s:h=((h^ord(char))*16777619)&0xffffffff
 return f'{h:08x}'
expect=list(range(561,572))
ck(len(receipts)==len(index)==len(notes)==11,'11 actual full-source chapter receipts missing')
ck([x['narrative_ordinal'] for x in receipts]==expect,'wrong 11 narrative ordinals in receipts')
ck([int(x['narrative_ordinal']) for x in index]==expect,'wrong index ordinals')
ck([x['narrative_ordinal'] for x in notes]==expect,'wrong observation ordinals')
ck(master[561]['epub_path']=='OEBPS/Text/Chapter_0574.xhtml' and master[571]['epub_path']=='OEBPS/Text/Chapter_0584.xhtml','wrong OPF last chapter')
paragraphs=claims=anchors=cross=0;mstr=[];astr=[];aspects=set();evs=set()
for r,s,o in zip(receipts,index,notes):
 n=r['narrative_ordinal'];m=master[n]
 ck(r['book_slug']=='wanming' and r['source_epub_sha256']==EPUB,str(n)+' original book/source SHA mismatch')
 ck(r['spine_index']==int(s['spine_index'])==int(m['spine_index'])==n+16,str(n)+' spine mismatch')
 ck(r['epub_path']==s['epub_path']==m['epub_path']==f'OEBPS/Text/Chapter_{n+13:04d}.xhtml',str(n)+' original XHTML member mismatch')
 ck(r['chapter_sha256']==s['chapter_sha256']==m['chapter_sha256'],str(n)+' original member SHA mismatch')
 ck(r['body_paragraph_count']==r['observed_paragraph_count']==int(s['nonempty_paragraphs'])==int(m['nonempty_paragraphs']),str(n)+' paragraph count mismatch')
 ck(r['mode']==s['mode']=='CLOSE_READ' and r['round_id']=='R035' and r['fixture_only'] is False,str(n)+' invalid read type')
 ck(r['paragraph_normalization']=='xhtml_visible_text_trim_whitespace_v1' and len(r['reader_session_id'])>10,str(n)+' invalid provenance')
 ck(len(r['event_chain'])==2 and all(len(v)>40 for v in r['event_chain']) and len(r['open_questions'])==1 and len(r['open_questions'][0])>25,str(n)+' shallow independent reading')
 ck(r['event_chain'][0] not in evs,str(n)+' duplicate event notes');evs.add(r['event_chain'][0])
 ck(o['observed_event']==r['event_chain'][0] and o['independent_choice']==r['event_chain'][1] and o['open_question']==r['open_questions'][0] and o['literary_status']=='PROVISIONAL',str(n)+' observation mismatch')
 own=[a for a in r['anchors'] if not a.get('source_ref')]
 ck(len(own)==3 and own[0]['paragraph_index']==1 and own[-1]['paragraph_index']==r['body_paragraph_count'],str(n)+' false first-to-last paragraph anchors')
 ck(';'.join(str(a['paragraph_index'])+':'+a['paragraph_sha256'] for a in own)==s['paragraph_sha256_anchors'],str(n)+' paragraph index SHA mismatch')
 ck(len(r['mechanism_claims'])==1,str(n)+' exactly one independently grounded close study required')
 for c in r['mechanism_claims']:
  claims+=1;aspects.add(c['aspect'])
  ck(c['verification_state']=='PROVISIONAL' and c['counterexample_status'] in ('FOUND','SEARCHED_NONE'),str(n)+' B improperly certified')
  ck(len(c['claim_text'])>50 and all(len(c[k])>40 for k in ('alternative_rendering_loss','failure_boundary','counterexample_search_note')),str(n)+' shallow close reading')
  ck(c['support_anchor_ids']==[own[1]['anchor_id']],str(n)+' claim anchor unrelated to scene')
  if c['counterexample_status']=='FOUND':
   cross+=1
   ck(len(c['counterexample_anchor_ids'])==1 and any(a.get('source_ref') and a['anchor_id']==c['counterexample_anchor_ids'][0] for a in r['anchors']),str(n)+' invalid FOUND opposite original')
  else:ck(not c['counterexample_anchor_ids'],str(n)+' invented contrary anchor')
 for a in r['anchors']:
  ref=a.get('source_ref');target=master[ref['narrative_ordinal']] if ref else m
  ck(1<=a['paragraph_index']<=int(target['nonempty_paragraphs']) and re.fullmatch(r'[a-f0-9]{64}',a['paragraph_sha256']) is not None,str(n)+' invalid anchor')
  if ref:ck(ref['book_slug']=='wanming' and ref['epub_path']==target['epub_path'] and ref['chapter_sha256']==target['chapter_sha256'],str(n)+' source_ref not authentic')
  astr.append(f'{n}/{ref["narrative_ordinal"] if ref else n}/{a["paragraph_index"]}/{a["paragraph_sha256"]}\n');anchors+=1
 mstr.append(f'{n}|{m["spine_index"]}|{m["epub_path"]}|{m["chapter_sha256"]}|{m["nonempty_paragraphs"]}\n');paragraphs+=r['body_paragraph_count']
ck((paragraphs,claims,anchors,cross)==(731,11,35,2),f'wrong coverage numbers: {paragraphs},{claims},{anchors},{cross}')
ck(len(aspects)>=7,'all literary close claims use same technique')
ck(stat['original_member_fnv']==fnv(mstr)=='424a2d84','original member aggregate invalid')
ck(stat['paragraph_anchor_fnv']==fnv(astr)=='e7521f1b','paragraph SHA aggregate invalid')
for name in ('cangjie/reading/wanming_561_571.md','cangjie/reading/R035/wanming_close_analysis.md','cangjie/reading/R035/wanming_continuity.md','cangjie/reading/R035/CONTENT_QUALITY_AUDIT.md','cangjie/reading/R035/FULL_BOOK_COVERAGE_AUDIT.md','cangjie/reading/R035/LOCAL_SOURCE_VERIFICATION.md','runs/R035.md'):
 ck((R/name).is_file(),'required artifact missing '+name)
cur=json.loads((R/'CURRENT_ROUND.json').read_text('utf8'))
if cur['current_round']=='R035':ck(cur['full_text_read_chapters']=={'wanming':560,'tiexuecanming':532},'advanced reads before formal PASS')
else:ck(cur['full_text_read_chapters']['wanming']>=571 and cur['full_text_read_chapters']['tiexuecanming']>=532,'official book reads regress')
for e in errors:print('FAIL',e)
if errors:sys.exit(1)
print(f'PASS R035 PUBLIC SOURCE_STRUCTURE_ONLY {paragraphs} paragraphs, {claims} close scenes, {anchors} private-SHA locators, {cross} genuine source_ref contrary studies')
parser=argparse.ArgumentParser();parser.add_argument('--source-dir',type=Path);args=parser.parse_args()
if args.source_dir:
 from lxml import html
 candidates=list(args.source_dir.glob('晚明*.epub'))
 if len(candidates)!=1:sys.exit('FAIL private original source EPUB missing or ambiguous')
 if sha(candidates[0].read_bytes())!=EPUB:sys.exit('FAIL private original EPUB SHA mismatch')
 with zipfile.ZipFile(candidates[0]) as archive:
  if archive.testzip() is not None:sys.exit('FAIL original EPUB ZIP CRC')
  for r in receipts:
   original=master[r['narrative_ordinal']];raw=archive.read(original['epub_path'])
   if sha(raw)!=r['chapter_sha256']:sys.exit('FAIL actual original member SHA')
   ps=[s for node in html.fromstring(raw).xpath('//body//p') if (s:=node.text_content().strip())]
   if len(ps)!=r['body_paragraph_count']:sys.exit('FAIL private paragraph full count')
   for a in r['anchors']:
    ref=a.get('source_ref');p=master[ref['narrative_ordinal']] if ref else original
    if ref:pbs=[s for node in html.fromstring(archive.read(p['epub_path'])).xpath('//body//p') if(s:=node.text_content().strip())]
    else:pbs=ps
    if sha(pbs[a['paragraph_index']-1].encode())!=a['paragraph_sha256']:sys.exit(f'FAIL original paragraph n={r["narrative_ordinal"]} {a["anchor_id"]}')
 print('PASS R035 PRIVATE ORIGINAL EPUB SHA, 11 authentic XHTML members and 35 exact paragraph SHA anchors; literary B PROVISIONAL; original creative C NOT_RUN')
