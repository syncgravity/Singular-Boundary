# PF-I16: exact low-cardinality Hall expansion at eight ports

Date: 2026-11-17

## 1. Exact pair and triple censuses

Let G_8=(X,Y,E) be the n=8 source-dependent leaf-last bipartite graph, with 608 child sources and 1,493 distinct target trees.

The exact pair verifier enumerated all

  C(608,2) = 184,528

source pairs. Its minimum Hall slack was 6, attained by exactly seven pairs. Every minimizing pair consists of two overlap-tree choices for the same matching and the same parent source. The verifier and run are:

- `research/verification/verify_pf_i16_pair_hall_slack.py`
- https://github.com/syncgravity/Singular-Boundary/actions/runs/43987522419

The exact triple verifier enumerated all

  C(608,3) = 37,274,656

source triples. Its minimum Hall slack was 5, attained by exactly two triples:

- source indices (69,71,73), all for matching
  ((1,4),(2,8),(3,6),(5,7)), with common parent
  (((1,3),(2,5),(4,6)), ((0,1),(1,2)));
- source indices (185,188,191), all for matching
  ((1,5),(2,8),(3,7),(4,6)), with common parent
  (((1,4),(2,6),(3,5)), ((0,2),(1,2))).

There are no triple slacks 6, 7, or 8: the next triple slack is 9. The exact triple verifier and CI run are:

- `research/verification/verify_pf_i16_triple_hall_slack.py`
- https://github.com/syncgravity/Singular-Boundary/actions/runs/43987620661

The pair census found seven minimizers; the triple census found two. In both cases the minimizing configurations are concentrated within a single matching and a single parent source, rather than spread across parent fibers.

## 2. A derived expansion bound for every small source set

For any source set A of size k>=4, every three-element subset B of A satisfies N(B) subset N(A), hence

  |N(A)| - k >= (|N(B)| - 3) - (k-3)
              = s(B) - (k-3).

Among the C(k,3) triples contained in A, at most two can be one of the two global minimum-slack triples. Therefore, for k>=4, at least one triple B is not a minimizer and has s(B)>=9. It follows that

  s(A) >= 9 - (k-3) = 12-k.

Combining this with the exact singleton, pair, and triple minima gives:

- |A|=1: s(A)>=7 (the verifier reports the minimum source degree);
- |A|=2: s(A)>=6;
- |A|=3: s(A)>=5;
- 4<=|A|<=9: s(A)>=12-|A|>=3.

Thus **every source set of cardinality at most nine has Hall slack at least three** in G_8.

This is a rigorous consequence of the exhaustive low-cardinality census. It is not an all-subsets Hall bound: for |A|>=10 the displayed estimate no longer guarantees slack three.

## 3. Consequence for three forced assignments

For any three pairwise vertex-disjoint forced edges F, the residual Hall condition is automatic for every remaining source set A with |A|<=9, since at most three target vertices are removed and s(A)>=3.

Therefore, any failure of a three-edge extension in G_8 must be witnessed by a remaining source set of size at least ten. This narrows the n=8 sampled triple-flexibility test to a large-set expansion problem.

The separate exhaustive census over all 2^22 unions of complete parent fibers found very large slack (minimum 149 at n=8). This does not settle arbitrary mixed subsets: the n=6 critical sets are small selections from parent fibers, not entire fibers. See `research/verification/verify_pf_i16_parent_fiber_hall_slack.py` and CI run https://github.com/syncgravity/Singular-Boundary/actions/runs/43987390685.

## 4. Limits

Established exactly:
- all source pairs at n=8 have slack at least 6;
- all source triples at n=8 have slack at least 5, with exactly two minimizers;
- every source subset of size at most nine has slack at least three;
- three-edge residual Hall obstructions, if any, must involve at least ten remaining sources.

Not established:
- a Hall-slack lower bound for all 608-source subsets at n=8;
- simultaneous extension of every triple at n=8;
- an all-orders expansion theorem;
- the weighted one-link inequality or Yang-Mills mass gap.
