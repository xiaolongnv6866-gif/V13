#!/usr/bin/env python3
"""V13 independently rebuild metadata-only EPUB chapter index from supplied originals.

No original book prose or excerpts are exported. Chapters are in OPF spine order;
printed chapter labels may be discontinuous. V10–V12 indices are never consumed.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import re
import zipfile
from pathlib import Path
from posixpath import dirname, join, normpath
from lxml import etree, html

SOURCES = {
    "wanming": ("晚明", "a8f3b43dcd496822cd384ac8e9aa85f7dc374f8430f06c6f8321c26825093082", 571, 12),
    "tiexuecanming": ("铁血残明", "9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf", 532, 16),
}
RE_NUMBER = re.compile(r"^第\s*[0-9０-９一二三四五六七八九十百千零]+\s*章")

def file_sha(path):
    h=hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def locate(root, stem):
    matches=sorted(set(root.glob(stem+" *.epub")) | set(root.glob(stem+".epub")))
    if len(matches)!=1:raise RuntimeError(f"{stem}: expected one EPUB in {root}; found {len(matches)}")
    return matches[0]

def index_book(book_key, ebook, sha, expected_count, first_ordinal_spine):
    if actual:=file_sha(ebook):
        if actual!=sha:raise RuntimeError(f"{book_key}: EPUB SHA mismatch {actual}")
    records=[]
    with zipfile.ZipFile(ebook) as z:
        bad=z.testzip()
        if bad:raise RuntimeError(f"{book_key}: ZIP bad file {bad}")
        info=etree.fromstring(z.read("META-INF/container.xml"))
        roots=info.xpath('//*[local-name()="rootfile"]/@full-path')
        if len(roots)!=1:raise RuntimeError("Expected one OPF root")
        opfpath=roots[0]
        opf=etree.fromstring(z.read(opfpath))
        manifest={it.get("id"):it.get("href") for it in opf.xpath('//*[local-name()="manifest"]/*')}
        spine=opf.xpath('//*[local-name()="spine"]/*')
        for i,item in enumerate(spine):
            rel=manifest.get(item.get("idref"))
            if rel is None:raise RuntimeError(f"spine entry {i} missing manifest ID")
            path=normpath(join(dirname(opfpath),rel.split("#")[0]))
            raw=z.read(path)
            doc=html.fromstring(raw)
            headings=doc.xpath("//h1|//h2|//title")
            title=next((s for el in headings if (s:=el.text_content().strip())),"")
            body=doc.xpath("//body")
            txt=body[0].text_content().strip() if body else ""
            paras=[s.strip() for x in doc.xpath("//body//p") if (s:=x.text_content()).strip()]
            narrative = i>=first_ordinal_spine and bool(RE_NUMBER.match(title)) and len(txt)>200
            records.append({
                "book":book_key, "spine_index":i, "epub_path":path, "chapter_title":title,
                "body_characters":len(txt),"nonempty_paragraphs":len(paras),
                "chapter_sha256":hashlib.sha256(raw).hexdigest(),
                "is_narrative_chapter":int(narrative),"narrative_ordinal":""
            })
    counter=0
    for row in records:
        if row["is_narrative_chapter"]:
            counter+=1;row["narrative_ordinal"]=counter
    if counter!=expected_count:
        raise RuntimeError(f"{book_key}: expected {expected_count} narrative chapters, found {counter}; inspect frontmatter/section rules")
    return records

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-dir",type=Path,default=Path("/mnt/data"))
    parser.add_argument("--out-dir",type=Path,default=Path("sources/metadata"))
    args=parser.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    combined=0
    for key,(cn,sha,count,first) in SOURCES.items():
        epub=locate(args.source_dir,cn)
        rows=index_book(key,epub,sha,count,first)
        dest=args.out_dir/f"{key}_v13_spine.csv"
        with dest.open("w",encoding="utf-8",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            writer.writeheader();writer.writerows(rows)
        covered=sum(row["is_narrative_chapter"] for row in rows)
        combined+=covered
        print(f"PASS {key}: spine={len(rows)} narrative={covered}, output={dest}")
    print(f"PASS V13: combined narrative chapters {combined}")

if __name__=="__main__":main()
