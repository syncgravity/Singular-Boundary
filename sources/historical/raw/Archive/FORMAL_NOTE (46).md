# Bianchi-compatible transport: displacement no-go and exact free-pivot construction
27 October 2026

## Setup
Let \(G=SU(2)\), normalized Haar, \(d(g)=1-\frac12\mathrm{Tr}(g)=1-\cos\theta(g)\), geodesic angle \(\theta\in[0,\pi]\). Let \(Q\) be inserted plaquettes, \(S_0\) the nonnegative undeleted Wilson action, and \(\mu_0\propto e^{-S_0}\) the genuine cavity measure. A (possibly configuration-dependent) measurable invertible transformation \(T\) acts on actual link variables, hence automatically respects all nonabelian cellular Bianchi relations. Write \(a_e(U)=d_G(U_e,(TU)_e)\), and \(A_p(U)=\sum_{e\in\partial p}a_e(U)\) (with appropriate multiplicities).

## 1. Nonperturbative metric transport inequality
For every plaquette, \(\sqrt{d_p(U)}\le\sqrt{d_p(TU)}+A_p(U)/\sqrt2\). Therefore
\[
 \mathbb E_{\mu_0}d_p(U)\le 2\mathbb E_{\mu_0}d_p(TU)+\mathbb E_{\mu_0}A_p(U)^2.
\]
This follows from the Lipschitz property of \(\sqrt{1-\cos\theta}\) and \((x+y)^2\le2x^2+2y^2\). It holds even for arbitrary nonlinear transports and all correlations.

Consequently, if both \(\beta_p\mathbb E_{\mu_0}d_p(TU)\le C\log\lambda\) and \(\mathbb E_{\mu_0}A_p^2\le C\log\lambda/\lambda\), then \(\mathbb E_{\mu_0}d_p(U)\le C'\log\lambda/\lambda\). Thus the sought displacement/curvature bounds already IMPLY the missing local cavity curvature estimate, and cannot provide an independent proof unless that initial curvature estimate is independently available.

## 2. Exact obstruction: private face under cavity Haar
Consider a single inserted face \(p\) possessing a link \(e\) not used by any undeleted plaquette. Even if \(S_0\) contains an arbitrarily large coupled SU(2) spatial-temporal Wilson theory on the other links, conditional on all other links, \(U_e\) is Haar. Therefore \(W_p\) is Haar and \(\mathbb E_{\mu_0}d_p(U)=1\).
For every link-coordinate transport \(T\), the inequality gives
\[
1\le 2\mathbb E_{\mu_0}d_p(TU)+\mathbb E_{\mu_0}A_p^2.
\]
If \(\lambda\mathbb E d_p(TU)=O(\log\lambda)\), then \(\liminf_{\lambda\to\infty}\mathbb E A_p^2\ge1\). In particular \(\mathbb E A_p^2=O(\log\lambda/\lambda)\) is impossible. If at most \(L\) links belong to the face, \(A_p^2\le L\sum_{e\in\partial p}a_e^2\), so at least one moved link has mean squared displacement of order \(1/L^2\). This counterexample persists with nontrivial undeleted Wilson correlations elsewhere.

## 3. Explicit radial transport achieves logarithmic insertion cost but necessarily moves O(1)
Let \(q(\beta)=\int_G e^{-\beta d(g)}dg=e^{-\beta}2I_1(\beta)/\beta\). Let \(\Phi_\beta\) push Haar on \(G\) to \(q(\beta)^{-1}e^{-\beta d(g)}dg\) via quantile transport of conjugacy-class angle, retaining unit quaternion axis. If \(W_p=L(U_{\ne e})U_e^{\pm1}R(U_{\ne e})\), change the private link uniquely so \(W_p'=\Phi_\beta(W_p)\). This map is invertible almost everywhere, acts on real gauge links (thus respects Bianchi constraints), and conditionally on other links transports Haar to the single-plaquette Wilson law. The relative entropy is \(\beta\mathbb E_\nu d-\log q(\beta)\), and inserted energy plus KL equals \(-\log q(\beta)=\frac32\log\beta+O(1)\). All undeleted plaquette holonomies are unchanged; their action change is exactly zero. Nevertheless the mean squared movement is bounded below by a positive constant as \(\beta\to\infty\), by Section 2.

For a family of distinct private pivot links each absent from \(S_0\), the same argument applies successively with independent conditional Haar measures. The cost is additive and equals \(-\sum_{p\in Q}\log q(\beta_p)\), provided each target face contains its unique pivot once and no target face depends on a different pivot in an incompatible way; a triangular elimination ordering is sufficient.

## 4. General exact entropy identity and missing result
For any invertible link transport \(T\) with Haar Jacobian \(J_T\):
\[
\mathcal F_Q\le\mathbb E_{\mu_0}[V_Q(TU)+S_0(TU)-S_0(U)-\log J_T(U)].
\]
The private-pivot construction proves all terms explicitly for its class. For arbitrary interior Penrose spacetime supports there is no proved triangular private-pivot structure or small expected crossing-action cost, and no known independent local cavity curvature estimate that would justify small displacement. The desired arbitrary-support logarithmic free-energy theorem and R3/R2 mass gap remain open.

## 5. Audit
The displacement-moment condition \(\mathbb E A_p^2\lesssim(\log\lambda)/\lambda\) is **not a universal necessary property of entropy-efficient transports**; in fact it is incompatible with nontrivial curvature-repair of Haar-distributed faces. One must use potentially order-one transports with controlled Jacobian and cancellation of crossing action, or a genuinely new localized Wilson inequality. No assertion of universal transport existence is justified.
