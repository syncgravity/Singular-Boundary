# PF-I16 n=10: fixed-witness subgraph obstruction

Date: 2026-11-17

## Exact source census

There are exactly 31,744 sources (M,tau) on ten ports, supported by 706 perfect matchings. The overlap-tree counts per matching range from 1 to 125. CI: https://github.com/syncgravity/Singular-Boundary/actions/runs/43990555456

## Canonical one-witness subgraph

A first compact subrelation fixed one canonical DFS parent-before-child insertion order for each source and, at every insertion, selected one connected-tree witness edge and retained all guarded local patterns on that edge.

It generated:
- 31,744 sources;
- 20,287 target trees;
- 804,980 source-target incidences;
- source degrees 16 through 81;
- maximum matching size 15,617.

Because the target union has only 20,287 vertices, this subrelation cannot saturate 31,744 sources. The maximum matching output confirms this; it is not a failure of the full leaf-last relation.

## Four traversal orders

The next variant used up to four parent-before-child orders (DFS/BFS, ascending/descending sibling order), still selecting one witness edge per insertion. It generated:
- 31,744 sources;
- 20,854 target trees;
- 1,095,014 incidences;
- source degrees 16 through 153;
- maximum matching size 16,212;
- a Hall witness consisting of the full source set, with deficiency 10,890.

Thus this modest deterministic enlargement still does not provide enough target diversity. The outputs of the different traversal orders overlap heavily.

Verifier:
`research/verification/verify_pf_i16_four_order_subgraph_n10.py`

CI:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43991202967

## Interpretation and next test

This is a negative result for the *single-witness-edge subrelation*, not for the complete leaf-last graph. It shows that simply varying the insertion order while retaining only one selected switch edge per state does not generate enough distinct right targets.

The next diagnostic samples the complete leaf-last neighborhood generator (all parent-before-child orders and all admissible overlapping edges) at a spread of n=10 sources. Its purpose is to estimate whether the full relation has sufficient target diversity and what computation is required for an exact matching/cut certificate.

No n=10 Hall expansion conclusion follows from these restricted-subgraph failures.
