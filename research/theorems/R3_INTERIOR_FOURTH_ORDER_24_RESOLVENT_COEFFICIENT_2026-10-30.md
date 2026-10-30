# Exact fourth-order interior deleted-face response: 24 electric-resolvent contractions
Date: 2026-10-30
Status: exact perturbative coefficient and finite-volume norm bound. NONVANISHING NOT VERIFIED.

Consider an interior deleted simple rhombus f having four distinct neighboring retained faces g1,...,g4. Let the only active magnetic terms be b_i(1-p_i) for these four neighbors, with all other magnetic couplings zero. T=sum_e a_e(-Delta_e) on the physical SU2 gauge invariant Hilbert space, all a_e>0, normalized Haar constant 1 its simple ground state at b=0. Let Q_f be canonical deleted-holonomy Haar complement. Let R=(T|_(1^perp))^-1 extended by 0 on constants; gamma_T>0 its positive spectral bottom. All four p_i are bounded real Wilson half-traces, ||p_i||_infty<=1.

For the ground state Omega(b) normalized in L2 with <1,Omega(b)>>0, analytic perturbation theory near b=0 and the exposed-edge theorem show Q_f Omega(b)=0 whenever any b_i=0. Thus the first potentially nonzero coefficient is mixed b1 b2 b3 b4. In the ground-state equation (T-sum_i b_i p_i)Omega=e(b)Omega (discarding scalar sum_i b_i), squarefree fourth-order coefficient after application of Q is
C_f=partial_b1 partial_b2 partial_b3 partial_b4 Q_f Omega|_0
= Q_f sum_(sigma in S4) R p_sigma1 R p_sigma2 R p_sigma3 R p_sigma4 1.
Energy-coefficient terms in the Rayleigh-Schr. recursion are killed by Q: each term uses a proper subset of the four couplings and at least one exposed f edge; on states independent of such an exposed link R preserves that independence because the original T is a sum of independent link Laplacians. Normalization terms are likewise supported in proper subsets or constants. Care: this formula assumes other magnetic couplings are zero, so the perturbative reference Hamiltonian is T; with other couplings fixed, replace R and rederive.

Elementary quantitative bound: ||R||<=1/gamma_T, each multiplication p_i has norm<=1, Q contraction, there are 4!=24 terms; hence ||C_f||_L2<=24 gamma_T^-4. With physical Casimir, gamma_T >=(3/4) min_e a_e as every nonconstant link Peter-Weyl mode carries j>=1/2; this is crude and may not be useful under h refinement.

This formula identifies a finite exact SU2 recoupling calculation but does NOT establish nonzero C_f, a numerical Penrose coefficient, uniform vacuum cap probability, or continuum mass gap. The previously indexed face star [0; neighbors 2,4,10,1] is from a periodic M=5 approximant, not a verified open-disk embedding. No 24-term exact contraction for it was computed in this entry.
