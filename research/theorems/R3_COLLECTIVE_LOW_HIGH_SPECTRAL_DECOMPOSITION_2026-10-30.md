# Low-energy spectral decomposition of the deleted-face collective orbit current
Date: 2026-10-30
Status: exact finite-volume spectral inequality and conditional cap criterion; no new Penrose spectral smallness proven.

Let K=H_f^--E_f^->=0, with finite compact SU(2) gauge-link Hamiltonian and unique normalized positive ground state Omega. Let D_{gamma,a} (a=1,2,3) be the smooth skew-adjoint dual-path SU(2) action generators from OT-1, and v_a=D_{gamma,a}Omega. For cutoff Lambda>0 set P_lo=1_[0,Lambda](K), P_hi=1_(Lambda,infinity)(K). Define L_gamma(Lambda)=sum_a ||P_lo v_a||² and S_gamma=sum_a <v_a,K v_a> (quadratic-form sense). Then exactly
J_gamma=sum_a ||v_a||² <= L_gamma(Lambda)+S_gamma/Lambda.
Proof: orthogonal spectral decomposition and K>=Lambda on Ran P_hi. No lower gap assumed. Because D_a is skew-adjoint and Omega is normalized real, <Omega,v_a>=0, so vacuum atom at eigenvalue zero vanishes, but this does NOT suppress near-zero modes.

Under the exact central-flux symmetry in OT-2 and center-even orbit Poincare, eta_f²=||Q_f Omega||² <= J_gamma/2 <=[L_gamma(Lambda)+S_gamma/Lambda]/2.
With c_delta=Haar probability of the identity holonomy cap and the exact cap bound
m_f^-(delta)>=[sqrt(c_delta)sqrt(1-eta²)-eta]_+²,
a sufficient UNPROVED condition for Haar-scale cap survival at delta~h is a choice Lambda_h such that uniformly over f in D_R and suitable gamma_f,
L_gamma(Lambda_h)+S_gamma/Lambda_h=o(h^(3/2)).
Then eta=o(h^(3/4)), c_delta~const h^(3/2), and m_f^-(delta)=(1-o(1))c_delta as a lower bound.

Representing S_gamma as the double commutator: S_gamma=-1/2 sum_a <Omega,[D_a,[H_f^-,D_a]]Omega>, and [V_-,D_a]=0, gives a purely electric source. Yet second-order [T,D_a] need not be small. Neither S nor L has been established uniformly.

Symmetry caution: the central element of the transported SU(2) action commutes with H, making Omega invariant and its orbit functions center-even. The derivative vectors D_a Omega need NOT themselves lie in any spectrally isolated or gapped sector of H. Center parity alone only removes the zero spectral atom via skew-adjointness and does not create a uniform excitation threshold.

No proof of the actual Penrose polynomial cap probability, bulk deletion theorem, or continuum mass gap.
