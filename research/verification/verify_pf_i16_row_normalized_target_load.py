#!/usr/bin/env python3
"""Exact row-normalized fractional-allocation test for PF-I16.

For every global fiber F=(p,J), construct its complete retained multivalued-pi
row N(F) and exact split demand delta(F). Test the sufficient allocation
lambda(F,T)=delta(F)/|N(F)| on every T in N(F). It is feasible exactly when
each target load L(T)=sum_{F:T in N(F)} delta(F)/|N(F)| is at most one.
This is a finite diagnostic, not an all-orders proof.
"""
import json
from collections import defaultdict, Counter
from fractions import Fraction
from pathlib import Path

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


def run(n, expected_sources):
    fibers = defaultdict(lambda: {
        "demand": Fraction(0), "children": 0, "representative": None
    })
    source_count = 0
    for intervals, tau in sources(n):
        source_count += 1
        leaves = nonroot_leaf_indices(intervals, tau)
        d = len(leaves)
        for leaf in leaves:
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            item = fibers[(parent, J)]
            item["demand"] += Fraction(1, d)
            item["children"] += 1
            if item["representative"] is None:
                item["representative"] = (intervals, tau, leaf)
    assert source_count == expected_sources, (n, source_count, expected_sources)

    parent_rows = {}
    target_load = defaultdict(Fraction)
    target_incident = defaultdict(list)
    fiber_records = []
    incidence_count = 0

    for idx, (key, item) in enumerate(fibers.items()):
        parent, J = key
        if parent not in parent_rows:
            pi, pt = parent
            if len(pi) == 1:
                parent_rows[parent] = {((1, 2),)}
            else:
                pl = canonical_leaf(pi, pt)
                parent_rows[parent] = candidate_outputs(pi, pt, forced_last=pl)

        intervals, tau, leaf = item["representative"]
        raw = candidate_outputs(intervals, tau, forced_last=leaf)
        for civ, ctau, cleaf in []:
            pass
        row = set()
        for T in raw:
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1, (n, key, T, inv)
            projected = compress_tree(next(iter(inv)), set(J), n)
            if projected in parent_rows[parent]:
                row.add(T)
        row = frozenset(row)
        assert row, (n, "empty retained fiber row", key, item["children"])

        demand = item["demand"]
        share = demand / len(row)
        record = {
            "parent": parent,
            "deleted_interval": J,
            "demand": demand,
            "row_size": len(row),
            "children": item["children"],
        }
        fiber_records.append(record)
        for T in row:
            target_load[T] += share
            target_incident[T].append(idx)
        incidence_count += len(row)

        if (idx + 1) % 2000 == 0:
            print(f"n={n} processed_fibers={idx+1}/{len(fibers)} "
                  f"targets={len(target_load)}", flush=True)

    assert len(fiber_records) == len(fibers)
    worst_target, worst_load = max(target_load.items(), key=lambda kv: kv[1])
    overloaded = [(T, load) for T, load in target_load.items() if load > 1]
    load_hist = Counter(target_load.values())
    print(f"ROW_NORMALIZED_RESULT n={n}")
    print(f"  sources={source_count} fibers={len(fibers)}")
    print(f"  targets={len(target_load)} fiber_target_incidences={incidence_count}")
    print(f"  max_target_load={worst_load} overloaded_targets={len(overloaded)}")
    print(f"  target_load_histogram={dict(sorted(load_hist.items()))}")
    print(f"  worst_target={worst_target}")
    print(f"  worst_target_incident_fibers={len(target_incident[worst_target])}")

    if overloaded:
        overloaded.sort(key=lambda item: item[1], reverse=True)
        witness_target, witness_load = overloaded[0]
        incident = []
        for i in target_incident[witness_target]:
            rec = fiber_records[i]
            p = rec["parent"]
            incident.append({
                "parent_intervals": [list(e) for e in p[0]],
                "parent_tree": [list(e) for e in p[1]],
                "deleted_interval": list(rec["deleted_interval"]),
                "demand": [rec["demand"].numerator, rec["demand"].denominator],
                "row_size": rec["row_size"],
                "children": rec["children"],
            })
        witness = {
            "n": n,
            "target": [list(e) for e in witness_target],
            "load": [witness_load.numerator, witness_load.denominator],
            "overloaded_target_count": len(overloaded),
            "incident_fibers": incident,
        }
        path = Path(f"row_normalized_n{n}_overload_witness.json")
        path.write_text(json.dumps(witness, separators=(",", ":")), encoding="utf-8")
        print(f"  witness={path} incident_fibers={len(incident)}")
        print("  RESULT: row-normalized sufficient condition FAILS at this finite order")
        return False

    print("  RESULT: row-normalized sufficient condition PASSES this finite order")
    return True


if __name__ == "__main__":
    result8 = run(8, 608)
    result10 = run(10, 31744)
    print(f"FINITE_DIAGNOSTIC_SUMMARY n8_pass={result8} n10_pass={result10}")
