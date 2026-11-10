"""Validate hand-made extractions (done in Claude Code, no API) and wrap them in the standard record.

Each file extractions/_manual/<stem>.json holds only the "extraction" object. Stems that start
with "fte_" are archived FiveThirtyEight methodology pages in sources/fivethirtyeight/.

Usage: python tools/wrap_manual.py            # wrap every valid manual file not yet wrapped
       python tools/wrap_manual.py --force    # rewrap all
"""
import csv
import datetime as dt
import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "extractions" / "_manual"
OUT = ROOT / "extractions"
SCHEMA = json.loads((ROOT / "prompts" / "extraction_schema.json").read_text(encoding="utf-8"))
MODEL = "claude-opus-5-5 (manual, Claude Code session)"
# Articles whose PDF holds substantially more than the text file; their PDF text was read too.
PDF_READ = {"2026-01-14_silver-bulletin-pollster-ratings-2025-archive",
            "2026-06-29_is-the-vibecession-real-or-is-the-survey-broken",
            "2026-08-13_prediction-markets-arent-magic-by-nate-silver",
            "2026-11-03_generic-congressional-ballot-latest-polls-silver-bulletin",
            "2026-11-03_2026-midterm-election-governors-forecast-silver-bulletin",
            "2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin",
            "2026-11-03_2026-midterm-election-forecast-senate-house-silver-bulletin",
            "2026-11-03_2026-midterm-election-house-forecast-silver-bulletin",
            "2026-11-04_trump-approval-rating-latest-polls-silver-bulletin"}


def article_meta(stem):
    if stem.startswith("fte_"):
        txt = (ROOT / "sources" / "fivethirtyeight" / f"{stem[4:]}.txt").read_text(encoding="utf-8")
        head = dict(line.split(": ", 1) for line in txt.splitlines()[:6] if ": " in line)
        return {"date": head.get("Date", ""), "title": head.get("Title", ""), "subtitle": "",
                "authors": head.get("Authors", ""), "url": head.get("URL", ""), "paywalled": "False",
                "relevance": "fte_methodology", "stem": stem}
    files = {r["file"]: r["url"] for r in csv.DictReader((ROOT / "sources" / "silver_bulletin" / "index.csv").open(encoding="utf-8"))}
    meta = {r["url"]: r for r in csv.DictReader((ROOT / "data" / "articles.csv").open(encoding="utf-8"))}
    m = meta[files[stem]]
    return {k: m[k] for k in ("date", "title", "subtitle", "authors", "url", "paywalled", "relevance")} | {"stem": stem}


def main():
    force = "--force" in sys.argv
    v = jsonschema.Draft202012Validator(SCHEMA)
    ok = bad = skipped = 0
    for p in sorted(MAN.glob("*.json")):
        stem = p.stem
        target = OUT / f"{stem}.json"
        if target.exists() and not force:
            skipped += 1
            continue
        x = json.loads(p.read_text(encoding="utf-8"))
        errs = [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message[:150]}" for e in v.iter_errors(x)]
        if errs:
            bad += 1
            print(f"INVALID {stem}:\n  " + "\n  ".join(errs[:8]))
            continue
        rec = {"article": article_meta(stem),
               "run": {"model": MODEL, "pdf_included": stem in PDF_READ, "cost_usd": 0.0,
                       "prompt_tokens": 0, "completion_tokens": 0, "finish_reason": "manual",
                       "valid": True, "validation_errors": [],
                       "timestamp": dt.datetime.now().isoformat(timespec="seconds")},
               "extraction": x}
        target.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        ok += 1
        print(f"ok      {stem}: {len(x['findings'])} findings, {len(x['political_insights'])} insights")
    print(f"wrapped {ok}, invalid {bad}, already wrapped {skipped}")


if __name__ == "__main__":
    main()
