# R3-IR-561 — Complete 3D prism Wilson plaquette incidence audit (2026-10-31)

This is an original-complex **discrete incidence** result, NOT a physically calibrated continuum Yang–Mills Hamiltonian.

Recovered the archived Approximant(M) geometry for M=5,7,9,11,13,15, built the same 14-cell radius-two face neighborhoods used in R3-IR-560, constructed bottom/top oriented horizontal edges and upward vertical edges, and enumerated bottom/top horizontal plaquettes and one vertical plaquette per base edge. For each hexahedral cell, verified the signed identity boundary-of-boundary = 0, using orientations induced from the local quadrilateral corners (not assuming archived face-sign ordering coincides with the chosen global plaquette orientation). Built a full 3D rooted spanning tree with three bottom boundary edges of the deleted face forced in and the selected fourth chord omitted.

|M|3D edges|plaquettes|tree edges|cycle rank|chord plaquette incidence|
|---:|---:|---:|---:|---:|---:|
|5|98|65|47|51|3|
|7|95|64|45|50|3|
|9|98|65|47|51|3|
|11|95|64|45|50|3|
|13|95|64|45|50|3|
|15|95|64|45|50|3|

In all six models the bottom protected chord occurs in exactly three plaquettes: the deleted bottom horizontal face 0, one retained neighboring bottom horizontal face, and its vertical extruded plaquette. Deleting face 0 leaves **two** chord-dependent magnetic interactions. Consequently the 2D single-retained-Wilson-term bound does not transfer unmodified. A conservative bounded multiplication perturbation uses B_e=|b_horizontal|+|b_vertical| (more generally sum over all retained incident plaquette coefficients). If all source-path transports avoid the chord, the SU2 non-tree sector argument of R3-IR-556 can be applied with |b| replaced by B_e, provided the kinetic-form and ground-state assumptions actually hold for the **3D** candidate. The bound remains conditional on physical normalization and uses the actual 3D chord mass, NOT the original 2D 30×30 matrix.

Important: these tests verify oriented topology, not SU2 matrix-valued flatness, a Gauss-law-constrained physical Hilbert space, the Yang–Mills Hamiltonian, renormalization, or continuum spectral gap. There is no established h-uniform positivity for physically derived b_h/g_h².

Persistence: full executed script and machine-readable JSON and NPZ are in ChatGPT Library `/The Singular Boundary/Source/` under `build_penrose_prism_plaquettes.py`, `penrose_prism3d_plaquette_incidence_2026-10-31.json`, `penrose_prism3d_plaquette_incidence_2026-10-31.npz`. SHA256: script `9eed5d09bbd93f253ffa2325e72dbe9499730ed1d0bb17e2b2a735d385749d06`; JSON `b4b3dd36a0eb64c401470b999328c13ddbb766ec88ebcc8f6d77d909c8bd3d0e`; NPZ `06f002943380d4270fe45cc9cb59e7a38b9d0a30ac9e67741757265485143a67`. Do not put binary arrays in Git.
