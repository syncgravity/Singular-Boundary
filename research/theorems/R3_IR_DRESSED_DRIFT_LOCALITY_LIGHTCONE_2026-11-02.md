# Dressed drift: formal locality light cone (2026-11-02)

For a finite open straight SU(2) strip with independent-link electric operator K, the centered free resolvent K^{-1}P0 preserves original-link dependence. Each Gamma(s_b(p_f),F) vanishes unless face f shares an original link with the support of F, and otherwise enlarges that support by at most one neighboring face.

Consequently the coefficient of b^k in the **formal** Haar-centered dressed-resolvent expansion of an observable on one face depends only on faces within k adjacency steps. This is a finite-order support statement, not a convergent inverse theorem.

The naive positive count of k local insertions is bounded by (k+2)!/2; propagation alone cannot establish summability. Crucially the full dressed Poisson equation needs a scalar counterterm c_b=mu_b(F), generally not Haar(F). Its Haar-centered part determines the nonconstant coefficients, with c_b recovered from the Haar mean of Gamma. The scalar correction requires separate control.

Exact strip graph checks passed for N=1..18 and insertion paths through k=6. Full proof and executable verifier are preserved under Library /The Singular Boundary/Proof Audits. Previously published matrix-Peter-Weyl bilinear estimates remain a separate proof-audit dependency. The interacting gap and continuum mass gap remain open.