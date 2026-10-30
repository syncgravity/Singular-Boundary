# R3-IR — Ground-state relative-energy neck criterion for moderate SU(2) curvature

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`.  
**Status:** New exact finite-volume ground-state relative-energy / spectral-neck theorems, plus their conditional fixed-physical-area Agmon consequence. **Not** a proof of the missing connected covariance concentration, a positive uniform gap, Stage 7/26 coefficient provenance, or R2 reconstruction.

## Source audit and definitions

Directly checked the current audit-branch manuscripts `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md`, `R3_IR_MODERATE_CURVATURE_CONCENTRATION_GATE_2026-10-28.md`, `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md`, `R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md`, and their local stored verification fixtures. The regional Agmon weighted moment and the fundamental SU(2) gradient identity were rederived. This theorem treats the **actual vacuum**, not the positive two-branch trial state from the prior result.

Let `H_h=Σ_e a_e(-Δ_e)+Σ_f b_fd_f` on the finite gauge-invariant SU(2) link Hilbert space, `d_f=1−(1/2)ReTr W_f`, `0<a_e≤a_max`, every face has four edges and every edge belongs to at most two faces. Let `Ω_h>0` be the unique normalized physical ground state, `E0=inf σ(H_h)`, `ν_h=Ω_h² dHaar` its true probability law, and `K_h=H_h−E0`. Denote the **physical** finite spectral gap by `Δ_h=inf(σ(K_h|physical)\{0})>0` (strictly positive at any fixed finite graph; no regulator-uniform lower bound is presumed).

Fix a face set `D`, a bounded real smooth-source weight vector `|q_f|≤q_*`, and define

`X_h=Σ_{f∈D}d_f`, `Z_h=h X_h≥0`, `Y_h=hΣ_{f∈D}q_fd_f` (possibly signed).

At the `α=3/2` normalization, the centered Wilson field is `−h^(−1/2)(Y_h−E_ν Y_h)`. Its fixed-support vacuum collapse criterion is **`Var_ν(Y_h)=o(h)`**.

## Theorem NE-1 — Exact nonlinear SU(2) source-induced one-dimensional ground-state Dirichlet form

The exact ground-state transformation gives, for every real Lipschitz function `g` on the compact range of `Y_h`, 

`〈g(Y_h)Ω_h,(H_h−E0)g(Y_h)Ω_h〉=E_ν[Γ(g(Y_h))]`, where `Γ(F)=Σ_ea_e|∇_eF|²`.

The SU(2) fundamental Casimir and face-edge incidence imply the **pointwise**, non-Gaussian bound

**`Γ(Y_h)≤4a_max q_*² h² X_h=4a_max q_*² h Z_h`.** (NE-1)

Consequently `Γ(g(Y_h))=|g'(Y_h)|² Γ(Y_h)` a.e. in the ground-state measure. The source's entire one-dimensional pushforward Dirichlet form is determined exactly by the conditional coefficient `γ_h(y)=E_ν[Γ(Y_h)|Y_h=y]` and its pushforward probability `μ_h=(Y_h)_*ν_h`:

**`E_ν[Γ(g(Y_h))]=∫|g'(y)|²γ_h(y) μ_h(dy)`.** (NE-2)

This is an identity in the actual interacting vacuum, not a claimed uniform conditional Poincaré inequality. It makes explicit the mathematical object that must be estimated to control moderate-curvature phases. If `μ_h(dy)=ρ_h(y)dy` and `ρ_hγ_h>0` a.e. across a specified interval `[u,v]`, the minimum Dirichlet cost for a scalar function rising from 0 to 1 between the endpoints is the elementary one-dimensional capacity

`cap_h(u,v)=[∫_u^v dy/(ρ_h(y)γ_h(y))]^(−1)`, with the usual variational interpretation if the integral is infinite. This formula alone does not lower-bound that capacity or yield the mass gap.

## Theorem NE-2 — Exact two-band relative-energy and physical-gap upper bounds

Fix real numbers `u<v` and write `w=v−u>0`. Let

`p_- = ν_h(Y_h≤u)`, `p_+ =ν_h(Y_h≥v)`, `p_0 =ν_h(u<Y_h<v)`.

Assume `p_-p_+>0`. Set the 0-to-1 Lipschitz cutoff `g(y)=0` for `y≤u`, `g(y)=(y−u)/w` for `u<y<v`, and `g(y)=1` for `y≥v`. Write `B={u<Y_h<v}` and `ζ_h=E_ν[Z_h 1_B]`.

The **normalized branch-localized physical trial vector** `ψ_+=g(Y_h)Ω_h/||g(Y_h)Ω_h||` has exact relative energy

`〈ψ_+,(H_h−E0)ψ_+〉= E_ν[Γ(g(Y_h))]/E_ν[g(Y_h)²]`

and hence obeys

**`〈ψ_+,(H_h−E0)ψ_+〉≤4a_max q_*² h ζ_h/(w²p_+)`.** (NE-3)

The **orthogonal** vector `χ=[g(Y_h)−E_ν g(Y_h)]Ω_h` is gauge invariant and satisfies

`Var_ν(g(Y_h))=||χ||²≥p_-p_+`, because the independent-pair variance formula collects the low/high pair contributions `p_-p_+·(1−0)²`. The Rayleigh–Ritz principle therefore gives the exact finite-model physical-gap upper bound

**`Δ_h≤4a_max q_*² h ζ_h/(w²p_-p_+)`.** (NE-4)

In particular, these statements hold for the true interacting Wilson vacuum at any positive magnetic coupling, with **no assumed lower bound on `Δ_h`**. They are conditional *upper* bounds on relative energy and the actual gap, not lower bounds or a solution of the gap problem.

