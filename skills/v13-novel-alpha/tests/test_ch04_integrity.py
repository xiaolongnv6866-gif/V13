#!/usr/bin/env python3
"""New chapter continuation and deliberate invalid-event regression checks.

These are structural/continuity diagnostics, not independent literary scores.
"""
import copy
import json
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(HERE/"scripts"))
from validate_state import validate,LedgerError

OLD=json.loads((HERE/"fixtures"/"chaoxun_ch03.json").read_text(encoding="utf-8"))
NEW=json.loads((HERE/"fixtures"/"chaoxun_ch04.json").read_text(encoding="utf-8"))
PROSE=(HERE.parent.parent/"experiments"/"novel_field_test_20261012"/"CH04.md").read_text(encoding="utf-8")

class FourthChapterIntegrity(unittest.TestCase):
    def test_continuity_and_no_false_payment(self):
        result=validate(NEW)
        self.assertEqual(result["events"],6)
        self.assertEqual(result["balances"],validate(OLD)["balances"])
        self.assertEqual(result["facts"]["east_17_households"],"HEARSAY")
        self.assertEqual(result["facts"]["east_original_wrapper"],"REPORTED")
        self.assertEqual(result["independent_review"],"NOT_RUN")
        self.assertIn("沈茂生",PROSE)
        self.assertIn("祁四娘",PROSE)
        self.assertIn("四十七",PROSE)
        self.assertGreater(sum("\u4e00"<=c<="\u9fff" for c in PROSE),1400)

    def test_receipt_must_credit_physical_stock(self):
        fake=copy.deepcopy(OLD)
        fake["events"].append({"id":"E05","chapter":4,"kind":"RECEIPT",
            "evidence_ref":"unverified claim","receipt_evidence_ref":"some paper",
            "changes":[{"account":"stock.promised_not_arrived","delta":-4}],
            "permission_ids":[],"facts_updates":[]})
        fake["expected_balances"]["stock.promised_not_arrived"]=8
        with self.assertRaisesRegex(LedgerError,"conserve physical stock"):
            validate(fake)

    def test_receipt_cannot_double_physical_credit(self):
        fake=copy.deepcopy(OLD)
        fake["events"].append({"id":"E05","chapter":4,"kind":"RECEIPT",
            "evidence_ref":"unverified claim","receipt_evidence_ref":"some paper",
            "changes":[{"account":"stock.promised_not_arrived","delta":-4},
                       {"account":"stock.dry","delta":8}],
            "permission_ids":[],"facts_updates":[]})
        fake["expected_balances"]["stock.promised_not_arrived"]=8
        fake["expected_balances"]["stock.dry"]=22
        with self.assertRaisesRegex(LedgerError,"conserve physical stock"):
            validate(fake)

    def test_false_grant_event_rejected(self):
        fake=copy.deepcopy(OLD)
        fake["events"][1]["kind"]="DOCUMENT_OBSERVATION"
        with self.assertRaisesRegex(LedgerError,"not an authorization"):
            validate(fake)

    def test_unknown_permission_reference_rejected(self):
        fake=copy.deepcopy(OLD)
        fake["events"][0]["permission_ids"]=["P_NOT_EXIST"]
        with self.assertRaisesRegex(LedgerError,"unknown permission ID"):
            validate(fake)

if __name__=="__main__":
    unittest.main()
