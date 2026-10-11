#!/usr/bin/env python3
"""Deterministically package the V13 writing Skill; structural build, NOT literary verification."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parent.parent
INCLUDED={".md",".tsv",".json",".py",".txt",".yaml",".yml"}

def inventory(root=ROOT):
    return sorted((p for p in root.rglob("*") if p.is_file()
                   and p.suffix in INCLUDED and "__pycache__" not in p.parts
                   and "dist" not in p.parts), key=lambda p:p.relative_to(root).as_posix())

def verify(root=ROOT):
    assert (root/"SKILL.md").exists()
    assert (root/"nuwa-theme/SKILL.md").exists()
    assert (root/"scripts/validate_state.py").exists()
    assert (root/"scripts/build_handoff.py").exists()
    cards=list((root/"capabilities/cards").glob("*.md"))
    assert len(cards)==64, f"Expected 64 source-bound RIA++ cards, got {len(cards)}"
    routes=(root/"routing/V1_187_FOURWAY_DELIVERY.tsv").read_text(encoding="utf-8").splitlines()
    assert len(routes)==188, f"Expected 187 historic cases, got {len(routes)-1}"
    for row in routes[1:]:
        fields=row.split("\t")
        if fields[-1].startswith("capabilities/cards/"):
            assert (root/fields[-1]).is_file(), fields[-1]
    for i in range(1,6):
        assert (root/f"examples/chaoxun/CH{i:02}.md").is_file()
    assert (root/"nuwa-theme/references/research/01-SOURCE_INVENTORY.md").is_file()
    return {"method_cards":len(cards),"historical_routes":len(routes)-1,
            "original_example_chapters":5,
            "files":len(inventory(root)),
            "independent_V3":"NOT_RUN_USER_WAIVED",
            "literary_blind_review":"NOT_RUN_USER_WAIVED"}

def build(destination,root=ROOT):
    info=verify(root)
    destination=Path(destination)
    destination.parent.mkdir(parents=True,exist_ok=True)
    manifest={}
    files=inventory(root)
    with zipfile.ZipFile(destination,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for path in files:
            rel=path.relative_to(root).as_posix()
            content=path.read_bytes()
            manifest[rel]=hashlib.sha256(content).hexdigest()
            name="v13-history-military/"+rel
            entry=zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0))
            entry.compress_type=zipfile.ZIP_DEFLATED
            entry.external_attr=0o644 << 16
            z.writestr(entry,content)
        entry=zipfile.ZipInfo("v13-history-military/BUILD_HASHES.json",date_time=(2026,1,1,0,0,0))
        entry.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(entry,json.dumps(manifest,indent=2,sort_keys=True,ensure_ascii=False).encode("utf-8"))
    return {"archive":str(destination),"sha256":hashlib.sha256(destination.read_bytes()).hexdigest(),**info}

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--out",type=Path,default=ROOT.parent.parent/"V13_HISTORY_MILITARY_SKILL.zip")
    a.add_argument("--check",action="store_true")
    x=a.parse_args()
    result=verify() if x.check else build(x.out)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
