#!/usr/bin/env python3
"""Records how many times each app release file has been downloaded.

GitHub counts every download of a release file but only keeps the running
total, so this takes a snapshot once a day and appends it to a CSV. The
difference between two days is that day's downloads. It reads public release
data only; nothing about who downloaded is known or stored.

Usage: download_stats.py <repo> <csv-path>   e.g. pesaclarity/pesaclarity-app stats/downloads.csv
"""

import csv
import datetime
import json
import os
import sys
import urllib.request


def releases(repo: str) -> list[dict]:
    out, page = [], 1
    while True:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}",
            headers={"Accept": "application/vnd.github+json"},
        )
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            batch = json.load(resp)
        if not batch:
            return out
        out.extend(batch)
        page += 1


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 64
    repo, path = sys.argv[1], sys.argv[2]
    today = datetime.date.today().isoformat()

    rows = [
        {"date": today, "release": r["tag_name"], "file": a["name"], "downloads": a["download_count"]}
        for r in releases(repo)
        for a in r["assets"]
    ]

    previous: dict[tuple[str, str], int] = {}
    existing = []
    if os.path.exists(path):
        with open(path, newline="") as f:
            existing = [row for row in csv.DictReader(f) if row["date"] != today]
        for row in existing:  # last snapshot before today, per file
            previous[(row["release"], row["file"])] = int(row["downloads"])

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "release", "file", "downloads"])
        writer.writeheader()
        writer.writerows(existing + rows)

    total = sum(r["downloads"] for r in rows)
    def since(r: dict) -> int:
        before = previous.get((r["release"], r["file"]), 0)
        # A replaced file (the rolling test build) starts counting from zero again.
        return r["downloads"] - before if r["downloads"] >= before else r["downloads"]

    new = sum(since(r) for r in rows)
    lines = [
        f"## App downloads on {today}",
        "",
        f"All time: **{total}**. Since the previous day's snapshot: **{new}**.",
        "",
        "| Release | File | Downloads |",
        "|---|---|---|",
        *(f"| {r['release']} | {r['file']} | {r['downloads']} |" for r in rows),
    ]
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
