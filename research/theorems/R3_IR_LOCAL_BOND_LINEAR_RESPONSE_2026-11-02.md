# R3-IR — Local residual-bond ground-state linear response (2026-11-02)

For finite straight open square SU(2) strips let L_N be the dressed reference generator with certified gap κ=23/144 and simple ground state 1. A single residual bond w_j has zero mean, belongs to martingale increment H_j, and obeys ||w_j||∞≤v=1/1152, ||w_j||₂≤v. For H_{j,t}=L_N+t w_j (|t|≤1), min–max proves the uniform single-bond gap gap(H_{j,t})≥κ−2v=91/576>0.

At t=0 exact perturbation differentiation gives E'_0=0, h'_0=−L_N⁻¹ w_j, E''_0=−2<w_j,L_N⁻¹w_j>, and the physical one-bond ground-state expectation susceptibility (d/dt) μ_{j,t}(A)|_0=−2<A−ν_N(A),L_N⁻¹w_j>.

Conditionally on the previous dressed inverse increment-decay theorem, with q=13/(72√3) and C=[κ(1−q)]⁻¹, for A∈H_i the susceptibility is at most 2Cv ||A||₂ q^|i−j| ≈0.01213451 ||A||₂ q^|i−j|. For A supported through first k faces and j≥k, the bound is 2Cv /√(1−q²) ||A−ν(A)||₂ q^(j−k+1) ≈0.01220099 ||A−ν(A)||₂ q^(j−k+1).

**Limitation:** The full all-bond perturbation t W_N has only the elementary gap bound κ−2|t|(N−1)v, which cannot certify an N-independent radius or physical gap. Higher nonlinear connected insertions remain uncontrolled. The logarithmic ground state solves L_N u−Γ(u,u)+t W_N=E_t, not merely a linear Poisson equation.

Complete proof, exact-rational verifier, log, SHA256 manifest: Library /The Singular Boundary/Proof Audits. Full interacting λ=1 and continuum mass gaps remain open.