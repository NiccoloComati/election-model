"""Save every open Silver Bulletin tab as a PDF and a plain-text file.

Usage:
  1. Run tools/launch_chrome_debug.bat (opens a separate Chrome on port 9222).
  2. Log in to Silver Bulletin in that window and open the articles you want.
  3. python tools/save_tabs.py            # save all matching tabs
     python tools/save_tabs.py --close    # ...and close each tab once saved

  Or skip opening tabs and let the script visit articles from data/articles.csv:
     python tools/save_tabs.py --from-csv core            # only "core" articles
     python tools/save_tabs.py --from-csv core,related    # core + related

Files go to sources/silver_bulletin/ named YYYY-MM-DD_slug.{pdf,txt}.
Already-saved articles are skipped, so you can rerun as you open more tabs.
An index.csv lists date, title, url for everything saved.
"""
import argparse
import base64
import csv
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "sources" / "silver_bulletin"

META_JS = r"""
() => {
  const m = (sel) => document.querySelector(sel)?.getAttribute('content') || '';
  let date = m('meta[property="article:published_time"]');
  if (!date) {
    for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
      try { const j = JSON.parse(s.textContent); if (j.datePublished) { date = j.datePublished; break; } } catch (e) {}
    }
  }
  if (!date) date = document.querySelector('time')?.getAttribute('datetime') || '';
  const title = document.querySelector('h1.post-title, h1')?.innerText || document.title;
  const subtitle = document.querySelector('h3.subtitle')?.innerText || '';
  const paywalled = !!document.querySelector('[data-testid="paywall"], .paywall');
  const body = ['div.available-content', 'div.body.markup', 'article']
    .map(sel => document.querySelector(sel)).find(Boolean) || document.body;
  return { date, title, subtitle, paywalled, text: body.innerText };
}
"""

SCROLL_JS = """
async () => {
  // capped so infinite-scroll pages (e.g. the homepage) cannot hang the script
  for (let y = 0, i = 0; y < document.body.scrollHeight && i < 80; y += 800, i++) {
    window.scrollTo(0, y);
    await new Promise(r => setTimeout(r, 150));
  }
  window.scrollTo(0, 0);
}
"""


def slugify(s: str, n: int = 80) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower()).strip()
    return re.sub(r"[\s_-]+", "-", s)[:n].strip("-") or "untitled"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=9222)
    ap.add_argument("--match", default="natesilver.net",
                    help="only save tabs whose URL contains this text")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--close", action="store_true", help="close each tab after saving")
    ap.add_argument("--from-csv", metavar="LEVELS",
                    help="visit URLs from data/articles.csv with these relevance levels, comma-separated")
    ap.add_argument("--delay", type=float, default=4.0,
                    help="seconds to wait between articles in --from-csv mode")
    ap.add_argument("--limit", type=int, help="in --from-csv mode, stop after this many articles")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    index_path = args.out / "index.csv"
    seen = set()
    if index_path.exists():
        with index_path.open(newline="", encoding="utf-8") as f:
            # only count an article as saved if its text file is actually on disk
            seen = {row["url"] for row in csv.DictReader(f)
                    if (args.out / f"{row['file']}.txt").exists()}
    new_index = not index_path.exists()

    with sync_playwright() as p, index_path.open("a", newline="", encoding="utf-8") as idx:
        writer = csv.DictWriter(idx, fieldnames=["date", "title", "url", "file"])
        if new_index:
            writer.writeheader()
        try:
            browser = p.chromium.connect_over_cdp(f"http://localhost:{args.port}")
        except Exception as e:
            sys.exit(f"Could not connect to Chrome on port {args.port}. "
                     f"Did you start it with launch_chrome_debug.bat?\n{e}")

        def save(pg, url):
            pg.bring_to_front()
            pg.wait_for_load_state("load", timeout=30000)
            pg.evaluate(SCROLL_JS)          # trigger lazy-loaded charts
            pg.wait_for_timeout(1000)
            meta = pg.evaluate(META_JS)
            date = (meta["date"] or "0000-00-00")[:10]
            stem = f"{date}_{slugify(meta['title'])}"
            cdp = pg.context.new_cdp_session(pg)
            pdf = cdp.send("Page.printToPDF", {"printBackground": True, "preferCSSPageSize": True})
            cdp.detach()
            (args.out / f"{stem}.pdf").write_bytes(base64.b64decode(pdf["data"]))
            header = f"Title: {meta['title']}\nSubtitle: {meta['subtitle']}\nDate: {date}\nURL: {url}\n\n"
            (args.out / f"{stem}.txt").write_text(header + meta["text"], encoding="utf-8")
            writer.writerow({"date": date, "title": meta["title"], "url": url, "file": stem})
            idx.flush()
            seen.add(url)
            warn = "  <-- PAYWALL PREVIEW ONLY: are you logged in?" if meta["paywalled"] else ""
            print(f"  saved  {stem}{warn}")

        saved = skipped = failed = 0
        if args.from_csv:
            levels = set(args.from_csv.split(","))
            with (ROOT / "data" / "articles.csv").open(encoding="utf-8") as f:
                urls = [r["url"] for r in csv.DictReader(f) if r.get("relevance") in levels]
            todo = [u for u in urls if u not in seen]
            skipped = len(urls) - len(todo)
            todo = todo[: args.limit]
            print(f"{len(urls)} articles at levels {sorted(levels)}; {len(todo)} still to save.")
            ctx = browser.contexts[0]
            for n, url in enumerate(todo, 1):
                pg = ctx.new_page()
                try:
                    pg.goto(url, wait_until="load", timeout=60000)
                    print(f"[{n}/{len(todo)}]", end="")
                    save(pg, url)
                    saved += 1
                except Exception as e:
                    failed += 1
                    print(f"  FAILED {url}: {e}")
                finally:
                    pg.close()
                time.sleep(args.delay)   # be polite to the server
        else:
            pages = [pg for c in browser.contexts for pg in c.pages if args.match in pg.url]
            print(f"Found {len(pages)} matching tabs.")
            for pg in pages:
                url = pg.url.split("?")[0].split("#")[0]
                if url in seen:
                    skipped += 1
                    if args.close:
                        pg.close()
                    continue
                try:
                    save(pg, url)
                    saved += 1
                    if args.close:
                        pg.close()
                except Exception as e:
                    failed += 1
                    print(f"  FAILED {url}: {e}")
        print(f"Done. saved={saved} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()
