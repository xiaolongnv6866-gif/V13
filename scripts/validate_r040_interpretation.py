#!/usr/bin/env python3
"""R040 Cangjie Adler Interpretive: source-structure CI plus private actual EPUB check.
A source hashes do not certify B literary interpretations or C novel-writing benefit.
"""
import argparse,csv,hashlib,re,sys,zipfile,json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'books/tiexuecanming/adler'
SHA='9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf'
ARCS=[(1,80),(81,160),(161,280),(281,400),(401,480),(481,532)]
def run(source_dir=None):
 errors=[]
 def ck(b,m):
  if not b:errors.append(m)
 study=(D/'INTERPRETATION.md').read_text(encoding='utf8');audit=(D/'INTERPRETATION_QUALITY_AUDIT.md').read_text(encoding='utf8')
 stats=json.loads((D/'STUDY_STATS.json').read_text(encoding='utf8'))
 with (D/'INTERPRETATION_EVIDENCE.tsv').open(encoding='utf8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
 with (ROOT/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf8',newline='') as f:meta={int(r['narrative_ordinal']):r for r in csv.DictReader(f) if r['is_narrative_chapter']=='1'}
 ck(len(meta)==532,'R002 spine must have 532 valid chapters')
 ck(len(rows)==87,'R040 expected 58 R039 + 29 newly selected locators')
 ck(len({(r['narrative_ordinal'],r['paragraph_index']) for r in rows})==len(rows),'duplicate paragraph locators')
 ck(len({r['narrative_ordinal'] for r in rows})==81,'expected 81 distinct original chapters')
 ck(set(r['stage'] for r in rows)=={f'S{i}' for i in range(1,7)},'missing one analytical story arc')
 cs=Counter(r['proposition_id'] for r in rows)
 ck(set(cs)=={f'P{i:02d}' for i in range(1,11)},'all ten propositions require real evidence')
 ck(all(cs[f'P{i:02d}']>=5 for i in range(1,11)),'at least five original source locators per proposition')
 ck(Counter(r['origin'] for r in rows)=={'R039_VERIFIED_RECHECKED':58,'R040_NEW_ORIGINAL_READING':29},'false provenance of new locators')
 for i in range(1,11):
  ck(bool(re.search(rf'^### P{i:02d}｜',study,re.M)),f'P{i:02d} independent interpretive claim missing')
 for word in ['关键术语','跨命题论证链','人物立场','SOURCE_FACT','LITERARY_HYPOTHESIS','EXTERNAL_NOT_VERIFIED','n532/p49','n530/p41','n531/p8','PROVISIONAL','NOT_RUN','R041','R042']:
  ck(word in study,'essential interpretive boundary missing '+word)
 ck(len(re.findall(r'^\| .+\| .+\| .+\| .+\|$',study,re.M))>=12,'12 contextual definitions missing')
 ck('R008—R024' in audit and 'PRIVATE_ORIGINAL_SHA_VERIFIED' in audit and 'SOURCE_STRUCTURE_ONLY' in audit,'historical quality debt or CI/source distinction hidden')
 ck(len(study)>12000,'Interpretive argument too shallow')
 ck(stats.get('proposition_count')==10 and stats.get('term_count')==12 and stats.get('citation_anchor_count')==87,'stats disagree')
 archive=None
 if source_dir:
  from lxml import html
  ps=list(Path(source_dir).glob('铁血残明*.epub'))
  ck(len(ps)==1,'must have exactly one private original Tiexuecanming EPUB')
  if len(ps)==1:
   ck(hashlib.sha256(ps[0].read_bytes()).hexdigest()==SHA,'private whole EPUB SHA mismatch')
   archive=zipfile.ZipFile(ps[0]);ck(archive.testzip() is None,'private original ZIP CRC failed')
 try:
  for r in rows:
   n=int(r['narrative_ordinal']);p=int(r['paragraph_index']);m=meta.get(n)
   ck(m is not None,'invalid source ordinal '+str(n))
   if m is None:continue
   arc=next((i for i,(lo,hi) in enumerate(ARCS,1) if lo<=n<=hi),None)
   ck(r['stage']==f'S{arc}','wrong research arc n'+str(n))
   for k in ('spine_index','epub_path','chapter_sha256'):
    ck(r[k]==m[k],f'R002 source metadata mismatch n{n}/{k}')
   ck(p>0 and len(r['paragraph_sha256'])==64,f'bad paragraph location n{n}/p{p}')
   ck(r['source_check']=='PRIVATE_SHA_PASS' and r['literary_status']=='PROVISIONAL',f'false B certification n{n}')
   ck(len(r['observed_scene_fact'])>=17 and len(r['competing_interpretation_or_boundary'])>=17,f'underspecified source/limit n{n}/p{p}')
   if archive:
    raw=archive.read(r['epub_path']);ck(hashlib.sha256(raw).hexdigest()==r['chapter_sha256'],f'original XHTML bytes mismatch n{n}')
    pars=[q.text_content().strip() for q in html.fromstring(raw).xpath('//body//p') if q.text_content().strip()]
    ck(p<=len(pars),f'original paragraph index out of range n{n}/p{p}')
    if p<=len(pars):ck(hashlib.sha256(pars[p-1].encode('utf8')).hexdigest()==r['paragraph_sha256'],f'actual original paragraph SHA mismatch n{n}/p{p}')
 finally:
  if archive:archive.close()
 print('R040', 'PASS' if not errors else 'FAIL',f'10 propositions / 12 terms / 5 chains / {len(rows)} genuine paragraph loci from {len({r["narrative_ordinal"] for r in rows})} different chapters, 6 arcs; A={"PRIVATE_ORIGINAL_SHA_VERIFIED" if source_dir else "SOURCE_STRUCTURE_ONLY"}, B PROVISIONAL, C NOT_RUN')
 for e in errors:print('FAIL:',e)
 return int(bool(errors))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source-dir');sys.exit(run(parser.parse_args().source_dir))
