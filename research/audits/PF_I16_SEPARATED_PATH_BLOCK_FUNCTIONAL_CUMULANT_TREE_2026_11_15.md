# PF-I16 — Sharp Markov path-block cumulant tree for separated temporal hulls

**Date:** 2026-11-15  
**Status:** ESTABLISHED for any fixed finite number q of bounded path-block observables whose temporal hull intervals are pairwise disjoint and ordered. The sharp one-link coefficient (2^{q-2}) survives unchanged, independent of the number of sample times inside a block, interval lengths, and horizon. Interlaced/overlapping hulls remain open.

## 1. Setup

Let (X_t) be a stationary reversible Markov process with semigroup (P_t), invariant law (pi), and
[
\|P_t-\Pi\|_{L^2(\pi)\to L^2(\pi)}\le e^{-\Delta_0t},
\qquad \Pi f=\pi(f)\mathbf1.
\tag{1.1}
]
Let (S_1,\ldots,S_q) be finite nonempty time sets, with ordered disjoint hulls
[
J_a=[u_a,v_a]=[\min S_a,\max S_a],
\qquad v_a<u_{a+1},\quad a=1,\ldots,q-1.
\tag{1.2}
]
Let (G_a) be any bounded measurable function of the path coordinates ((X_s)_{s\in S_a}), and put (M_a=\|G_a\|_\infty).

For (i<j), define the interval-gap weight
[
w_{ij}=e^{-\Delta_0(u_j-v_i)},\qquad w_{ji}=w_{ij}.
\tag{1.3}
]
For a tree T on the block labels, write (w(T)=\prod_{\{i,j\}\in T}w_{ij}).

## 2. Path transfer operators and Boolean cumulants

For each block a, define the path transfer operator from (u_a) to (v_a):
[
(K_af)(x)=\mathbb E_x[G_a f(X_{v_a})],
\tag{2.1}
]
where the conditional expectation includes the path coordinates in (S_a). Positivity and domination by (P_{v_a-u_a}) imply
[
\|K_a\|_{2\to2}\le M_a.
\tag{2.2}
]
For any ordered subfamily (i_1<\cdots<i_k), the Boolean cumulant is the interval-partition cumulant of these variables. Its transfer-operator identity is
[
B_k(G_{i_1},\ldots,G_{i_k})
=
\langle\mathbf1,
K_{i_1}(P_{u_{i_2}-v_{i_1}}-\Pi)K_{i_2}
\cdots
(P_{u_{i_k}-v_{i_{k-1}}}-\Pi)K_{i_k}
\mathbf1\rangle_\pi.
\tag{2.3}
]
Indeed, expanding each (P-Pi) gives inclusion–exclusion over interval partitions, which is precisely Boolean moment-cumulant inversion. Therefore
[
|B_k(G_{i_1},\ldots,G_{i_k})|
\le
\left(\prod_{\ell=1}^kM_{i_\ell}\right)
\exp\left[-\Delta_0
\sum_{\ell=1}^{k-1}(u_{i_{\ell+1}}-v_{i_\ell})\right].
\tag{2.4}
]
For k=1 this is the trivial mean bound.

## 3. Cyclic-permutation conversion

