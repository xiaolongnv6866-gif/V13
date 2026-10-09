#!/usr/bin/env python3
"""R041 Adler Critical + Applicability. Public CI checks structure, not B/C.
Private optional mode verifies actual supplied XHTML against SHA256 locators."""
import argparse,csv,hashlib,re,sys,zipfile
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'books/tiexuecanming/adler'
SOURCE_SHA='9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf'
ARCS=[(1,80),(81,160),(161,280),(281,400),(401,480),(481,532)]
def run(source_dir=None):
    errors=[]
    def ck(ok,msg):
        if not ok: errors.append(msg)
    evidence=D/'CRITIQUE_EVIDENCE.tsv'
    with evidence.open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    with (ROOT/'sources/metadata/tiexuecanming_v13_spine.csv').open(encoding='utf-8',newline='') as f:
        meta={int(x['narrative_ordinal']):x for x in csv.DictReader(f) if x['is_narrative_chapter']=='1'}
    ck(len(meta)==532,'expected 532 original narrative ordinal mappings')
    ck(len(rows)==63,'R041 requires 63 concrete original positions')
    ck(len({(r['narrative_ordinal'],r['paragraph_index']) for r in rows})==len(rows),'duplicate original locator')
    ck(len({r['narrative_ordinal'] for r in rows})==48,'expected 48 distinct original chapters')
    ck(set(r['proposition_id'] for r in rows)=={f'P{i:02d}' for i in range(1,11)},'ten propositions')
    ck(all(v>=6 for v in Counter(r['proposition_id'] for r in rows).values()),'each proposition >=6 source loci')
    ck(set(r['stage'] for r in rows)=={f'S{i}' for i in range(1,7)},'six narrative arcs')
    origins=Counter(r['origin'] for r in rows)
    ck(origins=={'R040_ORIGINAL_PRIVATE_R041_RECHECKED':51,'R041_NEW_PRIVATE_PARAGRAPH':12},f'wrong provenance {origins}')
    study=(D/'CRITIQUE_APPLICATION.md').read_text(encoding='utf-8')
    tasks=(D/'TASKS.md').read_text(encoding='utf-8')
    audit=(D/'CRITIQUE_QUALITY_AUDIT.md').read_text(encoding='utf-8')
    for i in range(1,11):
        ck(bool(re.search(rf'^### P{i:02d}｜',study,re.M)),f'P{i:02d} critical argument missing')
        ck(f'TX-T{i:02d}' in tasks,f'TX-T{i:02d} task missing')
    for s in ['最强反对意见','失效边界','n361/p35','n361/p36','n114/p27','n114/p29','n527/p30','n527/p31','n445/p1','SOURCE_FACT','CHARACTER_CLAIM','EXTERNAL_HISTORY','PROVISIONAL','NOT_RUN','R042']:
        ck(s in study,'critical check missing '+s)
    for s in ['陌生原创','验收','失败','输入','交付物','不适合','原书']:
        ck(s in tasks,'Applicability missing '+s)
    for s in ['SOURCE_STRUCTURE_ONLY','PRIVATE_ORIGINAL_SHA_VERIFIED','B PROVISIONAL','C NOT_RUN','R008','R024']:
        ck(s in audit,'quality separation missing '+s)
    ck(len(study)>7500 and len(tasks)>3400,'study / tasks too thin')
    source=None
    if source_dir:
        matches=list(Path(source_dir).glob('铁血残明*.epub'))
        ck(len(matches)==1,'exactly one private original EPUB required')
        if len(matches)==1:
            ck(hashlib.sha256(matches[0].read_bytes()).hexdigest()==SOURCE_SHA,'original full SHA mismatch')
            source=zipfile.ZipFile(matches[0])
            ck(source.testzip() is None,'original ZIP CRC invalid')
    try:
        for r in rows:
            n=int(r['narrative_ordinal']);p=int(r['paragraph_index']);m=meta.get(n)
            ck(m is not None,f'unknown source ordinal {n}')
            if not m: continue
            arc=next((i for i,(lo,hi) in enumerate(ARCS,1) if lo<=n<=hi),None)
            ck(r['stage']==f'S{arc}',f'wrong arc n{n}')
            for k in ('epub_path','spine_index','chapter_sha256'):
                ck(str(r[k])==str(m[k]),f'original metadata mismatch n{n}/{k}')
            ck(p>0 and len(r['paragraph_sha256'])==64,f'bad SHA locus n{n}p{p}')
            ck(r['source_check']=='PRIVATE_SHA_PASS' and r['literary_status']=='PROVISIONAL',f'false certification n{n}p{p}')
            ck(len(r['scene_fact'])>=12 and len(r['objection_or_boundary'])>=12,f'missing literary explanation n{n}p{p}')
            if source:
                from lxml import html
                raw=source.read(r['epub_path'])
                ck(hashlib.sha256(raw).hexdigest()==r['chapter_sha256'],f'XHTML chapter hash n{n}')
                ps=[q.text_content().strip() for q in html.fromstring(raw).xpath('//body//p') if q.text_content().strip()]
                ck(p<=len(ps),f'paragraph index n{n}p{p}')
                if p<=len(ps):
                    ck(hashlib.sha256(ps[p-1].encode('utf-8')).hexdigest()==r['paragraph_sha256'],f'paragraph content hash n{n}p{p}')
    finally:
        if source:source.close()
    print(f"R041 {'PASS' if not errors else 'FAIL'} 63 original positions, 48 distinct narrative chapters, 10 claims, 6 arcs, 12 NEW locators; A={'PRIVATE_ORIGINAL_SHA_VERIFIED' if source_dir else 'SOURCE_STRUCTURE_ONLY'}; B PROVISIONAL; C NOT_RUN")
    for e in errors: print('FAIL:',e)
    return int(bool(errors))
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-dir')
    sys.exit(run(parser.parse_args().source_dir))
