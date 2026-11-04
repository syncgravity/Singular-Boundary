# P2: fixed-collar two-node SU(2) Haar reduction and positive-axis scalar-majorant Borel singularity

**2026-11-04.** Corrected original-link SU(2) open straight-square strip, independent-face Peter–Weyl trace-class norm. Expanded proof, self-contained corrected physical Fourier/tensor sources, fixed-collar numerical Jacobi verifier, exact rational positive-majorant checker, execution logs and verified SHA-256/ZIP archive: companion research artifact **p2_fixed_collar_positive_majorant_2026-11-04.zip**. These results do **not** establish physical same-grade boundedness/obstruction, infinite-volume Borel summability, interacting vacuum or a 4D Yang–Mills mass gap.

## 1. True physical one-Haar scalar with at most 162 cubature group evaluations

Let even N, m≥3, outer alternating rank-one matrix X_N (before Gauss twirl) and separately invariant inner singleton χ_m(U_j). After the complete corrected original-link Poisson source and CG projection to output face degree l=m−1 or m+1, write Z_{j,l} for the untwirled source and Y_{j,l}=T_c Z_{j,l} for the genuine Gauss-invariant source. The two-bond-collar cancellation of P-38/P-42 means
\[
Z_{j,l}=Z_{j,l}^{\rm collar}\otimes\bigotimes_{i\notin C_j}|v_i\rangle\langle w_i|,\qquad c:=|C_j|\in\{2,3\}.
\]
**Improvement:** the linear source/CG map from the *outer* fundamental-spin collar to the fused-spin source is SU(2)-equivariant because the inner χ_m is a class function and the corrected original-link K is globally equivariant. Consequently the group dependence of the overlap \(\langle Z,\pi(g)Z\pi(g)^\dagger\rangle_2\) is a degree-≤2c polynomial in the fundamental entries of g **in the nontrivial collar**, regardless of output spin l or m. This is a much sharper degree bound than treating the fused source as an arbitrary high-spin matrix.

In Hopf coordinates g=[[z,w],[-conj(w),conj(z)]], \(z=\sqrt t\,e^{i\phi},\ w=\sqrt{1-t}\,e^{i\psi}\), Haar is uniform \(dt\,d\phi\,d\psi/(2\pi)^2\). Alternating untouched spectator factors are each either z² or conjugate(z)². Their product is \(t^{N-c}e^{i\delta\phi}\), with |\delta|≤2 for even N. After angular Fourier averaging, the collar produces a real polynomial \(P_{m,l,\tau}(t)\), degree ≤c, depending only on m,l and the insertion class τ (endpoint/interior parity), not N:
\[
\boxed{\|Y_{j,l}\|_2^2=\int_0^1t^{N-c}P_{m,l,\tau}(t)\,dt,\qquad\deg P\le c\le3.}\tag{1}
\]
The effective angular Fourier degree is at most 2c+|\delta|. Exactly M=2c+|\delta|+1≤9 nodes for each angle and **Q=ceil((c+1)/2)=2 shifted Gauss–Jacobi nodes** for the radial t^(N-c) weight integrate (1) exactly. Hence **at most 162 product-group nodes**, independent of *both* N and m; endpoints use 50. Each evaluation still requires polynomial local-spin arithmetic in m. This is a structured analytic quadrature theorem, *not* a machine-precision or polynomial-bit-complexity certification.

Writing P(t)=Σ_{k=0}^c p_k t^k immediately gives the **exact rational-moment representation**
\[
\boxed{\|Y_{j,l}\|_2^2=\sum_{k=0}^c\frac{p_k}{N-c+k+1},\qquad
\lim_{N\to\infty}N\|Y_{j,l}\|_2^2=P(1)=\|Z^{\rm collar}_{j,l}\|_2^2.}\tag{2}
\]
The limit is at **fixed m and fixed insertion type**. The identity at t=1 uses residual diagonal-torus invariance of the full alternating even-N untwirled source: collar and spectator phases cancel. In the P-44 **full-inverse Schatten dual lower certificate**, D_c=3N+O_m(1), α_c→1/2, and the local collar op norm is N-independent. Each interior site lower contribution is O_m(N^−2), and the complete extensive dual certificate obeys
\[
\boxed{L_{N,m}^{\rm full\ dual}=C_m/N+O_m(N^{-2})\quad(N\to\infty,\ m\ {\rm fixed}),}\tag{3}
\]
with explicit \(C_m=\frac19\sum_{\tau=\mathrm{even,odd}}\sum_{l=m\pm1}w_l\|Z^{\rm collar}_{m,l,\tau}\|_2^2/\|Z^{\rm collar}_{m,l,\tau}\|_{op}\), \(w_l=(l+1)^2/[4(m+1)^3]\). Endpoints contribute O_m(N^−2) to the total. This is a theorem about the **lower certificate**, NOT an upper bound or asymptotic for the true physical nuclear norm; the joint \(N\sim m^2\) limit is not obtained by exchanging limits.

