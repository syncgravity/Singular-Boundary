#!/usr/bin/env python3
"""Export the exact matching-relative digraph and run the C++ low-cut census."""
import subprocess
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case, hopcroft_karp


def run(n):
    rows, _, _ = build_case(n)
    ml, mr, right = hopcroft_karp(rows)
    assert all(x >= 0 for x in ml), (n, "base matching not left-saturating")
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    free = sorted(set(right) - set(owner))
    free_id = {t: i for i, t in enumerate(free)}
    arcs = []
    free_rows = []
    for x, row in enumerate(rows):
        out = sorted({owner[t] for t in row if t in owner and owner[t] != x})
        arcs.extend((x, y) for y in out)
        free_rows.append(sorted({free_id[t] for t in row if t in free_id}))

    lines = [f"{len(rows)} {len(arcs)} {len(free)}"]
    lines.extend(f"{u} {v}" for u, v in arcs)
    lines.extend(str(len(ts)) + (" " + " ".join(map(str, ts)) if ts else "")
                 for ts in free_rows)
    payload = "\n".join(lines) + "\n"
    result = subprocess.run(
        ["./pf_i16_low_boundary_cuts"],
        input=payload, text=True, capture_output=True, check=True,
    )
    print(f"n={n}: sources={len(rows)}, targets={len(right)}, "
          f"free_targets={len(free)}, arcs={len(arcs)}")
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr)
    if "NO_BOUNDARY_AT_MOST_2" not in result.stdout:
        raise SystemExit(f"n={n}: low Hall-slack witness found")


if __name__ == "__main__":
    run(6)
    run(8)
