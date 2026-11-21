# PF-I16: Restricted exchange and Hall-slack condition

Date: 2026-11-17

## 1. Three-edge obstruction data

The simultaneous three-edge verifier tests a set F of three individually flexible source-to-tree assignments, with distinct sources and distinct targets. It deletes the three forced sources and targets and checks whether the residual graph has a left-saturating matching.

The original deterministic-spread n=6 run tested 3,239 triples and found 7 failures. The Hall witnesses were:

- Five failures had a deficient two-source set with 2 sources and only 1 residual neighbor.
- Two failures had a deficient four-source set with 4 sources and only 3 residual neighbors.

The two-source witness was always source indices {5,7}; the four-source witness was {5,7,12,14}. These are indices in the deterministic source enumeration used by the verifier, not invariant mathematical labels. The three-edge forced assignments differed, but repeatedly exhausted the neighborhood of these same small source sets.

At n=8, 4,050 deterministic-spread triples passed; the full triple universe is approximately 4.5 trillion, so this is not exhaustive.

Initial run: https://github.com/syncgravity/Singular-Boundary/actions/runs/43984699820

## 2. Exact restricted-exchange criterion: residual Hall slack

Let G=(X,Y,E) be the child-source / child-tree bipartite graph. Let F be a set of pairwise disjoint forced assignments, and write X_F and Y_F for their source and target endpoints.

For every subset A of remaining sources X\\X_F, define its original neighborhood N(A) and Hall slack
  s(A) = |N(A)| - |A|.

The residual graph after forcing F has a left-saturating matching if and only if
  |N(A) \\ Y_F| >= |A|
for every A subset X\\X_F.

Equivalently, the forced targets must obey the *slack budget*
  |N(A) intersect Y_F| <= s(A)
for every remaining source subset A.

This is an exact necessary-and-sufficient restricted exchange theorem, not merely a sufficient condition. It identifies the precise obstruction: a forced exchange set is inadmissible when it consumes more target vertices from some remaining source neighborhood than that neighborhood's Hall surplus can absorb.

For the observed failures, the residual witnesses show a deficit of exactly one. The next structural problem is to identify a manageable family of source subsets A (ideally small, geometrically defined sets tied to parent fibers) whose slack budgets imply the inequality for all A.

## 3. What is and is not established

Established:
- All tested admissible two-edge requirements at n=4 and n=6 extend simultaneously; n=8 tested sample also passed.
- The sampled n=6 three-edge failures are certified by explicit residual Hall witnesses.
- Residual Hall slack gives an exact characterization for any finite forced assignment set F.

Not established:
- That the seven sampled failures are the only n=6 failures.
- That every three-edge set satisfying a proposed simpler local restriction extends.
- Any all-orders lower bound on Hall slack or residual expansion.
- The original weighted one-link inequality or Yang-Mills mass gap.

## 4. Current verifier

The verifier now prints each deficient source set and its residual neighbors, together with the corresponding child matching, overlap tree, canonical leaf, and parent source metadata:
`research/verification/verify_pf_i16_simultaneous_three_edge_flexibility.py`.

The diagnostic rerun after adding this metadata is:
https://github.com/syncgravity/Singular-Boundary/actions/runs/43986136845
