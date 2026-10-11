#!/usr/bin/env python3
"""A handoff must carry a lossless event ledger; display balances alone are insufficient."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from build_handoff import render
from validate_state import validate

STATE=json.loads((ROOT/"fixtures/chaoxun_ch04.json").read_text(encoding="utf-8"))

class HandoffRoundtrip(unittest.TestCase):
    def test_lossless_latest_ledger_survives_handoff(self):
        skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        last=(ROOT.parent.parent/"experiments/novel_field_test_20261012/CH04.md").read_text(encoding="utf-8")
        output=render(STATE,skill,last)
        raw=re.search(r"## B2\\. 完整事件账[^\\n]*\\n\\n```json\\n(.*?)\\n```",output,re.S)
        self.assertIsNotNone(raw,"event-sourced ledger missing from handoff")
        reconstructed=json.loads(raw.group(1))
        self.assertEqual(reconstructed,STATE)
        self.assertEqual(validate(reconstructed),validate(STATE))
        self.assertIn("第四章　两张纸的主人",output)
        self.assertIn("独立",output)
        self.assertEqual(reconstructed["independent_review"],"NOT_RUN")

    def test_cli_defaults_to_newest_written_chapter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"handoff.md"
            subprocess.run([sys.executable,str(ROOT/"scripts"/"build_handoff.py"),
                            "--out",str(path)],check=True,capture_output=True,text=True)
            output=path.read_text(encoding="utf-8")
            self.assertIn("第四章　两张纸的主人",output)
            self.assertIn('"id": "E06"',output)
            self.assertIn("## B2. 完整事件账",output)

if __name__=="__main__":
    unittest.main()