For an unsigned regional curvature source `q_f=1`, `Y_h=Z_h`, one has `ζ_h≤v p_0`, giving the clean neck criterion

**`Δ_h≤4a_max h v p_0/(w²p_-p_+)`.** (NE-5)

If a vacuum had two separated moderate-curvature bands with probabilities `p_-≥c_0>0`, `p_+≥c_1 h`, `p_0≤C e^(−κ/h²)` at fixed `u,v>0`, then NE-5 would force `Δ_h=O(e^(−κ/h²))`. A positive gap is *not* assumed; the result says that this sharply bimodal scenario produces an explicitly soft physical mode.

## Theorem NE-3 — Signed-source neck estimate using the **actual-vacuum** regional Agmon bound

For the original signed smooth test, `Y_h` need not be nonnegative and `Z_h` can be large on a narrow transition event. Assume the previously proved regional Agmon estimate AG-1 with

`b_f≥β_min h^(−2)` on D, `L_h=C_L/h≥2h²(E0−E_out)/β_min`, and `λ_h=c_λ/h`, `c_λ=√[β_min/(32a_max)]`. The true vacuum obeys

`E_ν[X_h exp(2λ_h(X_h−2L_h)) 1_{X_h≥2L_h}]≤64a_max h²/(β_min L_h)`.

Choose any **fixed** `J>2C_L`. Split `ζ_h=E_ν[Z_h 1_B]` according to `X_h<J/h` or `X_h≥J/h`. On the first event `Z_h≤J`; on the second the Agmon exponential weight is at least `exp[2c_λ(J−2C_L)/h²]`, so

**`ζ_h≤Jp_0+[64a_max/(β_min C_L)]h⁴ exp[−2c_λ(J−2C_L)/h²]`.** (NE-6)

Combining with NE-3/NE-4 gives the *actual-vacuum, signed-source*, nonperturbative spectral-neck estimate

**`Δ_h≤(4a_max q_*² h/(w²p_-p_+)) {Jp_0+[64a_max/(β_min C_L)]h⁴e^(−2c_λ(J−2C_L)/h²)}`.** (NE-7)

The analogous bound with `p_-p_+` replaced by `p_+` controls the relative energy of the normalized band-filtered state `ψ_+`.

For a fixed physical interior region under the declared Penrose coefficient trajectory, the regional energy comparison supplies a uniform `C_L`. Suppose a **hypothetical true vacuum** has a moderate-curvature rare upper band of probability `p_+≥c_1h`, lower band `p_-≥c_0>0`, and an exponentially unlikely neck `p_0≤Ce^(−κ/h²)`, with fixed band separation `w>0`. Then the **unconditional inequality** NE-7 yields the **conditional phase-structure consequence**

**`Δ_h≤C'e^(−min{κ,2c_λ(J−2C_L)}/h²)×(1+h⁴)`**, up to harmless h-independent factors. In particular the rare moderate-curvature two-branch mechanism from the prior exact trial-state witness, **if it occurred as the true vacuum**, would necessarily create a very soft, finite-volume *physical* excitation.

This does not forbid the mechanism without an independently established uniform gap. The true ground-state distribution's band masses are not determined by the Agmon theorem. Nor does this prove the sought `Var_ν(Y_h)=o(h)`: a single unimodal band can fluctuate on the natural `√h` scale and have `Var(Y_h)≈c h` without any narrow neck between two well-separated moderate-curvature phases.

## Exact SU(2) fixture and independent reproducibility

`verify_neck.py` performs only exact symbolic and deterministic quadrature checks. On one open SU(2) rhombus with the **pure electric** physical Hamiltonian `H_E=4a(−Δ_class)` and Haar class-trace coordinate `p=ReTr(U)/2`, the true vacuum law has density `ρ(p)=2√(1−p²)/π`, and the physical gap is exactly `3a` by the fundamental character. With `a=1`, `h=1`, `Y=1−p`, `u=1/2`, `v=3/2`, it finds `p_-=p_+=1/3−√3/(4π)=0.19550110947789…`, `p_0≈0.60899778104423`, the **exact Rayleigh quotient of g(Y)Ω** approximately `3.82008064759>3`, and the deliberately coarse NE-5 upper bound approximately `95.6023368056>3`. This is a genuine one-face SU(2) test of the variational inequality, not a fit or a claim about positive magnetic coupling; AG-1 is invoked only in the separate b_f>0 corollary. The canonical 3-face Penrose Z⁵ spatial incidence is also checked; it is not the recovered Q14 temporal cavity.

All operations are read-only relative to the original numerical and archive files; no Monte Carlo was performed. The verifier checks constants and a finite SU(2) fixture, while the general theorem follows from the written operator argument.

## Outstanding obligation and evidence gate

**Proved:** NE-1 exact interacting pushforward Dirichlet form and curvature bound; NE-2 relative energy / physical gap upper bound through a moderate-curvature neck; NE-3 Agmon-refined signed-source neck bound, conditional on the earlier ground-state tail theorem and stated geometry. These are **new necessary conditions** for moderate two-phase coherence, not a vacuum concentration theorem.

**Open:** establish from the actual nonlinear Hamiltonian a *positive lower bound on neck probability* or an independent energy penalty for moderate source-density splitting **without assuming the desired gap**, or rule out *unimodal* `O(√h)` coherent fluctuations. Neither existing regional Agmon control nor upper energy comparisons produce the target `Var_ν(Y_h)=o(h)`. The fixed-support three-/four-source response, all-regulator Stage 26 source provenance, infinite-volume physical gap and R2 quantum continuum remain open.
