# PF-I16 — Chromatic resummation for the symmetric binary one-link chain

**Date:** 2026-11-16  
**Status:** exact special-case cumulant identity and exponential-times-tree bound proved  
**Scope:** one stationary symmetric two-state Markov link, one centered coordinate observable at each ordered port. This is a genuine special-case support-tree result, not the general multi-link super-row theorem.

## 1. Model and exact moments

Let \(X_1,\ldots,X_R\in\{-1,+1\}\) be a stationary symmetric two-state Markov chain at ordered times \(t_1<\cdots<t_R\), with
[
\mathbb E[X_{j+1}\mid X_j]=r_jX_j,
\qquad 0\le r_j\le1.
]
For a heat-kernel/gap model one may take \(r_j=e^{-\Delta(t_{j+1}-t_j)}\). The increments \(Z_j=X_jX_{j+1}\) are independent, with \(\mathbb E Z_j=r_j\), and independent of the uniform initial sign.

For a subset \(B=\{b_1<\cdots<b_s\}\),
[
M_B=\mathbb E\prod_{i\in B}X_i
=
\begin{cases}
0,&s\text{ odd},\\[2mm]
\displaystyle\prod_{h=1}^{s/2}\prod_{j=b_{2h-1}}^{b_{2h}-1}r_j,
&s\text{ even}.
\end{cases}
\tag{1.1}
]
Thus each even block contributes the product of interval weights for the canonical pairing of its ordered elements:
\((b_1,b_2),(b_3,b_4),\ldots\).

## 2. Reindex the cumulant by perfect matchings

Assume \(R\) is even. In the moment-cumulant formula
[
\kappa(X_1,\ldots,X_R)
=\sum_{\pi\in\Pi_R}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}M_B,
\tag{2.1}
]
only partitions with every block even contribute.

Pair consecutive elements inside each block. The union of these blockwise pairings is a perfect matching \(M\) of \([R]\). Each matching edge \(a b\) represents the interval \([a,b]\), with weight
[
w_{ab}=\prod_{j=a}^{b-1}r_j.
]
For a fixed matching \(M\), form its interval-overlap graph \(H_M\): vertices are the matching intervals, and two vertices are adjacent exactly when their intervals overlap (crossing or nesting; disjoint intervals are nonadjacent).

A partition \(\pi\) produces the matching \(M\) precisely when its matching intervals are grouped into blocks whose intervals are pairwise disjoint. Equivalently, the blocks are the independent color classes of \(H_M\). Therefore the total Möbius coefficient of a fixed matching is
[
c(H_M)=
\sum_{\substack{\rho\text{ a partition of }V(H_M)\\
\text{each class independent}}}
(-1)^{|\rho|-1}(|\rho|-1)!
=[q]\,\chi_{H_M}(q),
\tag{2.2}
]
where \(\chi_H\) is the chromatic polynomial and \([q]\) denotes its linear coefficient. Hence the exact resummation is
[
\boxed{
\kappa(X_1,\ldots,X_R)
=\sum_{M\text{ perfect matching of }[R]}
c(H_M)\prod_{ab\in M}w_{ab}.
}
\tag{2.3}
]
For odd \(R\), the cumulant is zero.

This is the signed interval-overlap resummation in a concrete Markov model. It is not the false single-copy connected-reset formula: different blocks in a moment-cumulant term are separate replicas, and their intervals may overlap.

## 3. Why only connected interval-overlap graphs survive

The graph \(H_M\) is an interval graph, hence chordal. If it is disconnected, its chromatic polynomial is divisible by \(q^2\), so \([q]\chi_{H_M}(q)=0\). Thus only matchings whose interval-overlap graph is connected survive.

Equivalently, the union of the matching intervals covers every consecutive cut \(j|j+1\). If some cut is uncovered, all intervals lie on one side or the other, so \(H_M\) is disconnected. Conversely, if all cuts are covered, the interval-overlap graph is connected.

## 4. Chromatic coefficient bounded by spanning trees

