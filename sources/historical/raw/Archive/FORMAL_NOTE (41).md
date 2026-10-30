# Audit of explicit transport candidates for thin Wilson insertion bounds
2026-10-27.

## Setup
Finite SU(2) lattice gauge complex, normalized Haar link measure; S_0 is the sum of retained spatial and temporal Wilson interactions, V_Q=sum_{p in Q} beta_p (1-1/2 Tr W_p), c_- lambda <= beta_p <= c_+ lambda. F_Q = -log E_{mu_0} e^{-V_Q}.

## 1. Exact variational identity and transport
For nu << mu_0, F_Q <= E_nu V_Q + D(nu||mu_0). For product-Haar-preserving bijection T,
F_Q <= E_{mu_0}[V_Q(TU)+S_0(TU)-S_0(U)].
This identity by itself cannot provide a logarithmic estimate: an explicit T with controlled total expected action remains necessary. Gauge transformations preserve both actions and hence cannot repair gauge-invariant curvature. For arbitrary local rotations, retained crossing plaquettes may incur O(lambda) cost.

## 2. Exact conditional face-coordinate transport where face holonomies are free
Suppose a measurable Haar-preserving coordinate decomposition (W_Q,V) of all links exists under which (i) W_Q are independent normalized Haar SU(2) variables, (ii) S_0 depends only on V, (iii) V_Q=sum_{p in Q} beta_p d(W_p). Then
Z_1/Z_0=prod_{p in Q} q(beta_p), q(beta)=e^{-beta} 2 I_1(beta)/beta,
F_Q=sum_{p in Q}[-log q(beta_p)] <= C |Q|(1+log lambda) for beta_p<=c_+lambda (and beta_p>=c_-lambda when seeking asymptotics). The explicit trial measure nu(dW,dV)=prod_p [e^{-beta_p d(W_p)}/q(beta_p) dW_p] mu_0^V(dV), has E_nu V_Q +D(nu||mu_0)=F_Q exactly. Proof by direct factorization; Haar measure under the coordinate map is crucial. This includes simply connected planar free-boundary gauge theory and additional geometries admitting such free face-coordinate systems, but not arbitrary 3D Penrose interior sets.

## 3. Why naïve local heat bath is circular
The exact conditional trial density dnu=e^{-V_Q}dmu_0/E_mu0 e^{-V_Q} has KL + expectation equal F_Q, but its normalizing constant IS the missing insertion partition ratio. Similarly the trial measure conditioned on low V_Q has KL cost -log mu_0(low V_Q), the missing cavity probability. Neither is an independent construction.

## 4. Test of simple global local transport
T=identity yields F_Q <= E_mu0 V_Q <= 2c_+lambda|Q|. Haar-preserving gauge transformations yield same result. Link-wise right or left multiplication by an exterior-dependent target may concentrate an inserted plaquette but perturbs undeleted plaquettes; the exact expected crossing-action shift has no generally proved O(|Q|log lambda) bound. Fixed exterior opposing staples realize O(lambda) conditional repair cost, although unconditional mean could be much smaller.

## 5. Verdict
The free-face-coordinate theorem is an explicit noncircular comparison measure with O(|Q|log lambda) cost for its stated class. An analogous measure or transport has not been established for arbitrary interior Penrose spacetime supports. The unresolved theorem is still local, cutoff-uniform control of crossing-face action changes/correlations, or an independent positivity comparison strong enough to bound the insertion ratio. No continuum polymer convergence, R3 or R2 mass gap is proved.
