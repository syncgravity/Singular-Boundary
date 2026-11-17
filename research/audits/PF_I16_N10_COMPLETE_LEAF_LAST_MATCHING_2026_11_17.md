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

## Matching-relative expansion reduction

Fix the computed saturating matching mu:X->Y and let Y_free be the unmatched targets. For each source x define its free-target neighborhood F_x and the directed graph D on X by x->y iff x is adjacent to mu(y), x != y.

For every A subset X, exactly:

  |N(A)| - |A| = |out_D(A) \ A| + |union_{x in A} F_x|.

Thus the desired three-unit expansion follows immediately if every source has at least three free-target neighbors. Otherwise only subsets of the low-free-degree sources need further attention: any A containing a source with at least three free neighbors already has slack at least three.

The verifier now reports the free-target degree histogram under the fixed matching. This is the next diagnostic; the earlier matching result alone does not prove positive expansion.

## Scope

Established:
- complete n=10 leaf-last graph construction;
- exact source and target counts;
- a left-saturating matching for all 31,744 sources.

Not yet established:
- Hall expansion by three for all source subsets at n=10;
- a uniform all-orders expansion theorem;
- the weighted one-link inequality at all orders;
- the Yang-Mills mass gap.
