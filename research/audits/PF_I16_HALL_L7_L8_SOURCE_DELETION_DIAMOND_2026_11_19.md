# PF-I16 — source-level deletion diamonds and the all-orders combinatorial lemma

Date: 19 November 2026  
Branch: research/pf-i16-z5-incidence-lift-2026-11-18  
Verifier: research/scripts/verify_pf_i16_hall_l7_l8_deletion_diamond.py

## 1. All-orders source-level deletion-diamond lemma

Let x=(M,tau) be a Hall source with s matched intervals, and let J,K be two distinct eligible reverse marks: non-root leaves of tau. Let x_J and x_K denote the parent sources obtained by deleting the corresponding interval and order-compressing the retained ports.

**Lemma.** The two marks remain eligible in the opposite one-step parent, and the two two-step deletions agree exactly:
- deleting J and then the image of K gives the same ordered interval family and indexed tree as deleting K and then the image of J;
- both equal the direct deletion of J and K, followed by one order-compression of the remaining ports and restriction of tau to the remaining interval vertices.

**Proof.**

1. J and K are distinct matching intervals, so their endpoint pairs are disjoint.
2. The root interval is not deleted. It remains the unique retained interval whose left endpoint is the first retained port, so the root designation is unchanged.
3. Since tau is a tree and J,K are distinct leaves, they cannot be adjacent unless tau has exactly two vertices. In that two-vertex case there is only one non-root leaf, so two distinct eligible marks cannot occur. Thus J and K are nonadjacent.
4. Deleting J therefore leaves the degree of K equal to one; K remains a non-root leaf. The same argument applies with J and K interchanged.
5. Removing two disjoint endpoint pairs from a linearly ordered port set and then order-compressing is independent of the order of removal. Hence the final retained port labels agree.
6. The parent tree is the induced restriction of tau to the retained interval vertices, with the retained vertices reindexed in their inherited interval order. Restricting a graph to the complement of {J,K} is independent of the order of vertex deletion. Hence the final indexed tree agrees.
7. Strict interval overlap is invariant under order-preserving compression of retained endpoints. Thus the retained overlap graph is also the same on both paths, and the common restricted tree is a spanning tree of that parent overlap graph.

This proves the source-level diamond for every source and every pair of simultaneously eligible reverse marks. No finite-order assumption is used.

## 2. Exact order-eight regression enumeration

The canonical source enumerator was independently replayed at n=8, using perfect matchings of ordered ports, strict-interior interval overlap, every spanning tree of the full overlap graph, root at the unique interval beginning at port 1, and every non-root leaf as an eligible reverse mark.

| Quantity | Exact result |
|---|---:|
| Hall sources | 608 |
| Eligible marked projections | 1,050 |
| Distinct full-overlap graphs | 13 |
| Sources with one eligible mark | 214 |
| Sources with two eligible marks | 346 |
| Sources with three eligible marks | 48 |
| Pairs of simultaneously eligible marks | 490 |
| Deletion diamonds checked | 490 |
| Diamond failures | 0 |

The pair count is exactly 346*C(2,2) + 48*C(3,2) = 490.

For every source and every pair of distinct eligible marks i,j, both two-step paths were computed:
- x -> x_i -> x_ij
- x -> x_j -> x_ji

Each path was compared with the direct operation that deletes both marked intervals, compresses the remaining port order, and restricts/reindexes the original tree to the retained intervals. All 490 outputs agree exactly as ordered interval families and indexed trees.

This finite enumeration is an implementation-level regression check for the all-orders lemma above. It is not the proof of the lemma.

## 3. Consequence for L8

The **combinatorial source deletion diamond is now closed at all orders**. This removes source deletion order as an independent obstruction to L8.

It does **not** close the geometric marked-support diamond or L7b. For L6c/L7b, the two paths must additionally carry compatible data:
- the complete nonempty intersection diagram K_S, including triple and four-way intersections at order eight;
- relative deletion-collapse certificates;
- each retained interval's oriented boundary cycle anchored at its directed matched edge;
- the ordered footprint word and the incidence/intersection relations among all footprints on that boundary;
- coherence of these data when two paths reach the same doubly deleted parent.

The successful order-six alternative triple supplies a candidate three-interval base configuration, but its finite 30-projection verification is not itself a four-interval extension theorem. The earlier bounded one-/two-rhombus fourth-edge failure remains a bounded negative result only; the three-rhombus extension search is still outstanding and must be rerun exhaustively before drawing a geometric conclusion.

## 4. Next required calculation

Complete the order-eight four-interval extension search with the fixed alternative triple, but retain **all** admissible supports of up to three accepted rhombi rather than one lexicographically first realization. For every candidate fourth edge/support, test the full L6c intersection diagram and the multi-footprint L7b boundary word along every eligible deletion. Then verify the geometric support diagrams agree along both sides of each of the 490 source diamonds.

Do not call L7 or geometric L8 closed until that test is passed and an all-orders geometric induction hypothesis is proved. The source-level deletion-diamond lemma is now available as the combinatorial foundation of that proof.
