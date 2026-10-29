# The Singular Boundary — Moderate-curvature concentration gate and exact SU(2) two-phase witness

**Date:** 2026-10-28  
**Branch:** `audit/2026-10-28-independent-reconstruction`  
**Status:** Independently proved uniform exponential-integrability corollary for the *actual* finite interacting Wilson ground state under the previously proved regional Agmon estimate, and an explicit finite SU(2) gauge-invariant positive-wavefunction witness showing why moderate-curvature covariance requires a new estimate. **Does not establish vacuum connected-covariance collapse, spectral mass gap, infinite-volume continuum, or Stage 7/26 Hamiltonian correspondence.** No Monte Carlo, no alterations of historical samples.

## 1. Direct primary-source dependencies

The current branch versions of `research/theorems/R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1 through AG-6), `R3_IR_GAUGE_INVARIANT_COHERENT_COVARIANCE_WITNESS_2026-10-28.md` (CW-1/CW-2) and `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1) were read before performing this calculation. The previous actual-vacuum bound was:

`E_nu[X exp(2 lambda_h (X-2L)) 1_{X>=2L}] <= (64 a_max/beta_min) h²/L`,

where `X=sum_{f in D}d_f`, `d_f=1-(1/2)ReTr W_f in [0,2]`, `lambda_h=h^(-1)sqrt(beta_min/(32a_max))`, and `L>=2h²(E0-E_out)/beta_min`. On a fixed physical interior disk under the previously declared Penrose coefficient and collar hypotheses, one may choose `L_h=C_L/h` with `C_L>0` independent of h for sufficiently small h. This is a consequence of the actual vacuum eigenfunction, not an arbitrary state.

## Theorem MC-1 — Uniform exponential moments of *actual-vacuum* rescaled curvature

For every fixed real `theta>=0`, define `Y_h=h X_h`, where `X_h=sum_{f in D_R}d_f`. Then

**`sup_{0<h<h0} E_nu[exp(theta Y_h)] <= exp(2theta C_L) [1 + (32a_max/(beta_min C_L²)) h^4] < infinity`.**

More precisely,

**`E_nu[exp(theta hX_h) 1_{X_h>=2L_h}] <= (32 a_max/(beta_min C_L²)) exp(2theta C_L) h^4`.**

**Proof.** On `X<=2L`, `exp(theta hX)<=exp(2theta hL)`. On `X>=2L`, for all sufficiently small h one has `theta h <=2lambda_h`. Therefore

`exp(theta hX) <= exp(2theta hL) exp(2lambda_h (X-2L)) <= exp(2theta hL)[X/(2L)] exp(2lambda_h (X-2L))`.

Integrate against `nu`, apply AG-1, and substitute `L=C_L/h`. All estimates are at the **true** nonlinear ground-state measure `nu=Omega_h²dHaar`. No spectral gap, translational invariance, Gaussian comparison, or decay of spatial covariance is assumed. For theta<0, the moment is automatically <=1 because X>=0. Standard exponential-moment bounds give, for every finite integer n, `sup_h E[(hX_h)^n]<infinity`, and hence distributional tightness of `hX_h` along any refinement sequence. Neither tightness nor convergence of the mean implies a variance rate `o(h)`.

For signed bounded `q_f`, `|h sum_f q_f d_f|<=q_max hX_h`; the same uniform exponential-moment and absolute moment bounds hold for the weighted regional curvature `Y_h(q)=h sum_f q_f d_f` (use `exp(theta |Y_h(q)|)<=exp(|theta|q_max hX_h)`). The critical `alpha=3/2` source is `B_h=-h^(-1/2) Y_h(q)`. Consequently the exact fixed-support vacuum criterion is

**`Var_nu(Y_h(q))=o(h)`**, equivalently `Var_nu(B_h)=o(1)`.

The theorem establishes all finite exponential moments of `Y_h(q)`, **not** their needed shrinking variance rate.

## 2. Genuine SU(2) coherent states with only **moderate** plaquette curvature

Fix a simply connected finite face-complete planar SU(2) rhombus disk with `F_h asymp h^-2`, bounded physical area, each link in at most two four-edge faces, `a_e<=a_max` and `b_f<=beta_max/h²`. Assume face-center Riemann sums for a nonnegative fixed-support smooth test with `q_f=sigma_f phi(x_f)`, `I_h=h² sum_f q_f -> I_phi>0`.

