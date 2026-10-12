"""Production chapter gate regression; verifies structure, not literary quality."""
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from chapter_gate import verify

class ChenQimingChapterOne(unittest.TestCase):
    def test_current_redraft_has_actual_complete_production_receipt(self):
        project=ROOT.parent.parent / "novels" / "chen-qiming"
        content=(project/"CHAPTER_001.md").read_text(encoding="utf-8")
        self.assertNotIn("陈启明的左脚踩住了一张奏疏。", content)
        self.assertIn("宁武关", content)
        self.assertIn("八万", content)
        self.assertIn("许得安", content)
        self.assertIn("孙传庭", content)
        receipt=__import__("json").loads((project/"CHAPTER_001_REVIEW.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["literary_decision"],"EDITOR_ACCEPTABLE_SELF_REVIEW")
        self.assertEqual(receipt["user_acceptance"],"USER_REVIEW_PENDING")
        result=verify(project, 1)
        self.assertEqual(result["result"], "PASS_STRUCTURAL_GATE_ONLY")
        self.assertGreaterEqual(result["revisions"], 2)
        self.assertGreaterEqual(result["actors"], 2)
        self.assertGreaterEqual(result["scenes"], 2)
        self.assertGreaterEqual(result["events"], 1)

if __name__ == "__main__":
    unittest.main()
