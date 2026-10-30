# R3-IR-448 — Non-Markov Wilson exterior-information certificate

2026-10-30. Exact finite-volume information-theoretic inequality and finite-cage Wilson bound. No physical spatial information-decay rate is proved.

Let mu be the strictly positive genuine original-link Wilson ground-state measure, let S be a fixed target-face cage, let Y_r be exterior original links at distance >=r, and let O=O(S) be a bounded real target cap multiplier. Define I_cap(r)=Var_mu(E_mu[O|Y_r]) as in R3-IR-447. Define J(r)=D_KL(mu_(S,Y_r) || mu_S tensor mu_(Y_r)), the mutual information of the actual Wilson vacuum measure. These are classical equal-time probability quantities, not vacuum von Neumann entropies.

For each exterior configuration y, let mu_(S|y) be its conditional S distribution and mu_S its marginal. The difference in expectations of O is bounded by osc(O) times their total variation distance. Pinsker's inequality TV(P,Q)^2<=D_KL(P||Q)/2, followed by averaging y, yields

boxed: I_cap(r) <= (osc_S O)^2 J(r)/2. (MI-1)

The sigma-fields Y_(r+1) are contained in those of Y_r. Relative entropy data processing implies
0<=J(r+1)<=J(r), without a Markov assumption.
For finite-volume sets define shell Z_r=Y_r setminus Y_(r+1). The exact chain rule gives
J(r)-J(r+1)=I_mu(S;Z_r | Y_(r+1))>=0. (MI-2)
This is a genuine conditional-mutual-information shell decomposition; it does not imply that J(r) decreases geometrically.

For the physical original-link Wilson state, the R3-IR-439 local cage comparison supplies a common conditional Haar density bound rho_y(s)>=epsilon_S>0 for the distribution of S conditioned on ALL complement links. It also gives rho_y(s)<=epsilon_S^(-1), and the marginal S density q_S(s) shares the same two bounds. Thus the conditional-to-marginal density ratio is at most epsilon_S^(-2). Conditioning on the smaller sigma-field Y_r retains the same bounds by averaging conditional densities. Therefore
boxed: J(r) <=2 log(1/epsilon_S). (MI-3)
This is independent of distant lattice volume but may be very loose and depends on the local magnetic-to-electric ratio. It does NOT depend on r and hence does not close clustering.

Combining gives I_cap(r)<= (osc O)^2 log(1/epsilon_S), which must be combined with the elementary I_cap(r)<=Var(O). A regulator-uniform spatial information estimate J(r)<=C exp(-2m r) would yield exponential cap exterior influence energy and static clustering via R3-IR-447, but no such bound is established for the physical completed Wilson cage. The long-time resolvent response, half-Haar cap survival, infrared spectral estimate and continuum Yang-Mills mass gap remain OPEN.
