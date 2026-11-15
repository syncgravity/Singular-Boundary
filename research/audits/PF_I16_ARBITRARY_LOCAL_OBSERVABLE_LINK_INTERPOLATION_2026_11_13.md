# PF-I16 — Arbitrary local-observable link interpolation and radial pair contraction

**Date:** 2026-11-13  
**Status:** cross-split quasi-factorization is ESTABLISHED for arbitrary bounded local multiplication observables under the independent stationary link-path and uniform L2-gap hypotheses. The earlier row-factor-only scope restriction is superseded by Section 2 below. The all-orders support-sensitive cumulant tree and quantum cluster expansion remain OPEN.

## 1. Correction and main result

The earlier scope audit asserted that link-by-link path interpolation applied only to rank-one row factors. That restriction was unnecessary. The one-link covariance lemma allows an arbitrary bounded one-time multiplication function at each observation time. After conditioning on every other link path, **any bounded local multi-link row observable becomes exactly such a one-time function of the interpolated link**.

Let (I=J\sqcup K), let (X_i) be the finite link support of row (i), and let
[
F_i:\prod_{e\in X_i}G\longrightarrow\mathbb C
]
be any bounded measurable local multiplication observable. No tensor-product or smoothness assumption is imposed. For each shared link (e), write
[
J_e=\{i\in J:e\in X_i\},\qquad K_e=\{i\in K:e\in X_i\}.
]
Under the stationary independent link-path hypotheses and the one-link interlaced-time covariance lemma of the companion interpolation audit, the following holds:
[
\boxed{
\left|\mathbb E\prod_{i\in I}F_i(X(t_i))
-\mathbb E\prod_{i\in J}F_i(X(t_i))\,
 \mathbb E\prod_{i\in K}F_i(X(t_i))\right|
\le 2|I|\prod_{i\in I}\|F_i\|_\infty
\sum_{i\in J,j\in K}|X_i\cap X_j|e^{-\Delta_0|t_i-t_j|}.
}
\tag{1.1}
]
Thus actual face and face-pair insertions do not need a Peter–Weyl projective tensor decomposition to enter the link-interpolation QF estimate. The radial/tensor calculation below is an independent strengthening of the local activity bound, not a prerequisite for (1.1).

## 2. Proof for arbitrary bounded local observables

