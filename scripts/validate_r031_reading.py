#!/usr/bin/env python3
"""Validate R031 local research structure and optionally its private EPUB bytes.

Public-only checks MUST NOT be called full source validation or literary mastery.
To run locally:
  python3 scripts/validate_r031_reading.py --source-dir /mnt/data
The novel EPUB and its contents must never be committed to public GitHub.
"""
import argparse,csv,hashlib,json,re,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'cangjie/reading/R031'
EXPECTED='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
focus={481,482,483,484,487,488,492,493,495,497,498,501,503,505,506,507,511,513,519,520}
errs=[]
def check(p,msg):
 if not p:errs.append(msg)
def sha(data):return hashlib.sha256(data).hexdigest()
def fnv(values):
 x=2166136261
 for s in values:
  for c in s:x=((x^ord(c))*16777619)&0xffffffff
 return f'{x:08x}'

def run(srcdir=None):
 with (DATA/'wanming_source_index.csv').open(newline='',encoding='utf-8') as f:sources=list(csv.DictReader(f))
 receipts=[json.loads(line) for line in (DATA/'wanming_receipts.jsonl').read_text('utf-8').splitlines() if line.strip()]
 notes=[json.loads(line) for line in (DATA/'wanming_chapter_observations.jsonl').read_text('utf-8').splitlines() if line.strip()]
 check(len(receipts)==len(sources)==len(notes)==40,'missing any of 40 original chapter artifacts')
 check([r['narrative_ordinal'] for r in receipts]==list(range(481,521)),'ordinal sequence invalid')
 check([int(s['narrative_ordinal']) for s in sources]==list(range(481,521)),'source index sequence invalid')
 check([n['narrative_ordinal'] for n in notes]==list(range(481,521)),'chapter analysis sequence invalid')
 check(sum(r['body_paragraph_count'] for r in receipts)==1960,'paragraph total invalid')
 check(sum(r['mode']=='CLOSE_READ' for r in receipts)==20,'20 close read chapters required')
 check(sum(len(r['anchors']) for r in receipts)==82,'SHA anchor total must be 82')
 check(sum(c['counterexample_status']=='FOUND' for r in receipts for c in r['mechanism_claims'])==2,'cross chapter contrary evidence count invalid')
 check(len(set(r['event_chain'][0] for r in receipts))==40,'event notes not distinct')
 check(len(set(r['open_questions'][0] for r in receipts))==40,'open questions not distinct')
 claims=[c for r in receipts for c in r['mechanism_claims']]
 check(len(claims)==20,'exactly 20 scene claims required')
 for k in ('claim_text','alternative_rendering_loss','failure_boundary','counterexample_search_note'):
  check(len(set(c[k] for c in claims))==20,'templated '+k)
 check(len(set(c['aspect'] for c in claims))>=7,'insufficient different narrative aspects')
 source_hashes=[];anchor_hashes=[]
 arch=None;html=None
 if srcdir:
  from lxml import html
  files=list(Path(srcdir).glob('晚明*.epub'))
  check(len(files)==1,'private original EPUB must exist exactly once')
  if files:
   check(sha(files[0].read_bytes())==EXPECTED,'private original whole EPUB mismatch')
   arch=zipfile.ZipFile(files[0]);check(arch.testzip() is None,'EPUB CRC failed')
 for r,s,note in zip(receipts,sources,notes):
  n=r['narrative_ordinal'];in_focus=n in focus
  expected_spine=n+(15 if n<=487 else 16)
  expected_path=f'OEBPS/Text/Chapter_{n+(12 if n<=487 else 13):04d}.xhtml'
  check(r['book_slug']=='wanming' and r['source_epub_sha256']==EXPECTED,f'{n}: wrong source')
  check(r['spine_index']==int(s['spine_index'])==expected_spine,f'{n}: OPF spine mismatch')
  check(r['epub_path']==s['epub_path']==expected_path,f'{n}: wrong member path')
  check(r['chapter_sha256']==s['chapter_sha256'],f'{n}: reported chapter member SHA mismatch')
  check(r['body_paragraph_count']==r['observed_paragraph_count']==int(s['nonempty_paragraphs']),f'{n}: paragraph counts diverge')
  check(r['mode']==s['mode']==('CLOSE_READ' if in_focus else 'FULL_TEXT_READ'),f'{n}: wrong mode')
  check(r['fixture_only'] is False and r.get('round_id')=='R031' and len(r.get('reader_session_id',''))>10,f'{n}: fake reader session')
  check(r.get('paragraph_normalization')=='xhtml_visible_text_trim_whitespace_v1',f'{n}: wrong text extraction rule')
  check(len(r['event_chain'])==2 and all(len(x)>20 for x in r['event_chain']),f'{n}: generic or missing event analysis')
  check(note['observed_event']==r['event_chain'][0] and note['independent_choice']==r['event_chain'][1],f'{n}: narrative observations inconsistent')
  check(note['open_question']==r['open_questions'][0],f'{n}: unanswered event mismatch')
  a_own=[a for a in r['anchors'] if not a.get('source_ref')]
  check(len(a_own)==(3 if in_focus else 1),f'{n}: origin/support/exit anchors missing')
  check(';'.join(f"{a['paragraph_index']}:{a['paragraph_sha256']}" for a in a_own)==s['paragraph_sha256_anchors'],f'{n}: index anchors differ')
  check(len(r['mechanism_claims'])==(1 if in_focus else 0),f'{n}: literary claims incorrect for reading mode')
  if in_focus:
   c=r['mechanism_claims'][0]
   check(c['verification_state']=='PROVISIONAL',f'{n}: improper unreviewed literary verification')
   check(len(c['failure_boundary'])>30 and len(c['counterexample_search_note'])>30 and len(c['alternative_rendering_loss'])>30,f'{n}: insufficient substantive literary interpretation')
   check(c['support_anchor_ids']==[a_own[1]['anchor_id']],f'{n}: source scene locator not support anchor')
   cross=[a for a in r['anchors'] if a.get('source_ref')]
   if c['counterexample_status']=='FOUND':
    check(len(cross)==1 and c['counterexample_anchor_ids']==[cross[0]['anchor_id']],f'{n}: unsupported FOUND')
   else:check(c['counterexample_status']=='SEARCHED_NONE' and not c['counterexample_anchor_ids'] and not cross,f'{n}: improperly represented cross counterexample')
  source_hashes.append(f"{n}|{r['spine_index']}|{r['epub_path']}|{r['chapter_sha256']}|{r['body_paragraph_count']}\n")
  par=[]
  if arch:
   body=arch.read(expected_path)
   check(sha(body)==r['chapter_sha256'],f'{n}: actual member raw SHA mismatch')
   par=[t for p in html.fromstring(body).xpath('//body//p') if (t:=p.text_content().strip())]
   check(len(par)==r['body_paragraph_count'],f'{n}: actual original paragraph count mismatch')
  for a in r['anchors']:
   pos=a['paragraph_index'];ref=a.get('source_ref');other=ref['narrative_ordinal'] if ref else n
   check(re.fullmatch('[0-9a-f]{64}',a['paragraph_sha256']) is not None,f'{n}: malformed paragraph SHA')
   if ref:check(ref['epub_path']==f'OEBPS/Text/Chapter_{other+(12 if other<=487 else 13):04d}.xhtml',f'{n}: wrong cross reference')
   if arch:
    if ref:
     orig=arch.read(ref['epub_path']);check(sha(orig)==ref['chapter_sha256'],f'{n}: cross member incorrect')
     pars=[t for p in html.fromstring(orig).xpath('//body//p') if (t:=p.text_content().strip())]
    else:pars=par
    check(1<=pos<=len(pars),f'{n}: anchor out of chapter range')
    if 1<=pos<=len(pars):check(sha(pars[pos-1].encode('utf-8'))==a['paragraph_sha256'],f'{n}: original p{pos} SHA mismatch')
   anchor_hashes.append(f"{n}/{other}/{pos}/{a['paragraph_sha256']}\n")
 check(fnv(source_hashes)=='2289545f','40 source-member FNV mismatch')
 check(fnv(anchor_hashes)=='39e1af85','82 paragraph locator FNV mismatch')
 if arch:arch.close()
 if errs:
  for e in errs:print('FAIL',e)
  return 1
 print('PASS: R031 40 unique chapters; 1960 original paragraph positions; 20 distinctive CLOSE_READ; 82 SHA anchors; 2 anchored cross-chapter counterexamples')
 print('PASS: A=PRIVATE_SOURCE_SHA_VERIFIED' if srcdir else 'PASS: SOURCE_STRUCTURE_ONLY; original private EPUB not checked')
 print('B=PROVISIONAL; C=NOT_RUN; REMOTE_GITHUB_ACTIONS=NOT_RUN; R031_REMOTE_PASSED=FALSE')
 return 0
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source-dir',type=Path)
 args=parser.parse_args();sys.exit(run(args.source_dir))
