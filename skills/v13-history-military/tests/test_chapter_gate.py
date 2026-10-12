"""Gate regression. Structural checks only, NOT independent literary assessment."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from chapter_gate import GateError, verify

class ChapterGateRegression(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.p = Path(tmp.name)
        (self.p/"PROJECT_BIBLE.md").write_text("陈启明：1639现代肉身直达崇祯御前；后去南阳。"*20,encoding="utf8")
        labels = ("可观察目标", "时间地点、人物站位和进入时动作",
                  "POV及其未知情报", "场内每人自身目标/能拒绝什么",
                  "行动→反应→逆转→选择→差分",
                  "退出场景时具体悬念", "跨三章因果义务")
        (self.p/"CHAPTER_001_BRIEF.md").write_text(
            "\n".join(f"{k}：守卫、主角和皇帝都要用现场行动付出代价。" for k in labels),
            encoding="utf8")
        self.draft_excerpt = "陈启明看见守卫的手指压着门，门外有人争着去登记这件事。"
        self.final_excerpt = "陈启明不肯承认从门进入，因为那份供状会牵连守卫，也会牵连自己。"
        draft=self.draft_excerpt+"\n"+("内侍只是附和皇帝，侍卫没有任何独立行动。\n"*40)
        final=self.final_excerpt+"\n"+("内侍另起一份记录，侍卫拒绝代签，两人的风险不能消除。\n"*40)
        (self.p/"CHAPTER_001_DRAFT.md").write_text(draft,encoding="utf8")
        (self.p/"CHAPTER_001.md").write_text(final,encoding="utf8")
        (self.p/"NEXT_SCENE.md").write_text("次日皇帝要核对两份不同的见证，而陈启明需要决定是否说出自己所知的未来。",
                                            encoding="utf8")
        self.receipt={
            "schema":"v13-chapter-review-receipt-1","chapter":1,"status":"REVISED_AND_RECHECKED",
            "opening_goal":"陈启明希望活下来并保存真实证词。",
            "exit_change":"两份不能互相覆盖的记录得以保存。",
            "unpaid_obligation":"御前第二次核验尚未发生，问话风险仍在。",
            "independent_characters":[
                {"name":"陈启明","wants":"活命和避免伪造证词","can_refuse":"拒绝编造进宫过程",
                 "choice":"要求另立两份记录","consequence":"增加自己的调查风险"},
                {"name":"守门侍卫","wants":"尽量保住职位","can_refuse":"拒绝证实没看见的事",
                 "choice":"保留亲见范围","consequence":"皇帝继续追究他的责任"}],
            "scenes":[
                {"entry":"主角突然出现","conflict":"门守认为他有刺杀嫌疑",
                 "choice":"拒绝编造解释","visible_delta":"证词存在争议","cost":"被单独监视"},
                {"entry":"内侍准备记档","conflict":"两种记法引起争论",
                 "choice":"守卫坚持个人所见","visible_delta":"保留两份记录","cost":"可能被追责"}],
            "applied_cards":[
                {"id":"WM-f01","why":"看见来历异事不等于承认身份",
                 "how":"皇帝尚未授权任何待遇","boundary":"身份与实权仍分离"}],
            "nuwa_models":[
                {"id":"M4","why":"同一事件有不同版本","observed_effect":"原始见闻保留两份"}],
            "history_boundaries":[
                {"claim":"甲士与内侍是虚构人物","classification":"IN_WORLD_FICTION",
                 "evidence_or_assumption":"原创小说拟定人物设定"}],
            "adversarial_fixes":[
                {"draft_excerpt":self.draft_excerpt,"fault":"主角缺乏直接决策",
                 "final_excerpt":self.final_excerpt,"state_delta":"两份证词形成冲突"},
                {"draft_excerpt":"内侍只是附和皇帝","fault":"配角没有拒绝权",
                 "final_excerpt":"内侍另起一份记录","state_delta":"内侍承担个人责任"}]
        }
        self.rfile=self.p/"CHAPTER_001_REVIEW.json"
        self.rfile.write_text(json.dumps(self.receipt,ensure_ascii=False),encoding="utf8")
        state={
            "schema":"v13-novel-alpha-ledger-1","project":"陈启明","initial_accounts":{"stock.dry":0,"cash.public":0},
            "expected_balances":{"stock.dry":0,"cash.public":0},"permissions":[],
            "facts":[],"characters":[],"independent_review":"NOT_RUN",
            "events":[{"id":"e1","chapter":1,"kind":"OBSERVED",
                       "evidence_ref":"CHAPTER_001.md:1","changes":[]}],
            "open_loops":["第二次核验"],"next_chapter_brief":"崇祯将要求两份证词里的差异逐项解释。"}
        (self.p/"STATE.json").write_text(json.dumps(state,ensure_ascii=False),encoding="utf8")

    def test_positive_structural_gate(self):
        self.assertEqual(verify(self.p,1)["result"],"PASS_STRUCTURAL_GATE_ONLY")

    def test_missing_review_blocks(self):
        self.rfile.unlink()
        with self.assertRaisesRegex(GateError,"missing artifact"):
            verify(self.p,1)

    def test_no_real_revision_blocks(self):
        (self.p/"CHAPTER_001.md").write_text(
            (self.p/"CHAPTER_001_DRAFT.md").read_text(encoding="utf8"),encoding="utf8")
        with self.assertRaises(GateError):
            verify(self.p,1)

    def test_missing_next_scene_blocks(self):
        (self.p/"NEXT_SCENE.md").write_text("无",encoding="utf8")
        with self.assertRaisesRegex(GateError,"NEXT_SCENE"):
            verify(self.p,1)

    def test_explicit_literary_rejection_blocks(self):
        self.receipt["literary_decision"]="LITERARY_REVISION_REQUIRED"
        self.rfile.write_text(json.dumps(self.receipt,ensure_ascii=False),encoding="utf8")
        with self.assertRaisesRegex(GateError,"known rejected literary draft"):
            verify(self.p,1)

    def test_thirteen_relevant_cards_are_not_silently_dropped(self):
        # A cross-domain chapter may genuinely trigger more than the
        # previous arbitrary 12-card ceiling; structure must permit it.
        ids=sorted(p.stem for p in (ROOT/"capabilities/cards").glob("*.md"))[:13]
        self.assertEqual(len(ids),13)
        original=self.receipt["applied_cards"][0]
        self.receipt["applied_cards"]=[
            {**original,"id":cid} for cid in ids
        ]
        self.rfile.write_text(json.dumps(self.receipt,ensure_ascii=False),encoding="utf8")
        self.assertEqual(len(verify(self.p,1)["cards"]),13)

    def test_duplicate_relevant_card_blocks(self):
        self.receipt["applied_cards"].append(dict(self.receipt["applied_cards"][0]))
        self.rfile.write_text(json.dumps(self.receipt,ensure_ascii=False),encoding="utf8")
        with self.assertRaisesRegex(GateError,"duplicate applied cards"):
            verify(self.p,1)

    def test_fake_card_blocks(self):
        self.receipt["applied_cards"][0]["id"]="FAKE-001"
        self.rfile.write_text(json.dumps(self.receipt,ensure_ascii=False),encoding="utf8")
        with self.assertRaisesRegex(GateError,"unknown card"):
            verify(self.p,1)

if __name__ == "__main__":
    unittest.main()