Use the same whole-path coupling interpolation as in the link-by-link audit. For each shared link (e), its two side paths have law
[
\Gamma_{e,\lambda_e}
=\lambda_e\,\mathcal L(X_e,X_e)
 +(1-\lambda_e)\,\bigl(\mathcal L(X_e)\otimes\mathcal L(X'_e)\bigr).
]
The selector is sampled once for the whole path. The joint law over distinct links is a product.

Fix (e) and condition on all path pairs on links (e'\ne e); denote this conditioning data by \(\omega\). For a row (i\) whose support contains (e), define the one-time function
[
f_{i,e}^{\omega}(x)
=F_i\bigl((z_{i,e'}^{\omega}(t_i))_{e'\ne e},,z_{i,e}=x\bigr),
]
where (z_{i,e'}^{\omega}) is the J- or K-side path selected by the side of row (i). This is a deterministic bounded function once \(\omega\) is fixed, and
[
\|f_{i,e}^{\omega}\|_\infty\le\|F_i\|_\infty.
	ag{2.1}
]
Rows not containing (e) contribute a scalar multiplier (C_{-e}^{\omega}) with
[
|C_{-e}^{\omega}|
\le\prod_{i:e\notin X_i}\|F_i\|_\infty.
	ag{2.2}
]

Differentiating the affine path-law mixture in \(\lambda_e\), conditional on \(\omega\), gives exactly
[
\partial_{\lambda_e}\mathcal F
=\mathbb E_{\omega}\!\left[
C_{-e}^{\omega}\,
\operatorname{Cov}_{\nu_e}\!\left(
\prod_{i\in J_e}f_{i,e}^{\omega}(X_{t_i}),
\prod_{j\in K_e}f_{j,e}^{\omega}(X_{t_j})
\right)\right].
	ag{2.3}
]
The covariance is on the *single* link path. Apply the established interlaced-time lemma to the (n_e=|J_e|+|K_e|\) factors. Since (n_e\le|I|), its coefficient is at most (2|I|). Equations (2.1)–(2.2) give
[
|\partial_{\lambda_e}\mathcal F|
\le 2|I|\prod_{i\in I}\|F_i\|_\infty
\sum_{i\in J_e,j\in K_e}e^{-\Delta_0|t_i-t_j|}.
	ag{2.4}
]
Integrate the exact coordinatewise interpolation identity from all links copied to all links shared, then sum over (e). Each cross-row pair is counted once for every shared link, giving (1.1).

The proof uses only:
- product independence of the link path pairs across links;
- the stationary one-link Markov L2 contraction;
- boundedness of each full local observable (F_i);
- the fact that each row is evaluated at one time (t_i).

It does **not** use factorization of (F_i) across links, differentiability of (F_i), a projective tensor norm, or a smoothness estimate.

For actual PF-I16 insertions, (v_f) has support of at most four links and (v_{fg}) has support of at most eight. Thus (1.1) applies directly, with the link-multiplicity bond shown there. The crude indicator form follows with overlap multiplicity at most eight. This closes the actual-insertion cross-split QF subgate under the stated reference-process hypotheses.

## 3. Radial derivative bound in the plaquette coordinate

There is also a quantitative bound for the non-polynomial radial derivative. Put
[
p=\cos\theta,\qquad q(\theta)=s_\beta'(\theta),\qquad
h(\theta)=q(\theta)^2+\lambda_\beta,
]
where the corrected radial equation and weighted-mean identity are
[
q'+2\cot\theta\,q=-4(q^2+\beta\cos\theta+\lambda_\beta),
\qquad
\lambda_\beta=-\frac{\int_0^\pi\sin^2\theta\,q(\theta)^2d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}.
]
The already established bound (-2\beta\le q\le0) gives
[
|h|\le4\beta^2,qquad
J(\theta)=\int_0^\theta\sin^2u\,h(u)\,du,qquad J(\pi)=0.
]
Integrating the radial equation yields
[
q(\theta)=-\frac43\beta\sin\theta
-\frac{4J(\theta)}{\sin^2\theta}.
	ag{3.1}
]

Let (I(\theta)=\int_0^\theta\sin^2u\,du). For (0\le\theta\le\pi/2),
[
I(\theta)\le\frac\pi4\sin^3\theta.
	ag{3.2}
]
Indeed, the difference on the right minus the left vanishes at both endpoints; its derivative is
(sin^2\theta((3\pi/4)\cos\theta-1)), which changes sign exactly once from positive to negative. Reflecting about \(\pi/2\) gives the corresponding bound for the upper tail. Since (J(\pi)=0), use the lower or upper endpoint representation according to which is shorter:
[
|J(\theta)|
\le4\beta^2\min\{I(\theta),I(\pi)-I(\theta)\}
\le\pi\beta^2\sin^3\theta.
	ag{3.3}
]
For (g(p)=s_\beta(\arccos p)), (g'(p)=-q(\theta)/\sin\theta). Combining (3.1)–(3.3) gives the uniform endpoint-regular bound
[
\boxed{
\|g'\|_{L^\infty([-1,1])}
\le\frac43\beta+4\pi\beta^2.
}
\tag{3.4}
]
This is a scalar (L^\infty) derivative bound, not a projective tensor-norm estimate. Under (1.1), no such projective norm is needed for cross-split QF.

## 4. Contract the shared-link Lie-algebra index first

For (p_f(H_f)=\tfrac12\operatorname{Tr}H_f=\cos\theta_f), a unit tangent in the radius-two SU(2) metric gives
[
\nabla_e p_f=\frac12\sin\theta_f\,n_{f,e},
\qquad |n_{f,e}|=1,
]
where (n_{f,e}) is expressed in the original shared-link frame; the orientation sign is included in (n_{f,e}). Because (s_f(H_f)=g_f(p_f(H_f))) and (g_f'=-q_f/\sin\theta_f),
[
\nabla_e s_f=-\frac12q_f(\theta_f)n_{f,e}.
	ag{4.1}
]
Consequently the complete three-dimensional Lie-algebra contraction is exactly
[
\boxed{
2a_e\langle\nabla_e s_f,\nabla_e s_g\rangle
=\frac{a_e}{2}q_f(\theta_f)q_g(\theta_g)
\langle n_{f,e},n_{g,e}\rangle.
}
\tag{4.2}
]
The contraction is performed before absolute values. Since \(|q_f|\le2\beta_f\),
[
\left|2a_e\langle\nabla_e s_f,\nabla_e s_g\rangle\right|
\le2a_e\beta_f\beta_g.
]
There are at most four common boundary links, and the recorded allocation gives
(a_e\beta_f\beta_g\le16b_0^2/a_0). Therefore
[
\boxed{\|v_{fg}\|_\infty\le128\,b_0^2/a_0,}
\tag{4.3}
]
improving the earlier (512b_0^2/a_0) bound by a factor of four. This estimate is pointwise and volume-independent under the existing incidence/allocation hypotheses.

With at most 28 neighboring faces per face, the revised conservative per-face activity is
[
z_f=32b_0+3584\,b_0^2/a_0.
]
At (x=b_0/a_0=1/50000) and \(\Delta_0=3a_0/4\),
[
\frac{z_f}{\Delta_0}=0.0008552448,
\qquad
58\frac{z_f}{\Delta_0}=0.0496041984.
	ag{4.4}
]
If one assumes the same still-unproved single-tree/marked-root counting used in the prior candidate, its arithmetic candidate is
(4(2.7183)(58z_f/\Delta_0)<0.53936). This is only an arithmetic diagnostic; it is not a KP theorem.

## 5. Gate disposition

- Exact face/pair centering: **ESTABLISHED** under the recorded product-Haar geometry.
- One-link interlaced-time covariance: **ESTABLISHED** under the stationary Markov L2-gap hypothesis.
- Cross-split QF for arbitrary bounded local multiplication observables: **ESTABLISHED** by (2.1)–(2.4).
- Actual face/pair cross-split QF: **ESTABLISHED** under the same hypotheses, with link-multiplicity bonds.
- Radial derivative (d s_f/dp_f) bound (3.4): **ESTABLISHED** under the corrected radial ODE and endpoint regularity.
- Contracted pair bound (4.3): **ESTABLISHED** under the radius-two metric and recorded allocation/incidence hypotheses.
- All-orders support-sensitive joint cumulant tree: **OPEN**. The QF estimate is a candidate input to a weighted-dependency-graph/tree theorem, but the needed theorem and its constants must be proved in the exact form used by the space-time summation.
- Marked-root/cluster sum and quantum KP convergence: **OPEN**.
- Interacting-vacuum Poincare inequality and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.
