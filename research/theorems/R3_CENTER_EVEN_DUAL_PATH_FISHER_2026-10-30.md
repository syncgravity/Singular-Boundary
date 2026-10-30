# Center-even dual-path orbit spectral refinement and length-cost obstruction
Date: 2026-10-30
Status: proved finite-volume representation-theoretic refinement under OT-1/OT-2 group action; interacting uniform orbit Fisher smallness remains OPEN.

Setup: finite simply connected SU(2) Wilson disk H_f^-=T+V_-, unique positive normalized ground state Omega, physical generator -Delta chi_j=j(j+1)chi_j, and smooth Haar-preserving SU(2) dual-path action T_g of OT-1. Define P_f F(U)=int_G F(T_g U)dg, Q_f=I-P_f, and J_gamma(F)=sum_{a=1}^3 ||D_{gamma,a}F||_2². The center element -I acts by a center-flux string that commutes with both T and V_- (OT-2). Thus Omega(T_-I U)=Omega(U) by uniqueness and positivity.

THEOREM: ||Q_f Omega||² <= (1/2) J_gamma(Omega).
PROOF: For each U define F_U(g)=Omega(T_g U). The group action and central invariance imply F_U(-g)=F_U(g). Peter-Weyl on SU(2) decomposes such functions into integer spins j=0,1,2,...; the first nonzero Laplace eigenvalue is j(j+1)=2. Hence int_G |F_U(g)-int_G F_U|² dg <= (1/2) int_G sum_a |R_a F_U(g)|² dg. Integrate over U. Haar preservation makes left-hand side ||(I-P_f)Omega||² and right-hand side J_gamma(Omega)/2 (using covariance of group generators; if derivative frames are rotated by Ad, their squared sum is invariant). QED.

With c_delta the identity-center Haar cap and eta=||Q Omega||, OT-4 gives m_f^-(delta)>=[sqrt(c_delta)*sqrt(1-eta²)-eta]_+². Thus J_gamma=o(h^(3/2)) remains a sufficient (NOT PROVED) condition for Haar-scale cap probability at delta~h; center-even spectral gap improves only its prefactor.

LENGTH COST: Write D_gamma,a=sum_{e in crossed path} X_{e,a}(U) with unit-speed link tangents and coefficients conjugated in su(2). Cauchy in weighted link direct sum implies J_gamma(Omega)<= (sum_{e in gamma} a_e^-1) sum_{e in gamma} a_e ||grad_e Omega||². For bulk faces, OT-2 implies path length ell>=cR/h; if electric coefficients are uniformly comparable to constants, sum a_e^-1=Theta(ell) for a chosen shortest route, so this crude bound loses O(h^-1). To infer J_gamma=o(h^(3/2)) via it would require the path-local kinetic energy to be o(h^(5/2)); no such estimate is known and this is NOT asserted as necessary. Cancellations in the signed collective generators, or a direct commutator bound, must be measured before squaring.

SCOPE: does not prove the bound on actual interacting J_gamma, commutator source ||Q[T,P]Omega||, coercivity of QKQ, polynomial center-cap mass, deletion scaling, or continuum mass gap. The center-even conclusion relies on the exact group action and unique ground state of OT-1/OT-2 and should be separately rechecked if a different boundary condition or topology is used.
