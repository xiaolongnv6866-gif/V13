#!/usr/bin/env python3
"""V13 R052 pinned original Cangjie independent glossary SOURCE_STRUCTURE_ONLY check."""
from pathlib import Path
import csv,json,re,sys
R=Path(__file__).resolve().parents[1];B=R/'books/tiexuecanming/candidates';errors=[]
def ck(v,msg):
 if not v:errors.append(msg)
def tsv(file):
 with file.open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
s=(B/'glossary.md').read_text(encoding='utf8')
a=s.find('- id: g01');b=s.find('## 术语筛选边界',a)
ck(a>=0 and b>a,'missing glossary yaml span')
records=[v for v in re.split(r'(?=^- id: g\d\d$)',s[a:b] if a>=0 and b>a else '',flags=re.M) if v.lstrip().startswith('- id: g')]
ids=[re.match(r'^- id: (g\d\d)',v.lstrip()).group(1) for v in records]
ck(ids==[f'g{i:02}' for i in range(1,21)],'require 20 distinct glossary IDs')
matches={};anchors=set();tasks=set()
required=['term','type','source_chapter','source_quote','source_quote_status','author_definition','definition_status','textual_usage','key_distinction','why_it_matters','provenance','source_loci','corpus_occurrences','source_chapter_hits','summary','tags','task_ids','missing_conditions','verification_state']
for id,v in zip(ids,records):
 for field in required:ck(re.search(r'(?m)^  '+field+r':',v) is not None,id+' missing '+field)
 t=re.search(r'(?m)^  term: "([^"]+)"',v);occ=re.search(r'(?m)^  corpus_occurrences: (\d+)',v);ch=re.search(r'(?m)^  source_chapter_hits: (\d+)',v)
 ck(bool(t and occ and ch),id+' census fields')
 if not(t and occ and ch):continue
 matches[id]=(t.group(1),int(occ.group(1)),int(ch.group(1)))
 ck(int(occ.group(1))>=3 and int(ch.group(1))>=2,id+' too rare without explicit definition')
 ck('type: term' in v and 'source_quote: ""' in v,id+' wrong category/copyright')
 ck('source_quote_status: COPYRIGHT_OMITTED_PRIVATE_SHA' in v,id+' source_quote_status')
 ck('author_definition: ""' in v and 'definition_status: SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION' in v,id+' invented author definition')
 ck('verification_state: STAGE1_RAW_B_PROVISIONAL_C_NOT_RUN' in v,id+' premature B/C certification')
 loc=re.findall(r'^    - "(n\d{3}/p\d+)"',v,re.M)
 ck(len(loc)==2 and len(set(loc))==2,id+' requires two genuine paragraph contexts')
 anchors.update(loc)
 summary=v.split('  summary: |-',1)[-1].split('  tags:',1)[0]
 ck(len([line for line in summary.splitlines() if line.startswith('    ')])>=5,id+' insufficient contextual detail')
 task=re.search(r'(?m)^  task_ids: \[([^]]+)\]',v)
 if task:tasks.update(x.strip() for x in task.group(1).split(','))
ck(len(set(x[0] for x in matches.values()))==20,'duplicate term')
ck(tasks=={f'TX-{i:02}' for i in range(1,11)},'all 10 Stage0 independent tasks raw mapped')
ev=tsv(B/'GLOSSARY_EVIDENCE.tsv');census=tsv(B/'GLOSSARY_CENSUS.tsv')
ck(len(ev)==40 and len({x['source_locus'] for x in ev})==40,'40 real source anchor records')
ck(anchors=={x['source_locus'] for x in ev},'source/candidate loc mismatch')
ck(len(census)==20 and len({x['term_id'] for x in census})==20,'20 census rows')
for row in census:
 id=row['term_id'];ck(id in matches,'census id absent')
 if id in matches:
  ck((row['term'],int(row['original_epub_exact_substring_occurrences']),int(row['narrative_chapters_with_hit']))==matches[id],id+' census differs from candidate')
 ck(row['census_basis']=='ALL_532_NARRATIVE_EPUB_BODY_PARAGRAPHS_EXACT_SUBSTRING' and row['definition_claim_status']=='NO_EXPLICIT_AUTHOR_DEFINITION_CLAIMED','census claim not honest')
