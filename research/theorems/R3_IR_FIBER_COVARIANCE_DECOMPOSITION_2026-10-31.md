# R3-IR — Conditional covariance decomposition of the exact Wilson fiber-energy slope

**2026-10-31.** Exact finite-volume identity; no uniform signed-current bound.

Let the exact positive deleted-face Wilson ground state be Ω=Ψ(u)Φ, where u=arccos p_f and E_μ[Φ²|u]=1. The angular face-gradient lift Y from `R3_IR_ANGULAR_FIBER_TRANSPORT_2026-10-31.md` has Yu=1 and d/du E_μ[J|u]=E_μ[YJ|u]. Define conditional probability ν_u=Φ²μ_u, h=logΦ, k=Σ_(e,a) a_e(X_(e,a)h)², e=k+V_- and U(u)=E_(ν_u)[e].

**FC-1 (exact covariance decomposition).** At every interior angle:

`U'(u)= E_(ν_u)[Yk+YV_-] + 2 Cov_(ν_u)(k+V_-,Y logΦ)`.

Since differentiating E_μ[Φ²|u]=1 gives E_(ν_u)[Y logΦ]=0, the nonadiabatic remainder in the archived angular transport theorem is exactly

**`R(u)=E_(ν_u)[Yk]+2 Cov_(ν_u)(k+V_-,Y logΦ)`.**

Proof: Differentiate the conditional expectation of Φ²e with the exact material derivative, apply the product rule Y(Φ²e)=Φ²Ye+2Φ²eYlogΦ, and use conditional normalization. The material kinetic term includes the original-link commutators, since `Yk=2Σ a_e (Xh)(X(Yh)−[X,Y]h)`; it must not be discarded.

**FC-2 (conditional fluctuation bound).** Write M(u)=E_(ν_u)|Yk|, σ_e²=Var_(ν_u)(k+V_-), σ_h²=Var_(ν_u)(YlogΦ). Then

**`[-R(u)]_+≤M(u)+2σ_e(u)σ_h(u)`.**

The archived angular magnetic force bound and fiber-slope maximum principle imply the conditional sufficient estimate

**`𝔗_f≤(π/A_f)[B_f^inc+sup_(0<u<π/2)(M(u)+2σ_e(u)σ_h(u))]`.**

Here B_f^inc=(1/A_f)Σ_(e∈∂f)a_e Σ_(g≠f:e∈∂g)b_g. All terms retain the true nonlinear conditional Wilson state. No regulator-uniform control of M or the two conditional fluctuations is proved; the direct magnetic bound can itself scale as h^-2. No sign of R follows from the identity. The existing gauge-orbit Casimir and radial Fisher controls are probability-weighted and do not imply fiber-uniform bounds.

**Verification:** A normalized two-SU(2)-class conditional state Φ(p,q)=(1+κpq)/√(1+κ²p²/4), κ=.72, was tested with nontrivial p- and q-kinetics and coupled potential 1.3(1−pq) at 81 angles. Maximum covariance-formula differentiation residual 6.35e-11 and normalization residual 4.44e-16. This is an algebraic identity test, not a physical M55 vacuum simulation. Complete derivation and test script: Library `/The Singular Boundary/Proof Audits/R3_IR_FIBER_COVARIANCE_DECOMPOSITION_2026-10-31.zip`.

**OPEN:** Wilson-specific uniform conditional kinetic material-derivative and covariance bounds, unweighted score current sup_f 𝔗_(f,h)=o(h^-1/4), connected covariance and continuum Yang–Mills mass gap.