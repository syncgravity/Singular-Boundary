# R3: exact compact-SU(2) transfer comparison and exterior-barrier Laplace bound

**Date:** 2026-10-27. **Status:** rigorous for the stationary completed temporal-Wilson model; the arbitrary nonstationary completed-mask problem remains open.

## Setup and scope

Let \(\Gamma=(V,E,F)\) be any finite oriented spatial cellulation (Penrose rhombi, square lattice, or another graph) with spatial plaquette words and a periodic Euclidean time circle of \(N\ge1\) steps. At each spatial slice \(t\), all spatial Wilson plaquettes carry the *same time-independent* nonnegative couplings \(\kappa_f\), so that
\[
 m(u)=\exp\{-\sum_{f\in F}\kappa_f d(W_f(u))\},\quad d(g)=1-\tfrac12\operatorname{Tr}g,\quad u\in SU(2)^E.
\]
At every temporal slab \(t\), each spatial edge \(e\) generates one temporal Wilson face with a time-independent coupling \(\beta_e\ge0\). The *completed* reference theory contains all these faces. The cavity deletes any subset \(Q\subset\{0,\ldots,N-1\}\times E\), with \(Q_t=\{e:(t,e)\in Q\}\). All links, including temporal vertex links, are integrated against normalized SU(2) Haar measure. Write \(Z_+\) and \(Z_-\) for completed and cavity partition functions.

**Theorem 1 (exact arbitrary temporal-deletion bound).**
\[
 \boxed{\frac{Z_+}{Z_-}\ge\prod_{(t,e)\in Q}z(\beta_e),\qquad
 z(\beta)=\int_{SU(2)}e^{-\beta d(g)}\,dg
 =\frac{2e^{-\beta}I_1(\beta)}{\beta},\quad z(0)=1.}
\]
In particular, for all \(\beta_e=\lambda\ge0\),
\[
 -\log(Z_+/Z_-)\le |Q|\left[\tfrac32\log(1+\lambda)+\log(6\pi)+\tfrac12\right].
\]
All constants are independent of the spatial volume, topology, Penrose phason offset, and number of temporal slabs. The theorem permits arbitrary overlapping supports and time-dependent deletion patterns \(Q\), but the *completed* theory must be time-stationary.

**Stationary-mask extension.** The same proof permits the completed reference to retain only a *fixed time-independent subset* of spatial plaquettes and a *fixed time-independent subset* of temporal edge types. In the tensor convolution, edges absent from that reference carry \(P_0\) in every slab. One may delete an arbitrary time-dependent subset of its retained temporal faces, and the same product of \(z(\beta_e)\) is obtained. Thus completeness of the reference is not required; **time-stationarity of its mask is the essential assumption**.

### Proof: SU(2) Fourier positivity

Define \(k_\beta(g)=e^{-\beta d(g)}\), and convolution \((C_\beta f)(u)=\int k_\beta(uv^{-1})f(v)\,dv\) on \(L^2(SU(2))\). SU(2) Peter-Weyl decomposition gives the eigenvalue
\[
 c_j(\beta)=\frac{2e^{-\beta}}{\beta}I_{2j+1}(\beta)\ge0,\qquad j=0,\tfrac12,1,\ldots,
\]
with \(c_0(\beta)=z(\beta)\). At \(\beta=0\), \(C_0=P_0\), the orthogonal projection onto constant functions. Hence
\[
 C_\beta-z(\beta)P_0\succeq0.
\]
The exact formula follows from \(\int_{SU(2)}f(\cos\theta)dg=(2/\pi)\int_0^\pi f(\cos\theta)\sin^2\theta\,d\theta\) and the modified-Bessel recurrence \(I_0(x)-I_2(x)=2I_1(x)/x\). The other eigenvalues follow by character orthogonality and the same recurrence.

### Proof: temporal gauge integration and Loewner order

