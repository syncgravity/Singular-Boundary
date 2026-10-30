# R3: Explicit exterior-correlating SU(2) transport and its boundary defect

27 October 2026. All Haar measures are normalized. Finite SU(2) Wilson action on a bounded-incidence cell complex. Exact results below do not prove a uniform Penrose interior insertion estimate.

## 1. Constructive radial transport of Haar to a one-face Wilson law

Identify SU(2) with the unit 3-sphere. Write g=cos(theta)+sin(theta)n, theta in [0,pi], n in S^2. Normalized Haar measure is (2/pi)sin^2(theta)dtheta dOmega(n)/(4pi). Let d(g)=1-cos(theta) and q(lambda)=int exp[-lambda d(g)]dg=e^{-lambda}2I_1(lambda)/lambda. The normalized Wilson density is w_lambda(g)=exp[-lambda d(g)]/q(lambda).

Let F_0(t)=(2/pi)int_0^t sin^2(s)ds and F_lambda(t)= (2/(pi q(lambda)))int_0^t sin^2(s)exp[-lambda(1-cos(s))]ds. Both are continuous and strictly increasing from zero to one. Define h_lambda(theta)=F_lambda^{-1}(F_0(theta)), and Phi_lambda(cos(theta)+sin(theta)n)=cos(h_lambda(theta))+sin(h_lambda(theta))n (define at +/-identity by continuity). This deterministic bijection pushes Haar onto w_lambda(g)dg and satisfies Phi_lambda(aga^{-1})=a Phi_lambda(g)a^{-1}. Its change-of-variables Jacobian in the forward direction is 1/w_lambda(Phi_lambda(g)) almost everywhere. Let H(lambda)=int w_lambda log(w_lambda) dg = -lambda E_w[d] - log q(lambda). This is the KL cost of the transported face coordinate. As lambda->infty, E_w lambda d ->3/2 and -log q(lambda)=(3/2)log lambda -(1/2)log(2/pi)+o(1), so H(lambda)=(3/2)log lambda+O(1). For all lambda>=1 the thermal energy lambda E_w[d] is bounded (by continuity and the large-coupling asymptotic).

## 2. Exact correlated exterior transport for two plaquettes

Let e be a shared link with u and let a be an exterior private link entering the second plaquette exactly once, not any undeleted plaquette. Conditional on all variables except a, the cavity law for a is Haar, even though u is correlated with the undeleted first plaquette. Orient the second plaquette holonomy as W(u,a,v)=L(u,v) a R(u,v). The map a -> W is a Haar-preserving bijection for fixed (u,v). Define T_lambda on a by W(T_lambda a)=Phi_lambda(W(a)), keeping u,v unchanged. This is a deterministic bijection, conditionally Haar->Wilson, measurable in (u,v), gauge equivariant on the physical holonomy, and it changes the *exterior* marginal conditional on u. In the pushed-forward cavity law, W has exactly Wilson density w_lambda, independent of (u,v). The undeleted action S0 is unchanged pointwise, because a occurs in no undeleted face. Therefore E_{T_*mu0} V= lambda E_w d <= C, and KL(T_*mu0||mu0)=H(lambda)=(3/2)log lambda+O(1). Their sum is exactly -log q(lambda), the true insertion free energy. This exhibits a fully normalized exterior-correlating transport without use of the unknown interacting insertion ratio. The transport is restricted to the conditionally free exterior face coordinate; it does not handle general interior Penrose supports.

## 3. General constrained exterior transport and exact boundary cost identity

Consider an SU(2)^H exterior collar h, remaining variables w, cavity action S0(h,w), selected insertion V_Q(h,w). Let T_w be a measurable bijection on h for almost every w, differentiable a.e. with positive absolute Haar Jacobian J_T(h,w); it may depend on w and thus correlate exterior variables. Define nu=T_*mu0. Then

  KL(nu||mu0)=E_mu0[S0(T_w h,w)-S0(h,w)-log J_T(h,w)]

provided integrability. Gibbs variational principle gives

  F_Q <= E_mu0[V_Q(T_w h,w)+S0(T_w h,w)-S0(h,w)-log J_T(h,w)].

This is a genuinely independent comparison for an EXPLICIT T whose Jacobian is known. For the radial map above, the last term is O(log lambda) per coordinate, but the undeleted action change can be O(lambda) per crossing face. No general Penrose cutoff-uniform upper bound follows without controlling that term.

## 4. Conditional finite-rank flat-coordinate lemma

If a bounded collar admits a Haar-preserving product coordinate change (h,w)<->(W_1,...,W_r,v) such that the cavity law factors as mu0^v(dv) product Haar(dW_j) (although the W_j may be nonlinear functions of retained and exterior links), apply Phi_{beta_j} independently to each W_j. This gives an explicit, gauge-equivariant correlated transport with

  E_nu V_Q+KL(nu||mu0)=sum_{j=1}^r[-log q(beta_j)]

provided V_Q=sum beta_j d(W_j). Thus F_Q=sum[-log q(beta_j)] <= C r(1+log lambda). It covers all conditional free-face charts, not arbitrary interior three-dimensional supports. Merely having a local spanning tree does not imply this factorization when undeleted plaquettes share the transported variables.

## 5. Crucial logical limitation

An exterior transport can be explicit and normalized but still face an O(lambda) boundary cost. The known expected quadratic crossing cost for *fixed* rotations cannot be applied to a configuration-dependent radial map, whose rotation angles and Jacobian are correlated with the cavity field. No cutoff-uniform O(|Q| log lambda) transport has been proved on arbitrary thin interior Penrose spacetime supports. Therefore R3, continuum R2, and the Yang-Mills mass gap remain unproved.
