# Physical-link weighted gradient locality — 2026-11-02

Let E be the original links of a finite open straight SU(2) square strip with generator L_g=−Δ−2∇S_g·∇ and dressed probability ν_g∝exp(2S_g)Haar. Assume the preceding certified |g|≤0.001 bound q_g=||s'_g||∞+||s''_g||∞≤49/576. Define link adjacency by co-bounding a plaquette, distance d(e,S) from source-link set S, and weights w_e=(6/5)^{2d(e,S)}.

The face Hessian blocks satisfy ||Hess_{e,d}(s_g◦p_f)||≤q_g/4 and each link belongs to at most two four-link faces. Weighted Schur row/column bounds imply ||W^(1/2) Hess(S_g) W^(−1/2)||≤2q_g(6/5). With Ric(SU(2))=1/2 in the i_k/2 metric, weighted integrated Bochner yields the curvature margin κ_α≥1/2−4q_g(6/5)≥11/120, hence

**||∇e^(−t L_g)F||_{w,ν}≤e^(−11t/120)||∇F||_{w,ν}.**

Integrating over t gives, for centered smooth F and u=L_g⁻¹F,

**||∇u||_{w,ν}≤(120/11)||∇F||_{w,ν}.**

If F is supported on original links S, then for every integer r≥0,

**(Σ_{e:d(e,S)≥r}||∇_e u||²₂)^(1/2)≤(120/11)(5/6)^r||∇F||₂.**

This is a genuinely physical-link-distance locality estimate for the dressed-reference inverse under a smooth local *gradient-source* norm. It is NOT a weighted gradient estimate from a mere local L² source without derivative control; does not yet control nonlinear repeated residual multipliers or physical interacting ground-state observables, and does not prove λ=1 or continuum Yang–Mills gaps.

Detailed mathematical report, exact rational constant checker, verification log, SHA256 manifest are in Library /The Singular Boundary/Proof Audits.