#!/usr/bin/env python3
"""Optional N17 PRIVATE EPUB independent hash/source_quote replay.
Run: python3 scripts/verify_v13_n17_epub.py '/private/path/晚明.epub'
Never upload novel XHTML to the public repository; this script performs on-device verification.
"""
import csv,hashlib,sys,zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED="a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082"
class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.inside=False;self.buf=[];self.pars=[]
    def handle_starttag(self, tag, attrs):
        if tag=="p":self.inside=True;self.buf=[]
    def handle_data(self,data):
        if self.inside:self.buf.append(data.strip())
    def handle_endtag(self,tag):
        if tag=="p" and self.inside:
            self.pars.append("".join(self.buf));self.buf=[];self.inside=False
def tsv(name):
    with (ROOT/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))
if len(sys.argv)!=2:raise SystemExit("Supply the user-provided private EPUB path; no downloaded/public sources are substituted.")
epub=Path(sys.argv[1])
with epub.open("rb") as f:
    dig=hashlib.sha256()
    for piece in iter(lambda:f.read(1024*1024),b""):dig.update(piece)
assert dig.hexdigest()==EXPECTED,"Wrong book or EPUB variant"
records={}
for name in ("FRAMEWORK_EVIDENCE","PRINCIPLE_EVIDENCE","CASE_EVIDENCE","COUNTEREXAMPLE_EVIDENCE","GLOSSARY_EVIDENCE"):
    for row in tsv(f"books/wanming/candidates/{name}.tsv"):
        loc=row["source_locus"]
        if loc in records:
            assert (row["epub_path"],row["paragraph_sha256"])==(records[loc]["epub_path"],records[loc]["paragraph_sha256"]),loc
        else:records[loc]=row
assert len(records)==145
cache={}
with zipfile.ZipFile(epub) as z:
    for loc,row in records.items():
        path=row["epub_path"]
        if path not in cache:
            raw=z.read(path)
            assert hashlib.sha256(raw).hexdigest()==row["chapter_sha256"],path
            parser=Paragraphs()
            parser.feed(raw.decode("utf-8"))
            cache[path]=parser.pars
        pidx=int(loc.split("/p")[1])-1
        paragraph=cache[path][pidx]
        assert hashlib.sha256(paragraph.encode("utf-8")).hexdigest()==row["paragraph_sha256"],loc
    for item in tsv("v13_3/n17/N17_WM_V1_91.tsv"):
        pidx=int(item["first_original_locus"].split("/p")[1])-1
        paragraph=cache[records[item["first_original_locus"]]["epub_path"]][pidx]
        assert paragraph.startswith(item["short_source_quote"]),item["candidate_id"]
print("PRIVATE EPUB V1 REPLAY PASS: 145/145 full paragraph SHA-256, all chapter SHA-256, 91/91 short direct quote provenance; NOT method V2/V3 proof")
