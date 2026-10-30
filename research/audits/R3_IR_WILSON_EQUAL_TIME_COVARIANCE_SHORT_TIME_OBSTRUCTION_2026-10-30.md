# R3-IR-442 — Equal-time covariance obstruction and exact second-order short-time Wilson response

2026-10-30. Corrective audit of R3-IR-441 using the true physical Wilson ground-state transform. This is an exact finite-volume result, not uniform spatial clustering.

Let Omega>0 be the normalized Gauss-invariant original-link Wilson ground state, mu=Omega² dHaar, and L=Omega^(-1)(H-E)Omega the nonnegative self-adjoint ground-state transformed diffusion. Its symmetric Dirichlet form is D(f,g)=sum_e a_e int grad_e f dot grad_e g dmu. Choose smooth bounded real gauge-invariant observables O supported in link set S and p supported in a DISJOINT link set T, and center them f=O-E_mu O, g=p-E_mu p. Define the actual finite-volume Euclidean time covariance
C(s)=<f,e^(-sL)g>_mu.

At time ZERO, C(0)=Cov_mu(O,p), which need not vanish even for disjoint link sets: the interacting Wilson ground-state measure is not a product measure. This is the critical boundary term absent from a naive locality-only proof strategy.

The mixed Dirichlet form is exactly ZERO:
D(f,g)=sum_e a_e int grad_e f dot grad_e g dmu=0
because no link coordinate differentiates both observables. Consequently C'(0)=-<f,Lg>=-D(f,g)=0. On smooth compact finite-volume configurations f,g belong to the domain of L and the following exact spectral expansion with integral remainder applies:

C(s)=C(0)-s D(f,g)+int_0^s (s-r)<Lf,e^(-rL)Lg>_mu dr.

Hence for disjoint supports,

boxed: |C(s)-Cov_mu(O,p)| <= (s²/2) ||Lf||_(L2(mu)) ||Lg||_(L2(mu)). (ST-1)

Also a general form-domain bound (not requiring disjointness) is
|C(s)-C(0)|<=s sqrt(D(f,f) D(g,g)),
by spectral Cauchy-Schwarz and 1-exp(-s lambda)<=s lambda. (ST-2)

Integrating ST-1 up to tau yields the short-time resolvent contribution
K_short(tau)=int_0^tau C(s)ds
= tau Cov_mu(O,p)+ R_tau,
with
boxed: |R_tau| <= (tau³/6) ||Lf||_2 ||Lg||_2. (ST-3)

There is no graph-distance decay factor in ST-1 or ST-3. Even when short-time dynamical propagation is controlled, the equal-time interacting spatial covariance remains. Therefore a genuine distant-plaquette mixing theorem must separately establish quantitative STATIC clustering of the physical vacuum, in addition to source-specific long-time decay and any dynamical locality estimate. A hypothetical finite-range commutator estimate alone cannot remove the leading tau Cov term.

For comparison, when the physical measure is Haar product (fully private link), disjoint O,p indeed have zero covariance, but this special decoupling cannot be assumed in a completed cage.

These finite-volume identities do not prove uniform static clustering, the cap response sign, half-Haar cap survival, the infrared spectral gate, or the continuum Yang-Mills mass gap.
