# PF-I16 interlaced path-block cumulant: temporal-edge forest reduction

**Date:** 2026-11-15  
**Status:** rigorous reduction; the all-orders derivative estimate remains open  
**Scope:** one stationary Markov path, finite pairwise-disjoint port sets with arbitrary interlacing and overlapping temporal hulls.

## 1. Target

Let (X_t) be stationary with invariant law π, semigroup P_t, and
\[
\|P_t-\Pi\|_{L^2_0(\pi)\to L^2_0(\pi)}\le e^{-\Delta_0t},
\qquad \Pi f=\pi(f).
\]
Let S_1,...,S_q be finite, pairwise-disjoint sets of distinct times. No ordering or hull-separation assumption is imposed. Let
\[
G_i=G_i((X_s)_{s\in S_i}),\qquad \|G_i\|_\infty\le M_i,
\]
with arbitrary bounded measurable block functionals. Define
\[
W_{ij}=\sum_{s\in S_i}\sum_{t\in S_j}e^{-\Delta_0|s-t|}.
\]
The desired estimate is
\[
|\kappa(G_1,\ldots,G_q)|
\le C^q\prod_iM_i
\sum_{T\in\mathcal T_q}\prod_{\{i,j\}\in T}W_{ij},
\tag{1}
\]
with C independent of all port counts and time horizons.

## 2. Exact temporal-edge interpolation

Sort the union of ports as t_1<...<t_N, and let c_k∈[q] be the unique row label for which t_k∈S_{c_k}. For each adjacent gap d_k=t_{k+1}-t_k, introduce a parameter λ_ij∈[0,1] for the unordered pair {c_k,c_{k+1}}, provided c_k≠c_{k+1}. Keep same-row transitions unchanged. Replace each cross-row transition by
\[
K_k^{\lambda}=\Pi+\lambda_{c_kc_{k+1}}(P_{d_k}-\Pi)
=(1-\lambda_{c_kc_{k+1}})\Pi+\lambda_{c_kc_{k+1}}P_{d_k}.
\tag{2}
\]
This is a stationary Markov kernel. It defines one globally consistent path law, hence a consistent family of all subset moments. At λ_ij=1 for every pair, the original path law is recovered.

Let Φ(λ)=κ_λ(G_1,...,G_q). If the graph on row labels with edges {i,j} for which λ_ij>0 is disconnected, every transition across distinct graph components is Π. The path then splits into independent runs, each run containing labels from only one component. Thus the corresponding row families are independent and
\[
\Phi(\lambda)=0\quad\text{whenever the positive-parameter graph is disconnected.}
\tag{3}
\]

The Brydges--Kennedy--Abdesselam--Rivasseau forest formula applied to Φ therefore reduces its value at the all-ones point to spanning-tree terms:
\[
\Phi(\mathbf1)=
\sum_{T\in\mathcal T_q}
\int_{[0,1]^{T}}
(\partial_T\Phi)(\lambda^T(s))\,ds.
\tag{4}
\]
Here λ^T_ij(s) is the minimum of the edge parameters along the unique T-path from i to j. Non-spanning forests vanish because (3) holds identically on the corresponding disconnected parameter subspace.

## 3. The exact remaining analytic obligation

For a tree T, differentiating Φ in its q-1 distinct row-pair parameters selects one or more temporal transitions for each tree edge. A sufficient estimate is
\[
\sup_{\lambda\in[0,1]^{\binom q2}}
|\partial_T\Phi(\lambda)|
\le C^q\prod_iM_i
\prod_{\{i,j\}\in T}a_{ij},
\tag{5}
\]
where
\[
a_{ij}:=
\sum_{k:\{c_k,c_{k+1}\}=\{i,j\}}
e^{-\Delta_0d_k}
\le W_{ij}.
\tag{6}
\]
Indeed, inserting (5) into (4), integrating over a unit cube, and summing over row trees gives (1).

The local operator part of (5) is straightforward: differentiating one transition inserts Q_{d_k}=P_{d_k}-Π, whose L²-operator norm is at most e^{-Δ_0d_k}; all undifferentiated kernels in (2) are contractions. The unresolved part is the **connected-log / cumulant combinatorics**: the q-1 derivatives act on the logarithm of the path moment functional, not merely on its full joint moment. A uniform C^q bound for that connected derivative, with arbitrary interlacing and arbitrary numbers of ports, is not yet established.

## 4. A precise warning: derivative does not collapse to the full moment

It is tempting to assert ∂_TΦ=∂_TM([q]), where M([q])=E_λ∏_iG_i. This is false for the globally consistent interpolation (2), because a transition involving an omitted row can still affect the marginal law of a block whose ports straddle that transition.

An exact five-port example is:
- row A: ports 0,3, with G_A=X_0X_3;
- row B: port 1, with G_B=X_1;
- row C: ports 2,4, with G_C=X_2+X_4.

The temporal label sequence is A,B,C,A,C, so the hulls of A and C overlap and all five ports are used. Take a stationary symmetric two-state Markov chain. Under (2), let the adjacent transition correlations be
\\[
r_1=\\rho x,\\quad r_2=\\rho y,\\quad r_3=r_4=\\rho z,
\\]
where x=λ_AB, y=λ_BC, and z=λ_AC. Direct calculation gives
\\[
M_A=\\rho^3xyz,\\quad M_B=M_C=M_{AB}=M_{AC}=0,
\\]
\\[
M_{BC}=\\rho y+\\rho^3yz^2,\\qquad
M_{ABC}=2\\rho^2xz.
\\]
Hence
\\[
\\Phi(x,y,z)=\\kappa_\\lambda(G_A,G_B,G_C)
=\\rho^2xz\\left(2-\\rho^2y^2-\\rho^4y^2z^2\\right).
\\]
For the row tree T={{A,B},{A,C}},
\\[
\\partial_x\\partial_z\\Phi
=\\rho^2\\left(2-\\rho^2y^2-3\\rho^4y^2z^2\\right),
\\qquad
\\partial_x\\partial_z M_{ABC}=2\\rho^2.
\\]
Their difference is
\\[
-\\rho^4y^2(1+3\\rho^2z^2)\\ne0
\\]
whenever ρy≠0. The extra term comes from the partition contribution -M_A M_{BC}. This example is a regression against the invalid derivative-collapse shortcut, not a counterexample to (1).
## 5. What is established and what is not

Established:
1. The interpolation (2) is globally consistent and recovers the original path law at λ=1.
2. Disconnected positive-parameter graphs give exact independence of row families, hence (3).
3. The forest formula reduces the desired estimate to the spanning-tree derivative bound (5).
4. Every selected temporal transition has the required one-link factor e^{-Δ_0d_k}, and the row-pair sum (6) is bounded by the requested all-port weight.

Still open:
- Prove (5) with a constant exponential in q, independent of port count, or find a counterexample.
- The previous absolute-value LS resummation is not a substitute: its multiplicity-uniform majorant is false.
- Pairwise subjective HGR alone is not a substitute: the exact three-variable parity obstruction is already recorded in PF_I16_SUBJECTIVE_HGR_CUMULANT_TREE_OBSTRUCTION_2026_11_15.md.

No all-orders interlaced path-block theorem is claimed in this audit. This is a reduction of the unresolved obligation to one explicit connected-log derivative inequality.
