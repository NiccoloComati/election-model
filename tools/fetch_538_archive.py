"""Download the most complete (largest non-HTML) Internet Archive copy of FiveThirtyEight data files (site taken down in 2025-26).

Usage: python tools/fetch_538_archive.py
Saves to sources/fivethirtyeight/archive/<original path>, plus archive/index.csv with snapshot dates.
Already-downloaded files are skipped. Silver-era (2008-2023) model outputs and all poll feeds only;
the 2024 forecast (G. Elliott Morris's model) is deliberately excluded.
"""
import csv
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "fivethirtyeight" / "archive"
UA = {"User-Agent": "Mozilla/5.0 (research archive download)"}
PREFIXES = [
    "projects.fivethirtyeight.com/polls/data/",
    "projects.fivethirtyeight.com/polls-page/data/",
    "projects.fivethirtyeight.com/trump-approval-data/",
    "projects.fivethirtyeight.com/biden-approval-data/",
    "projects.fivethirtyeight.com/generic-ballot-data/",
    "projects.fivethirtyeight.com/congress-generic-ballot-polls/",
    "projects.fivethirtyeight.com/2020-general-data/",
    "projects.fivethirtyeight.com/2022-general-election-forecast-data/",
    "projects.fivethirtyeight.com/pollster-ratings/",
    "projects.fivethirtyeight.com/congress-model-2018/",
    "projects.fivethirtyeight.com/2020-primary-data/",
    "projects.fivethirtyeight.com/general-model/",
]
EXT = (".csv", ".zip", ".json", ".xlsx", ".tsv")


def latest_snapshots(prefix):
    for attempt in range(4):
        try:
            r = requests.get("https://web.archive.org/cdx/search/cdx", headers=UA, timeout=180, params={
                "url": prefix + "*", "output": "json", "fl": "original,timestamp,mimetype,length",
                "filter": "statuscode:200"})
            rows = r.json()[1:]
            break
        except Exception:
            time.sleep(15 * (attempt + 1))
    else:
        return {}
    best = {}
    for orig, ts, mime, length in rows:
        key = orig.split("?")[0].replace("http://", "https://").replace(":80/", "/")
        if not key.lower().endswith(EXT) or "html" in (mime or ""):
            continue                      # skip post-shutdown redirect pages archived under the file URL
        size = int(length) if str(length).isdigit() else 0
        # largest copy = most complete data (current-cycle feeds were reset after each election)
        if key not in best or (size, ts) > (best[key][2], best[key][0]):
            best[key] = (ts, mime, size)
    return best


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    previous = {}
    if (OUT / "index.csv").exists():
        with (OUT / "index.csv").open(encoding="utf-8") as f:
            previous = {r["path"]: r["snapshot"] for r in csv.DictReader(f)}
    for prefix in PREFIXES:
        snaps = latest_snapshots(prefix)
        print(f"{prefix}: {len(snaps)} files", flush=True)
        for url, (ts, mime, _size) in sorted(snaps.items()):
            rel = url.split("fivethirtyeight.com/", 1)[1]
            target = OUT / rel
            status = "exists"
            if not target.exists() or previous.get(rel) != ts:
                status = "failed"
                for attempt in range(3):
                    try:
                        r = requests.get(f"https://web.archive.org/web/{ts}id_/{url}", headers=UA, timeout=180)
                        if r.ok and r.content:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            target.write_bytes(r.content)
                            status = "ok"
                            break
                        status = f"HTTP {r.status_code}"
                    except Exception as e:
                        status = f"error {type(e).__name__}"
                    time.sleep(10 * (attempt + 1))
                time.sleep(1.2)          # be polite to the Internet Archive
            index.append({"path": rel, "snapshot": ts, "status": status, "bytes": target.stat().st_size if target.exists() else 0})
        failed = [x for x in index if x["status"] not in ("ok", "exists")]
        print(f"   running total {len(index)} files, {len(failed)} failed", flush=True)
    with (OUT / "index.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(index[0]))
        w.writeheader()
        w.writerows(index)
    print("done:", sum(x["status"] in ("ok", "exists") for x in index), "of", len(index), "saved")


if __name__ == "__main__":
    main()
