# R3-IR-542 — Exact metric co-transport resolves rooted-frame equivalence (2026-10-30)

## Theorem (same electric operator in different frames)

Let D_i^(2)=R_i(U)D_i^(1) with R_i(U)∈SO(3) the SU2 adjoint change of rooted frame. Start from the positive quadratic form Q1[ψ]=∫Σ_ij K_ij D_i^(1)ψ·D_j^(1)ψ, with K=M^-1 fixed and symmetric SPD on edge indices, and define a *transported* block metric

K2_(i,a;j,b)(U)=K_ij [R_i(U)R_j(U)^T]_(a,b).

Then pointwise Σ_ij (D_i^(2)ψ)^T K2_ij (D_j^(2)ψ)=Σ_ij K_ij D_i^(1)ψ·D_j^(1)ψ for **every** smooth ψ, even if ψ is not gauge invariant. Here the block transformation is K2=R K1 R^T with block-diagonal orthogonal R; because d2=R d1 one may equivalently read K2=R K1 R^T (both orientations consistent because d1=R^T d2). Thus the positive closed quadratic forms and associated Friedrichs operators agree *in the common configuration coordinate space* if potentials and boundary/form domains agree. There is no need to invoke a nontrivial orbit-space unitary to identify this correctly co-transported *same* operator.

This is not a proof that two independently defined **fixed scalar K** Hamiltonians H_T1,K and H_T2,K have the same spectrum or are unitarily equivalent. Those fixed-K models were shown to differ on gauge-invariant Wilson quadratic-form densities in R3-IR-538–541.

## Actual Penrose check

Use original SHA-256-verified `global_whitney_11face.npz` from Library, the recovered M5 graph, and the two root trees T1 BFS and T2=T1-{4}+{13}. On the gauge-invariant function ψ(U)=p_face0 p_face10, eight new seeded (542) independent Haar configurations were tested with full 30×30 original inverse Whitney K. With original fixed K, max |Q_T2,K-Q_T1,K|≈0.0961069026. With K2(U) transported as above, max |Q_T2,K2-Q_T1,K|=6.661338147750939e-16. The first configuration gives (Q_T1,K, Q_T2,K, Q_T2,K2)≈(1.0543408816363156,1.085699853181761,1.0543408816363151). The equality is **analytical**; the numbers are an implementation check.

## Consequences and boundaries

1. The prior fixed-K differences are real **prescription differences**, not proof of physically invariant tree dependence.
2. A correctly transported K2(U) generally has configuration-dependent 3×3 off-diagonal blocks; a scalar constant-edge Schur coefficient 1/M_ee is not automatically usable in the transformed frame. An intrinsic protected-link theorem should be expressed against the **form itself**, not against a tree label.
3. This settles the simple frame-change equivalence of one fixed operator when kinetic metric is co-transported; it does NOT derive which untransported/rooted electric metric is physically canonical from a continuum Yang–Mills action, or whether another discretization is unitarily equivalent.
4. The physical refinement ratio b_h/gamma_h and any positive relative deleted-face cap as δ→0 remain OPEN. A finite-model gap does not prove the 3+1 continuum Yang–Mills mass gap.

Reproducibility: `research/scripts/validate_m5_metric_cotransport.py` (also copied to ChatGPT Library), with original matrix in Library `/The Singular Boundary/Source/global_whitney_11face.npz` and recovered original source. This adds no binary artifacts to Git.
