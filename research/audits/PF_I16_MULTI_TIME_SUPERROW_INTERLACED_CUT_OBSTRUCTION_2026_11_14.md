# PF-I16 — Multi-time super-row mixing: interlaced-time obstruction and corrected target

**Date:** 2026-11-14  
**Status:** A sharp coefficient-one pairwise-distance lemma is REFUTED by an exact finite-state example. An exponential-in-number-of-time-cuts bound remains OPEN.  
**Scope:** one stationary two-state Markov link path; arbitrary bounded functions of finite observation sets. No P0–P5 gate is promoted.

## 1. Candidate lemma tested

A tempting extension of the one-time link contraction is the following: if
\[
F=F((X_s)_{s\in S}),\qquad G=G((X_t)_{t\in T}),
\]
and
\[
d(S,T)=\min_{s\in S,t\in T}|s-t|,
\]
then perhaps
\[
|\operatorname{Cov}(F,G)|
\le e^{-\Delta_0d(S,T)}\|F\|_\infty\|G\|_\infty.
\tag{1.1}
\]
This is true when the two observation sets lie on opposite sides of a single temporal cut, by the Markov property and the L2 gap. It is not true for interlaced observation sets.

## 2. Exact counterexample

Let \(X_n\in\{-1,+1\}\) be the stationary two-state Markov chain with uniform stationary law and transition
\[
\mathbb P(X_{n+1}=y\mid X_n=x)=\frac{1+qxy}{2},
\qquad q=\frac12.
\tag{2.1}
\]
Its mean-zero L2 contraction over a gap of d steps is exactly \(q^d=e^{-\Delta_0d}\), where \(\Delta_0=\log2\).

Take interlaced observation sets
\[
S=\{0,2,4\},\qquad T=\{1,3\},
\]
so \(d(S,T)=1\). Define sign-valued functions by the following lookup tables, with binary index
\(b=x_0+2x_2+4x_4\) for F and \(c=x_1+2x_3\) for G:
\[
(f_0,\ldots,f_7)=(-1,-1,-1,+1,-1,-1,+1,+1),
\]
\[
(g_0,\ldots,g_3)=(-1,-1,-1,+1).
\]
Then exact path enumeration gives
\[
\mathbb EF=-\frac9{64},\qquad
\mathbb EG=-\frac38,\qquad
\mathbb E[FG]=\frac{73}{128},
\]
and therefore
\[
\boxed{
\operatorname{Cov}(F,G)=\frac{265}{512}
>\frac12
=q^{d(S,T)}\|F\|_\infty\|G\|_\infty.
}
\tag{2.2}
\]
Thus the coefficient-one estimate (1.1) fails, even for a reversible finite-state chain with an exact spectral gap.

The failure is caused by multiple temporal cuts between the two interlaced observation sets. A single nearest-pair gap does not account for all the boundary channels through which the two path functionals can correlate.

## 3. Corrected multi-cut target

For finite time sets S,T, let \(N(S,T)\) be the number of connected components of the bipartite crossing graph obtained by placing the ordered union \(S\cup T\) on the time line and joining consecutive observations of opposite colors. Let
\[
d_j(S,T)
\]
be the temporal length of the j-th such crossing interval. A useful sufficient estimate would be
\[
|\operatorname{Cov}(F,G)|
\le C^{N(S,T)}
\|F\|_\infty\|G\|_\infty
\exp\!\left[-\Delta_0\min_j d_j(S,T)\right],
\tag{3.1}
\]
or, more usefully for tree extraction, a sum over a controlled family of crossing cuts with the product of their gap weights.

The local PF-I16 incidence bounds make the number of observation times in a conditional super-row at most the number of incident original faces, which is uniformly bounded (six for a four-dimensional link). Therefore an exponential-in-cut-count loss may still be absorbed into an exponential-in-order constant. But (3.1) is only a proposed target; it is not established here.

For cumulants of three or more super-rows, the needed statement is stronger: a multi-cut projection/cumulant inequality whose bonds can be assigned to original row pairs sharing the relevant link, and whose total cut multiplicity is bounded exponentially in the number of original row-link incidences.

## 4. Consequence for the hyperedge proof

The exact conditional-cumulant partition identity remains valid. The pair-incidence deletion–contraction theorem remains valid under its stated hypothesis. What fails is the naive attempt to treat a multi-time conditional super-row as if it were a one-time insertion and attach one contraction factor using only the minimum pairwise time separation.

A correct continuation must retain the full ordered cut profile of each multi-time super-row. The relevant combinatorial object is therefore a temporal cut multigraph/hypergraph, not just the graph of super-row supports. One must then prove a controlled map from its cut structure to a spanning tree on original rows.

## 5. Disposition

- One-time single-link L2 contraction: **ESTABLISHED**.
- Two path functionals separated by one temporal cut: **ESTABLISHED** with coefficient one.
- Coefficient-one covariance bound based only on minimum distance of arbitrary interlaced time sets: **REFUTED** by (2.2).
- Exponential-in-cut-count covariance bound: **OPEN**.
- Multi-time super-row cumulant tree with original-row support bonds: **OPEN**.
- Full PF-I16 face/pair support-temporal tree: **OPEN**.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