Let \(\mathcal H=L^2(SU(2)^E)\). The gauge group \(SU(2)^V\) acts unitarily by \((h\cdot u)_e=h_{s(e)}u_e h_{t(e)}^{-1}\). Let \(P_G\) be its orthogonal averaging projection. Define
\[
 C=\bigotimes_{e\in E}C_{\beta_e},\qquad
 C_t=\bigotimes_{e\notin Q_t}C_{\beta_e}\otimes\bigotimes_{e\in Q_t}P_{0,e}.
\]
Each \(C_{\beta_e}\) is equivariant under left and right SU(2) translations (central convolution), hence \(C,C_t\) commute with \(P_G\). Direct integration over all temporal vertex links in one slab produces the kernel of \(P_G C\), respectively \(P_G C_t\). Both are positive self-adjoint trace-class operators. Since all one-edge factors commute and are positive,
\[
 C\succeq\left(\prod_{e\in Q_t}z(\beta_e)\right)C_t.
\]
Let \(M\) denote multiplication by \(m(u)\), which is a bounded positive operator. Define completed and deleted-slab transfer operators
\[
 T=M^{1/2}P_G C P_G M^{1/2},\qquad
 T_t=M^{1/2}P_G C_t P_G M^{1/2}.
\]
Then \(T,T_t\) are positive trace-class, and
\[
 T\succeq z_t T_t,\quad z_t=\prod_{e\in Q_t}z(\beta_e).
\]

### Proof: Schatten-Hölder across arbitrary time slabs

The time-stationary completed theory has \(Z_+=\operatorname{Tr}T^N\), while the deleted theory has \(Z_-=\operatorname{Tr}(T_0T_1\cdots T_{N-1})>0\). The latter trace is nonnegative because it is the original integral of strictly positive Wilson weights, not because arbitrary products of positive operators are positive. Schatten-Hölder gives
\[
 Z_-\le\prod_{t=0}^{N-1}\|T_t\|_N.
\]
From \(0\preceq T_t\preceq z_t^{-1}T\), eigenvalue monotonicity for compact positive operators yields \(\|T_t\|_N\le z_t^{-1}\|T\|_N\). Thus
\[
 Z_-\le\left(\prod_t z_t^{-1}\right)\|T\|_N^N
 =\left(\prod_{(t,e)\in Q}z(\beta_e)^{-1}\right)Z_+.
\]
This completes the exact noncommutative SU(2) proof. No claim about termwise positivity of mixed spin-network coefficients is required.

For \(\beta\ge0\), restrict the SU(2) Haar integral for \(z(\beta)\) to the geodesic ball of radius \(r=(1+\beta)^{-1/2}\le1\). Since \(d(g)=1-\cos\theta\le\theta^2/2\), the integrand there is at least \(e^{-1/2}\). The normalized Haar ball volume is \(v(r)=(r-\sin r\cos r)/\pi\ge r^3/(6\pi)\) for \(r\le1\). Therefore \(z(\beta)\ge e^{-1/2}(6\pi)^{-1}(1+\beta)^{-3/2}\), proving the explicit logarithmic estimate.

## The exact exterior-barrier target

Let \(H\) be all links of the inserted temporal faces \(Q\), \(k=|H|\), and let \(v\) denote the exterior links. Let \(S_0(u,v)\) be the retained Wilson action on all retained faces meeting \(H\), and \(S_1=S_0+\sum_{q\in Q}d(W_q(u))\). (The inserted faces have all their links in \(H\).) Define \(m_i(v)=\min_{u\in SU(2)^H}S_i(u,v)\), \(\Delta(v)=m_1(v)-m_0(v)\ge0\), and \(K_i(v)=\int e^{-\lambda S_i(u,v)}du\). The exact retained exterior marginal is proportional to \(e^{-\lambda S_{\rm far}(v)}K_0(v)dv\).

Assume every face has at most four distinct links and every link is incident to at most \(\nu\) retained-or-inserted faces. For the Penrose rhombus-prism incidence, the verified bound is \(\nu\le7\). Let \(k\ge1\), and put
\[
 b_{k,\nu}(\lambda)=e^{-1}(6\pi)^{-k}(2\nu k)^{-3k/2}(1+\lambda)^{-3k/2}.
\]

**Lemma 2 (two-sided nonlinear Laplace comparison).** Uniformly in all exterior configurations \(v\),
\[
 b_{k,\nu}(\lambda)e^{-\lambda\Delta(v)}\le\frac{K_1(v)}{K_0(v)}
 \le b_{k,\nu}(\lambda)^{-1}e^{-\lambda\Delta(v)}.
\]