Order the intervals by nondecreasing right endpoint. This is a perfect-elimination ordering of an interval graph: the later neighbors of each interval all contain its right endpoint and hence form a clique. Let \(d_i^+\) be the number of later neighbors in this ordering. Chordal-graph coloring gives
[
\chi_{H_M}(q)=\prod_{i=1}^{n}(q-d_i^+),
\qquad n=R/2,
]
with the final factor equal to \(q\). Therefore
[
|c(H_M)|=\prod_{i=1}^{n-1}d_i^+.
\tag{4.1}
]
Choosing one later neighbor for each non-root interval gives a distinct spanning tree of \(H_M\): indices strictly increase along parent edges, so there are no cycles and every vertex reaches the final root. Consequently
[
|c(H_M)|\le \tau(H_M)\le n^{n-2}
\tag{4.2}
]
for connected \(H_M\), with the one-vertex case interpreted as \(\tau=1\).

There are \((R-1)!!\le R^{R/2}\) perfect matchings. Thus, for even \(R\ge2\),
[
\sum_M|c(H_M)|
\le (R-1)!!\,(R/2)^{R/2-2}
\le R^R
\le 4^R R^{R-2}.
\tag{4.3}
]

## 5. The weighted tree-graph inequality is the sharper target

The coefficient-only estimate in Section 4 is not, by itself, a support-tree estimate: a factor \(R^{R-2}\) cannot be discarded merely because the complete support graph has \(R^{R-2}\) spanning trees. Their temporal weights need not be comparable to the path weight.

The correct weighted quantity is
\[
\mathcal L_R(r)=
\sum_{M\text{ perfect matching}}
|c(H_M)|\prod_{ab\in M}\prod_{j=a}^{b-1}r_j.
\]
For the complete temporal graph on the ordered ports, put
\[
\mathcal T_R(r)=
\sum_{T\in\mathcal T_R}
\prod_{\{a,b\}\in T}\prod_{j=\min(a,b)}^{\max(a,b)-1}r_j.
\]
The missing combinatorial inequality suggested by the exact low-arity tests is
\[
\boxed{\mathcal L_R(r)\le C^R\mathcal T_R(r),\quad 0\le r_j\le1.}
\tag{5.1}
\]
If proved with universal \(C\), this immediately gives the desired complete temporal tree bound for this symmetric binary one-link family.

For \(R=4\), the two nonzero matching terms each have weight \(r_1r_2^2r_3\); the complete tree polynomial contains two distinct trees with exactly that weight, so \(\mathcal L_4\le\mathcal T_4\) in this case.

The verifier now checks (5.1) exactly on a deterministic collection of rational gap vectors through \(R=8\), using the Matrix–Tree determinant for \(\mathcal T_R\). These are finite tests, not a proof for arbitrary \(R\) or real gap weights.

## 6. Four-port check and the interlacing obstruction
he interlacing obstruction

For \(R=4\), the three matchings are
\[
12|34,\qquad 13|24,\qquad 14|23.
\]
The first has disjoint intervals and coefficient zero. The other two have connected interval-overlap graph and coefficient \(-1\). Hence
[
\kappa_4
=-w_{13}w_{24}-w_{14}w_{23}
=-2r_1r_2^2r_3.
\]
In particular,
[
M_{1234}=r_1r_3,
\qquad
\kappa_4=-2r_1r_2^2r_3.
]
The single-copy all-\(Q\) term in the full four-row moment is zero (for the symmetric binary chain, \(Q M_X Q=0\)); the nonzero cumulant is carried by the two overlapping/nested *replica* interval families. This explains why the naive single-copy connected-component expansion fails.

## 7. Boundary of the result

Established here:

- exact perfect-matching / interval-overlap-graph resummation for the symmetric binary coordinate chain;
- exact chromatic-polynomial interpretation of the Möbius coefficient;
- connectedness cancellation and a \(4^R R^{R-2}\) coefficient bound;
- an exact matching/chromatic resummation; the weighted tree-graph inequality (5.1) is supported by finite tests but remains unproved in general.

Not established:

- arbitrary bounded one-link functions;
- general finite-state or compact-group Markov links;
- multiple independent links with row observables that are products over link supports;
- the required general \(C_m^R\) multi-link support-localized cumulant-tree theorem.

The special case provides a concrete model for the missing signed interval-overlap resummation. The remaining weighted inequality is open; this audit does not establish a uniform temporal tree bound or close the Yang–Mills mass-gap proof.
