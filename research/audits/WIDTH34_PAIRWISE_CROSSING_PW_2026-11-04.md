# Arbitrary-width pairwise PW Poisson control and width-3/4 feedback

**2026-11-04 | Self-contained original-link SU(2) finite-open-strip family theorem; exact matrix regressions.** The full mathematical report, four independently runnable verifiers, execution log, and SHA-256 manifest are supplied in the companion conversation archive **width34_pairwise_crossing_audit_2026-11-04.zip**. This theorem does **not** prove arbitrary *nested anchored* closure, convergence, an interacting lattice gap, or the continuum Yang–Mills mass gap.

## Same gauge-reduced coefficient norm throughout

For independent SU(2) face holonomies on an open straight strip, the corrected original-link positive generator is
\[
K=4\sum_i C_i+2\sum_i D_{i,i+1},\quad D_{i,i+1}=\sum_{a=1}^3R_i^a L_{i+1}^a.
\]
Degree \(n\) is spin \(n/2\), \(e_n=n(n+2)\). On an output face multidegree \(\mathbf c\), the **trace-expansion** Peter–Weyl coefficient is \(A_{\mathbf c}\), with nuclear norm \(\|A_{\mathbf c}\|_1\), dimension \(d_{\mathbf c}=\prod_i(c_i+1)\), and analytic weight \(e^{\sigma\sum_i c_i}\). Put \(P_\sigma^{(r)}(f)=\sum_{\mathbf c}d_{\mathbf c}e^{\sigma\sum c_i}(1+\max_i c_i)^r\|A_{\mathbf c}\|_1\), \(r\ge1,\sigma\ge0\). The anchored local-first \(L^{(r)}_{\kappa,\sigma}\) also sums over history intervals *inside* the anchor supremum and weights each by \(e^{\kappa|I|}\), \(\kappa>0\). This is a **face-coordinate** PW norm; do not identify it with the inequivalent original-link nuclear norm.

Let \(\mathcal B=K^{-1}Q\Gamma_K\), \(\Gamma_K(f,g)=(fKg+gKf-K(fg))/2\), and let \(Q\) discard **only the full Haar constant**. Every other SU(2)-physical output, including disconnected-minimal-support recouplings, is retained on the *connected union-history label*.

## Theorem A: any two finite histories, all degrees, arbitrary matrices

Let \(I,J\) be linked original-face intervals, let \(h=|I\cap J|\), and let \(f_I,g_J\) be arbitrary trace-expansion PW coefficient polynomials on their respective faces (including off-diagonal complex matrices; Gauss-invariant observables form a subspace). Then for every \(r\ge1,\sigma\ge0\),
\[
\boxed{P_\sigma^{(r)}(\mathcal B(f_I,g_J))\le (2+6h)
P_\sigma^{(r)}(f_I)P_\sigma^{(r)}(g_J).}\tag{1}
\]
It follows for one history-labelled pair that
\[
\boxed{\|\mathcal B_{\rm hist}([I]f_I,[J]g_J)\|_{L^{(r)}}
\le (2+6h)e^{-\kappa h}\|[I]f_I\|_{L^{(r)}}\|[J]g_J\|_{L^{(r)}}.}\tag{2}
\]
The constant depends only on **shared face count**, not either history length or highest spin. For h=3,4 the unweighted constants are 20,26.

