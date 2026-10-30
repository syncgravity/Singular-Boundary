# The Singular Boundary — Volume-uniform SU(2) magnetic Taylor remainder and quartic-fluctuation obstruction

**Research date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Scope:** exact quantitative result in the **full shared-edge Gaussian tangent vacuum** on arbitrary complete rhombus disks of growing face count; the perturbed observable is the **exact nonlinear SU(2) magnetic potential evaluated on exponential-coordinate tangent fields**. This is not the actual nonlinear interacting ground-state law. The result is a rigorous obstruction to an *uncentered or merely O(1)-bounded global perturbation-remainder argument*, not an impossibility theorem for local/renormalized vacuum comparison, norm-resolvent convergence, or the mass gap.

## 1. Precise models and preceding input

For an embedded simply connected edge-to-edge rhombus disk with F faces, four edges per face, and edge incidence at most two, let B be the oriented face-edge incidence matrix. All electric coefficients are equal to a>0; the exact tangent kinetic matrix is M=a B B^T with M_ff=4a and 0<M<=8a I, a symmetric M-matrix. For the physical trajectory let common magnetic coupling be b_h=beta/h² with beta>0. The exact tangent oscillator, including all shared edges, has vacuum probability on y=(y_f) in (R³)^F with independent colors and cross-face covariance

  E_G[y_f^alpha y_g^gamma] = delta_(alpha,gamma) s_fg,
  s = sqrt(2/beta) sqrt(M).

This is the exact rescaling x_f=sqrt(h)y_f of the tangent oscillator with unscaled covariance sqrt(2/b_h) sqrt(M). It is **not** an assumption on the true SU(2) Wilson vacuum. By the previously audited MF-2 signed-matrix theorem, K=(sqrt(M))∘(sqrt(M)) obeys

  (105a/64)||q||² <= q^T K q <=4a||q||².

The covariance matrix s obeys, uniformly in F, the following identities and bounds:

  t_f := s_ff in [2sqrt(a/beta), sqrt(8a/beta)],
  ||s||_op <=4sqrt(a/beta),
  sum_g s_fg²=(s²)_ff=8a/beta,
  q^T(s∘s)q >= (105a/(32beta))||q||².

The lower t_f bound follows from sqrt(M)>=M/sqrt(8a); the upper bound follows by diagonal Jensen. No translation invariance or square-grid replacement is used in the theorem.

## 2. Exact nonlinear magnetic potential in Gaussian exponential coordinates

For a single SU(2) face holonomy exp(i sqrt(h) y_f·sigma/2), its fundamental Wilson deficit is

  d_h(y_f)=1-cos(sqrt(h)|y_f|/2).

The exact nonlinear magnetic energy and its quadratic tangent approximation differ by the real multiplier

  R_(h,q)(y) := (beta/h²)sum_f q_f[d_h(y_f)-h|y_f|²/8].

The q=1 choice is the total magnetic remainder; arbitrary real q produces a weighted local remainder. The cosine is meaningful on all R³ because the exponential map defines a group element; this global extension does not claim the principal logarithm is a global injective chart or that the Gaussian tangent distribution equals Haar.

Taylor's theorem gives the **exact global** decomposition

  R_(h,q) = -(beta/384) sum_f q_f |y_f|⁴ + E_(h,q),

where each residual summand e_h(r) satisfies, for all r>=0,

  |e_h(r)| <= (beta/46080) h r⁶,
  |e_h'(r)| <= (beta/7680) h r⁵.

The derivative estimate follows from |sin z-z+z³/6|<=|z|⁵/120, valid for all real z. Every single-site Gaussian moment E|y_f|^10 is bounded by a constant depending only on a/beta.

## 3. Theorem UR-1 — Uniform centered remainder error in the **exact tangent vacuum**

Let q=(q_f) be any real vector. The Gaussian Poincare inequality on R^(3F), using the full cross-face covariance s⊗I₃ and the above derivative bound, gives

  Var_G(E_(h,q)) <= ||s||_op E_G[||grad E_(h,q)||²]
                  <= C_(a,beta) h² sum_f q_f².       (UR-1)

The constant is independent of F, geometry, q and h in (0,1]. The ordinary absolute bound also gives |E_G E_(h,q)|<= C h sum|q_f|; this is not the same as its centered fluctuation norm.

**Proof:** The gradient component at f has magnitude <=C h |q_f||y_f|⁵. Square and sum over f: no mixed derivatives occur in this expression, even though the Gaussian y_f are correlated. Bound each tenth moment by its t_f upper bound; multiply by the uniform operator norm ||s||. QED.

## 4. Theorem UR-2 — Exact Gaussian quartic covariance including every shared-link interaction

For any centered isotropic jointly Gaussian three-vectors y_f,y_g with variances t_f,t_g and cross-color covariance s_fg, Wick's theorem yields

  E_G |y_f|⁴ = 15 t_f²,
  Cov_G(|y_f|⁴,|y_g|⁴) = 600 t_f t_g s_fg² +120 s_fg⁴. (UR-2)

