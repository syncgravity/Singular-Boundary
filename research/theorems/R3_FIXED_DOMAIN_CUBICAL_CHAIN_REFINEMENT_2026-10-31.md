# R3-IR-586 — Exact cubical chain refinement on a fixed physical domain

Date: 2026-10-31. Independent control geometry for the R3-IR-585 continuum gate; **not** a Penrose approximant or a Yang–Mills continuum construction.

## Explicit infinite family
On the fixed cube Ω=[0,1]³ take standard Cartesian cube partitions with n=2^j subdivisions per axis, j>=1. Each cell has side h=1/n, diameter √3/n, volume n^-3, and uniform shape regularity. Cell count n³, edge count 3n(n+1)², face count 3n²(n+1), vertex count (n+1)³. Hence geometric max diameter tends rigorously to zero under the stated infinite subdivision rule while total domain volume remains 1.

Orient all edges along positive coordinate axes, faces cyclically xy, yz, zx, and cubes xyz. Construct integer cellular boundary matrices B1 (vertices←edges), B2 (edges←faces), B3 (faces←cubes). The executable checked B1 B2=0 and B2 B3=0 exactly at n=2,4,8,16.

Define integer subdivision maps S_k: each vertex maps to doubled fine-grid location; each oriented edge to two aligned fine edges; each oriented face to four aligned subfaces; each cube to eight subcubes. The executable verified the exact chain-map conditions B_k(fine) S_k=S_(k−1) B_k(coarse) for k=1,2,3 at 2→4, 4→8, and 8→16.

| n | h | max diameter | vertices | edges | faces | cells |
|---:|---:|---:|---:|---:|---:|---:|
|2|1/2|0.8660254|27|54|36|8|
|4|1/4|0.4330127|125|300|240|64|
|8|1/8|0.2165064|729|1944|1728|512|
|16|1/16|0.1082532|4913|13872|13056|4096|

All chain-boundary and subdivision checks passed. These are topology and geometry checks only. The matrices neither implement SU(2) Wilson variables nor prove gauge invariance of a quantum Hamiltonian.

## Critical limitations
This cubical benchmark is intentionally **not Penrose**. It does not validate the historic 2D Penrose Whitney data, embed the six small 3D Penrose candidates into a compatible sequence, or establish a 3D nonperiodic Penrose regulator. Cubical grids can serve as a known-consistent geometric control, while a distinct explicitly nested nonperiodic tiling sequence would need to be constructed and audited.

For a 3+1D SU(2) Yang–Mills claim, still necessary: define time slicing / transfer matrix and Gauss-law physical Hilbert space; derive a consistent spatial 1-form mass operator and plaquette action on every grid; specify renormalized bare coupling g(h), time anisotropy and physical energy units; show stability/locality/positivity as appropriate; establish existence of a nontrivial continuum theory and uniform positive gap in the relevant volume/refinement limits. None is provided by cellular chain identities.

## Persistence
Reproducible source `construct_fixed_domain_cubical_refinement.py` and machine-readable test output `fixed_domain_cubical_refinement_2026-10-31.json` are preserved under ChatGPT Library `/The Singular Boundary/Source/`. No false 31-state M5 Ritz gap is claimed; R3-IR-584 electric contraction remains open.