# R3: Exact nonlinear guarded-block decoupling and the boundary mixing gate
26 October 2026

## Setup
Let K be a finite bounded-incidence 2+1D Penrose-derived cell complex, with SU(2) Wilson measure exp[-sum_p beta_p(1-p(W_p))] product Haar. Partition links into guards Y and interiors I_b such that every plaquette contains interior links from at most one I_b. Define S_b(X_b,Y) as all plaquette terms touching I_b, S_Y as remaining plaquettes, Z_b(Y)=int exp(-S_b)dX_b and nu_b=dX_b exp(-S_b)/Z_b. Exact Fubini disintegration: dmu=dmu_Y prod_b dnu_b, with dmu_Y proportional to exp(-S_Y)prod Z_b dY. Gauge covariance follows from invariance of Wilson action and Haar measure.

## Theorem 1: zero cross-interior conditional cumulants
For bounded observables O_b(X_b,Y), O_c(X_c,Y), distinct b,c, conditional covariance given Y vanishes. Joint interior generating function factors and its log is additive, hence all mixed cumulants across blocks vanish, including nonquadratic/higher-spin sources. Holds for every positive coupling, every lattice size, and all temporal plaquettes.

## Theorem 2: all remaining covariance is guard covariance
Law of total covariance gives Cov_mu(O_b,O_c)=Cov_muY(m_b(Y),m_c(Y)), m_b(Y)=nu_b(O_b|Y). This is not a decay theorem. Guard effective action is S_Y(Y)-sum_b log Z_b(Y). For sources supported in distinct interiors, the conditional mixed source derivative of log Z_total(Y,t) is zero, while unconditional mixed derivative of log int dY exp(-S_eff(Y,t)) is generally nonzero.

## Theorem 3: a quantitative conditional Dobrushin gate
Suppose the effective guard measure admits site conditional kernels pi_i(.|Y_{-i}), with total variation influence coefficients c_ij=sup_{Y,Y':Y_{-j}=Y'_{-j}} ||pi_i(.|Y)-pi_i(.|Y')||_TV. Assume q=sup_i sum_{j!=i}c_ij<1 and c_ij=0 when guard-site distance >R. Standard Dobrushin comparison then bounds covariances of bounded local guard observables by a constant times the geometric series D=sum_{n>=0}C^n, in a support-sensitive variation norm. As (C^n)_ij=0 for n<dist(i,j)/R and ||C^n||_infty<=q^n, the dependence tails are bounded by q^{ceil(dist/R)}/(1-q). Constants are independent of total volume, if q,R and per-observable variations are uniform. This is a conditional theorem, not verified for Wilson at beta~h^-1. The result concerns distances in coarse guard units; physical-distance decay depends on the RG scaling.

## Strong-coupling obstruction to a naive guard Dobrushin test
For a one-link SU(2) heat bath pi_k(du)=e^{k dot u}du/z(|k|), two exterior configurations can yield k=2 beta n and k=0 (two equal staples parallel versus antiparallel). As beta -> infinity, pi_{2 beta n} concentrates at n while pi_0 is Haar, and TV(pi_{2 beta n},pi_0)->1. This prevents deducing a uniformly contracting Dobrushin influence solely from Wilson positivity and bounded incidence. It does not rule out an appropriately blocked/renormalized strong-mixing theorem.

## Limits
The guard conditional exact independence is not post-integration boundary-response decay. The effective action can generate arbitrarily strong couplings: for two faces sharing an eliminated link logZ = log z(sqrt(t^2+s^2+2ts p(V))); at t=s=T its oscillation grows as 2T. Uniform small effective influences, nonlinear RG polymer bounds, Hamiltonian gap, and continuum R2 remain unproved.
