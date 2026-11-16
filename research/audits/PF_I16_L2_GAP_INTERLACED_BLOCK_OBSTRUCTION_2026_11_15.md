# PF-I16 — L2-gap obstruction for interlaced arbitrary block observables

**Date:** 2026-11-15  
**Status:** rigorous counterexample to the L2-gap-only formulation  
**Scope:** already fails at cumulant order two; does not apply to uniformly positive compact-group heat-kernel bridges.

## 1. Claim

There is no universal constant C for which every stationary Markov chain satisfying
\[
\|P-\Pi\|_{L^2_0(\pi)\to L^2_0(\pi)}\le\theta
\]
obeys, for arbitrary bounded observables of disjoint interlaced port sets,
\[
|\operatorname{Cov}(G_1,G_2)|
\le C^2\|G_1\|_\infty\|G_2\|_\infty
\sum_{s\in S_1,t\in S_2}\theta^{|s-t|}.
\tag{1}
\]
The counterexample has S_1={0,2}, S_2={1}, so their temporal hulls overlap.

## 2. Ramanujan graph walk

Take a non-bipartite LPS Ramanujan graph X of degree d=p+1, with girth at least five. Its simple random walk P is stationary and reversible for uniform π. Ramanujan gives
\[
\|P-\Pi\|_{L^2_0(\pi)\to L^2_0(\pi)}
\le \theta_p:=\frac{2\sqrt p}{p+1}.
\tag{2}
\]
The LPS construction permits p,q distinct primes, p≡q≡1 (mod 4), (p/q)=1, and gives girth
\[
g(X)\ge 2\log_p q.
\]
Choose q>p^2, so g(X)>4. The construction is non-bipartite under the stated quadratic-residue condition.

**Reference for the graph family:** Lubotzky, Phillips and Sarnak, “Ramanujan graphs,” *Combinatorica* 8 (1988), 261–277, [DOI 10.1007/BF02126799](https://doi.org/10.1007/BF02126799). The non-bipartite LPS case and its high-girth bound are summarized in [this construction note](https://www.math.uchicago.edu/~may/REU2016/REUPapers/Zhang%2CR.pdf).

## 3. Two-time block decodes the middle state

Choose any balanced function g:V(X)→{-1,+1}; this exists because
\[
|V(X)|=\tfrac12(q-1)q(q+1)
\]
is even.

For vertices y,z, define
\[
h(y,z)=
\begin{cases}
g(w),&y\ne z\text{ and }w\text{ is their unique common neighbor},\\
0,&\text{otherwise}.
\end{cases}
\]
This is well-defined. If y,z are distinct neighbors of x and had another common neighbor w≠x, the edges x-y-w-z-x would form a 4-cycle. Thus x is their unique common neighbor.

For a stationary walk (X_t), conditional on X_1=x, the variables X_0 and X_2 are independent uniform neighbors of x. Hence
\[
\mathbb E[h(X_0,X_2)\mid X_1=x]
=\Pr(X_0\ne X_2\mid X_1=x)g(x)
=\left(1-\frac1d\right)g(x).
\]
Set
\[
G_1=h(X_0,X_2),\qquad G_2=g(X_1).
\]
Both are bounded by one and centered. Therefore
\[
\boxed{
|\operatorname{Cov}(G_1,G_2)|
=1-\frac1d=\frac p{p+1}.
}
\tag{3}
\]

## 4. Contradiction with the proposed port weight

The two port sets are S_1={0,2} and S_2={1}. Taking the spectral decay parameter so that e^{-\Delta_0}=\theta_p, the proposed weight is
\[
W_{12}=\theta_p+\theta_p=\frac{4\sqrt p}{p+1}.
\]
Thus
\[
\frac{|\operatorname{Cov}(G_1,G_2)|}{W_{12}}
\ge \frac{p/(p+1)}{4\sqrt p/(p+1)}
=\frac{\sqrt p}{4}\longrightarrow\infty.
\]
No fixed C can make (1) hold.

The obstruction is synergistic decoding: each one-step transition has small L2 operator norm, but the pair of endpoints (X_0,X_2) can identify X_1. This is exactly the kind of multi-coordinate dependence that a mere pairwise spectral gap does not control.

## 5. Boundary: why this does not refute the heat-kernel target

The graph transition has zero entries. It has no uniform Doeblin minorization and no uniform positive bridge-density ratio. The earlier compact-group heat-kernel bridge audit supplies stronger conditional regularity, which excludes this construction.

Therefore:
- **Disproved:** the interlaced arbitrary-block estimate from an L2 spectral gap alone.
- **Not disproved:** the estimate for compact-group heat-kernel paths under the uniform bridge-Doeblin hypothesis.
- **Required next step:** prove an all-orders block-cumulant/tree inequality using that stronger bridge regularity, not merely the one-link L2 contraction or pairwise HGR.

This is an order-two obstruction, not an all-orders counterexample to the heat-kernel setting.
