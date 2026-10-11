#!/usr/bin/env python3
"""Recover the approved W5 authority, never the archived V4 N21 cursor."""
from pathlib import Path
import json,csv,subprocess,sys
P=Path(__file__).resolve().parents[1]
def read(name): return (P/name).read_text(encoding="utf-8")
s=json.loads(read("V13_W_CURRENT_V5.json"))
ledger=list(csv.DictReader(read("V13_W_LEDGER_V5.tsv").splitlines(),delimiter="\t"))
if "--check" in sys.argv:
    for script in ("validate_v13_w5.py","validate_v13_v4_sync.py","validate_v13_governance.py","validate_v13_global_traceability.py","validate_v13_full_skill_contract.py"):
        subprocess.run([sys.executable,str(P/"scripts"/script)],check=True)
p=next((x for x in ledger if x["work_package"]==s["current_package"]),None)
if not p or p["status"]!=s["current_package_status"]: raise SystemExit("BLOCKED: W5 cursor/ledger mismatch")
print(json.dumps({"authority":[s["plan"],s["ledger"],"V13_W_CURRENT_V5.json"],"current_work_package":p["work_package"],"status":p["status"],"completed":s["completed_packages"],"total":s["total_packages"],"scope":p["scope"],"acceptance":p["acceptance"],"old_n_contracts":p["original_n_rounds"],"old_r_contracts":p["original_r_contracts"],"approval":p["user_confirmation"],"source_skills":[s["pinned_cangjie"],s["pinned_nuwa"]],"history":"V4 N01-N20 PASSED preserved as read-only snapshot; N21-N48 mapped to W01-W11","quality_limits":["no false independent judges","no copyrighted EPUB publication","no unverified SKILL certification"]},ensure_ascii=False,indent=2))