with (R/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf8',newline='') as f:meta={int(v['narrative_ordinal']):v for v in csv.DictReader(f) if v['is_narrative_chapter']=='1'}
ck(len(meta)==532,'frozen OPF changed')
chapters=set();arcs=set()
for x in ev:
 try:
  mt=re.fullmatch(r'n(\d{3})/p(\d+)',x['source_locus']);assert mt
  n,p=map(int,mt.groups());m=meta[n];chapters.add(n)
  ck(n==int(x['narrative_ordinal']) and p==int(x['paragraph_index']),'source ordinal')
  ck(1<=p<=int(m['nonempty_paragraphs']),'source paragraph range')
  ck(x['epub_path']==m['epub_path'] and x['chapter_sha256']==m['chapter_sha256'],'frozen source chapter/path')
  ck(bool(re.fullmatch('[0-9a-f]{64}',x['paragraph_sha256'])),'bad actual original SHA')
  ck(x['term_id'] in matches and x['term']==matches[x['term_id']][0],'source term linkage')
  ck(x['verification']=='PRIVATE_EPUB_ACTUAL_SHA_RECHECK' and x['literary_status']=='B_PROVISIONAL_C_NOT_RUN','incorrect private source state')
  arcs.add(1 if n<=80 else 2 if n<=160 else 3 if n<=280 else 4 if n<=400 else 5 if n<=480 else 6)
 except Exception as ex:errors.append('bad source anchor '+str(ex))
ck(len(chapters)==38 and len(arcs)==6,'coverage six novel arcs and expected source chapters')
audit=(B/'GLOSSARY_AUDIT.md').read_text(encoding='utf8')
for tok in ['532','33,278','2,087,500','20个','40处','38个','SOURCE_STRUCTURE_ONLY','PROVISIONAL','NOT_RUN','R053','SOURCE_CONTEXT_PARAPHRASE_NOT_EXPLICIT_AUTHOR_DEFINITION']:
 ck(tok in audit,'missing audit marker '+tok)
old=tsv(R/'cangjie/reading/R042_OLD_CLAIM_QUARANTINE.tsv')
ck(len(old)==14 and all(x['stage1_permission']=='NO_DIRECT_PROMOTION_RECONSTRUCT_FROM_SOURCE' for x in old),'old source debt accidentally promoted')
ctrl=json.loads((R/'CURRENT_ROUND.json').read_text(encoding='utf8'))
number=int(ctrl['current_round'][1:])
ck((ctrl["round_status"]=="NOT_STARTED" or (ctrl["current_round"]=="R057" and ctrl["round_status"]=="BLOCKED" and ctrl["rounds_completed"]==56 and ctrl["last_passed_round"]=="R056" and ctrl.get("cangjie_stage1_5_user_confirm") in ("PENDING_R057_USER_APPROVAL","USER_APPROVED_R057_TRIAGE_SCHEME_A_EXECUTION_SCOPE_PENDING"))) and ((number==52 and ctrl['rounds_completed']==51 and ctrl['last_passed_round']=='R051') or (number>=53 and ctrl['rounds_completed']==number-1 and int(ctrl['last_passed_round'][1:])>=52)),'R052 cursor mismatch')
ck(ctrl['cangjie_stage0_gate']=='PASSED' and ctrl['legacy_quality_debt_status']=='OPEN_QUARANTINED','Stage0/old debt barrier changed')
ck(ctrl['skill_certified_count']==0 and ctrl['heldout_bank_status']=='SEALED_NOT_RUN' and ctrl['original_output_test_status']=='NOT_RUN','premature skill certification')
with (R/'ROUND_LEDGER.csv').open(encoding='utf8',newline='') as f:ld={x['id']:x for x in csv.DictReader(f)}
ck(ld['R051']['status']=='PASSED','R051 prior checkpoint lost')
ck(ld['R052']['status']==('NOT_STARTED' if number==52 else 'PASSED'),'R052 bookkeeping mismatch')
if number==53:ck(ld['R053']['status']=='NOT_STARTED','R053 cannot automatically start')
for msg in errors:print('FAIL:',msg)
print('R052','FAIL' if errors else 'PASS','20 candidate terms, 40 source SHA, 38 chapters, 10 TX, six arcs; SOURCE_STRUCTURE_ONLY, B PROVISIONAL C NOT_RUN')
sys.exit(bool(errors))
