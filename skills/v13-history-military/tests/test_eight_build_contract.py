#!/usr/bin/env python3
"""E01-E08 construction assertions. NOT independent V3, blind judging or literary evaluation."""
from pathlib import Path
import json
import re
import unittest

ROOT=Path(__file__).resolve().parent.parent
REPO=ROOT.parent.parent

class EightBuildContract(unittest.TestCase):
    def test_only_one_host_discoverable_skill_entry(self):
        entries=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob("SKILL.md")]
        self.assertEqual(entries,["SKILL.md"])
        self.assertTrue((ROOT/"nuwa-theme/TOPIC_OPERATIONS.md").is_file())
        self.assertIn("M4", (ROOT/"SKILL.md").read_text(encoding="utf-8"))
    def test_187_per_id_provenance_and_routing(self):
        a=(REPO/"v13_e/E01_187_METHOD_SOURCE_DECISIONS.tsv").read_text(encoding="utf-8").strip().splitlines()
        b=(REPO/"v13_e/E03_187_PROMOTION_ROUTING.tsv").read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual((len(a),len(b)),(188,188))
        headers=a[0].split("\t")
        rows=[dict(zip(headers,line.split("\t"))) for line in a[1:]]
        self.assertEqual(len(set(x["candidate_id"] for x in rows)),187)
        for x in rows:
            for field in ("title","loci","V1_scope_limited","failure_boundary","nonpromotion_reason"):
                self.assertTrue(x.get(field), f'{x["candidate_id"]} missing {field}')
            self.assertEqual(int(x["hash_prefix_conflicts"]),0)
        receipt=json.loads((REPO/"v13_e/E01_PRIVATE_EPUB_HASH_RESULT.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["total_unique_loci"],322)
        self.assertEqual(receipt["missing"],0)
    def test_twenty_original_multi_scene_prose_deliveries(self):
        for prefix in ("WM","TX"):
            for n in range(1,11):
                id=f"{prefix}-T{n:02}"
                file=ROOT/"examples/stage0"/f"{id}.md"
                text=file.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(text),1000,id)
                scenes=re.findall(r"^### [一二三四五六七八九十]+｜",text,re.MULTILINE)
                self.assertGreaterEqual(len(scenes),2,id)
                self.assertRegex(text,r"状态|事实账|关系事实|因果树|时延|节点|权责|后果|承诺账|职责|五账|事实／记忆|事实/记忆")
    def test_64_RIA_and_router_graph(self):
        caps=[]
        for book in ("wanming","tiexuecanming"):
            bundle=json.loads((ROOT/"capabilities/bundles"/f"{book}.json").read_text(encoding="utf-8"))
            self.assertFalse(bundle["cangjie_verified"])
            caps.extend(bundle["capabilities"])
        self.assertEqual(len(caps),64)
        for card in caps:
            text=(ROOT/card["card"]).read_text(encoding="utf-8")
            for name in ("R","I","A1","A2","E","B"):
                self.assertIn(f"## {name}｜",text)
            for path in card["also_read"]:
                self.assertTrue((ROOT/path).is_file(),path)
        edges=json.loads((ROOT/"capabilities/RELATIONSHIPS.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(edges["edges"]),18)
    def test_nuwa_phase1_phase2_phase3_material(self):
        d=ROOT/"nuwa-theme/references"
        self.assertTrue((d/"research/07-E06_PRIMARY_SIX_DIMENSION_DEEP_RESEARCH.md").exists())
        r=(d/"research/09-E07_MODELS_TRIPLE_GATE_AND_HEURISTICS.md").read_text(encoding="utf-8")
        o=json.loads((d/"MODEL_ROUTER.json").read_text(encoding="utf-8"))
        self.assertEqual((len(o["models"]),len(o["heuristics"])),(4,8))
        for m in o["models"]:
            self.assertIn(m["id"],r)
            self.assertTrue(m["triad"].get("cross_domain"))
            self.assertTrue(m["triad"].get("generativity"))
            self.assertTrue(m["triad"].get("distinctiveness"))
        self.assertTrue((ROOT/"nuwa-theme/TOPIC_OPERATIONS.md").is_file())
        self.assertEqual(o["independent_phase4"],"NOT_RUN_USER_WAIVED")
    def test_v13_whole_skill_retains_all_nine_domains_and_models(self):
        """Structural guard against a future prose-only or AI-flavor-only rewrite."""
        entry=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        router=(ROOT/"references/09-ROUTER_AND_HANDOFF.md").read_text(encoding="utf-8")
        audit=(ROOT/"references/07-EDITOR_AND_FAILURES.md").read_text(encoding="utf-8")
        index=(ROOT/"capabilities/INDEX.md").read_text(encoding="utf-8")
        nuwa=(ROOT/"nuwa-theme/TOPIC_OPERATIONS.md").read_text(encoding="utf-8")
        self.assertIn("整体创作能力运行协议",entry)
        self.assertIn("最近一次用户纠正什么，不等于下一次只执行什么",entry)
        self.assertIn("全域扫描",entry)
        self.assertIn("综合审稿",entry)
        for n in range(1,10):
            self.assertRegex(entry,rf"references/{n:02}-[A-Z_]+\\.md")
        for name in ("终局","财政","人物","历史","军事","连续性","文笔","心理","AI味","幽默"):
            self.assertIn(name,entry,name)
        for id in ("M1","M2","M3","M4","H01","H08"):
            self.assertIn(id,nuwa,id)
        self.assertIn("64张卡属于同一个作者能力系统",index)
        self.assertIn("整体能力的统一路由",router)
        self.assertIn("文学审稿必须与全部原有能力合并执行",audit)

    def test_two_complete_stage5_digest_and_package(self):
        for book in ("wanming","tiexuecanming"):
            digest=(REPO/"books"/book/"DIGEST.md").read_text(encoding="utf-8")
            self.assertTrue(5000<=len(digest)<=10000,book)
        for name in ("DIGEST_WANMING.md","DIGEST_TIEXUECANMING.md"):
            digest=(ROOT/"capabilities"/name).read_text(encoding="utf-8")
            self.assertTrue(5000<=len(digest)<=10000,name)
        from sys import path as syspath
        syspath.insert(0,str(ROOT/"scripts"))
        from build_release import verify
        status=verify()
        self.assertEqual(status["stage0_original_prose"],20)
        self.assertEqual(status["nuwa_models"],4)
        self.assertTrue(status["single_discoverable_entry"])

if __name__=="__main__":
    unittest.main()
