# Localized physical Q resolvent duality and nonlocal projector tail
Date: 2026-10-30
Status: exact finite-regulator identity and geometric obstruction; uniform Penrose cap response OPEN.

Let P denote conditional Haar averaging of deleted based-face holonomy on the physical Hilbert space, Q=I-P, Omega>0 normalized, p=P Omega, q=Q Omega. Let M_delta be multiplication by the identity cap indicator, c_delta its Haar mass, and A=Q(H_--E)Q positive on Ran Q. Assume L2 source s=-QTPp and q=A^-1 s.

THEOREM 1 (localized dual resolvent):
||M_delta q|| = sup{|<s,A^-1 Qg>| : g physical, ||g||<=1, M_delta g=g}.
Proof: dual formula for norm supported on cap, q=Qq, and self-adjoint A^-1 on Q. Hence sufficient condition for Haar-order cap via previous localized cap inequality is this supremum=o(sqrt(c_delta_h)), with inf ||P Omega||>0. Not established.

THEOREM 2 (nonlocal Haar projection tail). Since P M_delta P = c_delta P as an operator on the physical space, for any cap-supported physical g,
||Pg||² = ||P M_delta g||² <= c_delta ||g||².
Therefore ||Qg||²=||g||²-||Pg||² >= (1-c_delta)||g||². Moreover Pg is fiber-constant and hence globally supported in the deleted face fiber whenever nonzero. Thus projecting a cap test with Q does NOT preserve support on the cap. Ordinary short-range resolvent or off-diagonal locality cannot be applied naively to A^-1 Qg. The estimate is a geometric property independent of the interacting vacuum; c_delta~delta^(3/2) for SU(2). The inequality is sharp at the operator norm level for g supported on cap of the form g=1_cap(W_f) times a function of all other based face coordinates.

REMARK. M_delta q is localized, but Q M_delta Q is not a local multiplication operator. The exact form <s,A^-1 Q M_delta Q A^-1 s> remains nonlocal in the deleted-face fiber. A Combes-Thomas or Agmon bound requires a proven commutator or localized-domain statement that respects this tail; neither follows from magnetic invariance.

No independently established bound on the right-hand side of Theorem 1, polynomial Penrose cap mass, deletion scaling, or continuum mass gap is claimed.
