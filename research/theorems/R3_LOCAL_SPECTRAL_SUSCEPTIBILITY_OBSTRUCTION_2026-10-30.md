# R3-IR-508: local plaquette spectral variance/susceptibility audit (2026-10-30)

Let H be the finite connected gauge-invariant SU(2) Hamiltonian with Friedrichs inverse-Whitney electric form (g2²/2)D*KD and bounded real multiplication potential V. Assume normalized ground state Omega of eigenvalue E0. Let p=Tr(U_f)/2, m=<p>_Omega, phi=(p-m)Omega, and define the centered variance v=||phi||²=<p²>-m². Let s=<phi,(H-E0)phi>, the **first spectral moment**. The exact ground-state transform gives

s=(g2²/2) integral Omega²(Dp)*K(Dp) <= C_f <1-p²>,    C_f=(g2²/2)lambda_max(K_ff).

Since p-m differs by a constant from p, the derivative is unchanged. On the orthogonal complement of the ground state, define the (possibly infinite) static susceptibility chi=2 <phi,(H-E0)^(-1)phi> via the reduced pseudoinverse. By Cauchy-Schwarz in the spectral measure,

v² <= (chi/2) s <= (chi/2) C_f <1-p²>.

If the complete *interacting* Hamiltonian has a verified positive gap Delta above the ground state, then v <= s/Delta <= (C_f/Delta)<1-p²>. This is a VARIANCE comparison, not the needed upper bound on <1-p²>. It does not control magnetization m, and <1-p²>=1-m²-v. In particular, small v is consistent both with p near +1 (desired) and p near 0 (undesired).

A finite-dimensional multiplication example makes this explicit: on a two-point state space with p=0 at one site and p=1 at the other, the pure state at p=0 has v=0 while <1-p²>=1; the pure state at p=1 has v=0 and <1-p²>=0. These algebraic states are examples of insufficiency of a variance estimate, not claims that the exact Penrose ground state equals either example.

To bound the double-center probability from below, the established Markov estimate still requires an independent UPPER estimate for <1-p²>, or a direct center-localized comparison. A spectral gap or susceptibility estimate alone cannot furnish that because it leaves m undetermined. Uniform ellipticity of K, the local f-sum, and the bound on chi cannot be substituted for a local magnetic concentration argument.

An additional technical warning: a zero mode degeneracy requires centering and a reduced inverse with respect to the **entire** ground eigenspace; without ground state uniqueness, phi may overlap the zero eigenspace. For positivity improving finite elliptic SU2 Schrödinger operators on the connected compact configuration space the unrestricted ground state is simple; gauge restriction needs a separate justification, but the positive invariant ground state is the same. All spectral tests are finite-regulator.

Local archived 30-edge geometry coefficient max over its eleven faces C_f=3.4922466271 at g2²=1, verified using local SU2 invariant-gradient identity; this is a numerical double precision constant. All analytic spectral identities are conditional on the stated self-adjoint finite Hamiltonian and domains.

No refinement-uniform local magnetic moment, shrinking-center-cap estimate, or continuum Yang-Mills mass gap is proved.
