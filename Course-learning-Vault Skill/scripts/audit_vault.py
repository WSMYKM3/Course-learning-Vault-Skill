#!/usr/bin/env python3
"""Read-only structural audit for an Obsidian course-learning vault."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
FILELIKE_SUFFIXES = {".txt", ".md", ".pdf", ".ipynb", ".srt", ".vtt"}
LESSON_TYPES = {"lesson", "lesson-note"}
ATOMIC_TYPES = {
    "concept",
    "term",
    "formula",
    "method",
    "theorem",
    "proof",
    "code-reference",
    "classic-example",
}


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    file: str
    line: int
    message: str


@dataclass
class Note:
    path: Path
    relative: str
    text: str
    metadata: dict[str, object]
    body_start_line: int
    title: str
    note_type: str
    aliases: list[str]
    outgoing: list[tuple[str, int]]


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value.strip()


def parse_frontmatter(text: str) -> tuple[dict[str, object], int, bool]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 1, False

    metadata: dict[str, object] = {}
    current_list: str | None = None
    for index, raw in enumerate(lines[1:], start=2):
        if raw.strip() == "---":
            return metadata, index + 1, True
        list_match = re.match(r"^\s+-\s+(.+?)\s*$", raw)
        if list_match and current_list:
            value = clean_scalar(list_match.group(1))
            existing = metadata.setdefault(current_list, [])
            if isinstance(existing, list):
                existing.append(value)
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
        if not key_match:
            current_list = None
            continue
        key, raw_value = key_match.groups()
        if raw_value:
            if raw_value.startswith("[") and raw_value.endswith("]"):
                values = [clean_scalar(item) for item in raw_value[1:-1].split(",")]
                metadata[key] = [item for item in values if item]
            else:
                metadata[key] = clean_scalar(raw_value)
            current_list = None
        else:
            metadata[key] = []
            current_list = key
    return metadata, 1, False


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_name(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).strip().replace("\\", "/")
    if normalized.lower().endswith(".md"):
        normalized = normalized[:-3]
    return re.sub(r"\s+", " ", normalized).casefold()


def link_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target[:-3] if target.lower().endswith(".md") else target


def note_line(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def mask_code(text: str) -> str:
    """Blank code spans while preserving offsets and newlines."""

    chars = list(text)

    def blank(match: re.Match[str]) -> None:
        for position in range(match.start(), match.end()):
            if chars[position] != "\n":
                chars[position] = " "

    for match in re.finditer(r"^\s*(```|~~~).*?^\s*\1\s*$", text, re.MULTILINE | re.DOTALL):
        blank(match)
    masked = "".join(chars)
    for match in re.finditer(r"(?<!`)`[^`\n]+`(?!`)", masked):
        blank(match)
    return "".join(chars)


def load_notes(vault: Path) -> tuple[list[Note], list[Issue]]:
    notes: list[Note] = []
    issues: list[Issue] = []
    for path in sorted(vault.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(vault).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            relative = path.relative_to(vault).as_posix()
            issues.append(Issue("error", "decode-error", relative, 1, "File is not valid UTF-8."))
            continue
        metadata, body_start, has_frontmatter = parse_frontmatter(text)
        relative = path.relative_to(vault).as_posix()
        if not has_frontmatter:
            issues.append(Issue("error", "missing-frontmatter", relative, 1, "Markdown note has no valid YAML frontmatter."))
        title_match = TITLE_RE.search(text)
        title = title_match.group(1).strip() if title_match else ""
        if not title:
            issues.append(Issue("warning", "missing-title", relative, body_start, "Note has no level-one title."))
        aliases = as_list(metadata.get("aliases"))
        note_type = str(metadata.get("type", "")).strip().casefold()
        link_text = mask_code(text)
        outgoing = [(link_target(match.group(1)), note_line(text, match.start())) for match in LINK_RE.finditer(link_text)]
        notes.append(Note(path, relative, text, metadata, body_start, title, note_type, aliases, outgoing))
    return notes, issues


def has_heading(note: Note, alternatives: Iterable[str]) -> bool:
    headings = [match.group(1).strip().casefold() for match in HEADING_RE.finditer(note.text)]
    wanted = tuple(value.casefold() for value in alternatives)
    return any(any(term in heading for term in wanted) for heading in headings)


def add_required_metadata_issues(note: Note, issues: list[Issue]) -> None:
    required: dict[str, tuple[str, ...]] = {
        "course-map": ("course_id", "course", "output_language", "lesson_dir", "concept_dir", "formula_dir"),
        "lesson": ("course", "chapter", "topic", "source"),
        "lesson-note": ("course", "chapter", "topic", "source"),
        "concept": ("course",),
        "term": ("course",),
        "formula": ("course",),
        "method": ("course",),
        "checkpoint-review": ("course", "scope"),
        "quiz": ("course", "scope"),
    }
    if not note.note_type:
        issues.append(Issue("warning", "missing-type", note.relative, 2, "Frontmatter has no type."))
        return
    for key in required.get(note.note_type, ()):
        if not as_list(note.metadata.get(key)):
            issues.append(Issue("error", "missing-property", note.relative, 2, f"Type '{note.note_type}' requires frontmatter property '{key}'."))


def add_contract_issues(note: Note, issues: list[Issue]) -> None:
    if note.note_type in LESSON_TYPES:
        contracts = (
            (("学习目标", "learning objectives"), "lesson-objectives", "Lesson has no learning-objectives section."),
            (("知识节点", "graph view 节点", "knowledge nodes"), "lesson-nodes", "Lesson has no knowledge-node section."),
            (("复习检查", "self-check", "review questions"), "lesson-review", "Lesson has no self-check section."),
            (("一句话总结", "summary"), "lesson-summary", "Lesson has no summary section."),
        )
        for alternatives, code, message in contracts:
            if not has_heading(note, alternatives):
                issues.append(Issue("warning", code, note.relative, note.body_start_line, message))
    if note.note_type == "formula":
        if "$$" not in note.text:
            issues.append(Issue("error", "formula-math", note.relative, note.body_start_line, "Formula note has no display-math block."))
        if not re.search(r"(?:例子|示例|example|worked example)", note.text, re.IGNORECASE):
            issues.append(Issue("warning", "formula-example", note.relative, note.body_start_line, "Formula note has no worked example."))


def source_looks_filelike(source: str) -> bool:
    if re.match(r"^[a-z][a-z0-9+.-]*://", source, re.IGNORECASE):
        return False
    candidate = Path(source)
    return candidate.suffix.casefold() in FILELIKE_SUFFIXES or "/" in source or "\\" in source


def add_source_issues(note: Note, vault: Path, issues: list[Issue]) -> None:
    for source in as_list(note.metadata.get("source")):
        if not source_looks_filelike(source):
            continue
        source_path = Path(source).expanduser()
        if source_path.is_absolute() and source_path.exists():
            continue
        bases = [vault, vault.parent, vault.parent.parent]
        if not any((base / source_path).exists() for base in bases):
            issues.append(Issue("warning", "missing-source", note.relative, 2, f"Source path does not resolve near the vault: {source}"))


def add_math_issues(note: Note, issues: list[Issue]) -> None:
    math_text = mask_code(note.text)
    display_tokens = list(re.finditer(r"(?<!\\)\$\$", math_text))
    if len(display_tokens) % 2:
        line = note_line(math_text, display_tokens[-1].start()) if display_tokens else 1
        issues.append(Issue("error", "math-delimiter", note.relative, line, "Unbalanced display-math delimiter '$$'."))

    without_display = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", "", math_text, flags=re.DOTALL)
    inline_tokens = list(re.finditer(r"(?<![\\$])\$(?!\$)", without_display))
    if len(inline_tokens) % 2:
        issues.append(Issue("warning", "inline-math-delimiter", note.relative, 1, "Possibly unbalanced inline-math delimiter '$'."))

    math_spans = re.finditer(r"\$\$(.*?)\$\$|\$(.*?)\$", math_text, re.DOTALL)
    suspicious_re = re.compile(r"(?<!\\)(?:\b(?:frac|sqrt|partial|operatorname|mathrm)\s*\{|(?:left|right)\.)")
    for span in math_spans:
        content = span.group(1) if span.group(1) is not None else span.group(2)
        for match in suspicious_re.finditer(content or ""):
            absolute = span.start() + match.start()
            token = match.group(0)
            issues.append(Issue("warning", "latex-backslash", note.relative, note_line(note.text, absolute), f"Possible missing LaTeX backslash near '{token}'."))


def audit(vault: Path) -> dict[str, object]:
    notes, issues = load_notes(vault)
    basename_index: dict[str, list[Note]] = defaultdict(list)
    path_index: dict[str, Note] = {}
    alias_index: dict[str, list[Note]] = defaultdict(list)
    for note in notes:
        basename_index[normalize_name(note.path.stem)].append(note)
        path_index[normalize_name(str(Path(note.relative).with_suffix("")))] = note
        for alias in note.aliases:
            alias_index[normalize_name(alias)].append(note)

    for matches in basename_index.values():
        if len(matches) > 1:
            names = ", ".join(note.relative for note in matches)
            for note in matches:
                issues.append(Issue("error", "duplicate-basename", note.relative, 1, f"Duplicate note basename is ambiguous: {names}"))
    for alias, matches in alias_index.items():
        unique = {note.relative for note in matches}
        basename_matches = {note.relative for note in basename_index.get(alias, [])}
        conflicts = unique | basename_matches
        if len(conflicts) > 1:
            message = ", ".join(sorted(conflicts))
            for note in matches:
                issues.append(Issue("warning", "duplicate-alias", note.relative, 2, f"Alias resolves to multiple notes: {message}"))

    incoming: dict[str, int] = defaultdict(int)
    map_linked_lessons: set[str] = set()
    course_maps = [note for note in notes if note.note_type == "course-map"]

    def resolve(target: str) -> list[Note]:
        normalized = normalize_name(target)
        if normalized in path_index:
            return [path_index[normalized]]
        basename = normalize_name(Path(target).name)
        combined = basename_index.get(basename, []) + alias_index.get(basename, [])
        unique: dict[str, Note] = {note.relative: note for note in combined}
        return list(unique.values())

    for note in notes:
        add_required_metadata_issues(note, issues)
        add_contract_issues(note, issues)
        add_source_issues(note, vault, issues)
        add_math_issues(note, issues)
        for target, line in note.outgoing:
            if not target:
                continue
            matches = resolve(target)
            if not matches:
                issues.append(Issue("error", "unresolved-link", note.relative, line, f"WikiLink target does not resolve: {target}"))
            elif len(matches) > 1:
                names = ", ".join(sorted(match.relative for match in matches))
                issues.append(Issue("error", "ambiguous-link", note.relative, line, f"WikiLink target is ambiguous: {target} -> {names}"))
            else:
                incoming[matches[0].relative] += 1
                if note.note_type == "course-map" and matches[0].note_type in LESSON_TYPES:
                    map_linked_lessons.add(matches[0].relative)

    for note in notes:
        if note.note_type != "course-map" and incoming[note.relative] == 0 and not note.outgoing:
            issues.append(Issue("info", "orphan-note", note.relative, 1, "Note has no incoming or outgoing WikiLinks."))
        if course_maps and note.note_type in LESSON_TYPES and note.relative not in map_linked_lessons:
            issues.append(Issue("warning", "course-map-coverage", note.relative, 1, "Lesson is not linked from a course map."))

    severity_order = {"error": 0, "warning": 1, "info": 2}
    issues = sorted(set(issues), key=lambda item: (severity_order[item.severity], item.file.casefold(), item.line, item.code))
    counts = {level: sum(issue.severity == level for issue in issues) for level in ("error", "warning", "info")}
    return {
        "vault": str(vault),
        "notes": len(notes),
        "summary": counts,
        "issues": [asdict(issue) for issue in issues],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, help="Path to the Obsidian vault to inspect")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="Return non-zero for warnings as well as errors")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault = args.vault.expanduser().resolve()
    if not vault.is_dir():
        print(f"error: vault is not a directory: {vault}", file=sys.stderr)
        return 2

    report = audit(vault)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        summary = report["summary"]
        print(f"Vault: {report['vault']}")
        print(f"Notes: {report['notes']} | Errors: {summary['error']} | Warnings: {summary['warning']} | Info: {summary['info']}")
        for issue in report["issues"]:
            print(f"{issue['severity'].upper():7} {issue['code']:24} {issue['file']}:{issue['line']} — {issue['message']}")

    summary = report["summary"]
    if summary["error"] or (args.strict and summary["warning"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
