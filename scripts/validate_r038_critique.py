#!/usr/bin/env python3
"""R038 Adler Critical+Applicability: actual, bounded text evidence; no original copyrighted source in GitHub.
Without --source-dir CI is STRUCTURE_ONLY, with original private EPUB validate genuine source bytes.
No claim of independent literary correctness or original creative gain.
"""
import argparse,csv,hashlib,re,sys,zipfile
from collections import Counter
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
D=BASE/'books/wanming/adler'
SOURCE_SHA='a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082'
V=[(1,51),(52,105),(106,155),(156,271),(272,487),(488,571)]
def run(src=None):
 errs=[]
 def ck(a,m):
  if not a:errs.append(m)
 study=(D/'CRITIQUE_APPLICATION.md').read_text(encoding='utf8')
 tasks=(D/'TASKS.md').read_text(encoding='utf8')
 audit=(D/'CRITIQUE_QUALITY_AUDIT.md').read_text(encoding='utf8')
 with (D/'CRITIQUE_EVIDENCE.tsv').open(encoding='utf8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
 with (BASE/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
 ck(len(meta)==571,'source narrative mapping must contain 571 original members')
 ck(len(rows)==48,'48 critique anchors expected')
 ck(len(set((r['narrative_ordinal'],r['paragraph_index']) for r in rows))==48,'source positions repeated')
 ck(len({r['narrative_ordinal'] for r in rows})==45,'45 different source chapters required')
 ck(set(r['volume'] for r in rows)=={f'S{x}' for x in range(1,7)},'six OPF spans must appear')
 counts=Counter(r['critique_id'] for r in rows)
 ck(set(counts)=={f'C{x:02d}' for x in range(1,11)},'all ten critiques must have authentic original source anchors')
 ck(all(counts[f'C{x:02d}']>=4 for x in range(1,11)),'each critique requires 4+ true scene positions')
 for i in range(1,11):
  ck(bool(re.search(rf'^### C{i:02d} ',study,re.M)),f'C{i:02d} critique section missing')
  ck(bool(re.search(rf'^\| T{i:02d} \|',tasks,re.M)),f'T{i:02d} actual task input/output line missing')
  ck(f'T{i:02d}' in study and f'C{i:02d}' in tasks,f'critique-task relation not demonstrated {i}')
 for token in ['时代局限','叙事立场盲点','未被证明的假设','最强反驳','最强总反对意见','EXTERNAL_NOT_VERIFIED','B=PROVISIONAL','C=NOT_RUN','R042','NEEDS_REVIEW','n519/p70','n519/p69']:
  ck(token in study,f'missing Adler criticism and validity boundary {token}')
 for token in ['task_id','原创任务','所需输入','实际交付物','验收条件','来源','尚缺条件','T09','盲评','certified_skills=0']:
  ck(token in tasks,'task deliverable or limitation missing '+token)
 ck(len(study)>6000 and len(tasks)>2500,'critique or task study too shallow')
 ck('R007—R024' in audit and 'INDEPENDENT_REVIEW_NOT_DONE' in audit and 'SOURCE_STRUCTURE_ONLY' in audit,'quality debt or A/B/C audit missing')
 archive=None
 if src:
  from lxml import html
  files=list(Path(src).glob('晚明*.epub'))
  ck(len(files)==1,'exactly one original private Wanming EPUB needed')
  if len(files)==1:
   ck(hashlib.sha256(files[0].read_bytes()).hexdigest()==SOURCE_SHA,'original EPUB SHA mismatch')
   archive=zipfile.ZipFile(files[0]);ck(archive.testzip() is None,'EPUB CRC corruption')
 try:
  for row in rows:
   n=int(row['narrative_ordinal']);p=int(row['paragraph_index']);m=meta.get(n)
   ck(m is not None,f'invalid ordinal {n}')
   if not m:continue
   vol=next((i for i,(a,b) in enumerate(V,1) if a<=n<=b),None)
   ck(row['volume']==f'S{vol}',f'wrong OPF volume {n}')
   ck(int(m['spine_index'])==int(row['spine_index']),f'wrong OPF spine {n}')
   ck(row['epub_path']==m['epub_path'],f'wrong EPUB chapter path {n}')
   ck(row['chapter_sha256']==m['chapter_sha256'],f'wrong recorded chapter SHA {n}')
   ck(len(row['paragraph_sha256'])==64 and p>0,f'wrong source p SHA {n}/{p}')
   ck(row['source_status']=='PRIVATE_EPUB_SHA_MATCH' and row['literary_status']=='PROVISIONAL',f'inappropriate unproven upgrade {n}')
   ck(len(row['original_observation'])>=18 and len(row['competing_explanation_or_limit'])>=18,f'template or shallow scene {n}/{p}')
   if archive:
    data=archive.read(row['epub_path']);ck(hashlib.sha256(data).hexdigest()==row['chapter_sha256'],f'private chapter SHA wrong {n}')
    ps=[x.text_content().strip() for x in html.fromstring(data).xpath('//body//p') if x.text_content().strip()]
    ck(p<=len(ps),f'private paragraph missing {n}/{p}')
    if p<=len(ps):ck(hashlib.sha256(ps[p-1].encode()).hexdigest()==row['paragraph_sha256'],f'private paragraph SHA incorrect {n}/{p}')
  flagged=[r for r in rows if int(r['narrative_ordinal'])==519 and int(r['paragraph_index']) in (69,70)]
  ck(len(flagged)==2,'n519/p69 + corrective n519/p70 both required')
  if len(flagged)==2:
   ck(any('MISALIGNMENT' in x['evidence_role'] for x in flagged if int(x['paragraph_index'])==69),'R037 support-misalignment not flagged')
   ck(any('CORRECTIVE' in x['evidence_role'] for x in flagged if int(x['paragraph_index'])==70),'genuine corrective paragraph missing')
 finally:
  if archive: archive.close()
 print('R038', 'PASS' if not errs else 'FAIL',f'10 critiques + 10 concrete creative task candidates + {len(rows)} original SHA loci / {len(set(x["narrative_ordinal"] for x in rows))} chapters + six volumes + R037 misaligned p69 corrected by p70; A={"PRIVATE_ORIGINAL_SHA_VERIFIED" if src else "SOURCE_STRUCTURE_ONLY"}; B PROVISIONAL; C NOT_RUN')
 for e in errs:print('FAIL',e)
 return int(bool(errs))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source-dir');ns=p.parse_args();sys.exit(run(ns.source_dir))
