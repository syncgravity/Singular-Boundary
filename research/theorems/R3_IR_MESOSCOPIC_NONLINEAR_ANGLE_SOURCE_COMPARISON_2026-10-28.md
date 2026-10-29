# The Singular Boundary — Regulator-uniform mesoscopic Wilson/angle observable comparison in the nonlinear SU(2) vacuum

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Proof status:** exact *operator-on-energy-band* theorem for the declared finite nonlinear SU(2) Hamiltonian, with a Penrose shrinking-support corollary under its declared coefficient and collar assumptions. **Not** a comparison of the nonlinear vacuum with a Gaussian vacuum. **Not** a fixed-physical-support covariance theorem, an all-sector gap, a quartic resolvent estimate, or continuum reconstruction. No Monte Carlo and no change to historical Stage7/26 artifacts.

## 1. Why this is the correct notion of comparison at this stage

The preceding volume-uniform quartic-remainder audit (`R3_IR_VOLUME_UNIFORM_MAGNETIC_QUARTIC_REMAINDER_2026-10-28.md`) proved that the magnetic Taylor correction has extensive mean and order-sqrt(F) centered fluctuations in the *Gaussian tangent reference* at F~h^-2. Thus an O(1) uncentered global perturbation norm is not available. A weaker, mathematically distinct question is whether **two gauge-invariant source multipliers**, evaluated in the *same actual interacting SU(2) low-energy states*, become equivalent on mesoscopic supports. This can be answered nonperturbatively with the previously audited regional relative-energy bound (`R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md`) and all-band compression (`R3_IR_MESOSCOPIC_SOURCE_COMPRESSION_2026-10-28.md`). It does not assert any equality between vacuum distributions or kinetic forms.

Consider a finite edge-to-edge rhombus disk G_h, four boundary links per face, link-face incidence at most two. On the physical vertex-Gauss-invariant subspace of L^2(SU(2)^E), let

    H_h = sum_e a_e(-Delta_e)+sum_f b_f d_f,
    d_f=1-p_f, p_f=(1/2)Re Tr W_f, a_e>0, b_f>=0.

For a face region D with incident edge set S and exterior face collar C(D), define

    E_D=(3/sqrt(2))sqrt[(sum_{e in S}a_e)(sum_{f in D}b_f)]
          +2 sum_{g in C(D)}b_g.

Assume b_f>=beta_min h^-2 for f in D. Let K_h=H_h-E0(H_h), and P_eta=1_[0,eta](K_h) restricted to the physical sector, eta>=0. ER-1 establishes for *each* unit vector psi in Ran P_eta:

    <psi, sum_{f in D} d_f psi> <= (h^2/beta_min)(E_D+eta).     (A1)

There is no assumption of a uniform gap or independent face variables.

## 2. Exact intrinsic SU(2) angle inequality

The fundamental plaquette trace uniquely defines the principal class angle

    theta_f = 2 arccos p_f in [0,2 pi],
    Q_f = theta_f^2/8 = (arccos p_f)^2/2.

The quadratic *magnetic observable* Q_f is gauge invariant and bounded, but it is **not** the noncompact Gaussian tangent Hamiltonian and does not alter the kinetic energy. Write r_f=Q_f-d_f. Then, for all SU(2) group elements, including W_f=-I,

    0 <= r_f <= c_angle d_f,
    c_angle=pi^2/4-1,                                           (A2)
    0 <= r_f <= (pi^4/96)d_f^2.                                (A3)

Proof: put x=arccos p in [0,pi]. Then d=1-cos x=2sin²(x/2), Q=x²/2. The elementary bounds 2x²/pi²<=1-cos x<=x²/2 imply d<=Q<=pi² d/4, giving (A2). Taylor's integral remainder yields 0<=x²/2-(1-cos x)<=x^4/24. Since x²<=pi² d/2, obtain (A3). All inequalities hold globally, including the conjugacy cut locus; no differentiability of theta at W=-I is used.

For any bounded real signed weights |q_f|<=q_* on D, define the critically normalized, scalar-subtracted physical multipliers

    B^W_h=-sqrt(h) sum_{f in D}q_f d_f,
    B^angle_h=-sqrt(h) sum_{f in D}q_f Q_f,
    Delta B_h=B^angle_h-B^W_h=-sqrt(h)sum_{f in D}q_f r_f.

The same deterministic bound applies to any projected physical state:

    |Delta B_h|² <= h q_*² c_angle² (sum_D d_f)²
                 <= 2h q_*² c_angle² |D| sum_D d_f,             (A4)

using 0<=d_f<=2. The signed q terms require no positivity or independence: all absolute values are absorbed in q_*.

## 3. Theorem AC-1: all-energy-band nonlinear-to-intrinsic-angle source comparison

**At every finite regulator**, for all eta>=0 and b_f>=beta_min h^-2 on D,

    ||(B^angle_h-B^W_h) P_eta||²
      <= (2 c_angle² q_*²/beta_min) |D| h³ (E_D+eta).            (AC-1)

Proof: take a unit vector psi in Ran P_eta, integrate pointwise (A4) against |psi|² Haar, apply (A1), and take the supremum over such psi. The multipliers are physical because they are class functions of plaquette holonomies. The bound controls the full output norm; it is *not* restricted to low-energy output. In particular for all energy cutoffs Lambda>=0,

    ||P_>Lambda (B^angle_h-B^W_h) P_eta|| <= RHS(AC-1)^(1/2),

