# PF-I16 global alternating-path and cycle rerouting diagnostic

Date: 2026-11-16

## Motivation

The source-constrained parent-exchange graph is disconnected at eight ports:
5,156 collision pairs have projections in different components. A reroute
must therefore be allowed to pass through the full child-source-to-final-tree
relation, including multiple parent fibers.

## Exact test

For each child source, enumerate its complete leaf-last output neighborhood
and compute a deterministic maximum bipartite matching M. The matching must
saturate every child source.

For every final tree T shared by multiple child sources, test every
challenger x other than the current matched owner of T. Search from T along
alternating transitions

```
T = T_0 -> y_0 -> T_1 -> y_1 -> ... -> T_r.
```

For each i<r, T_i is matched to y_i and y_i--T_{i+1} is an unmatched
candidate edge. The challenger x is forbidden from appearing among the
intermediate y_i. Accept either of two endpoints:

1. **Free-path:** T_r is unmatched. Flip the path, shifting each y_i to
   T_{i+1}, then assign x to T_0.
2. **Alternating cycle:** T_r is the tree currently matched to x. Flip the
   path and assign x to T_0; the final shift assigns y_{r-1} to x's former
   tree, closing the cycle.

If T itself is unmatched, x can take it directly. The verifier asserts the
matched-owner, unmatched-edge, endpoint, and challenger-exclusion conditions
for every returned path.

Each successful case produces a valid left-saturating matching containing
the particular challenger edge x--T. This is a single-edge flexibility
statement; different reroutes need not be compatible simultaneously.

## Exact results

Successful GitHub Actions run: 43982703932
Verifier commit: 8f0cfb1a5ef0dba430e2681d44133b2dab3eee51

| Ports | Child sources | Target trees | Parent fibers | Free targets | Collision targets | Challenger reroutes | Failures | Max alternating steps | Max parent fibers on path |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | 1 | 1 | 2 | 2/2 | 0 | 1 | 1 |
| 6 | 22 | 43 | 2 | 21 | 39 | 173/173 | 0 | 2 | 2 |
| 8 | 608 | 1,493 | 22 | 885 | 1,480 | 29,985/29,985 | 0 | 3 | 3 |

At eight ports, there were 495,974 pairwise source-collision pairs across
shared target trees. The stricter challenger test examined 29,985 distinct
target/challenger reassignment cases, all successful.

Reroute-kind counts:
- n=4: 1 alternating cycle, 1 free-path.
- n=6: 20 alternating cycles, 65 direct free-target moves, 88 free-paths.
- n=8: 1,106 alternating cycles, 12,813 direct free-target moves,
  16,066 free-paths.

At eight ports, the alternating-step histogram was:
- 0 steps: 12,813 direct moves to an already free target
- 1 step: 14,333
- 2 steps: 2,724
- 3 steps: 115

The maximum path involved sources from three parent fibers, out of 22 total
parent fibers.

## Finite alternating reroute lemma

Let M be a matching saturating the left vertex set X in a bipartite graph
(X,Y,E). Suppose x is a left vertex, T is a right neighbor of x, and T is
matched to y_0 != x. Let

```
T_0=T, y_0, T_1, y_1, ..., T_r
```

be an alternating sequence: T_i is matched to y_i for i<r, and
y_i--T_{i+1} is an unmatched edge. Assume x is not among y_0,...,y_{r-1}.
If T_r is free, or if T_r is the tree matched to x, then switching along
the sequence and assigning x to T_0 gives another matching saturating X.
The first endpoint is an augmenting path; the second closes an alternating
cycle through x--T_0.

The verifier establishes one of these two mechanisms for every tested
challenger edge at n=4,6,8.

## Correction to the initial path-only test

A first strengthened test required a path to a free right vertex while
forbidding the challenger as an intermediate source. It failed for one
four-port collision. That was not a genuine obstruction: the two sources
could exchange their assigned trees by a length-one alternating cycle.
The final verifier therefore checks both free-path and alternating-cycle
endpoints, while retaining challenger exclusion from the interior.

## What this does and does not establish

At the tested orders, every child-source-to-shared-tree edge can individually
be included in some left-saturating matching. This is stronger than the
existence of one matching, and it uses cross-fiber alternating rerouting.

It remains a finite, matching-dependent flexibility result. It does not
supply a simultaneous reassignment of an arbitrary collection of edges,
an all-orders bound on alternating path length, a uniform fractional
transport, the all-orders Hall inequality, or the weighted one-link
inequality. The original Hall problem and Yang--Mills mass-gap target remain
open.
