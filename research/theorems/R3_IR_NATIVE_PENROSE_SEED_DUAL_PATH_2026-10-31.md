# Native three-face Penrose dual-path incidence and electric Jacobian
Date: 2026-10-31. Status: source-backed finite native-seed certification, not all-refinement.

Source: `sources/historical/raw/Archive_3/singular_boundary_deleted_face_orbit_transport_2026-10-29.zip/__nested__/sb_deleted_face_orbit_transport_20261029/verify_orbit_transport.py` (native spatial three-rhombus Z5 seed, not Stage 26 production catalogue). Its recovered cyclic perimeter has three faces, ten unique undirected edges, at most two faces per edge. The exact dual walk `[0,1,exterior]` uses an edge shared by faces 0/1 and a different exterior boundary edge of face 1.

On original-link SU(2)^10, multiply the first crossed edge by fixed g on the left. Write the preserved face-1 word as A'X'B'; solve X'=(A')^{-1}W_1(B')^{-1}, respecting original link orientation. The retained face word is identically preserved, while every non-crossed link is unchanged. Because the updates are triangular conditional SU(2) Haar translations/inversions, the transformation is a smooth product-Haar-preserving bijection. The exact native incidence is used; abstract xzy orientation is not assumed.

Full 30x30 left-trivialized original-link tangent Jacobian audited on five fixed noncommuting deterministic configurations (symmetric difference step 1e-6). Retained face residual < 6.2e-16; det deviation < 2.9e-10; measured operator norms 1.6934 to 2.2592. The geometry is not generally an electric isometry. This is a numerical diagnostic of the exact finite geometric claim, not a bound uniform in lattice size.

**Open:** all-refinement Penrose production incidence and dual paths, rooted kinetic coefficients, complete-cage nonlinear signed current `sup_f T_{f,h}=o(h^{-1/4})`, and any continuum mass gap. Full original code, faces, matrix tests, JSON results and SHA-256 file manifest stored in Library `/The Singular Boundary/Proof Audits/PENROSE_NATIVE_SEED_DUAL_PATH_AUDIT_2026-10-31.zip`.
