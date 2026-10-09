#!/usr/bin/env python3
"""R033 whole-batch original narrative receipts validator; public CI cannot validate private novels.
With --source-dir, all forty real original XHTML member SHA and every paragraph anchor are rechecked.
Structural validation does not mean any independent literary mastery certification.
"""
import argparse,csv,hashlib,json,re,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'cangjie/reading/R033'
EXPECT_EPUB='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
FOCUS={521, 522, 523, 525, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 559}
with (ROOT/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:master={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['narrative_ordinal']}
with (BASE/'wanming_source_index.csv').open(encoding='utf-8',newline='') as f:sources=list(csv.DictReader(f))
records=[json.loads(x) for x in (BASE/'wanming_receipts.jsonl').read_text('utf-8').splitlines() if x.strip()]
observations=[json.loads(x) for x in (BASE/'wanming_chapter_observations.jsonl').read_text('utf-8').splitlines() if x.strip()]
errors=[]
def ck(cond,msg):
 if not cond:errors.append(msg)
def fnv(strings):
 h=2166136261
 for s in strings:
  for ch in s:h=((h^ord(ch))*16777619)&0xffffffff
 return f'{h:08x}'
ck(len(records)==len(sources)==len(observations)==40,'40 chapter records/source indexes/independent observations required')
ck([r['narrative_ordinal'] for r in records]==list(range(521,561)),'original narrative ordinals incomplete')
ck([int(s['narrative_ordinal']) for s in sources]==list(range(521,561)),'original OPF ordinal drift')
ck(master[521]['epub_path']=='OEBPS/Text/Chapter_0534.xhtml' and master[560]['epub_path']=='OEBPS/Text/Chapter_0573.xhtml','printed chapter number confused with true OPF narrative ordinal')
T=A=C=FOUND=0;claims=[];seen=set();members=[];anchors=[]
for r,s,o in zip(records,sources,observations):
 n=r['narrative_ordinal'];m=master[n];close=n in FOCUS
 ck(r['book_slug']=='wanming' and r['source_epub_sha256']==EXPECT_EPUB,str(n)+': source changed')
 ck(r['spine_index']==int(m['spine_index'])==int(s['spine_index']),str(n)+': spine changed')
 ck(r['epub_path']==m['epub_path']==s['epub_path'] and r['chapter_sha256']==m['chapter_sha256']==s['chapter_sha256'],str(n)+': ZIP member SHA drift')
 ck(r['body_paragraph_count']==r['observed_paragraph_count']==int(m['nonempty_paragraphs'])==int(s['nonempty_paragraphs']),str(n)+': original body paragraph mismatch')
 ck(r['mode']==s['mode']==('CLOSE_READ' if close else 'FULL_TEXT_READ'),str(n)+': sampling falsely represented as full reading')
 ck(r['round_id']=='R033' and not r['fixture_only'] and len(r['reader_session_id'])>10,str(n)+': provenance missing')
 ck(r['paragraph_normalization']=='xhtml_visible_text_trim_whitespace_v1',str(n)+': normalization altered')
 ck(len(r['event_chain'])==2 and all(len(t)>20 for t in r['event_chain']) and bool(r['open_questions']),str(n)+': independent narrative observation insufficient')
 ck(r['event_chain'][0] not in seen,str(n)+': duplicate narrative note');seen.add(r['event_chain'][0])
 ck(o['observed_event']==r['event_chain'][0] and o['independent_choice']==r['event_chain'][1] and o['open_question']==r['open_questions'][0] and o['literary_status']=='PROVISIONAL',str(n)+': observation mismatch')
 own=[a for a in r['anchors'] if not a.get('source_ref')]
 ck(';'.join(str(a['paragraph_index'])+':'+a['paragraph_sha256'] for a in own)==s['paragraph_sha256_anchors'],str(n)+': recorded original paragraph SHA different from index')
 ck(len(own)==(3 if close else 1),str(n)+': original body anchor count incorrect')
 for a in r['anchors']:
  src=a.get('source_ref');t=master[src['narrative_ordinal']] if src else m
  ck(re.fullmatch('[a-f0-9]{64}',a['paragraph_sha256']) is not None and 0<a['paragraph_index']<=int(t['nonempty_paragraphs']),str(n)+': paragraph reference malformed')
  if src:ck(src['epub_path']==t['epub_path'] and src['chapter_sha256']==t['chapter_sha256'] and src['book_slug']=='wanming',str(n)+': source_ref forged')
  anchors.append(f"{n}/{src['narrative_ordinal'] if src else n}/{a['paragraph_index']}/{a['paragraph_sha256']}\n")
  A+=1
 if close:
  C+=1;ck(len(r['mechanism_claims'])==1,str(n)+': close claim missing')
  for c in r['mechanism_claims']:
   claims.append(c)
   ck(c['verification_state']=='PROVISIONAL' and c['counterexample_status'] in ('FOUND','SEARCHED_NONE'),str(n)+': literary B prematurely certified')
   ck(set(c['support_anchor_ids'])<=set(a['anchor_id'] for a in own),str(n)+': claim anchor unsourced')
   ck(all(len(c[k])>35 for k in ('counterexample_search_note','alternative_rendering_loss','failure_boundary')),str(n)+': weak literature or boundary')
   if c['counterexample_status']=='FOUND':
    FOUND+=1;ck(c['counterexample_anchor_ids'] and all(any(a['anchor_id']==q and a.get('source_ref') for a in r['anchors']) for q in c['counterexample_anchor_ids']),str(n)+': real cross-chapter FOUND missing')
   else:ck(not c['counterexample_anchor_ids'],str(n)+': fake FOUND or unrelated anchor')
 else:ck(not r['mechanism_claims'],str(n)+': other full-read chapter pretends CLOSE')
 members.append(f"{n}|{m['spine_index']}|{m['epub_path']}|{m['chapter_sha256']}|{m['nonempty_paragraphs']}\n")
 T+=r['body_paragraph_count']
ck((T,C,A,FOUND)==(1892,20,82,2),f'counts mismatch T={T} C={C} A={A} FOUND={FOUND}')
ck(fnv(members)=='21953130' and fnv(anchors)=='a7e0af45','source/anchor provenance FNV changed')
ck(len({c['claim_text'] for c in claims})==20 and len({c['failure_boundary'] for c in claims})==20 and len({c['alternative_rendering_loss'] for c in claims})==20,'copied generic mechanisms or risk boundary')
ck(len({c['aspect'] for c in claims})>=6,'insufficient distinct narrative aspect coverage')
for p in ['cangjie/reading/wanming_521_560.md','cangjie/reading/R033/wanming_close_analysis.md','cangjie/reading/R033/wanming_continuity.md','cangjie/reading/R033/LOCAL_SOURCE_VERIFICATION.md','runs/R033.md']:
 ck((ROOT/p).is_file(),'missing full R033 artifact '+p)
cur=json.loads((ROOT/'CURRENT_ROUND.json').read_text('utf-8'))
if cur['current_round']=='R033':ck(cur['full_text_read_chapters']=={'wanming':520,'tiexuecanming':520},'official chapter count increased before PASS')
else:ck(cur['full_text_read_chapters']['wanming']>=560 and cur['full_text_read_chapters']['tiexuecanming']>=520,'official source counts regressed')
for e in errors:print('FAIL',e)
if errors:sys.exit(1)
print('PASS R033 PUBLIC SOURCE_STRUCTURE_ONLY:',T,'paragraphs',C,'close scenes',A,'SHA locators',FOUND,'cross chapter counterexamples','member-FNV',fnv(members),'anchor-FNV',fnv(anchors))
parser=argparse.ArgumentParser();parser.add_argument('--source-dir',type=Path);arg=parser.parse_args()
if arg.source_dir:
 from lxml import html
 options=list(arg.source_dir.glob('晚明*.epub'))
 if len(options)!=1:sys.exit('FAIL expected exactly one privately provided Wanming EPUB')
 path=options[0];validsha=hashlib.sha256(path.read_bytes()).hexdigest()==EXPECT_EPUB
 if not validsha:sys.exit('FAIL original book fingerprint')
 with zipfile.ZipFile(path) as archive:
  if archive.testzip() is not None:sys.exit('FAIL ZIP CRC')
  for r in records:
   for a in r['anchors']:
    src=a.get('source_ref');t=master[src['narrative_ordinal']] if src else master[r['narrative_ordinal']]
    raw=archive.read(t['epub_path'])
    if hashlib.sha256(raw).hexdigest()!=t['chapter_sha256']:sys.exit('FAIL original raw member SHA')
    ps=[v.strip() for tag in html.fromstring(raw).xpath('//body//p') if (v:=tag.text_content()).strip()]
    if hashlib.sha256(ps[a['paragraph_index']-1].encode()).hexdigest()!=a['paragraph_sha256']:sys.exit('FAIL original body p SHA')
 print('PASS R033 PRIVATE ORIGINAL EPUB: matched complete source SHA and all 82 original paragraph SHA locators (no literary certification)')
