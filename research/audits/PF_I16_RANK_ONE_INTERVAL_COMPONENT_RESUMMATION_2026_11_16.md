# PF-I16 — Exact interval-component resummation in the rank-one link model

**Date:** 2026-11-16  
**Status:** exact scalar-model resummation proved; multi-link extension remains open  
**Scope:** isolate the cancellation mechanism for the interval-covering partitions left by the omitted-port derivative obstruction. This is a rigorous subcase, not a proof of the general support-localized cumulant-tree theorem.

## 1. Rank-one ordered-link model

Take one stationary Markov link with ordered ports (1<\cdots<R). Assume each row observable is the same centered eigenfunction (X_i=X(t_i)), with
[
\mathbb E X=0,\qquad \|X\|_\infty\le1,\qquad
P_{s,t}X=q_{s,t}X,quad 0\le q_{s,t}\le1.
]
For the link-compressed interpolation, write the transition across consecutive ports as
[
K_i(\lambda_i)=\Pi+\lambda_i(P_i-\Pi),\qquad i=1,\ldots,R-1.
]
Because (X) is centered and is an eigenfunction, the marginal moment on a retained block (B\subseteq[R]) is exactly
[
M_B(\lambda)
=m_{|B|}\prod_{i\in H(B)}(\lambda_iq_i),\qquad
m_j=\mathbb E X^j,
]
where
[
H(B)=\{i:\min B\le i<\max B\}
]
is the set of transition cuts inside the block's port hull. In particular, singleton block moments vanish.

For a partition \(\pi\), let
[
c_i(\pi)=\#\{B\in\pi:i\in H(B)\}.
]
Then
[
\prod_{B\in\pi}M_B(\lambda)
=\left(\prod_{B\in\pi}m_{|B|}\right)
 \prod_{i=1}^{R-1}(\lambda_iq_i)^{c_i(\pi)}.
]
Differentiating once in every path transition and integrating over the BKAR cube gives the exact identity
[
\int_{[0,1]^{R-1}}
\left|\partial_{\lambda_1}\cdots\partial_{\lambda_{R-1}}
\prod_{B\in\pi}M_B(\lambda)\right|d\lambda
=
\begin{cases}
\displaystyle
\left(\prod_{B\in\pi}|m_{|B|}|\right)
\prod_{i=1}^{R-1}q_i^{c_i(\pi)},&
c_i(\pi)\ge1\text{ for every }i,\\
0,&\text{otherwise.}
\end{cases}
\tag{1.1}
]
The factors (c_i(\pi)) from differentiation disappear because
\(\int_0^1c_i\lambda_i^{c_i-1}d\lambda_i=1\).
This is the exact cancellation mechanism that the previous pointwise derivative estimate missed.

## 2. Signed interval-covering sum

The moment-cumulant formula and (1.1) imply
[
\begin{aligned}
&\int_{[0,1]^{R-1}}
\left|\partial_{\lambda_1}\cdots\partial_{\lambda_{R-1}}
\kappa(X_1,\ldots,X_R)\right|d\lambda\\
&\quad\le
\sum_{\substack{\pi\in\Pi_R:\ c_i(\pi)\ge1\ \forall i}}
(|\pi|-1)!\prod_{B\in\pi}|m_{|B|}|
\prod_{i=1}^{R-1}q_i^{c_i(\pi)}.
\end{aligned}
\tag{2.1}
]
Every surviving partition has block hulls whose union covers the full ordered port interval. Since (q_i\le1) and (c_i\ge1), its temporal factor is bounded by the path-tree weight
\(\prod_iq_i\).

