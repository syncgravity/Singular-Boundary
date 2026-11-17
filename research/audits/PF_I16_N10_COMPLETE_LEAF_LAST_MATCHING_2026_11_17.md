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

## Matching-relative expansion: exact n=10 result

Fix the computed saturating matching mu:X->Y and let Y_free be the unmatched targets. For each source x define its free-target neighborhood F_x and the directed graph D on X by x->y iff x is adjacent to mu(y), x != y.

For every A subset X, exactly:

  |N(A)| - |A| = |out_D(A) \\ A| + |union_{x in A} F_x|.       (MR)

The corrected exact verifier computes each F_x by removing the one matched target mu(x) from the complete row N(x). It finds:
- free-target degree range: 15 to 2,676;
- exactly 35 sources attain the minimum 15;
- no source has free-target degree below 15;
- 64,120 unmatched right targets.

Consequently, for every nonempty A choose any x in A. Then
|union_{z in A} F_z| >= |F_x| >= 15,
and |out_D(A) \\ A| >= 0. By (MR),

  |N(A)| - |A| >= 15  for every nonempty A subset X.

This is sharp: a source of minimum row degree 16 has singleton slack
|N({x})|-1=15. Therefore the exact global minimum Hall slack is

  min_{empty != A subset X} (|N(A)|-|A|) = 15.

In particular the complete n=10 leaf-last relation has Hall expansion by 15, stronger than the three-unit expansion previously targeted. This conclusion requires no subset enumeration: it follows from the fixed saturating matching and the verified per-source free-neighbor lower bound.

Corrected diagnostic CI:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43997960767

The verifier now asserts min_free >= 3 and min_free == min_source - 1, and prints the exact global Hall-slack lower bound. The assertion turns the deduction into a regression-checked certificate.

## Scope

Established:
- complete n=10 leaf-last graph construction;
- exact source and target counts;
- a left-saturating matching for all 31,744 sources.

Not yet established:
Established:
- complete n=10 leaf-last graph construction;
- exact source and target counts and incidence count;
- a left-saturating matching for all 31,744 sources;
- exact Hall expansion constant 15 for every nonempty source subset at n=10.

Not established:
- a uniform all-orders expansion theorem;
- the weighted one-link inequality at all orders;
- the Yang-Mills mass gap.
