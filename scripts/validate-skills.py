#!/usr/bin/env python3
"""Validate LibreChat skill repo structure without third-party dependencies."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "skills-manifest.yaml"
MAX_FILE_BYTES = 1_000_000
MAX_SKILL_BYTES = 5_000_000
SAFE_PART_RE = re.compile(r"^[A-Za-z0-9._-]+$")
SOURCE_RE = re.compile(r"^  ([A-Za-z0-9_-]+):$")
SOURCE_PATH_RE = re.compile(r"^    path: (.+)$")
SKILL_ID_RE = re.compile(r"^      - id: (.+)$")
SKILL_PATH_RE = re.compile(r"^        path: (.+)$")
REFERENCE_RE = re.compile(r"references/[A-Za-z0-9._/-]+")
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
]


@dataclass(frozen=True)
class SkillEntry:
    source_id: str
    source_path: Path
    skill_id: str
    skill_path: Path


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_manifest(errors: list[str]) -> list[SkillEntry]:
    # Repo-owned YAML subset avoids a PyYAML dependency in bootstrap CI.
    if not MANIFEST.exists():
        fail(errors, "skills-manifest.yaml missing")
        return []

    entries: list[SkillEntry] = []
    source_id: str | None = None
    source_path: Path | None = None
    pending_skill_id: str | None = None

    for lineno, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), start=1):
        if match := SOURCE_RE.match(line):
            source_id = match.group(1)
            source_path = None
            pending_skill_id = None
            continue
        if source_id and (match := SOURCE_PATH_RE.match(line)):
            raw_path = match.group(1).strip()
            source_path = Path(raw_path)
            validate_relative_path(raw_path, errors, f"manifest line {lineno}")
            continue
        if source_id and (match := SKILL_ID_RE.match(line)):
            pending_skill_id = match.group(1).strip()
            if not SAFE_PART_RE.match(pending_skill_id):
                fail(errors, f"manifest line {lineno}: unsafe skill id {pending_skill_id!r}")
            continue
        if source_id and pending_skill_id and (match := SKILL_PATH_RE.match(line)):
            raw_path = match.group(1).strip()
            validate_relative_path(raw_path, errors, f"manifest line {lineno}")
            if source_path is None:
                fail(errors, f"manifest line {lineno}: skill before source path")
            else:
                entries.append(
                    SkillEntry(
                        source_id=source_id,
                        source_path=source_path,
                        skill_id=pending_skill_id,
                        skill_path=Path(raw_path),
                    )
                )
            pending_skill_id = None

    if not entries:
        fail(errors, "manifest has no skills")
    return entries


def validate_relative_path(raw_path: str, errors: list[str], label: str) -> None:
    path = Path(raw_path)
    if path.is_absolute():
        fail(errors, f"{label}: absolute path not allowed: {raw_path}")
    if ".." in path.parts:
        fail(errors, f"{label}: parent path not allowed: {raw_path}")
    for part in path.parts:
        if not SAFE_PART_RE.match(part):
            fail(errors, f"{label}: unsafe path part {part!r} in {raw_path}")


def read_frontmatter(skill_file: Path, errors: list[str]) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        fail(errors, f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
        return {}

    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(errors, f"{skill_file.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_skill(entry: SkillEntry, seen_names: dict[str, set[str]], errors: list[str]) -> None:
    skill_dir = ROOT / entry.source_path / entry.skill_path
    skill_file = skill_dir / "SKILL.md"

    if not skill_dir.is_dir():
        fail(errors, f"{entry.skill_id}: missing skill directory {skill_dir.relative_to(ROOT)}")
        return
    if not skill_file.is_file():
        fail(errors, f"{entry.skill_id}: missing SKILL.md")
        return

    frontmatter = read_frontmatter(skill_file, errors)
    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name:
        fail(errors, f"{skill_file.relative_to(ROOT)}: missing frontmatter name")
    if not description:
        fail(errors, f"{skill_file.relative_to(ROOT)}: missing frontmatter description")
    if name:
        source_names = seen_names.setdefault(entry.source_id, set())
        if name in source_names:
            fail(errors, f"{skill_file.relative_to(ROOT)}: duplicate skill name {name!r}")
        source_names.add(name)

    skill_bytes = 0
    nested_skill_files = [path for path in skill_dir.glob("**/SKILL.md") if path != skill_file]
    for nested in nested_skill_files:
        fail(errors, f"{nested.relative_to(ROOT)}: nested skill directories are not supported")

    for path in skill_dir.glob("**/*"):
        if path.is_dir():
            continue
        rel = path.relative_to(ROOT)
        validate_relative_path(str(rel), errors, str(rel))
        size = path.stat().st_size
        skill_bytes += size
        if size > MAX_FILE_BYTES:
            fail(errors, f"{rel}: file exceeds {MAX_FILE_BYTES} bytes")
        scan_for_secrets(path, errors)

    if skill_bytes > MAX_SKILL_BYTES:
        fail(errors, f"{skill_dir.relative_to(ROOT)}: skill exceeds {MAX_SKILL_BYTES} bytes")

    validate_references(skill_file, skill_dir, errors)


def validate_references(skill_file: Path, skill_dir: Path, errors: list[str]) -> None:
    text = skill_file.read_text(encoding="utf-8")
    for match in REFERENCE_RE.finditer(text):
        ref = match.group(0).rstrip(").,;:")
        if "*" in ref:
            continue
        target = skill_dir / ref
        if not target.is_file():
            fail(errors, f"{skill_file.relative_to(ROOT)}: missing referenced file {ref}")


def scan_for_secrets(path: Path, errors: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(errors, f"{path.relative_to(ROOT)}: possible secret matched {pattern.pattern}")


def validate_manifest_coverage(entries: list[SkillEntry], errors: list[str]) -> None:
    by_source: dict[Path, set[str]] = {}
    manifest_by_source: dict[Path, set[str]] = {}
    for source_path in sorted({entry.source_path for entry in entries}):
        source_dir = ROOT / source_path
        if not source_dir.is_dir():
            fail(errors, f"manifest source path missing: {source_path}")
            continue
        by_source[source_path] = {path.name for path in source_dir.iterdir() if path.is_dir()}
        manifest_by_source[source_path] = {
            entry.skill_path.as_posix() for entry in entries if entry.source_path == source_path
        }

    for source_path, actual in by_source.items():
        declared = manifest_by_source[source_path]
        missing = actual - declared
        extra = declared - actual
        if missing:
            fail(errors, f"{source_path}: skill dirs missing from manifest: {sorted(missing)}")
        if extra:
            fail(errors, f"{source_path}: manifest entries missing dirs: {sorted(extra)}")


def validate_global_paths(errors: list[str]) -> None:
    for path in ROOT.glob("**/*"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        validate_relative_path(str(rel), errors, str(rel))


def main() -> int:
    errors: list[str] = []
    entries = parse_manifest(errors)
    validate_global_paths(errors)
    validate_manifest_coverage(entries, errors)

    seen_names: dict[str, set[str]] = {}
    seen_keys: set[tuple[str, str]] = set()
    for entry in entries:
        key = (entry.source_id, entry.skill_id)
        if key in seen_keys:
            fail(errors, f"duplicate manifest entry: {entry.source_id}/{entry.skill_id}")
        seen_keys.add(key)
        if entry.skill_id != entry.skill_path.name:
            fail(errors, f"{entry.source_id}/{entry.skill_id}: id must match path {entry.skill_path}")
        validate_skill(entry, seen_names, errors)

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(entries)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
