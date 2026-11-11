# R3 P2/T2 — Coupled cubic SU(2) vacuum-to-Wilson-flow averaged-curvature bound
**2026-11-06 · proposed finite-regulator theorem, independent review pending · continuum gates OPEN**

Let H=αΣ_e C_e+βΣ_p ℓ(U_p), where C_e=−Δ_e for generators iσ_j/2, ℓ(U)=1−½tr₂U, α=g₀(h)²/(2h), β=2/[g₀(h)²h]. Let E and P be counts of original links and plaquettes in a finite open cubic lattice. The strictly positive interacting full-space ground state is gauge invariant by uniqueness and gauge symmetry; its probability law is ν=Ω² Haar.

**Theorem (volume-uniform averaged defect, before and after full classical non-Abelian flow).** For all s≥0,

    E_ν[ |P|⁻¹ Σ_p ℓ(U_p(Φ_s U)) ] ≤ (3g₀(h)²/2) sqrt(|E|/|P|).

Here Φ_s is the original-link classical gradient flow dU_s/ds=−∇Σℓ_p(U_s). For an open n×n×n grid, |E|=3n(n+1)² and |P|=3n²(n+1); thus the upper bound is ≤(3/√2)g₀(h)², uniformly in n and s, including s=τ/h².

**Proof.** Put x(u)=½tr₂u. Use the independent-link *trial wavefunction* F_t(U)=∏_e z_t⁻¹ᐟ² exp(t x(U_e)), where z_t=I₁(2t)/t. The scalar link expectation is ∫u|f_t|²du=r_t I with r_t=I₂(2t)/I₁(2t), 0<r_t<1 and 1−r_t≤3/(2t). Integration by parts using Δx=−3x/4 gives exactly ∫|∇f_t|²=(3t/8)r_t≤3t/8. For any plaquette with four distinct links, ∫ℓ_p|F_t|²=1−r_t⁴≤6/t. Thus the full-space Rayleigh quotient is ≤(3α|E|/8)t+6β|P|/t. The full-space lowest eigenfunction is unique positive and gauge invariant, so its energy E₀ equals the Gauss-invariant ground energy, and non-gauge-invariant trial F_t is legitimate for the energy upper bound. Optimizing t=4sqrt(β|P|/(α|E|)) yields E₀≤3sqrt(αβ|E||P|). Since C_e≥0, β E_ν Σℓ_p≤E₀. Since the *exact nonlinear full SU(2) flow* decreases S=Σℓ_p pathwise, S(Φ_sU)≤S(U), the bound transfers to every s≥0 without requiring bounded initial classical action. □

For ε,η>0 define the fraction of bad plaquettes F_ε(s)=|P|⁻¹#{p:ℓ(U_p(Φ_sU))>ε}. Then the same proof and Markov yield
ν(F_ε(s)>η)≤min{1, [3g₀(h)²/(2εη)]sqrt(|E|/|P|)}, for each s≥0. This concerns a fixed lattice-unit threshold and is NOT a bound on sup_s F_ε(s).

**Important limitation.** The physical classical curvature-energy density is (8/hV)Σ_pℓ_p, so on fixed volume V, |P|~3Vh⁻³, our estimate only bounds its expectation by O(g₀(h)²h⁻⁴); that typically diverges along weak bare coupling. Smooth continuum curvature requires plaquette defects O(h⁴), far beyond the O(g₀²) bound here. Thus this is a valid nontrivial quantum-to-classical-flow transfer but does NOT close the flowed renormalized-curvature, infrared, continuum or Penrose/quantum-gravity gates.

Reproducibility: 281 deterministic calibration assertions passed (grid counts n=1..100, Bessel inequalities, trial-energy optimization). Executable Python script, log, full report, SHA-256 manifest and integrity-tested ZIP are persisted in Library /The Singular Boundary/Proof Audits/. Source: existing exact nonlinear classical spatial flow theorem R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md. No canonical theorem status upgraded.
