# The Singular Boundary — Two-scale physical Wilson spectral band and the infrared boundary layer

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Evidence:** exact finite-Hilbert-space spectral theorems applied to the *actual* interacting SU(2) Wilson ground state, conditional only on the previously recorded Penrose regional, Agmon and third-spectral-moment hypotheses. **Not claimed:** a positive regulator-uniform physical gap, finite-energy source survival, a variance upper bound of order h, a nonzero limiting field, nonlinear quartic resolvent, full continuum construction, or Stage7/26 source identity. No Monte Carlo.

## 1. Rechecked dependencies and definitions

Directly inspected the current GitHub branch's `R3_IR_ENERGY_WEIGHTED_PHYSICAL_SPECTRAL_COMPACTNESS_2026-10-28.md`-predecessor results in the prior dialogue, `R3_IR_PHYSICAL_THIRD_MOMENT_LOCAL_COMMUTATOR_2026-10-28.md` (TS-1–TS-13), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), `R3_IR_PROBABILITY_WEIGHTED_MAGNETIC_CONVEX_CORE_2026-10-28.md` (PC-1), and `R3_IR_PHYSICAL_SOURCE_RESPONSE_SPECTRAL_TRICHOTOMY_2026-10-28.md` (PS-1). The first- and third-moment inputs are used *as assumptions established in those earlier theorems under their explicit coefficient, geometry and collar conditions*: no original Stage26 identification is inferred.

Finite SU(2) Wilson Hamiltonian `H_h=Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f)` on a face-complete planar rhombus disk; true normalized strictly positive Gauss-invariant ground state Ω_h and physical positive operator `K_h=H_h−E0,h`. For a fixed physical support D_R and real bounded test q_f define

`Y_h=hΣ_{f∈D_R}q_f(1-p_f)`, `A_h=(Y_h−E_νY_h)/√h`, `Z_h=hΣ_{f∈D_R}(1-p_f)`.

Let μ_h be the **physical** excitation spectral measure of A_hΩ_h (not a nonphysical constant-link derivative), with `v_h=∫dμ_h`, `m_{k,h}=∫E^k dμ_h`. For **nonzero nonnegative macroscopic tests** (and the relevant electric lower bound), prior independent theorems yield positive constants m_*, M_1, M_3 (uniform in h under the declared geometry):

`m_*≤m_{1,h}≤M_1`, `m_{3,h}≤M_3/h²`.

From the regional AG-1/PC-1 exponential moment, `sup_h E_ν[Z_h²]≤M_Z<∞`. Since `|Y_h|≤q_*Z_h`,

`v_h=Var_ν(Y_h)/h≤q_*²M_Z/h=:V/h`.

The constants m_*, M_1, M_3, V are assumed positive. For signed q without a positive first-moment lower bound, the theorem holds with the corresponding actual lower bound if established independently; this report does not silently grant it.

Define the energy-weighted measure Σ_h on `ξ=hE` by `Σ_h(B)=∫_{hE∈B} E μ_h(dE)`. Then `Σ_h` is a nonzero finite measure with mass m1, and `∫ξ² dΣ_h=h² m3≤M_3`.

## 2. Theorem SB-1 — Unconditional intermediate *physical-energy* band for the nonlinear vacuum

**Exact two-sided removal of ultrasoft and ultraviolet contributions.** For all δ,R>0 and h>0,

`∫_{(0,δh)}E μ_h(dE) ≤ δh v_h ≤ δ V`,

`∫_{(R/h,∞)}E μ_h(dE) ≤ h² m_{3,h}/R² ≤ M_3/R²`.

Set **δ=m_*/(4V)** and **R=2√(M_3/m_*)**. For all sufficiently small h so that δh≤R/h, the actual physical source obeys

**(SB-1)** `∫_[δh,R/h] E μ_h(dE)≥ m_*/2`.

This improves the previous one-sided `(0,R/h]` spectral window by removing ultralow physical energies `E<δh`. In particular, for any positive function `e_h=o(h)`, the energy-weighted mass below e_h is `O(e_h/h)=o(1)`. Thus ultrasoft eigenstates may exist, but **they cannot carry an order-one share of this Wilson source's first spectral moment below energies o(h)**.

The prior spectral Cauchy–Schwarz and third moment give `m_{2,h}≤√(M_1M_3)/h`. Applying Cauchy–Schwarz to the same band,

**(SB-2)** `μ_h([δh,R/h])≥ [m_*²/(4√(M_1M_3))]h`.

No lower bound independent of h follows. The full physical mass gap may be much smaller than δh because the theorem constrains only the selected source's energy-weighted spectral mass.

## 3. Theorem SB-2 — Exact rescaled infrared boundary-layer formula and corrected proposed gate

For any ε>0, `Σ_h((0,ε])≤(ε/h)v_h≤Vε/h²`. Therefore

**(SB-3)** `Σ_h((0,ε])≤min{M_1,Vε/h²}`.

Any `ε_h=o(h²)` has `Σ_h((0,ε_h])→0`; this **does not** exclude a limiting atom of Σ at ξ=0 because all intermediate scales `ε_h≈h²`, `ε_h≈h` and `ε_h≈√h` can still collapse to zero as h→0.

For any physical cutoff Λ>0 the exact boundary-layer inversion is

