#!/usr/bin/env python3
"""R037 exact Adler interpretive step: grounded fictional concepts, 10 propositions, 60 private-source SHA anchors.

Without --source-dir this checks the public structure; GitHub cannot check privately supplied source.
With --source-dir this checks the entire original EPUB SHA and each genuine original paragraph.
B is interpretive hypothesis PROVISIONAL; C original-fiction utility NOT_RUN.
"""
import argparse,csv,hashlib,json,re,sys,zipfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'books/wanming/adler'
EXPECTED='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
VOLS=[(1,51,12,62),(52,105,64,117),(106,155,119,168),(156,271,170,285),(272,487,287,502),(488,571,504,587)]
ERRORS=[]
def ck(b,msg):
 if not b:ERRORS.append(msg)
def digest(b):return hashlib.sha256(b).hexdigest()
def verify(private_dir=None):
 body=(D/'INTERPRETATION.md').read_text('utf-8')
 with (D/'INTERPRETATION_EVIDENCE.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
 with (ROOT/'sources/metadata/wanming_v13_spine.csv').open(newline='',encoding='utf-8') as f:
  meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
 ck(len(meta)==571,'frozen R002 metadata 571 narratives not present')
 ck(len(rows)==60,'R037 must contain exactly 60 original scene anchors')
 ck(len({(x['narrative_ordinal'],x['paragraph_index']) for x in rows})==60,'duplicate source paragraph locators')
 ck(len({int(x['narrative_ordinal']) for x in rows})==57,'exactly 57 distinct anchored original chapters expected')
 ck(sum(x['evidence_kind']=='R037_NEW_ORIGINAL_READING' for x in rows)==24,'missing 24 new original reading anchors')
 ck(sum(x['evidence_kind']=='R036_VERIFIED_REEXAMINED' for x in rows)==36,'missing 36 inherited R036 source anchors')
 counts=Counter(x['proposition_id'] for x in rows)
 ck(set(counts)=={f'P{i:02d}' for i in range(1,11)},'wrong R037 proposition IDs')
 ck(all(counts[f'P{i:02d}']>=4 for i in range(1,11)),'some interpretations have insufficient grounded scenes')
 ck(len(set(x['volume'] for x in rows))==6,'missing an original OPF narrative volume')
 ck('EXTERNAL_NOT_VERIFIED' in body and 'B=PROVISIONAL' in body and 'C=NOT_RUN' in body,'A/B/C boundaries missing')
 ck('R042' in body and 'R038' in body,'Adler sequence and user confirmation missing')
 ck('作者' in body and '原书' in body,'source vs intent separation missing')
 for n in range(1,11):
  ck(bool(re.search(rf'^### P{n:02d}｜',body,re.M)),f'P{n:02d} detailed proposition section missing')
 ck('n565/p69→n571/p5' in body,'missing falsifiable cross-chapter source reversal')
 for k in ['词项及类型','竞争解释','人物立场','推导链','历史事实']:
  ck(k in body,f'missing interpretive section {k}')
 ck(len({x['scene_fact'] for x in rows})==60,'duplicated scene facts, possible template leakage')
 ck(len({x['interpretation_scope_or_alternative'] for x in rows})==60,'duplicated limitations, possible template leakage')
 archive=None
 if private_dir:
  from lxml import html
  files=list(Path(private_dir).glob('晚明*.epub'))
  ck(len(files)==1,'private original Wanming EPUB must appear exactly once')
  if len(files)==1:
   ck(digest(files[0].read_bytes())==EXPECTED,'private whole original EPUB SHA mismatch')
   archive=zipfile.ZipFile(files[0]);ck(archive.testzip() is None,'private original EPUB CRC mismatch')
 for r in rows:
  n=int(r['narrative_ordinal']);p=int(r['paragraph_index']);m=meta.get(n)
  ck(m is not None,f'narrative ordinal missing {n}')
  if not m:continue
  expected_vol=next((i for i,(a,b,_,_) in enumerate(VOLS,1) if a<=n<=b),None)
  ck(r['volume']==f'S{expected_vol}',f'wrong volume n={n}')
  ck(int(r['spine_index'])==int(m['spine_index']),f'wrong OPF spine n={n}')
  ck(r['epub_path']==m['epub_path'],f'wrong original XHTML path n={n}')
  ck(r['chapter_sha256']==m['chapter_sha256'],f'wrong original XHTML member SHA n={n}')
  ck(p>=1 and len(r['paragraph_sha256'])==64,f'invalid paragraph locator {n}/{p}')
  ck(r['literary_status']=='PROVISIONAL' and r['source_check']=='PRIVATE_SHA_PASS','overclaim in evidence rows')
  ck(len(r['scene_fact'])>=22 and len(r['interpretation_scope_or_alternative'])>=20,f'weak observation or limitation n={n}')
  if archive:
   data=archive.read(r['epub_path'])
   ck(digest(data)==r['chapter_sha256'],f'actual chapter bytes disagree n={n}')
   paragraphs=[x.text_content().strip() for x in html.fromstring(data).xpath('//body//p') if x.text_content().strip()]
   ck(p<=len(paragraphs),f'original paragraph missing {n}/{p}')
   if p<=len(paragraphs):ck(digest(paragraphs[p-1].encode('utf-8'))==r['paragraph_sha256'],f'PRIVATE anchor mismatch {n}/{p}')
 if archive:archive.close()
 print('R037', 'PASS' if not ERRORS else 'FAIL', f'10 interpretive narrative hypotheses, {len(rows)} original paragraph positions, {len(set(x["narrative_ordinal"] for x in rows))} chapters, 24 new + 36 reused verified, 6 OPF volumes; A={"PRIVATE_ORIGINAL_SHA_VERIFIED" if private_dir else "SOURCE_STRUCTURE_ONLY"}; B PROVISIONAL; C NOT_RUN')
 for e in ERRORS:print('FAIL',e)
 return 0 if not ERRORS else 1
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source-dir');args=parser.parse_args();sys.exit(verify(args.source_dir))
