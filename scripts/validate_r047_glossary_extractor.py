#!/usr/bin/env python3
"""V13 R047 original Cangjie glossary Stage1 public structural gate.

Private EPUB quotation semantics / author attribution require later V1 proof.
"""
from pathlib import Path
import csv, json, re, sys
R=Path(__file__).resolve().parents[1]
P=R/'books/wanming/candidates'
err=[]
def ck(ok,msg):
 if not ok:err.append(msg)
def readtsv(p):
 with p.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
paths=[P/x for x in ['glossary.md','GLOSSARY_EVIDENCE.tsv','GLOSSARY_CENSUS.tsv','GLOSSARY_AUDIT.md']]
for p in paths:ck(p.is_file(),str(p)+' missing')
if err:
 for x in err:print('FAIL:',x)
 sys.exit(1)
s=paths[0].read_text(encoding='utf8')
start=s.find('- id: g01')
end=s.find('## 术语筛选边界',start)
ck(start>=0 and end>start,'glossary YAML block missing')
blocks=re.split(r'(?=^- id: g\d{2}$)',s[start:end] if start>=0 and end>start else '',flags=re.M)
terms=[x for x in blocks if x.strip() and x.lstrip().startswith('- id: g')]
ids=[re.match(r'^- id: (g\d{2})',x.lstrip()).group(1) for x in terms]
ck(ids==[f'g{i:02}' for i in range(1,19)],'18 original glossary IDs incomplete or duplicated')
locs=set();links=set();terms_map={}
required=['term','type','source_chapter','source_quote','source_quote_status','author_definition','definition_status','textual_usage','key_distinction','why_it_matters','provenance','source_loci','corpus_occurrences','source_chapter_hits','summary','tags','task_ids','missing_conditions','verification_state']
for unit in terms:
 mid=re.match(r'^- id: (g\d{2})',unit.lstrip()).group(1)
 for key in required:ck(bool(re.search(r'^  '+key+r':',unit,re.M)),mid+' missing '+key)
 m=re.search(r'^  term: "([^"]+)"',unit,re.M)
 if not m:err.append(mid+' missing literal term');continue
 word=m.group(1)
 ck('type: term' in unit and 'source_quote: ""' in unit,mid+' invalid original type or copyrighted excerpt')
 ck('source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA' in unit,mid+' ungrounded quote omission')
 ck('author_definition: ""' in unit and 'definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION' in unit,mid+' falsely claimed author authored a definition')
 ck('verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN' in unit,mid+' prematurely certified')
 ex=re.search(r'^  corpus_occurrences: (\d+)',unit,re.M); ch=re.search(r'^  source_chapter_hits: (\d+)',unit,re.M)
 ck(bool(ex and ch and int(ex.group(1))>=3 and int(ch.group(1))>=2),mid+' frequency below upstream term admission rule')
 refs=re.findall(r'^    - "(n\d{3}/p\d+)"',unit,re.M)
 ck(len(refs)==2,mid+' requires two independent original context paragraph anchors')
 locs.update(refs)
 summary=unit.split('  summary: |-',1)[-1].split('  tags:',1)[0]
 ck(len([v for v in summary.splitlines() if v.startswith('    ')])>=5,mid+' insufficient contextual distinction and limitations')
 m2=re.search(r'^  task_ids: \[([^\]]+)\]',unit,re.M)
 if m2:links.update(x.strip() for x in m2.group(1).split(','))
 terms_map[mid]=(word,int(ex.group(1)) if ex else -1,int(ch.group(1)) if ch else -1)
