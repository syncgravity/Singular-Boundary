# R3-IR — Excited-state curvature Ward identity and very-soft/high-energy decoupling
**Date:** 2026-10-28. **Proof classification:** independently proved at fixed finite SU(2) regulator under explicitly declared geometric/coupling assumptions; *not* a proof of the nonlinear quartic spectral response, physical gap or continuum. No simulations.

## Primary sources and audit
Current GitHub audit branch was read directly: \`research/theorems/R3_IR_QUARTIC_SPECTRAL_WARD_AUDIT_2026-10-28.md\` (QR-2/QR-5); \`R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md\` (SU2 Casimir local Dirichlet); \`R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md\` (MI-3); \`R3_IR_PARITY_RESOLVED_SECOND_RESPONSE_2026-10-28.md\` (quartic identity). Canonical spatial three-face Penrose seed fixture: 10 links, each face four edges, link multiplicity at most two. **Not** full Q14. The claimed equality of original Stage7/26 action and the declared Hamiltonian remains unverified.

## Set-up
Let G=(V,E,F) be a finite face-complete rhombus complex, with four distinct edges per face and at most two faces per edge. On L²(SU(2)^E), consider
 H = H_E + V,    H_E = Σ_e a_e(-Δ_e),    V = Σ_f b_f(1-p_f),
where p_f = ½ReTr(W_f), 0<a_e≤a_max and b_f≥0. Use -Δχ_j=j(j+1)χ_j so |∇_e p_f|²=(1-p_f²)/4 for e∈∂f. The compact finite configuration space has a simple strictly positive gauge-invariant ground state Ω; E0 is the ground energy and K=H-E0≥0. Statements remain true after restricting to the physical Gauss-invariant subspace, because H and every source below commute with gauge transformations.

Assume on a selected region D⊆F the magnetic coefficients satisfy b_f≥β_min h^-2 (β_min>0), and across all faces b_f≤β_max h^-2; assume Fh²≤A0, a_e≤a_max. Choose a fixed bounded real test φ and q_f=σ_f φ(x_f), |q_f|≤q_max; for α∈R set
 A=A_{h,α}=h^(2-α) Σ_{f∈D}q_f p_f,
 c=h^(2-α) Σ_{f∈D}q_f,
 B=A-cI=−h^(2-α) Σ_{f∈D}q_f d_f, d_f=1-p_f∈[0,2].
The deterministic subtraction c (not the vacuum mean) changes no off-diagonal spectral transitions: P_>Λ A P_≤η=P_>Λ B P_≤η, Λ>η≥0.

Let P_≤η=1_[0,η](K) and P_>Λ=1_(Λ,∞)(K), optionally both intersected with the physical subspace. Put
 Γ(A)=Σ_e a_e |∇_e A|²
as a nonnegative multiplication operator.

## Theorem EX-1: positive-potential low-excitation curvature bound
For every unit vector ψ∈Ran P_≤η (not just Ω),
 Σ_{f∈D}〈ψ,d_f ψ〉 ≤ h²(E0+η)/β_min.                  (EX-1)
Proof: 0≤(β_min/h²)Σ_D d_f ≤V≤H as quadratic forms. Moreover 〈ψ,Hψ〉≤E0+η. No mixing, resolvent or spectral gap hypothesis is used.

A global, noncircular ground-energy trial already audited in \`R3_IR_STRONG_FIELD_MEAN_CURVATURE_AND_TORQUE_LIMIT_2026-10-28.md\` yields
 E0≤(3/√2)√[(Σ_e a_e)(Σ_f b_f)] ≤3√2 F√(a_max β_max)/h.
Therefore normalized *low-excitation* states have a mean curvature deficit O(h) when averaged over a physical area with face count comparable to h^-2, as long as η=o(h^-3). This is not a facewise or joint curvature estimate. The constant includes total physical area A0 (not infinite-volume uniform).

## Theorem EX-2: exact excited-state local f-sum/Ward identity
On the common smooth form core,
 [A,[H,A]]=2Γ(A),    Γ(A)=Σ_e a_e |∇_e A|².             (EX-2)
The Wilson magnetic multiplication potential drops out exactly. By edge incidence at most two, Cauchy-Schwarz, and 1-p_f²≤2d_f,
 Γ(A)(U) ≤ 4a_max q_max² h^(4-2α) Σ_{f∈D}d_f(U).       (EX-3)
Thus
 ||P_≤η Γ(A) P_≤η|| ≤(4a_max q_max²/β_min) h^(6-2α)(E0+η).  (EX-4)
This controls a local kinetic source form in **all** low-energy interacting states, rather than using the full electric energy of those states as in QR-5. It is pointwise curvature-weighted, all positive magnetic couplings.

For any unit eigenvector ψ of K with eigenvalue ε≤η, the exact double commutator gives
 〈Aψ,(K-ε)Aψ〉=〈ψ,Γ(A)ψ〉.                           (EX-5)
In particular, for a genuine SU2 one-rhombus electric character state χ_(1/2) (ε=3a), the two lower/upper character channels give (-3a)/4+(8a-3a)/4=a/2, exactly equal to the SU2 gradient expectation a(1-〈p²〉)=a/2. For the electric vacuum, both sides equal 3a/4. These are exact Peter-Weyl identities, not simulations.

## Theorem EX-3: vacuum-independent spectral-band transfer estimate
The double commutator gives a **quadratic-form operator identity**
 P_≤η B K B P_≤η
 =P_≤η Γ(A)P_≤η + ½{K_≤η,P_≤η B²P_≤η}.
Here K_≤η=P_≤η K P_≤η, and B is a real self-adjoint multiplier. Since B differs from A by a constant, Γ(B)=Γ(A). The elementary pointwise inequality
 (Σ_{f∈D}d_f)²≤2|D|Σ_{f∈D}d_f
implies
 ||B P_≤η||² ≤ (2|D|q_max²/β_min) h^(6-2α)(E0+η).  (EX-6)
Since K_≤η≤ηP_≤η and K≥ΛP_>Λ, operator norm estimates give
 **||P_>Λ A P_≤η||²
 ≤ [2q_max²/(β_min Λ)] h^(6-2α)(E0+η)(2a_max+η|D|).**  (EX-7)
This is an exact source-specific separated-band bound. It is noncircular; it depends only on finite positive Wilson couplings, source size and the global upper bound on E0, and not on an assumed physical gap.

The gain compared with QR-5 is that high-energy transitions are bounded using a **low-excitation magnetic-curvature expectation** rather than ∑_e a_e||∇ψ||²≤E0+η. The gain is strongest when η is genuinely small; it does not automatically solve the full intermediate-window problem.

## Precise scaling and honest limit
For α=3/2 with |D|≤F≤A0/h², E0≤C_E A0/h³ and Λ_h=h^(-1-δ), δ∈(0,1) fixed, (EX-7) gives
 ||P_>Λ_h A P_≤η||² ≤C [h^(1+δ)+η h^(-1+δ)+η h^(4+δ)+η² h^(2+δ)]
for sufficiently small h (coarse powers depend on fixed A0). In particular, for η_h=O(h),
 **||P_>h^(-1-δ) A P_≤O(h)|| =O(h^(δ/2))**.  (EX-8)
The source does not transmit very-soft excitations of energy O(h) into extremely high excitations above h^(-1-δ) with order-one amplitude. Neither O(h) states nor a lower spectral gap are presumed to exist; if the spectral window is empty the estimate is vacuous. For η fixed positive, this bound is generally too weak to decay when δ<1; it does not control all relevant middle energies or the quartic inverse-energy response.

**Important dimensional note:** h powers refer to the fixed declared physical Hamiltonian normalization with energy measured in its physical time units; conclusions cannot be transferred to an unverified Stage26 implementation or another regulator's temporal normalization.

## Research consequence and next noncircular gate
**Proved:** EX-1 low-energy state curvature density, EX-2 exact excited-state f-sum, EX-3 separated-band transition bound and very-soft-to-UV corollary, all for genuine nonlinear finite SU2 Wilson Hamiltonians under displayed coefficients.
**Open:** uniform local (not globally averaged) excited-state curvature estimates, transitions from excitations of fixed positive physical energy to the cutoff h^(-1-δ), the odd/even resolvent norms G_o X and G_e S, the quartic response, interacting field variance, spatial continuum and mass gap.
**Next proof target:** derive a localized relative-energy/conditional Caccioppoli estimate for low **excited** states which replaces the η|D| term in EX-7 by a term that is o(h^(-1-δ)) at fixed η, without assuming a gap or ground-state mixing. Alternatively prove a direct quartic response cancellation for the physical SU2 source. A uniform positive gap or transfer contraction may not be assumed as input.

All historical archives and original certificates remain unchanged; no Monte Carlo performed.
