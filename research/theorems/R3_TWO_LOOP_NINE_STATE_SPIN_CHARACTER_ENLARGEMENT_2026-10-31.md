# R3-IR-568 — Nine-state SU(2) two-loop spin-network expansion and design orientation audit

2026-10-31. Six candidate 3D Penrose-prism graphs. The finite gauge-invariant trial basis is Phi_{ab}=chi_{a/2}(U_A)chi_{b/2}(U_B), a,b=0,1,2 (9 states), where A,B are the two distinct retained plaquettes sharing the deleted bottom chord. Haar orthonormality holds analytically because independent Haar chord variables induce independent Haar holonomies on these loops.

The archived deterministic two-loop contraction program was extended to these characters. Using p=Tr U/2, chi_0=1, chi_{1/2}=2p, chi_1=4p²−1; derivatives are 0,2,8p times the p derivative, respectively. The full inverse-Whitney matrix K and all root-transport derivative positions are retained, with the tree fixed to identity under gauge invariance. The projected magnetic matrix is exactly a rectangular spin-character nearest-neighbor hopping with coefficients −b_A/2 and −b_B/2. The 9×9 Haar Gram matrix equals identity to machine precision in both tested designs.

The standard 24-cell spherical SU(2) 5-design is sufficient to certify the previous four-state polynomial integration, but products of spin-1 characters can yield higher total polynomial degrees. Accordingly **these nine-state electric cubatures are numerical candidate values, not mathematically exact Haar contractions** until a higher-design proof or independent exact tensor integration is performed. A second quadrature created by one independent 4D orthogonal rotation of the 24-cell design agrees within floating-point precision. This is a helpful consistency test, not a rigorous exactness certificate.

| M | 4-state Ritz gap | 9-state candidate Ritz gap | Difference |
|---:|---:|---:|---:|
| 5 | 60.4364057 | 58.7441547 | -1.6922511 |
| 7 | 86.4815376 | 83.6151468 | -2.8663908 |
| 9 | 116.8900633 | 111.1253365 | -5.7647269 |
| 11 | 136.3407650 | 132.1789229 | -4.1618421 |
| 13 | 162.3628315 | 158.3118891 | -4.0509424 |
| 15 | 195.1584610 | 183.9733967 | -11.1850643 |

All nine-state trial electric matrices were diagonal within floating-point tolerance in these cubatures, with electric spectra remaining positive; exact diagonality for the enlarged sector would require a separate representation-theoretic selection proof, since simple two-edge parity alone does not separate all nine characters. The four-state results from R3-IR-567 are preserved, not overwritten.

**Important minmax distinction:** the nine-dimensional variational *ground-state energy* is bounded above by the four-dimensional variational ground-state energy, and the corresponding excited Ritz eigenvalue is likewise nonincreasing as a nested subspace expands. Their **difference** (the Ritz gap) is not mathematically monotone under subspace enlargement. The observed decreases are contingent numerical results.

Limitations: these nine trial functions do not span the full Gauss-law Hilbert space on a 95–98-link prism, nor do they retain all independent plaquette holonomies or vertex intertwiner channels. The six formal h=1/M patches are not a calibrated continuum refinement. These Ritz gaps prove neither a full finite-volume spectral gap nor a continuum Yang–Mills mass gap.

Artifacts persisted in ChatGPT Library /The Singular Boundary/Source/ as `two_loop_nine_state_audit.py` and `two_loop_nine_state_rotated_cubature_2026-10-31.json`; binary source data remain Library-only. Next computational obligation: certified degree-sufficient SU2 Haar design/tensor moment contraction for the nine-state electric entries; then increase the cutoff and add independent plaquette loops/intertwiners under controlled computational complexity.
