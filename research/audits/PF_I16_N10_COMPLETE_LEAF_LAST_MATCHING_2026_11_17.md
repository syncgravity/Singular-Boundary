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
