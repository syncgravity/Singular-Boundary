# R3-IR — Local Wilson score Caccioppoli identity

For finite original-link SU(2) deleted Wilson vacuum Ω, ν=Ω²μ, ℒ=Σ_k a_k(Δ_k+2∇logΩ·∇), v_a=X_(e,a)logΩ, φ_a=X_(e,a)V_−, the exact forced score equation is ℒv_a=φ_a. For every smooth gauge-invariant scalar cutoff χ,

**Σ_a ∫ Γ(χv_a)dν = −Σ_a ∫ χ²v_aφ_a dν + Σ_a ∫ v_a²Γ(χ)dν.**

This follows by reversibility, integration by parts and the carré-du-champ product rule. The extensive potential cancels; only the link-local derivative XV remains. By source-vertex spin-one gauge-orbit coercivity δ_v=2/(Σ_(k∋v)a_k^(-1)), setting D=Σ∫Γ(χv_a), F²=Σ∫χ²φ_a² and B=Σ∫v_a²Γχ gives

**D≤F√(D/δ_v)+B**, thus **√D≤[F/√δ_v+√(F²/δ_v+4B)]/2.**

For χ=χ(u_f), Γχ=(A_f/4)|χ′|². For one retained adjacent plaquette g, Σ_aφ_a²=b_g²(1−p_g²)/4≤b_g²/4. Hence the forcing is link local, while the cutoff-shell score energy B remains unbounded by current results. The identity does not bound rare-fiber unweighted current or prove a regulator-uniform second-order estimate. Full theorem, reproducible one-dimensional IMS verifier (residual 2.22e−16), 5000 quadratic tests and SHA256 manifest in Library Proof Audits archive `R3_IR_LOCAL_SCORE_CACCIOPPOLI_2026-10-31.zip`. Signed-current, connected covariance and continuum mass gap remain open.