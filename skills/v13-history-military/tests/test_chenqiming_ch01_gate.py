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
        result=verify(project, 1)
        self.assertEqual(result["result"], "PASS_STRUCTURAL_GATE_ONLY")
        self.assertGreaterEqual(result["revisions"], 2)
        self.assertGreaterEqual(result["actors"], 2)
        self.assertGreaterEqual(result["scenes"], 2)
        self.assertGreaterEqual(result["events"], 1)

if __name__ == "__main__":
    unittest.main()
