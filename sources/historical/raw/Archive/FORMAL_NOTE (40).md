# Independent Wilson-measure comparison: rigorous audit

Date: 2026-10-27. Model: finite bounded-incidence SU(2) lattice gauge theory with Wilson action S= sum beta_p d_p, d_p=1-1/2 Tr W_p, 0<=d_p<=2, normalized Haar link measure.

## 1. Exact independent variational *framework* (not a closed thin bound)

Write S=S_0+V_Q, V_Q=sum_{p in Q} beta_p d_p, Z_0=int exp(-S_0), Z_1=int exp(-S_0-V_Q). The insertion free energy F_Q=log(Z_0/Z_1)=-log E_{mu_0} exp(-V_Q).

For ANY probability measure nu absolutely continuous w.r.t. mu_0, Gibbs variational principle gives

F_Q <= E_nu V_Q + D(nu||mu_0).

Proof: D(nu||mu_1) = D(nu||mu_0)+E_nu V_Q - F_Q >=0, where mu_1=exp(F_Q-V_Q)mu_0. Equality at nu=mu_1. This is a rigorous independent way to prove logarithmic insertion IF a local comparison measure nu with both E_nu V_Q and D(nu||mu_0) <= C |Q| log lambda can be CONSTRUCTED. Choosing nu=mu_1 is tautological, and choosing nu conditioned on a low-energy cavity event repackages the compatibility-event criterion. No such uniform independent nu has been constructed for arbitrary interior Penrose supports.

## 2. Independent comparison via a local deterministic transport

Let T be a measurable bijection of the link space, nonsingular under normalized Haar, and set nu=T_# mu_0. Then

F_Q <= E_{mu_0}[V_Q(TU)] + D(T_#mu_0||mu_0).

If T preserves product Haar, then D(T_#mu_0||mu_0) = E_{mu_0}[ S_0(TU)-S_0(U)] (because mu_0 density e^{-S_0}/Z_0), so

F_Q <= E_{mu_0}[ V_Q(TU) + S_0(TU)-S_0(U)].

This is an exact noncircular transport inequality. The identity also follows by Jensen on Z_1/Z_0=E_{mu_0} exp[-V_Q(TU)-S_0(TU)+S_0(U)] for Haar-preserving T.

T=identity gives F_Q<=E_mu0 V_Q<=2 sum_Q beta_p (O(lambda |Q|)). Haar-preserving local link rotations can lower V_Q, but may increase S_0 by O(lambda |boundary|). A uniform transport with expected *combined* cost C|Q|log lambda remains unconstructed; its existence is a concrete independent sufficient theorem, not a proven consequence of locality.

## 3. Coupling interpolation audit

For beta_p(t)=(1-t)beta_p on Q, F_Q(theta)=log Z(beta(theta))-log Z(beta(0)) = int_0^theta sum_Q beta_p <d_p>_{beta(t)} dt. This is identity, not a bound. Convexity: second derivative Var_{beta(t)}(sum_Q beta_p d_p) >=0. Thus F_Q is convex in theta. It supplies no O(|Q|log lambda) estimate alone.

## 4. Differentiated source expectations

For 0<=t<=1, -log E_mu0 exp(-t V_Q) is nondecreasing concave in t, with first derivative <V_Q>_t and second derivative -Var_t(V_Q). Such concavity cannot constrain its endpoint value without an independent derivative or trial-measure bound.

## 5. Full-geometry limitations

The full spatial-temporal Penrose interactions remain coupled. The analytic bound 0<=V_Q<=2c_+lambda |Q| is unconditional and yields 0<=F_Q<=2c_+lambda |Q|. Neither a local transport with cost O(|Q|log lambda) nor the corresponding entropy-efficient trial measure is currently proved for arbitrary interior thin supports.

## 6. Research status

Proved: Gibbs relative-entropy variational upper bound, exact Haar-preserving local transport inequality, exact interpolation, unconditional O(lambda |Q|) bound. Open: independent cutoff-uniform O(|Q|log lambda) insertion free energy for arbitrary thin Penrose supports; uniform connected nonlinear polymer bounds, R3/R2 mass gap.

Literature context: T. Balaban, Ultraviolet stability of three-dimensional lattice pure gauge field theories, Commun. Math. Phys. 102 (1985), 255-275, DOI 10.1007/BF01229380. Its regular-lattice RG theorem should not be assumed to establish arbitrary Penrose thin-support comparison.
