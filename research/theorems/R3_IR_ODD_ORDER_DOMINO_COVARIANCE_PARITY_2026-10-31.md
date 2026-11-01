# R3-IR — Exact all-odd-order cancellation of SU(2) domino covariance

2026-10-31; original-link SU(2) on a simply connected finite planar disk.

Let K=−Σ_e a_eΔ_e, B=Σ_(k≠f)b_k, P=Σ_(k≠f)b_k p_k, and H_λ=K+λ(B−P). The finite planar face-edge incidence equations over F₂ admit a central-link sign assignment z_e∈{±1} such that each plaquette boundary has product −1. Define S(U)_e=z_eU_e. The involution preserves product Haar and the original-link Laplacian, flips every elementary plaquette trace, and obeys the **exact operator conjugation** 𝕊⁻¹H_λ𝕊=H_(−λ)+2λB.

By uniqueness/positivity of the normalized finite-volume ground state, Ω_(−λ)(U)=Ω_λ(SU) for all real λ. Every two-face domino outer-boundary Wilson trace r_i is invariant under S, so **Cov_νλ(r_i,r_j)=Cov_ν(−λ)(r_i,r_j)** identically. Analytic perturbation theory implies **all odd coupling derivatives of every domino-loop covariance at λ=0 vanish**, including the previously open cubic term. Consequently Cov=δ_ij/4+λ² M_ij/2+λ⁴ N_ij/24+O(λ⁶) in fixed finite volume.

On N×N square disks one explicit sign assignment is z_(horizontal row y)=(−1)^y and z_(vertical)=+1. A reproducible original-link SU(2) quaternion checker verified 7,896 plaquette/domino character identities on 3×3,5×5,9×9,21×21 disks with zero numerical residual. This establishes symmetry but not the fourth-order coefficient N, uniform Taylor remainder, covariance at physical coupling λ=1, signed current or continuum Yang–Mills gap.

Complete proof, executable checker, JSON results and SHA256 manifest: Library /The Singular Boundary/Proof Audits/R3_IR_ODD_ORDER_DOMINO_COVARIANCE_PARITY_2026-10-31.zip.