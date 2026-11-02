# R3-IR — Connected-tree analytic-radius audit (2026-11-01)

**Status:** Finite-order majorant and obstruction for a specified positive uniform-slicing majorant. **Not** a divergence theorem for actual SU(2) score coefficients, an interacting gap, or a continuum mass-gap proof.

## Inputs
On the complexified unit-quaternion domains Q_R, for K=-Σ_e a_e Σ_k X_{e,k}², a_0≤a_e≤a_*, the earlier holomorphic bridge asserts
||K_T^{-1}P_0 Γ_K(f,g)||_{R'} ≤ [3 B_m/(4 log²(R/R'))] (Σ_{e∈E(f)∩E(g)} a_e) ||f||_R ||g||_R,
where B_m=a_0^{-1}[2+(8/3)(1+log_+(m C_*/2))], C_*≈2.18611927699.
This is taken as an *input*, not newly proved here.

## Formal score recurrence
For ψ_λ=exp(S_λ), (K+λV)ψ_λ=E_λ ψ_λ implies K S_λ=E_λ−λV+Γ_K(S_λ,S_λ).
Haar-centered formal coefficients satisfy K S_1=−P_0 V and K S_n=P_0 Σ_{i=1}^{n−1}Γ_K(S_i,S_{n−i}) for n≥2. Haar-centering chooses constants but is not a normalization of ψ.

## Fixed ordered tree, fixed spatial embedding
Fix a tree with n single-plaquette leaves on a connected strip of at most n square faces (≤3n+1≤4n links). Let ||V_f||_{R_in}≤v, R_in>R_out>1, L=log(R_in/R_out). Assign to each k-leaf vertex R_k=R_out exp((n−k)L/n), so every child-to-parent loss is at least L/n. Leaf norm ≤A=B_4 v. The shared-link weight is ≤4a_*n; every internal vertex therefore costs at most W_n=3 a_* B_{4n} n³/L². Each tree is bounded by A^n W_n^{n−1}. For a fixed ordered leaf list with at most Catalan(n−1) planar trees, the sum is ≤Catalan(n−1) A^n W_n^{n−1}.

**Scope warning:** This does not include multiplicity of all leaf labels, repeated face insertions, or spatial embeddings, and cannot be advertised as an upper bound for the complete coefficient S_n without them.

Because B_{4n}=O(log n), this general-purpose upper bound has an unbounded n-th root. It **fails to establish** a positive convergence radius; this does not show the true series diverges.

## Restricted scalar obstruction
In an auxiliary *positive* scalar tree model where every vertex is charged a uniform loss L/n and a fixed positive overlap coefficient c, a comb of n−1 vertices has weight A^n (c n²/L²)^{n−1}. Its n-th root diverges, so the positive uniform-slicing model has zero convergence radius. This is a fact about that artificial majorant, not a lower bound on actual score coefficients.

## Open obligations
Estimate all embeddings and repeated insertions; find a derivative-tame electric resolvent or a mechanism canceling comb contributions; reconcile the three-face sign conventions; prove interacting λ=1 gap and Penrose current estimate. The continuum mass gap is open.

Companion local artifacts: R3_IR_CONNECTED_TREE_RADIUS_AUDIT_2026-11-01.md, verify_connected_tree_radius_audit.py, verify_connected_tree_radius_audit.log, SHA256 manifest.
