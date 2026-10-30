# R3-IR-425 — Nonperturbative local electric-energy budget and private-edge spin tail

2026-10-30. An exact finite-volume variational estimate for original-link SU(2) Wilson ground states, valid at FULL coupling of the selected neighboring face, with arbitrary other interacting plaquettes. Not a continuum gap proof.

Let x be an original interior edge shared only by the magnetically deleted target face f and one neighboring face g. Its SU(2) electric term is a_x(-Delta_x), a_x>0. Since the target magnetic term is deleted and x occurs in no other magnetic plaquette, after omitting the scalar b_g the Hamiltonian splits

H=a_x(-Delta_x)+H_y-b_g p_g(x,y),

where H_y is the exact interacting original-link environment Hamiltonian and p_g=Tr W_g/2 is multiplication by a real function in [-1,1]. Work on the full original-link Hilbert space. The unique normalized positive ground state Omega is gauge invariant, so all gauge-invariant conclusions are physical. Let e_y=inf spec H_y, E=inf spec H, and denote <...> in Omega.

The normalized trial vector phi(x,y)=1_x omega_y, with omega_y the normalized positive environment ground state, is gauge invariant and has <phi,p_g phi>=0 by x-Haar orthogonality. Consequently E<=e_y. Since H_y>=e_y and -p_g>=-1,

E=<Omega,H Omega>
>=e_y+a_x<Omega,-Delta_x Omega>-b_g.

Combining gives the NONPERTURBATIVE local energy budget

boxed: a_x <Omega,-Delta_x Omega> <= b_g. (LB-1)

This is independent of all other Wilson magnetic couplings, environmental volume and any interacting physical gap. It is valid for b_g>=0, including the full physical strength, and for all SU(2) disk refinements satisfying the stated private-edge geometry. It concerns only a selected edge, not a global electric-energy bound.

Let P_x^{>=s} be the Peter-Weyl orthogonal projection onto x-link irreducible spins ell>=s, with s a positive half-integer or integer. Since the Casimir of spin ell is ell(ell+1),

a_x s(s+1) ||P_x^{>=s}Omega||² <= a_x<Omega,-Delta_x Omega> <= b_g.

Thus the rigorous high-spin tail is

boxed: ||P_x^{>=s}Omega||² <= min(1,b_g/[a_x s(s+1)]). (LB-2)

This is a state-space tail, not a bound on the target character expectation by itself. For an integer target character chi_j(W_f) with 0<=ell<j/2 in both bra and ket, SU(2) tensor-product selection gives P_low chi_j(W_f) P_low=0. Writing delta_s=||P_x^{>=s}Omega|| and choosing s=j/2 (with strict low spins ell<j/2), one obtains the valid but conservative estimate

|<chi_j(W_f)>|
<= (2j+1)(2 delta_{j/2}+delta_{j/2}²)
<= (2j+1)(2 sqrt[min(1,4b_g/(a_x j(j+2)))]+min(1,4b_g/(a_x j(j+2)]).
 No estimate better than the trivial |<chi_j>|<=2j+1 is claimed at large j, because the character multiplication operator norm grows with j. Hence LB-2 is **not sufficient** to close the cap-sensitive Fourier tail R3-IR-422 at physical magnetic scaling.

At physical b_g/a_x large, the kinetic tail only becomes small above spins of order sqrt(b_g/a_x); character resolution for radius a_h~sqrt(h) requires spins of order 1/a_h by R3-IR-423, and no favorable comparison of these scales has been established. This is a real full-coupling local Wilson estimate with an explicit limitation, not a cap-survival or infrared mass-gap theorem.
