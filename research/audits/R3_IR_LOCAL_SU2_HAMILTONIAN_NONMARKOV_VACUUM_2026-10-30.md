# R3-IR-445 — A local SU(2) rotor Hamiltonian has a nonlocal equal-time vacuum specification

2026-10-30. Explicit perturbative diagnostic of the proposed nearest-neighbor Markov shell contraction. This is a three-rotor SU(2) model, NOT a realization of the gauge-invariant Penrose original-link Wilson disk.

Let x,y,z belong to SU(2), with normalized Haar measures and Laplacian eigenvalues -j(j+1). Define p(u)=Tr(u)/2 and
H_t=-Delta_x-Delta_y-Delta_z-t[p(xy^{-1})+p(yz^{-1})].
For sufficiently small real t its unique normalized positive ground state Omega_t is analytic; Omega_0=1. The Hamiltonian has nearest-neighbor potentials only, connecting x--y--z.

Write A=p(xy^{-1}), B=p(yz^{-1}). Since each first-order source has spins (1/2,1/2) and kinetic eigenvalue 3/2,
Omega_t=1+t(2/3)(A+B)+t² Omega_2+O(t³).
All terms that depend jointly on x and z at second order come from the cross term in the perturbation equation:
(-Delta_x-Delta_y-Delta_z) Omega_2|cross=(4/3)AB.
The y-Haar projection of AB equals
P_y^0(AB)=int AB dy=(1/4)p(xz^{-1}).
Its complementary y-spin-one component is AB-P_y^0(AB). The kinetic eigenvalue on the y-spin-zero part is 3/2, and that of the y-spin-one part is 7/2. Hence the jointly x,z-dependent second-order wavefunction coefficient is exactly
Omega_2|cross=(8/9)P_y^0(AB)+(8/21)[AB-P_y^0(AB)].
The second-order cross term in log Omega is obtained by subtracting half the square of its first-order term, whose cross coefficient is (4/9)AB. Thus
(log Omega_t)|cross,t²=
(4/9)P_y^0(AB)-(4/63)[AB-P_y^0(AB)].
The x,z mixed contribution to log rho_t=2log Omega_t therefore has the y-average
P_y^0[(log rho_t)|cross,t²]=(8/9)P_y^0(AB)=(2/9)p(xz^{-1}). (NM-1)

If the strictly positive equal-time law rho_t(x,y,z)=Omega_t² were a nearest-neighbor Markov field on the x--y--z chain, conditional independence x perpendicular z given y would require log rho_t=F_t(x,y)+G_t(y,z) (up to normalization). Averaging over y, this would yield an additive function of x alone plus one of z alone. But (NM-1) is proportional to p(xz^{-1}), which cannot be so decomposed (its Haar integrals in x and z separately vanish, but it is not identically zero). Analyticity ensures the order-t² obstruction persists for all sufficiently small nonzero t. Hence the equal-time positive ground-state density of a local SU(2) rotor Hamiltonian is generally NOT a finite-range Markov field even though its potential is nearest-neighbor.

This does not prove the failure of any particular spatial mixing estimate for actual 3+1D original-link Wilson gauge theory. It invalidates deriving a Dobrushin nearest-neighbor condition for the equal-time vacuum solely from locality of the Hamiltonian. Any valid Wilson shell contraction must directly control the vacuum conditional influence across shells or work with the space-time Feynman-Kac Gibbs specification, not assume equal-time finite-range conditional independence.

No physical Penrose refinement-uniform cap bound, infrared spectral estimate, or continuum Yang-Mills mass gap is proved.
