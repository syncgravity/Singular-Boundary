# PF-I16 — All-orders interlaced block cumulant tree from Doeblin regeneration

**Date:** 2026-11-15  
**Status:** theorem proved under a uniform positive transition-density / Doeblin envelope; finite exact replica-cancellation regression added.  
**Scope:** one stationary Markov path; arbitrary bounded functionals of pairwise-disjoint finite port sets, including interlaced sets with overlapping temporal hulls. Constants are uniform in the number of ports and the time horizon.

## 1. Theorem

Let (X_t) be a stationary Markov process with invariant probability μ. Suppose its transition kernels have densities
\[
P_d(x,dy)=p_d(x,y)\,\mu(dy),\qquad d>0,
\]
and there are constants C_0,Δ_0>0 such that
\[
\alpha(d):=\inf_{x,y}p_d(x,y)>0,
\qquad
1-\alpha(d)\le C_0e^{-\Delta_0d}
\quad(d>0).
\tag{1.1}
\]
Let S_1,...,S_q be nonempty, pairwise-disjoint finite sets of distinct times, with no restriction on interlacing or temporal-hull overlap. Let
\[
G_i=G_i((X_s)_{s\in S_i}),\qquad \|G_i\|_\infty\le M_i,
\]
and put
\[
W_{ij}=\sum_{s\in S_i}\sum_{t\in S_j}e^{-\Delta_0|s-t|}.
\]
Then
\[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le C_q\prod_{i=1}^qM_i
\sum_{T\in\mathcal T_q}\prod_{\{i,j\}\in T}W_{ij},
}
\tag{1.2}
\]
where one valid explicit constant is
\[
C_q=K_q(qC_0)^{q-1},
\qquad
K_q=\sum_{\pi\in\Pi_q}(|\pi|-1)!.
\tag{1.3}
\]
For any fixed support-type cap q≤232, C_232:=max_{q≤232}C_q is finite and independent of every port count and time horizon.

This proves the requested all-orders-in-port-count estimate in the compact heat-kernel regime. The constant is deliberately crude; numerical usefulness for the later KP sum is a separate question.

## 2. Regeneration decomposition

Sort all ports as t_1<...<t_N, and let c_k∈[q] be the unique row label with t_k∈S_{c_k}. Write d_k=t_{k+1}-t_k.

By (1.1), for each gap
\[
P_{d_k}=\alpha_k\Pi+w_kR_k,
\qquad
\alpha_k=\alpha(d_k),\quad w_k=1-\alpha_k,
\tag{2.1}
\]
where Πf=μ(f) and
\[
R_k(x,dy)=\frac{p_{d_k}(x,y)-\alpha_k}{1-\alpha_k}\,\mu(dy)
\tag{2.2}
\]
is a Markov kernel preserving μ. If w_k=0, the residual kernel is immaterial.

Thus the sampled path has an exact construction with independent Bernoulli indicators A_k~Bernoulli(w_k). When A_k=0, the next state is a fresh independent μ-sample (a reset); when A_k=1, use R_k. Conditional on all indicators, the path decomposes into independent runs separated by reset gaps. Each run starts from μ and evolves by the corresponding stationary residual kernels.

The crucial activity estimate is
\[
w_k\le C_0e^{-\Delta_0d_k}.
\tag{2.3}
\]

## 3. Replica graph representation of the cumulant

Take q independent full copies (replicas) of the sampled path, each with its own independent reset indicators A_k^(r), r=1,...,q.

For each set partition π∈Π_q, assign its blocks injectively to the first |π| replica indices in a fixed canonical order; write r_π(B) for the replica assigned to block B. Define
\[
\Xi_\pi=
\prod_{B\in\pi}\prod_{i\in B}
G_i\big((X^{(r_\pi(B))}_s)_{s\in S_i}\big).
\tag{3.1}
\]
Because distinct blocks use independent replicas,
\[
\mathbb E\Xi_\pi=
\prod_{B\in\pi}\mathbb E\prod_{i\in B}G_i.
\]
The moment-partition formula for the classical cumulant is therefore the exact identity
\[
\kappa(G_1,\ldots,G_q)
=
\mathbb E\,\Xi,
\qquad
\Xi:=\sum_{\pi\in\Pi_q}
(-1)^{|\pi|-1}(|\pi|-1)!\,\Xi_\pi.
\tag{3.2}
\]
Pointwise,
\[
|\Xi|\le K_q\prod_iM_i.
\tag{3.3}
\]

Construct a random simple graph H on row labels [q]. Put edge {i,j} in H if, in at least one of the q replicas, at least one adjacent temporal gap k with {c_k,c_{k+1}}={i,j} is active (A_k^(r)=1). Same-row gaps are internal loops and are not included.

## 4. The disconnected-union cancellation lemma

**Lemma.** Conditional on H, if H has at least two connected components, then
\[
\mathbb E[\Xi\mid H]=0.
\tag{4.1}
\]

**Proof.** Fix H with components C_1,...,C_m, m≥2.

For every pair of labels in different H-components, all corresponding temporal-gap indicators are zero in every replica. Hence every transition between ports whose labels lie in different components is a reset. The reset indicators for distinct unordered row pairs are independent; conditioning on H preserves independence between the collections internal to distinct components, because H_ij is a function only of the indicators attached to pair {i,j}. Same-row indicators and all reset/residual transition innovations are also independent across components. Consequently, conditional on H, the arrays of all q replicas restricted to ports whose labels lie in different components are independent.

