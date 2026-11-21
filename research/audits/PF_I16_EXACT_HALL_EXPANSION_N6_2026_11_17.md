# PF-I16: exact Hall expansion and three-edge extension at six ports

Date: 2026-11-17

## 1. Object and scope

Let G_6=(X,Y,E) be the finite bipartite graph used by the source-dependent leaf-last construction at six ports:

- X consists of the 22 sources (M,tau);
- Y consists of the 43 distinct port trees appearing in at least one leaf-last source neighborhood;
- x~T exactly when T is an output of the guarded leaf-last switch construction for x.

A left-saturating matching of G_6 was already certified by the exact source-assignment verifier. This audit studies the Hall expansion of this particular finite graph, not the full coordinatewise Hall graph at arbitrary order.

## 2. Exhaustive Hall-slack census

For every nonempty A subset X, compute

  s(A) = |N(A)| - |A|.

All 2^22-1 = 4,194,303 nonempty source subsets were enumerated exactly using integer bitsets for target neighborhoods. The result is:

  min_{nonempty A subset X} s(A) = 2.

There are exactly two subsets attaining this minimum:

1. A_2 = {5,7}, with |A_2|=2 and |N(A_2)|=4.
2. A_4 = {5,7,12,14}, with |A_4|=4 and |N(A_4)|=6.

The indices are the verifier's deterministic source enumeration indices. The complete neighborhoods are:

N(A_2) = {
  ((1,2),(2,3),(2,6),(3,4),(3,5)),
  ((1,2),(2,3),(2,6),(3,4),(4,5)),
  ((1,2),(2,3),(3,4),(3,5),(3,6)),
  ((1,2),(2,3),(3,4),(3,6),(4,5))
}.

N(A_4) is the same four trees together with:

  ((1,2),(2,4),(2,6),(3,4),(4,5)),
  ((1,2),(2,4),(3,4),(4,5),(4,6)).

There are no nonempty subsets with slack 0 or 1. The minimum-slack census and the complete neighborhoods above are reproduced by
`research/verification/verify_pf_i16_exact_hall_slack_census.py`.

CI:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43987155197

## 3. Exact forced-edge extension theorem for this graph

Let F be a set of pairwise vertex-disjoint source-target edges of G_6. Write X_F and Y_F for their source and target endpoints. The residual graph after forcing F has a matching saturating X\X_F if and only if

  |N(A) intersect Y_F| <= s(A)
  for every A subset X\X_F.

This is simply Hall's theorem applied to the residual graph, since its neighborhood of A is N(A)\Y_F.

The exhaustive census gives the following consequences.

### Two forced edges

If |F|<=2, then for every remaining source set A,

  |N(A) intersect Y_F| <= |Y_F| <= 2 <= s(A).

Thus **every pair of vertex-disjoint individually admissible assignments extends simultaneously** in G_6. This is an exact graph-theoretic theorem at six ports, not a sample result.

### Three forced edges

Suppose |F|=3. Every source set other than A_2 and A_4 has slack at least 3, so it automatically satisfies the residual Hall condition. The only possible obstructions are:

- if A_2 is wholly unforced, at most two of the three forced target trees may lie in N(A_2);
- if A_4 is wholly unforced, at most two of the three forced target trees may lie in N(A_4).

These two conditions are jointly necessary and sufficient for the three forced edges to extend to a left-saturating matching.

If a source in one of A_2 or A_4 is itself forced, that set is not a subset of the remaining left vertices and imposes no condition; all its proper subsets have slack at least 3.

This exactly explains the seven sampled n=6 three-edge failures: their residual Hall witnesses were A_2 or A_4, and the three forced targets exhausted three members of the corresponding critical neighborhood. The census shows these are the only possible three-edge Hall obstructions in G_6, not merely the only ones seen in the sample.

## 4. What this does and does not advance

Established exactly for G_6:

- exhaustive expansion bound |N(A)| >= |A|+2 for every nonempty source subset;
- exactly two critical source sets attain slack 2;
- every two disjoint forced assignments extend;
- a necessary-and-sufficient characterization of which triples extend;
- the sampled failures are instances of the only two possible critical Hall obstructions.

Not established:

- an analogous expansion theorem for n>=8;
- an all-orders lower bound on leaf-last Hall slack;
- an all-orders assignment or fractional transport;
- the original weighted one-link inequality;
- the Yang-Mills mass gap.

The promising structural target is now sharper: understand why the two critical n=6 sets are unions of complete parent fibers, and find an all-orders description of low-slack unions of parent fibers. Any all-orders argument must control how many output trees from each such critical neighborhood can be consumed by forced assignments.
