"""Merge per-article extractions into tables and per-component notes. No API calls.

Usage: python tools/merge_extractions.py [--src extractions]

Writes:
  data/findings.csv              one row per finding, with article date/title/url
  data/political_insights.csv    one row per political insight
  data/article_summaries.csv     one row per article: content level, models, summary, cost
  notes/components/<component>.md   all findings for that component, in date order
  notes/references.md            every methodology page / source the articles point to
  notes/open_questions.md        details alluded to but not explained
  notes/README.md                counts by component
"""
import argparse
import csv
import difflib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "silver_bulletin"


def norm(t: str) -> str:
    """Normalize quotes, dashes and whitespace so verbatim checks survive typography."""
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-"), (" ", " ")):
        t = t.replace(a, b)
    return " ".join(t.split()).lower()


def check_quote(quote: str, source: str, source_nofn: str) -> str:
    """ok = verbatim (allowing '...' elisions); close = near-verbatim; NOT FOUND otherwise."""
    q = norm(quote).replace("…", "...")
    parts = [p.strip("\"' .,;:-") for p in re.split(r"\.{3,}|\[\.\.\.\]", q)]
    parts = [p for p in parts if p]
    for src in (source, source_nofn):
        pos, ok = 0, True
        for p in parts:
            i = src.find(p, pos)
            if i < 0:
                ok = False
                break
            pos = i + len(p)
        if ok and parts:
            return "ok"
    # near-verbatim: e.g. a footnote digit glued to a number ("2023-20242")
    longest = max(parts, key=len) if parts else q
    sm = difflib.SequenceMatcher(None, source, longest, autojunk=False)
    m = sm.find_longest_match(0, len(source), 0, len(longest))
    start = max(0, m.a - m.b)
    window = source[start:start + len(longest) + 5]
    if difflib.SequenceMatcher(None, window, longest).ratio() >= 0.95:
        return "close"
    return "NOT FOUND"


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")   # older extractions may carry extra fields
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=ROOT / "extractions")
    ap.add_argument("--data", type=Path, default=ROOT / "data")
    ap.add_argument("--notes", type=Path, default=ROOT / "notes")
    args = ap.parse_args()

    recs = []
    for p in sorted(args.src.glob("*.json")):
        if p.name.endswith(".INVALID.json"):
            continue
        r = json.loads(p.read_text(encoding="utf-8"))
        if r.get("extraction"):
            recs.append(r)
    recs.sort(key=lambda r: (r["article"]["date"], r["article"]["title"]))
    invalid = len(list(args.src.glob("*.INVALID.json")))

    findings, insights, summaries, refs, questions = [], [], [], [], []
    for r in recs:
        a, x = r["article"], r["extraction"]
        base = {"date": a["date"], "title": a["title"], "url": a["url"]}
        txt = SRC / f"{a['stem']}.txt"
        if a["stem"].startswith("fte_"):      # archived FiveThirtyEight methodology pages
            txt = ROOT / "sources" / "fivethirtyeight" / f"{a['stem'][4:]}.txt"
        source_text = norm(txt.read_text(encoding="utf-8")) if txt.exists() else None
        # same text with footnote markers glued to words removed ("another1," -> "another,")
        source_nofn = re.sub(r"(?<=[a-z.,;:)'\"!?])\d{1,2}\b", "", source_text) if source_text else None
        summaries.append({**base, "relevance": a["relevance"], "model_content_level": x["model_content_level"],
                          "n_findings": len(x["findings"]), "n_insights": len(x["political_insights"]),
                          "models_discussed": "; ".join(x["models_discussed"]), "summary": x["summary"],
                          "model": r["run"]["model"], "cost_usd": r["run"]["cost_usd"]})
        for i, f in enumerate(x["findings"]):
            q = "; ".join(f"{q['name']} = {q['value']} {q['unit']}".strip() + (f" ({q['context']})" if q["context"] else "")
                          for q in f["quantities"])
            if not f["evidence_quote"] or source_text is None:
                qc = "n/a"
            else:
                qc = check_quote(f["evidence_quote"], source_text, source_nofn)
            findings.append({**base, "finding_id": f"{a['stem']}#{i}", **{k: v for k, v in f.items() if k != "quantities"},
                             "quantities": q, "quote_check": qc})
        for s in x["political_insights"]:
            insights.append({**base, **s})
        for ref in x["references"]:
            refs.append({**base, **ref})
        for oq in x["open_questions"]:
            questions.append({**base, "question": oq})

    if not recs:
        print("No valid extractions found.")
        return

    fcols = ["finding_id", "date", "title", "url", "component", "finding_type", "statement", "quantities",
             "rationale", "model_version", "evidence_quote", "explicitness", "quote_check"]
    write_csv(args.data / "findings.csv", findings, fcols)
    write_csv(args.data / "political_insights.csv", insights,
              ["date", "title", "url", "topic", "insight", "evidence", "forecasting_implication"])
    write_csv(args.data / "article_summaries.csv", summaries, list(summaries[0]))

    comp_dir = args.notes / "components"
    comp_dir.mkdir(parents=True, exist_ok=True)
    by_comp = defaultdict(list)
    for f in findings:
        by_comp[f["component"]].append(f)
    for comp, fs in by_comp.items():
        lines = [f"# {comp.replace('_', ' ').capitalize()}", "",
                 f"{len(fs)} findings from {len({f['url'] for f in fs})} articles, oldest first.", ""]
        for f in fs:
            lines.append(f"### {f['date']} · [{f['title']}]({f['url']})")
            lines.append(f"**{f['finding_type'].replace('_', ' ')}** · {f['model_version']} · "
                         f"{f['explicitness']}")
            lines.append("")
            lines.append(f["statement"])
            if f["quantities"]:
                lines.append(f"\n*Numbers:* {f['quantities']}")
            if f["rationale"]:
                lines.append(f"\n*Why:* {f['rationale']}")
            if f["evidence_quote"]:
                flag = "  *(quote not found in article text, check it)*" if f["quote_check"] == "NOT FOUND" else ""
                lines.append(f"\n> {f['evidence_quote']}{flag}")
            lines.append(f"\n<sub>{f['finding_id']}</sub>\n")
        (comp_dir / f"{comp}.md").write_text("\n".join(lines), encoding="utf-8")

    ref_lines = ["# References to methodology and sources", ""]
    for r in refs:
        link = f" <{r['url']}>" if r["url"] else ""
        ref_lines.append(f"- {r['description']}{link}. Cited in \"{r['title']}\" ({r['date']})")
    (args.notes / "references.md").write_text("\n".join(ref_lines) + "\n", encoding="utf-8")

    q_lines = ["# Open questions", "", "Model details the articles allude to but do not explain.", ""]
    for q in questions:
        q_lines.append(f"- {q['question']} ({q['date']}, [{q['title']}]({q['url']}))")
    (args.notes / "open_questions.md").write_text("\n".join(q_lines) + "\n", encoding="utf-8")

    cc = Counter(f["component"] for f in findings)
    bad = sum(f["quote_check"] == "NOT FOUND" for f in findings)
    lc = Counter(s["model_content_level"] for s in summaries)
    readme = ["# Extraction overview", "",
              f"{len(recs)} articles extracted ({invalid} invalid, not included). "
              f"{len(findings)} findings, {len(insights)} political insights. "
              f"{bad} quotes could not be matched to the article text.", "",
              "| Model content | Articles |", "|---|---|"] + \
             [f"| {k} | {lc[k]} |" for k in ("high", "medium", "low", "none")] + \
             ["", "| Component | Findings |", "|---|---|"] + \
             [f"| [{c}](components/{c}.md) | {n} |" for c, n in cc.most_common()]
    (args.notes / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print(f"{len(recs)} articles, {len(findings)} findings, {len(insights)} insights, "
          f"{len(by_comp)} components -> {args.data}, {args.notes}")


if __name__ == "__main__":
    main()
