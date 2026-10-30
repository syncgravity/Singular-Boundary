# R3: Independent small-rotation crossing-action bound and finite-transport obstruction

27 October 2026. Scope: finite bounded-incidence SU(2) spacetime Wilson cell complexes; applies to Penrose-prism finite regulators assuming uniform incidence and bounded face length. Does not prove arbitrary-thin-support insertion bound.

## Setup
Let normalized Haar measure on SU(2)^E be dU. The undeleted Wilson action is S_0(U)=sum_{p in P_0} beta_p [1-(1/2)Tr W_p(U)], beta_p <= c_+ lambda, lambda >=1. Each edge belongs to at most D plaquettes, and plaquette boundaries have at most L edges. Let H be any collection of r distinct oriented links, and for each e in H let R_e=exp(X_e) in SU(2), with |X_e| the SU(2) geodesic angle, <=pi, and define the Haar-preserving deterministic map T(U)_e=R_e U_e for e in H, unchanged otherwise. Fixed R_e must be independent of U for this statement. The map is not a gauge transformation; its gauge-covariant form transports the chosen Lie-algebra directions at the corresponding source vertex. For fixed gauge frames, Wilson trace formulas suffice.

## Theorem (small-rotation mean action bound)
There exists C=C(D,L,c_+) such that
0 <= E_{mu_0}[S_0(TU)-S_0(U)] = D_KL(T_*mu_0 || mu_0) <= C lambda sum_{e in H}|X_e|^2,
where mu_0=e^{-S_0}dU/Z_0. Thus if |X_e|<=a/sqrt(lambda), then crossing-action expectation <= C a^2 r, independent of total volume and support shape.

Proof: Introduce T_t(U)_e=exp(tX_e) U_e. Define f(t)=E_{mu_0} S_0(T_t U). By Haar invariance for each selected link, E_{mu_0} [d/dt S_0(T_t U)|_{t=0}]= E_{mu_0} (D_X S_0)= (1/Z_0) integral D_X[-e^{-S_0}] dU=0. For each plaquette, the second derivative of d_p(T_tU) has magnitude <= C_L (sum_{e in partial p cap H}|X_e|)^2, as products of unit quaternions differentiated twice remain bounded; trace is bounded. Hence sup|f''(t)| <= C c_+ lambda sum_{p intersect H}sum_{e in partial p cap H}|X_e|^2 <= C(D,L,c_+) lambda sum_e|X_e|^2. Taylor integral f(1)-f(0) <= C lambda sum|X_e|². Nonnegativity and KL identity: density T_*mu_0(V)=exp[-S_0(T^{-1}V)]/Z_0; D_KL(T_*mu_0||mu_0)=E_mu0[S_0(TU)-S_0(U)]. (Check orientation: yes.)

## Exact variational insertion comparison
If V_Q=sum_{p in Q} beta_p d_p >=0, F_Q=-log E_mu0 exp(-V_Q), then for any Haar-preserving T,
F_Q <= E_mu0[V_Q(TU)+S_0(TU)-S_0(U)].
The proof is Jensen after substitution in Z_1 and equality E_mu0 exp[-V_Q(TU)-S_0(TU)+S_0(U)] = Z_1/Z_0. Therefore the above small-rotation estimate gives F_Q <= E_mu0 V_Q(TU)+C lambda sum_e |X_e|². This is a noncircular local *crossing-cost* result, but not a general insertion upper bound because the inserted energy remains uncontrolled.

## Repair-size obstruction
For SU(2) bi-invariant geodesic angle, a plaquette holonomy changes by at most sum_{e in its boundary cap H}|X_e| (triangle inequality on products). For each p with length <= L, |theta(W_p(TU))-theta(W_p(U))| <= L a/sqrt(lambda) under Gaussian-scale rotations. Hence a plaquette with theta(W_p(U)) >= theta_0>0 retains angle >=theta_0/2 for sufficiently large lambda and V_Q(TU) >=c lambda on that configuration. Even to reduce defects at the lambda^{-1/2} scale, plaquette angle theta~lambda^{-1/4} requires rotations on scale >=lambda^{-1/4}, for which our bound costs O(sqrt(lambda) r), not O(r log lambda). This does not prove a no-go theorem for all more sophisticated transports; it proves the small fixed rotation estimate alone cannot establish the desired bound.

One may permit random R_e independent of U with support angles <=a/sqrt(lambda); averaging preserves the mean action bound. Config-dependent rotations require inclusion of their Jacobian/entropy contribution; Haar invariance no longer automatic.

## Research status
Unconditionally proved: cutoff-uniform crossing action cost for small fixed/right-or-left rotations; exact KL representation; exact insertion transport identity. Not proved: a transport which both repairs arbitrary inserted Wilson plaquettes and has O(|Q| log lambda) crossing-cost plus entropy. Not proved: arbitrary thin Penrose insertion free energy, polymer convergence, mass gap.
