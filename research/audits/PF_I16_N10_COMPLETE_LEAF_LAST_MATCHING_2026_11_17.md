# PF-I16 n=10: complete leaf-last graph matching

Date: 2026-11-17

## Exact graph

The complete leaf-last candidate relation on ten ports was enumerated for all 31,744 sources (M,tau), using every parent-before-child insertion order and every guarded admissible overlapping edge.

The resulting bipartite graph has:
- 31,744 left sources;
- 95,864 distinct right port trees;
- 12,748,570 source-target incidences;
- source degrees from 16 to 2,677.

An exact Hopcroft-Karp computation found a matching saturating every left source:

  nu(G_10) = 31,744.

This is a finite injective assignment for the complete n=10 leaf-last relation, not merely for a restricted subgraph.

Successful CI:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43991584609

Verifier:
`research/verification/verify_pf_i16_full_leaf_last_graph_n10.py`

Workflow:
`.github/workflows/pf-i16-full-leaf-last-graph-n10.yml`

## Matching-relative expansion reduction and diagnostic correction

Fix the computed saturating matching mu:X->Y and let Y_free be the targets unmatched by every left source. For each source x define its genuinely free-target neighborhood F_x=N(x) intersect Y_free and the directed graph D on X by x->y iff x is adjacent to mu(y), x != y.

For every A subset X, exactly:

  |N(A)| - |A| = |out_D(A) \\ A| + |union_{x in A} F_x|.       (MR)

The first corrected diagnostic run reported the range 15 to 2,676 by removing only the source's own matched target from each row. That is not the free-target degree: other neighbors in that row may be matched to other sources. Consequently the apparent lower bound 15 and the claimed exact Hall slack 15 were invalid and are withdrawn.

The verifier has now been corrected to form the global set
Y_free={right[j] : mr[j]<0}
from the right-to-left matching array, then count only row neighbors belonging to Y_free. The complete n=10 saturating matching and graph counts remain valid. The true free-target degree census is pending a rerun of the full exact enumeration.

Corrected verifier:
`research/verification/verify_pf_i16_full_leaf_last_graph_n10.py`

The matching-relative identity (MR) remains valid. If the corrected census eventually shows |F_x|>=r for every source, it will imply expansion by r for every nonempty source set. No such bound is asserted until the true globally unmatched target neighborhoods are verified.

## Scope

Established:
- complete n=10 leaf-last graph construction;
- exact source and target counts and incidence count;
- a left-saturating matching for all 31,744 sources;
- the exact matching-relative Hall-slack identity (MR).

Not established:
- positive Hall expansion at n=10 from this matching;
- a uniform all-orders expansion theorem;
- the weighted one-link inequality at all orders;
- the Yang-Mills mass gap.


## Corrected true-free-target census and full SCC condensation

The corrected full enumeration completed successfully in CI:

https://github.com/syncgravity/Singular-Boundary/actions/runs/44005349911

Commit:
`7b0cac850898ae50f48f5163346de4d5c044fc3f`

The matching and graph counts are unchanged:
- 31,744 sources;
- 95,864 right target trees;
- 12,748,570 incidences;
- matching size 31,744/31,744;
- 64,120 genuinely unmatched right target trees.

The true free-target degree range is 0 to 1,980. There are 2,669 sources with zero genuinely free-target neighbors and 2,931 with at most two. Thus a pointwise lower bound on |F_x| cannot establish expansion.

The matching-relative digraph has 6,156,818 arcs and exactly ten strongly connected components. The exact component census is listed as (component, source_count, outgoing_component_count, incoming_component_count, distinct_free_target_neighbors, total_source_incidence_count, minimum_source_index):

```
(0, 1,     1, 0, 362,   621,       26408)
(1, 1,     2, 0, 324,   540,       26308)
(2, 4,     4, 0, 1290,  3295,      22164)
(3, 4,     2, 1, 1315,  3390,      24564)
(4, 4,     2, 1, 1277,  3267,      23334)
(5, 4,     1, 0, 1010,  2626,      21237)
(6, 4,     1, 0, 1008,  2517,      20909)
(7, 1,     2, 0, 205,   414,       20523)
(8, 30505, 1, 8, 62145, 12569380,  2)
(9, 1216,  0, 6, 3263,  162520,    0)
```

The condensation arcs are:
```
0->8
1->8, 1->9
2->3, 2->4, 2->8, 2->9
3->8, 3->9
4->8, 4->9
5->8
6->8
7->8, 7->9
8->9
```

There is one sink SCC, component 9, with 1,216 sources and 3,263 distinct free-target neighbors. No sink SCC has zero free-target neighbors.

By (MR), a nonempty set A has zero Hall slack only if it is out-closed in D and has no free-target neighbor. Every nonempty out-closed set contains a sink SCC of the condensation. Therefore a tight nonempty Hall set would force a sink SCC with no free-target neighbor. Since none exists, the finite n=10 graph satisfies the strict expansion statement
[
|N(A)|\ge |A|+1
\qquad(\varnothing\ne A\subseteq X_{10}).
]

This is a complete finite-order statement for the n=10 leaf-last graph. It does not provide a uniform surplus greater than one, nor an induction in n. In particular, it does not establish the weighted one-link inequality or the Yang-Mills mass gap.
