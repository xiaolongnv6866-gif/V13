#!/usr/bin/env python3
"""Unit tests for the experimental state validator and explicit cross-chat handoff."""
import copy
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "scripts"))
from validate_state import LedgerError, validate
from build_handoff import render

DATA = json.loads((HERE / "fixtures" / "chaoxun_ch03.json").read_text(encoding="utf-8"))


class AlphaLedgerTests(unittest.TestCase):
    def test_real_three_chapter_fixture(self):
        result = validate(DATA)
        self.assertEqual(result["balances"]["stock.dry"], 14)
        self.assertEqual(result["balances"]["stock.wet"], 6)
        self.assertEqual(result["balances"]["stock.promised_not_arrived"], 12)
        self.assertEqual(result["balances"]["cash.public"], 3)
        self.assertEqual(result["balances"]["debt.wages"], 0)
        self.assertEqual(result["facts"]["east_17_households"], "HEARSAY")
        self.assertEqual(result["independent_review"], "NOT_RUN")

    def test_cannot_spend_more_cash_than_exists(self):
        x = copy.deepcopy(DATA)
        x["events"][3]["changes"][0]["delta"] = -8
        with self.assertRaisesRegex(LedgerError, "exceeds permission|negative balance"):
            validate(x)

    def test_cannot_distribute_without_signed_permission(self):
        x = copy.deepcopy(DATA)
        x["events"][2]["permission_ids"] = []
        with self.assertRaisesRegex(LedgerError, "without exactly one"):
            validate(x)

    def test_cannot_exceed_four_bag_authority(self):
        x = copy.deepcopy(DATA)
        x["events"][2]["changes"][0]["delta"] = -5
        with self.assertRaisesRegex(LedgerError, "exceeds permission"):
            validate(x)

    def test_cannot_pay_wages_by_erasing_debt_only(self):
        x = copy.deepcopy(DATA)
        x["events"][3]["changes"] = [{"account": "debt.wages", "delta": -3}]
        with self.assertRaisesRegex(LedgerError, "without corresponding cash payment"):
            validate(x)

    def test_cannot_promote_hearsay_to_confirmed_without_proof(self):
        x = copy.deepcopy(DATA)
        x["events"][3]["facts_updates"] = [{
            "fact_id": "east_17_households", "status": "CONFIRMED"
        }]
        with self.assertRaisesRegex(LedgerError, "rumor promoted"):
            validate(x)

    def test_no_unwitnessed_promised_stock_transfer(self):
        x = copy.deepcopy(DATA)
        x["events"].append({
            "id":"E05","chapter":4,"kind":"ESTIMATE",
            "evidence_ref":"someone hopes the supplies arrived",
            "changes":[{"account":"stock.promised_not_arrived","delta":-4}],
            "permission_ids":[],"facts_updates":[]
        })
        with self.assertRaisesRegex(LedgerError, "witnessed receipt"):
            validate(x)

    def test_actual_receipt_not_automatically_cash(self):
        x = copy.deepcopy(DATA)
        x["events"].append({
            "id":"E05","chapter":4,"kind":"RECEIPT",
            "evidence_ref":"CH04 receipt witnessed",
            "receipt_evidence_ref":"CH04 signed actual receipt",
            "changes":[
                {"account":"stock.promised_not_arrived","delta":-4},
                {"account":"stock.dry","delta":4}
            ],
            "permission_ids":[],"facts_updates":[]
        })
        # Contradictory declared final accounts must fail; a changed story must update the ledger.
        with self.assertRaisesRegex(LedgerError, "expected balance differs"):
            validate(x)
        x["expected_balances"]["stock.promised_not_arrived"] = 8
        x["expected_balances"]["stock.dry"] = 18
        self.assertEqual(validate(x)["balances"]["stock.dry"],18)

    def test_duplicate_event_is_rejected(self):
        x=copy.deepcopy(DATA)
        x["events"][1]["id"]=x["events"][0]["id"]
        with self.assertRaisesRegex(LedgerError,"duplicate event"):
            validate(x)

    def test_future_authority_cannot_be_used_in_chapter_one(self):
        x=copy.deepcopy(DATA)
        x["events"][2]["chapter"]=2
        with self.assertRaisesRegex(LedgerError,"outside valid time"):
            validate(x)

    def test_handoff_is_useful_without_original_books(self):
        skill=(HERE/"SKILL.md").read_text(encoding="utf-8")
        chapter=(HERE.parent.parent/"experiments/novel_field_test_20261012/CH03.md").read_text(encoding="utf-8")
        output=render(DATA,skill,chapter)
        for item in ("## B. 已核账的续写状态", "## C. 事实可靠等级",
                     "## D. 人物各自所知与目标","## E. 待偿的真实因果",
                     "14","3","HEARSAY","吴嫂","第二张收单","CHAPTER"):
            self.assertIn(item,output)
        self.assertNotIn("已通过独立盲测",output)

    def test_relative_skill_references(self):
        skill=(HERE/"SKILL.md").read_text(encoding="utf-8")
        for ref in ("references/NARRATIVE_ENGINE.md",
                    "references/STATE_PROTOCOL.md",
                    "references/EDITOR_PROTOCOL.md",
                    "templates/CHAPTER_BRIEF.md",
                    "templates/STATE_TEMPLATE.json",
                    "scripts/validate_state.py",
                    "scripts/build_handoff.py"):
            self.assertIn(ref,skill)
            self.assertTrue((HERE/ref).is_file(),ref)


if __name__=="__main__":
    unittest.main()
