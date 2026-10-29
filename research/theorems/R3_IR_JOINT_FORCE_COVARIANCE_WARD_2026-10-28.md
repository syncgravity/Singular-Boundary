# R3-IR — Exact interacting Wilson joint-force covariance Ward identity and centered-score reduction

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Evidence:** exact finite SU(2) Hamiltonian theorem, plus a conditional fixed-area scaling consequence using previously established actual-vacuum regional Agmon moments. The source covariance, regulator-uniform physical gap, quartic resolvent, original Stage7/Stage26 coefficient correspondence, and full nonlinear continuum **remain open**. No Monte Carlo or alteration of historical files.

## Dependencies and model

The current GitHub branch's `R3_IR_WEIGHTED_SCORE_SECOND_SPECTRAL_MOMENT_2026-10-28.md` (WS-1 through WS-9), `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-1 to VF-8), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), `R3_IR_PHYSICAL_SOURCE_RESPONSE_SPECTRAL_TRICHOTOMY_2026-10-28.md` (PS-1 to PS-3), and `R3_IR_SHARED_EDGE_GAUSSIAN_SECOND_MOMENT_2026-10-28.md` (Gaussian-only benchmark) were inspected. Their finite-model assumptions are maintained, rather than silently promoted to historical Stage26 provenance.

On a finite complete planar rhombus disk, the full link Hilbert space is L²(SU(2)^E), with physical Gauss-invariant reducing sector. Let

`H_h=Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f)`, `p_f=(1/2)ReTr W_f`, `0<a_e≤a_max`, each face has four distinct boundary edges and any edge belongs to at most two faces. The unique positive normalized ground state Ω_h is Gauss invariant, and `ν_h=Ω_h²dHaar`. For a fixed face set D and arbitrary real `|q_f|≤q_*`, set

`Y_h=hΣ_{f∈D}q_f d_f`, `Z_h=hΣ_{f∈D}d_f`, `d_f=1-p_f`.

The true-ground-state diffusion generator and carré-du-champ are

`L_h f = Σ_e a_e [Δ_e f +2∇_e logΩ_h ·∇_e f]`,
`Γ(f,g)=Σ_e a_e∇_e f·∇_e g`.

For every pair of smooth real gauge-invariant multipliers `f,g`, the exact Ward identity holds:

`E_ν[f L_h g]=−E_ν[Γ(f,g)]`, and `E_ν[L_h g]=0`.

Define the split into the explicit Haar-geometric force `D_h` and true vacuum-score force `F_h`:

`D_h=Σ_e a_e Δ_e Y_h=(3h/4)Σ_{f∈D} q_f s_f p_f`, `s_f=Σ_{e∈∂f}a_e`;
`F_h=+2Σ_{e∈S}a_e ∇_e logΩ_h·∇_eY_h`;
`L_h Y_h=D_h+F_h`.

**Sign audit:** the force is `+2∇logΩ·∇Y`. Equivalently, since `∇Y=−hΣ_f q_f∇p_f`, it is `−2hΣ_fq_fΣ_{e∈∂f}a_e ∇logΩ·∇p_f`. Some earlier branch reports wrote `−2∇logΩ·∇Y` in their abbreviated force definition, an algebraic sign typo inconsistent with their correct displayed `L Y` expansion and stationarity calculation. The two abbreviated definitions must be corrected in the live repository before applying JF-1.

## JF-1. Exact joint-force covariance at the original nonlinear coupling

Apply the ground-state Ward identity with `f=D_h, g=Y_h`:

`E_ν[D_h(D_h+F_h)] = −E_ν[Γ(D_h,Y_h)]`.

Therefore, without any approximation, at each finite regulator,

**`E_ν[D_h F_h]=−E_ν[D_h²]−E_ν[Γ(D_h,Y_h)]`.** (JF-1)

Since `E_νF_h=−E_νD_h`, centering gives the exact identity

**`Cov_ν(D_h,F_h)=−Var_ν(D_h)−E_ν[Γ(D_h,Y_h)]`.** (JF-2)

This fixes the previous **unknown mixed** geometric/vacuum-score term. The identity is a physical-sector Ward theorem because D, F, and Y are gauge-invariant scalars: under vertex-gauge transformations, Ω and Y are invariant and L preserves the physical sector. It does not involve the nonphysical constant-link derivative excitations of QH-1.

The more general bilinear result is, for sources `Y_q,Y_r` and corresponding `D_q,F_r`,

**`E[D_q F_r]=−E[D_qD_r]−EΓ(D_q,Y_r)`.** (JF-3)

No symmetry in q/r is claimed separately for the last term.

## JF-2. Explicit O(h) remainder and O(1) geometric-force variance

Because `p_f=1-d_f` and `0<s_f≤4a_max`, write

`D_h=C_h−R_h`, `C_h=(3h/4)Σ_f q_f s_f` (deterministic),
`R_h=(3h/4)Σ_f q_f s_f d_f`, `|R_h|≤3a_max q_* Z_h`.

Using only the local SU(2) identity `|∇_e p_f|²=(1-p_f²)/4≤d_f/2`, four links per face, at most two incident faces per link, and the weighted Cauchy inequality, for any real bounded weights r_f,

`Γ(hΣ_f r_f d_f) ≤4a_max||r||∞² h Z_h` pointwise.

Applying this to Y and R, and then to `Γ(D,Y)=−Γ(R,Y)`, yields the fully explicit bound

**`|Γ(D_h,Y_h)|≤12a_max² q_*² h Z_h`.** (JF-4)

Consequently,

