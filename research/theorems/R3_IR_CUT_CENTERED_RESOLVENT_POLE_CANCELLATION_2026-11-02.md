# R3-IR — Exact cut centered-resolvent pole cancellation (2026-11-02)

Let A=L0≥0 be the correctly cut original-link generator in L²(nu0), and B=ULU⁻¹=A+V_cut≥0, with U multiplication by normalized exp(s) for the crossing plaquette. The normalized ground vectors are e=1 for A and h=U1 for B. Denote ground projections P_e and P_h and reduced inverses R_A=A⁻¹(1−P_e), R_B=B⁻¹(1−P_h), with the inverse taken on the positive spectral subspace.

**Exact identity:** R_B−R_A=−P_h R_A+R_B P_e−R_B V_cut R_A. This follows from (B+μ)⁻¹−(A+μ)⁻¹=−(B+μ)⁻¹ V_cut (A+μ)⁻¹ and the exact double-pole cancellation P_h V_cut P_e=0. After canceling the remaining simple-pole terms, the reduced shifted identity holds for every μ>0 and passes to μ↓0 when both generators have positive gaps.

**Ground projection estimate:** Earlier certified 24/25≤exp(s)≤26/25 yields 12/13≤h≤13/12 and ||h||_{L²(nu0)}=1. Thus ||P_h−P_e||=sqrt(Var_nu0 h)≤(13/12−12/13)/2=25/312≈0.0801282, by the elementary variance bound. This is volume uniform but not a spatial-decay result.

The three terms in the identity must all be retained for any connected fourth-order cut comparison. No localized matrix-element estimate, fourth-order extensivity, interacting λ=1 spectral gap or continuum Yang–Mills mass gap follows yet.

Complete proof, exact rational finite-dimensional verifier, execution log, and SHA-256 manifest saved in Library /The Singular Boundary/Proof Audits.