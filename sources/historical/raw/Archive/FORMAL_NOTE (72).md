# Correlated Moser transport for a finite assembled SU(2) two-prism Wilson system

27 October 2026. Scope: complete finite two-prism complex with all 20 links integrated under product normalized Haar, all 11 faces with couplings at most c_+ lambda, and the shared temporal face Q optionally deleted from the reference action. This is a combinatorial quadrilateral-prism example, not a certified Penrose-tiling extraction and not an arbitrary cavity with frozen or Gibbs-correlated outer surroundings.

## Verified incidence input
The source `../R3_two_prism_certified_2026_10_27/incidence.npz` has 12 vertices, 20 edges, 11 faces, two cells, one face shared with opposite signs, and integer boundary compositions zero. The shared face index is 3 (zero-based). Its four boundary edges are 1, 5, 8, 10. Full and single-deletion linearized curvature ranks are 9. Link-based transport automatically respects nonlinear Bianchi identities.

## Theorem (fully coupled finite-patch transport)
Let G=SU(2)^E with E=20, product normalized Haar m. For face p let d_p(U)=1-Tr(W_p(U))/2, 0<=d_p<=2. Set
S_0(U)=sum_{p not in Q} beta_p d_p(U), V(U)=sum_{p in Q} beta_p d_p(U), S_1=S_0+V, with beta_p between 0 and c_+lambda, lambda>=2. Let Z_t=int_G exp(-S_0-tV) dm, rho_t=Z_t^{-1}exp(-S_0-tV), mu_t=rho_t m. Then there exists a smooth family of diffeomorphisms T_t:G->G, T_0=id, with (T_t)_*mu_0=mu_t, constructed as the flow of a weighted Poisson vector field. In particular T_1 is an exact Bianchi-compatible, exterior-correlating, configuration-dependent link transport.

An explicitly normalizable construction is: at each t let phi_t have rho_t-weighted zero mean and solve
  div_m(rho_t grad phi_t)=rho_t(V- E_{mu_t} V).
This PDE has a smooth solution on compact connected G, since its right side integrates to 0. The smooth time-dependent vector field v_t=grad phi_t has a global flow, and the continuity equation d_t rho_t+div_m(rho_t v_t)=0 shows the claimed pushforward. The construction requires finite-volume integrals Z_t; no uniform spatial control of phi_t is asserted.

Define c_N = (3/2) E log lambda + C E for constant C depending only on c_+, maximum face length and maximum incidence. Then
  0<= F_Q= -log(Z_1/Z_0) <= -log Z_1 <= c_N,
  0<= E_{mu_1} V <= c_N,
  E_{mu_0}[S_0(T_1 U)-S_0(U)] <= c_N,
  0<= D_KL(mu_1||mu_0) = F_Q-E_{mu_1}V <= c_N,
  -E_{mu_0} log J_{T_1} <= 2 c_N.
Here J_T is the Jacobian with respect to product Haar, and the last bound is on the signed average, not on its absolute magnitude. In fact D=E_{mu_0}[S_0(TU)-S_0(U)-log J_T].

## Proof of logarithmic cost independent of insertion ratio
On product geodesic balls of radius a/sqrt(lambda) around the all-identity link configuration, all plaquette holonomy angles are <= L a/sqrt(lambda), where L is the maximal plaquette length. Thus S_1<= C E (by bounded incidence), while the normalized Haar mass is >= (c lambda^{-3/2})^E. Hence Z_1 >= exp(-CE) (c lambda^{-3/2})^E. Also Z_0<=1, so F_Q=log Z_0 -log Z_1<=-log Z_1<=c_N. For each normalized Gibbs law mu_i, nonnegative relative entropy to product Haar gives E_{mu_i} S_i <= -log Z_i. Thus E_mu1 V<=c_N, E_mu1 S_0<=c_N, E_mu0 S_0<=-log Z_0<=-log Z_1<=c_N. The latter inequality on Z holds because V>=0. The expected retained action increase is E_mu1 S_0 -E_mu0 S_0 <=c_N. Relative entropy identity D(mu_1||mu_0)=F_Q-E_mu1 V establishes the entropy estimate. Change of variables gives D = E_mu0 Delta S_0 - E_mu0 log J_T, hence -E log J = D-E Delta S_0 <=c_N + E_mu0 S_0<=2c_N.

## Important limitations
1. This pays for *all* E=20 links, not O(|Q|) for arbitrary Q in a growing volume. The construction is neither uniformly local nor effective with arbitrary exterior conditional data.
2. The elliptic vector field may be long-ranged and its intermediate action/entropy may be large. Only the endpoint cost is proven.
3. The control is for the net expected S_0 difference and signed expected minus-log-J, not for either positive part or absolute value separately.
4. The use of -log Z_1 is not a circular assumption: it is bounded independently via a product Haar small-ball estimate; this independent bound scales with the *entire patch size*.
5. No arbitrary-support Penrose thin-surface free energy theorem, RG convergence, or continuum mass gap follows.