The multivariate classical/Boolean cumulant formula expresses the classical cumulant as a signed sum over cyclic permutations. Each cycle is decomposed into its maximal increasing runs; each run contributes one Boolean cumulant, and the sign is ((-1)^{\#\mathrm{runs}-1}). Taking absolute values and applying (2.4), we obtain
[
|\kappa(G_1,\ldots,G_q)|
\le
\left(\prod_{i=1}^qM_i\right)W_q,
\tag{3.1}
]
where
[
W_q=
\sum_{\sigma\in\mathfrak C_q}
\prod_{a\to b\text{ an increasing edge of }\sigma}w_{ab}.
\tag{3.2}
]
The increasing edges of a cycle are exactly the adjacent pairs within its increasing runs. This is the same cyclic weight polynomial as in the one-time Markov theorem, with (e^{-\Delta_0(s_j-s_i)}) replaced by the interval-gap weight (w_{ij}).

## 4. Temporal tree theorem for interval-gap weights

Let
[
\tau_q=\sum_{T\in\mathcal T_q}w(T)
\tag{4.1}
]
be the spanning-tree polynomial of the complete graph on block labels.

**Theorem.** For all q≥2,
[
\boxed{W_q\le2^{q-2}\tau_q.}
\tag{4.2}
]

**Proof.** The case q=2 is equality. For q≥3, insert the largest label q into a directed edge (a\to b) of a cycle (sigma') on ([q-1]). If (a<b), the old increasing edge (a\to b) is replaced by the increasing edge (a\to q), while (q\to b) is decreasing. The ratio of new to old weight is
[
\frac{w_{aq}}{w_{ab}}
=e^{-\Delta_0[(u_q-v_a)-(u_b-v_a)]}
=e^{-\Delta_0(u_q-u_b)}
\le e^{-\Delta_0(u_q-v_b)}=w_{bq}.
\tag{4.3}
]
If (a>b), the old edge was decreasing and had weight one in (3.2); the insertion creates the increasing edge (a\to q), whose weight is (w_{aq}=w_{\max(a,b),q}). Thus in either case the insertion multiplies the cycle weight by at most (w_{\max(a,b),q}).

Every vertex of (sigma') is incident to two directed edges, so summing over all insertion positions gives
[
W_q\le2W_{q-1}\sum_{i=1}^{q-1}w_{iq}.
\tag{4.4}
]
On the other hand, every tree on ([q]) obtained by attaching q as a leaf to i to a tree on ([q-1]) is distinct, hence
[
\tau_q\ge\tau_{q-1}\sum_{i=1}^{q-1}w_{iq}.
\tag{4.5}
]
Induction proves (4.2). \(\square\)

Combining (3.1) and (4.2),
[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le
2^{q-2}\left(\prod_{i=1}^q\|G_i\|_\infty\right)
\sum_{T\in\mathcal T_q}
\prod_{\{i,j\}\in T}
e^{-\Delta_0(u_{\max(i,j)}-v_{\min(i,j)})}.
}
\tag{4.6}
]

## 5. Port-pair tree form

Define
[
W_{ij}^{\mathrm{port}}
=\sum_{s\in S_i,t\in S_j}e^{-\Delta_0|s-t|}.
\tag{5.1}
]
For i<j, the last port (v_i\in S_i) and first port (u_j\in S_j) give
[
W_{ij}^{\mathrm{port}}\ge e^{-\Delta_0(u_j-v_i)}=w_{ij}.
\tag{5.2}
]
Therefore (4.6) implies the desired port-pair tree estimate
[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le
2^{q-2}\left(\prod_i\|G_i\|_\infty\right)
\sum_{T\in\mathcal T_q}
\prod_{\{i,j\}\in T}W_{ij}^{\mathrm{port}}.
}
\tag{5.3}
]
The coefficient is exactly the one-link coefficient (2^{q-2}), and is independent of the number of time ports in each block.

## 6. Extension to port-overlap clusters with separated cluster hulls

There is a useful extension when individual block hulls overlap, but their actual port-overlap components remain temporally separated. Form the graph O on block labels by joining a,b when (S_a\cap S_b\ne\varnothing). Let its connected components be (C_1,\ldots,C_k), ordered so that their union hulls
[
J_j=[U_j,V_j]=
[\min_{a\in C_j,s\in S_a}s,\max_{a\in C_j,s\in S_a}s]
]
satisfy (V_j<U_{j+1}). Put (g_j=U_{j+1}-V_j).

For any subset (B\subseteq[q]), the product of the selected (G_a)'s within a component (C_j) is a bounded path functional on (J_j), with norm at most (prod_{a\in B\cap C_j}M_a). Its path transfer operator therefore has the same contraction bound as in (2.2). The global moment has the transfer representation (2.2) with one such component operator per (C_j) and gap transitions (P_{g_j}). The exact gap-cancellation lemma from Section 3 applies verbatim, giving
[
|\kappa(G_1,\ldots,G_q)|
\le C_q\left(\prod_aM_a\right)e^{-\Delta_0\sum_{j=1}^{k-1}g_j}.
\tag{6.1}
]

This decay is represented by a spanning tree on the original q block labels. Inside each overlap component (C_j), choose a spanning tree of its overlap graph; every chosen edge has (S_a\cap S_b\ne\varnothing), hence (W_{ab}^{\mathrm{port}}\ge1). Between consecutive components, choose a block containing (V_j) and a block containing (U_{j+1}); their port-pair weight is at least (e^{-\Delta_0g_j}). The union of the internal component trees and these k−1 cross-component edges is a spanning tree on [q]. Consequently the port-pair tree polynomial dominates the exponential in (6.1), and
[
|\kappa(G_1,\ldots,G_q)|
\le C_q\left(\prod_aM_a\right)
\sum_{T\in\mathcal T_q}\prod_{\{a,b\}\in T}W_{ab}^{\mathrm{port}}.
\tag{6.2}
]
When every overlap component is a singleton, the sharper (2^{q-2}) coefficient of (5.3) applies.

This cluster extension still excludes the genuinely interlaced case in which two port sets are disjoint but their hulls overlap (for example (S_a=\{0,100\}), (S_b=\{40,60\})). In that case there is no shared-port tree edge of weight at least one and no temporal cut separating the two block functionals.

## 7. Boundary

- Arbitrary bounded path functionals on pairwise disjoint ordered hulls: **ESTABLISHED**.
- Number of sample times per block and horizon: unrestricted.
- Number q of blocks: arbitrary finite; for PF-I16 local support types, q≤232.
- Interlaced port sets whose hulls overlap: **OPEN**. The ordered block transfer-operator representation no longer applies as a simple chain of disjoint segments. Compressing to hulls loses the finer port-pair weights; pairwise conditional HGR alone is insufficient.
- General repeated-support local block-functional theorem, cyclic hyperedges of arity at least four, KP convergence, interacting-vacuum Poincaré, scale setting, and the continuum mass gap remain open.

The companion verifiers check the exact gap-reset cancellation and the interval-weight cyclic insertion/tree inequality with rational finite data. The semigroup norm bound (1.1) is an analytic hypothesis. No P0–P5 gate is promoted.
