#!/usr/bin/env python3
"""Verify the PF-I16 all-orders port-completion injection at finite orders.

The mathematical proof is the all-orders construction in the companion
theorem record. This verifier audits the projection expansion, canonical
completion, profile preservation, and exact decoding for m <= 9.
It does not prove the quantum time-ordered connected-resolvent theorem.
"""
from collections import Counter
from itertools import product
from math import factorial
import argparse


def set_partitions(items):
    if not items:
        yield []
        return
    x = items[0]
    for p in set_partitions(items[1:]):
        yield [[x]] + [b[:] for b in p]
        for j in range(len(p)):
            q = [b[:] for b in p]
            q[j] = [x] + q[j]
            yield q


def nonzero_q_choices(block):
    r = len(block)
    if r < 2:
        return []
    out = []
    for mask in range(1 << (r - 1)):
        cuts = [j for j in range(r - 1) if not (mask >> j) & 1]
        bounds = [-1] + cuts + [r - 1]
        lengths = [bounds[j + 1] - bounds[j]
                   for j in range(len(bounds) - 1)]
        if all(n >= 2 for n in lengths):
            out.append(tuple((block[j], block[j + 1])
                             for j in range(r - 1) if (mask >> j) & 1))
    return out


def projection_terms(m):
    coeff = Counter()
    for part in set_partitions(list(range(m))):
        k = len(part)
        if any(len(block) == 1 for block in part):
            continue
        choices = [nonzero_q_choices(block) for block in part]
        if any(not c for c in choices):
            continue
        mu = (-1) ** (k - 1) * factorial(k - 1)
        for selected in product(*choices):
            edges = tuple(sorted(edge for group in selected for edge in group))
            coeff[edges] += mu
    return {edges: c for edges, c in coeff.items() if c}


