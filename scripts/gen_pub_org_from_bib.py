#!/usr/bin/env python3
"""Generate Wowchemy-style publication Org subtrees from HaoYan.bib (Yan as author)."""
from __future__ import annotations

import re
from pathlib import Path
from collections import defaultdict


def strip_tex(s: str) -> str:
    s = re.sub(r"\\\w+", "", s)
    s = s.replace("\\&", "&")
    return re.sub(r"\s+", " ", s).strip()


def _brace_value(body: str, start: int) -> tuple[str, int]:
    """Return content of {...} starting at body[start] == '{'."""
    assert body[start] == "{"
    i = start + 1
    depth = 1
    while i < len(body) and depth:
        if body[i] == "{":
            depth += 1
        elif body[i] == "}":
            depth -= 1
        i += 1
    return body[start + 1 : i - 1], i


def _field(body: str, name: str) -> str:
    m = re.search(r"\b" + name + r"\s*=", body, re.I)
    if not m:
        return ""
    j = m.end()
    while j < len(body) and body[j] in " \t\n":
        j += 1
    if j >= len(body):
        return ""
    if body[j] == '"':
        end = body.find('"', j + 1)
        return strip_tex(body[j + 1 : end]) if end != -1 else ""
    if body[j] == "{":
        inner, _ = _brace_value(body, j)
        # unwrap {{ }}
        if inner.startswith("{") and inner.endswith("}"):
            inner = inner[1:-1]
        return strip_tex(inner.replace("\n", " "))
    return ""