**Joint-regime numerical probes (NOT interval certified):** after exactly grouping the 2N output blocks into endpoints and the two interior parities and evaluating the complete *full-inverse dual lower formula*, with the common history factor e^(−κ) omitted:

| m | even N≈m² | full-inverse dual lower expression | m × lower expression |
|---:|---:|---:|---:|
| 3 | 10 | .010490463739 | .031471391216 |
| 4 | 16 | .008225724408 | .032902897631 |
| 5 | 26 | .006489432655 | .032447163275 |
| 6 | 36 | .005461655598 | .032769933585 |
| 8 | 64 | .004068836587 | .032550692698 |
| 10 | 100 | .003237929960 | .032379299600 |
| 12 | 144 | .002687461896 | .032249542758 |
| 16 | 256 | .002004610774 | .032073772391 |

The observed behavior is approximately 1/m for the **dual lower expression**. It does **not** establish that the actual physical response is bounded or grows at that rate, and is not a rigorous joint limit. A sharper valid Schatten witness or upper certificate is still required.

## 2. Rigorous positive-axis Borel singularity of the *scalar* Gevrey majorant

At κ=log4, the P-45 directly established graded scalar bound uses C=88/3, h_{ij}=C+6(i+j+2), and fundamental source M=(16/3)e^σ. Define its **nonnegative saturating scalar recurrence** (NOT the actual sign-sensitive SU(2) coefficient recurrence)
\[
\boxed{a_1=M,\quad a_n=(C+6(n+2))\sum_{i=1}^{n-1}a_i a_{n-i}\quad(n\ge2).}\tag{4}
\]
The ordinary formal series \(A(\lambda)=\sum_{n\ge1}a_n\lambda^n\) satisfies the **formal** Riccati-type differential equation
\[
\boxed{A=M\lambda+(C+12)A^2+6\lambda(A^2)'.}\tag{5}
\]
Let \(\widehat A(\xi)=\sum a_n\xi^n/n!\). The prior Gevrey-1 scalar certificate gives \(\mathrm{rad}(\widehat A)\ge9e^{-\sigma}/5120\). All a_n>0. For n≥3, the two endpoint convolution terms yield \(a_n\ge2M(C+6(n+2))a_{n-1}\ge12Mn\,a_{n-1}\), hence \(a_n/n!\ge12M\,a_{n-1}/(n-1)!\). Therefore
\[
\boxed{\frac9{5120}e^{-\sigma}\le\mathrm{rad}(\widehat A)\le\frac1{12M}=\frac1{64}e^{-\sigma}<\infty.}\tag{6}
\]
By **Pringsheim's theorem** for power series with nonnegative coefficients, \(\widehat A\) has a singularity at its strictly positive real radius. This rigorously shows why the **existing saturating nonnegative scalar majorant** cannot itself prove positive-ray continuation. It is **NOT a singularity theorem for the actual gauge-invariant SU(2) Borel transform**; the true recurrence includes sign/CG structure and possible cancellations. Observed scalar Borel adjacent coefficient ratios at orders 25,50,100,200,400 are .01036087, .01261322, .01399759, .01477695, .01519183; convergence to 1/64 is not proved.

## Independent checks and next proof gates

The companion standalone package includes corrected original-link Fourier engine and tensor-local CG source, a two-radial-node Jacobi/Hopf module, eight previously audited genuine Gauss-invariant one-Haar source values reproduced for N=2,4,10,16, a joint 8-point even N≈m² sweep through N=256, an independent high-order Jacobi comparison through m=10, and exact-rational checks of the first 99 nonnegative scalar recurrence coefficients plus 400-order high-precision ratio numerics. All logs, SHA-256 checksums and ZIP integrity passed.

**Next physical gate:** improve on the Hilbert–Schmidt Rayleigh lower witness to obtain a matching *actual* physical trace-norm lower/upper estimate along N≈m², with interval-controlled values or a closed asymptotic. **Next analytic gate:** exploit sign-sensitive SU(2) representation structure or the actual nonlinear Borel-plane Volterra equation to continue the *physical* score; the nonnegative scalar majorant is provably singular on the positive axis. Infinite-volume Borel summability, interacting vacuum, OS positivity, positive 4D continuum Yang–Mills mass gap remain OPEN.