and for every bounded Borel function F of K_h with ||F||∞<=1,

    ||F(K_h)(B^angle_h-B^W_h)P_eta|| <= RHS(AC-1)^(1/2).

These are exact statements in the *nonlinear* physical Hilbert space and do not compare either state to a Gaussian.

## 4. Theorem AC-2: Penrose mesoscopic threshold, including growing excitation windows

For a genuine complete interior Penrose face disk D_R, with h<<R<=R0 and a complete collar, use the existing geometric counts and declared coefficients (not fully source-certified for Stage26):

    |D_R| <= C_F R²/h²,
    E_D <= C_E (R²+R)/h³.

AC-1 gives

    ||Delta B_h P_eta||² <= C[(R^4+R^3)/h² + eta R² h].           (AC-2)

Let R(h)=ell^(1-gamma) h^gamma, with fixed ell>0 and 2/3<gamma<1. Then for any excitation-energy horizon eta_h=O(h^(-kappa)) with

    0<=kappa<1+2 gamma,

one has

    ||Delta B_h P_eta_h||
       = O(h^((3 gamma-2)/2) + h^((1+2 gamma-kappa)/2)) ->0.     (AC-3)

The first exponent is positive exactly for gamma>2/3 and the second for kappa<1+2 gamma. This permits energy bands increasing *faster* than the natural h^-1 UV scale; e.g., gamma=4/5 and eta_h=h^-2 give O(h^(1/5)). There is **no analogous vanishing conclusion at fixed physical radius R>0** from these estimates: the first bound becomes O(h^-2) after squaring.

## 5. Theorem AC-3: actual-vacuum spectral-measure comparison and Euclidean times

For eta>=0, the actual normalized interacting vacuum Omega_h belongs to Ran P_eta. Set x=Q0 B^W_h Omega_h and y=Q0 B^angle_h Omega_h, where Q0=I-|Omega_h><Omega_h|. From AC-1,

    ||x-y|| <= delta_h,
    ||x||+||y|| <= C_0 delta_bound_h,

where both multipliers are bounded pointwise by c sum_Dd_f, and delta_bound_h²=C[(R^4+R^3)/h²+eta R²h] can be evaluated at eta=0. Hence for the respective **positive physical excitation-energy spectral measures** mu_W and mu_angle,

    sup_{||F||infty<=1} |<x,F(K_h)x>-<y,F(K_h)y>|
          <= ||x-y||(||x||+||y||) <= C delta_bound_h².          (AC-4)

The left-hand side is the total variation norm of the difference of the scalar spectral measures. This controls **all** energy windows, as well as the physical Euclidean two-point functions for **every t>=0** by taking F(E)=e^(-tE). For the shrinking region with gamma>2/3, it vanishes as O(h^(3gamma-2)) for eta=0. Both unamplified mesoscopic source vectors themselves vanish in norm: AC-4 is a legitimate observable equivalence but **not** a construction of a nontrivial field.

For a fixed physical region D_R, there is a weaker but unconditional area-density comparison in the actual vacuum: define T_h=h² sum_D q_f r_f. By (A2), |T_h|<=c_angle q_* h Z_h, Z_h=h sum_Dd_f. The previously proved true-vacuum Agmon theorem gives sup_h E[Z_h²]<∞; therefore

    ||T_h Omega_h||_2 = O_R(h).                             (AC-5)

This is convergence of *unnormalized area-density observables*, not of the alpha=3/2 critical source or either vacuum law.

## 6. Sharp boundary of the result and next obligation

The present work **proves** a quantitative nonlinear-to-intrinsic-angle **observable** comparison on shrinking physical regions, uniform on large physical excitation-energy subspaces, plus full spectral-measure/Euclidean-time equivalence for the resulting vanishing mesoscopic fields. It does **not** compare the actual nonlinear ground state with the oscillator/Gaussian tangent ground state; the cubic/quartic Hamiltonian corrections, Haar Jacobian, mixed-link kinetic terms, and extensive vacuum fluctuation remain unbounded globally by this theorem.

At fixed positive physical radius, AC-2 is insufficient for the alpha=3/2 source. The next genuinely unresolved gate is a **connected (centered) fourth-moment or conditional-covariance bound for the regional angular remainder** under the *actual* Wilson ground state, not the Gaussian reference, strong enough to show its source-projected error goes to zero at fixed support. Independent source-specific control of the potential/kinetic resolvent difference and true-vacuum response is then required for any claimed nonlinear-to-Gaussian comparison at fixed physical time. A regulator-uniform physical mass gap, original Stage7/26 coefficient identity, quartic inverse resolvent and continuum reconstruction remain open.

## 7. Independent audit

A separate deterministic SymPy and SU(2) character-basis verifier checks (A2)-(A4), the penalty constant and h powers in AC-1/AC-3, the authentic three-rhombus ten-edge Penrose spatial fixture, and a genuinely interacting one-plaquette spectral-band operator norm bound. This verifier is evidence for algebraic integrity, **not** a substitute for the operator inequalities. No Monte Carlo or modification of historical archives.