Gauge fixing along a primal spanning tree and triangular elimination along a dual spanning tree give independent product-Haar rooted face holonomies. For each `kappa>0`, the **positive, normalized, vertex-gauge-invariant** smooth link wavefunction

`Psi_kappa(U)=Z(kappa)^(-F/2) exp(kappa sum_f p_f(U))`,

`Z(kappa)=int_SU2 exp(2 kappa p(U)) dHaar(U)=I_1(2kappa)/kappa`

therefore has independent face-trace variables in its own Born measure. The exact one-face mean and variance are

`r_kappa=I_0(2kappa)/I_1(2kappa)-1/kappa`,

`v_kappa=Var_kappa(p)=r_kappa'/2`.

By standard large-positive-argument Bessel asymptotics,

`r_(c/h)=1-3h/(4c)+O(h²)`, `v_(c/h)=3h²/(8c²)+O(h³)`,

for any fixed c>0. Thus each individual state with `kappa=c/h` has **only moderately curved faces**: `E[d_f]=3h/(4c)+O(h²)`, with no nearly all-curved component.

Choose two fixed distinct positive parameters `c_1!=c_2`, `kappa_i=c_i/h`, and `eps_h=h` (or, separately, a fixed eps∈(0,1)). Define

`Phi_h=[sqrt(1-eps_h) Psi_(c1/h)+sqrt(eps_h) Psi_(c2/h)]/sqrt(N_h)`,

where `s_h=<Psi_(c1/h),Psi_(c2/h)> = [Z((kappa_1+kappa_2)/2)/sqrt(Z(kappa_1)Z(kappa_2))]^F` and `N_h=1+2sqrt(eps_h(1-eps_h))s_h`. Both branches and Phi_h are strictly positive physical SU(2) states. Since

`Z(kappa)=e^(2kappa)/(sqrt(4pi)kappa^(3/2))(1+O(kappa^-1))`,

`s_h=( [2sqrt(c1 c2)/(c1+c2)]^(3/2)+O(h))^F =exp[-c_*F+o(F)]`, `c_*>0`; hence the overlap is exponentially small in h^-2.

### Theorem MC-2 — Finite (or divergent) critical covariance with moderate curvature

For `A_h=h^(1/2) sum_f q_f p_f` and the state Phi_h above,

**`<Phi_h,H_h Phi_h>=O(h^-3)`**,  
**`F_h^-1 sum_f<Phi_h,d_f Phi_h>=O(h)`**,  
**`<Phi_h,Gamma(A_h)Phi_h>=O(1)`**,

and, for `eps_h=h`,

**`Var_(Phi_h)(A_h) -> (9/16) I_phi² (1/c1-1/c2)² >0`.**

For a fixed eps∈(0,1) instead,

**`Var_(Phi_h)(A_h) ~ (9/16) eps(1-eps) I_phi² (1/c1-1/c2)² h^-1`.**

These variances arise from **different moderate curvature densities** in the two positive branches, not from rare, nearly maximally curved faces.

**Proof of energy and gradient bounds.** On the link Hilbert space, `grad_e Psi_kappa=kappa Psi_kappa sum_{f containing e}grad_e p_f`. Edge incidence≤2, and the exact SU(2) fundamental carré du champ `|grad_e p_f|²=(1-p_f²)/4`, give

`<Psi_kappa,H_E Psi_kappa> <= 2a_max kappa² F (1-E_kappa[p²])=O(h^-3)`

for kappa=c/h, since `1-E[p²]=O(h)` and F=O(h^-2). The magnetic contribution is `sum_f b_f(1-r_kappa)=O(h^-3)`. The quadratic-form triangle inequality for `H>=0`, followed by the normalization `N_h>=1`, gives the same total energy order for the positive superposition, uniformly for eps∈[0,1]. Each branch's face deficits average O(h), and their mixed density is `s_h Psi_((kappa1+kappa2)/2)²`, so the superposition has mean deficit O(h). The pointwise SU(2) inequality `Gamma(A_h)<=4a_max q_max² h sum_f d_f` then gives an O(1) gradient expectation.

