#!/usr/bin/env python3
"""R039 Cangjie Adler Structural entry gate; public source-structure, private EPUB paragraphs.
Explicitly not a test of independent literary mastery, historical correctness, or Skill gains.
"""
import argparse,csv,hashlib,re,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'books/tiexuecanming/adler'
EPUB_SHA='9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf'
STAGES={'S1':(1,80),'S2':(81,160),'S3':(161,280),'S4':(281,400),'S5':(401,480),'S6':(481,532)}

def run(source_dir=None):
 errs=[]
 def ck(cond,msg):
  if not cond:errs.append(msg)
 sha=lambda s:hashlib.sha256(s).hexdigest()
 doc=(D/'STRUCTURE.md').read_text(encoding='utf-8')
 quality=(D/'STRUCTURE_QUALITY_AUDIT.md').read_text(encoding='utf-8')
 with (D/'STRUCTURE_EVIDENCE.tsv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
 with (ROOT/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:
  md={int(r['narrative_ordinal']):r for r in csv.DictReader(f) if r['is_narrative_chapter']=='1'}
 ck(len(md)==532,'source spine requires 532 narrative members')
 ck(len(rows)==58,'require 58 actual paragraph locators')
 ck(len(set((x['narrative_ordinal'],x['paragraph_index']) for x in rows))==len(rows),'repeated original paragraph locator')
 ck(len(set(x['narrative_ordinal'] for x in rows))==53,'expected 53 independently chosen chapters')
 ck(all(f'### S{i}｜' in doc for i in range(1,7)),'six concrete structural arguments required')
 ck('一句话结构主旨' in doc and '核心问题' in doc and '## 四、开篇' in doc,'original Structural Adler four questions or final reread absent')
 ck('不是原书正式六卷' in doc or '不是声称原书OPF存在六个卷界' in doc,'analytic segments confused with real OPF volumes')
 ck('n532/p49' in doc and 'n530/p41' in doc and 'n161/p65' in doc,'key original/source-limited contradictions not anchored')
 ck('PROVISIONAL' in doc and 'NOT_RUN' in doc and 'R042' in doc and 'R040' in doc,'A/B/C and user gate absent')
 ck('R008' in quality and 'R024' in quality,'historic source interpretation quality debts suppressed')
 count={x:0 for x in STAGES}
 for row in rows:
  try:n=int(row['narrative_ordinal']);p=int(row['paragraph_index'])
  except:errs.append('malformed ordinal/paragraph');continue
  st=row['stage']
  ck(st in STAGES,f'unknown group for n{n}')
  if st in STAGES:
   count[st]+=1;lo,hi=STAGES[st];ck(lo<=n<=hi,f'chapter n{n} not within analytical story arc {st}')
  ck(n in md,f'unknown narrative ordinal n{n}')
  if n in md:
   ref=md[n]
   for key in ('spine_index','epub_path','chapter_sha256'):
    ck(row[key]==ref[key],f'R002 book-source metadata mismatch n{n} {key}')
  ck(p>=1 and len(row['paragraph_sha256'])==64,f'invalid private paragraph source digest n{n}')
  ck(len(row['evidence_role'])>=13 and len(row['competing_interpretation_or_limit'])>=13,f'non-specific interpretation or boundary n{n}')
  ck(row['literary_judgment']=='PROVISIONAL',f'false independent literary B certification n{n}')
 ck(min(count.values())>=8,'missing one structural arc evidence coverage')
 ck(len(set(x['evidence_role'] for x in rows))==len(rows),'repeated/template evidence claims')
 if source_dir:
  from lxml import html
  f=list(Path(source_dir).glob('铁血残明*.epub'))
  ck(len(f)==1,'expected single original private book')
  if len(f)==1:
   ck(sha(f[0].read_bytes())==EPUB_SHA,'private whole EPUB sha256 mismatch')
   with zipfile.ZipFile(f[0]) as z:
    ck(z.testzip() is None,'private original bad zip CRC')
    for row in rows:
     n=row['narrative_ordinal'];p=int(row['paragraph_index'])
     member=z.read(row['epub_path'])
     ck(sha(member)==row['chapter_sha256'],f'private raw XHTML SHA wrong n{n}')
     paragraphs=[q.text_content().strip() for q in html.fromstring(member).xpath('//body//p') if q.text_content().strip()]
     ck(1<=p<=len(paragraphs),f'original paragraph index out of bound n{n}/p{p}')
     if 1<=p<=len(paragraphs):ck(sha(paragraphs[p-1].encode('utf-8'))==row['paragraph_sha256'],f'original paragraph SHA mismatch n{n}/p{p}')
 print('R039', 'PASS' if not errs else 'FAIL',f'6 independent analytical arcs, {len(rows)} original locators, {len(set(x["narrative_ordinal"] for x in rows))} distinct source chapters; A={"PRIVATE_ORIGINAL_SHA" if source_dir else "SOURCE_STRUCTURE_ONLY"}; B PROVISIONAL C NOT_RUN')
 for e in errs:print('FAIL:',e)
 return 0 if not errs else 1
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--source-dir');sys.exit(run(ap.parse_args().source_dir))
