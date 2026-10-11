#!/usr/bin/env python3
"""Verify the delivered structure. This is NOT a different model or an independent literary evaluator."""
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from build_release import verify

class ShippedSkillBuild(unittest.TestCase):
    def test_all_production_files_and_counts(self):
        info=verify()
        self.assertEqual(info["method_cards"],64)
        self.assertEqual(info["historical_routes"],187)
        self.assertEqual(info["original_example_chapters"],5)
    def test_book_bundles_and_methods(self):
        paths=set(p.name for p in (ROOT/"capabilities/cards").glob("*.md"))
        found=set()
        for book in ("wanming","tiexuecanming"):
            data=json.loads((ROOT/"capabilities/bundles"/(book+".json")).read_text(encoding="utf-8"))
            self.assertEqual(len(data["capabilities"]),32)
            self.assertFalse(data["cangjie_verified"])
            for method in data["capabilities"]:
                found.add(method["capability_id"]+".md")
        self.assertEqual(found,paths)
    def test_readable_task_paths(self):
        s=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        import re
        for path in re.findall(r"references/\d\d-[A-Z_]+\.md",s):
            self.assertTrue((ROOT/path).exists(),path)
        self.assertIn("NOT_RUN_USER_WAIVED",s)
    def test_valid_template(self):
        state=json.loads((ROOT/"templates/STATE_TEMPLATE.json").read_text(encoding="utf-8"))
        sys.path.insert(0,str(ROOT/"scripts"))
        from validate_state import validate
        self.assertEqual(validate(state)["events"],0)
        self.assertEqual(state["independent_review"],"NOT_RUN")

if __name__=="__main__":
    unittest.main()
