# R3-IR — Equal-depth tree–cotree electric metric and signed trial-state diagnostics

**2026-10-31.** Finite 3×3 planar original-link SU(2) geometry, 24 links, 9 faces, central target (1,1). This is a deterministic numerical comparison, **not** a universal tree optimality theorem, not an interacting Wilson vacuum calculation, and not a continuum mass-gap result.

## Setup and exact properties

Let face holonomies be ordered products around each square. For a dual spanning tree rooted at the exterior, choose each face's dual-parent primal edge as its update edge. Change only target face word W_f into gW_f, leave desired retained holonomy words unchanged, and update face variables in descending dual depth. Each update solves the group word exactly for its corresponding link; because a changed link is a parent edge in the dual tree, the descending-order algorithm preserves all intended face words. This provides a bijective, Haar-preserving tree–cotree coordinate translation, although its original-link electric metric is not preserved.

Numerically construct the complete left-trivialized Jacobian J of this map by independent perturbation of **every** original link Lie direction, including directions on unchanged links. For electric coefficients a_e∈[0.75,1.25], A=diag(a_e I_3), form M=J A J^T−A and D=A^(−1/2) M A^(−1/2). Report max(0, λ_max(D)).

Three trees: forward-order BFS; reverse-order BFS; DFS. Both BFS variants have target dual depth 2, modify two original links, and are shortest-path trees, but have distinct coordinate dependencies. For the same first random configuration and fixed noncentral SU(2) g, maximum positive metric distortions are **3.6177336**, **9.0756100**, **37.0593271** (forward BFS, reverse BFS, DFS). Their full metric support has 3, 4 and 9 original links, respectively. All retained face holonomies were verified up to ~1e-15. Across four seeded configurations, forward BFS distortions were 3.618,3.599,3.082,4.298; reverse BFS 9.076,8.031,7.451,8.047; DFS 37.059,41.272,41.439,44.328. These are samples, not expectations.

## Gauge-invariant trial-state diagnostic

Take the smooth strictly positive, gauge-invariant **unnormalized** amplitude Ω_κ(U)=exp(κ Σ_{g≠f}p_g(U)), for κ=0.15 and 0.5. A normalization constant would cancel in a ratio of expectations but is not estimated in this diagnostic. Compute ∇logΩ_κ at the transported configuration by central SU(2) Lie finite differences. The pointwise signed electric quadratic density q_T(U)=∇logΩ_κ(TU)^T M_T(U) ∇logΩ_κ(TU) is **not sign-definite**, even for fixed κ=0.5 and the same tree choice across different configurations. For example, forward BFS produces −0.00609, 0.00356, 0.025..., 0.046... on the four configurations; reverse BFS yields both signs. By contrast λ_max^+(D_T) is nonnegative by definition. This is a pointwise calculation with a positive gauge-invariant trial amplitude, **not** a Haar-integrated electric-form defect, a Rayleigh quotient, or a Wilson vacuum expectation.

The full signed vacuum expectation Q_T=⟨P_TΩ,(H−E0)P_TΩ⟩, and its uniform dependence on refinement, remain uncomputed. Since Ω_κ is a trial function, its signed integrated form need not be nonnegative and no positivity conclusion should be drawn from individual pointwise densities. A two-sample comparison cannot establish a universal distortion optimizer.

## Methods and reproducibility

`verify.py` builds the 3×3 primal and dual networks, computes exact SU(2) quaternion face words and transports, checks the transformed holonomies, finite-differences all 72 original-link directions with step 2e−6, diagonalizes the full 72×72 normalized metric defect, and checks the positive gauge-invariant trial gradient using central step 1e−5. The RNG is explicitly seeded. `results.json` contains all measured data. Finite differences are not interval-certified; all analytical conclusions in this report are restricted to the exact construction and the elementary support implications, while quoted metric eigenvalues are numerical approximations.

## Proof obligation

The next target is to integrate signed metric defects against properly normalized gauge-invariant trial measures, then obtain independent control for the **actual** interacting deleted-face Wilson ground state. It remains necessary to prove the one-sided current gate sup_{f∈D_R} 𝔗_{f,h}=o(h^(−1/4)); connected covariance and continuum Yang–Mills mass gap remain **OPEN**.