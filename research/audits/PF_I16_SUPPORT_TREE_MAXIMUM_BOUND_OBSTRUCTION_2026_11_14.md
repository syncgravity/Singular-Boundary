# PF-I16 — Obstruction to an exponential coefficient times the support maximum-tree weight

**Date:** 2026-11-14  
**Status:** the proposed pointwise bound with a single support-maximum-tree factor and only exponential order coefficient is FALSE for the stated general bounded-local-observable / independent-link Markov class. A weaker support-tree *sum* bound remains a possible target. This is not a counterexample to the actual smooth face/pair insertion subclass, and it does not close or refute the PF-I16 mass-gap program.

## 1. The proposed estimate and why it needs testing

The termwise support-temporal extraction suggests trying
[
|kappa(A_1(t_1),ldots,A_r(t_r))|
le C_{m slot}^{,r}prod_i|A_i|_infty,
mathcal M(G_X;mathbf t),
qquad
mathcal M(G_X;mathbf t)
=max_{Tinmathcal T(G_X)}
prod_{{i,j}in T}e^{-Delta|t_i-t_j|}.
	ag{1.1}
]
The desired coefficient is exponential in (r), not factorial. The next example shows that (1.1) cannot hold uniformly for arbitrary bounded local observables, even when the reference process is a single stationary Markov link with a uniform spectral gap.

## 2. One-link stationary Markov counterexample

Let the single link state space be (SU(2)), with normalized Haar law (
u). Define the stationary reset semigroup
[
P_t=e^{-Delta t}I+(1-e^{-Delta t})Pi,
qquad
Pi f=int f,d
u.
	ag{2.1}
]
This is a Markov semigroup: it is the process that keeps its current state until a rate-(Delta) Poisson reset to an independent Haar state. It is stationary and satisfies the exact mean-zero contraction
[
|P_t-Pi|_{2	o2}=e^{-Delta t}.
	ag{2.2}
]

Let
[
h(U)=operatorname{sgn}(operatorname{Tr}U).
	ag{2.3}
]
The trace is real on (SU(2)), the zero-trace set has Haar measure zero, and Haar invariance under (Umapsto-U) gives
[

u(h=1)=
u(h=-1)=	frac12.
]
Thus (h) is a Haar Rademacher variable. For every row (i), take the same one-link local observable
[
A_i(t_i)=h(X_{t_i}),qquad X_i={e}.
	ag{2.4}
]
The incidence budget is (sum_e|I_e|=rle8r), and the support-overlap graph (G_X) is the complete graph (K_r).

Set all observation times equal, (t_1=cdots=t_r=0). Then every edge weight is one and
[
mathcal M(K_r;mathbf0)=1,qquad |A_i|_infty=1.
	ag{2.5}
]
The joint cumulant is exactly the scalar Rademacher cumulant.

## 3. Exact cumulant and factorial growth

The moment generating function of a Rademacher variable is (cosh z), so its cumulant generating function is
[
logcosh z
=sum_{nge1}kappa_{2n}rac{z^{2n}}{(2n)!},
qquad kappa_{2n+1}=0.
]
Using the Bernoulli-number expansion,
[
oxed{
kappa_{2n}
=rac{2^{2n}(2^{2n}-1)}{2n}B_{2n}.
}
	ag{3.1}
]
Since
[
|B_{2n}|=rac{2(2n)!}{(2pi)^{2n}}zeta(2n),
]
we get the exact magnitude
[
oxed{
|kappa_{2n}|
=left(rac4{pi^2}ight)^n
left(1-4^{-n}ight)rac{(2n)!}{n},zeta(2n).
}
	ag{3.2}
]
In particular, because (zeta(2n)>1) and (1-4^{-n}ge3/4),
[
|kappa_{2n}|
gerac34left(rac4{pi^2}ight)^nrac{(2n)!}{n}.
	ag{3.3}
]
For every fixed finite (C), the ratio (|kappa_{2n}|/C^{2n}) diverges as (n	oinfty), by factorial growth.

But (1.1) would give (|kappa_{2n}|le C_{m slot}^{2n}) in this example, contradicting (3.3). Therefore:

[
oxed{	ext{No uniform }C^rmathcal M(G_X;mathbf t)	ext{ bound holds for all bounded local observables.}}
]

This obstruction is within the independent-link stationary Markov framework itself; it is stronger than the earlier parity example, which only ruled out deriving a tree-product bound from abstract cut-QF.

## 4. What survives and the correct revised target

The obstruction does **not** rule out a bound with a sum over support trees:
[
|kappa(A_1(t_1),ldots,A_r(t_r))|
le C^rprod_i|A_i|_infty
sum_{Tinmathcal T(G_X)}
prod_{{i,j}in T}e^{-Delta|t_i-t_j|}.
	ag{4.1}
]
For (G_X=K_r) and coincident times, the tree sum is (r^{r-2}), which has the factorial-scale growth needed to accommodate (3.2). A support-tree sum also retains the spatial dependency graph, unlike the existing global projection-tree estimate over all labeled trees.

The remaining problem is therefore sharpened:

1. Prove (4.1), or a suitable marked-root/weighted variant, for the actual PF-I16 face/pair insertion class.
2. Preserve coordinate labels so trees lie in (G_X), while using the signed product-semigroup projection expansion before absolute values.
3. Keep the tree **sum**, rather than replacing it by its maximum, so high-order one-link cumulants are not forced into an impossible exponential-only coefficient.
4. Integrate the tree sum with the Feynman–Kac (1/r!) normalization and perform the spatial support sum under the actual activity constants.

The parity-law cut-QF obstruction remains relevant: QF alone still does not imply (4.1). The product Markov/tensor structure and local coordinate incidence must be used.

## 5. Scope

- The proposed (C^r) times a single support-maximum-tree factor for arbitrary bounded local observables: **REFUTED** by (2.1)–(3.3).
- A support-tree **sum** bound: **OPEN**.
- The same maximum-tree bound restricted to the actual smooth face/pair insertions: **NOT DECIDED** by this counterexample.
- Global complete-graph projection-tree temporal cumulant bound: **ESTABLISHED** under the independent stationary product-Markov hypotheses in its companion audit.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincaré inequality, continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
