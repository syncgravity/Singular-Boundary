# PF-I16 — source-level deletion diamonds at order eight

Date: 19 November 2026  
Branch: `research/pf-i16-z5-incidence-lift-2026-11-18`  
Verifier: `research/scripts/verify_pf_i16_hall_l7_l8_deletion_diamond.py`

## Result

The canonical source enumerator was independently replayed at (n=8), using the existing conventions: perfect matchings of ordered ports, strict-interior interval overlap, every spanning tree of the full overlap graph, root at the unique interval beginning at port 1, and every non-root leaf as an eligible reverse mark.

| Quantity | Exact result |
|---|---:|
| Hall sources | 608 |
| Eligible marked projections | 1,050 |
| Distinct full-overlap graphs | 13 |
| Sources with one eligible mark | 214 |
| Sources with two eligible marks | 346 |
| Sources with three eligible marks | 48 |
| Pairs of simultaneously eligible marks | 490 |
| Deletion diamonds verified | 490 |
| Diamond failures | 0 |

The pair count is (346inom{2}{2}+48inom{3}{2}=490).

For every source and every pair of distinct eligible marks (i,j), both two-step paths were computed:
[
x\xrightarrow{i}x_i\xrightarrow{j}x_{ij},
\qquad
x\xrightarrow{j}x_j\xrightarrow{i}x_{ji}.
]
Each path was compared with the direct operation that deletes both marked intervals, compresses the remaining port order, and restricts/reindexes the original tree to the retained intervals. All three outputs agree exactly as ordered interval families and indexed trees.

This verifies the **source combinatorial deletion-diamond property at (n=8)**. It is stronger than merely observing that the two paths have isomorphic unlabelled overlap graphs: the ordered compressed interval records and retained tree edges agree.

## Why the source diamond is valid

The two marks are distinct non-root leaves of the same selected tree. Their endpoint pairs are disjoint because the matching is a partition of the ports. Deleting either leaf leaves the other as a leaf of the restricted tree. The retained port order after deleting both endpoint pairs is independent of deletion order. The induced tree on the remaining interval labels is likewise independent of the order of vertex deletion. Thus the equality is expected structurally; the finite verifier checks the repository's precise indexing and parent conventions.

## Consequence for L8

This closes only the combinatorial part of the local-confluence diagram. It does **not** yet close the geometric marked-support diamond.

For L6c/L7b, the two paths must additionally carry compatible data:
- the complete nonempty intersection diagram (K_S), including triple and four-way intersections at order eight;
- relative deletion-collapse certificates;
- each retained interval's oriented boundary cycle anchored at its directed matched edge;
- the ordered footprint word and the incidence/intersection relations among all footprints on that boundary;
- coherence of these data when two paths reach the same doubly deleted parent.

The successful order-six alternative triple supplies a candidate three-interval base configuration, but its finite 30-projection verification is not itself a four-interval extension theorem. The earlier bounded one-/two-rhombus fourth-edge failure remains a bounded negative result only; the three-rhombus extension search is still outstanding and must be rerun exhaustively before drawing a geometric conclusion.

## Next required calculation

Complete the order-eight four-interval extension search with the fixed alternative triple, but retain **all** admissible supports of up to three accepted rhombi rather than one lexicographically first realization. For every candidate fourth edge/support, test the full L6c intersection diagram and the multi-footprint L7b boundary word along every eligible deletion, then test both sides of every one of the 490 source diamonds.

Do not call L7 or L8 closed until that geometric diamond test is passed and an all-orders induction hypothesis is proved. The source-level diamond result is a verified lemma that can be used as the combinatorial foundation of that proof.