def parse_bib(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    # Keep leading '@' on each entry (split removes it otherwise).
    chunks = re.split(r"\n(?=@)", text)
    out = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk.startswith("@"):
            continue
        m = re.match(r"@(\w+)\{([^,]+),", chunk)
        if not m:
            continue
        typ, key = m.group(1).lower(), m.group(2).strip()
        body = chunk[m.end() :]

        def gf(nm: str) -> str:
            return _field(body, nm) or _field(body, nm.upper())

        title = gf("title")
        author = gf("author")
        year_s = gf("year") or gf("YEAR") or ""
        ym = re.search(r"\d{4}", year_s) or re.search(r"\d{4}", key)
        year = int(ym.group(0)) if ym else 0

        au_norm = author.lower().replace("yan1", "yan")
        if not re.search(r"\byan\b", au_norm):
            continue

        out.append(
            {
                "key": key,
                "type": typ,
                "title": title,
                "author": author,
                "year": year,
                "journal": gf("journal"),
                "booktitle": gf("booktitle") or gf("BOOKTITLE"),
                "volume": gf("volume"),
                "number": gf("number"),
                "pages": gf("pages"),
                "doi": gf("doi"),
                "url": gf("url") or gf("URL"),
                "note": gf("note"),
                "school": gf("school"),
                "publisher": gf("publisher"),
            }
        )
    return out


# Canonical EXPORT slug per bib key (matches existing Hugo / prior Org exports).
SLUG = {
    "xu2026pathcoupled": "xu-path-coupled-icml-2026",
    "chen2026dconvexity": "chen-dconvexity-cvpr-2026",
    "rathnakumar2026bayesian": "rathnakumar-benn-ress-2026",
    "huang2025multi": "huang-multimodal-case-2025",
    "hu2025personalized": "hu-personalized-tucker-2025",
    "dhulipala2025moose": "dhulipala-moose-jocs-2025",
    "zhao2025hierarchical": "zhao-hierarchical-ijds-2025",
    "shi2025diffusion": "shi-diffusion-surrogate-tase-2025",
    "moradi2025single": "moradi-single-image-zeroshot-arxiv-2025",
    "zou2025probabilistic": "zou-probabilistic-kan-case-2025",
    "chen2025bayesian": "chen-bayesian-reactor-ans-2025",
    "xu2025partially": "xu-pomdp-degradation-jqt-2025",
    "sergin2025low": "sergin-low-rank-tensor-ijds-2025",
    "lee2025oral": "lee-oral-anatomical-cbct-tase-2025",
    "zhang2024power": "zhang-power-rser-2024",
    "sergin2024image": "sergin-image-iise-2024",
    "guo2024thompson": "guo-thompson-ijds-2024",
    "huang2024uncertainty": "huang-uncertainty-bayesian-unet-joen-2024",
    "chen2024leveraging": "chen-leveraging-transformers-cbct-joen-2024",
    "yan2024sparse": "yan-sparse-decomposition-springer-chapter-2024",
    "huang2023posterior": "huang-posterior-2023",
    "biehler2023antler": "biehler-antler-tase-2023",
    "li2023graph": "li-graph-tensor-iise-2023",
    "li2023tensor": "li-tensor-dpmm-sigspatial-2023",
    "hu2023adaptive": "hu-adaptive-2022",
    "guo2023bayesian": "guo-bayesian-2023",
    "wang2022attention": "wang-attentionbased-2022",
    "li2022individualized": "li-individualized-dmkd-2022",
    "zhao2022event": "zhao-event-extraction-aiaa-2022",
    "pang2022bayesian": "pang-bayesian-2022",
    "li2022profile": "li-profile-2022",
    "li2022multi": "li-multi-task-latent-tase-2022",
    "du2022tensor": "du-tensor-voting-jmse-2022",
    "zhao2022deep": "zhao-deep-2022",
    "zhao2022adaptive": "zhao-adaptive-2022",
    "zhao2022rapid": "zhao-rapid-2021",
    "wu2022adaptive": "wu-adaptive-2021",
    "lahoti2022convolutional": "lahoti-cnn-adaptive-sampling-is-2022",
    "yan2022real": "yan-realtime-2021",
    "zhang2021dynamic": "zhang-dynamic-2020",
    "lahoti2021image": "lahoti-image-2021",
    "pang2021data": "pang-data-2021",
    "huang2021combining": "huang-combining-2021",
    "zhao2021hierarchical": "zhao-hierarchical-2021",
    "yan2021deep": "haoyan-deep-2021",
    "sergin2021toward": "sergin-2021-toward",
    "fang2021multi": "fang-multi-sensor-2020",
    "gahrooei2021multiple": "gahrooei-multiple-2020",
    "setzer2020artificial": "setzer-artificial-2020",
    "reisi2020comments": "reisigahrooei-comments-2020",
    "li2020tensor": "li-tensor-2020",
    "yan2020akm2d": "yan-akm-2-d-2020",
    "kang2019performance": "kang-performance-2020",
    "huang2020edge": "huang-edge-2021",
    "zhao2020simultaneous": "zhao-simultaneous-2021",
    "gu2020multiport": "gu-multiport-electrification-2020",
    "guo2020partially": "guo-partially-observable-arxiv-2020",
    "yan2019structured": "yan-structured-2019",
    "yan2019image": "yan-imagebased-2019",
    "yan2019physics": "yan-physicsbased-2019",
    "zhao2019spatio": "zhao-spatiotemporal-2019",
    "zhao2019rapid": "zhao-rapid-2019",
    "zhao2019semi": "zhao-semi-supervised-hmm-phm-2019",
    "kang2018real": "kang-realtime-2018",
    "zhang2018weakly": "zhang-weakly-2018",
    "zhang2018multiple": "zhang-multiple-2018",
    "yan2018real": "yan-real-time-2018",
    "yue2017wavelet": "yue-wavelet-based-2018",
    "pacella2017point": "pacella-point-cloud-informs-2017",
    "yan2017anomaly": "yan-anomaly-2017",
    "yan2017high": "yan-high-2017",
    "yue2017generalized": "yue-generalized-2017",
    "mesnil2016fast": "mesnil-fast-2016",
    "yan2016multiple": "yan-multiple-2016",
    "mesnil2015guided": "mesnil-guided-wavefield-2015",
    "yan2014image": "yan-imagebased-2015",
    "mesnil2014frequency": "mesnil-frequency-2014",
    "li2013globally": "li-globally-attractive-cycle-arxiv-2013",
    "li2020long": "li-long-short-spatiotemporal-ral-2020",
    "zheng2020anatomically": "zheng-anatomicallyconstrained-2020",
}


def pub_type(entry: dict) -> str:
    t = entry["type"]
    if t == "inproceedings":
        return "paper-conference"
    if t == "phdthesis":
        return "thesis"
    if t == "incollection":
        return "chapter"
    if t == "article":
        j = entry["journal"].lower()
        if "arxiv" in j or "preprint" in j:
            return "article"
        return "article-journal"
    return "article-journal"


def venue_markdown(entry: dict) -> str:
    if entry["booktitle"]:
        return f"*{_escape_yaml_string(entry['booktitle'])}*"
    if entry["journal"]:
        return f"*{_escape_yaml_string(entry['journal'])}*"
    if entry["school"]:
        return f"*{_escape_yaml_string(entry['school'])}*"
    return "*"


def _escape_yaml_string(s: str) -> str:
    return s.replace("'", "''")


def format_authors(author_field: str) -> list[str]:
    """Very rough 'Last, First' -> 'First Last' for common cases."""
    parts = author_field.split(" and ")
    names = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if "," in p:
            last, first = p.split(",", 1)
            names.append(f"{first.strip()} {last.strip()}")
        else:
            names.append(p)
    return names


def yaml_block(entry: dict) -> str:
    lines = []
    authors = format_authors(entry["author"])
    lines.append("authors:")
    for a in authors:
        lines.append(f"- {a}")
    lines.append("publication_types:")
    lines.append(f"- {pub_type(entry)}")
    ven = venue_markdown(entry)
    if ven != "*":
        lines.append(f"publication: '{ven}'")
    lines.append(f"year: '{entry['year']}'")
    if entry["volume"]:
        lines.append(f"volume: '{entry['volume']}'")
    if entry["number"]:
        lines.append(f"number: '{entry['number']}'")
    if entry["pages"]:
        lines.append(f"pages: '{entry['pages']}'")
    if entry["doi"]:
        lines.append(f"doi: '{entry['doi']}'")
    if entry["url"]:
        lines.append(f"url_pdf: '{entry['url']}'")
    abst = entry["title"][:400]
    if entry["note"]:
        note = entry["note"].replace(r"\%", "%").replace("\\", " ")
        abst = f"{note}. {abst}"
    lines.append(f"abstract: '{_escape_yaml_string(abst[:800])}'")
    return "\n".join(lines)


def org_tags(title: str) -> str:
    """Derive a few Org tags from title words (capitalized token)."""
    stop = {
        "a",
        "an",
        "the",
        "for",
        "and",
        "of",
        "in",
        "on",
        "via",
        "with",
        "to",
        "using",
        "based",
    }
    words = re.findall(r"[A-Za-z][a-z]+", title)[:4]
    tags = [w for w in words if w.lower() not in stop][:3]
    return ":" + ":".join(tags) + ":" if tags else ":Publication:"


def org_entry(entry: dict, slug: str) -> str:
    title_clean = strip_tex(entry["title"])
    headline = title_clean.replace(":", "—")  # avoid Org headline breaks
    tags = org_tags(title_clean)
    yblock = yaml_block(entry)
    return f"""*** {headline} {tags}
:PROPERTIES:
:EXPORT_HUGO_SECTION: publication/{slug}
:EXPORT_FILE_NAME: index
:END:
#+begin_src yaml :front_matter_extra t
{yblock}
#+end_src

"""


def main():
    bib = Path("/Users/haoyan/ASU Dropbox/Hao Yan/CVs/HaoYan.bib")
    entries = parse_bib(bib)
    slug_map = dict(SLUG)
    for e in entries:
        slug_map.setdefault(
            e["key"], re.sub(r"[^a-z0-9]+", "-", e["key"].lower()).strip("-")
        )

    by_year = defaultdict(list)
    for e in entries:
        by_year[e["year"]].append(e)

    lines = []
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"** {year}\n")
        for e in sorted(by_year[year], key=lambda x: strip_tex(x["title"]).lower()):
            lines.append(org_entry(e, slug_map[e["key"]]))

    out = Path("/Users/haoyan/Dropbox/academic-website/scripts/pub_section_generated.org")
    out.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} publications)")


if __name__ == "__main__":
    main()
