# R3-IR — Exact single-face SU(2) dressing and physical residual
Research: 2026-11-03. Exact finite-lattice statement, **NOT** volume-uniform interacting convergence, 3D bulk or continuum mass gap. Complete report, verifier, log, checksum manifest: conversation file R3_IR_EXACT_SINGLE_FACE_DRESSING_2026-11-03.zip.

## One-face theorem
On a square plaquette with four ORIGINAL electric links, normalized SU(2) characters \(\chi_n\) satisfy \(K\chi_n=n(n+2)\chi_n\) and \(\chi_1\chi_n=\chi_{n+1}+\chi_{n-1}\). For \(h(z)=K-z\chi_1/2\), normalize its ground eigenfunction by Haar mean one:
\[
\psi(z,U)=1+\sum_{n\ge1}a_n(z)\chi_n(U),\quad
E(z)=-za_1(z)/2,\quad
[n(n+2)-E]a_n=\frac z2(a_{n-1}+a_{n+1}),\quad a_0=1.
\]

Define the character Wiener algebra \(W\) by \(\|f\|_W=\sum_{n\ge0}(n+1)|f_n|\). SU(2) character fusion proves the algebra property with constant one, \(\|\chi_1\|_W=2\), \(\|K^{-1}Q\|=1/3\), and \(\|f\|_\infty\le\|f\|_W\). For \(u=\psi-1\), the exact fixed point is
\[
u=K^{-1}Q\left[\frac z2\chi_1(1+u)-\frac z2([\chi_1]u)u\right].
\]
For \(\|u\|_W\le1/2\) and \(|z|\le3/4\), this map has image norm at most \(25/64<1/2\) and Lipschitz constant at most \(5/16<1\). Banach contraction gives a unique small normalized eigenbranch, holomorphic in \(|z|<3/4\). The logarithm \(s=\log(1+u)\) converges in W because \(\|u\|_W\le1/2\). For real couplings in that interval, \(\psi>0\) pointwise and is the positive one-face ground-state eigenfunction. The complex analyticity radius is a **sufficient** bound, not a claim about optimal radius or the full interacting theory.

Exact perturbative coefficients:
\[
a_1=z/6-5z^3/1728+289z^5/2488320+O(z^7),\quad
a_2=z^2/96-37z^4/138240+O(z^6),\quad
E=-z^2/12+5z^4/3456-289z^6/4976640+O(z^8).
\]
The prior positive scalar tree majorant had zero radius even for one face; this exact character-resolved one-face solution proves the divergence was a deficiency of that majorant, not of the local eigenbranch.

## Exact original-link dressing residual
For a finite square strip with couplings \(z_f\), let \(\psi_f=\psi(z_f,P_f)\), \(s_f=\log\psi_f\), \(\Phi=\prod_f\psi_f\), and \(H=K-\sum_f z_f\chi_1(P_f)/2\). Then the original-link product rule gives the exact identities
\[
\boxed{\frac{H\Phi}{\Phi}=\sum_f E(z_f)+W,\qquad
W=-2\sum_{f<g}\Gamma_K(s_f,s_g),}
\]
\[
\boxed{\Phi^{-1}(H-\sum_fE_f)\Phi
=K-2\Gamma_K(\log\Phi,\cdot)+W.}
\]
Only plaquette pairs sharing an **original link** contribute to W; for a straight row, these are neighbors. Leading term:
\[
W=-\frac1{18}\sum_{f\sim g}z_fz_g\,\Gamma_K(\chi_1(P_f),\chi_1(P_g))
+O(\mathbf z^3).
\]
This is an exact algebraic reorganization, not a proof that residual polymers converge or the dressed operator is gapped uniformly in volume.

## Required regression and next objective
The exact physical three-face score projection from the prior ten-link audit is \(\langle\chi_1(P_1)\chi_1(P_3),S_{121}\rangle=-1381/1261578240\ne0\); the original verifier was rerun and passed 62 tests. The dressed identity guarantees any valid re-expansion of the same vacuum must reproduce it, but **the dressed residual series has not yet been independently evaluated to obtain that coefficient**. This is the immediate regression task.

Next: prove original-link dressed diffusion/resolvent estimates uniform in face number, build connected residual polymer bounds retaining low-energy/disconnected physical output channels, and only then address the interacting \(\lambda=1\) gap, 3D geometry and nontrivial 4D continuum mass gap.

Verification: 5,217 exact character-algebra, recurrence, contraction and majorant assertions, plus independent numerical Jacobi diagonalization. The analytic proof is written in the expanded local report; finite checker assertions are not machine-checked proofs.