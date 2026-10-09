#!/usr/bin/env python3
"""V13 R036 Adler structural entry gate: 6 narrative spines + source-grounded arguments.

Public mode validates evidence structure against R002 and headings; it cannot read copyrighted EPUB.
Private mode (--source-dir) verifies exactly the submitted original EPUB and all 36 anchor paragraphs.
This is *not* a literary B/C mastery or BOOK_OVERVIEW approval test.
"""
import argparse,csv,hashlib,json,zipfile,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
EPUB_SHA='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
VOLS=[(1,51,12,62),(52,105,64,117),(106,155,119,168),(156,271,170,285),(272,487,287,502),(488,571,504,587)]
D=R/'books/wanming/adler'
errors=[]
def require(cond,msg):
 if not cond:errors.append(msg)
def digest(b):return hashlib.sha256(b).hexdigest()
def run(source_dir=None):
  doc=(D/'STRUCTURE.md').read_text('utf-8')
  with (D/'STRUCTURE_EVIDENCE.tsv').open(encoding='utf-8',newline='') as f:obs=list(csv.DictReader(f,delimiter='\t'))
  with (R/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:
    meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
  require(len(meta)==571,'R002 metadata must identify exactly 571 narrative chapters')
  require(len(VOLS)==6 and sum(b-a+1 for a,b,_,_ in VOLS)==571,'six OPF narrative ranges must cover whole book')
  require(all(f'**S{i} ' in doc for i in range(1,7)),'six distinct structure headers S1-S6 missing')
  require('STRUCTURAL_DRAFT' in doc and 'PROVISIONAL' in doc,'must disclose structural draft status')
  require('R042' in doc and 'NOT_RUN' in doc,'Stage0 user approval and skill C boundaries absent')
  require(len(obs)==36,'must preserve 36 exact original paragraph anchor notes')
  require(len(set((x['narrative_ordinal'],x['paragraph_index']) for x in obs))==len(obs),'duplicate paragraph locator')
  require(len(set(int(x['narrative_ordinal']) for x in obs))>=30,'not enough distinct chapters for six-part structure')
  vols=[]
  for row in obs:
   n=int(row['narrative_ordinal']);p=int(row['paragraph_index']);volume=next((i for i,(a,b,_,_) in enumerate(VOLS,1) if a<=n<=b),None)
   require(volume is not None,f'ordinal out of bounds {n}')
   if volume:vols.append(volume)
   if n not in meta:continue
   m=meta[n];sp=int(row['spine_index']);path=row['epub_path']
   exp=n+(11 if n<=51 else 12 if n<=105 else 13 if n<=155 else 14 if n<=271 else 15 if n<=487 else 16)
   require(sp==int(m['spine_index'])==exp,f'R002 spine mismatch n={n}')
   require(path==m['epub_path'],f'R002 path mismatch n={n}')
   require(row['chapter_sha256']==m['chapter_sha256'],f'R002 member SHA mismatch n={n}')
   require(p>=1 and len(row['paragraph_sha256'])==64,f'malformed paragraph SHA n={n}')
   for key in ['observed_support','competing_explanation_or_limit']:
     require(len(row[key])>=18,f'{key} too short n={n}')
   require(row['literary_judgment']=='PROVISIONAL',f'literary false certification n={n}')
  require(sorted(set(vols))==list(range(1,7)),'source anchors do not cover all six volumes')
  require(len({x['observed_support'] for x in obs})==len(obs),'duplicated structure evidence claims')
  require('n565' in doc and 'n571/p5' in doc,'end counterexample n565 to n571 not demonstrated')
  require('S1' in doc and 'S6' in doc and '一句结构性主旨' in doc and '核心结构问题' in doc,'incomplete Adler structural response')
  if source_dir:
   from lxml import html
   src=list(Path(source_dir).glob('晚明*.epub'))
   require(len(src)==1,'expected exactly one user Wanming EPUB')
   if len(src)==1:
    require(digest(src[0].read_bytes())==EPUB_SHA,'private source whole SHA invalid')
    with zipfile.ZipFile(src[0]) as arch:
     require(arch.testzip() is None,'private EPUB bad ZIP CRC')
     for row in obs:
      n=int(row['narrative_ordinal']);p=int(row['paragraph_index'])
      data=arch.read(row['epub_path'])
      require(digest(data)==row['chapter_sha256'],f'private member SHA wrong n={n}')
      pars=[x.text_content().strip() for x in html.fromstring(data).xpath('//body//p') if x.text_content().strip()]
      require(p<=len(pars),f'private paragraph locator overflow n={n}')
      if p<=len(pars):require(digest(pars[p-1].encode())==row['paragraph_sha256'],f'private paragraph SHA mismatch n={n}/p{p}')
  print('R036', 'PASS' if not errors else 'FAIL',f'6 volumes, {len(obs)} source locators, {len(set(int(x["narrative_ordinal"]) for x in obs))} distinct chapters; A={"PRIVATE_ORIGINAL_SHA" if source_dir else "SOURCE_STRUCTURE_ONLY"}; B=PROVISIONAL; C=NOT_RUN')
  for e in errors:print('ERROR',e)
  return 0 if not errors else 1
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source-dir');args=parser.parse_args();sys.exit(run(args.source_dir))