**`|Cov(D_h,F_h)+Var(D_h)|≤12a_max²q_*²h E_ν[Z_h]`.** (JF-5)

The regional vacuum comparison and Agmon theorem, under the *declared fixed physical region* with `b_f≥β_min/h²`, `Δ_D≤C_E/h³`, and a full interior collar, yield `E Z_h≤C_Z`, `E Z_h²≤C_{Z,2}` uniformly. Therefore

**`Var_ν(D_h)≤9a_max²q_*²C_{Z,2}=O(1)`**, and

**`Cov_ν(D_h,F_h)=−Var_ν(D_h)+O(h)`**. (JF-6)

This is an exact cancellation of the mixed geometric/score fluctuations to the stated order. It does **not** imply an upper bound on the variance of F itself.

## JF-3. Exact second-spectral-moment law and the corrected obligation

For the centered physical source `A_h=(Y_h−E_νY_h)/√h`, the positive Gauss-invariant spectral measure has exact second energy moment

`m2_h=||K_h A_hΩ_h||²=(1/h)E_ν[(L_hY_h)²]`.

Expanding the square and inserting JF-1 gives

**`h m2_h=E_ν[F_h²]−E_ν[D_h²]−2E_ν[Γ(D_h,Y_h)]`.** (JF-7)

The means cancel (`E F=−E D`), so equivalently

**`h m2_h=Var_ν(F_h)−Var_ν(D_h)−2E_ν[Γ(D_h,Y_h)]`.** (JF-8)

Under JF-4 and the bounded geometric variance, the difference obeys

**`|h m2_h−Var_ν(F_h)|≤9a_max²q_*²C_{Z,2}+24a_max²q_*²C_Z h=O(1)`.** (JF-9)

Thus **`m2_h=O(h^{-1})` is equivalent to `Var_ν(F_h)=O(1)`** along the fixed-physical-support sequence. No unverified cancellation of a large mixed term remains: the mixed term is exactly known. The genuinely unknown quantity is the centered *vacuum-score force* variance, not merely the mean score, and it is unbounded by the current Fisher estimate. Previous WS-6 gives only `m2_h=O(h^{-3})` and therefore at most `Var(F_h)=O(h^{-2})`.

For uniform electric coefficient `a_e=a`, `s_f=4a` and `D_h=3ahΣ_f q_f−3aY_h`, whence

`Γ(D_h,Y_h)=−3aΓ(Y_h)`, `Var(D_h)=9a²Var(Y_h)`.

Hence the particularly transparent **exact** identity

**`h m2_h=Var(F_h)−9a²Var(Y_h)+6a E_ν[Γ(Y_h)]`.** (JF-10)

It is possible for `m2_h=Θ(h^{-1})` and `Var(A_h)→0` while a physical source-specific gap stays positive, as the previously audited Gaussian tangent explicitly illustrates; the Gaussian result is *not* being transferred to nonlinear SU(2).

## JF-4. Deterministic, genuinely interacting SU(2) gauge-invariant one-plaquette test

Take the exact one-plaquette **physical** class-function Hamiltonian for four equal electric link coefficients `a=1` and genuine magnetic coupling `b=5`:

`H_b χ_n = [a n(n+2)+b]χ_n −(b/2)(χ_{n−1}+χ_{n+1})`, with `χ_n(p)=U_n(p)` (Chebyshev II, χ_{−1}=0).

The source is `Y=h(1-p)` with h=0.1. The SU(2) Haar-class measure is `ρ0(p)=2√(1−p²)/π`. In this **interacting** vacuum,

`D(p)=3ahp`, `F(p)=−2ah(1−p²)Ω_b'(p)/Ω_b(p)`,
`Γ(D,Y)=−3a²h²(1−p²)`.

A deterministic character-basis tridiagonal diagonalization (N=24,36,48) and exact SU(2) Gauss–Chebyshev quadrature give stable values:

`E0=3.404460441011`, `E[DF]=−0.017087825124`,
`−E[D²]−EΓ(D,Y)=−0.017087825124`,
`Cov(D,F)=0.007615798928`, `−Var(D)−EΓ(D,Y)=0.007615798928`,
`m2_h=0.325527660402` both from the joint-force Ward formula and independently from the physical spectral Jacobi matrix, with `|E[L Y]|<2×10^(−17)`.

This is a deterministic numerical illustration, not an exact proof by finite matrix truncation and not a Monte Carlo sample. The general theorem is established by the above exact ground-state Dirichlet calculus. The local script also checks the exact SU(2) Casimir and the canonical three-face, ten-edge **spatial** Penrose fixture; no temporal Q14 test is implied.

## Corrected critical path

**Proved:** the entire geometric/score *mixed* covariance is explicit (JF-1/JF-2), with O(h) remainder after centering (JF-5) and a uniform geometric-force variance (JF-6); the nonlinear physical source's second spectral moment reduces **exactly** to a centered-score variance (JF-8). These are valid at finite SU(2) Wilson coupling, unlike the separate Gaussian tangent benchmark.

**Still open:** independent `Var(F_h)=O(1)` for the actual finite interacting vacuum at fixed physical support; bounds on `Var(A_h)` above or below by positive constants; regulator-uniform physical excitation gap; all-sector physical quartic resolvent; full continuum, and Stage7/26 action/provenance.

**Next noncircular route:** use a derivative of the *gauge-invariant* vacuum-score force or a conditioning argument to estimate `Var(F_h)`, possibly through a second-order Ward/Bochner relation with explicit mixed-link and score-Hessian terms. Do not assume log-concavity or a physical gap. The new exact identity eliminates the mixed covariance as a separate open unknown but not the residual variance itself.