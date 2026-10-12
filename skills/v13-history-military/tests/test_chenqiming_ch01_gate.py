"""Production chapter gate regression; verifies structure, not literary quality."""
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from chapter_gate import verify, GateError

class ChenQimingChapterOne(unittest.TestCase):
    def test_current_redraft_with_literary_rejection_is_not_released(self):
        project=ROOT.parent.parent / "novels" / "chen-qiming"
        content=(project/"CHAPTER_001.md").read_text(encoding="utf-8")
        self.assertNotIn("陈启明的左脚踩住了一张奏疏。", content)
        self.assertIn("宁武关", content)
        self.assertIn("八万", content)
        self.assertIn("许得安", content)
        self.assertIn("孙传庭", content)
        receipt=__import__("json").loads((project/"CHAPTER_001_REVIEW.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["literary_decision"],"LITERARY_REVISION_REQUIRED")
        self.assertGreaterEqual(receipt["editor_ai_flavor_severity_0_to_10"],7)
        self.assertEqual(receipt["user_acceptance"],"USER_REVIEW_PENDING")
        with self.assertRaisesRegex(GateError, "known rejected literary draft"):
            verify(project, 1)

if __name__ == "__main__":
    unittest.main()
