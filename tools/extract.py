"""Extract structured model knowledge from each saved Silver Bulletin article via MIT Parley.

Setup: put your key in a file named .env in the project root:
    PARLEY_API_KEY=sk-parley-v1-...
(or set the PARLEY_API_KEY environment variable).

Usage:
    python tools/extract.py --dry-run                     # estimate cost, send nothing
    python tools/extract.py --levels core --limit 3       # pilot on 3 core articles
    python tools/extract.py --levels core --budget 25     # all core, stop after $25
    python tools/extract.py --levels related --budget 15

One JSON file per article goes to extractions/. Articles already extracted are skipped
(use --force to redo). Every call is logged with its cost in extractions/_runs.csv.
"""
import argparse
import base64
import csv
import datetime as dt
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import jsonschema
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "silver_bulletin"
OUT = ROOT / "extractions"
PROMPT = (ROOT / "prompts" / "extraction_system.md").read_text(encoding="utf-8")
SCHEMA = json.loads((ROOT / "prompts" / "extraction_schema.json").read_text(encoding="utf-8"))
URL = "https://parley.api.mit.edu/v1/chat/completions"

# USD per million tokens (input, output), from Parley's Cost Guidance page, Sept 2026.
PRICES = {
    "claude-opus-5-5": (4.0, 20.0),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-haiku-5-5": (0.10, 0.50),
    "gpt-5.6-sol": (4.0, 20.0),
    "gpt-5.6-terra": (2.0, 12.0),
    "gemini-3.1-pro": (2.0, 12.0),
}
PDF_TOKENS_PER_PAGE = 2000      # rough: page image + extracted text; fits the pilot
# Output incl. thinking. Core = Opus average over 61 articles (2026-11-04); related is still a guess.
OUTPUT_TOKENS_GUESS = {"core": 10000, "related": 6000}
# Parley caches every request automatically: new input is billed as a cache write at 2x the input
# rate, and the shared prompt prefix is then read back at ~5-10% of the input rate on later calls.
CACHE_WRITE_MULT, CACHE_READ_MULT = 2.0, 0.1

lock = threading.Lock()
spent = 0.0
halt = False          # set when Parley says the account is out of credit


class BillingError(RuntimeError):
    pass


def api_key() -> str:
    key = os.environ.get("PARLEY_API_KEY")
    env = ROOT / ".env"
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("PARLEY_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("No API key. Put PARLEY_API_KEY=sk-parley-v1-... in a .env file in the project root.")
    return key


def load_articles(levels):
    meta = {r["url"]: r for r in csv.DictReader((ROOT / "data" / "articles.csv").open(encoding="utf-8"))}
    files = {}
    for r in csv.DictReader((SRC / "index.csv").open(encoding="utf-8")):
        files[r["url"]] = r["file"]          # later rows win, so re-saves replace earlier ones
    arts = []
    for url, m in meta.items():
        if m["relevance"] in levels and url in files and (SRC / f"{files[url]}.txt").exists():
            arts.append({**m, "stem": files[url]})
    return arts


def pdf_pages(path: Path) -> int:
    try:
        return len(PdfReader(path).pages)
    except Exception:
        return 0


def build_messages(art, include_pdf):
    text = (SRC / f"{art['stem']}.txt").read_text(encoding="utf-8")
    header = (f"Article metadata\nTitle: {art['title']}\nSubtitle: {art['subtitle']}\n"
              f"Date: {art['date']}\nAuthors: {art['authors']}\nURL: {art['url']}\n"
              f"Paywalled post: {art['paywalled']}\n\n=== ARTICLE TEXT ===\n{text}")
    content = [{"type": "text", "text": header}]
    if include_pdf:
        data = base64.b64encode((SRC / f"{art['stem']}.pdf").read_bytes()).decode()
        content.insert(0, {"type": "document",
                           "source": {"type": "base64", "media_type": "application/pdf", "data": data}})
        content.append({"type": "text", "text": "The PDF above is the same article as rendered in the "
                        "browser, including charts and tables. Use it for information found only in figures."})
    return [{"role": "system", "content": PROMPT}, {"role": "user", "content": content}], len(text)


def parse_json(s: str):
    s = s.strip()
    s = re.sub(r"^```(?:json)?\s*|\s*```$", "", s)
    return json.loads(s)


def validation_errors(obj):
    v = jsonschema.Draft202012Validator(SCHEMA)
    return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in v.iter_errors(obj)][:15]


