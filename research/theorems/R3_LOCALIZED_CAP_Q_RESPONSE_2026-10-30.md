# Local cap response instead of global Haar projection
Date: 2026-10-30
Status: exact finite physical projection identities and conditional local criterion. Penrose cap survival remains OPEN.

Let P be Haar averaging in the deleted based-face holonomy on the finite simply connected SU(2) disk, Q=I-P, Omega>0 normalized physical ground state, p=P Omega, q=Q Omega. Let M_delta multiply by indicator of the identity-center cap 1-Tr(W_f)/2<=delta. Haar cap probability is c_delta. Since P M_delta P=c_delta P and M_delta is an orthogonal multiplication projection,
m(delta)=||M_delta Omega||²=c_delta ||p||²+2 Re<M_delta p,M_delta q>+||M_delta q||².
The reverse triangle inequality gives
m(delta)>=[sqrt(c_delta)||p||-||M_delta q||]_+².
This is generally stronger than the global OT-4 bound using ||q||. If inf_f ||p||>=c0>0, and sup_f ||M_delta_h q||=o(sqrt(c_delta_h))=o(h^(3/4)), then m(delta_h)>=(c0²-o(1))c_delta_h, enough for polynomial cap lower bound and, under the previously proved exponential tilt, logarithmic deletion scaling.

With A=Q(H_--E0)Q, s=-QTPp and q=A^-1 s (operator domain as in R3_PHYSICAL_Q_SOURCE_SPECTRAL_RESPONSE), the local error has exact positive operator expression
||M_delta q||² = <s,A^-1 Q M_delta Q A^-1 s>.
Here Q M_delta Q is a positive bounded operator on Ran Q, but it generally DOES NOT COMMUTE WITH A. As a result, this is a two-variable spectral kernel rather than the scalar positive inverse-square source spectral integral. A direct scalar spectral bound derived by commuting Q M Q through A would be invalid.

An exact counterexample to NEEDING global smallness: in a product Haar face coordinate choose a smooth center-even real function k supported away from both center caps with Haar mean zero; let Omega=Z^-1/2(1+epsilon k), small epsilon for strict positivity. Then P Omega=Z^-1/2, Q Omega=epsilon k/Z^1/2, ||QOmega|| is order epsilon independent of cap radius, while ||M_delta QOmega||=0 for sufficiently small caps. The cap mass is exactly c_delta/Z and remains Haar order. This is a smooth positive gauge-invariant auxiliary state, not the actual Penrose ground state; a smooth shifted potential can make it a ground state. It demonstrates the new sufficient condition is strictly weaker than global Q smallness.

A still weaker necessary/sufficient target is directly m(delta)>=h^s; the localized Q criterion is NOT claimed necessary. It retains an independently unproved lower bound on ||p||. No uniform Penrose bound or continuum mass gap is established.
