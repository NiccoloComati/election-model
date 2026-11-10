"""Add a `relevance` column to data/articles.csv: core / related / unrelated.

Classification was done by hand (Claude, 2026-11-04) from title + subtitle, using row
indices in date order. Recall-first: anything touching elections, polls, public opinion,
or politics is at least `related`; `core` = likely contains model mechanics, polling
methodology, forecast reasoning, or polling-error/fundamentals discussion.
Edit the sets below to override.
"""
import csv
from pathlib import Path

CORE = {7, 23, 24, 49, 64, 83, 104, 105, 106, 107, 110, 112, 119, 126, 127, 128, 130, 135,
        147, 148, 151, 152, 153, 154, 157, 162, 163, 164, 165, 166, 167, 168, 169, 173, 174,
        175, 176, 178, 179, 182, 183, 184, 188, 190, 191, 192, 195, 196, 198, 203, 217, 228,
        229, 244, 261, 268, 290, 294, 332, 333, 334, 337, 338, 363, 374, 377, 393, 407, 422,
        423, 424, 425, 427, 428, 429, 430, 431, 440, 442, 445, 448, 453, 454, 456, 457, 458,
        459, 460, 465, 467, 471, 472, 473, 474, 475, 476, 477, 480}
UNRELATED = {0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 16, 20, 22, 27, 28, 29, 31, 33, 34, 36,
             37, 38, 45, 52, 56, 58, 61, 69, 70, 71, 72, 73, 74, 75, 77, 82, 85, 86, 87, 91,
             92, 96, 97, 101, 103, 125, 137, 138, 140, 142, 202, 208, 209, 211, 212, 214, 215,
             216, 223, 225, 227, 230, 232, 233, 237, 240, 242, 243, 247, 250, 251, 256, 265,
             266, 269, 277, 281, 282, 284, 287, 292, 295, 300, 302, 304, 307, 311, 316, 318,
             319, 325, 326, 328, 330, 335, 341, 343, 344, 346, 347, 351, 355, 360, 364, 366,
             367, 368, 369, 371, 372, 375, 376, 383, 387, 388, 389, 392, 394, 396, 397, 399,
             400, 403, 404, 405, 406, 410, 414, 415, 416, 418, 432, 434, 435, 438, 444, 447,
             455, 478, 479}
assert not CORE & UNRELATED

path = Path(__file__).resolve().parents[1] / "data" / "articles.csv"
rows = list(csv.DictReader(path.open(encoding="utf-8")))
for i, r in enumerate(rows):
    r["relevance"] = "core" if i in CORE else "unrelated" if i in UNRELATED else "related"
with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
from collections import Counter
c = Counter((r["relevance"], r["paywalled"]) for r in rows)
for k in ("core", "related", "unrelated"):
    print(f"{k:10} total={c[(k,'True')]+c[(k,'False')]:4}  paywalled={c[(k,'True')]}")
