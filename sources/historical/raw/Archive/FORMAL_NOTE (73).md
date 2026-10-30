# Localized Moser transport: exact conditional theorem and obstruction

27 October 2026. We examine an arbitrary finite SU(2) Wilson cell complex (including Penrose prism complexes) with a selected set K of k links and frozen complement v. Every retained face incident on K must be included in the local action S_0(u;v); the inserted action is V(u;v)>=0. Conditional partition functions Z_i(v)=integral_{SU(2)^k} exp(-S_i(u;v)) du, S_1=S_0+V. Conditional laws pi_i(du|v)=exp(-S_i)/Z_i du. The assumptions are normalized Haar, all face lengths and link incidences uniformly bounded, 0<=beta_p<=c_+lambda, lambda>=2, and that all faces depending on selected K are included, with their external link variables frozen at v.

## Theorem 1 (fiberwise Moser, preserving exterior)
For every v there is a smooth SU(2)^k diffeomorphism T_v with (T_v)_*pi_0(.|v)=pi_1(.|v), obtained by the weighted Poisson equation div(pi_t grad phi_t)=pi_t(V-E_pi_t V) and its complete flow. The map (u,v)->(T_v(u),v) preserves the exterior marginal of the full cavity measure. It is Bianchi-compatible because it maps actual link configurations. Its exact conditional Gibbs variational cost is
 E_pi_0[V(T_v(u);v)+S_0(T_v(u);v)-S_0(u;v)-log J_{T_v}(u)]=F(v):=log Z_0(v)-log Z_1(v).
Conditional KL=F(v)-E_pi_1 V >=0. The global cost of this fiberwise transport is E_eta0 F(v) (eta0 the cavity exterior marginal). In contrast the actual insertion free energy is -log E_eta0 exp(-F(v)). Jensen shows actual F_global <= E_eta0 F(v), possibly with order-lambda gap. Thus freezing the exterior may lose essential exterior correlations.

## Theorem 2 (relative minimum audit)
Let M_i(v)=min_u S_i(u;v) and Delta(v)=M_1(v)-M_0(v)>=0. Let L_k=(3/2)k log lambda+Ck, C independent of v and ambient volume. Because each action is smooth with global derivative bounds from bounded incidence and is minimized on compact SU(2)^k, product balls of radius c/sqrt(lambda) about its minimizer give e^{-M_i-L_k}<=Z_i(v)<=e^{-M_i}. Therefore
       Delta(v)-L_k <= F(v) <= Delta(v)+L_k.
Thus a uniformly support-local frozen-exterior transport cost would require a bound on Delta(v) at precisely that scale; the Moser equation supplies no such bound.

## Theorem 3 (explicit frustration obstruction)
For one SU(2) link u with opposite Wilson staples choose S_0(u)=lambda(1-u_0), V(u)=lambda(1+u_0), where u_0=Tr(u)/2. Both terms are legitimate oriented Wilson-plaquette factors with exterior paths frozen to opposite SU(2) values. Then S_1=2lambda for all u, Z_0=e^{-lambda}z(lambda), Z_1=e^{-2lambda}, z(lambda)=2I_1(lambda)/lambda. Consequently
 F(v)=lambda+log z(lambda)=2lambda-(3/2)log lambda+(1/2)log(2/pi)+o(1),
 Delta(v)=2lambda (because min S_0=0 and min S_1=2lambda). This is an order-lambda counterexample to any universal conditional logarithmic bound with frozen exterior, despite k=1 and 2 touched faces.

## An exact full-marginal warning
For a two-plaquette model where the second face has a genuinely free private link (now integrated, not frozen), the actual insertion free energy equals -log q(lambda)=(3/2)log lambda+O(1) even though the conditional single-link cost can be order lambda on opposing exterior staples. This demonstrates why conditional bounds cannot be substituted for annealed bounds.

## Open problem
Construct a joint exterior-interior transport with support-sized information/entropy budget, *under the actual eta0*, proving E[retained action change -log Jacobian+ inserted energy]<=C|Q|(1+log lambda), without presupposing the global ratio or a large-field probability estimate. No such unconditional theorem for arbitrary Penrose cavities is obtained by this note. The supposed volume-uniform fiberwise Moser estimate is false.
