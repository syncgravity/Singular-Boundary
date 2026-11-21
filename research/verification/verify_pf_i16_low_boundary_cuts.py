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
    found = "LOW_SLACK_WITNESS" in result.stdout
    passed = "NO_BOUNDARY_AT_MOST_2" in result.stdout
    return found, passed


if __name__ == "__main__":
    # n=6 is a positive control: the known two-source/two-slack obstruction
    # must be recovered. n=8 is the target: no boundary of size <=2 may exist.
    found6, passed6 = run(6)
    assert found6 and not passed6, "n=6 positive control was not recovered"
    found8, passed8 = run(8)
    assert passed8 and not found8, "n=8 has a Hall-slack <=2 witness"
    print("Exact low-boundary cut census: PASS")