def components_from_edges(edges, m):
    adj = [set() for _ in range(m)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, comps = set(), []
    for v in range(m):
        if v in seen:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        comps.append(sorted(comp))
    return comps


def block_edges(block):
    b = sorted(block)
    return [(b[i], b[i + 1]) for i in range(len(b) - 1)]


def profile(edges, m):
    return tuple(sum(a <= q < b for a, b in edges) - 1
                 for q in range(m - 1))


def interval_overlap(a, b):
    return max(min(a), min(b)) < min(max(a), max(b))


def increasing_parent_maps(blocks):
    order = sorted(range(len(blocks)), key=lambda i: max(blocks[i]))
    root = order[-1]
    options = {}
    for i in order[:-1]:
        options[i] = [
            j for j in order
            if max(blocks[j]) > max(blocks[i])
            and interval_overlap(blocks[i], blocks[j])
        ]
        if not options[i]:
            raise AssertionError("connected interval graph has a non-root sink")
    keys = list(options)
    for values in product(*(options[i] for i in keys)):
        yield dict(zip(keys, values)), root


def complete(blocks, parent, root):
    """Return the completed tree and final incoming/outgoing port pairs."""
    tree = set()
    chains = {}
    for bi, block in enumerate(blocks):
        for ei, edge in enumerate(block_edges(block)):
            chains[(bi, ei)] = [edge[0], edge[1]]
    for edge in block_edges(blocks[root]):
        tree.add(tuple(edge))

    ports = {}
    order = sorted((i for i in range(len(blocks)) if i != root),
                   key=lambda i: max(blocks[i]), reverse=True)
    for i in order:
        p = parent[i]
        c = min(v for v in blocks[i]
                if min(blocks[p]) < v < max(blocks[p]))
        pb = sorted(blocks[p])
        ei = next(j for j in range(len(pb) - 1)
                  if pb[j] < c < pb[j + 1])
        chain = chains[(p, ei)]
        pos = next(j for j in range(len(chain) - 1)
                   if chain[j] < c < chain[j + 1])
        x, y = chain[pos], chain[pos + 1]
        if (x, y) not in tree:
            raise AssertionError("maintained parent-edge chain is not in tree")

        # Transport every earlier port that is being subdivided.
        for d, (pin, pout) in list(ports.items()):
            if pin == (x, y):
                ports[d] = ((c, y), pout)
            if pout == (x, y):
                ports[d] = (pin, (x, c))

        tree.remove((x, y))
        tree.add((x, c))
        tree.add((c, y))
        chain[pos:pos + 2] = [x, c, y]
        for edge in block_edges(blocks[i]):
            tree.add(tuple(edge))
        ports[c] = ((x, c), (c, y))

    return tuple(sorted(tree)), tuple(
        (c, ports[c][0], ports[c][1]) for c in sorted(ports)
    )


def is_tree(edges, m):
    return len(edges) == m - 1 and len(components_from_edges(edges, m)) == 1


def decode(tree_edges, port_data, m):
    """Recover the forest and parent map by following port-transition chains."""
    tree = set(tree_edges)
    ports = {c: (ein, eout) for c, ein, eout in port_data}
    adj = {edge: set() for edge in tree}
    for c, (ein, eout) in ports.items():
        if ein not in tree or eout not in tree:
            raise AssertionError("port edge is absent from completed tree")
        if ein[1] != c or eout[0] != c:
            raise AssertionError("port orientation is inconsistent")
        adj[ein].add(eout)
        adj[eout].add(ein)

    seen, transition_paths = set(), []
    for edge in sorted(tree):
        if edge in seen:
            continue
        stack, component = [edge], []
        seen.add(edge)
        while stack:
            current = stack.pop()
            component.append(current)
            for nxt in adj[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        if any(len(adj[e]) > 2 for e in component):
            raise AssertionError("transition graph branches")
        degree = Counter()
        for a, b in component:
            degree[a] += 1
            degree[b] += 1
        endpoints = [v for v, d in degree.items() if d == 1]
        if len(endpoints) != 2:
            raise AssertionError("transition component is not a path")
        transition_paths.append((component, tuple(sorted(endpoints))))

    forest, connector_parent_edge = set(), {}
    for component, bypass in transition_paths:
        forest.add(bypass)
        for c, (ein, eout) in ports.items():
            if ein in component and eout in component:
                connector_parent_edge[c] = bypass

    blocks = components_from_edges(tuple(forest), m)
    edge_component = {}
    for bi, block in enumerate(blocks):
        for edge in block_edges(block):
            edge_component[tuple(edge)] = bi

    parent = {}
    for c, edge in connector_parent_edge.items():
        child = next(i for i, block in enumerate(blocks) if c in block)
        parent[child] = edge_component[edge]
    roots = [i for i, block in enumerate(blocks)
             if not any(c in block for c in ports)]
    return tuple(sorted(tuple(b) for b in blocks)), parent, roots


def audit(m):
    terms = projection_terms(m)
    seen_codes, pair_count = set(), 0
    for forest_edges, alpha in terms.items():
        blocks = components_from_edges(forest_edges, m)
        parent_maps = list(increasing_parent_maps(blocks))
        if len(parent_maps) != abs(alpha):
            raise AssertionError(
                f"coefficient/parent-tree mismatch at m={m}: "
                f"{len(parent_maps)} != {abs(alpha)}"
            )
        for parent, root in parent_maps:
            tree, ports = complete(blocks, parent, root)
            if not is_tree(tree, m):
                raise AssertionError("completion did not produce a spanning tree")
            if profile(tree, m) != profile(forest_edges, m):
                raise AssertionError("temporal cut profile changed")
            code = (tree, ports)
            if code in seen_codes:
                raise AssertionError("port-completion encoding is not injective")
            seen_codes.add(code)

            decoded_blocks, decoded_parent, roots = decode(tree, ports, m)
            original_blocks = tuple(sorted(tuple(b) for b in blocks))
            if decoded_blocks != original_blocks:
                raise AssertionError("decoder did not recover the original forest")
            if len(roots) != 1 or decoded_blocks[roots[0]] != tuple(blocks[root]):
                raise AssertionError("decoder did not recover the root component")

            def normalize(blks, par):
                return {tuple(sorted(blks[i])): tuple(sorted(blks[j]))
                        for i, j in par.items()}

            if normalize(blocks, parent) != normalize(
                    [list(b) for b in decoded_blocks], decoded_parent):
                raise AssertionError("decoder did not recover the parent tree")
            pair_count += 1

    return {
        "m": m,
        "projection_forests": len(terms),
        "absolute_coefficient_mass": sum(abs(a) for a in terms.values()),
        "increasing_rooted_pairs": pair_count,
        "unique_tree_port_codes": len(seen_codes),
        "injection_collisions": 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=9)
    args = parser.parse_args()
    if not 2 <= args.max_m <= 9:
        raise SystemExit("--max-m must be between 2 and 9")
    for m in range(2, args.max_m + 1):
        print(audit(m))
    print("PASS: port-completion decoder is injective on every audited order.")
    print("SCOPE: finite combinatorial audit only; the all-orders proof is in the theorem record.")
    print("OPEN: quantum time-ordered connected-resolvent/tree inequality.")


if __name__ == "__main__":
    main()
