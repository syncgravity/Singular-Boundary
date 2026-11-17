# PF-I16: exact matching-relative expansion at eight ports

Date: 2026-11-17

## Result

For the n=8 source-dependent leaf-last bipartite graph:

- left sources: 608;
- right target trees in the union: 1,493;
- one fixed left-saturating matching exists;
- free right targets relative to that matching: 885;
- matching-relative digraph arcs: 17,172.

The exact low-boundary verifier tested every deleted-vertex set B of size at most two:

  1 + 608 + C(608,2) = 185,137 cases.

For each B, it computes the strongly connected components of D-B and inspects every sink component C. It computes

  q(C) = |out_D(C)| + |F(C)|,

where out_D(C) is the set of vertices outside C receiving an arc from C, and F(C) is the set of free targets adjacent to at least one source in C.

The output on n=8 was:

- no sink component with q(C)<=2;
- minimum q(C)=883;
- minimum free-target-neighbor count among examined sink components: 881;
- minimum sink-component source count: 604;
- minimum attained by 3 cases;
- slack histogram over all examined sink components: 883:3, 884:11, 885:104, 886:8,326, 887:176,693.

The minimum example had deleted vertices (1,467), a sink component of 604 sources, 2 outgoing boundary vertices, and 881 free target neighbors.

The n=6 positive control recovered a slack-2 sink component with deleted vertices (9,10), boundary count 2, no free target neighbors, and 2 sources. This is consistent with the independently established n=6 critical pair.

## Why the cut census proves all-subset expansion

Fix the verifier's left-saturating matching mu:X->Y. Let Y_free be the unmatched right vertices. Define a digraph D on X by

  x -> y  iff  x is adjacent to mu(y), with x != y.

For every A subset X, let

  B_D(A) = { y outside A : there exists x in A with x->y },
  F(A) = { t in Y_free : t is adjacent to some x in A }.

The matched targets mu(A) are |A| distinct members of N(A). Every other neighbor of A is either a matched target mu(y) with y outside A, or a free target. Therefore the exact identity is

  |N(A)| - |A| = |B_D(A)| + |F(A)|.                 (1)

Suppose, for contradiction, some nonempty A has Hall slack at most two. Put B=B_D(A). By (1), |B|<=2 and |F(A)|<=2. Since A has no outgoing arc to X\(A union B), A is out-closed in D-B.

In the condensation DAG of D-B, start from any SCC meeting A and follow outgoing edges. Out-closedness keeps this walk inside A; finiteness gives a sink SCC C contained in A. Because C is a sink SCC of D-B, all its outgoing D-neighbors lie in B. Also F(C) is a subset of F(A). Hence

  |out_D(C)| + |F(C)| <= |B| + |F(A)| <= 2.

But the exhaustive census examined every B of size at most two and every sink SCC of D-B, and found no such component. Contradiction.

Thus the finite n=8 graph satisfies

  |N(A)| >= |A| + 3 for every nonempty A subset X.

This is a complete all-subsets Hall-expansion proof for this finite graph. It does not rely on enumerating all 2^608 subsets; it reduces the search to 185,137 vertex-deletion cases and their sink SCCs.

## Reproducibility

- Python graph export and assertions:
  `research/verification/verify_pf_i16_low_boundary_cuts.py`
- C++ exact SCC/cut enumerator:
  `research/verification/pf_i16_low_boundary_cuts.cpp`
- Workflow:
  `.github/workflows/pf-i16-low-boundary-cuts.yml`
- Successful certificate run:
  https://github.com/syncgravity/Singular-Boundary/actions/runs/43990138426

The n=6 case is deliberately a positive control, not an expected pass: it must find a slack-2 obstruction. The n=8 case must prove absence of any slack-at-most-two obstruction.

## Scope

This establishes uniform Hall expansion for the specific n=8 leaf-last graph and hence a left-saturating matching with three units of global Hall surplus for every nonempty source set.

It does not establish:
- the same expansion for n=10 or general n;
- a general theorem for the family of leaf-last graphs;
- the weighted one-link inequality at all orders;
- the Yang-Mills mass gap.
