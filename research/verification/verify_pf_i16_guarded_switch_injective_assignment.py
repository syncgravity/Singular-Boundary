#!/usr/bin/env python3
"""Exact injective source-to-output assignment for the guarded switch relation.

A matching saturating every source is a stronger certificate than a fractional
transport: assign each source's full unit mass to its matched distinct output.
The output is admissible by construction, so its cut load is <= the source
matching load. Failure returns an alternating-reachability Hall witness.
"""
from verify_pf_i16_local_switch_fractional_transport import (
    candidate_outputs, matchings, overlap_edges, spanning_trees,
)


def hopcroft_karp(adjacency):
    """Return left/right mate arrays and cardinality for a bipartite graph."""
    n_left = len(adjacency)
    right_ids = {}
    adj = []
    for row in adjacency:
        mapped = []
        for target in row:
            if target not in right_ids:
                right_ids[target] = len(right_ids)
            mapped.append(right_ids[target])
        adj.append(mapped)
    n_right = len(right_ids)
    pair_l = [-1] * n_left
    pair_r = [-1] * n_right
    dist = [0] * n_left
    inf = n_left + n_right + 1

    from collections import deque

    def bfs():
        q = deque()
        found = inf
        for u in range(n_left):
            if pair_l[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf
        while q:
            u = q.popleft()
            if dist[u] >= found:
                continue
            for v in adj[u]:
                mate = pair_r[v]
                if mate == -1:
                    found = dist[u] + 1
                elif dist[mate] == inf:
                    dist[mate] = dist[u] + 1
                    q.append(mate)
        return found != inf

    def dfs(u):
        for v in adj[u]:
            mate = pair_r[v]
            if mate == -1 or (dist[mate] == dist[u] + 1 and dfs(mate)):
                pair_l[u] = v
                pair_r[v] = u
                return True
        dist[u] = inf
        return False

    cardinality = 0
    while bfs():
        for u in range(n_left):
            if pair_l[u] == -1 and dfs(u):
                cardinality += 1

    return pair_l, pair_r, cardinality, adj, right_ids


def hall_witness(adj, pair_l, pair_r):
    """Alternating-reachable S and N(S) from unmatched left vertices."""
    from collections import deque
    seen_l = {u for u, v in enumerate(pair_l) if v == -1}
    seen_r = set()
    q = deque(seen_l)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if pair_l[u] == v or v in seen_r:
                continue
            seen_r.add(v)
            mate = pair_r[v]
            if mate != -1 and mate not in seen_l:
                seen_l.add(mate)
                q.append(mate)
    return sorted(seen_l), sorted(seen_r)


def run(n, expected_sources):
    rows = []
    source_labels = []
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = candidate_outputs(intervals, tau)
            rows.append(outputs)
            source_labels.append((intervals, tau))

    assert len(rows) == expected_sources, (n, len(rows))
    pair_l, pair_r, size, adj, right_ids = hopcroft_karp(rows)
    print(
        f"n={n}: sources={len(rows)}, target_union={len(right_ids)}, "
        f"maximum_matching={size}, saturated={size == len(rows)}"
    )
    if size == len(rows):
        assignment = [
            (i, list(right_ids.keys())[pair_l[i]])
            for i in range(len(rows))
        ]
        assert len({t for _, t in assignment}) == len(rows)
        print("  CERTIFICATE: injective assignment saturates every source.")
        print(f"  first_assignments={assignment[:min(5, len(assignment))]}")
    else:
        S, NS = hall_witness(adj, pair_l, pair_r)
        print(
            f"  HALL_DEFICIT: |S|={len(S)}, |N(S)|={len(NS)}, "
            f"deficit={len(S)-len(NS)}"
        )
        print(f"  witness_source_indices={S}")
        print(f"  witness_source_labels={[source_labels[i] for i in S]}")
    return size == len(rows)


def main():
    results = [
        run(4, 2),
        run(6, 22),
        run(8, 608),
    ]
    if not all(results):
        raise SystemExit("Guarded relation does not admit an injective assignment at every tested order.")
    print("All tested guarded relations admit source-saturating injective assignments.")


if __name__ == "__main__":
    main()
