# Local plaquette carré-du-champ / spectral first-moment bound — 2026-10-30

For a finite open SU(2) lattice, let H=(g2_squared/2)D* K D+V, where K is the symmetric SPD inverse assembled Whitney mass matrix, D are adjoint-transported left/right invariant link derivatives in a common root frame, and V is any real bounded magnetic multiplication potential. Let Omega>0 be a normalized eigenfunction at the bottom E0, and p_f=Tr(U_f)/2 for a fundamental four-link plaquette with no repeated links. The ground-state transform for the real multiplication observable p_f gives the exact local identity

< p_f Omega,(H-E0) p_f Omega> = (g2_squared/2) integral Omega² (D p_f)* K (D p_f) dHaar.

Only the four face links contribute. With -Delta chi_fund=(3/4) chi_fund, each independent link gradient obeys sum_a |X_e^a p_f|²=(1-p_f²)/4; adjoint transport preserves this norm. Therefore sum_{e in boundary(f),a}|D_e^a p_f|²=1-p_f² and

0 <= <p_f Omega,(H-E0)p_f Omega> <= (g2_squared/2) lambda_max(K_boundary(f),boundary(f)) <1-p_f²>_Omega.

This is also a spectral first-moment or f-sum inequality. It has no explicit sum of magnetic strengths and holds for arbitrarily large bounded V in the finite regulator. If a uniform matrix spectral bound K<=c_tile^-1 I holds over a genuine uniformly nondegenerate tile family, then the coefficient <=g2_squared/(2 c_tile) is patch-size independent (BEFORE applying any physical g² refinement scaling). This is an UPPER energy moment bound given the plaquette fluctuation; it does NOT provide an UPPER bound on <1-p_f²> and cannot by itself prove double-center cap probability. A complementary spectral/variance lower bound or conditional response estimate is needed; circularly identifying the right side as a small moment would be invalid.

For archived M5 11-face open disk, diagonalization of K face-principal four-link blocks shows maximum lambda_max about 6.9844932542 at face 7, yielding coefficient 3.4922466271 at g2_squared=1. Numeric entries are standard double precision, not certified interval bounds. SU2 link derivative gradient identity was checked with normalized unit quaternions for 10000 random points. Reproduction script research/scripts/validate_local_carre_du_champ.py.

The prior coupling-response secant formula remains valid but does not supply the missing small moment. No refinement-uniform center-cap estimate or continuum Yang-Mills mass gap is established.
