# Joint lower-tail audit for cavity filling plaquettes (27 Oct 2026)

## Setting
Finite SU(2) Wilson cellular gauge theory with normalized product Haar link measure, plaquette defect d_p=1-(1/2)Tr(W_p) in [0,2], couplings 0<=beta_p<=c_+ lambda, lambda>=2. Delete all faces touching a link set I; denote retained (undeleted) face set P_0, number of all links N_E and face set N_P, incidence at most D. The cavity law rho_I is the Gibbs law with action S_0=sum_{p in P_0} beta_p d_p. Let Q be an arbitrary multiset of undeleted filling faces, with multiplicities a_p in nonnegative integers, total appearances A=sum_p a_p and max multiplicity a_*.

## Theorem 1 (unconditional global cavity action average)
For every coupling interpolation b in [0,beta] on P_0,

 sum_{p in P_0} b_p E_{rho_b} d_p <= C N_E (1+log lambda).

Proof: Let Z_b=integral exp(-S_b) dHaar. Relative entropy D(rho_b || Haar)=-E_b S_b -log Z_b >=0, hence E_b S_b <= -log Z_b. To bound -log Z_b, integrate all N_E link variables over balls of radius epsilon/sqrt(lambda) about identity. Each face has at most a fixed number of edges; its holonomy is within O(1/sqrt(lambda)) of identity, so b_p d_p <= C uniformly, and product Haar measure >=(c lambda^-3/2)^N_E. Thus -log Z_b<= (3/2)N_E log lambda+C(N_E+N_P) <= C_D N_E(1+log lambda) when every edge has bounded incidence. Degenerate cells with isolated links cause no problem. Note this bounds only the beta-weighted sum.

If b_p >= c_- lambda for all undeleted faces, then E sum_{p in P_0}d_p <= C N_E(1+log lambda)/lambda.

## Theorem 2 (correlated joint lower tail for macroscopically supported filling sets)
Assume beta_p>=c_-lambda for p in P_0 and A>=alpha N_E, a_*<=M, alpha>0. Then

 rho_I[sum_p a_p d_p <= 2 C M N_E (1+log lambda)/lambda] >= 1/2.

Equivalently, since N_E<=A/alpha,

 rho_I[sum_p a_p d_p <= (2CM/alpha) A(1+log lambda)/lambda] >= 1/2.

Proof: E sum a_p d_p <= M E sum_{p in P_0}d_p <= CM N_E(1+log lambda)/lambda; apply Markov. No factorization or independence, and all spatial and temporal faces are present. The conclusion is NOT uniform for thin A=o(N_E).

## Theorem 3 (conditional local lower tail with a controlled insertion normalization)
Let K be a finite set of adjustable exterior links (size r). Freeze w outside K. Let S_0(k;w) be the true cavity action touching K. Let B(k,w) be a nonnegative defect sum for any prescribed undeleted filling faces, and assume a k_*(w) exists with B(k_*,w)<=B_* and S_0(k_*,w)-min_k S_0(k;w)<=Delta_*. If changing all links in K by group geodesic <=eps/lambda changes S_0 by <=C r and B by <=C_B r/lambda (bounded face incidence/multiplicity), then

 rho_I[B<=B_*+C_B r/lambda |w] >= (c lambda^-3)^r exp[-Delta_*-Cr].

Proof: Haar balls volume >=(c lambda^-3)^r; action bound on balls, denominator <=exp[-min S_0]. The bound is correlated. The hypotheses B_* and Delta_* must be established independently and may fail for arbitrary w; this theorem does not imply unconditional polynomial probability for arbitrary thin filling sets.

## Critical separation
Bianchi/holonomy fillings imply deterministic frustration <=C lambda times filling-face defect sum under bounded shellable-fillings hypotheses. They impose no lower-tail probability under rho_I. The required event lower bound on arbitrary thin filling sets and arbitrary interior Penrose supports is still unproved. The macroscopically supported theorem above does not bridge the gap because the factor N_E/A diverges. A local thermodynamic bound or direct local cavity probability bound, independent of the desired insertion free energy, is necessary. Consequently no continuum R3 or mass-gap claim follows.
