# Exact Gauss-twirl singular spectrum and fixed-history entire Borel transform

**2026-11-04 — P2 mathematical audit.** Finite original-link SU(2) open straight square strip, in one independent-face trace-expansion Peter–Weyl nuclear norm. This establishes the full singular spectrum of a *genuine residual Gauss-invariant* balanced intertwiner at every even history width, and entire Borel continuation of the *individual fixed-history components* of the infinite-row formal fundamental-source score. **Neither result proves a width-uniform physical Poisson response, infinite-row Borel continuation in the global anchored norm, physical interacting vacuum, or the continuum Yang–Mills mass gap.**

The expanded detailed proof, two independently executed verifiers, run logs and SHA-256 checked ZIP are preserved in conversation artifact \`p2_spin_spectrum_historywise_borel_2026-11-04.zip\`.

## Theorem A: all-even-width singular values of the actual invariant coefficient

Let \(N=2k\ge2\), \(v=|+,-,\ldots,+,-\rangle\), \(w=|-,+,\ldots,-,+\rangle\) in \((\mathbb C^2)^{\otimes N}\), and \(X=|v\rangle\langle w|\). The actual SU(2) residual Gauss projection
\[
T_N=\int_{SU(2)}g^{\otimes N}X(g^\dagger)^{\otimes N}\,dg
\]
has the **complete nonzero singular spectrum**
\[
\boxed{s_j=\frac{\binom{2k}{k-j}}{(k+j+1)\binom{2k}k},
\quad\text{multiplicity }2j+1,\quad j=0,\ldots,k.}
\]
In particular
\[
\boxed{\|T_N\|_{S_1}=1,\quad\|T_N\|_{S_2}^2=\frac1{N+1},\quad
\|T_N\|_{\rm op}=\frac2{N+2},\quad\operatorname{rank}T_N=(k+1)^2.}
\]
**Proof:** diagonal SU(2) decomposes the \(N\)-fold tensor representation into total spin \(j\in\{0,\ldots,k\}\). The two balanced computational weight-zero states have equal projected multiplicity norms, with relative spin-flip phase \((-1)^{k+j}\). For \(C=\binom{2k}k\) the squared norm in spin j is \(\mu_j/C\), \(\mu_j=\binom{2k}{k-j}-\binom{2k}{k-j-1}=(2j+1)\binom{2k}{k-j}/(k+j+1)\). Twirling therefore leaves an \(I_{2j+1}/(2j+1)\) times rank-one multiplicity matrix, of singular value \(\mu_j/[(2j+1)C]\). The S1 sum is one, the nonzero rank is \(\sum_j(2j+1)=(k+1)^2\), and monotonicity gives \(s_0=1/(k+1)\). Independently, the Hilbert–Schmidt orthogonal-projection identity gives \(\|T_N\|_2^2=\int dg |\alpha|^{2N}=1/(N+1)\), since \(|\alpha|^2\) is uniform on [0,1] under Haar SU(2).

This gives a scalable exact total-spin spectral description of the invariant outer **input**; it does **not** evaluate or bound its corrected original-link nonlinear Poisson response to a **sum** of high-spin characters for \(N\sim m^2\). Sector additivity from P-30 continues to hold and the physical same-grade question remains open.

## Theorem B: entire Borel continuation for every fixed connected history

Let I be a fixed connected interval with length \(L\ge1\). Retain every history label and define the **finite unweighted history** norm
\[
\|F\|_{\mathscr H_I}=\sum_{J\subseteq I,\ J\ {\rm connected}}P_\sigma^{(1)}(f_J).
\]
The independently certified **pairwise** face-coordinate Poisson theorem (P-22) bounds the complete history bilinear operation **on this fixed interval**:
\[
\|\mathcal B_{\rm hist}(F,G)\|_{\mathscr H_I}\le C_L\|F\|_{\mathscr H_I}\|G\|_{\mathscr H_I},
\qquad C_L=2+6L.
\]
For the fundamental magnetic singleton source, \(\|A_I\|_{\mathscr H_I}=M_L=(4/3)Le^\sigma\). The exact formal source-order recurrence and Catalan estimate imply
\[
\|S_{I,n}^{\rm family}\|_{\mathscr H_I}
\le\operatorname{Cat}_{n-1} C_L^{n-1}M_L^n
\le(4C_L)^{n-1}M_L^n.
\]
P-31 showed **exact historywise stabilization** of the infinite-row source coefficients: the coefficient carrying history exactly I is unchanged by enlarging the finite strip containing I. Hence its *actual formal-coefficient* Borel transform has an **entire continuation**, with explicit bound
\[
\boxed{\widehat S_{\infty,I}(\xi)=\sum_{n\ge1}\frac{S_{\infty,n,I}}{n!}\xi^n
\ \text{entire in }\xi\in\mathbb C,}
\]
\[
\boxed{
P_\sigma^{(1)}(\widehat S_{\infty,I}(\xi))
\le\frac{\exp\left[\frac{16}3 e^\sigma L(2+6L)|\xi|\right]-1}{4(2+6L)}.
}
\]
The **history-labelled** finite algebra was used so this does not assume cancellation between reconstructed histories.

**Essential limitation:** the exponential type is \(O(L^2)\). Summing these **upper bounds** over unbounded lengths with \(e^{\kappa L}\) does not give a convergent global anchored estimate at any nonzero \(\xi\). This is **not proof** that the actual global Borel transform fails to continue. Families with individually entire components \(\xi^{|I|}\) may have only finite Banach-valued disks. Thus componentwise entire continuation does **not** establish a globally Banach-valued positive-ray Borel function, an infinite-volume Laplace sum, or a physical interacting measure.

## Reproducibility and next gates

The companion package contains: an exact rational spectrum audit for all even widths N=2..200 (S1, S2, operator norm and rank), full dense SU(2) Gauss-twirl comparisons at N=2,4,6, and 5,000 exact Catalan/historywise Borel coefficient checks over fixed interval lengths 1..100 and orders 1..50. SHA-256 manifest and ZIP integrity passed.

**Next:** exploit the exact total-spin spectrum as an input to a scalable transfer/coupled-spin calculation of the *physical summed Poisson response* along N=m²+O(1); independently seek volume-uniform global-norm or suitable local-topology positive-ray continuation/growth for the **actual** nonlinear Borel Volterra solution. None of these two outstanding proofs is supplied by the present input-spectrum or fixed-history results.