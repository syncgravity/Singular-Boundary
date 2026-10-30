# R3-IR-444 — Repeated magnetic-cut bounds do not amplify into spatial clustering

2026-10-30. Exact finite-volume Wilson cut calculus and rigorous limitation of R3-IR-443; no assertion of regulator-uniform decay.

Partition original links into ordered disjoint nonempty shells S_0,...,S_L, with target O in S_0 and exterior P in S_L. Let H_dec be the sum of electric terms and all magnetic plaquette terms whose links are wholly inside a single shell. Let V_cross be the sum over all other retained plaquettes, so H=H_dec+V_cross, with 0<=V_cross<=2B_cross, B_cross=sum_(g crossing shells)b_g. Let delta_dec>0 be the first excitation gap of the decoupled shell Hamiltonian, which has a product positive ground state.

Applying the R3-IR-443 variational argument ONCE to this many-block decomposition gives
|Cov_H(O,P)| <= 6||O||||P|| min(1,sqrt(2B_cross/delta_dec)). (MC-1)

This is an exact, potentially coarse, bound and is not improved by introducing additional shells. Indeed B_cross is a nondecreasing sum of nonnegative crossing weights as a partition is refined; the product gap delta_dec is the MINIMUM over all shells' gaps. Neither operation produces a factor decaying in L. The proof of MC-1 gives no amplification from separation distance.

More generally, for each index i between 0 and L-1, take the single bipartition A_i=S_0 union ... union S_i, B_i=S_(i+1) union ... union S_L. With crossing magnetic budget B_i and decoupled two-block gap delta_i, R3-IR-443 gives
|Cov_H(O,P)| <= 6||O||||P|| inf_i min(1,sqrt(2B_i/delta_i)). (MC-2)
The infimum is valid because each of the cuts separately bounds the SAME physical covariance. It is not a product of cut coefficients.

In particular, even if every cut has B_i/delta_i<=epsilon with epsilon small but independent of L, the direct argument gives O(sqrt(epsilon)), NOT O(epsilon^(L/2)). Multiplying independently obtained upper bounds on the same covariance is invalid. If one instead constructs a sequential interpolation of Hamiltonians, a telescoping triangle inequality sums errors; multiplicative decay requires a separately justified contraction of conditional influence or a genuine transfer/resolvent estimate.

At physical Wilson coupling, B_i need not decay with distance and delta_i lacks a regulator-uniform lower bound. Thus MC-1 and MC-2 do not show spatial exponential clustering, the cap survival lower bound, an IR gap, or a continuum Yang-Mills mass gap.

One concrete sufficient direction for future work would be a uniform shell-to-shell oscillation contraction for conditional cap expectations in the TRUE ground-state measure. No such contraction is established here.
