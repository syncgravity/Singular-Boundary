# R3-IR: Cut-eigenvalue cancellation and uniformly gapped interpolation (2026-11-02)

For the physical original-link cut of the dressed SU(2) finite square strip, previous audit gives U L U^{-1}=L_0+Vcut, Vcut=Δs+2Γ(S0,s)+Γ(s,s), with s=log ψ_g(pcut). The exact isolated plaquette eigenvalue equation (-Δ-g p)ψ_g=E_g ψ_g gives Δs+Γ(s,s)=-g p-E_g. Hence **Vcut=-g pcut-E_g+2Γ(S0,s)**.

There are at most two neighboring face cross-terms; original shared-link gradients satisfy |Γ_link(p_f,p_h)|≤1/4. Certified ||s'_g||∞≤1/24 and isolated eigenvalue -|g|≤E_g≤0 imply **||Vcut||∞≤2|g|+1/576≤269/72000≈0.0037361111** for |g|≤0.001. This corrects the excessive 41/192 estimate obtained before cancellation.

The factorized L0 has certified gap≥23/144, including free spectator links. For H_t=L0+tVcut, t∈[0,1], the minmax spectral gap bound yields **gap(H_t)≥23/144−2·269/72000=609/4000=0.15225**, independent of strip length and cut.

This is a stronger cut-comparison prerequisite, not localized fourth-order clustering. A spatially localized susceptibility along H_t and moving ground-state projections remain to be controlled; full physical interacting lambda=1 and continuum Yang–Mills mass gaps remain open.

Complete proof, exact-rational verifier, execution log, SHA256 manifest archived in Library /The Singular Boundary/Proof Audits.