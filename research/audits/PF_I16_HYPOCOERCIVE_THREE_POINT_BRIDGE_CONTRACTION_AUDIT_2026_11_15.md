# PF-I16 — Audit of the proposed hypocoercive three-point bridge contraction

**Date:** 2026-11-15  
**Status:** The proposed Lemma 3 bound is REFUTED, including for reversible Ornstein–Uhlenbeck dynamics. The bridge-variance differential identity and hypocoercive transfer require substantial reformulation. No multi-cut or PF-I16 gate is promoted.  
**Scope:** Three-point conditional expectation for a stationary continuous-time process; this audit does not settle the distinct continuous-time multi-cut HGR conjecture for arbitrary interlaced observation sets.

## 1. Proposed statement and immediate endpoint obstruction

The proposed target is
\[
\rho_{\max}( (X_0,X_T),X_t)
\le \sqrt{1-e^{-2\lambda\min(t,T-t)}},\qquad 0<t<T.
\tag{1.1}
\]
This cannot hold for any \(\lambda>0\). Since \(X_0\) is one of the conditioning variables, data processing gives
\[
\rho_{\max}((X_0,X_T),X_t)
\ge \rho_{\max}(X_0,X_t).
\tag{1.2}
\]
For any stochastically continuous stationary process with nondegenerate observable(s) that are continuous in probability, the right side can approach one as \(t\downarrow0\). The right side of (1.1), in contrast, approaches zero. The same obstruction occurs as \(t\uparrow T\), using \(X_T\).

This is an endpoint geometry issue, not a non-normal transient-growth issue. It already occurs in a reversible process.

## 2. Exact reversible Ornstein–Uhlenbeck calculation

