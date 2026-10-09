#!/usr/bin/env python3
"""R034 actual original last twelve narrative chapters, public structural + private byte audit.
Public CI has no user copyrighted original; A=SOURCE_STRUCTURE_ONLY there.
With --source-dir, validate EPUB whole-SHA and ALL original 12 XHTML members plus 38 paragraph anchors.
B literary interpretation PROVISIONAL; C independent original-skills test NOT_RUN.
"""
import argparse,csv,hashlib,json,re,sys,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1]; BASE=R/'cangjie/reading/R034'
EPUB='9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf'
with (R/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf8',newline='') as f:master={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['narrative_ordinal']}
with (BASE/'tiexue_source_index.csv').open(encoding='utf8',newline='') as f:index=list(csv.DictReader(f))
receipts=[json.loads(s) for s in (BASE/'tiexue_receipts.jsonl').read_text(encoding='utf8').splitlines() if s.strip()]
observations=[json.loads(s) for s in (BASE/'tiexue_chapter_observations.jsonl').read_text(encoding='utf8').splitlines() if s.strip()]
stats=json.loads((BASE/'STUDY_STATS.json').read_text('utf8'))
errors=[]
def ck(ok,msg):
 if not ok:errors.append(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def fnv(ss):
 h=2166136261
 for s in ss:
  for ch in s:h=((h^ord(ch))*16777619)&0xffffffff
 return f'{h:08x}'
ck(len(receipts)==len(index)==len(observations)==12,'exactly 12 original full reading receipts required')
ck([x['narrative_ordinal'] for x in receipts]==list(range(521,533)),'narrative chapter IDs incomplete')
ck([int(x['narrative_ordinal']) for x in index]==list(range(521,533)),'source index missing required chapter')
ck([x['narrative_ordinal'] for x in observations]==list(range(521,533)),'observations missing chapter')
ck(master[521]['epub_path']=='OEBPS/Text/chapter530.html' and master[532]['epub_path']=='OEBPS/Text/chapter541.html','printed titles incorrectly used as IDs')
paragraphs=claims=anchors=cross=0;mm=[];aa=[];unique=set();aspects=set()
for receipt,src,obs in zip(receipts,index,observations):
 n=receipt['narrative_ordinal'];m=master[n]
 ck(receipt['book_slug']=='tiexuecanming' and receipt['source_epub_sha256']==EPUB,str(n)+' original book SHA drift')
 ck(receipt['spine_index']==int(src['spine_index'])==int(m['spine_index'])==n+17,str(n)+' spine mismatch')
 ck(receipt['epub_path']==src['epub_path']==m['epub_path']==f'OEBPS/Text/chapter{n+9}.html',str(n)+' OPF path mismatch')
 ck(receipt['chapter_sha256']==src['chapter_sha256']==m['chapter_sha256'],str(n)+' original member SHA drift')
 ck(receipt['body_paragraph_count']==receipt['observed_paragraph_count']==int(src['nonempty_paragraphs'])==int(m['nonempty_paragraphs']),str(n)+' paragraph count drift')
 ck(receipt['mode']==src['mode']=='CLOSE_READ' and receipt['round_id']=='R034' and receipt['fixture_only'] is False,str(n)+' invalid read type')
 ck(len(receipt['reader_session_id'])>10 and receipt['paragraph_normalization']=='xhtml_visible_text_trim_whitespace_v1',str(n)+' provenance/normalization missing')
 ck(len(receipt['event_chain'])==2 and all(len(s)>35 for s in receipt['event_chain']) and len(receipt['open_questions'])==1 and len(receipt['open_questions'][0])>25,str(n)+' shallow chapter-specific observation')
 ck(receipt['event_chain'][0] not in unique,str(n)+' duplicate generic observation');unique.add(receipt['event_chain'][0])
 ck(obs['observed_event']==receipt['event_chain'][0] and obs['independent_choice']==receipt['event_chain'][1] and obs['open_question']==receipt['open_questions'][0] and obs['literary_status']=='PROVISIONAL',str(n)+' independent observation mismatch')
 own=[a for a in receipt['anchors'] if not a.get('source_ref')]
 ck(len(own)==3 and own[0]['paragraph_index']==1 and own[-1]['paragraph_index']==receipt['body_paragraph_count'],str(n)+' false full coverage anchors')
 ck(';'.join(str(a['paragraph_index'])+':'+a['paragraph_sha256'] for a in own)==src['paragraph_sha256_anchors'],str(n)+' paragraph original SHA anchors/index drift')
 ck(len(receipt['mechanism_claims'])==1,str(n)+' one actual close claim required')
 for c in receipt['mechanism_claims']:
  aspects.add(c['aspect']); claims+=1
  ck(c['verification_state']=='PROVISIONAL' and c['counterexample_status'] in('FOUND','SEARCHED_NONE'),str(n)+' B prematurely upgraded or counter status invalid')
  ck(len(c['claim_text'])>45 and all(len(c[x])>40 for x in('alternative_rendering_loss','failure_boundary','counterexample_search_note')),str(n)+' shallow claim alternatives or boundaries')
  ck(c['support_anchor_ids']==[own[1]['anchor_id']],str(n)+' unsupported mid-scene claim')
  if c['counterexample_status']=='FOUND':
   cross+=1;ck(len(c['counterexample_anchor_ids'])==1 and any(a['anchor_id']==c['counterexample_anchor_ids'][0] and a.get('source_ref') for a in receipt['anchors']),str(n)+' false FOUND claim')
  else:ck(not c['counterexample_anchor_ids'],str(n)+' fabricated contrary anchor')
 for x in receipt['anchors']:
  ref=x.get('source_ref');target=master[ref['narrative_ordinal']] if ref else m
  ck(0<x['paragraph_index']<=int(target['nonempty_paragraphs']) and re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256']) is not None,str(n)+' invalid original paragraph locator')
  if ref:ck(ref['book_slug']=='tiexuecanming' and ref['epub_path']==target['epub_path'] and ref['chapter_sha256']==target['chapter_sha256'],str(n)+' contrary source_ref invalid')
  aa.append(f"{n}/{ref['narrative_ordinal'] if ref else n}/{x['paragraph_index']}/{x['paragraph_sha256']}\n");anchors+=1
 mm.append(f"{n}|{m['spine_index']}|{m['epub_path']}|{m['chapter_sha256']}|{m['nonempty_paragraphs']}\n")
 paragraphs+=receipt['body_paragraph_count']
ck((paragraphs,claims,anchors,cross)==(673,12,38,2),f'false claimed coverage: got paragraphs={paragraphs},close={claims},anchors={anchors},cross={cross}')
ck(len(aspects)>=7,'lacks diversity of scene narration aspects')
ck(stats['original_member_fnv']==fnv(mm)=='7abab7b5','original 12 raw XHTML member proof aggregate mismatch')
ck(stats['paragraph_anchor_fnv']==fnv(aa)=='5eed412c','original 38 paragraph SHA proof aggregate mismatch')
for filename in ('cangjie/reading/tiexue_521_532.md','cangjie/reading/R034/tiexue_close_analysis.md','cangjie/reading/R034/tiexue_continuity.md','cangjie/reading/R034/CONTENT_QUALITY_AUDIT.md','cangjie/reading/R034/LOCAL_SOURCE_VERIFICATION.md','runs/R034.md'):
 ck((R/filename).is_file(),'missing required artifact '+filename)
cur=json.loads((R/'CURRENT_ROUND.json').read_text('utf8'))
if cur['current_round']=='R034':ck(cur['full_text_read_chapters']=={'wanming':560,'tiexuecanming':520},'advanced official chapter count before formal PASS')
else:ck(cur['full_text_read_chapters']['wanming']>=560 and cur['full_text_read_chapters']['tiexuecanming']>=532,'official counts regress')
for e in errors:print('FAIL',e)
if errors:sys.exit(1)
print(f'PASS R034 PUBLIC SOURCE_STRUCTURE_ONLY: {paragraphs} paragraphs, {claims} close studies, {anchors} SHA paragraph anchors, {cross} anchored contrary studies')
parser=argparse.ArgumentParser();parser.add_argument('--source-dir',type=Path);args=parser.parse_args()
if args.source_dir:
 from lxml import html
 matches=list(args.source_dir.glob('铁血残明*.epub'))
 if len(matches)!=1:sys.exit('FAIL exactly one private original Tiexue EPUB required')
 if sha(matches[0].read_bytes())!=EPUB:sys.exit('FAIL original full EPUB SHA mismatch')
 with zipfile.ZipFile(matches[0]) as archive:
  if archive.testzip():sys.exit('FAIL original EPUB CRC')
  for r in receipts:
   source=master[r['narrative_ordinal']];raw=archive.read(source['epub_path'])
   if sha(raw)!=source['chapter_sha256']:sys.exit('FAIL 12-original-member SHA')
   ps=[t.strip() for node in html.fromstring(raw).xpath('//body//p') if(t:=node.text_content()).strip()]
   if len(ps)!=r['body_paragraph_count']:sys.exit('FAIL full real paragraph counts')
   for x in r['anchors']:
    ref=x.get('source_ref');m=master[ref['narrative_ordinal']] if ref else source
    if ref:
     raw2=archive.read(m['epub_path']);ps2=[t.strip() for node in html.fromstring(raw2).xpath('//body//p') if(t:=node.text_content()).strip()]
    else:ps2=ps
    if sha(ps2[x['paragraph_index']-1].encode())!=x['paragraph_sha256']:sys.exit(f'FAIL source-aligned paragraph at {r["narrative_ordinal"]}/{x["anchor_id"]}')
 print('PASS R034 PRIVATE ORIGINAL EPUB: full SHA, all 12 members and all 38 paragraph SHA anchors verified; B PROVISIONAL C NOT_RUN')