**(SB-4)** `μ_h((0,Λ])=h∫_{(0,hΛ]} ξ^(−1) Σ_h(dξ)`,

and the full source variance and Euclidean covariance are

**(SB-5)** `v_h=h∫_(0,∞) ξ^(−1)Σ_h(dξ)`,

**(SB-6)** `C_h(t)=h∫_(0,∞)ξ^(−1)e^(−tξ/h)Σ_h(dξ)`.

The shrinking **width h** near ξ=0 in SB-4 corresponds to *fixed physical energies* E≤Λ. It is incorrect to identify ξ→0 solely with a physical zero-energy excitation. This is a two-scale statement; the normalized energy-current response `−C_h'(hτ)=∫e^(−τξ)Σ_h(dξ)` captures different information from C_h(t) at fixed t>0.

**Correction to the prior proposed sufficient gate.** Suppose one proves, for all sufficiently small h and every 0<ε≤1, the strong uniform bound `Σ_h((0,ε])≤K ε^(1+η)` with fixed K and η>0. Stieltjes integration by parts gives

`∫_(0,1] ξ^(−1)Σ_h(dξ)≤K(1+1/η)`;
`∫_(1,∞) ξ^(−1)Σ_h(dξ)≤M_1`.

Therefore

**(SB-7)** `v_h≤h[K(1+1/η)+M_1]→0`.

Such a small-ξ power bound would prove **triviality of this normalized field**; it must not be presented as a necessary condition for a positive Yang–Mills mass gap or for a nontrivial finite-energy source. At the same time, it is mathematically a valid sufficient criterion for `v_h=O(h)`. Its exponent and uniformity need an independent interacting proof.

## 4. Theorem SB-3 — A practical finite-*physical*-time spectral survival criterion

For any fixed t>0 and physical energy Λ>0, positivity and first-moment control give

`e^(−tΛ) μ_h((0,Λ])≤ C_h(t)≤ μ_h((0,Λ])+(M_1/Λ)e^(−tΛ)`.

The first lower bound is one-sided (not an equality), and the second uses `μ_h((Λ,∞))≤M_1/Λ`. It follows, along any chosen refinement subsequence, that the following are equivalent:

(i) `liminf C_h(t)>0` for **some** fixed t>0;
(ii) `liminf μ_h((0,Λ])>0` for **some** fixed physical Λ>0.

For (i)→(ii), choose Λ large enough that `(M_1/Λ)e^(−tΛ)` is less than half the lower bound. For (ii)→(i), use the lower bound for any fixed t>0. This criterion makes *fixed-time* Euclidean source survival an explicit, independently testable dynamical obligation; it does not ask the source variance to vanish, and it does not infer a uniform physical mass gap. Note subtle quantifiers: liminf must hold on the same subsequence, and the chosen Λ may depend on t and the lower bound, not on h.

## 5. Exact witnesses proving the information loss of rescaled compactness

For h∈(0,1), define abstract one-atom positive spectral measures `μ_h=E_h^(−1)δ_(E_h)` with E_h taking each of the following values. In every case `m1=1`, `m3=E_h²≤h^(−2)`, and `v_h=1/E_h≤1/h`.

| Energy E_h | ξ_h=hE_h | Variance v_h | Weak energy-flux limit |
|---|---|---|---|
| h^(-1) | 1 | h | δ_1 |
| h^(-1/2) | h^(1/2) | h^(1/2) | δ_0 |
| 1 | h | 1 | δ_0 |
| h | h² | h^(-1) | δ_0 |

Thus the *same weak limit* Σ→δ_0 is consistent with vanishing source variance, nonzero finite source variance and divergent source variance. The lower band E≥δh is sharp at the level of these moment hypotheses, because the last example saturates the v_h≤1/h envelope. These are **abstract spectral witnesses**, not actual SU(2) Wilson vacua or a refutation of the true model's mass gap.

## 6. Conclusions and honest next proof obligations

**New conclusions for the true interacting finite Wilson model under the earlier declared hypotheses:** (1) a nonzero fraction of the first physical source energy moment lies in [δh,R/h], (2) the unweighted physical source measure carries at least c h mass in the same band, and (3) no O(1) first energy-moment mass lies below energies o(h). The constants are explicit in terms of the existing regional estimates. The proposed small-ξ power gate has been reclassified as a field-collapse criterion, not a required mass-gap step. Fixed physical-time Euclidean covariance survival is exactly equivalent to finite physical-energy source mass survival under the first moment bound.

**Still OPEN:** prove finite physical-time source covariance survival for actual nonlinear Penrose vacuum, or independently establish variance upper/lower at physical normalization; source-specific inverse-energy quartic resolvents; full physical regulator-uniform gap for *every* excitation; quantum continuum and Stage7/26 source provenance. The source spectral band includes E~h and E~h^(−1), so it is *not* a gap theorem. An appropriate next calculation is an explicitly Gauss-invariant, source-conditioned Euclidean lower bound at some fixed t>0, not suppression of all ξ→0 energy flux.

**Reproducibility:** Accompanying deterministic exact-rational spectral verifier checks the band constants, inversion identities, Stieltjes argument and all four sharp examples. It does not numerically simulate the true SU(2) vacuum, certify Stage26 or replace any historical data.