Using \(|m_j|\le1\) and the Stirling-number estimate
\[
S(R,k)\le\frac{k^R}{k!},
]
the right side of (2.1) is at most
[
\sum_{k=1}^R(k-1)!S(R,k)\prod_iq_i
\le\left(\sum_{k=1}^Rk^{R-1}\right)\prod_iq_i
\le R^R\prod_iq_i.
]
For (R\ge2), (R^R\le4^R R^{R-2}). The path is a spanning tree of the complete one-link support graph (K_R), so
[
\boxed{
\int_{[0,1]^{R-1}}|\partial_{[R-1]}\kappa|\,d\lambda
\le4^R
\sum_{T\in\mathcal T(K_R)}\prod_{\{i,j\}\in T}w_{ij},
}
\tag{2.2}
]
where the path-tree weight is \(\prod_iq_i\), and the other tree terms are nonnegative. This is an exponential-coefficient integrated tree estimate for this rank-one, one-link model.

The estimate is deliberately crude. It does not establish the desired theorem for general bounded link observables or multi-link super-rows.

## 3. Exact connected-component generating function

There is a useful exact resummation of the signed sum at coincident times (q_i=1). For a partition \(\pi\), form the union of its block hull intervals. An uncovered transition cut separates \(\pi\) into independent consecutive restrictions. Cutting at all uncovered cuts decomposes every partition uniquely into consecutive components whose block hulls cover every internal cut.

Let
[
P_R(u)=\sum_{\pi\in\Pi_R}u^{|\pi|}
\prod_{B\in\pi}m_{|B|},
]
and let (C_R(u)) be the same weighted sum restricted to partitions whose block hulls cover all (R-1) cuts. With ordinary generating functions
[
P(z,u)=\sum_{R\ge0}P_R(u)z^R,\qquad
C(z,u)=\sum_{R\ge1}C_R(u)z^R,
]
the unique consecutive-component decomposition gives
[
P(z,u)=1+C(z,u)+C(z,u)^2+\cdots
=\frac1{1-C(z,u)}.
]
Hence
[
\boxed{C(z,u)=1-\frac1{P(z,u)}.}
\tag{3.1}
]
The ordinary partition polynomial is computable from the partial Bell recurrence
[
P_0(u)=1,\qquad
P_R(u)=\sum_{j=1}^R
\binom{R-1}{j-1}m_j u P_{R-j}(u).
\tag{3.2}
]
The fully signed interval-covering sum is therefore the explicit coefficient functional
[
\boxed{
S_R=\sum_{k=1}^R(-1)^{k-1}(k-1)![u^k]C_R(u).
}
\tag{3.3}
]
Equations (3.1)–(3.3) resum the Möbius signs before taking absolute values.

For the symmetric two-state eigenfunction (X\in\{-1,+1\}), so (m_j=1) for even (j) and (m_j=0) for odd (j), the exact values are
[
S_2=1,\ S_4=-1,\ S_6=8,\ S_8=-149,\
S_{10}=4778,\ S_{12}=-231205,\ S_{14}=15638140.
]
These values are diagnostics, not an asymptotic theorem.

## 4. What this resolves and what it does not

Resolved in this subcase:

1. The surviving partitions are exactly those whose block hulls cover every differentiated transition.
2. Integrating the differentiated monomial over its BKAR parameter removes the multiplicity (c_i(\pi)) exactly.
3. The remaining signed partition sum has a connected-component generating function (C=1-P^{-1}).
4. A direct absolute bound gives an exponential coefficient (4^R) against the complete one-link support-tree polynomial.

Still open for the PF-I16 target:

- for a general bounded link observable, a block marginal need not be divisible by every \(\lambda_i\) in its hull: resetting at a cut can leave a product of nonzero left and right marginal moments. Thus (1.1) does not extend by simply replacing (m_{|B|}) with a general block moment;
- in the multi-link case, a differentiated support edge may be covered by a hull on one of several links, and the link colors must be combined without losing the row-incidence factor (m);
- the connected-component identity (3.1) is one-link and ordered-port-specific; no multi-link analogue with an exponential (C_m^R) coefficient is proved here.

Accordingly, this result does not promote any P0–P5 gate and does not close the Yang–Mills mass-gap proof.
