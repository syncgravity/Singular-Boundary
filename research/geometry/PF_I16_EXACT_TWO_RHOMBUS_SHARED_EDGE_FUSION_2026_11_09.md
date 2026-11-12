# PF-I16 — Exact two-rhombus shared-edge SU(2) fusion amplitude

**Research audit 2026-11-09.** On the original authenticated five-direction accepted source rhombi and original SU(2) links; not a cubic/Voronoi surrogate. Finite, auxiliary Hamiltonian statement only. The complete derivation, exact rational arithmetic, independent quaternion simulation and manifest are preserved in Library at \`/The Singular Boundary/Proof Audits/PF_I16_TWO_FACE_FUSION_2026_11_09.zip\`.

On a fixed finite source complex, let \`H(t)=K+tV\`, \`K=sum_e a_e C_e\`, \`V=sum_f b_f(1-p_f)\`, and \`p_f=Tr(U_f)/2\`, with \`a_e>0\`. Expand the positive ground-state score \`log Omega_t=t S1+t^2 S2+...\` in its scalar-normalization-free coefficients. Then
\[
S_1=\sum_f\frac{b_f}{\lambda_f}p_f,\quad
KS_2=P_0\Gamma_K(S_1,S_1),\quad
\lambda_f=\tfrac34\sum_{e\in\partial f}a_e.
\]

Take distinct simple four-edge rhombi \`f,g\` sharing exactly one original edge \`s\`; all six other edges are distinct. Set \`X=p_fp_g\` and singlet/triplet projections along the shared edge
\[
X_0=\int_{SU(2)}X\,dU_s,\qquad X_1=X-X_0.
\]
The exact SU(2) Clebsch–Gordan decomposition of the two fundamental representations \`1/2 tensor 1/2=0 plus 1\` yields
\[
C_sX_0=0,\quad C_sX_1=2X_1,\quad
\Gamma_s(p_f,p_g)=\tfrac34X_0-\tfrac14X_1.
\]
Six external edges each carry fundamental Casimir 3/4, hence \(\Lambda_0=\frac34\sum_{e\in(\partial f\cup\partial g)\setminus\{s\}}a_e\) and \(\Lambda_1=\Lambda_0+2a_s\). Both ordered pair contributions in \(\Gamma_K(S_1,S_1)\) give the **exact history-labelled second-order amplitude**
\[
\boxed{S_{2;f,g}=\frac{2a_sb_fb_g}{\lambda_f\lambda_g}
\left(\frac{3X_0}{4\Lambda_0}-\frac{X_1}{4\Lambda_1}\right).}
\]
Haar orthogonality and the equivalent SU(2) unit-quaternion representation give \(\|X_0\|_2^2=1/64,\ \|X_1\|_2^2=3/64,\ \langle X_0,X_1\rangle=0\). So its L2 norm is **exactly**
\[
\|S_{2;f,g}\|_2^2=\left(\frac{2a_sb_fb_g}{\lambda_f\lambda_g}\right)^2
\left[\frac{9}{16\Lambda_0^2}\frac1{64}
+\frac{1}{16\Lambda_1^2}\frac3{64}\right].
\]
For all unit electric coefficients (\(\lambda_f=\lambda_g=3\), \(\Lambda_0=9/2\), \(\Lambda_1=13/2\)):
\[
\boxed{S_{2;f,g}=b_fb_g(X_0/27-X_1/117),\qquad
\|S_{2;f,g}\|_2=\tfrac7{1404}|b_fb_g|.}
\]
This is the exact **pair-history coefficient**, not an estimate of the full S2 score and not a physical mass.

If \(a_0\le a_e\le a_*\) and \(0\le b_f\le b_0\), then \(\|S_{2;f,g}\|_2\le(7/1404)a_*b_0^2/a_0^3\). Each authentic elementary source face has at most 28 edge-overlap neighbors, so the triangle inequality bounds its anchored unordered pair-history sum by \((49/351)a_*b_0^2/a_0^3\). These are fixed-order volume-independent amplitude estimates, *not* uniform convergence radii or infrared exclusion.

The checker used exact rational arithmetic for every spectral coefficient and independent 400,000-sample quaternion SU(2) Monte Carlo to test the singlet/triplet Haar norms, orthogonality, shared-link gradient identity and amplitude norm. It passed. The six-exterior-link electric energy is **lower** in the shared-link singlet than in the triplet channel, explicitly confirming the recoupling issue that defeats naive order-growing denominator arguments.

**Still OPEN:** all-order cluster amplitude summability; collective interacting Poincare inequality; source-selected physical time/kinetic normalization; continuum and OS reconstruction; four-dimensional Yang–Mills mass gap. No canonical proof gate or historical archive was changed.