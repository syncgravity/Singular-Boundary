# PF-I16 global alternating-path rerouting diagnostic

Date: 2026-11-16

## Motivation

The source-constrained parent-exchange graph is disconnected at eight ports:
5,156 collision pairs have projections in different components. A reroute
must therefore be allowed to pass through multiple parent fibers and use
the full child-source-to-final-tree relation.

## Exact test

For each child source, enumerate its complete leaf-last output neighborhood
and compute a deterministic maximum bipartite matching. The matching must
saturate every child source.

For every final tree T shared by multiple child sources, test every
challenger x other than the current matched owner of T. If T is occupied by
y, search for an alternating path

```
T = T_0 -> y_0 -> T_1 -> y_1 -> ... -> T_r (free),
```

where each T_i (i < r) is matched to y_i, each y_i--T_{i+1} edge is
unmatched, and the challenger x is forbidden from appearing among the
intermediate y_i. This exclusion is essential: x is being reassigned to T
and cannot simultaneously be shifted along the path.

Flipping the path assigns y_i to T_{i+1}; then assign x to T_0. The
challenger's former matched tree becomes free. Thus each successful path
gives a valid left-saturating matching in which that particular collision
edge x--T is selected. If T is already unmatched, x can take it directly.

The verifier checks every child-to-parent projection belongs to the exact
guarded output neighborhood of its parent source. It reports collision
counts, challenger reroutes, shortest path lengths, and the number of parent
fibers represented along each path.

## Exact results

Successful GitHub Actions run: 43982198609
Successful run commit: 6d2229f3634b5def7f6f8798e72f10cc7205449b

| Ports | Child sources | Target trees | Parent fibers | Free targets | Collision targets | Challenger reroutes | Failures | Max alternating steps | Max parent fibers on path |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | 1 | 1 | 2 | 2/2 | 0 | 2 | 1 |
| 6 | 22 | 43 | 2 | 21 | 39 | 173/173 | 0 | 2 | 2 |
| 8 | 608 | 1,493 | 22 | 885 | 1,480 | 29,985/29,985 | 0 | 3 | 2 |

At eight ports, the test considered 495,974 pairwise source collisions
across shared target trees; the more stringent challenger test covered
29,985 distinct target/challenger reassignment cases. All passed.

The alternating-path length histogram at eight ports was:
- 0 steps (contested target already free): 12,813
- 1 step: 13,770
- 2 steps: 3,245
- 3 steps: 157

The maximum path visited sources from two parent fibers, despite there
being 22 parent fibers in total.

## The finite rerouting lemma

Let M be a matching saturating the left vertex set X in a bipartite graph
(X,Y,E). Let T_0 be a right vertex matched to y_0, and let x in X be a
different neighbor of T_0. Suppose there is an alternating path
T_0,y_0,T_1,y_1,...,T_r with T_r unmatched, and x is not among the y_i.
Flipping the path and assigning x to T_0 produces another matching
saturating X. This is the exact combinatorial operation tested above.

The verifier establishes this condition for every tested challenger edge
under the selected deterministic matching at n=4,6,8.

## What this does and does not establish

This is stronger than merely finding one matching: every tested
source-to-shared-target collision edge can individually be made part of a
left-saturating matching by an alternating reroute that avoids the
challenger source.

It is still a finite, matching-dependent flexibility statement. The
rerouting paths for different collision edges may overlap and compete, and
the test does not give a simultaneous reassignment theorem, a uniform
fractional transport, an all-orders Hall inequality, or the weighted
one-link inequality. The original Hall problem and Yang--Mills mass-gap
target remain open.
