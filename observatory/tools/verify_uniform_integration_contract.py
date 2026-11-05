#!/usr/bin/env python3
"""Self-contained structural checks for the Observatory theorem-integration draft.

These tests verify integrity, required content/status markers, and HTML/JavaScript
structure only. They do not certify Yang--Mills mathematics or external source files.
"""
from html.parser import HTMLParser
from pathlib import Path
from pathlib import PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "integration.html"
BRIDGE = ROOT / "UNIFORM_INTERACTING_THEOREM_BRIDGE_2026-11-04.md"
PLAN = ROOT / "DISSERTATION_EVOLUTION_AND_PUBLICATION_PLAN_2026-11-04.md"
GATES = {"P0", "P1", "P2", "P3", "P4", "P5"}


class Tags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicate_ids = []
        self.gates = []
        self.links = []
        self.scripts = 0

    def handle_starttag(self, name, attrs):
        a = dict(attrs)
        if a.get("id"):
            if a["id"] in self.ids:
                self.duplicate_ids.append(a["id"])
            self.ids.add(a["id"])
        if name == "button" and a.get("data-gate"):
            self.gates.append(a["data-gate"])
        if name == "a" and a.get("href"):
            self.links.append(a["href"])
        if name == "script":
            self.scripts += 1


def check():
    assert all(p.is_file() for p in [HTML, BRIDGE, PLAN]), "A required file is missing"
    h = HTML.read_text(encoding="utf-8")
    b = BRIDGE.read_text(encoding="utf-8")
    p = PLAN.read_text(encoding="utf-8")
    dom = Tags()
    dom.feed(h)
    assert not dom.duplicate_ids, f"duplicate HTML ids: {dom.duplicate_ids}"
    assert set(dom.gates) == GATES and len(dom.gates) == len(GATES), dom.gates
    assert dom.scripts == 1, "expected single local script, no third-party analytics"
    assert "mass gap: OPEN" in h and "v2.25-draft" in h
    assert "not deployed" in h.lower()
    assert "not" in h.lower() and "first spectral moment" in h
    assert all(k in h for k in ["physical", "h → 0", "R → ∞", "renormalized", "OS", "P0", "P5"])
    assert "P3 is **route-specific**" in b
    assert "R3-IR-586" in b and "R3-IR-590" in b
    assert "g0(h/2)^2=g0(h)^2/4" in b
    assert "μ_ψ([0,a])" in b and "H_phys" in b
    assert "independent" in b.lower() and "same" in b.lower()
    assert "**No at present**" in p
    assert "v10.7" in p
    assert "Stage26" in p
    for link in dom.links:
        assert not link.startswith("javascript:"), "active JavaScript links not allowed"
        if link.startswith("http"):
            assert link.startswith("https://github.com/syncgravity/singular-boundary/"), link
        elif link.startswith("#"):
            assert link[1:] in dom.ids, f"missing anchor: {link}"
        else:
            assert PurePosixPath(link).name in {"index.html", "integration.html"}, f"unexpected local link {link}"
    assert 'choose(\'P0\')' in h, "gate detail not initialized"
    assert 'document.createElement(\'li\')' in h, "dynamic details should use DOM safe text"
    node = shutil.which("node")
    if node:
        script = h.split("<script>", 1)[1].split("</script>", 1)[0]
        with tempfile.TemporaryDirectory() as d:
            js = Path(d) / "integration.js"
            js.write_text(script)
            subprocess.run([node, "--check", str(js)], check=True, capture_output=True)
        print("PASS: JavaScript syntax via Node --check")
    else:
        print("SKIP: Node unavailable; JavaScript syntax not independently checked")
    print(f"PASS: {len(dom.gates)} unique interactive gates P0-P5")
    print(f"PASS: {len(dom.ids)} unique IDs, {len(dom.links)} allowed links, valid anchors")
    print("PASS: static source scope, P0 correction, OS spectral lemma, publication gates")
    print("LIMIT: No proof correctness, reproducibility of older work or GitHub deployment certified")


if __name__ == "__main__":
    try:
        check()
    except (AssertionError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
