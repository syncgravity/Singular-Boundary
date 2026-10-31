# R3-IR-581 — Nested 16-state M5 higher-spin connected-three-loop fused Ritz

Date 2026-10-31.

## Trial space and nestedness

Union of R3-IR-570's nine A/B character products (a,b=0,1,2) and R3-IR-580's eleven connected A=4,B=29,D=33 states including 1,A,B,D,AB,AD,BD,ABD,F_AD,F_BD,F_AB. Intersection has four vectors 1,A,B,AB, giving **16 linearly independent** Gauss-invariant states.

The ordered 16 basis is [1,A,B,D,AB,AD,BD,ABD,F_AD,F_BD,F_AB,B2,A_B2,A2,A2_B,A2_B2], where A2 and B2 denote χ_1(U_A), χ_1(U_B), rather than squared χ_1/2. For each pair fused trace F_XY=(2/sqrt3)[Tr(U_X U_Y)−Tr(U_X)Tr(U_Y)/2].

## Exact-degree Haar contraction

Root-gauge fix the spanning tree, retain all active link derivatives and the complete K=(M5_mass3d)^−1 mixed edge metric. The active non-tree chords are [1,26,75,95]; chord incidence is A:{1,26}, B:{1,75}, D:{75,95}. At most degree four of an individual basis polynomial arises in chord 1 (A2_B2); products of two derivatives therefore require degree at most eight there. The other three chords have degree at most two per trial basis function, hence electric/Gram products degree at most four. Accordingly use the 120-vertex degree-eight SU(2) 600-cell design on chord 1 and 24-point degree-five 24-cell designs on other chords. Total 120×24³=1,658,880 deterministic Haar nodes.

The complete 16×16 electric matrix and three 16×16 trace-multiplier matrices were accumulated in seven separately executed consecutive node batches. The magnetic coefficients at g²=1 are b_A=25.71208103423584, b_B=19.380965603695362, b_D=14.729533858808479. All retained plaquette support center-parity candidates are exactly indices [4,29,33], with deleted index 0 excluded. Thus the projected magnetic form contains only these three Wilson multipliers.

## Results

The Haar Gram max entrywise error from I_16 is 1.67e−15. The 11×11 electric block agrees with the independent R3-IR-580 calculation within 3.41e−13 and the three magnetic multipliers within 1.45e−15. Sorted first Ritz eigenvalues start E0=−4.83158380, E1=53.71453634, E2=71.09591938, E3=76.58419402; first gap **58.546120141058005**. Previously nested 11-state first gap 60.19916649640645, 10-state first gap 60.435026563191684. These are numerically stable Haar Galerkin calculations under the stated polynomial-degree proof; floating-point rounding has not been interval certified.

Important: although the *individual* first and second Ritz eigenvalues of a nested subspace are minmax nonincreasing, their difference need not be. These are candidate finite-regulator Ritz gaps, not full gauge-constrained spectrum gaps. This fixed M5 candidate is not a demonstrated continuum h-refinement with physical bare-coupling renormalization. No 3+1D Yang–Mills mass gap theorem has been obtained.

Reproduction: ChatGPT Library /The Singular Boundary/Source/compute_m5_connected_sixteen_full.py, finalize_m5_connected_sixteen.py, m5_connected_sixteen_hybrid_ritz_2026-10-31.json. The complete matrices/eigenvalues and audited crosschecks are in the JSON; matrix/incidence binaries remain Library. The script supports CHUNK_START/CHUNK_END so complete quadrature may be executed in seven 250000-node intervals followed by summation in finalize_m5_connected_sixteen.py. Next: add triple fused intertwiners or other independent nearby plaquettes to improve the controlled nested basis and seek genuine regulator-uniform estimates.