The q replicas are exchangeable under conditioning on H, since H is defined symmetrically as their union graph. For a partition π, the conditional expectation of Xi_π therefore factors as
\[
\mathbb E[\Xi_\pi\mid H]
=
\prod_{a=1}^m F_{C_a}(\pi|_{C_a}),
\tag{4.2}
\]
where π|_{C_a} is the partition of C_a obtained by intersecting the blocks of π with C_a and deleting empty intersections. Exchangeability makes F_{C_a} depend only on this restricted partition, not on the replica indices assigned to the global blocks.

It remains to use a partition-lattice identity. For any nontrivial partition C={C_1,...,C_m} of [q], and arbitrary functions F_C on partitions of C,
\[
\sum_{\pi\in\Pi_q}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{C\in\mathcal C}F_C(\pi|_C)=0.
\tag{4.3}
\]
To see this, fix restrictions σ_C=π|_C. Regard the blocks of all σ_C as atoms, colored by C. Global partitions π with these restrictions are exactly partitions of these atoms into rainbow blocks (no two atoms of the same color in one block). Such partitions are the color-class partitions of proper colorings of the disjoint union graph
\[
G_\sigma=\bigsqcup_{C\in\mathcal C}K_{|\sigma_C|}.
\]
The sum of their Möbius coefficients is the derivative at zero of the chromatic polynomial:
\[
\sum_{\pi:\,\pi|_C=\sigma_C}
(-1)^{|\pi|-1}(|\pi|-1)!
=\chi'_{G_\sigma}(0).
\]
But
\[
\chi_{G_\sigma}(x)=
\prod_{C\in\mathcal C}x^{\underline{|\sigma_C|}}
\]
has a zero of order m≥2 at x=0. Thus the derivative is zero. Summing over all restrictions proves (4.3). Combining (4.2) and (4.3) gives (4.1). ∎

## 5. Connectivity probability and the tree bound

By (4.1), E Xi receives contribution only when H is connected. Therefore (3.3) gives
\[
|\kappa(G_1,\ldots,G_q)|
\le K_q\prod_iM_i\,\Pr(H\text{ connected}).
\tag{5.1}
\]

For each row pair {i,j}, the edge event H_ij is the OR of q independent-replica indicators over all adjacent temporal gaps with endpoint labels i,j. Hence
\[
p_{ij}:=\Pr(H_{ij}=1)
\le q\sum_{k:\{c_k,c_{k+1}\} =\{i,j\}}w_k
\le qC_0
\sum_{k:\{c_k,c_{k+1}\} =\{i,j\}}
e^{-\Delta_0d_k}
\le qC_0W_{ij}.
\tag{5.2}
\]
For distinct row pairs, the underlying gap-indicator sets are disjoint, so the edge events H_ij are independent. If H is connected it contains a spanning tree; the union bound and independence yield
\[
\Pr(H\text{ connected})
\le
\sum_{T\in\mathcal T_q}\prod_{\{i,j\}\in T}p_{ij}
\le(qC_0)^{q-1}
\sum_{T\in\mathcal T_q}\prod_{\{i,j\}\in T}W_{ij}.
\tag{5.3}
\]
Equations (5.1)–(5.3) prove (1.2).

## 6. Compact-group heat-kernel hypothesis

For a compact group with normalized Haar measure and strictly positive continuous heat kernel p_t(x,y), compactness gives α(d)=inf_{u≥d,x,y}p_u(x,y)>0 for every d>0. If
\[
\sup_{x,y}|p_t(x,y)-1|\le C e^{-\lambda t}
\]
for t≥t0, then 1-α(d)≤C_0e^{-λd} for all d>0 after enlarging C_0 to cover d<t0. Thus (1.1) holds.

For the SU(2) heat kernel in the existing bridge audit,
\[
\sup_g|\kappa_\tau(g)-1|\le C e^{-3\tau/4},\qquad \tau\ge1.
\]
Under the already stated refinement-uniform link-gap hypothesis Δ_h≥Δ_0>0, the heat-kernel parameter satisfies α_h≥4Δ_0/3, giving (1.1) uniformly in the link and regulator.

## 7. Scope and constants

Established:
- Arbitrary bounded block functionals; no product expansion of G_i is used.
- Pairwise-disjoint port sets with arbitrary interlacing and overlapping hulls.
- Uniformity in port count, temporal horizon, and (under the uniform SU(2) heat-kernel bounds) link/regulator.
- An explicit all-orders tree coefficient C_q=K_q(qC_0)^(q-1), and hence a finite C_232 for the PF-I16 per-link distinct-support cap.

Limitations:
- The displayed C_q is crude and grows faster than exponentially; it proves the finite-q/port-uniform statement but may not be numerically useful for the later KP sum.
- The argument requires a genuine uniform minorization P_d(x,·)≥α(d)μ(·). An L2 spectral gap alone is insufficient; see PF_I16_L2_GAP_INTERLACED_BLOCK_OBSTRUCTION_2026_11_15.md.
- This closes the local interlaced block-functional obligation, not the multiplicity-uniform global occurrence-level resummation, marked-root spatial summation, KP convergence, interacting-vacuum Poincare inequality, or continuum mass gap.
