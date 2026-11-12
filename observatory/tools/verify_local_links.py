#!/usr/bin/env python3
"""Check local Observatory href/src targets and HTML fragment anchors.

External URLs are intentionally not fetched. This is a deterministic, offline
integrity check for the curated static Observatory tree.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for key in ("href", "src"):
            value = values.get(key)
            if value is not None:
                self.references.append(value)
        for key in ("id", "name"):
            value = values.get(key)
            if value:
                self.anchors.add(value)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def parse_html(path: Path) -> DocumentParser:
    parser = DocumentParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def inside_root(path: Path) -> bool:
    try:
        path.relative_to(ROOT)
        return True
    except ValueError:
        return False


def resolve_target(source: Path, raw: str) -> tuple[Path | None, str]:
    parts = urlsplit(raw.strip())
    if parts.scheme or parts.netloc:
        return None, ""
    target_text = unquote(parts.path)
    if target_text.startswith("/"):
        target = ROOT / target_text.lstrip("/")
    elif target_text:
        target = source.parent / target_text
    else:
        target = source
    target = target.resolve()
    if not inside_root(target):
        return target, parts.fragment
    if target.is_dir():
        target = target / "index.html"
    return target, parts.fragment


def main() -> int:
    pages = sorted(ROOT.rglob("*.html"))
    parsed = {page.resolve(): parse_html(page) for page in pages}
    failures: list[str] = []
    checked = 0
    external = 0

    for source in pages:
        parser = parsed[source.resolve()]
        for raw in parser.references:
            target, fragment = resolve_target(source.resolve(), raw)
            if target is None:
                external += 1
                continue
            checked += 1
            if not inside_root(target) or not target.is_file():
                failures.append(f"{source.relative_to(ROOT)}: missing local target {raw!r}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target.resolve())
                if target_parser is None:
                    target_parser = parse_html(target)
                    parsed[target.resolve()] = target_parser
                if unquote(fragment) not in target_parser.anchors:
                    failures.append(
                        f"{source.relative_to(ROOT)}: missing anchor #{fragment} in "
                        f"{target.relative_to(ROOT)}"
                    )

    if failures:
        print("FAIL: Observatory local-link integrity")
        for failure in failures:
            print(f" - {failure}")
        return 1
    print(f"PASS: {len(pages)} HTML pages; {checked} local href/src targets; "
          f"{external} external references skipped")
    print("PASS: all local HTML fragments resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
