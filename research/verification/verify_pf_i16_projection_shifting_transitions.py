#!/usr/bin/env python3
"""Exact PF-I16 projection-shifting transition census (n=6,8).

A certified transition is a witnessed D-S-D path in the source-mark incidence
complex. At a common retained target T for marks J,K, first verify the
mutually-surviving deletion diamond. Move by a sibling-lift S edge from T to
T' while preserving (J,parent-target P). At T', verify a second mutually
surviving J,K diamond and record the changed K-parent projection Q -> Q'.

Every inverse uses the repository's full inverse/compression routines plus
explicit no-reinsertion and positive-overlap checks. The common double inverse
is checked in the ordinary C(r), never assumed canonical.

This is a finite diagnostic, not a capacity theorem or an all-orders result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources,
    parent_data,
    canonical_leaf,
    inverse_last_switch,
    compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices

sys.setrecursionlimit(100000)

EXPECTED = {
    6: {"sources": 22, "ordered_leaf_pairs": 16, "common_incidences": 74,
        "unordered_leaf_pairs": 8, "unordered_common_incidences": 37},
    8: {"sources": 608, "ordered_leaf_pairs": 980, "common_incidences": 22172,
        "unordered_leaf_pairs": 490, "unordered_common_incidences": 11086},
}


def overlaps(edge, interval):
    u, v = sorted(edge)
    a, b = interval
    return max(u, a) < min(v, b)


def exact_guarded_inverse(tree, mark, n):
    """Return (uncompressed parent tree, restored edge, removed local edges).

    The repository inverse checks the unique four-vertex local tree. This
    wrapper additionally checks no-reinsertion and positive interval overlap.
    """
    try:
        inverse = inverse_last_switch(tree, mark, n)
    except (AssertionError, KeyError, ValueError):
        return None
    if not inverse or len(inverse) != 1:
        return None
    parent = next(iter(inverse))
    old = set(parent) - set(tree)
    removed = set(tree) - set(parent)
    if len(old) != 1 or len(removed) != 3:
        return None
    restored = next(iter(old))
    if restored in tree or not overlaps(restored, mark):
        return None
    return parent, restored, tuple(sorted(removed))


def compress_mark(mark, removed, n):
    remaining = [x for x in range(1, n + 1) if x not in removed]
    rank = {x: i + 1 for i, x in enumerate(remaining)}
    return tuple(sorted(rank[x] for x in mark))


def canonical_parent_targets(parent, cache):
    if parent not in cache:
        intervals, tau = parent
        if len(intervals) == 1:
            cache[parent] = {((1, 2),)}
        else:
            leaf = canonical_leaf(intervals, tau)
            cache[parent] = candidate_outputs(intervals, tau, forced_last=leaf)
        assert cache[parent]
    return cache[parent]


def ordinary_parent_targets(parent, cache):
    if parent not in cache:
        intervals, tau = parent
        if len(intervals) == 1:
            cache[parent] = {((1, 2),)}
        else:
            cache[parent] = candidate_outputs(intervals, tau)
        assert cache[parent]
    return cache[parent]


def encode_tree(tree):
    return [list(edge) for edge in sorted(tree)]


def mutual_diamond(target, intervals, tau, J, K, n, source_index,
                   ordinary_cache, diamond_cache):
    """Exact same-source D-edge certificate for two disjoint eligible marks."""
    key = (source_index, target, intervals[J], intervals[K])
    if key in diamond_cache:
        return diamond_cache[key]

    markJ, markK = intervals[J], intervals[K]
    invJ = exact_guarded_inverse(target, markJ, n)
    invK = exact_guarded_inverse(target, markK, n)
    if invJ is None or invK is None:
        diamond_cache[key] = None
        return None

    parentJ, restoredJ, removedJ = invJ
    parentK, restoredK, removedK = invK
    projectedJ = compress_tree(parentJ, set(markJ), n)
    projectedK = compress_tree(parentK, set(markK), n)
    markK_after_J = compress_mark(markK, set(markJ), n)
    markJ_after_K = compress_mark(markJ, set(markK), n)

    # Both second inverses must survive in the opposite compressed parent.
    invK_after_J = exact_guarded_inverse(projectedJ, markK_after_J, n - 2)
    invJ_after_K = exact_guarded_inverse(projectedK, markJ_after_K, n - 2)
    if invK_after_J is None or invJ_after_K is None:
        diamond_cache[key] = None
        return None

    parentK_after_J, restoredK_after_J, removedK_after_J = invK_after_J
    parentJ_after_K, restoredJ_after_K, removedJ_after_K = invJ_after_K
    U_JK = compress_tree(parentK_after_J, set(markK_after_J), n - 2)
    U_KJ = compress_tree(parentJ_after_K, set(markJ_after_K), n - 2)
    if U_JK != U_KJ:
        raise AssertionError(
            ("mutually surviving reverse orders disagree",
             n, intervals, tau, markJ, markK, target, U_JK, U_KJ)
        )

    # The two source deletions must produce the same ordinary grandparent.
    parentJ_source = parent_data(intervals, tau, J)
    pJ_intervals, pJ_tau = parentJ_source
    k_in_pJ = pJ_intervals.index(markK_after_J)
    r_from_J = parent_data(pJ_intervals, pJ_tau, k_in_pJ)

    parentK_source = parent_data(intervals, tau, K)
    pK_intervals, pK_tau = parentK_source
    j_in_pK = pK_intervals.index(markJ_after_K)
    r_from_K = parent_data(pK_intervals, pK_tau, j_in_pK)
    if r_from_J != r_from_K:
        raise AssertionError(("source deletion diamond mismatch", r_from_J, r_from_K))

    if U_JK not in ordinary_parent_targets(r_from_J, ordinary_cache):
        raise AssertionError(
            ("mutual target inverse not in ordinary common-parent neighborhood",
             n, intervals, tau, markJ, markK, target, U_JK, r_from_J)
        )

    witness = {
        "U": U_JK,
        "projected_J": projectedJ,
        "projected_K": projectedK,
        "J_restored_edge": restoredJ,
        "J_removed_edges": removedJ,
        "K_restored_edge": restoredK,
        "K_removed_edges": removedK,
        "K_after_J_restored_edge": restoredK_after_J,
        "K_after_J_removed_edges": removedK_after_J,
        "J_after_K_restored_edge": restoredJ_after_K,
        "J_after_K_removed_edges": removedJ_after_K,
        "common_parent_source": r_from_J,
    }
    diamond_cache[key] = witness
    return witness


def tarjan_scc(adjacency):
    nodes = set(adjacency)
    for targets in adjacency.values():
        nodes.update(targets)
    index = 0
    stack = []
    on_stack = set()
    indices = {}
    low = {}
    components = []

    def visit(v):
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adjacency.get(v, ()):
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            components.append(component)

    for v in sorted(nodes):
        if v not in indices:
            visit(v)
    return components


def summarize_graphs(graphs):
    total_sccs = 0
    sink_sccs = 0
    sink_hist = Counter()
    max_scc = 0
    nontrivial_sccs = 0
    graphs_with_shift = 0
    graph_summaries = []

    for key, record in graphs.items():
        adjacency = record["adj"]
        components = tarjan_scc(adjacency)
        component_of = {}
        for i, component in enumerate(components):
            for node in component:
                component_of[node] = i
        outgoing = [set() for _ in components]
        for u, targets in adjacency.items():
            cu = component_of[u]
            for v in targets:
                cv = component_of[v]
                if cu != cv:
                    outgoing[cu].add(cv)
        sinks = [components[i] for i, out in enumerate(outgoing) if not out]
        total_sccs += len(components)
        sink_sccs += len(sinks)
        max_scc = max(max_scc, max(map(len, components), default=0))
        nontrivial_sccs += sum(len(c) > 1 for c in components)
        for component in sinks:
            sink_hist[len(component)] += 1
        if record["shifted_arc_set"]:
            graphs_with_shift += 1
        nodes = set(adjacency)
        for targets in adjacency.values():
            nodes.update(targets)
        graph_summaries.append({
            "source_index": key[0],
            "J": list(key[1]),
            "K": list(key[2]),
            "P": encode_tree(key[3]),
            "vertices": len(nodes),
            "arcs": len(record["arc_set"]),
            "shifted_arcs": len(record["shifted_arc_set"]),
            "transition_witnesses": record["witness_count"],
            "scc_sizes": sorted((len(c) for c in components), reverse=True),
            "sink_scc_sizes": sorted((len(c) for c in sinks), reverse=True),
        })

    return {
        "projection_graphs": len(graphs),
        "graphs_with_projection_shifts": graphs_with_shift,
        "total_sccs": total_sccs,
        "nontrivial_sccs": nontrivial_sccs,
        "sink_sccs": sink_sccs,
        "sink_scc_size_histogram": dict(sorted(sink_hist.items())),
        "maximum_scc_size": max_scc,
        "per_graph": graph_summaries,
    }


def census(n):
    expected = EXPECTED[n]
    source_count = 0
    unordered_pairs = 0
    unordered_common = 0
    ordered_pairs = 0
    ordered_common = 0
    stable_hist = Counter()
    max_stable = 0
    projection_graphs = {}
    transitions = []
    transition_count = 0
    shifted_count = 0
    loop_count = 0
    j_inverse_rejects = 0
    k_inverse_rejects = 0
    k_noncanonical_projections = 0
    start_diamond_rejects = 0
    end_diamond_rejects = 0
    parent_cache = {}
    ordinary_cache = {}
    diamond_cache = {}

    for source_index, (intervals, tau) in enumerate(sources(n)):
        source_count += 1
        leaves = nonroot_leaf_indices(intervals, tau)
        if len(leaves) < 2:
            continue

        rows = {}
        parent_sources = {}
        for leaf in leaves:
            mark = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            parent_sources[leaf] = parent
            allowed = canonical_parent_targets(parent, parent_cache)
            row = {}
            for target in candidate_outputs(intervals, tau, forced_last=leaf):
                inv = exact_guarded_inverse(target, mark, n)
                if inv is None:
                    j_inverse_rejects += 1
                    continue
                parent_tree, restored, removed = inv
                projected = compress_tree(parent_tree, set(mark), n)
                if projected in allowed:
                    row[target] = {
                        "P": projected,
                        "parent_tree": parent_tree,
                        "restored": restored,
                        "removed": removed,
                    }
            rows[leaf] = row

        # Ordered pairs: J supplies the S move; K supplies the D move.
        for J in leaves:
            for K in leaves:
                if J == K:
                    continue
                ordered_pairs += 1
                if J < K:
                    unordered_pairs += 1

                rowJ, rowK = rows[J], rows[K]
                common = set(rowJ) & set(rowK)
                ordered_common += len(common)
                if J < K:
                    unordered_common += len(common)
                if not common:
                    continue

                grouped = defaultdict(list)
                lifts_by_P = defaultdict(list)
                for target, data in rowJ.items():
                    lifts_by_P[data["P"]].append(target)
                for target in common:
                    P = rowJ[target]["P"]
                    Q = rowK[target]["P"]
                    grouped[(P, Q)].append(target)

                for (P, Q), start_targets in grouped.items():
                    stable_size = len(start_targets)
                    stable_hist[stable_size] += 1
                    max_stable = max(max_stable, stable_size)

                by_P = defaultdict(list)
                for (P, Q), start_targets in grouped.items():
                    by_P[P].append((Q, sorted(start_targets)))

                for P, q_groups in by_P.items():
                    graph_key = (source_index, intervals[J], intervals[K], P)
                    graph = projection_graphs.setdefault(
                        graph_key,
                        {
                            "adj": defaultdict(set),
                            "arc_set": set(),
                            "shifted_arc_set": set(),
                            "witness_keys": set(),
                            "witness_count": 0,
                        },
                    )
                    for Q, _ in q_groups:
                        graph["adj"].setdefault(Q, set())

                    # A starting D edge is required: T must have mutually
                    # surviving J,K inverses, with common U in ordinary C(r).
                    mutually_surviving_starts = {}
                    for Q, start_targets in q_groups:
                        valid_starts = []
                        for target in start_targets:
                            diamond = mutual_diamond(
                                target, intervals, tau, J, K, n, source_index,
                                ordinary_cache, diamond_cache
                            )
                            if diamond is None:
                                start_diamond_rejects += 1
                                continue
                            valid_starts.append((target, diamond))
                        mutually_surviving_starts[Q] = valid_starts

                    if not any(mutually_surviving_starts.values()):
                        continue

                    # All J-lifts in this fixed P block are candidate S moves.
                    # Keep only those with a valid K inverse, canonical q-target,
                    # and a second mutually surviving D diamond at T'.
                    k_valid = []
                    allowed_K = canonical_parent_targets(parent_sources[K], parent_cache)
                    for target_prime in sorted(lifts_by_P[P]):
                        invK = exact_guarded_inverse(target_prime, intervals[K], n)
                        if invK is None:
                            k_inverse_rejects += 1
                            continue
                        parentK, restoredK, removedK = invK
                        Qprime = compress_tree(parentK, set(intervals[K]), n)
                        if Qprime not in allowed_K:
                            k_noncanonical_projections += 1
                            continue
                        if target_prime not in rowK:
                            raise AssertionError(
                                ("K-valid target missing from exact K-last row",
                                 n, intervals, tau, intervals[J], intervals[K],
                                 P, Qprime, target_prime)
                            )
                        if rowJ[target_prime]["P"] != P or rowK[target_prime]["P"] != Qprime:
                            raise AssertionError("projection identity mismatch")
                        diamond_prime = mutual_diamond(
                            target_prime, intervals, tau, J, K, n, source_index,
                            ordinary_cache, diamond_cache
                        )
                        if diamond_prime is None:
                            end_diamond_rejects += 1
                            continue
                        k_valid.append(
                            (target_prime, Qprime, restoredK, removedK, diamond_prime)
                        )

                    for Q, valid_starts in mutually_surviving_starts.items():
                        for target, diamond_start in valid_starts:
                            for target_prime, Qprime, restoredK, removedK, diamond_prime in k_valid:
                                witness_key = (Q, Qprime, target, target_prime)
                                graph["adj"][Q].add(Qprime)
                                graph["arc_set"].add((Q, Qprime))
                                if Q != Qprime:
                                    graph["shifted_arc_set"].add((Q, Qprime))
                                if witness_key in graph["witness_keys"]:
                                    continue
                                graph["witness_keys"].add(witness_key)
                                graph["witness_count"] += 1
                                transition_count += 1
                                if Q == Qprime:
                                    loop_count += 1
                                else:
                                    shifted_count += 1
                                transitions.append({
                                    "source_index": source_index,
                                    "intervals": [list(x) for x in intervals],
                                    "overlap_tree": [list(x) for x in tau],
                                    "J": list(intervals[J]),
                                    "K": list(intervals[K]),
                                    "P": encode_tree(P),
                                    "Q": encode_tree(Q),
                                    "Q_prime": encode_tree(Qprime),
                                    "T": encode_tree(target),
                                    "T_prime": encode_tree(target_prime),
                                    "common_grandparent_U_at_T": encode_tree(diamond_start["U"]),
                                    "common_grandparent_U_at_T_prime": encode_tree(diamond_prime["U"]),
                                    "J_restored_edge_at_T": list(diamond_start["J_restored_edge"]),
                                    "K_restored_edge_at_T": list(diamond_start["K_restored_edge"]),
                                    "J_restored_edge_at_T_prime": list(diamond_prime["J_restored_edge"]),
                                    "K_restored_edge_at_T_prime": list(diamond_prime["K_restored_edge"]),
                                    "J_removed_edges_at_T_prime": encode_tree(rowJ[target_prime]["removed"]),
                                    "K_removed_edges_at_T_prime": encode_tree(removedK),
                                })

    assert source_count == expected["sources"], (n, source_count)
    assert unordered_pairs == expected["unordered_leaf_pairs"], (n, unordered_pairs)
    assert unordered_common == expected["unordered_common_incidences"], (
        n, unordered_common
    )
    assert ordered_pairs == expected["ordered_leaf_pairs"], (n, ordered_pairs)
    assert ordered_common == expected["common_incidences"], (n, ordered_common)
    assert max_stable == 1, (n, max_stable)
    assert sum(stable_hist.values()) == ordered_common, (
        n, sum(stable_hist.values()), ordered_common
    )

    graph_summary = summarize_graphs(projection_graphs)
    payload = {
        "schema": "PF-I16-PROJECTION-SHIFTING-TRANSITIONS-v1",
        "order": n,
        "source_count": source_count,
        "unordered_eligible_leaf_pairs": unordered_pairs,
        "unordered_common_target_incidences": unordered_common,
        "ordered_eligible_leaf_pairs": ordered_pairs,
        "ordered_common_target_incidences": ordered_common,
        "fixed_projection_group_histogram": dict(sorted(stable_hist.items())),
        "maximum_fixed_projection_group_size": max_stable,
        "J_inverse_rejections": j_inverse_rejects,
        "K_inverse_rejections": k_inverse_rejects,
        "K_valid_but_noncanonical_projections": k_noncanonical_projections,
        "starting_diamond_rejections": start_diamond_rejects,
        "ending_diamond_rejections": end_diamond_rejects,
        "transition_witness_count": transition_count,
        "projection_shift_witness_count": shifted_count,
        "same_projection_loop_witness_count": loop_count,
        "graph_summary": graph_summary,
        "transitions": transitions,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["canonical_transition_sha256"] = hashlib.sha256(canonical).hexdigest()

    print(
        f"n={n}: sources={source_count}, unordered_pairs={unordered_pairs}, "
        f"common_incidences={unordered_common}, ordered_pairs={ordered_pairs}, "
        f"ordered_common={ordered_common}"
    )
    print(
        f"  fixed_(P,Q)_group_histogram={dict(sorted(stable_hist.items()))}, "
        f"max_group={max_stable}"
    )
    print(
        f"  inverse_rejects_J={j_inverse_rejects}, inverse_rejects_K={k_inverse_rejects}, "
        f"K_noncanonical={k_noncanonical_projections}, "
        f"start_D_rejects={start_diamond_rejects}, end_D_rejects={end_diamond_rejects}"
    )
    print(
        f"  transition_witnesses={transition_count}, "
        f"projection_shift_witnesses={shifted_count}, same_projection_loops={loop_count}, "
        f"unique_transition_digest={payload['canonical_transition_sha256']}"
    )
    print(
        f"  projection_graphs={graph_summary['projection_graphs']}, "
        f"graphs_with_shifts={graph_summary['graphs_with_projection_shifts']}, "
        f"nontrivial_SCCs={graph_summary['nontrivial_sccs']}, "
        f"sink_SCCs={graph_summary['sink_sccs']}, "
        f"sink_sizes={graph_summary['sink_scc_size_histogram']}, "
        f"max_SCC={graph_summary['maximum_scc_size']}"
    )
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="pf_i16_projection_shifting_transitions.json")
    args = parser.parse_args()

    reports = [census(6), census(8)]
    output = {
        "schema": "PF-I16-PROJECTION-SHIFTING-TRANSITIONS-BATCH-v1",
        "orders": reports,
        "scope_note": (
            "Exact finite source-preserving D-S-D transition census at n=6,8. "
            "Each transition has two mutually-surviving reverse-mark diamonds "
            "and an exact common ordinary-parent target. No capacity-preserving "
            "transport, PFEL, all-orders Hall, or helical phase map is claimed."
        ),
    }
    Path(args.output).write_text(json.dumps(output, sort_keys=True, indent=2) + "\n")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
