# Exact SU(2) connected triple resolvent, M5 chain 1-3-2
Date: 2026-10-30. Exact rational finite-link calculation. No seven-face or continuum mass-gap claim.

On supplied periodic M5 approximant, retained plaquettes 1,3 share link 3; 3,2 share link 2; 1,2 edge-disjoint. Both shared edges have opposite boundary orientations. The 3-face union has eight boundary edges [0,1,5,14,86,87,88,89]. Set all link electric coefficients to one and use physical SU(2) j(j+1).

Let G=p1*p3*p2, X=p_(1 union 3)*p2, Y=p1*p_(3 union 2), Z=p_(1 union 3 union 2), with union traces the simple concatenated boundary loops. By the SU2 fundamental Fierz identity and Laplacian product rule, the EXACT electric action closes:
T G=10G-(X+Y)/2;
T X=8X-Z/2;
T Y=8Y-Z/2;
T Z=6Z.
The individual simple-loop electric eigenvalues equal three quarters times respective loop lengths.

From exact first- and second-order subset coefficients F_i=p_i/3, F_ij=(4/39)p_i p_j+(4/351)p_(i union j) when adjacent, and F_12=p1*p2/9, the source for squarefree triple J={1,3,2} is
T F_J=(37/117)G+(4/351)(X+Y).
Inverting the exact triangular block gives
F_J=(37/1170)G+(191/56160)(X+Y)+(191/336960)Z.
Direct rational substitution confirms all four coefficients in T F_J match the source, including exact cancellation in the Z channel. The implementation test validates the archived face incidence, opposite orientations and union edge count, and verifies rational coefficients. This is an exact **three-face** connected response within the seven-active-face squarefree recursion, NOT the full seventh-order coefficient; in particular it cannot certify Q_f Omega !=0 since every term above depends on retained holonomies only. Full Q response and continuum mass gap OPEN.