ck(len({x[0] for x in terms_map.values()})==18,'duplicated glossary terms')
ck(links=={f'WM-{i:02}' for i in range(1,10)},'Stage0 nine independent tasks not mapped at raw glossary level')
anchors=readtsv(paths[1]);census=readtsv(paths[2])
ck(len(anchors)==34 and len({x['source_locus'] for x in anchors})==34,'34 unique original paragraph anchors expected')
ck(set(x['source_locus'] for x in anchors)==locs,'candidate citation and source ledger mismatch')
ck(len(census)==18 and len({x['term_id'] for x in census})==18,'18 exact term frequency census entries expected')
for x in census:
 idx=x['term_id']
 ck(idx in terms_map,'census ID not found in terms')
 if idx in terms_map:
  ck((x['term'],int(x['original_epub_exact_substring_occurrences']),int(x['narrative_chapters_with_hit']))==terms_map[idx],'census term/frequency does not match raw glossary')
 ck(x['census_basis']=='ALL_571_NARRATIVE_EPUB_BODY_PARAGRAPHS_EXACT_SUBSTRING' and x['definition_claim_status']=='NO_EXPLICIT_AUTHOR_DEFINITION_CLAIMED','source census scope overstated')
with (R/'sources/metadata/wanming_v13_spine.csv').open(encoding='utf8',newline='') as f:
 spine={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
ck(len(spine)==571,'frozen R002 chapter index changed')
chap=set();arcs=set()
for x in anchors:
 try:
  m=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert m
  n,p=map(int,m.groups());c=spine[n];chap.add(n)
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),x['source_locus']+' point mismatch')
  ck(1<=p<=int(c['nonempty_paragraphs']),x['source_locus']+' paragraph outside original chapter')
  ck(x['epub_path']==c['epub_path'] and x['chapter_sha256']==c['chapter_sha256'],x['source_locus']+' original chapter path/SHA mismatch')
  ck(bool(re.fullmatch(r'[a-f0-9]{64}',x['paragraph_sha256'])),x['source_locus']+' invalid original paragraph SHA')
  ck(x['verification']=='PRIVATE_EPUB_ACTUAL_SHA_RECHECK' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN',x['source_locus']+' verification metadata inflated')
  arcs.add(1 if n<=51 else 2 if n<=105 else 3 if n<=155 else 4 if n<=271 else 5 if n<=487 else 6)
 except (KeyError,AssertionError,TypeError,ValueError) as e:err.append('invalid source anchor '+str(e))
ck(len(chap)==27 and arcs==set(range(1,7)),'27 actual chapters and six full story arcs required')
audit=paths[3].read_text(encoding='utf8')
for k in ['CI_CLASSIFICATION: SOURCE_STRUCTURE_ONLY','18个','34个','27个','571','30,221','2,245,824','SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION','PROVISIONAL','NOT_RUN','R048']:
 ck(k in audit,'audit report incomplete '+k)
with (R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv').open(encoding='utf8',newline='') as f:old=list(csv.DictReader(f,delimiter='\t'))
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'legacy source quarantine gate lost')
cur=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
ck(int(cur['current_round'][1:])>=48 and int(cur['last_passed_round'][1:])>=47 and cur['rounds_completed']>=47,'R047 not formally passed')
if cur['current_round']=='R048':ck(cur['round_status']=='NOT_STARTED' and cur['rounds_completed']==47,'R048 started without a separate user trigger')
ck(cur['cangjie_stage0_gate']=='PASSED' and cur['legacy_quality_debt_status']=='OPEN_QUARANTINED','Stage0 signoff or historical debt lost')
ck(cur['skill_certified_count']==0 and cur['heldout_bank_status']=='SEALED_NOT_RUN' and cur['original_output_test_status']=='NOT_RUN','premature certification/test')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ledger={x['id']:x for x in csv.DictReader(f)}
ck(ledger['R047']['status']=='PASSED','R047 ledger not PASSED')
if cur['current_round']=='R048':ck(ledger['R048']['status']=='NOT_STARTED','R048 ledger prematurely started')
for x in err:print('FAIL:',x)
print('R047', 'FAIL' if err else 'PASS','18 source-bound glossary terms / 34 source paragraph anchors / 27 original chapters / 9 task links / six arcs; public SOURCE_STRUCTURE_ONLY, B PROVISIONAL C NOT_RUN')
sys.exit(bool(err))
