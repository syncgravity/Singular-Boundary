#!/usr/bin/env python3
"""Independently replay the exported n=10 split-demand fiber-flow certificate.

This checker does not run max flow. It reconstructs the finite source/fiber
set and retained multivalued-pi rows, then checks exact fiber conservation,
unit target capacities, and every positive-flow incidence.
"""
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


def edges(value):
    return tuple(tuple(e) for e in value)


def main():
    cert = json.loads(Path("n10_split_demand_flow_certificate.json").read_text())
    assert cert["schema"] == "pf-i16-split-demand-flow-v1"
    assert cert["n"] == 10 and cert["scale"] == 12
    assert cert["source_count"] == 31744
    scale = cert["scale"]

    # Reconstruct exact source-side fiber demands, independently of the
    # max-flow network and its residual graph.
    fibers = defaultdict(lambda: {"demand": Fraction(0), "children": []})
    source_count = 0
    for iv, tau in sources(10):
        source_count += 1
        leaves = nonroot_leaf_indices(iv, tau)
        d = len(leaves)
        for leaf in leaves:
            J = iv[leaf]
            p = parent_data(iv, tau, leaf)
            item = fibers[(p, J)]
            item["demand"] += Fraction(1, d)
            item["children"].append((iv, tau, leaf))
    assert source_count == cert["source_count"]
    assert len(fibers) == cert["fiber_count"]

    targets = [edges(T) for T in cert["targets"]]
    assert len(targets) == cert["target_count"]
    assert len(set(targets)) == len(targets)

    # Reconstruct each retained row. The row is shared by every child in a
    # fixed (parent,J) fiber; verify that identity rather than assume it.
    parent_rows = {}
    eligible_cache = {}
    fiber_records = cert["fibers"]
    assert len(fiber_records) == len(fibers)
    seen_keys = set()
    target_load = [0] * len(targets)
    total_units = 0
    positive_arcs = 0

    for rec in fiber_records:
        parent = (edges(rec["parent_intervals"]), edges(rec["parent_tree"]))
        J = tuple(rec["deleted_interval"])
        key = (parent, J)
        assert key in fibers and key not in seen_keys
        seen_keys.add(key)
        item = fibers[key]
        demand = Fraction(*rec["demand"])
        assert demand == item["demand"]

        iv = edges(rec["representative_intervals"])
        tau = edges(rec["representative_tree"])
        leaf = rec["representative_leaf_index"]
        assert 0 <= leaf < len(iv) and iv[leaf] == J
        assert parent_data(iv, tau, leaf) == parent
        assert (iv, tau, leaf) in item["children"]

        raw = candidate_outputs(iv, tau, forced_last=leaf)
        for civ, ctau, cleaf in item["children"]:
            assert candidate_outputs(civ, ctau, forced_last=cleaf) == raw

        if parent not in parent_rows:
            pi, pt = parent
            if len(pi) == 1:
                parent_rows[parent] = {((1, 2),)}
            else:
                pl = canonical_leaf(pi, pt)
                parent_rows[parent] = candidate_outputs(pi, pt, forced_last=pl)

        eligible = set()
        for T in raw:
            inv = inverse_last_switch(T, J, 10)
            assert len(inv) == 1
            projected = compress_tree(next(iter(inv)), set(J), 10)
            if projected in parent_rows[parent]:
                eligible.add(T)
        eligible_cache[key] = eligible

        assigned_units = 0
        seen_in_fiber = set()
        for target_id, units in rec["assignments"]:
            assert isinstance(target_id, int) and 0 <= target_id < len(targets)
            assert isinstance(units, int) and units > 0
            T = targets[target_id]
            assert T in eligible, ("flow edge not in retained relation", key, T)
            assert target_id not in seen_in_fiber
            seen_in_fiber.add(target_id)
            assigned_units += units
            target_load[target_id] += units
            total_units += units
            positive_arcs += 1
        required = demand * scale
        assert required.denominator == 1
        assert assigned_units == required.numerator, (
            "fiber flow conservation", key, assigned_units, required
        )

    assert seen_keys == set(fibers)
    assert max(target_load, default=0) <= scale
    assert total_units == cert["scaled_total_demand"] == cert["max_flow"]
    assert total_units == sum((v["demand"] for v in fibers.values()), Fraction(0))*scale
    assert sum(load > 0 for load in target_load) == cert["used_target_count"]
    assert max(target_load, default=0) == cert["max_target_load"]

    print("PASS: independent n=10 split-demand flow certificate replay")
    print(f"  sources={source_count} fibers={len(fibers)} targets={len(targets)}")
    print(f"  positive_flow_arcs={positive_arcs}")
    print(f"  used_targets={sum(load > 0 for load in target_load)}")
    print(f"  max_target_load={max(target_load)} / capacity={scale}")
    print(f"  total_scaled_flow={total_units}")


if __name__ == "__main__":
    main()