The two terms are respectively the second and fourth Wiener-chaos contributions. The complete covariance matrix is positive semidefinite, including both terms, for arbitrary F. In particular

  Var_G(S_q), S_q:=sum_f q_f|y_f|⁴,
  = 600 (D_t q)^T(s∘s)(D_t q) + 120 q^T(s∘s∘s∘s)q,

with D_t=diag(t_f). Schur's product theorem proves that both forms are nonnegative. By the signed MF-2 lower bound, t_f²>=4a/beta, and row-sum upper bounds, one obtains, **uniformly in F and for all signed q**,

  (7875 a²/beta²) sum q_f² <= Var_G(S_q)
            <= (46080 a²/beta²) sum q_f².          (UR-3)

The lower constant is 600*(4a/beta)*(105a/(32beta))=7875 a²/beta². For the upper bound, use tmax²<=8a/beta and sum_g s_fg²=8a/beta. Further |s_fg|²<=t_ft_g<=8a/beta, so the fourth-chaos row sum is at most 64 a²/beta²; the first-chaos-matrix row sum contributes at most 600*64 a²/beta². Total 46080 a²/beta².

Taking the coefficient of the quartic magnetic remainder, UR-3 becomes

  **(875a²/16384) ||q||² <= Var_G[(beta/384)S_q]
                                <= (5a²/16) ||q||².** (UR-4)

All estimates hold for arbitrary real weights and complete Penrose face graphs; only electric coefficient uniformity enters the current explicit signed lower bound. In particular the residual cannot be suppressed by distant-face signed cancellations in this reference vacuum.

## 5. Theorem UR-3 — Extensive correction in simultaneous Penrose refinement

Apply the reverse triangle inequality to centered L² random variables, UR-1 and UR-4. Writing c0=875a²/16384, C0=5a²/16 and C1=C_(a,beta),

  (sqrt(c0)-sqrt(C1)h)||q|| <= sqrt[Var_G R_(h,q)]
                            <= (sqrt(C0)+sqrt(C1)h)||q||.  (UR-5)

Therefore, for h small enough, there are positive c,C independent of h,F and signed weights q with

  **c sum_f q_f² <= Var_G R_(h,q) <= C sum_f q_f².** (UR-6)

For q_f=1 and a fixed positive physical area with F_h=Theta(h^-2), the mean satisfies

  E_G R_(h,1)= -(15beta/384)sum_f t_f² + O(h F_h)
            = -Theta(F_h) = -Theta(h^-2),          (UR-7)

while

  **Var_G R_(h,1)=Theta(F_h)=Theta(h^-2),**
  **StdDev_G R_(h,1)=Theta(sqrt(F_h))=Theta(h^-1).** (UR-8)

For a signed smooth fixed-area test with h²sum q_f² bounded above and away from zero, the same variance order holds, even if the mean cancels. Thus h(R_(h,q)-E_G R_(h,q)) has uniformly bounded, nonvanishing variance (between fixed positive constants).

At the same time, the Gaussian tangent *quadratic* magnetic energy is of order F_h/h=Theta(h^-3) in expectation. The exact nonlinear magnetic quartic correction is relatively O(h) in its mean, yet its **absolute** mean and centered standard deviation diverge. This is a specific quantitative reason why a global naive perturbative comparison requiring an O(1) remainder in the tangent vacuum cannot be valid at F_h~h^-2, b_h~h^-2. It is **not** a proof that local observables cannot be compared after counterterms, nor that the two full quantum vacua are asymptotically singular.

## 6. Integrity and exact scope

**Newly proved:** UR-1 uniform centered Taylor-error gradient estimate in the exact shared-edge tangent vacuum; UR-2 Wick fourth covariance retaining every shared-edge pair; UR-3 extensive magnetic Taylor remainder and a signed cancellation-resistant variance bound independent of face count. The nonlinear SU(2) cosine function is used exactly, but it is evaluated under a **Gaussian tangent ground-state distribution**; no result in UR-1 through UR-8 is asserted as a variance under the true nonlinear Wilson ground state.

**Not proved:** a regulator-uniform nonlinear-to-Gaussian comparison of actual vacuum measures, covariance matrices or Euclidean dynamics; a uniform operator norm or norm-resolvent approximation with or without renormalization; nontrivial fixed-time physical source survival; a positive all-sector physical gap; original Stage7/26 action identity or full continuum reconstruction.

**Refined next gate:** compare *centered source correlation functions* or local relative-energy forms after accounting for an extensive quartic counterterm; do not seek an uncentered O(1) global Taylor remainder. A potentially useful quantitative goal is a *source-projected* covariance bound independent of F, with a separate Euclidean-time estimate. A global total-variation approximation is neither assumed nor established. The historical Stage7/Stage26 and temporal Q14 provenance remain a separate verification obligation.

## 7. Deterministic verification

`verify_quartic_remainder.py` verifies the exact SU(2) cosine Taylor coefficients, derives the three-color Gaussian quartic covariance by symbolic differentiation of its moment-generating function, checks the signed-kernel constants, reconstructs the authentic three-rhombus ten-edge Z⁵ Penrose **spatial** fixture, and tests the bounds on three-face and growing square-grid incidence-class surrogate matrices (which are **not** asserted to be Penrose fixtures). It uses no Monte Carlo and modifies no historical data.
