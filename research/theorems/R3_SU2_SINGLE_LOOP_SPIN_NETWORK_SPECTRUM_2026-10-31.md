# R3-IR-564 — Explicit gauge-invariant SU(2) single-loop spin-network benchmark

Date: 2026-10-31. **This is a controlled reduced rotor benchmark, not the constrained spectrum of the actual 95–98-link Penrose-prism Hamiltonians.**

Consider one gauge-invariant residual SU(2) loop holonomy U modulo conjugation. Its Hilbert space is the class-function subspace of L²(SU2), with normalized SU2 characters χ_{n/2}(U), n=0,1,... as an orthonormal spin-network basis. The exact Casimir eigenvalues are j(j+1)=n(n+2)/4, and multiplication by p(U)=Tr U/2 obeys p χ_{n/2}=(χ_{(n+1)/2}+χ_{(n−1)/2})/2. Thus the self-adjoint single-loop Hamiltonian H=c C−B p has symmetric tridiagonal finite representation H_nm=c n(n+2)/4 δ_nm−B/2(δ_{n,m+1}+δ_{n,m−1}), 0≤n,m≤N.

For an *illustrative reduced model only*, substitute c=1/(2M_ee) and B=b_horizontal+b_vertical from the previous candidate 3D coefficient audit, at g²=1. This substitution collapses two distinct plaquette loops to one variable and **discards the other links and mixed inverse-Whitney interactions**; the reduced operator is NOT shown to be a compression or invariant sector of the actual prism Hamiltonian.

The three lowest eigensolutions were checked for N=8,16,32,64,128 using a symmetric tridiagonal eigensolver. At N=128:

| Approximant | B/c | First excitation gap E1−E0 | Largest difference in E0,E1,E2 for N=64 vs N=128 |
|---:|---:|---:|---:|
| 5 | 4.243 | 27.258195 | 1.2e−12 |
| 7 | 4.603 | 38.997692 | 3.8e−12 |
| 9 | 5.850 | 49.088987 | 4.0e−12 |
| 11 | 4.420 | 60.798294 | 6.5e−12 |
| 13 | 4.009 | 70.535455 | 8.4e−12 |
| 15 | 6.406 | 83.514082 | 4.5e−12 |

These constitute finite spin cutoff convergence of the *single-loop class rotor* spectral benchmark. Cutoff convergence at a fixed reduced rotor does not imply either full gauge-invariant spin-network convergence on the six original 3D graphs or convergence of physical energies under M→∞. Their gap trend largely tracks the changing electric parameter c=1/(2M_ee).

The first rigorous **full-graph** spectrum will require vertex intertwiners and multi-loop Wilson characters, preserving distinct plaquette holonomies, the inverse-Whitney mixed electric form, and the Gauss-law physical Hilbert space. No 3+1D Yang–Mills continuum mass gap is established.

Executed sources: `audit_spin_network_single_loop_2026_10_31.py`, results `spin_network_single_loop_benchmark_2026_10_31.json`, persisted ChatGPT Library `/The Singular Boundary/Source/`. No binary Git data.
