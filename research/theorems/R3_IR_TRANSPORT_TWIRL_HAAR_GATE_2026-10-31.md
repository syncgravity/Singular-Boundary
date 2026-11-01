# R3-IR — Transport-twirl Haar comparison and spectral-gap cost

**Date:** 2026-10-31. **Status:** exact *conditional finite-volume* comparison theorem, not an established SU(2) interior transport or a regulator-uniform current estimate.

On the full original-link Haar Hilbert space let H=H_f⁻, Ω>0 normalized, E₀ its simple ground energy, and γ>0 its first full-link excitation gap (finite volume). **Assume** a measurable family of Haar-preserving bijections T_g indexed by g∈SU(2) with V_−∘T_g=V_− and W_f(T_gU)=gW_f(U). Their existence for every completed cage is not proved by the archived M55 six-link cut. Define P_gf=f∘T_g, Ω_g=P_gΩ and Q_g=⟨Ω_g,(H−E₀)Ω_g⟩.

For every bounded target-holonomy test 0≤q≤1, set m_q=∫Ω²q(W_f)dμ and h_q=∫_SU2 q(g)dg. The change of variables U→T_gU, then averaging over g, gives **exact target Haar twirling**: ∫dg∫Ω_g²q(W_f)dμ=h_q.

The vacuum overlap c_g=⟨Ω,Ω_g⟩ satisfies 0≤c_g≤1. The spectral theorem yields Q_g≥γ(1−c_g²). The elementary total-variation/Hellinger inequality for the two positive normalized amplitudes gives |∫(Ω_g²−Ω²)q(W_f)dμ|≤sqrt(1−c_g²)≤sqrt(Q_g/γ). Therefore

**|m_q−h_q| ≤ ∫dg sqrt(Q_g/γ) ≤ sqrt[(∫Q_gdg)/γ].**

The Q_g are the exact *signed electric-metric-defect vacuum expectations* of the M55-type quadratic-form commutator, not necessarily positive pointwise. This statement requires both the assumed SU(2) transport family and an independent estimate of its vacuum defects.

For the SU(2) center cap p_f≥1−h, h_H(h)=[arccos(1−h)−(1−h)sqrt(2h−h²)]/π∼4sqrt(2)/(3π)h^(3/2). A sufficient condition for Haar-order cap mass is **(∫Q_gdg)/γ=o(h³)**. At a fixed small cap, controlling total variation does not by itself bound the full unweighted signed score variation.

The γ here is the **full-link** first-excitation gap. Inserting a uniform γ without proof would be circular, and the earlier gauge-charged Casimir gap cannot automatically replace γ because Ω_g−Ω may contain gauge-invariant components. No M55 interacting-vacuum expectation or continuum mass gap is determined.

**Verification:** 10,000 positive finite spectral models checked Q≥γ(1−c²), zero positive violations; this checks the algebraic comparison, not physical completed-cage Wilson dynamics. The full theorem is in the Library Proof Audits archive.