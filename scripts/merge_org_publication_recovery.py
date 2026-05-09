#!/usr/bin/env python3
"""Replace publication/*** subtrees in website.org using recovered Org fragments (matched by EXPORT slug)."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def normalize_block(block: str) -> str:
    block = block.replace("pulication:", "publication:")
    lines = block.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "publication_types:" and i + 1 < len(lines):
            nxt = lines[i + 1].strip()
            if nxt in ("- '1'", '- "1"'):
                out.append(line)
                out.append("- paper-conference")
                i += 2
                continue
            if nxt in ("- '2'", '- "2"'):
                out.append(line)
                out.append("- article-journal")
                i += 2
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


def parse_recovery(recovery: str) -> dict[str, str]:
    recovery = recovery.strip()
    blocks: dict[str, str] = {}
    parts = re.split(r"(?m)^(?=\*\*\* )", recovery)
    for p in parts:
        p = p.strip()
        if not p.startswith("***"):
            continue
        m = re.search(r":EXPORT_HUGO_SECTION: publication/(\S+)", p)
        if not m:
            continue
        slug = m.group(1).strip()
        blocks[slug] = normalize_block(p).rstrip() + "\n"
    return blocks


def extract_org_block(org_text: str, slug: str) -> tuple[int, int] | None:
    """Slice [slice_from:end) is one *** subtree whose PROPERTIES mention this slug."""
    needle_line = f":EXPORT_HUGO_SECTION: publication/{slug}"
    search_pos = 0
    while True:
        export_idx = org_text.find(needle_line, search_pos)
        if export_idx == -1:
            return None
        cur = export_idx
        slice_from = -1
        while cur > 0:
            prev_star = org_text.rfind("\n*** ", 0, cur)
            if prev_star < 0:
                break
            slice_from = prev_star + 1
            next_star = org_text.find("\n*** ", slice_from + 4)
            chunk = (
                org_text[slice_from:]
                if next_star < 0
                else org_text[slice_from:next_star]
            )
            m = re.search(r":EXPORT_HUGO_SECTION: publication/(\S+)", chunk)
            if m and m.group(1).strip() == slug:
                break
            cur = prev_star
            slice_from = -1
        if slice_from < 0:
            search_pos = export_idx + 1
            continue
        end_i = org_text.find("#+end_src", slice_from)
        if end_i < 0:
            return None
        end = end_i + len("#+end_src")
        if end < len(org_text) and org_text[end] == "\n":
            end += 1
        return slice_from, end


def merge(org_text: str, recovery_blocks: dict[str, str]) -> str:
    spans: list[tuple[int, int, str]] = []
    missing: list[str] = []
    for slug, block in recovery_blocks.items():
        span = extract_org_block(org_text, slug)
        if span is None:
            missing.append(slug)
            continue
        spans.append((span[0], span[1], block))
    spans.sort(key=lambda x: x[0], reverse=True)
    for s, e, block in spans:
        org_text = org_text[:s] + block + org_text[e:]
    for m in missing:
        print("warning: slug not found in org:", m, file=sys.stderr)
    return org_text


def main() -> None:
    recovery_path = Path(sys.argv[1])
    org_path = Path(sys.argv[2])
    recovery_blocks = parse_recovery(recovery_path.read_text(encoding="utf-8"))
    org_text = org_path.read_text(encoding="utf-8")
    merged = merge(org_text, recovery_blocks)
    org_path.write_text(merged, encoding="utf-8")
    print(f"Merged {len(recovery_blocks)} recovery blocks into {org_path}")


if __name__ == "__main__":
    main()
