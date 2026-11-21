# PF-I16 — Formal interval-component resummation and its Markov obstruction

**Date:** 2026-11-16  
**Status:** exact formal-combinatorial identity proved; proposed Markov monomial reduction REFUTED by a four-port example  
**Scope:** a candidate resummation device for the interval-covering partition sum, together with the exact reason it cannot yet be applied to genuine Markov block moments.

## 1. The formal monomial model

For ordered ports (1<\cdots<R), let
[
H(B)=\{i:\min B\le i<\max B\}
]
be the set of cuts inside the hull of a nonempty block (B\subseteq[R]). Consider the *formal* block weights
[
\widetilde M_B(\lambda)
=m_{|B|}\prod_{i\in H(B)}(\lambda_iq_i),
\qquad |m_j|\le1,\quad 0\le q_i\le1.
\tag{1.1}
]
These are a combinatorial model, not the general block moments of a Markov chain.

For a partition \(\pi\), put
[
c_i(\pi)=\#\{B\in\pi:i\in H(B)\}.
]
Then
[
\prod_{B\in\pi}\widetilde M_B
=\left(\prod_{B\in\pi}m_{|B|}\right)
\prod_{i=1}^{R-1}(\lambda_iq_i)^{c_i(\pi)}.
]
Consequently,
[
\int_{[0,1]^{R-1}}
\left|\partial_{\lambda_1}\cdots\partial_{\lambda_{R-1}}
\prod_{B\in\pi}\widetilde M_B\right|d\lambda
=
\begin{cases}
\displaystyle\prod_{B\in\pi}|m_{|B|}|
\prod_iq_i^{c_i(\pi)},&c_i(\pi)\ge1\ \forall i,\\
0,&\text{otherwise.}
\end{cases}
\tag{1.2}
]
Here the derivative multiplicities disappear by
\(\int_0^1c\lambda^{c-1}d\lambda=1\).

Thus the formal moment-cumulant derivative has the integrated absolute bound
[
\sum_{\substack{\pi\in\Pi_R:\ c_i(\pi)\ge1\ \forall i}}
(|\pi|-1)!\prod_{B\in\pi}|m_{|B|}|
\prod_iq_i^{c_i(\pi)}
\le R^R\prod_iq_i.
\tag{1.3}
]
Indeed, (q_i^{c_i}\le q_i), and
\[
\sum_{k=1}^R(k-1)!S(R,k)
\le\sum_{k=1}^Rk^{R-1}\le R^R
\le4^R R^{R-2}.
\]
Since the consecutive-port path is a spanning tree of the one-link clique, (1.3) is bounded by (4^R) times the complete one-link support-tree polynomial.

This is a valid bound for the formal monomial model (1.1). It is not yet a Markov theorem.

## 2. Exact connected-component generating function

For the formal weights with (q_i=1), define
[
P_R(u)=\sum_{\pi\in\Pi_R}u^{|\pi|}
\prod_{B\in\pi}m_{|B|},
]
and let (C_R(u)) restrict the sum to partitions whose block-hull intervals cover all (R-1) cuts. Every partition decomposes uniquely at its uncovered cuts into consecutive components whose hulls cover all cuts internal to each component. Therefore, for ordinary generating functions,
[
P(z,u)=\sum_{R\ge0}P_R(u)z^R,\qquad
C(z,u)=\sum_{R\ge1}C_R(u)z^R,
]
one has
[
P(z,u)=1+C+C^2+\cdots=\frac1{1-C(z,u)},
\qquad
\boxed{C(z,u)=1-\frac1{P(z,u)}}.
\tag{2.1}
]
The partition polynomial obeys
[
P_0(u)=1,\qquad
P_R(u)=\sum_{j=1}^R
\binom{R-1}{j-1}m_j uP_{R-j}(u).
\tag{2.2}
]
The formal signed interval-covering sum is
[
\boxed{
S_R=\sum_{k=1}^R(-1)^{k-1}(k-1)![u^k]C_R(u).
}
\tag{2.3}
]
For the formal symmetric sequence (m_j=1) for even (j) and (0) for odd (j), the first values are
[
S_2=1,\ S_4=-1,\ S_6=8,\ S_8=-149,\
S_{10}=4778,\ S_{12}=-231205,\ S_{14}=15638140.
]
These are exact formal-combinatorial values only.

## 3. Four-port Markov counterexample to the monomial reduction

Let (X_i\in\{-1,+1\}) be a stationary symmetric two-state Markov chain with interpolated consecutive transition correlations
[
r_i=\lambda_iq_i,\qquad
\mathbb E[X_{i+1}\mid X_i]=r_iX_i.
]
For the four-row block (B=\{1,2,3,4\}), direct conditioning gives
[
\mathbb E[X_1X_2X_3X_4]
=r_1r_3,
\tag{3.1}
]
because (X_2^2=X_3^2=1). In particular, this block moment is independent of the middle transition parameter \(\lambda_2\), although the block hull (H(B)) contains cut 2.

