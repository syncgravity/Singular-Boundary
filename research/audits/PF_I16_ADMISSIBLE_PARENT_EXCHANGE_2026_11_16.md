# PF-I16 admissible parent-exchange connectivity test

Date: 2026-11-16

## Question tested

For a fixed parent source p, let C(p) be its exact guarded-switch output set.
Form the graph with vertex set C(p), joining two parent trees when their
edge sets have symmetric difference of size 2 (one graphic basis exchange).

For every child target T shared by multiple child sources in the same parent
fiber, each child has a unique leaf-last inverse projection in C(p). The
test asks whether all such projections lie in one connected component of
this admissible parent-exchange graph.

This is a finite test of the source-constrained local exchange proposal.
It is not a test of the full coordinatewise Hall condition.

## Exact results

GitHub Actions run: 43980414697
Commit: ff2d6c0b7128f9ca112675afa7143592a2982a26

| Ports n | Parent fibers | Shared child targets | Projection-collision pairs | Disconnected pairs |
|---:|---:|---:|---:|---:|
| 4 | 1 | 2 | 2 | 0 |
| 6 | 2 | 58 | 223 | 0 |
| 8 | 22 | 7,658 | 41,848 | 5,156 |

Maximum shortest admissible exchange distance among connected pairs:
- n=4: 0
- n=6: 2
- n=8: 7

The n=8 test fails: 5,156 projection-collision pairs lie in different
connected components of the relevant parent-source output graph.

## First exact disconnection witness

Parent source:
- matching intervals: ((1,4), (2,5), (3,6))
- overlap tree: ((0,1), (1,2))

Shared child target:
((1,2), (2,3), (2,5), (3,4), (4,6), (6,7), (7,8))

Its two parent projections are:
- P = ((1,2), (2,3), (2,5), (3,4), (4,6))
- Q = ((1,2), (2,3), (2,4), (3,5), (5,6))

Both are valid members of C(p), but no path of single-edge exchanges
between them stays inside C(p).

## Consequence

The proposed source-constrained local parent-exchange lemma is false in
this form. In particular, the unrestricted graphic-matroid exchange path
cannot generally be made admissible by requiring every intermediate tree
to remain in the same parent source's output neighborhood.

This does not disprove:
- the finite global child-to-tree matchings at n=4,6,8;
- the full coordinatewise down-set Hall condition;
- the weighted one-link inequality;
- the Yang-Mills mass-gap target.

The induction must therefore use a genuinely global alternating-path or
multi-fiber rerouting mechanism, rather than insisting that each collision
be resolved inside one parent neighborhood.
