"""Download the datasets linked from saved Silver Bulletin pages.

Links are read from the hyperlinks Chrome preserved in sources/silver_bulletin/*.pdf.

  python tools/download_datasets.py charts   # public Datawrapper chart CSVs ("Get the data")
  python tools/download_datasets.py sheets   # published Google Sheets (poll databases), as CSV
  python tools/download_datasets.py hosted   # Silver Bulletin-hosted XLSX files (needs login:
                                             # run tools/launch_chrome_debug.bat first, logged in)

Output goes to data/silver_bulletin_datasets/{charts,sheets,hosted}/ with an index.csv in each.
Files already downloaded are skipped.
"""
import csv
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "silver_bulletin"
OUT = ROOT / "data" / "silver_bulletin_datasets"
UA = {"User-Agent": "Mozilla/5.0 (research download script)"}


def pdf_links():
    """Map each URL to the set of article stems whose PDF links to it."""
    links = defaultdict(set)
    for p in sorted(SRC.glob("*.pdf")):
        try:
            pages = PdfReader(p).pages
        except Exception:
            continue
        for page in pages:
            for a in page.get("/Annots") or []:
                u = (a.get_object().get("/A") or {}).get("/URI")
                if u:
                    links[str(u)].add(p.stem)
    return links


def slug(s, n=70):
    s = re.sub(r"[^\w\s-]", "", (s or "").lower()).strip()
    return re.sub(r"[\s_-]+", "-", s)[:n].strip("-") or "untitled"


def write_index(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def charts(links):
    out = OUT / "charts"
    out.mkdir(parents=True, exist_ok=True)
    ids, versions = defaultdict(set), defaultdict(set)
    for u, stems in links.items():
        m = re.search(r"(?:datawrapper\.dwcdn\.net|static\.dwcdn\.net/data)/(\w{5})\b(?:/(\d+))?", u)
        if m:
            ids[m.group(1)] |= stems
            if m.group(2):
                versions[m.group(1)].add(int(m.group(2)))

    def fetch(cid):
        stems = sorted(ids[cid])
        title = ""
        try:
            h = requests.get(f"https://datawrapper.dwcdn.net/{cid}/", headers=UA, timeout=30)
            m = re.search(r"<title>(.*?)</title>", h.text, re.S)
            title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
        except Exception:
            pass
        fname = f"{cid}__{slug(title)}.csv"
        target = out / stems[0] / fname
        status = "exists"
        if not target.exists():
            r = requests.get(f"https://static.dwcdn.net/data/{cid}.csv", headers=UA, timeout=30)
            if not r.ok:   # fallback: versioned dataset (tab-separated), newest known version first
                for v in sorted(versions[cid] or {1}, reverse=True):
                    r = requests.get(f"https://datawrapper.dwcdn.net/{cid}/{v}/dataset.csv", headers=UA, timeout=30)
                    if r.ok:
                        break
            if r.ok and r.content:
                target.parent.mkdir(exist_ok=True)
                target.write_bytes(r.content)
                status = "ok"
            else:
                status = f"HTTP {r.status_code}"
        time.sleep(0.2)
        return {"chart_id": cid, "title": title, "status": status, "file": str(target.relative_to(OUT)) if status in ("ok", "exists") else "",
                "first_article": stems[0], "all_articles": "; ".join(stems)}

    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch, sorted(ids)))
    rows.sort(key=lambda r: (r["first_article"], r["chart_id"]))
    write_index(out / "index.csv", rows)
    bad = [r for r in rows if r["status"] not in ("ok", "exists")]
    print(f"charts: {len(rows)} found, {len(rows) - len(bad)} saved, {len(bad)} failed")
    for r in bad[:10]:
        print("  failed", r["chart_id"], r["status"])


def sheets(links):
    out = OUT / "sheets"
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for u, stems in sorted(links.items()):
        m = re.search(r"docs\.google\.com/spreadsheets/d/e/([\w-]+)", u)
        if not m:
            continue
        key = m.group(1)
        gid = re.search(r"[?&#]gid=(\d+)", u)
        export = f"https://docs.google.com/spreadsheets/d/e/{key}/pub?output=csv" + (f"&gid={gid.group(1)}" if gid else "")
        name = f"{sorted(stems)[-1]}__{key[-8:]}" + (f"_gid{gid.group(1)}" if gid else "") + ".csv"
        target = out / name
        status = "exists"
        if not target.exists():
            r = requests.get(export, headers=UA, timeout=60)
            ok = r.ok and "text/csv" in r.headers.get("content-type", "")
            if ok:
                target.write_bytes(r.content)
            status = "ok" if ok else f"HTTP {r.status_code} {r.headers.get('content-type', '')[:30]}"
        rows.append({"file": name, "status": status, "source_url": u, "articles": "; ".join(sorted(stems))})
        print(f"  {status:8} {name}")
    write_index(out / "index.csv", rows)
    print(f"sheets: {len(rows)} links")


def hosted(links, port=9222):
    from playwright.sync_api import sync_playwright
    out = OUT / "hosted"
    out.mkdir(parents=True, exist_ok=True)
    urls = {u.split("?")[0]: stems for u, stems in links.items() if "natesilver.net/api/v1/file/" in u}
    rows = []
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://localhost:{port}")
        except Exception as e:
            sys.exit(f"Could not connect to Chrome on port {port}. Run tools/launch_chrome_debug.bat and log in.\n{e}")
        ctx = browser.contexts[0]
        for u, stems in sorted(urls.items(), key=lambda kv: sorted(kv[1])[-1]):
            fid = u.rsplit("/", 1)[-1].split(".")[0]
            done = list(out.glob(f"*__{fid[:8]}.xlsx"))
            if done:
                rows.append({"file": done[0].name, "status": "exists", "url": u, "articles": "; ".join(sorted(stems))})
                continue
            r = ctx.request.get(u, timeout=120000)          # uses the browser's logged-in cookies
            ctype = r.headers.get("content-type", "")
            if r.ok and "html" not in ctype:
                cd = r.headers.get("content-disposition", "")
                m = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)', cd)
                orig = requests.utils.unquote(m.group(1)) if m else "file.xlsx"
                name = f"{sorted(stems)[-1][:10]}_{slug(Path(orig).stem, 50)}__{fid[:8]}.xlsx"
                (out / name).write_bytes(r.body())
                status = "ok"
            else:
                name, status = "", f"HTTP {r.status} {ctype[:20]} (logged in?)"
            rows.append({"file": name, "status": status, "url": u, "articles": "; ".join(sorted(stems))})
            print(f"  {status:8} {name or u}")
            time.sleep(1.5)
    write_index(out / "index.csv", rows)
    print(f"hosted: {sum(r['status'] in ('ok', 'exists') for r in rows)} of {len(rows)} saved")


if __name__ == "__main__":
    what = sys.argv[1:] or ["charts", "sheets"]
    L = pdf_links()
    print(f"{len(L)} links read from PDFs")
    for w in what:
        {"charts": charts, "sheets": sheets, "hosted": hosted}[w](L)