The other nonzero moments needed for the fourth cumulant are
[
M_{12}=r_1,\quad M_{13}=r_1r_2,\quad
M_{14}=r_1r_2r_3,\quad
M_{23}=r_2,\quad M_{24}=r_2r_3,\quad M_{34}=r_3.
]
All odd centered moments vanish. Hence
[
\begin{aligned}
\kappa(X_1,X_2,X_3,X_4)
&=M_{1234}-M_{12}M_{34}
-M_{13}M_{24}-M_{14}M_{23}\\
&=-2r_1r_2^2r_3.
\end{aligned}
\tag{3.2}
]
Thus the full mixed derivative is carried by nontrivial partition terms, while the full block moment itself has zero derivative in \(\lambda_2\):
[
\partial_{\lambda_1}\partial_{\lambda_2}\partial_{\lambda_3}M_{1234}=0,
\qquad
\partial_{\lambda_1}\partial_{\lambda_2}\partial_{\lambda_3}\kappa
=-4q_1q_2^2q_3\lambda_2.
\tag{3.3}
]
At \(q_i=1,\lambda_i=1\), these are (0) and (-4), respectively.

This refutes the proposed inference that a block moment contains one factor \(\lambda_iq_i\) for every cut in its port hull. The *joint marginal law* of the selected ports remembers the intervening transition, but a particular product moment can annihilate that dependence through algebraic identities such as (X^2=1).

## 5. Exact coefficient-support consequence of disconnected cancellation

There is a more general algebraic fact available from the link-compressed interpolation, independent of the false monomial ansatz above. Let (E) be the finite set of consecutive-port transition edges in the union of the link paths, and write the actual cumulant polynomial as
[
\Phi(\lambda)=\sum_{\mathbf n\in\mathbb N^E}a_{\mathbf n}\lambda^{\mathbf n}.
]
The interpolation has finitely many transition parameters, and every transition kernel is affine in its own parameter, so this is a finite polynomial. Exact projective factorization gives
[
\Phi(\lambda)=0\quad\text{whenever }G_{\{e:\lambda_e>0\}}
\text{ is disconnected}.
]
If the support (H=\{e:n_e>0\}) of a multi-index is disconnected, set every parameter outside (H) to zero. The resulting polynomial in the variables indexed by (H) vanishes identically, since every such parameter assignment has disconnected active support. Therefore
[
\boxed{a_{\mathbf n}=0\quad\text{whenever }G_H\text{ is disconnected}.}
\tag{5.1}
]
Every nonzero Taylor monomial of the actual cumulant has connected transition-edge support. This is a coefficient-level consequence of the already established disconnected-support cancellation; it does not assume block moments are hull monomials.

If each row belongs to at most (m) links, then
[
|E|=\sum_e(|I_e|-1)\le\sum_e|I_e|\le mR,
]
so there are at most (2^{mR}) possible transition-edge supports. The unresolved part is the coefficient norm. Each occurrence of \(Q_e\) in a coefficient contributes a contraction bounded by \(w_e\); write the resulting operator estimate as
\[
|a_{\mathbf n}|\le b_{\mathbf n}\prod_{e\in\operatorname{supp}\mathbf n}w_e^{n_e},
\]
where \(b_{\mathbf n}\) records the normalized combinatorial/operator coefficient. Exponents can exceed one (the symmetric four-port example has exponent two on the middle edge). The missing estimate is a uniform bound on the sum of \(b_{\mathbf n}\) over exponent vectors with a fixed connected support, strong enough that
\[
\sum_{\mathbf n:\,G_{\operatorname{supp}\mathbf n}\text{ connected}}
 b_{\mathbf n}\prod_{e\in\operatorname{supp}\mathbf n}w_e^{n_e}
\le C_m^R\sum_{T\in\mathcal T(G_X)}\prod_{e\in T}w_e.
\]
For each connected support \(H\), choose a spanning tree \(T(H)\subseteq H\); since \(n_e\ge1\) on \(H\) and \(w_e\le1\), its temporal monomial is bounded by the tree weight. There are at most \(2^{mR}\) possible supports, so a per-support exponential bound on \(\sum_{\operatorname{supp}\mathbf n=H}b_{\mathbf n}\) would suffice. This is the precise remaining coefficient-resummation target; (5.1) alone does not establish it.

## 6. Corrected frontier

What survives:

- The interval-covering partition family is the right combinatorial family for the formal monomial model.
- The consecutive-component decomposition and (C=1-P^{-1}) identity are exact.
- The formal model has an exponential coefficient relative to the complete one-link tree count.

What does not follow:

- General Markov block moments are not hull monomials; even the symmetric two-state chain violates that representation at four ports.
- The formal connected-component generating function therefore cannot yet be substituted into the actual differentiated moment-cumulant sum.
- A valid extension must retain the full operator-valued subset expansion of each block moment, including reset-separated left/right factors, and resum their Möbius signs before taking absolute values.
- No multi-link (C_m^R) support-localized cumulant-tree estimate is established here.

This audit is a formal resummation identity plus a counterexample to its naive Markov application. It does not promote any P0–P5 gate and does not close the Yang–Mills mass-gap proof.
