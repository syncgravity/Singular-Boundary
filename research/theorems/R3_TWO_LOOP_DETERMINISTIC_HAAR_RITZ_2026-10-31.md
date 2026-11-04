# R3-IR-567 — Deterministic exact Haar contractions for two-loop four-state Ritz Hamiltonians

Date 2026-10-31. Replaces the exploratory electric Monte Carlo diagonals of R3-IR-566 for the **four-dimensional** gauge-invariant trial subspace on six candidate 3D Penrose-prism graphs.

## Exact reduction

The rooted transported electric Dirichlet-form integrand is invariant under vertex gauge transformations. Fix all links in the rooted spanning tree to the identity using the unique root-fixed tree gauge. Product Haar disintegration leaves non-tree holonomies Haar independent. The two neighboring retained plaquettes depend on precisely **three distinct non-tree chords**, as directly verified in each of M=5,7,9,11,13,15. Other chord holonomies do not appear in the four-state trial derivatives and integrate out.

For each chord, SU(2) is identified with the unit quaternion sphere S³. The 24-cell cubature has 24 equal-weight points: eight ±coordinate axes and sixteen 4-vector corners with entries ±1/2. It integrates polynomials of total degree ≤5 on S³ exactly. Each rooted-electric gradient inner product of trial functions 1, χ_A, χ_B, χ_Aχ_B becomes a polynomial of degree at most four **in each chord separately** after tree gauge fixing. Hence a tensor product of 24³=13,824 nodes evaluates the required Haar matrix entries exactly (up to floating rounding). The full K=M1^-1 is contracted on all active link derivatives, including the mixed edge couplings; fixing tree links does not set their derivatives to zero.

Under the normalized Wilson trace p=χ_1/2/2, the exact magnetic projected coefficient is −b/2 times nearest trial-state adjacency. An initial integration-check script omitted this normalization in the *test quadrature* and failed; corrected script reproduces the previously derived 4×4 magnetic matrix to tolerance <1e−10. The trial Gram matrix is I_4, and the electric matrix is exactly diagonal by edge-center parity, also verified numerically.

## Computed coefficients and Ritz eigenvalue gaps

| M | E_A | E_B | E_AB | four-state Ritz gap |
|---:|---:|---:|---:|---:|
|5|54.694131550224|75.529087571912|130.223219122136|60.436405726551|
|7|76.723896813264|111.426612170538|188.150508983802|86.481537580066|
|9|97.073615883578|123.310655820611|220.384271704189|116.890063310413|
|11|122.196216451192|175.846506874947|298.042723326139|136.340765011333|
|13|148.643157351169|207.924788475883|356.567945827053|162.362831503306|
|15|156.532804152922|202.782730917840|359.315535070762|195.158460996253|

These deterministic results supersede the 128-draw sample estimates of R3-IR-566 and agree in order of magnitude with the independent 2048-draw M5 diagnostic. They are exact-form *four-state Ritz* calculations using candidate kinetic and magnetic normalization, not the spectrum of the full gauge-constrained 95–98-link Hamiltonian. The gap's growth with M cannot establish a physical continuum mass gap since these are different small patches with arbitrarily assigned h=1/M and no physical running coupling. The 24-cell integration is exact for the declared polynomial class, but the matrix inversion/eigensolver remain floating point, so the decimals are not rigorous machine-certified intervals.

## Durable reproducibility

The complete executed source `exact_two_loop_ritz.py` and six-model machine-readable `two_loop_exact_haar_ritz_2026-10-31.json` are in ChatGPT Library `/The Singular Boundary/Source/`. SHA256 script `7463bd359eb3fb84f01d3e489fa03d90e4861820430b37948c1ea6ca5cd30175` and JSON `f81c45a628f75147d785f9f2b3f32315bef7f6ceab54e463d1183f2293cbc01a`. Prior candidate matrix and incidence NPZ archives remain in Library, not Git.

## Next obligation

Build a systematic Gauss-invariant multi-loop basis beyond four trial states; retain intertwiners, Wilson traces for other plaquettes and all K cross terms, and seek convergence bounds in a controlled spin cutoff. No continuum Yang–Mills mass-gap result is established.
