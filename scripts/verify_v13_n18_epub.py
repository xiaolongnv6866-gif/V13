#!/usr/bin/env python3
"""PRIVATE REPLAY of N18《铁血残明》 source hashes/short quotations; no public EPUB storage.
Usage: python3 scripts/verify_v13_n18_epub.py '/private/path/铁血残明.epub'
Requires beautifulsoup4 + lxml (install locally if missing); NOT run on GitHub Actions.
"""
from __future__ import annotations
import csv,hashlib,sys,zipfile,warnings
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BOOK_SHA="9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf"
def table(path):
    with (ROOT/path).open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
try:
    from bs4 import BeautifulSoup,XMLParsedAsHTMLWarning
except ImportError:
    raise SystemExit("Install pip packages beautifulsoup4 and lxml in the private verifier environment.")
warnings.filterwarnings("ignore",category=XMLParsedAsHTMLWarning)
if len(sys.argv)!=2: raise SystemExit("Usage: verify_v13_n18_epub.py path_to_user_original_private_epub")
path=Path(sys.argv[1])
sha=hashlib.sha256(path.read_bytes()).hexdigest()
assert sha==BOOK_SHA,("EPUB_SHA_CHANGED",sha)
sources={}
for name in ("FRAMEWORK_EVIDENCE","PRINCIPLE_EVIDENCE","CASE_EVIDENCE","COUNTEREXAMPLE_EVIDENCE","GLOSSARY_EVIDENCE"):
    for x in table(f"books/tiexuecanming/candidates/{name}.tsv"):
        loc=x["source_locus"]
        if loc in sources:
            previous=sources[loc]
            assert (previous["epub_path"],previous["paragraph_sha256"],previous["chapter_sha256"])==(x["epub_path"],x["paragraph_sha256"],x["chapter_sha256"]),loc
        else:sources[loc]=x
assert len(sources)==177
paragraphs={}
with zipfile.ZipFile(path) as z:
    for loc,source in sources.items():
        filename=source["epub_path"]
        if filename not in paragraphs:
            raw=z.read(filename)
            assert hashlib.sha256(raw).hexdigest()==source["chapter_sha256"],("CHAPTER_HASH",filename)
            soup=BeautifulSoup(raw,"lxml")
            paragraphs[filename]=[p.get_text("",strip=True) for p in soup.find_all("p")]
        pidx=int(loc.rsplit("/p",1)[1])-1
        arr=paragraphs[filename]
        assert 0<=pidx<len(arr),("PARAGRAPH_OUT_OF_RANGE",loc)
        current=arr[pidx]
        assert hashlib.sha256(current.encode("utf-8")).hexdigest()==source["paragraph_sha256"],("PARAGRAPH_HASH",loc)
    docs=table("v13_3/n18/N18_TX_V1_96.tsv")
    assert len(docs)==96
    for row in docs:
        source=sources[row["source_first_locus"]]
        pidx=int(row["source_first_locus"].rsplit("/p",1)[1])-1
        original=paragraphs[source["epub_path"]][pidx]
        assert original.startswith(row["short_source_quote"]),("QUOTE_NOT_FROM_SOURCE",row["candidate_id"])
assert len(paragraphs)==74
print("PASS PRIVATE N18 EPUB replay: original whole-book SHA, 74 chapter SHA, 177 paragraph SHA, 96 short exact quote beginnings; not V2, V3 or literature-effect certification.")
