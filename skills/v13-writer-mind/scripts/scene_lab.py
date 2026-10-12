#!/usr/bin/env python3
"""V13 same-scene literary rehearsal ledger.

Uses only Python standard library. Preserves a fixed prompt, immutable drafts,
and human feedback; never evaluates literary quality or modifies Canon.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def case_dir(root: Path, case: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", case):
        raise ValueError("case must be 1-64 ASCII letters/digits/_/- and start alphanumeric")
    return root.resolve() / case


def read_nonempty(path: Path) -> bytes:
    data = path.read_bytes()
    if not data.strip():
        raise ValueError(f"empty source is not a valid artifact: {path}")
    data.decode("utf-8")
    return data


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    fd, tmp = tempfile.mkstemp(prefix=".manifest-", suffix=".json.tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as fp:
            fp.write(encoded)
            fp.flush()
            os.fsync(fp.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def load(root: Path, case: str) -> tuple[Path, dict]:
    directory = case_dir(root, case)
    manifest_path = directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != 1 or manifest.get("case") != case:
        raise ValueError("unknown or inconsistent manifest")
    check_file(directory / "PROMPT_LOCK.md", manifest["prompt_sha256"], "PROMPT_LOCK")
    return directory, manifest


def check_file(path: Path, expected: str, description: str) -> None:
    if not path.is_file():
        raise ValueError(f"missing {description}: {path}")
    actual = sha(path.read_bytes())
    if actual != expected:
        raise ValueError(f"{description} modified after registration: {path}")


def init(args: argparse.Namespace) -> None:
    directory = case_dir(args.root, args.case)
    data = read_nonempty(args.prompt)
    # Refuse collision rather than silently changing the fixed scene.
    directory.mkdir(parents=True, exist_ok=False)
    (directory / "drafts").mkdir()
    (directory / "feedback").mkdir()
    (directory / "PROMPT_LOCK.md").write_bytes(data)
    manifest = {
        "schema": 1,
        "case": args.case,
        "prompt_sha256": sha(data),
        "created_at": utc_now(),
        "versions": [],
    }
    atomic_json(directory / "manifest.json", manifest)
    print(f"INITIALIZED {directory} lock_sha256={manifest['prompt_sha256']}")


def submit(args: argparse.Namespace) -> None:
    directory, manifest = load(args.root, args.case)
    data = read_nonempty(args.draft)
    versions = manifest["versions"]
    if versions:
        # Do not append onto an undetected edited manuscript.
        verify_records(directory, manifest)
    number = len(versions) + 1
    version = f"V{number:03d}"
    relative = f"drafts/{version}.md"
    destination = directory / relative
    # x mode: immutable draft path; never clobber prior data.
    with destination.open("xb") as file:
        file.write(data)
        file.flush()
        os.fsync(file.fileno())
    versions.append({
        "version": version,
        "parent_version": versions[-1]["version"] if len(versions) > 1 else None,
        "draft_path": relative,
        "draft_sha256": sha(data),
        "hypothesis": args.hypothesis,
        "submitted_at": utc_now(),
        "human_feedback": None,
    })
    atomic_json(directory / "manifest.json", manifest)
    print(f"SUBMITTED {version} {destination} sha256={sha(data)} STATUS=UNRATED")


def record_feedback(args: argparse.Namespace) -> None:
    directory, manifest = load(args.root, args.case)
    verify_records(directory, manifest)
    item = next((i for i in manifest["versions"] if i["version"] == args.version), None)
    if item is None:
        raise ValueError("unknown version")
    if item["human_feedback"] is not None:
        raise ValueError("feedback already recorded; never silently overwrite human judgment")
    data = read_nonempty(args.file)
    relative = f"feedback/{args.version}.md"
    with (directory / relative).open("xb") as fp:
        fp.write(data)
        fp.flush()
        os.fsync(fp.fileno())
    item["human_feedback"] = {
        "verdict": args.verdict,
        "path": relative,
        "sha256": sha(data),
        "recorded_at": utc_now(),
        "source": "user-supplied-feedback-file",
    }
    atomic_json(directory / "manifest.json", manifest)
    print(f"FEEDBACK {args.version} verdict={args.verdict}; never promoted to Canon")


def verify_records(directory: Path, manifest: dict) -> None:
    check_file(directory / "PROMPT_LOCK.md", manifest["prompt_sha256"], "scene lock")
    previous = None
    for index, record in enumerate(manifest["versions"], start=1):
        vid = f"V{index:03d}"
        if record["version"] != vid or record["parent_version"] != previous:
            raise ValueError(f"broken version chain at {vid}")
        check_file(directory / record["draft_path"], record["draft_sha256"], vid)
        feedback = record.get("human_feedback")
        if feedback is not None:
            check_file(directory / feedback["path"], feedback["sha256"], f"{vid} feedback")
        previous = vid


def verify(args: argparse.Namespace) -> None:
    directory, manifest = load(args.root, args.case)
    verify_records(directory, manifest)
    print(f"VERIFIED {args.case} versions={len(manifest['versions'])} (integrity only, NOT literary approval)")


def status(args: argparse.Namespace) -> None:
    directory, manifest = load(args.root, args.case)
    verify_records(directory, manifest)
    print(f"CASE {args.case} prompt={manifest['prompt_sha256']} versions={len(manifest['versions'])}")
    for record in manifest["versions"]:
        feedback = record["human_feedback"]
        verdict = feedback["verdict"] if feedback else "UNRATED"
        print(f"  {record['version']} <- {record['parent_version'] or 'START'} | {verdict} | {record['hypothesis']}")


def compare(args: argparse.Namespace) -> None:
    directory, manifest = load(args.root, args.case)
    verify_records(directory, manifest)
    by_id = {record["version"]: record for record in manifest["versions"]}
    if args.before not in by_id or args.after not in by_id:
        raise ValueError("both versions must exist")
    before = by_id[args.before]
    after = by_id[args.after]
    old = (directory / before["draft_path"]).read_text(encoding="utf-8").splitlines(keepends=True)
    new = (directory / after["draft_path"]).read_text(encoding="utf-8").splitlines(keepends=True)
    print("".join(difflib.unified_diff(old, new, fromfile=args.before, tofile=args.after)), end="")
    print("\n(Exact text difference; no automated literary judgment.)")


def main() -> None:
    parser = argparse.ArgumentParser(description="V13 immutable same-scene draft and feedback ledger")
    commands = parser.add_subparsers(dest="command", required=True)
    def common(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument("--root", type=Path, default=Path("training/scene_lab"))
        cmd.add_argument("--case", required=True)
    p = commands.add_parser("init")
    common(p)
    p.add_argument("--prompt", type=Path, required=True, help="approved fixed scene prompt")
    p.set_defaults(func=init)
    p = commands.add_parser("submit")
    common(p)
    p.add_argument("--draft", type=Path, required=True)
    p.add_argument("--hypothesis", required=True, help="specific narrative change attempted")
    p.set_defaults(func=submit)
    p = commands.add_parser("feedback")
    common(p)
    p.add_argument("--version", required=True)
    p.add_argument("--file", type=Path, required=True)
    p.add_argument("--verdict", required=True, choices=["better", "worse", "mixed", "unrated"])
    p.set_defaults(func=record_feedback)
    for name, fn in [("verify", verify), ("status", status)]:
        p = commands.add_parser(name)
        common(p)
        p.set_defaults(func=fn)
    p = commands.add_parser("compare")
    common(p)
    p.add_argument("--before", required=True)
    p.add_argument("--after", required=True)
    p.set_defaults(func=compare)
    args = parser.parse_args()
    try:
        args.func(args)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(2, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
