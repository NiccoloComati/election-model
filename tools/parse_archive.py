"""Turn a saved Silver Bulletin archive page into data/articles.csv.

Usage: python tools/parse_archive.py ["Archive - Silver Bulletin.html"]
One row per article: date, title, subtitle, authors, paywalled, likes, comments, url, slug.
"""
import csv
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "Archive - Silver Bulletin.html"
out = ROOT / "data" / "articles.csv"

soup = BeautifulSoup(src.read_text(encoding="utf-8"), "lxml")
rows, seen = [], set()
for t in soup.select('a[data-testid="post-preview-title"]'):
    url = t["href"].split("?")[0]
    if url in seen:
        continue
    seen.add(url)
    card = t
    while card is not None and card.find("time") is None:
        card = card.parent
    links = [a for a in card.find_all("a", href=True) if a["href"].split("?")[0] == url]
    subtitle = links[1].get_text(" ", strip=True) if len(links) > 1 else ""
    time = card.find("time")
    authors = [a.get_text(strip=True) for a in card.select('a[href^="https://substack.com/@"]')]
    like = card.find("button", attrs={"aria-label": re.compile(r"^Like")})
    com = card.find("button", attrs={"aria-label": re.compile(r"comments")})
    num = lambda b: (re.search(r"\((\d+)\)", b["aria-label"]) or [None, ""])[1] if b else ""
    rows.append({
        "date": time["datetime"][:10] if time else "",
        "title": t.get_text(" ", strip=True),
        "subtitle": subtitle,
        "authors": "; ".join(dict.fromkeys(authors)),
        "paywalled": bool(card.select_one("svg.lucide-lock")),
        "likes": num(like),
        "comments": num(com),
        "url": url,
        "slug": url.rstrip("/").rsplit("/", 1)[-1],
    })

rows.sort(key=lambda r: r["date"])
out.parent.mkdir(exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"{len(rows)} articles, {rows[0]['date']} to {rows[-1]['date']} -> {out}")
