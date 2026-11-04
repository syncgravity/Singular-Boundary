# R3-IR-556 — Non-tree SU(2) sector-Sobolev relative center-cap theorem

Date: 2026-10-30. **Rigorous finite-regulator theorem**, conditional on the specified rooted SU(2) electric form and protected non-tree link. Unlike R3-IR-552–555, this estimate does **not require global mixing or Poisson-response localization**. It yields a cap-width-independent bound and remains useful under refinement IF an explicit interaction/kinetic ratio remains uniformly below a threshold. That physical scaling assumption remains open.

## Hypotheses

Let X=SU(2)^E carry normalized product Haar measure, with electric quadratic form
  E_E(f)= (g2²/2) ∫ Σ_{i,j} (M^-1)_ij D_i f·D_j f dμ,
where M is constant SPD, D_i=Ad(V_i) X_i, X_i are normalized left derivatives exp(t iσ/2), and root transports V_i follow a fixed tree. Fix a non-tree edge e such that **all V_i are independent of U_e**, and assume the real multiplication potential V_other of H0=H_E+V_other is independent of U_e. The adjacent Wilson multiplier W satisfies |W|≤1 and is linear in the quaternion coordinates of U_e (true for a Wilson plaquette involving e once). Define H_b=H0+bW. Assume unique normalized positive compact finite-regulator ground states Ω0,Ω_b (e.g. smooth bounded potentials, elliptic connected compact configuration manifold), and the corresponding Friedrichs form domains.

The Haar-chord projection reducing H0 and positivity imply Ω0 independent of U_e. Set π=Ω0² μ, q=Ω_b/Ω0 normalized by ∫q² dπ=1. The stationary ground-state transform A0=Ω0^-1(H0−E0)Ω0 has the exact nonnegative Dirichlet form E_π(q)= (g2²/2)∫ Σ K_ij D_iq·D_jq dπ. The π law factorizes into spectator π_other times independent Haar(U_e).

## Exact sector coercivity

Set c_e=g2²/(2M_ee), and let C_e=−Σ_a (X_e^a)² be the nonnegative SU(2) Casimir on U_e, with eigenvalues j(j+1) for j=0,1/2,1,... . Schur completion of the real SPD block K=M^-1 gives pointwise Σ_ij K_ij D_iq·D_jq ≥ (1/M_ee)|D_eq|²=(1/M_ee)|X_eq|². Therefore

  A0 ≥ c_e C_e    in the quadratic-form sense.

Because all D_i coefficients and V_other are U_e-independent and C_e commutes with each X_e, **[A0,C_e]=0**. Thus on each spin-j block, A0|_j ≥ c_e j(j+1), j>0. Define γ_half=3c_e/4. The Wilson multiplier W is bounded by 1; its mean π(W)=0 since U_e is Haar and W linear. The variational principle with trial Ω0 yields δE=E_b−E0≤b π(W)=0. The q equation is

  (A0−δE)q = −bWq.

Writing P_j for SU(2) Peter–Weyl chord-spin projections and Q=I−P_0, the sector equations imply, for j>0,

  ||P_j q||_2 ≤ |b|/[c_e j(j+1)] ||P_j Wq||_2.

Since ||q||_2=1, the orthogonality of spin sectors yields two regulator-explicit estimates

  ||Qq||_2 ≤ |b|/γ_half =:ρ,
  ||C_e Qq||_2 ≤ |b|/c_e.

These inequalities hold with *arbitrarily strong* spectator-only Wilson potentials; no full-configuration spectral gap or mixing lower bound is used.

## Quantitative SU(2) Sobolev embedding

At each fixed spectator configuration, Peter–Weyl's normalized matrix coefficient basis has diagonal reproducing sum (2j+1)² for spin j. Cauchy–Schwarz therefore bounds

  sup_{U_e} |(Qq)(y,U_e)| ≤ S ||C_e(Qq)(y,.)||_{L²(Haar)},

where
  S² = Σ_{j=1/2,1,...} (2j+1)²/[j(j+1)]²
     = 16 Σ_{n=1}∞ (n+1)²/[n²(n+2)²]
     ≤16 Σ_{n=1}∞ 1/n² = 8π²/3,

hence S≤4π/√6≈5.130199321. (Numerical actual S≈3.762886198; the simpler rigorous upper bound is used in the certificate.) Integrate the squared inequality over spectator π_other to get a Hilbert-valued sup-in-chord estimate

  ||sup_{U_e}|Qq(y,U_e)|| ||_{L²(π_other)} ≤ S |b|/c_e.

Write q=q0(y)+q_perp(y,U_e), with q0=P0q and ||q0||_2=√(1−||Qq||²) ≥√(1−ρ²) for ρ<1. For a deleted-face trace p0 which is a group translate of U_e at each spectator y, the Haar conditional distribution of p0 is the standard w(p)dp and conditioning leaves π_other unchanged. For every p∈[-1,1] the conditional L² triangle inequality gives

  [E_π(q²|p0=p)]^(1/2)
    ≥ ||q0||_{L²(π_other)} − ||sup_{U_e}|q_perp|||_{L²(π_other)}
    ≥√(1−ρ²) − S |b|/c_e.

Therefore, **for all radial events A, including every two-center cap C_delta simultaneously**,

  Pr_{Ω_b²μ}(A) ≥ [√(1−ρ²) − (4π/√6)|b|/c_e]_+² μ_Haar(A), provided ρ<1.

This is a *nonperturbative* relative bound in b in its useful small-coupling regime. Its lower coefficient is independent of spectator graph size, the absolute strength of V_other, and cap width. It does not depend on the previous even-parity quadratic cancellation; its degradation is O(|b|). One could pursue an O(b²) bound using center parity and higher sector estimates, but this is not needed for the present multiplicative certificate.

## Archived actual M5 evaluation and independent check

Original source /The Singular Boundary/Source/global_whitney_11face.npz, SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf. The Schur identity was verified numerically: K_ee−K_eB K_BB^-1 K_Be=1/M_ee=1.2855799879953353. With g2²=1, c_e=0.6427899939976677, γ_half=0.4820924954982508, b=3/32000, ρ≈0.0001944647570, the rigorous coefficient is **0.9985040576166548**, uniformly in δ.

A separate SU(2) class-rotor eigensolve in Haar-orthonormal characters U_n(p) tested the same bound at b=0.00009375, 0.01, 0.05, 0.1, all passing. This validates a one-link specialization, **not** a numerical eigensolve of full 30-link interacting Penrose Hamiltonian. Computation source: research/scripts/audit_chord_sector_sobolev_cap.py.

## Refinement obligation and boundaries

For refined geometries, one must prove: (1) each deleted-face chord remains non-tree under a prescribed uniform tree construction and every other retained Wilson face depends on that chord through at most one bounded perturbation of strength b_h (otherwise use total chord-dependent sup norm); (2) the physical ratio ρ_h=8|b_h|M_ee(h)/(3g2²(h)) stays uniformly below the positivity threshold ρcrit=[1+(3S/4)²]^-1/2 (~0.2514 using safe S), and preferably small; (3) other required spectral and continuum estimates independent of cap protection. None of these follows merely from one M5 matrix. The statement does not prove the 3+1D continuum Yang–Mills mass gap.

This corrects the earlier view that global temporal mixing is necessary to achieve uniform-in-cap **finite-regulator** protection. The localization criteria R3-IR-553–555 remain useful for broader response observables and other coupling regimes, but are not necessary for this specific small-coupling protected-chord bound.
