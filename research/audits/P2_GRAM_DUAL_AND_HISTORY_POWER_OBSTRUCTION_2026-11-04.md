# P2: Schatten dual certificates and the super-Gaussian history Banach algebra obstruction

**2026-11-04 | Corrected original-link SU(2) finite open straight square strip, one gauge-reduced face-Peter–Weyl trace-expansion norm.** Expanded report, corrected physical Fourier engine, four independent completed regressions, execution log, verified SHA-256 manifest and ZIP integrity: conversation archive \`p2_gram_dual_weighted_no_go_2026-11-04.zip\`. **Not** a physical high-spin same-grade no-go, infinite-volume Borel summability, positive interacting gap or 4D continuum mass-gap result.

## A. Certified trace-norm dual bracket from tensor-local Gram matrices

The previously proved P-38 tensor factorization of each q-truncated physical output block is \(X=UV^\dagger\). Its r×r Hermitian positive Gram matrices are \(A=U^\dagger U\), \(B=V^\dagger V\), whose entries factor into **local face overlaps**. Let \(T=\mathrm{tr}(AB)=\|X\|_{S_2}^2\), \(u=\sqrt{\|A\|_{\rm op}\|B\|_{\rm op}}\) and \(r_*=\min(\operatorname{rank}A,\operatorname{rank}B)\). Then the exact **two-sided certificate**
\[
\boxed{\frac{T}{u}\le\|UV^\dagger\|_{S_1}\le\sqrt{r_*T}}\tag{1}
\]
follows directly. The lower bound has the explicit valid Schatten dual observable \(W=X/u\): \(\|W\|_{\rm op}\le1\), \(\operatorname{Re}\operatorname{tr}(W^\dagger X)=T/u\). The upper bound is Cauchy on at most r_* singular values. If X=0, both are zero. No exponential-dimensional Fourier matrix is necessary to form these quantities. Numerically safe enclosures for \(\|A\|_{\rm op},\|B\|_{\rm op}\), \(T\) and ranks require a separate implementation.

For the actual **summed physical Gauss-invariant** high-spin singleton insertion response \(R_{N,m}\), denote each independent sector by \(c=(j,l)\), \(l=m\pm1\), and its positive Fourier dimension/moment normalization by \(w_c\). Apply (1) to each q-truncated Neumann block \(X_{c,[q]}\), sum the resulting lower/upper bounds \(L_q,U_q\), and include the previously certified full physical Neumann remainder \(\Delta_q\):
\[
\boxed{\max(0,L_q-\Delta_q)\le R_{N,m}\le U_q+\Delta_q.}\tag{2}
\]
This is a valid structured dual interval, not an asymptotic result. For first-moment grade r=1, σ=0, the **correct** Fourier sector factor is
\[
w_{j,l}=\frac{(l+1)^2}{4(m+1)^3}.
\]
It is important not to substitute (m+2) for (l+1) in the lower CG output l=m−1. Corrected original-link full gauge-invariant matrix responses and q=0 Gram dual enclosures (the history discount e^-κ is omitted):
| N | m | L_0 | direct q0 nuclear | U_0 | exact physical |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 0.05626390 | 0.06556450 | 0.06918140 | 0.07239097 |
| 2 | 4 | 0.04904075 | 0.05721637 | 0.05981416 | 0.06125810 |
| 4 | 3 | 0.07289734 | 0.11013522 | 0.16608637 | 0.12912501 |
| 4 | 4 | 0.07006959 | 0.10410337 | 0.15495852 | 0.11698333 |

The table encloses **q0**, not the full physical response until \(\Delta_0\) is added. Exact finite checks passed, but no positive large-width dual limit is certified at N=m²+O(1).

## B. Entire Banach-valued Borel continuation for every power p>2, and limits of its growth

For the exactly stabilized infinite-row **formal fundamental-source score**, fixed-history Borel components obey \(P_\sigma^{(1)}(\widehat S_{\infty,I}(\xi))\le(e^{B_L|\xi|}-1)/(4(2+6L))\), with \(B_L\le b_\sigma L^2\), \(b_\sigma=128e^\sigma/3\). For any p>2, a>0, κ>0 define
\[
\|F\|_{a,p;\kappa,\sigma}=\sup_x\sum_{I\ni x}e^{\kappa |I|-a|I|^p}P_\sigma^{(1)}(f_I).
\]
Since exactly L histories of length L contain a fixed anchor x, the formal Borel transform is entire in this weakened history Banach space. Optimizing \(b_\sigma R L^2-(a/2)L^p\) gives
\[
\boxed{\|\widehat S_\infty(\xi)\|_{a,p;\kappa,\sigma}
\le C_{a,p,\kappa}\exp[D_{a,p,\sigma}|\xi|^{p/(p-2)}],}\tag{3}
\]
where
\[
D_{a,p,\sigma}=\frac{p-2}{p}b_\sigma\left(\frac{4b_\sigma}{ap}\right)^{2/(p-2)},
\quad
C_{a,p,\kappa}=\frac14\sum_{L\ge1}\frac{L}{2+6L}e^{\kappa L-(a/2)L^p}<\infty.
\]
p=3 recovers the original order-three majorant, p=4 yields order two, p=6 yields order 3/2. The guaranteed growth exponent p/(p−2) remains **strictly larger than one at every finite p>2**. This majorant alone cannot justify positive-ray Laplace integrability. It does not prove the actual Borel function grows that fast, nor that a true Borel sum is impossible.

## C. Important correction: these weighted spaces are not nonlinear Banach algebras

A decisive **gauge-invariant** counterexample demonstrates that the unrestricted history-labelled Poisson bilinear map is **unbounded** on every norm \(\|\cdot\|_{a,p;\kappa,\sigma}\) with a>0 and p>1. Take connected history \(I_L=[1,L]\) but place the gauge-invariant one-face character at face 1:
\[
F_L=G_L=[I_L]\otimes\chi_1(U_1).
\]
These are valid **history-labelled algebra** inputs whose minimal active support is smaller than their declared history. The algebra explicitly allows such nonminimal history tags (as it retains them in output). In the corrected physical electric generator, Kχ1=3χ1 and Kχ2=8χ2. Because χ1²=1+χ2, the true centered Poisson response is
\[
\boxed{\mathcal B(\chi_1(U_1),\chi_1(U_1))=-\chi_2(U_1)/8.}
\]
For any integer spin grade r≥0, with \(P_\sigma^{(r)}(\chi_n)=(n+1)^{r+2}e^{\sigma n}\), and since both input history labels and the union output label equal \(I_L\), the **exact normalized ratio** is
\[
\boxed{\frac{\|\mathcal B_{\rm hist}(F_L,G_L)\|_{a,p;\kappa,\sigma}}
{\|F_L\|_{a,p;\kappa,\sigma}\|G_L\|_{a,p;\kappa,\sigma}}
=\frac{9\,3^r}{8(4\,2^r)^2}\exp(aL^p-\kappa L)
\xrightarrow{L\to\infty}\infty.}\tag{4}
\]
Thus the whole unrestricted Poisson history algebra **cannot** be used as a bounded-bilinear fixed-point space merely because the specific formal Borel transform is entire in the weaker norm. This does **not** establish failure of boundedness on a smaller **source-generated** subspace with appropriate minimal/connected-history restrictions, nor does it affect the existence of the individual entire Borel function.

## Independent reproducibility and open gates

The companion archive contains fully standalone corrected physical Fourier engine, 20 arbitrary complex local-tensor Gram dual tests, four complete physical response/block dual checks (N=2,4; m=3,4), exact rational SU(2) χ1×χ1 centered-Poisson counterexample at spin grades 0–5, and whole-power Borel bound tests p=5/2,3,4,6,10. All logs, SHA-256 hashes and ZIP integrity pass.

**Next:** obtain a large-N≈m² dual lower bound (or upper certificate) for the actual Gauss-invariant summed insertion, rather than mere low-rank representation and loose Gram enclosures; and identify a source-reachable nonlinear norm/sector carrying sufficiently strong anchored long-history control for positive-ray Borel summability. Infinite-volume interacting gap, Osterwalder–Schrader reconstruction and 4D continuum Yang–Mills mass gap remain OPEN.