**Proof.** Fix input multidegrees \(\mathbf a,\mathbf b\), extend by zero on unused faces, set \(D_A=\sum_i a_i(a_i+2)\), \(D_B=\sum_i b_i(b_i+2)\), \(A=1+\max a_i\), \(B=1+\max b_i\). On a fixed degree sector, each shared-link trace-norm superoperator satisfies \(\|\mathscr D_{i,i+1}\|_{1\to1}\le\sqrt{e_{a_i}e_{a_{i+1}}}/4\). AM–GM on the **path** gives \(\|K_{\mathbf a}\|_{1\to1}\le(3/2)D_A\). For every nonconstant output degree \(\mathbf c\), \(D_C=\sum_i c_i(c_i+2)\ge3\), the Neumann inverse gives \(\|K_{\mathbf c}^{-1}\|_{1\to1}\le2/D_C\). Use the *exact* polarization identity
\[
\mathcal B(f,g)=\tfrac12\{K^{-1}[(Kf)g+f(Kg)]-fg\}
\]
on each nonconstant block. Unitary facewise SU(2) CG decomposition and Schatten-1 block pinching prove the coefficient nuclear product inequality \(\sum_{\mathbf c}\|C_{\mathbf c}^*(A_{\mathbf a}\otimes B_{\mathbf b})C_{\mathbf c}\|_1\le\|A_{\mathbf a}\|_1\|B_{\mathbf b}\|_1\). Dimension and analytic output weights are submultiplicative. The first-moment **per-output envelope** is
\[
M_{\mathbf a,\mathbf b,\mathbf c}=\frac{W}{AB}
\left[\frac12+\frac{3}{2}\frac{D_A+D_B}{D_C}\right],\quad
W=1+\max_i c_i.
\]
Every allowed CG output satisfies \(|a_i-b_i|\le c_i\le a_i+b_i\), hence the exact integer inequality
\[
a_i(a_i+2)+b_i(b_i+2)-c_i(c_i+2)
\le 2a_ib_i+4\min(a_i,b_i)\le 6a_ib_i.
\]
At most \(h\) face indices carry both nonzero input degrees, so \(D_A+D_B\le D_C+6h(A-1)(B-1)\le D_C+6hAB\). Moreover \(W\le AB\), and \(W/D_C\le2/3\), the latter because the largest nonzero output degree \(c_*\ge1\) gives \((1+c_*)/[c_*(c_*+2)]\le2/3\). Thus
\[
M\le2W/(AB)+9h W/D_C\le2+6h.
\]
For \(r\ge1\), \((W/AB)^r\le W/AB\). **Pinch/sum CG blocks once**; never multiply by their count. Equation (1) follows. Since \(|I|+|J|-|I\cup J|=h\), the history factor is precisely \(e^{-\kappa h}\), proving (2).

## Theorem B: width-independent anchored crossing/end-joining operation

Let \(\mathcal B_{\rm cross}\) comprise crossing face intervals, neither containing the other, and adjacent end-joining intervals. For a fixed output anchor x, each of the four oriented crossing types charges a partner interval of prescribed overlap h to its exterior endpoint anchor. The exact pairwise estimate (2) applies before summing h. With \(t=e^{-\kappa}<1\),
\[
\boxed{\|\mathcal B_{\rm cross}(F,G)\|_{L^{(r)}}
\le\left[\frac8{1-t}+\frac{24t}{(1-t)^2}\right]
\|F\|_{L^{(r)}}\|G\|_{L^{(r)}},\quad r\ge1.}\tag{3}
\]
The proof uses the charged anchored sums and \(\sum_{h\ge0}(2+6h)t^h=2/(1-t)+6t/(1-t)^2\). Unlike the earlier crossing audit, the local coefficientwise Poisson gate in this argument is **derived directly in the stated face PW norm**, not imported from an unverified original-link/face norm transport.

## Exact width-three/four feedback and unresolved nested sum

Independent actual SU(2) original-link Fourier superoperator inversions tested 10 arbitrarily complex matrix input pairs on widths 3/4, totaling **58 nonconstant output blocks**, including fully overlapping width-four histories. An independent 2-step history feedback uses input sectors \((1,1,0,0)\), \((0,1,1,0)\), \((0,0,1,1)\): the first Poisson response has middle degree 0 **and** 2; the second has nonzero sectors \((1,0,0,1)\), \((1,0,2,1)\), \((1,2,0,1)\), \((1,2,2,1)\). They all retain their union-history labels, including disconnected-minimal-support outputs.

The same pairwise estimate **does not** close arbitrary nested anchored interactions. An outer interval of length N against N weighted singleton histories produces a **positive scalar majorant** of \(8Ne^{-\kappa}\) (at normalized input anchored norms). This only demonstrates failure of that crude majorant, **not** physical SU(2) bilinear divergence: the Casimir energy and recoupling correlations require a separate charge argument. The weighted exceptional-energy theorem and Gevrey/Borel implication remain conditional on the full nonlinear coefficientwise hypotheses. No physical interacting gap, \(\lambda=1\) convergence, 3D regulator certification, or 4D continuum mass-gap proof follows.

## Executable audit

The companion ZIP contains complete source:
- \`verify_width34_scalar.py\`: **149,655** exact/local and sampled multiwidth spin-channel charge assertions.
- \`verify_width34_matrix.py\`: **10** actual complex PW matrix test pairs and **58** original-link Fourier inverse blocks.
- \`verify_feedback.py\`: **two physical Poisson steps**, keeping every nonconstant output block.
- \`verify_crossing.py\`: **390 exact rational anchored crossing configurations**, plus the positive nested-countermajorant diagnostic.
- \`verification.log\` and \`SHA256SUMS.txt\`.

**Next gate:** replace the scalar nested positive majorant with an independently certified *coefficientwise physical* Casimir/exceptional-history summation in this same norm, or exhibit a genuine off-diagonal high-spin nested obstruction.