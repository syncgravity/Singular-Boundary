# R3-IR — Full-strip prefix-future conditional locality (2026-11-02)

On an open straight square SU(2) strip, let F_j be the sigma algebra of *all old original links* through face j, and let T_{>j} contain **all** future original links. Freezing the old links leaves a future product-Haar diffusion with the remaining dressed face weights, including boundary-spanning plaquettes. Under the previously certified curvature/Hessian estimate κ=23/144, the same Bakry–Émery lower bound holds for the conditional future-link diffusion uniformly in strip size and frozen old-link values. Hence P_j u=E[u|F_j] satisfies

||u−P_j u||²₂ ≤ κ⁻¹ Σ_{e∈T_{>j}}||∇_e u||²₂.

Conditional on the previously reported physical-distance weighted Bochner theorem for u=L_N⁻¹F from smooth local centered F supported in S, with r=d(T_{>j},S),

||u−P_j u||₂ ≤ [1440/(11√23)](5/6)^r||∇F||₂ ≈27.2964324(5/6)^r||∇F||₂.

The residual bond w_j is centered given F_j exactly (unlike conditioning on T_j^c for only three new links), so
|<w_j,L_N⁻¹F>|≤[1440/(11√23·1152)](5/6)^r||∇F||₂≈0.02369482(5/6)^r||∇F||₂.

Using the previous conservative ||∇w_i||₂≤0.012823014 yields the full-strip two-bond response ≤0.0003038390(5/6)^r for an earlier-supported w_i. No interior conditional-mean leakage remains in this *prefix* pairing.

This is a conditional theorem based on the prior weighted-gradient and uniform curvature estimates; it does not prove third-order connected response, weighted L²→gradient locality, volume-uniform physical interacting gap, or Yang–Mills mass gap. Exact arithmetic tests and product-Walsh centering checks passed. The complete proof/checker/log/hash manifest are archived in Library /The Singular Boundary/Proof Audits.