def call(key, model, messages, max_tokens):
    body = {"model": model, "messages": messages, "max_tokens": max_tokens,
            "response_format": {"type": "json_schema",
                                "json_schema": {"name": "article_extraction", "schema": SCHEMA, "strict": True}}}
    for attempt in range(4):
        r = requests.post(URL, json=body, timeout=900,
                          headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        if r.status_code in (429, 500, 502, 503, 504) and attempt < 3:
            time.sleep(10 * 2 ** attempt)
            continue
        if r.status_code == 402:
            raise BillingError(f"HTTP 402: {r.text[:300]}")
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
        return r.json(), float(r.headers.get("x-parley-v1-cost", 0) or 0)


def log_run(row):
    path = OUT / "_runs.csv"
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(row))
        if new:
            w.writeheader()
        w.writerow(row)


def process(art, args, key):
    global spent
    level = art["relevance"]
    model = args.model_core if level == "core" else args.model_related
    pdf_path = SRC / f"{art['stem']}.pdf"
    include_pdf = (args.pdf == "all" or (args.pdf == "core" and level == "core")) and pdf_path.exists() \
        and 0 < pdf_pages(pdf_path) <= 100
    messages, _ = build_messages(art, include_pdf)

    cost = 0.0
    usage = {"prompt_tokens": 0, "completion_tokens": 0, "cache_read_tokens": 0, "cache_write_tokens": 0}
    obj, errors, finish, raw = None, ["no response"], "", ""
    for attempt in range(2):                 # first try + one repair round
        resp, c = call(key, model, messages, args.max_tokens)
        cost += c
        u = resp.get("usage", {}) or {}
        details = u.get("prompt_tokens_details", {}) or {}
        usage["prompt_tokens"] += u.get("prompt_tokens", 0) or 0
        usage["completion_tokens"] += u.get("completion_tokens", 0) or 0
        usage["cache_read_tokens"] += details.get("cache_read_input_tokens", 0) or 0
        usage["cache_write_tokens"] += details.get("cache_write_input_tokens", 0) or 0
        choice = resp["choices"][0]
        finish = choice.get("finish_reason", "")
        raw = choice["message"].get("content") or choice["message"].get("refusal") or ""
        if finish == "content_filter":
            errors = ["blocked by Parley content filter"]
            break
        try:
            obj = parse_json(raw)
            errors = validation_errors(obj)
        except json.JSONDecodeError as e:
            obj, errors = None, [f"invalid JSON: {e}"]
        if not errors or finish == "length":
            break
        messages = messages + [
            {"role": "assistant", "content": raw},
            {"role": "user", "content": "Your JSON failed schema validation:\n- " + "\n- ".join(errors)
             + "\nReturn the complete corrected JSON object only."}]

    record = {
        "article": {k: art[k] for k in ("date", "title", "subtitle", "authors", "url", "paywalled", "relevance", "stem")},
        "run": {"model": model, "pdf_included": include_pdf, "cost_usd": round(cost, 6), **usage,
                "finish_reason": finish, "valid": not errors, "validation_errors": errors,
                "timestamp": dt.datetime.now().isoformat(timespec="seconds")},
        "extraction": obj,
    }
    if obj is None:
        record["raw_output"] = raw
    name = f"{art['stem']}.json" if not errors else f"{art['stem']}.INVALID.json"
    (OUT / name).write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    with lock:
        spent += cost
        log_run({"timestamp": record["run"]["timestamp"], "stem": art["stem"], "level": level, "model": model,
                 "pdf": include_pdf, "cost_usd": round(cost, 6), **usage, "finish": finish, "valid": not errors,
                 "n_findings": len((obj or {}).get("findings", []) or [])})
    return art["stem"], cost, errors, (obj or {}).get("model_content_level", "?"), len((obj or {}).get("findings", []) or [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", default="core", help="comma-separated: core,related")
    ap.add_argument("--model-core", default="claude-opus-5-5")
    ap.add_argument("--model-related", default="claude-sonnet-5-5")
    ap.add_argument("--pdf", choices=["core", "all", "none"], default="core",
                    help="which articles also get their PDF (charts/tables)")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", help="only articles whose file name contains this text")
    ap.add_argument("--budget", type=float, default=5.0, help="stop starting new calls after this many USD")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--force", action="store_true", help="redo articles that already have an extraction")
    ap.add_argument("--dry-run", action="store_true", help="estimate cost only; send nothing")
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    arts = load_articles(set(args.levels.split(",")))
    if args.only:
        arts = [a for a in arts if args.only in a["stem"]]
    if not args.force:
        arts = [a for a in arts if not (OUT / f"{a['stem']}.json").exists()]
    arts = arts[: args.limit]

    if args.dry_run:
        prompt_tok = (len(PROMPT) + len(json.dumps(SCHEMA))) // 4
        tot = {}
        for a in arts:
            lvl = a["relevance"]
            model = args.model_core if lvl == "core" else args.model_related
            pin, pout = PRICES.get(model, (0, 0))
            n_new = (SRC / f"{a['stem']}.txt").stat().st_size // 4
            if args.pdf == "all" or (args.pdf == "core" and lvl == "core"):
                n_new += pdf_pages(SRC / f"{a['stem']}.pdf") * PDF_TOKENS_PER_PAGE
            n_in = prompt_tok + n_new
            c = (prompt_tok * pin * CACHE_READ_MULT + n_new * pin * CACHE_WRITE_MULT
                 + OUTPUT_TOKENS_GUESS[lvl] * pout) / 1e6
            t = tot.setdefault((lvl, model), [0, 0, 0.0])
            t[0] += 1; t[1] += n_in; t[2] += c
        print(f"{'level':8} {'model':20} {'articles':>8} {'input tokens':>13} {'est. USD':>9}")
        for (lvl, model), (n, nin, c) in sorted(tot.items()):
            print(f"{lvl:8} {model:20} {n:8} {nin:13,} {c:9.2f}")
        print(f"TOTAL estimate ${sum(t[2] for t in tot.values()):.2f} "
              f"(output tokens assumed per article: {OUTPUT_TOKENS_GUESS})")
        return

    key = api_key()
    print(f"{len(arts)} articles to extract. Budget ${args.budget:.2f}.")
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {}
        it = iter(arts)
        def submit_next():
            with lock:
                if halt or spent >= args.budget:
                    return False
            a = next(it, None)
            if a is None:
                return False
            futures[pool.submit(process, a, args, key)] = a
            return True
        for _ in range(args.workers):
            submit_next()
        while futures:
            for fut in as_completed(list(futures)):
                a = futures.pop(fut)
                done += 1
                try:
                    stem, cost, errors, level, n = fut.result()
                    status = "ok" if not errors else f"INVALID ({errors[0][:80]})"
                    print(f"[{done}/{len(arts)}] ${cost:.3f}  total ${spent:.2f}  {level:6} {n:3} findings  {stem}  {status}")
                except BillingError as e:
                    global halt
                    halt = True
                    print(f"[{done}/{len(arts)}] STOPPED {a['stem']}: Parley credit exhausted. "
                          f"Add billing, then rerun the same command to continue.\n  {e}")
                except Exception as e:
                    print(f"[{done}/{len(arts)}] FAILED {a['stem']}: {e}")
                submit_next()
                break
    print(f"Finished. Spent ${spent:.2f} this run." + ("  Budget reached." if spent >= args.budget else ""))


if __name__ == "__main__":
    main()
