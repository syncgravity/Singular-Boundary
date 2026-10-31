# R3-IR-572 — M5 three-loop full-metric eight-state electric Ritz via exact Haar factorization

Date: 2026-10-31.

The eight Haar-orthonormal Gauss-invariant trial functions Φ_abc=χ_{1/2}(U_A)^a χ_{1/2}(U_B)^b χ_{1/2}(U_C)^c, (a,b,c)∈{0,1}³, were built in R3-IR-571 on the archived candidate M5 prism. A and B share only the protected chord; the third plaquette C is edge-disjoint from A∪B. The three loops involve five non-tree chord holonomies total. In rooted tree gauge, SU2 character derivatives are evaluated at the identity tree links but **tree-link derivatives are not discarded**.

## Exact Haar factorization and full mixed K

Let K be the **complete inverse 98×98 Whitney mass matrix**, including all mixed link couplings. The rooted electric Dirichlet form is E(f,g)=(g²/2)∫Σ K_ij D_i f·D_j g dHaar. Because the third loop uses disjoint links and Haar-independent chord variables, any mixed derivative term between the AB sector and the C sector integrates to zero: a single C-character derivative integrates to zero, and χ_C Dχ_C has zero mean by Haar integration by parts. Terms within the AB sector factorize against ∫χ_C²=1, and within C against the AB trial-state squared norm. Consequently the 8×8 projected electric matrix is **diagonal** with entries E_AB(a,b)+c E_C, where E_AB(0,0)=0, E_AB(1,0)=E_A, E_AB(0,1)=E_B, E_AB(1,1)=E_A+E_B (the final identity is established by the earlier exact 4-state computation), and c∈{0,1}. This vanishing is by symmetry/integration, NOT an artificial truncation of inverse-Whitney off-diagonal entries.

Compute E_C via the same analytic quaternion Lie derivative, rooted transport and 24-cell Haar quadrature as R3-IR-567. The C loop contains two non-tree chord variables, requiring only 24²=576 deterministic design nodes. The derivative squared integrand has degree at most four in each variable, within the 24-cell 5-design exactness; all inverse mass entries on the four C-loop edges are retained. Independently recompute E_A and E_B, and verify agreement with archived exact previous results.

|Coefficient|Deterministic value|
|---|---:|
|E_A|54.694131550223595|
|E_B|75.5290875719122|
|E_C|61.13073538685618|
|E_AB|130.2232191221358|

Combining with the **exact complete projected magnetic** 8×8 matrix from R3-IR-571 yields sorted eight-state Ritz eigenvalues:
[-7.46710558, 50.55935264, 61.00892533, 72.31857096, 119.03538355, 130.34502918, 140.79460187, 198.82106009].
The first gap is **58.026458221786925**, compared with the earlier four-state gap **60.436405726550944**. This difference is informative about variational truncation, not the full physical excitation gap. The 8-state extension is in a different basis direction from the previous 9-state two-loop spin-1 extension, and both must eventually be combined with more plaquettes/intertwiners.

Caveats: the calculation is for one **alternative candidate** M5 3D prism kinetic/magnetic prescription at illustrative g²=1, not the authoritative historical 11-face 2D Whitney matrix. The six approximant family has no validated continuum coupling law. Deterministic cubature is exact for the prescribed polynomial degree, but reported floating-point Ritz values are not interval-certified. There is no full gauge-invariant finite-prism gap theorem or continuum Yang–Mills mass gap.

Persistent output: ChatGPT Library /The Singular Boundary/Source/compute_three_loop_m5_exact_electric.py (SHA256 75c71e4d9bf6acaea75bc5b0fdc279e07ec086bb14d8e2f670fa4fc426a09441) and m5_three_loop_exact_electric_ritz_2026-10-31.json (SHA256 09d1feeb7d73b89f2d98336aa4d6c98d2867798c81ed40a2620d5d49c4cf92f9). Binary data remain in Library.
