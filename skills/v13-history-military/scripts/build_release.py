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
    assert (root/"nuwa-theme/TOPIC_OPERATIONS.md").exists()
    assert [p.relative_to(root).as_posix() for p in root.rglob("SKILL.md")] == ["SKILL.md"], "Only one discoverable SKILL.md allowed"
    assert (root/"scripts/validate_state.py").exists()
    assert (root/"scripts/build_handoff.py").exists()
    assert (root/"scripts/chapter_gate.py").exists(), "chapter delivery gate must ship"
    assert (root/"templates/CHAPTER_REVIEW_RECEIPT.json").exists(), "review receipt must ship"
    assert (root/"tests/test_chapter_gate.py").exists(), "chapter gate negative tests must ship"
    entry=(root/"SKILL.md").read_text(encoding="utf-8")
    assert "章节交付门禁" in entry and "scripts/chapter_gate.py" in entry, "main entry must enforce chapter gate"

    cards=list((root/"capabilities/cards").glob("*.md"))
    assert len(cards)==64, f"Expected 64 source-bound RIA++ cards, got {len(cards)}"
    routes=(root/"routing/V1_187_FOURWAY_DELIVERY.tsv").read_text(encoding="utf-8").splitlines()
    assert len(routes)==188, f"Expected 187 historic cases, got {len(routes)-1}"
    for row in routes[1:]:
        fields=row.split("\t")
        if fields[-1].startswith("capabilities/cards/"):
            assert (root/fields[-1]).is_file(), fields[-1]
    stage0 = list((root/"examples/stage0").glob("??-T??.md"))
    assert len(stage0)==20, f"Expected 20 prose task deliveries, got {len(stage0)}"
    for prefix in ("WM","TX"):
        for i in range(1,11):
            p=root/"examples/stage0"/f"{prefix}-T{i:02}.md"
            assert p.is_file() and len(p.read_text(encoding="utf-8")) >= 750, p
    model=json.loads((root/"nuwa-theme/references/MODEL_ROUTER.json").read_text(encoding="utf-8"))
    assert len(model["models"])==4 and len(model["heuristics"])==8
    edges=json.loads((root/"capabilities/RELATIONSHIPS.json").read_text(encoding="utf-8"))["edges"]
    assert len(edges)>=18
    for book in ("wanming","tiexuecanming"):
        b=json.loads((root/"capabilities/bundles"/f"{book}.json").read_text(encoding="utf-8"))
        assert len(b["capabilities"])==32
        for c in b["capabilities"]:
            assert (root/c["card"]).is_file(),c["card"]
            for rel in c["also_read"]: assert (root/rel).is_file(),rel
            txt=(root/c["card"]).read_text(encoding="utf-8")
            assert all(f"## {section}｜" in txt for section in ("R","I","A1","A2","E","B")), c["capability_id"]
    for i in range(1,6):
        assert (root/f"examples/chaoxun/CH{i:02}.md").is_file()
    assert (root/"nuwa-theme/references/research/01-SOURCE_INVENTORY.md").is_file()
    return {"method_cards":len(cards),"historical_routes":len(routes)-1,
            "original_example_chapters":5,"stage0_original_prose":len(stage0),
            "nuwa_models":4,"nuwa_heuristics":8,"single_discoverable_entry":True,
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
