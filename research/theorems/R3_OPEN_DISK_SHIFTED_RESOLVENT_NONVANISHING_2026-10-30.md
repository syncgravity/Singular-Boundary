# Open-disk shifted electric resolvent: rigorous nonzero Q response at large shift
Date: 2026-10-30. PROVED positive-shift response; unshifted T_perp^-1 response remains OPEN.

For the extracted 11-face open disk with unit link electric coefficients, set G=p_A p_B, where A=face 1 has 4 edges and B=the retained nine-face union has 20 edges; they share 2 edges. Thus the product has 22 distinct active links, of which 20 occur once in fundamental j=1/2 and 2 occur twice and can recouple to j=0 or j=1. The smallest T-invariant subspace containing G is contained in the tensor Peter-Weyl direct sum with those link-spin bounds. On that finite invariant space, physical SU2 electric T=sum_e(-Delta_e) satisfies 0<=T<=L I, where L=20*(3/4)+2*(1*2)=19. This is an exact bound, independent of any Galerkin spectral truncation. Two independent Haar unique links give ||G||_2=1/4.

The previous open-disk exact Fierz certificate establishes Q_f G=0 and ||Q_f T G||_2=sqrt(3)/8. For any real z>0 define the shifted electric inverse R_z=(T+z)^{-1}. Resolvent identity on the finite invariant subspace gives
Q_f R_z G= -z^{-2}Q_f T G + z^{-2} Q_f T^2(T+z)^{-1}G.
Since ||T^2(T+z)^-1 G|| <= L² ||G||/z=361/(4z), the reverse triangle inequality yields
||Q_f(T+z)^{-1}G|| >= sqrt(3)/(8z²) - 361/(4z³).
Consequently it is STRICTLY NONZERO for all z>722/sqrt(3) (about 416.85). The bound is crude but a fully validated analytic nonvanishing certificate for an actual resolvent. In particular, the analytically constructed electric response cannot vanish identically as a function of spectral shift z.

CRITICAL LIMITATION: The needed ground-state perturbative response uses R=T_perp^-1 at zero shift, not R_z for z>0. Nonzero R_z at large z does not establish nonzero Q_f T_perp^-1 G, as an analytic function may have zeros at isolated shifts. Nor does it prove nonzero interacting deleted vacuum, uniform cap probability or a Yang-Mills continuum mass gap. The next obligation is to compute the exact finite-link-spin matrix and certify the zero-shift matrix element or a dual lower bound.
