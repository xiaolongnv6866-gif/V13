#!/usr/bin/env python3
"""CH05 story and financial provenance regression; not a literary blind score."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
from validate_state import validate,LedgerError
OLD=json.loads((ROOT/"fixtures/chaoxun_ch04.json").read_text(encoding="utf-8"))
NEW=json.loads((ROOT/"fixtures/chaoxun_ch05.json").read_text(encoding="utf-8"))
PROSE=(ROOT.parent.parent/"experiments/novel_field_test_20261012/CH05.md").read_text(encoding="utf-8")

class ChapterFiveChecks(unittest.TestCase):
    def test_new_continuous_chapter_and_accounts(self):
        result=validate(NEW)
        self.assertEqual(result["events"],9)
        self.assertEqual(result["balances"],validate(OLD)["balances"])
        self.assertEqual(result["facts"]["east_17_households"],"HEARSAY")
        self.assertEqual(result["facts"]["you_san_grain_handling"],"REPORTED")
        self.assertEqual(result["independent_review"],"NOT_RUN")
        self.assertGreater(sum("\u4e00"<=c<="\u9fff" for c in PROSE),2000)
        for token in ("渡口","老陈","贺良","苏鹭","尤三","四十七","巡夜","丁掌柜"):
            self.assertIn(token,PROSE)

    def test_no_unwitnessed_inventory_credit(self):
        x=copy.deepcopy(OLD)
        x["events"].append({"id":"E07","chapter":5,"kind":"NOTE",
            "evidence_ref":"future goods merely promised",
            "changes":[{"account":"stock.dry","delta":5}],
            "permission_ids":[],"facts_updates":[]})
        x["expected_balances"]["stock.dry"]=19
        with self.assertRaisesRegex(LedgerError,"physical stock credit requires"):
            validate(x)

    def test_no_unwitnessed_cash_credit(self):
        x=copy.deepcopy(OLD)
        x["events"].append({"id":"E07","chapter":5,"kind":"PROMISE",
            "evidence_ref":"someone said money will arrive",
            "changes":[{"account":"cash.public","delta":5}],
            "permission_ids":[],"facts_updates":[]})
        x["expected_balances"]["cash.public"]=8
        with self.assertRaisesRegex(LedgerError,"public cash credit requires"):
            validate(x)

    def test_real_cash_receipt_event_can_credit(self):
        x=copy.deepcopy(OLD)
        x["events"].append({"id":"E07","chapter":5,"kind":"CASH_RECEIPT",
            "evidence_ref":"a separate fictional scenario",
            "receipt_evidence_ref":"scene signed money receipt",
            "changes":[{"account":"cash.public","delta":5}],
            "permission_ids":[],"facts_updates":[]})
        x["expected_balances"]["cash.public"]=8
        self.assertEqual(validate(x)["balances"]["cash.public"],8)

if __name__=="__main__":
    unittest.main()