Let
\[
dX_s=-aX_s\,ds+\sqrt{2a}\,dW_s,\qquad a>0,
\]
in its stationary law \(N(0,1)\). The generator is
\[
\mathcal L f=a(f''-xf'),
\]
self-adjoint in \(L^2(N(0,1))\), with spectral gap \(a\). Thus \(\mathcal A=0\); no hypocoercive correction is needed.

Write \(r=e^{-at}\), \(s=e^{-a(T-t)}\), and \(u=e^{-aT}=rs\). The covariance matrix of the endpoint vector \((X_0,X_T)\) is
\[
\Sigma_E=\begin{pmatrix}1&u\\u&1\end{pmatrix},
\]
and its covariance with \(X_t\) is \((r,s)\). For jointly Gaussian variables, the maximal correlation between a scalar Gaussian and a Gaussian vector is the multiple correlation coefficient. Hence
\[
\rho_{\max}^2((X_0,X_T),X_t)
=(r,s)\Sigma_E^{-1}\binom r s
=\frac{r^2+s^2-2u rs}{1-u^2}.
\]
Equivalently,
\[
\boxed{
\rho_{\max}^2((X_0,X_T),X_t)
=1-\frac{(1-e^{-2at})(1-e^{-2a(T-t)})}{1-e^{-2aT}}.
}
\tag{2.1}
\]
The bridge conditional variance is exactly
\[
\boxed{
\mathbb E[\operatorname{Var}(X_t\mid X_0,X_T)]
=\operatorname{Var}(X_t\mid X_0,X_T)
=\frac{(1-e^{-2at})(1-e^{-2a(T-t)})}{1-e^{-2aT}}.
}
\tag{2.2}
\]
In particular,
\[
\rho_{\max}((X_0,X_T),X_t)\ge e^{-at}\to1
\quad(t\downarrow0),
\]
whereas (1.1) tends to zero. This is a strict contradiction for sufficiently small positive \(t\), for every fixed \(\lambda>0\).

For fixed T, the bridge conditional variance in (2.2) vanishes at both endpoints and is maximal in the interior. The maximal correlation has the opposite profile: it is one at both endpoints and smallest at the midpoint. It is therefore not a quantity that decays monotonically as the middle time moves away from either endpoint.

## 3. Correct operator/variance identity

For centered \(f\in L^2(\pi)\), define
\[
m_f(X_0,X_T)=\mathbb E[f(X_t)\mid X_0,X_T].
\]
Stationarity and the law of total variance give
\[
\mathbb E[\operatorname{Var}(f(X_t)\mid X_0,X_T)]
=\|f\|_2^2-\|m_f\|_{L^2(\pi_{0,T})}^2.
\tag{3.1}
\]
Consequently,
\[
\rho_{\max}^2((X_0,X_T),X_t)
=\sup_{f\in L_0^2(\pi),\,f\ne0}
\frac{\|m_f\|_2^2}{\|f\|_2^2}
=1-\inf_{f\in L_0^2(\pi),\,f\ne0}
\frac{\mathbb E[\operatorname{Var}(f(X_t)\mid X_0,X_T)]}{\|f\|_2^2}.
\tag{3.2}
\]
Thus an upper bound on maximal correlation requires a **uniform lower bound** on bridge conditional variance over the relevant observable class. A decay estimate for \(P_t-\Pi\) alone does not supply such a lower bound. In degenerate or deterministic systems the infimum in (3.2) can be zero, giving maximal correlation one.

The displayed definition of \(\mathcal E_{0,T}f(x_0)\) in the proposal also suppresses its dependence on \(x_T\). The bridge expectation is a function of both endpoints:
\[
(\mathcal E_{0,T}f)(x_0,x_T)
=\mathbb E[f(X_t)\mid X_0=x_0,X_T=x_T].
\]

## 4. Bridge evolution is not the original semigroup evolution

For a diffusion with generator
\[
\mathcal L f=b\cdot\nabla f+\tfrac12 a:\nabla^2 f
\]
and a sufficiently regular transition density, the bridge from \(x_0\) to \(x_T\) has a time-inhomogeneous Doob-transform generator (for \(s<T\))
\[
\mathcal L_s^{x_0,x_T} f(x)
=\mathcal L f(x)
+a(x)\nabla\log p_{T-s}(x,x_T)\cdot\nabla f(x).
\tag{4.1}
\]
The additional drift depends on the terminal endpoint and becomes singular in typical diffusion coordinates as \(s\uparrow T\). The bridge law is not governed by the stationary generator \(\mathcal L\) alone.

Accordingly, the proposed differential identity
\[
v'(t)=-2\langle\mathcal S\nabla f_t,\nabla f_t\rangle
+\text{antisymmetric terms}
\]
is not a general identity as written. It needs a precise state space, bridge density, time-dependent bridge generator, observable evolution, and endpoint-integrability conditions. For a general Markov process there may be no gradient or carré-du-champ structure at all. Even for diffusions, differentiating the bridge conditional variance includes the time dependence of the bridge generator and bridge law.

The OU calculation is a direct diagnostic: its bridge conditional variance increases from zero and then decreases to zero. There is no global monotone decay of this variance along the bridge.

## 5. Hypocoercivity decomposition: what is missing

The formal decomposition
\[
\mathcal S=\tfrac12(\mathcal L+\mathcal L^*),\qquad
\mathcal A=\tfrac12(\mathcal L-\mathcal L^*)
\]
requires appropriate common domains/closures and an invariant reference measure. It does not by itself produce a coercive modified norm. A first-order \(\Gamma\), commutator estimate, or modified entropy is model-specific; it must be defined on a specified function space and shown to control the relevant norm.

More importantly, hypocoercivity for the unconditioned semigroup \(P_t\) is not automatically hypocoercivity for the endpoint-conditioned, time-inhomogeneous bridge family (4.1), nor does it imply the uniform lower bound in (3.2). A valid bridge estimate would need constants uniform in endpoints (or an explicitly averaged endpoint norm), control of the singular terminal drift, and a precise observable class.

## 6. Recommended repair to the research program

1. **Withdraw (1.1) and the stated Lemma 3.** The proposed right side has the wrong endpoint limit.
2. **Use OU as a mandatory calibration case** for any replacement bridge inequality. It must reproduce (2.1) or a valid upper bound consistent with it.
3. **Separate bridge geometry from interlaced-block mixing.** The three-point quantity \(\rho_{\max}((X_0,X_T),X_t)\) is not a decaying mixing coefficient near the endpoints. It should not be used as a direct surrogate for the HGR coefficient between two arbitrary interlaced observation sigma-fields.
4. **If a bridge method is pursued**, formulate a time-inhomogeneous Doob-transform estimate and prove a uniform lower bound on conditional variance (equivalently an upper bound on HGR) for a restricted observable class, with explicit dependence on both \(t\) and \(T-t\). State endpoint degeneracy explicitly.
5. **For the PF-I16 multi-cut problem**, return to a cut-profile/cumulant formulation that retains all temporal crossing intervals and original row-link labels. A three-point bridge estimate, even if proved in a corrected form, would still require a separate tensorization/conditional-cumulant argument to yield the required support-labelled spanning tree.

## 7. Disposition

- Proposed bridge bound (1.1): **REFUTED**, by reversible stationary OU.
- Exact OU bridge formula (2.1)–(2.2): **ESTABLISHED**.
- General bridge-variance differential identity as stated: **NOT ESTABLISHED / INSUFFICIENTLY SPECIFIED**.
- Transfer of unconditioned hypocoercivity to endpoint-conditioned bridge HGR: **OPEN**.
- Continuous-time multi-cut HGR inequality for arbitrary interlaced observation sets: **OPEN**.
- Multi-time super-row cumulant tree with original-row support bonds: **OPEN**.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.


## 8. Corrected three-point calibration: retain both cuts

The failed square-root expression (1.1) should not be confused with the distinct two-cut HGR target. For the three-point pattern \(S=\{0,T\}\), \(R=\{t\}\), the relevant candidate is
\[
\rho_{\max}((X_0,X_T),X_t)
\le \tanh\!\bigl(\operatorname{arctanh}q_t+
\operatorname{arctanh}q_{T-t}\bigr)
=\frac{q_t+q_{T-t}}{1+q_tq_{T-t}},
\tag{8.1}
\]
where \(q_s=\|P_s-\Pi\|_{L^2(\pi)\to L^2(\pi)}\). Under a semigroup gap estimate, one may substitute \(q_s\le e^{-\Delta_0s}\) on the right, since the displayed expression is increasing in each argument. Unlike (1.1), (8.1) tends to one at either endpoint.

For stationary unit-variance OU, put \(r=e^{-at}\), \(s=e^{-a(T-t)}\). The exact value from (2.1) is
\[
\rho_{\rm OU}^2=\frac{r^2+s^2-2r^2s^2}{1-r^2s^2}.
\]
The two-cut right side is \(c=(r+s)/(1+rs)\), and direct algebra gives
\[
c^2-\rho_{\rm OU}^2
=\frac{2rs(1-r^2)(1-s^2)}{(1-rs)(1+rs)^2}\ge0.
\tag{8.2}
\]
Thus OU satisfies (8.1), strictly for \(0<r,s<1\). Equivalently, the OU bridge conditional variance is larger than the lower bound
\[
\frac{(1-q_t^2)(1-q_{T-t}^2)}
{(1+q_tq_{T-t})^2}\,\|f\|_2^2
\]
for every centered observable, with equality in the HGR variational characterization only in limiting/degenerate cases.

**Status:** (8.1) is a corrected and well-calibrated candidate for continuous-time semigroups, not a theorem. The previously recorded strictly positive discrete-time counterexample refutes the analogous assertion for arbitrary stationary discrete-time kernels. Whether continuous-time embeddability and generator structure suffice remains OPEN. Even a proof of (8.1) for the three-point pattern would not by itself establish the arbitrary interlaced multi-time or multi-row cumulant theorem needed for PF-I16.


## 9. Finite CTMC obstruction to the stronger bridge-to-unconditioned contraction

A separate finite continuous-time test shows why it is not enough to assume that endpoint-conditioned bridge correlations are bounded by the unconditioned semigroup norm. Consider the irreducible three-state generator (off-diagonal rates are strictly positive)
\[
Q=10^{-6}\begin{pmatrix}
-187844&167637&20207\\
45820559&-45891980&71421\\
7805983&12454510&-20260493
\end{pmatrix},
\]
with exact stationary law
\[
\pi=\left(
\frac{464452312993715}{466746007289039},
\frac{3648076548611}{933492014578078},
\frac{939312042037}{933492014578078}
\right).
\]
At gaps \(t=0.064\) and \(s=0.078\), numerical matrix exponentials and normalized-joint SVDs give
\[
q_t=\|e^{tQ}-\Pi\|_{2\to2}\approx0.2787927451,
\quad
q_s\approx0.2104539989,
\]
but
\[
\sup_z\rho_{\max}(X_0,X_t\mid X_T=z)\approx0.4764845757,
\quad
\sup_x\rho_{\max}(X_T,X_t\mid X_0=x)\approx0.4571207077.
\]
Thus both endpoint-conditioned bridge HGR coefficients can substantially exceed their corresponding unconditioned semigroup contractions, even for a finite irreducible continuous-time Markov chain.

For the full three-point coefficient, the same calculation gives
\[
\rho_{\max}((X_0,X_T),X_t)\approx0.3771389403.
\]
It exceeds the stronger but unjustified substitution
\[
\sqrt{1-(1-q_t^2)(1-q_s^2)}\approx0.3443453990,
\]
while remaining below the weaker two-cut tanh expression
\[
\tanh(\operatorname{arctanh}q_t+\operatorname{arctanh}q_s)
\approx0.4621320481.
\]

This is a numerical finite-state witness (the generator and stationary law are rational; exponentials and singular values are evaluated numerically). It does **not** refute the tanh two-cut continuous-time conjecture. It does refute the proposed shortcut of bounding each subjective/endpoint-conditioned HGR coefficient by the unconditioned \(L^2\) semigroup norm, and it shows why the sharp N-against-1 tensorization theorem cannot be fed the unconditional \(q_t,q_s\) without a separate conditional estimate.

The reproducible NumPy verifier is `research/verification/verify_pf_i16_ctmc_bridge_conditional_hgr_obstruction.py`.