**Exact variance.** Put `m_i=h^(1/2) Q_h r_(kappa_i)`, `v_i=h(sum q_f²) v_(kappa_i)`, `Q_h=sum q_f`, and similarly `m_m,v_m` for kappa_mid. Then

`E_Phi[A]=( (1-eps)m1 +eps m2+2sqrt(eps(1-eps))s_h m_m)/N_h`,

`E_Phi[A²]=( (1-eps)(m1²+v1)+eps(m2²+v2)+2sqrt(eps(1-eps))s_h(m_m²+v_m))/N_h`.

These formulas are exact at finite h. Since the s_h corrections are exponentially small, `v_i=O(h)`, and

`m_1-m_2=(3I_phi/4)(1/c2-1/c1)h^(-1/2)+O(h^(1/2))`,

we obtain the asserted limits from `eps(1-eps)(m1-m2)²`. In particular, for c1=1,c2=2,I_phi=1 the rare eps=h limit is `9/64`; the equal-weight divergence coefficient is `9/256`. This is a proof, not a numerical fit.

### Theorem MC-3 — Even large-deviation suppression does not force moderate covariance decay

In **each pure branch**, the entire sum `X_h=sum_f d_f` has the exact moment generating function

`E_(Psi_(c/h))[e^(tX_h)]=[e^t Z(c/h-t/2)/Z(c/h)]^F`.

With `t=s/h`, fixed `0<s<2c`, the logarithm per face is

`(3/2) log[c/(c-s/2)]+O(h)`.

Thus Markov/Chernoff gives: for any fixed `rho>0` and `F asymp h^-2`,

`P_(Psi_(c/h))[X_h>=rho F] <=exp(-C_rho h^-3)`

for small h and a suitable constant C_rho>0. Similarly, for any `C_L>(3/4) limsup(h²F)/min(c1,c2)`, the probability that `X_h>C_L/h` is `<=exp(-C h^-2)` for a suitable C>0. Since pointwise `|Phi_h|² <= 2[(1-eps)|Psi_1|²+eps|Psi_2|²]` (N_h≥1), the corresponding large-deviation estimates also hold for Phi_h. Thus the two-branch witness can have **exponentially suppressed extremely large curvature excursions** while retaining the nonzero critical covariance of MC-2.

**Precise logical scope:** MC-2/MC-3 are genuine SU(2) positive *trial-state* results with true Wilson Hamiltonian expectation values; they do **not** show these states are ground states, eigenstates below a fixed excitation threshold, or subject to the exact vacuum Agmon identity. Matching its tail *rate* does not establish its weighted AG-1 inequality for the trial. No physical gap or ground-state counterexample is constructed.

## 3. Strongest remaining proof obligation

For the actual nonlinear Wilson ground state, prove a **first-order fluctuation-rate improvement** for fixed physical support:

**`Var_(Omega_h)(Y_h(q))=o(h)`**, `Y_h(q)=h sum_f q_f d_f`.

Uniform exponential moments and exclusion of very high total curvature have been established from the true vacuum (MC-1), but do not imply this o(h) variance rate. The two-branch SU(2) states (MC-2) demonstrate that a wavefunction can exhibit exactly such O(h) variance while remaining moderate-curvature and satisfying the previously available energy/gradient envelope. The **only** plausible route using the current methods is to exploit additional *ground-state energy minimization at the relative-excess level*, source-dependent conditional spatial covariance, or a noncircular coercive Ward estimate. One cannot assume a global gap or Gaussian/log-Sobolev domination.

The original Stage7/26 simulation Hamiltonian and its physical normalization remain an independent provenance gate. The full R3-IR mass gap and R2 continuum remain OPEN.

## 4. Reproducibility and integrity

`verify_moderate_excursions.py` checks the exact SU(2) Bessel/Haar identities, rare-branch/equal-weight asymptotic constants, the overlap factor, and the Agmon exponential-moment algebra with exact symbolic arithmetic. It also makes a few **deterministic** special-function evaluations (no stochastic sampling) as a numerical sanity check. This verifier does not by itself prove spatial independence or the asymptotic large-deviation theorem, which are derived analytically above. All historical source archives remain untouched.