# Joint exterior-endpoint/bridge transport in cyclic SU(2) Wilson chains
27 October 2026. Restricted exact theorem, not arbitrary Penrose spacetime result.

## Setup
Let G=SU(2) with normalized Haar dg, d(g)=1-Tr(g)/2, and q(beta)=int exp(-beta d(g))dg=e^-beta 2 I_1(beta)/beta. Define the central symmetric Wilson step density K_beta(g)=exp(-beta d(g))/q(beta)=exp(beta Tr(g)/2)/z(beta), z=2I_1(beta)/beta. For n>=1 take independent increments g_1,...,g_n with density product K_beta(g_i) dg_i and endpoint H=g_1...g_n. This is equivalent to a nonlinear nearest-neighbor Wilson Gibbs measure for cumulative holonomies H_j=g_1...g_j. Insert V=beta d(H). The insertion free energy is F_n=-log E exp(-V).

## Theorem (uniform cyclic insertion and exterior rearrangement)
For every n>=1 and beta>=1,
  0<=F_n<=-log q(beta)<= (3/2) log beta+C,
independently of chain length. More exactly,
  E exp(-beta d(H)) = q(beta) K_beta^{*(n+1)}(I)
  =q(beta) sum_{ell=1}^infty ell^2 [I_ell(beta)/I_1(beta)]^{n+1} >= q(beta).
Proof: The SU(2) central character expansion is K_beta(g)=sum_{ell=1}^infty ell[I_ell(beta)/I_1(beta)] chi_{(ell-1)/2}(g). Each scalar Fourier multiplier is alpha_ell=I_ell(beta)/I_1(beta)>0, with alpha_1=1. Convolution gives K^{*m}(I)=sum ell^2 alpha_ell^m, where m=n+1>=2. This converges absolutely at finite beta and all summands are nonnegative. Symmetry K(h^-1)=K(h) yields the insertion identity. Nonnegative V gives F_n>=0. The q asymptotic follows from the standard Bessel asymptotic.

## Explicit jointly correlated exterior transport
The endpoint h has known density p_n(h)=K_beta^{*n}(h) under the cavity. The inserted endpoint has density p_n'(h)=exp(-beta d(h))p_n(h)/R_n where R_n=q(beta)K_beta^{*(n+1)}(I) is explicitly given by the convergent character series, not an assumed estimate for an unknown Penrose partition function. Both are central with strictly positive smooth densities. Transport their SU(2) conjugacy angle by the monotone quantile map F_{p_n'}^{-1} o F_{p_n} and retain the conjugacy axis. This defines an almost-everywhere invertible, conjugation-equivariant endpoint map, h -> h'. Conditional on h, the cavity increments form an SU(2) bridge law B_h(dg_1...dg_n) supported on g_1...g_n=h. Under the insertion measure the bridge law for each fixed endpoint h is *identical* B_h, as the new factor depends only on h. Thus a Markov transport first moves h to h' by the explicit map and then samples from B_{h'}. It yields exactly the inserted joint Gibbs law, including all coupled exterior coordinates. The conditional bridge B_h is explicitly normalized through the known convolution p_n(h). A deterministic measurable transport may also be built using atomless conditional bridge isomorphisms; the explicit construction here is a randomized Markov transport.

The output measure nu is the exact inserted law, so the Gibbs variational identity gives
 E_nu V + KL(nu||mu_0) = F_n <= 1.5 log beta+C.
Consequently each nonnegative term is <= F_n. Furthermore
 E_nu S_0 <= -log Z_full <= n(1.5 log beta+C),
but this **does not** by itself yield an O(log beta) absolute bound on the signed change E_nu S_0-E_mu0 S_0. It follows instead from the KL identity that the combined signed retained-action change minus average log-Jacobian is <=F_n, if a deterministic map is used; its individual terms may cancel. For an unbranched chain, the cavity steps are independent, which makes the spectral argument possible.

## Numerical audit
The script verify.py evaluates the convergent positive series for beta=2,10,100 and n=1,2,10,100, checks K^{*(n+1)}(I)>=1 and 0<=F_n<=-log q(beta). This numerical audit is illustrative; positivity proof is exact.

## Scope and obstruction
This theorem is valid for serial Wilson increments, including long correlated cumulative-holonomy chains. It shows a noncircular exterior-marginal rearrangement with logarithmic *combined energy-entropy* cost independent of chain length. It is not a construction on an arbitrary Penrose rhombus-prism cavity: branched face interactions do not generally make endpoint increments conditionally independent Wilson steps, and the nonnegative character-multiplier argument does not automatically extend to an arbitrary multi-face gauge theory. In particular, the theorem is **not** an O(|Q| log beta) insertion result for arbitrary 3D Penrose supports; the requisite positivity, conditional bridge normalization, and support-local crossing comparison remain open.
