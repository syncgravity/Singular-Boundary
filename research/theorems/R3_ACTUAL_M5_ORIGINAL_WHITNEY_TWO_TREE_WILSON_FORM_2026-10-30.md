# R3-IR-538 — Actual archived M5 inverse-Whitney gauge-invariant two-tree Wilson form comparison (2026-10-30)

## Provenance

**Input:** original `global_whitney_11face.npz` recovered from ChatGPT Library `/The Singular Boundary/Source/`, exactly 8,448 bytes, SHA-256 `d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf`. It contains the original 30x30 `matrix`, `edge_ids` and `eigenvalues` arrays. This is NOT the alternative 30x30 candidate mass of R3-IR-537. Geometry: recovered `penrose_causal_study.Approximant(M=5)` and `wilson_torus.penrose_faces` from Source archive `Archive 4.zip`.

## Two actual rooted trees

Eleven retained-plus-deleted faces: (0,1,3,2,4,154,150,11,10,7,8), 30 edges and 20 vertices. T1 is sorted BFS tree from smallest disk vertex 0; T2 replaces edge 4 with edge 13 on the fundamental cycle. Both valid 19-edge spanning trees. At every configuration and for each edge j, root transport V_j(T) is the quaternion product on the unique rooted path to the source endpoint of edge j (with inverse for reversed paths). The electric principal form is
[
 Q_T(U;
abla F)=sum_{i,j} (M^{-1})_{ij} [mathrm{Ad}_{V_i(T)}X_iF]cdot[mathrm{Ad}_{V_j(T)}X_jF].
]
Here X_i differentiates the left endpoint link variable via left multiplication by exp(t i sigma_a/2). The gauge-invariant test is **F(U)=p_{face0}(U),p_{face10}(U)**, with each p the normalized SU2 loop trace and actual oriented face incidence.

## Numeric witness and controls

25 seeded independent random Haar quaternion link configurations, seed=537; central derivative step 2e-6 in quaternion SU2 angle. For the final run: configuration zero gives Q_T1=1.7777528214216918, Q_T2=1.7873254170011779, difference -0.009572595579486087; largest observed absolute difference **0.12010552226507187**, average absolute difference **0.03910980893552327**. A random independent vertex gauge transformation of the first configuration left F unchanged at tolerance 1e-10. Central derivative gradients at steps 2e-6 and 1e-6 agreed to 5e-9 for this configuration. M was checked against exact historical SHA-256 before loading, and M^-1 was computed from that original matrix. This is an ordinary floating-point witness, **not** a computer-assisted exact certification, spectrum comparison, or gauge-unitary-equivalence exclusion.

## Limits and storage

This establishes numerical nonidentity of the two rooted electric principal quadratic forms on the **actual M5 geometry with the original Whitney inverse matrix**, for at least one gauge-invariant Wilson observable. It is stronger than the toy two-cycle check R3-IR-535; it does NOT prove different spectra or physical inequivalence. The root-transport convention itself remains a model assumption. The unresolved Whitney assembly recipe mismatch with the candidate remains open (the original matrix bytes now exist, so the issue is provenance/derivation, not missing data). Neither physical refinement-uniform caps nor continuum Yang–Mills mass gap follows.

**Binary test output:** ChatGPT Library `/The Singular Boundary/Source/actual_m5_tree_wilson_results_2026-10-30.npz` (DO NOT commit NPZ in Git). The complete portable test script is `research/scripts/validate_actual_m5_two_tree_wilson_forms.py`; requires original data restored from Library and archived source modules. Use SHA-256 to avoid replacing original Whitney matrix with candidate. Future-chats recovery manifest: `research/SOURCE_DATA_RECOVERY_MANIFEST_2026-10-30.md`.
