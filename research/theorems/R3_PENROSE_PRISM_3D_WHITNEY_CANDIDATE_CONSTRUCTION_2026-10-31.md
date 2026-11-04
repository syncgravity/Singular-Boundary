# R3-IR-560 — Six explicit 3D Penrose-prism Whitney mass candidates

Date 2026-10-31. Built a genuine *three-dimensional candidate edge-complex mass assembly*, beyond the horizontal-only scenario R3-IR-559. **Not** yet a canonical discretized 3+1D Yang-Mills Hamiltonian.

Starting from face-0 radius-2 neighborhoods on six distinct Penrose periodic approximants M=5,7,9,11,13,15, geometrically scale each 2D projected cell by h=1/M and extrude into a hexahedral prism of height h. Build two horizontal layers and vertical edges at every base vertex. Each prism carries twelve first-family tensor-product H(curl) edge functions: four bottom horizontal functions N2D_e(u,v)(1-z), four top functions N2D_e(u,v)z, and four vertical functions (0,0,Nvertex(u,v)). Assemble the full 12×12 local mass by 2×2×2 Gauss-Legendre quadrature with affine 3D Piola transform J^-T, using consistent global edge signs. The resulting global matrices include horizontal–vertical interaction (whose orthogonality happens for block-diagonal affine J), horizontal interlayer coupling and vertical edge degrees. All assembled matrices are symmetric positive definite.

|M|h|Prism cells|3D edges|smallest eigenvalue|condition number|bottom chord M_ee|
|---:|---:|---:|---:|---:|---:|---:|
|5|0.20000|14|98|0.00297341|76.7236|0.04704556|
|7|0.14286|14|95|0.00234449|67.9531|0.03445817|
|9|0.11111|14|98|0.00154553|77.8310|0.03135971|
|11|0.09091|14|95|0.00149552|67.4326|0.02159502|
|13|0.07692|14|95|0.00125244|65.5806|0.01759319|
|15|0.06667|14|95|0.00106808|68.1164|0.01939508|

The bottom horizontal chord local mass equals h/3 times the associated 2D edge mass because ∫_0^1(1-z)^2 dz=1/3. Its top counterpart agrees. All rows passed direct dense SPD checks. This is an *alternative* conforming hexahedral edge mass discretization. The original archival 30×30 Whitney matrix uses a different unresolved recipe; never identify these objects.

**Essential limitations.** These are six distinct small physical regions, not a nested shape-regular sequence resolving one fixed spatial 3-manifold. The 3D edge complex is an explicit kinetic mass only: no plaquette magnetic operator, canonical continuum-action normalization, running coupling, Hamiltonian spectrum, or Gauss-law physical subspace was constructed. The prior protected-chord proof requires a non-tree edge; a spanning-tree choice for these full 3D prisms and a count of every incident 3D plaquette still must be made and verified. In particular, an edge formerly adjacent to only one *retained horizontal face* now also participates in **vertical plaquettes**, so the prior single-Wilson-forcing hypothesis does not automatically survive extrusion. The earlier small interaction/gap ratios must NOT be transplanted to this model.

**Recovery:** full executed source build_penrose_prism3d.py, numerical JSON penrose_prism3d_candidate_results_2026-10-31.json and binary NPZ penrose_prism3d_candidate_matrices_2026-10-31.npz are all stored in ChatGPT Library /The Singular Boundary/Source. Binary data excluded from Git. Continuum Yang-Mills mass gap remains unproved.

**Next construction:** build all horizontal and vertical elementary plaquettes and select 3D rooted tree, tabulate incident Wilson terms for the target edge, implement a consistent 3D Hamiltonian with action-derived coupling law; only then revisit the protected-sector bound at physical refinement.
