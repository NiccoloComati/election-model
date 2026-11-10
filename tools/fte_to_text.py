"""Convert archived FiveThirtyEight methodology pages (Wayback Machine HTML) to plain text.

Usage: python tools/fte_to_text.py
Reads sources/fivethirtyeight/raw/*.html, writes sources/fivethirtyeight/<name>.txt with a header
(Title, Date, URL, Authors) in the same shape as the Silver Bulletin text files.
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "sources" / "fivethirtyeight" / "raw"
OUT = ROOT / "sources" / "fivethirtyeight"

for p in sorted(RAW.glob("*.html")):
    soup = BeautifulSoup(p.read_text(encoding="utf-8", errors="ignore"), "lxml")
    for bad in soup(["script", "style", "noscript", "iframe", "svg"]):
        bad.decompose()
    title = (soup.find("h1") or soup.title).get_text(" ", strip=True)
    canon = soup.find("link", rel="canonical")
    url = canon["href"] if canon else ""
    t = soup.find("time")
    date = (t.get("datetime") or t.get_text(strip=True)) if t else ""
    meta_date = soup.find("meta", attrs={"property": "article:published_time"})
    if meta_date:
        date = meta_date["content"]
    authors = sorted({a.get_text(strip=True) for a in soup.select('a[rel="author"], .author a, .single-header-metadata-wrap .author')
                      if a.get_text(strip=True)})
    body = soup.select_one("div.entry-content, div.single-post-content, article") or soup.body
    blocks = []
    for el in body.find_all(["h2", "h3", "h4", "p", "li", "blockquote", "table", "figcaption"]):
        if el.find_parent(["li", "table", "blockquote"]) and el.name != "table":
            continue                       # avoid duplicating nested text
        if el.name == "table":
            rows = [" | ".join(c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])) for tr in el.find_all("tr")]
            blocks.append("\n".join(rows))
            continue
        txt = el.get_text(" ", strip=True)
        if not txt:
            continue
        if el.name in ("h2", "h3", "h4"):
            txt = f"\n## {txt}"
        elif el.name == "li":
            txt = f"- {txt}"
        blocks.append(txt)
    text = re.sub(r"\n{3,}", "\n\n", "\n\n".join(blocks))
    header = (f"Title: {title}\nSubtitle: \nDate: {date[:10]}\nURL: {url}\nAuthors: {', '.join(authors)}\n"
              f"Source: Internet Archive copy of FiveThirtyEight (site taken down by Disney in 2026)\n\n")
    (OUT / f"{p.stem}.txt").write_text(header + text, encoding="utf-8")
    print(f"{p.stem}: {len(text):,} chars, date {date[:10]}, authors {authors}")
