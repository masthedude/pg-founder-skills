#!/usr/bin/env python3
"""Download the Paul Graham essays each skill references, for local use only.

The essays are copyrighted by Paul Graham and are not redistributed in this
repo. This script reads each skill's references/essays.md, fetches every
listed essay from paulgraham.com, converts it to plain text, and saves it to
that skill's references/essays/ folder. Already-downloaded files are skipped.

Usage:
    python3 scripts/fetch_essays.py                    # skills/ next to this script
    python3 scripts/fetch_essays.py ~/.claude/skills   # skills already installed
"""
import html
import pathlib
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROW = re.compile(r"\|\s*`([a-z0-9]+)\.txt`\s*\|.*?\|\s*(https://paulgraham\.com/[a-z0-9]+\.html)\s*\|")


def to_text(page: str) -> str:
    page = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", "", page)
    page = re.sub(r"(?i)<br\s*/?>", "\n", page)
    page = re.sub(r"(?i)</p>|</tr>|</div>", "\n\n", page)
    page = re.sub(r"(?s)<[^>]+>", "", page)
    page = html.unescape(page)
    page = re.sub(r"[ \t]+\n", "\n", page)
    return re.sub(r"\n{3,}", "\n\n", page).strip() + "\n"


UA = "pg-founder-skills/1.0 (personal local copy)"


def decode(raw: bytes) -> str:
    """paulgraham.com serves some pages as Windows-1252 without declaring it."""
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def download(url: str) -> str:
    """Fetch a page. Falls back to curl when Python lacks root certificates,
    which is common with python.org builds on macOS. Verification stays on."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return decode(resp.read())
    except urllib.error.URLError as exc:
        if not isinstance(exc.reason, ssl.SSLError) or not shutil.which("curl"):
            raise
        out = subprocess.run(["curl", "-sSfL", "-A", UA, "--max-time", "30", url],
                             check=True, capture_output=True)
        return decode(out.stdout)


def main() -> int:
    # Use the first argument that is a folder. Anything else (for example a
    # second script path from a shell glob over several plugin versions) is
    # ignored, and the default is the skills/ folder next to this script.
    dirs = [pathlib.Path(a).expanduser() for a in sys.argv[1:] if pathlib.Path(a).expanduser().is_dir()]
    root = dirs[0] if dirs else pathlib.Path(__file__).resolve().parent.parent / "skills"
    manifests = sorted(root.glob("pg-*/references/essays.md"))
    if not manifests:
        print(f"No pg-* skills with references/essays.md found under {root}")
        return 1
    fetched = skipped = failed = 0
    for manifest in manifests:
        out_dir = manifest.parent / "essays"
        out_dir.mkdir(exist_ok=True)
        for slug, url in ROW.findall(manifest.read_text(encoding="utf-8")):
            target = out_dir / f"{slug}.txt"
            if target.exists() and target.stat().st_size > 0:
                skipped += 1
                continue
            try:
                target.write_text(to_text(download(url)), encoding="utf-8")
                fetched += 1
                print(f"saved  {manifest.parent.parent.name}/{slug}.txt")
                time.sleep(0.5)  # be polite to paulgraham.com
            except Exception as exc:  # keep going if one essay fails
                failed += 1
                print(f"FAILED {url}: {exc}")
    print(f"\nDone: {fetched} fetched, {skipped} already present, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
