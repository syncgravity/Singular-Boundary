# R3-IR-446 — One-block Wilson conditional Doeblin bound without a Markov assumption

2026-10-30. Exact finite-volume original-link SU(2) Wilson conditional influence estimate. It does not imply iterative spatial clustering.

Fix a finite set S of original links, with exterior Y, in the physical positive ground-state measure mu(ds,dy)=rho_y(s) ds nu(dy). R3-IR-439 proves for any time t>0 the pointwise conditional lower density bound rho_y(s)>=epsilon_S(t):=r_S(t)^2>0 for every exterior configuration y, where r_S(t)=exp[-2t B_S] prod_(e in S)m_e(t), and B_S sums ONLY retained magnetic faces incident to S.

For any y,y', both conditional distributions admit the common Haar minorant epsilon_S(t) ds. Write
rho_y ds=epsilon_S ds+(1-epsilon_S)eta_y,
rho_y' ds=epsilon_S ds+(1-epsilon_S)eta_y',
where eta_y,eta_y' are probability measures (the case epsilon_S=1 is trivial). By the definition of total variation sup_A |P(A)-Q(A)|,

boxed: ||rho_y ds-rho_y' ds||_TV <=1-epsilon_S(t). (DI-1)

For every bounded real S-cylinder observable O,

boxed: |E[O|Y=y]-E[O|Y=y']|
 <=(1-epsilon_S(t)) osc_S(O), (DI-2)

where osc_S(O)=sup_s O(s)-inf_s O(s). More generally the Dobrushin oscillation contraction of the conditional expectation operator T_S mapping an S-observable O to the function y -> E[O|y] is at most 1-epsilon_S(t), and this is independent of distant volume and all couplings disjoint from S. Taking the best time gives epsilon_S^*=sup_(t>0) r_S(t)^2>0.

This is a TRUE Wilson-specific one-block conditional influence bound. It does NOT establish decay with distance between two exterior configurations y,y': the right-hand side is the SAME irrespective of where y and y' differ. Crucially, although T_S has oscillation coefficient below one, repeated composition of T_S across nested shells is not justified without an exact conditional-expectation factorization or a separate conditional influence telescoping theorem. R3-IR-445 demonstrates that local Hamiltonian interactions do not imply the required equal-time finite-range Markov specification.

When local b/a is large under refinement, epsilon_S^* may tend to zero and the coefficient 1-epsilon_S^* may approach one. Therefore this theorem is not the desired spatial mixing or regulator-uniform cap-survival result, and proves no infrared or continuum Yang-Mills gap.
