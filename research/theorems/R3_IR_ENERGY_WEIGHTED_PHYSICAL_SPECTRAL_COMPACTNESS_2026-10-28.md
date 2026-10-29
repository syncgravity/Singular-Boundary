# R3-IR — Energy-weighted physical Wilson spectral compactness, UV-time response, and exact infrared obstruction

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Scope:** exact physical-sector theorems for the declared finite nonlinear SU(2) Wilson Hamiltonian; Penrose refinement bounds conditional on the already established local first- and third-spectral-moment bounds. **Not proved:** a positive uniform physical mass gap, a nontrivial finite-energy Wilson continuum, an upper variance bound, quartic resolvent control, or original Stage7/26 action correspondence. No Monte Carlo or alteration of historical data.

## 1. Inputs, checked against current GitHub branch

We use the *finite-regulator* physical spectral-measure construction of `R3_IR_PHYSICAL_SOURCE_RESPONSE_SPECTRAL_TRICHOTOMY_2026-10-28.md` (PS-1/PS-3), the first physical f-sum `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-8) and `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md` (FS-1), and the independently derived third physical f-sum `R3_IR_PHYSICAL_THIRD_MOMENT_LOCAL_COMMUTATOR_2026-10-28.md` (TS-1 through TS-13). The TS proof relies on the local first-order vacuum Fisher bound and a complete geometric collar, and has not been identified with the source code of Stage7/26. The preceding joint-force/Bochner results remain valid and do not imply a mass gap.

For finite connected face-complete planar SU(2) rhombus disk, let

  H_h = sum_e a_e(-Delta_e)+sum_f b_f[1-p_f],   p_f=1/2 ReTr W_f,
  K_h=H_h-E0,h,     Omega_h>0 the unique Gauss-invariant normalized vacuum.

Take finitely many real bounded face weights q^j on a fixed physical region with full collar, and define

  Y_h^j=h sum_f q_f^j(1-p_f),  A_h^j=(Y_h^j-<Y_h^j>)/sqrt(h).

The vectors A_h^j Omega_h are genuinely Gauss invariant and vacuum orthogonal. Let `mu_h^{ij}(dE)=<A_h^i Omega_h, 1_{dE}(K_h) A_h^j Omega_h>` be the Hermitian matrix of physical excitation-energy measures on E>0. At every finite h the unique ground state ensures there is no source spectral mass exactly at E=0.

For each fixed i, the previous actual interacting vacuum theorems yield

  0 <= m1_h^i = int E mu_h^{ii}(dE) <= C1_i,
  0 <= m3_h^i = int E^3 mu_h^{ii}(dE) <= C3_i h^-2.

For a nonzero nonnegative macroscopic test with electric coefficients bounded below and h² sum q_f>=q_mass>0, the earlier exact stationarity theorem yields m1_h^i>=c_i>0 for all sufficiently small h. Constants may depend on the test and physical domain, not on h or ambient volume, under the same hypotheses as the cited theorems. These bounds are the *only* analytic moment inputs below.

## 2. Theorem EW-1: unconditional rescaled physical energy-flux measure compactness

Define a positive semidefinite n-by-n matrix measure on xi=hE>=0 by

  Sigma_h^{ij}(B)=int_{E>0, hE in B} E mu_h^{ij}(dE).

Equivalently, Sigma_h^{ij}(B)=<K_h^(1/2) A_h^i Omega_h,1_B(hK_h)K_h^(1/2) A_h^j Omega_h>. Every spectral projection and source multiplier in this definition preserves Gauss invariance.

Its diagonal mass and second xi moment are exactly

  Sigma_h^{ii}([0,infty))=m1_h^i<=C1_i,
  int xi² Sigma_h^{ii}(dxi)=h² m3_h^i<=C3_i.          (EW-1)

Thus, for all R>0,

  Sigma_h^{ii}((R,infty))<=C3_i/R²,
  |Sigma_h^{ij}|((R,infty))<=sqrt(C3_i C3_j)/R².     (EW-2)

For the off-diagonal entry, use the Cauchy–Schwarz inequality for spectral projector integrals, first for a finite partition of (R,infty), then take the total-variation supremum. The diagonal uniform second xi moment supplies the bound. The analogous total-variation control for all measurable B follows from sqrt(Sigma_ii(B) Sigma_jj(B)).

For a fixed finite family of sources, the matrix measures have uniformly bounded mass and are tight on [0,infty). Therefore there is a refining subsequence on which Sigma_h converges weakly to a finite positive semidefinite matrix measure Sigma. Because tightness controls escaped mass, its total mass matrix also converges. For any nonzero nonnegative macroscopic test i,

  Sigma^{ii}([0,infty))=lim m1_h^i>=c_i>0.          (EW-3)

**Interpretation:** A nonzero *energy-weighted*, *rescaled-energy* spectral limit exists along a subsequence without assuming source-variance tightness. It is neither finite-physical-energy spectral survival nor a mass gap. Sigma may have an atom at xi=0, which aggregates excitation energies much smaller than h^-1 (including E=O(1) or E->0). This is an ultraviolet-time scaling statement, not full OS quantum reconstruction.

## 3. Theorem EW-2: exact UV-time Euclidean derivative kernel and positivity

For physical time t>=0 define C_h^{ij}(t)=<A_h^i Omega_h,e^(-tK_h) A_h^j Omega_h>. For rescaled time tau>=0 set

  D_h^{ij}(tau)=-d/dt C_h^{ij}(t)|_(t=h tau)
               =int exp(-tau xi) Sigma_h^{ij}(dxi). (EW-4)

Because the first moment of the xi-weighted measure is

  int xi Sigma_h^{ii}(dxi)=h m2_h^i<=sqrt(C1_i C3_i),

by spectral Cauchy–Schwarz, D_h is uniformly bounded and uniformly Lipschitz on tau>=0, including mixed entries. Weak convergence of Sigma_h gives uniform convergence of D_h on compact tau intervals to

  D^{ij}(tau)=int exp(-tau xi) Sigma^{ij}(dxi).       (EW-5)

For any tau_j>=0 and complex column vectors v_j in C^n,

  sum_{j,k} v_j^* D(tau_j+tau_k) v_k
    =int [sum_j exp(-xi tau_j)v_j]^* Sigma(dxi)[sum_k exp(-xi tau_k)v_k] >=0.   (EW-6)

The last expression is the positive quadratic-form integral against the matrix-valued positive semidefinite measure; this is exact reflection positivity for the one-dimensional matrix kernel. It does not prove spatial locality or the full OS axioms.

If a test i additionally satisfies m1_h^i>=c_i, set B_i=sqrt(C1_i C3_i). Jensen for the probability Sigma_h^{ii}/m1_h^i yields

  D_h^{ii}(tau)>=m1_h^i exp[-tau h m2_h^i/m1_h^i]
                >=c_i exp[-tau B_i/c_i].          (EW-7)

The same nonzero bound passes to the limit at every finite tau. This shows **nonzero energy-flux Euclidean response on times t=h tau** for the true finite interacting SU(2) vacuum under the previous verified moments, not nonzero variance of A_h at fixed physical time. The limit D^{ii} can be constant if Sigma concentrates at xi=0; genuine time decay is not asserted.

## 4. Theorem EW-3: exact variance as an inverse rescaled-energy moment and a quantitative UV-band criterion

At finite h, the source variance v_h^i=mu_h^{ii}((0,infty)) is exactly

  v_h^i=h int_(0,infty) xi^-1 Sigma_h^{ii}(dxi).   (EW-8)

This identity pinpoints the remaining obstruction: the previous first/third energy moments bound Sigma_h at large xi but do not control its inverse moment near xi=0. An independent source-specific *small-xi regularity estimate* is required for an O(h) variance upper bound.

**Conditional quantitative UV band.** Suppose for a nonzero nonnegative test i there is an independently established Gaussian-order variance upper bound v_h^i<=K_i h (NOT currently proved in nonlinear SU(2)). Then for any epsilon>0 and R>0,

  Sigma_h^{ii}((0,epsilon])<=epsilon v_h^i/h<=K_i epsilon,
  Sigma_h^{ii}((R,infty))<=C3_i/R².                 (EW-9)

Choose epsilon_i=c_i/(4K_i), R_i=2 sqrt(C3_i/c_i). Then

  **Sigma_h^{ii}([epsilon_i,R_i])>=c_i/2,**
  **mu_h^{ii}([epsilon_i/h,R_i/h])>=c_i h/(2R_i).**  (EW-10)

In particular the limiting Sigma has positive spectral mass away from xi=0, and D^{ii}(tau)<D^{ii}(0) for every tau>0. This is a *conditional* theorem: the missing upper bound v_h<=K_i h is not supplied by the existing SU(2) Hamiltonian estimates, so EW-10 does not prove that the interacting source's energy resides in this UV band.

**General small-xi condition:** If one can prove uniformly Sigma_h^{ii}((0,epsilon])<=C epsilon^(1+delta) for some delta>0 and all 0<epsilon<=1, then integrate (EW-8) by parts to get v_h^i=O(h). The condition is an independent IR-spectral regularity target, not an established consequence. Under only EW-1 no such estimate is valid.

## 5. Exact sharpness witness: the existing moments do not distinguish three regimes

Fix c>0 and 0<h<=1. The following *abstract positive physical spectral measures* all satisfy m1_h=c and m3_h<=c h^-2:

(i) finite physical energy: mu_h=c delta_{E=1}. Then v_h=c and Sigma_h=c delta_{xi=h} ->c delta_0.

(ii) ultraviolet energy: mu_h=c h delta_{E=h^-1}. Then v_h=c h and Sigma_h=c delta_{xi=1}.

(iii) infrared softening: mu_h=c h^-1 delta_{E=h}. Then v_h=c h^-1 and Sigma_h=c delta_{xi=h²} ->c delta_0.

They also satisfy the generic Agmon-based upper variance envelope O(h^-1) in the sense of that numeric bound, but are NOT constructed from any genuine SU(2) Wilson Hamiltonian; in particular they do not reproduce all higher source moments. They certify only the **logical insufficiency of m1/m3 alone** for finite-energy survival, source-variance classification, or a gap. The rescaled sigma limit delta_0 by itself cannot distinguish fixed-energy spectral survival from an excitation gap closing.

Each case can be realized by a two-level nonnegative Hamiltonian K=diag(0,E_h), normalized vacuum |0>, and selfadjoint off-diagonal physical source A=sqrt(v_h)(|0><1|+|1><0|). This is an abstract Hilbert-space counterexample, not gauge Wilson dynamics.

## 6. Evidence and next actual nonlinear obligation

**Proved for the declared finite nonlinear SU(2) model under upstream first/third moment bounds:** EW-1 positive Gauss-invariant energy-flux spectral tightness after rescaling E->hE, nonzero weak limiting diagonal mass for nonnegative macroscopic sources; EW-2 UV-time derivative Euclidean kernel compactness and reflection positivity; EW-7 quantitative nonzero UV-time response; EW-8 exact source variance as inverse rescaled-energy moment. These statements are unconditional on a mass gap and on source variance tightness. EW-10 is conditional on an **unproved** Gaussian-scale variance bound.

**OPEN:** any uniform bound on the small-xi inverse moment of Sigma_h, finite-energy spectral-weight survival, actual source variance upper/tightness, source-specific or full physical spectral gap, quartic nonlinear inverse resolvent, Stage7/26 source-level provenance and complete continuum reconstruction.

**Most useful next task:** derive a Wilson-Hamiltonian-based estimate controlling *small-xi spectral mass* of the actual energy-weighted physical source, without importing the tangent Gaussian model or a spectral gap. Such an estimate would control variance O(h) if the integrated x^-1 tail is small. Alternatively prove a fixed-physical-energy source projection lower bound directly from a noncircular interacting vacuum comparison. Preserve the original Stage7/26 archives unmodified.