*Proof.* Each \(S_i\) is smooth on the compact manifold \(SU(2)^H\), and attains a minimum \(u_i^*\). Along the simultaneous geodesics \(u_e(t)=\exp(tX_e)u_{i,e}^*\), \(|X_e|\le r\le1\), every four-link plaquette satisfies
\[
 \left|\frac{d^2}{dt^2}d(W_p(u(t),v))\right|
 \le\left(\sum_{e\in\partial p\cap H}|X_e|\right)^2.
\]
Cauchy-Schwarz and the incidence bound give \(|S_i''(t)|\le4\nu\sum_{e\in H}|X_e|^2\). At a minimizer \(S_i'(0)=0\), so \(S_i(u(1),v)\le m_i(v)+2\nu k r^2\). Choose \(r=[2\nu k(1+\lambda)]^{-1/2}\). Then \(\lambda(S_i-m_i)\le1\) on a product of \(k\) geodesic balls. Its normalized Haar measure is at least \([r^3/(6\pi)]^k\). Therefore
\[
 b_{k,\nu}(\lambda)e^{-\lambda m_i(v)}\le K_i(v)\le e^{-\lambda m_i(v)}
\]
for both \(i=0,1\), and taking ratios proves the lemma. This uses a global nonlinear Hessian bound and exact Haar geometry, **not** a Gaussian or Morse-Bott approximation.

**Corollary 3 (the requested actual-marginal bound).** For the stationary completed model of Theorem 1, with uniform temporal coupling \(\lambda\),
\[
 \boxed{\mathbb E_{\nu_{0,\Lambda}}e^{-\lambda\Delta(v)}
 \ge b_{k,\nu}(\lambda)\,z(\lambda)^{|Q|}.}
\]
Equivalently,
\[
 \boxed{\sup_\Lambda\left[-\log\mathbb E_{\nu_{0,\Lambda}}e^{-\lambda\Delta(v)}\right]
 \le\frac32(k+|Q|)\log(1+\lambda)+C_{k,\nu,|Q|},}
\]
where one explicit valid constant is
\[
 C_{k,\nu,q}=1+k\log(6\pi)+\frac{3k}{2}\log(2\nu k)
 +q\left[\log(6\pi)+\frac12\right].
\]
For the previously verified 14-temporal-face Penrose support with \(k=36\), \(q=14\), \(\nu\le7\), the logarithmic coefficient is **75**. The theorem does not require the 14 faces to lie in one temporal slab. More generally \(k\le4q\) gives coefficient at most \(\tfrac{15}{2}q\).

*Direction check:* the upper conditional bound \(K_1/K_0\le b^{-1}e^{-\lambda\Delta}\) implies \(\mathbb E e^{-\lambda\Delta}\ge b\,Z_+/Z_-\); the opposite conditional bound alone would NOT establish this.

## An abstract obstruction to dropping time-stationarity

For general nonstationary completed backgrounds, separate Loewner comparisons do not imply a trace-product comparison. For example, take rank-one orthogonal projections onto the real unit vectors \(a=(1,0)\), \(b=(1/2,\sqrt3/2)\), and \(c=(-1/2,\sqrt3/2)\). Then \(D=|a\rangle\langle a|\succeq0\), \(B=|b\rangle\langle b|\succeq0\), and \(C=|c\rangle\langle c|\succeq0\), but \(\operatorname{Tr}(DBC)=-1/8\). Thus replacing a factor \(A\) by \(A+D\) can *decrease* \(\operatorname{Tr}(ABC)\) even though \(A+D\succeq A\). This is only an abstract matrix warning, **not** a counterexample to a Wilson-gauge insertion inequality. The Schatten-Hölder argument avoids this issue by comparing every slab to one common stationary completed operator.

## Precise limitations

1. The completed reference action must be time-stationary. Theorem 1 does not prove the R3 inequality for arbitrary pairs \(R\subset R\cup Q\) if \(R\cup Q\) itself has an arbitrary time-dependent retained-face mask. This is the remaining mixed-background problem.
2. The theorem establishes a local insertion free-energy bound, not a Yang-Mills continuum mass gap, exponential clustering, or Penrose-versus-square continuum gap comparison.
3. The stated \(\nu\le7\) applies to the rhombus-prism geometry and should be recomputed for other cellulations. If couplings are face-dependent, the Hessian lemma uses their weighted incidence bound and the barrier estimate must be correspondingly adjusted.
4. Spatial insertions are not covered by the temporal convolution argument. The spatial Wilson potential is kept identical across slices and across the two compared ensembles.

## Why this is a real advance over the exterior-surgery approach

The spectral inequality \(C_\lambda\succeq z_\lambda P_0\) is a nonabelian, compact-group, exact operator statement. Schatten-Hölder converts **local Loewner control of each slab** into a global bound for an **arbitrary temporal deletion pattern**, avoiding any need to prove positivity of individual mixed spin-network coefficients or to construct a bounded-multiplicity action-decreasing surgery. The barrier Laplace bound then follows under the actual exterior Gibbs marginal via the two-sided conditional Laplace comparison.
