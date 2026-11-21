#!/usr/bin/env python3
"""Exact matching-relative SCC census for multivalued-pi graphs at n=4,6,8."""
from verify_pf_i16_n10_multivalued_pi_exchange_scc import build_rows
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_full_leaf_last_graph_n10 import sink_scc_census


def run(n):
    rows, raw, parents = build_rows(n)
    ml, mr, right = hopcroft_karp(rows)
    matching = sum(v >= 0 for v in ml)
    print(f"n={n}: sources={len(rows)} parent_sources={parents} "
          f"incidences={sum(map(len, rows))} targets={len(right)} "
          f"matching={matching}/{len(rows)}")
    if matching != len(rows):
        raise AssertionError(f"no saturating matching at n={n}")
    census = sink_scc_census(rows, ml, mr, right)
    zero = [x for x in census if x[1] == 0]
    print(f"n={n}: sink_scc_count={len(census)} "
          f"zero_free_sink_scc_count={len(zero)}")
    if zero:
        raise AssertionError(f"zero-free sink SCC at n={n}: {zero}")


if __name__ == "__main__":
    for n in (4, 6, 8):
        run(n)
