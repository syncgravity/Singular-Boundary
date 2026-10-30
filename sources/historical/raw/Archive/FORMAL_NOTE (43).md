# R3: Nonlinear heat-bath repair and the necessity of transporting exterior correlations

27 October 2026. Finite SU(2) Wilson systems. This note distinguishes a complete proof for a restricted conditional transport from the unsolved correlated global transport.

## 1. Exact conditional Gibbs-optimal repair

Let u be a selected SU(2) link, and fix all exterior links v. The undeleted conditional law is dpi_k(u)=exp(k·u)du/z(kappa), with kappa=|k|, z(x)=2 I_1(x)/x, and SU(2) represented by unit quaternions. Insert one Wilson term V(u)=b(1-q·u), b>0, |q|=1, where q includes the correct orientation and parallel transport of the target plaquette. The variational identity, for any trial law nu on SU(2), is

  E_nu V + KL(nu||pi_k) >= c(k,q,b)
  c(k,q,b) = b + log z(kappa) - log z(|k+bq|).

Equality holds for the explicit tilted heat-bath law

  nu_star(du) = exp[(k+bq)·u] du / z(|k+bq|).

The finite-dimensional variational identity follows from KL(nu||nu_star)>=0. The formula includes spatial and temporal staples already contained in k. The construction is covariant under simultaneous conjugation of k,q,u by the gauge frame at the link endpoint. Note: selected links can be jointly updated by this product kernel only when no plaquette contains two selected links.

Write Delta(k,q,b)=kappa+b-|k+bq|>=0, ell(t)=log z(t)-t. Then

  c(k,q,b)=Delta(k,q,b)+ell(kappa)-ell(|k+bq|).

From z(t) comparable to exp(t)(1+t)^(-3/2) for all t>=0, one obtains

  |c(k,q,b)-Delta(k,q,b)| <= C + (3/2) log[ (1+kappa+|k+bq|)/(1+min(kappa,|k+bq|)) ]
  <= C + C log(1+kappa+b).

The first comparison is a weak generic bound; when both fields are order lambda and comparable, the fluctuation correction is O(1). A simple global statement is |c-Delta|<=C(1+log(1+kappa+b)). This does NOT control Delta.

For opposed equal fields k=b n, q=-n: |k+bq|=0, Delta=2b, and c=b+log z(b)=2b-(3/2)log b+O(1). Therefore any trial heat-bath law concentrating near the opposed target pays an order-b cost relative to pi_k. The pointwise repair cannot be logarithmic uniformly in exterior fields.

## 2. An exact two-plaquette test: failure of exterior-fixed conditional transport

Take two face loops sharing one link e and with otherwise disjoint private links, each carrying coupling lambda. Delete face 2 to form mu_0. Given exterior staple quaternions q1,q2 of the two faces, the conditional undeleted law for e is pi_{lambda q1}, and the optimal insertion/transport cost of adding face 2 is

  c(q1,q2)=lambda+log z(lambda)-log z(lambda|q1+q2|).

In the cavity mu_0, q2 is Haar independent of q1. (The private links of face 2 are absent from S_0; it suffices that at least one of them is a Haar variable.) The relative angle theta of q1^{-1}q2 has density (2/pi)sin^2(theta) on [0,pi], and |q1+q2|=2cos(theta/2). By the large-x Bessel asymptotic and dominated convergence,

  E_mu0 c / lambda -> 2 - 2 E cos(theta/2)
   = 2 - 64/(15 pi) = 0.641877... > 0.

Integral verification: E cos(theta/2) = (2/pi) integral_0^pi cos(theta/2) sin^2 theta dtheta = 32/(15pi).

On the other hand, exact private-link integration of the inserted face gives

  Z_1/Z_0=q(lambda)=exp(-lambda) z(lambda),
  F_Q=-log q(lambda)=(3/2)log lambda - (1/2)log(2/pi)+o(1).

Thus the *best* comparison measure that retains the full cavity exterior marginal and changes only the shared link has expected variational cost asymptotic to 0.641877 lambda, although the true insertion free energy is logarithmic. A comparison proof must transport or reweight the exterior (for this model, its independent Haar private link provides an exact escape route). This is a mathematically explicit limitation, not a disproof of existence of sophisticated global Penrose transport.

## 3. Joint source identity and entropy decomposition

Let v be the exterior variable, mu_0(dv,du)=eta_0(dv)pi_0(du|v). Any trial nu with marginal eta_0 and conditional nu(du|v) has KL(nu||mu_0)=E_eta0 KL(nu(du|v)||pi_0(du|v)). Its minimum variational cost for insertion V is E_eta0 c(v), NOT -log E_eta0 exp[-c(v)]. The exact insertion free energy is

  F=-log E_eta0 exp[-c(v)] <= E_eta0 c(v),

with often macroscopic Jensen gap, as in the explicit example. Allowing exterior reweighting eta_star(dv) proportional to exp[-c(v)]eta_0(dv) makes the bound exact, but eta_star normalization is the unknown insertion ratio, so this is not an independent construction. The only way forward is an explicit exterior transport or a separately normalized trial exterior law with KL+energy O(|Q|log lambda).

## 4. Consequence for R3

Unconditionally proved: the conditional optimal heat-bath kernel and variational cost, its gauge covariance; the exact two-plaquette linear-cost obstruction to exterior-fixed transport despite logarithmic true insertion cost. Not proved: an explicit independent local transport rearranging correlated exterior link fields for *arbitrary* thin Penrose spacetime supports at O(|Q|log lambda) energy+entropy; uniform nonlinear large-field contour bounds; R3; continuum R2 mass gap.
