# R3-IR — Exact first disconnected-output channel in the physical three-face vacuum score
**Date: November 3, 2026. Exact finite original-link SU(2) calculation. Not a volume-uniform, interacting spectral-gap or continuum Yang–Mills theorem.**

## Hamiltonian and coefficient
Use the open straight three-square strip (8 vertices, 10 original links), unit electric coefficients, \(K=-\sum_{e,a}X_{e,a}^2\), \(\Gamma_K(f,g)=\sum_{e,a}(X_{e,a}f)(X_{e,a}g)\), \(V_p=-\chi_1(P_p)/2\), and independent formal magnetic variables \(z_1,z_2,z_3\). The Haar-centered formal logarithmic ground-state score obeys
\[
KS=-Q\sum_p z_pV_p+Q\Gamma_K(S,S).
\]
Let \(S_{121}=[z_1z_2^2z_3]S\) and \(H=\chi_1(P_1)\chi_1(P_3)\), whose Haar norm is 1 and original-link electric eigenvalue is \(KH=6H\).

**Exact outcome:**
\[
\boxed{\langle H,S_{121}\rangle_{\rm Haar}=-\frac{1381}{1261578240}
\approx -1.0946606054334\times10^{-6}\ne0.}
\]

## Verification and proof skeleton
The trace-word electric calculus uses original top, bottom, and vertical links—not a simplified face-neighbor electric operator—and the identities
\[
\sum_a\mathrm{Tr}(T_aP)\mathrm{Tr}(T_aQ)
=-\tfrac12\mathrm{Tr}(PQ)+\tfrac14\mathrm{Tr}(P)\mathrm{Tr}(Q),\qquad
K(fg)=(Kf)g+f(Kg)-2\Gamma_K(f,g).
\]
First orders: \(S_{100}=x/6,S_{010}=y/6,S_{001}=z/6\); centered \(S_{020}=-(y^2-1)/288\), and \(S_{110}=-xy/468+2\mathrm{Tr}(AB)/351\). The earlier corrected two-/three-face Poisson identities are reproduced.

Exact rational recursion gives a 10-dimensional fourth-order trace-word module with full-rank electric matrix. The source projection can be computed **without** final inversion because \(KH=6H\). For four unordered source partitions the corresponding \(\langle H,\Gamma_K\rangle\) are:
- \((0,0,1)+(1,2,0)\): \(0\)
- \((0,1,0)+(1,1,1)\): \(-19/10782720\)
- \((0,1,1)+(1,1,0)\): \(-1/657072\)
- \((0,2,1)+(1,0,0)\): \(0\).

All four partitions have multiplicity two. Therefore
\[
\langle H,S_{121}\rangle
=\frac13\left(-\frac{19}{10782720}-\frac1{657072}\right)
=-\frac{1381}{1261578240}.
\]
Direct inversion in the 10-dimensional fourth-order module independently produces exactly the same projection.

For exact Haar integration, tree gauge fix gives independent SU(2) face holonomies \(A,B,C\). Every fourth-order trace monomial has quaternion-coordinate degrees (1,2,1) in (A,B,C). Multiplying by \(H=\operatorname{Tr}(A)\operatorname{Tr}(C)\) makes degree 2 in each. Uniform Haar second moments \(\mathbb E[q_iq_j]=\delta_{ij}/4\) are reproduced by the four quaternion axes \(1,i,j,k\), giving
\[
\langle H,F\rangle=\frac1{16}\sum_{u\in\{1,i,j,k\}}F(1,u,1).
\]
These are **exact rational** calculations; no stochastic sampling or floating-point quadrature is used.

The expanded local audit and reproducible Python modules (trace engine, score recursion, quaternion projector, verifier, log, SHA256 manifest) are bundled as conversation artifact R3_IR_THREE_FACE_FIRST_DISCONNECTED_SCORE_2026-11-03.zip. **62 verification assertions passed**, including all lower-order recurrence residuals, independent last-step projection routes, projective Haar moment identities, and separate original-link finite-difference K diagnostics. They do not amount to independent peer review or a proof of any infinite-volume claim.

## Consequence
The previous formal multigrading theorem said the disconnected output \(\chi_1(P_1)\chi_1(P_3)\) with **connected source history** \(\{1,2,3\}\) could first appear at \((1,2,1)\). The present exact coefficient proves it **does** appear. Therefore one cannot obtain an invariant linked-cluster score space merely by projecting away disconnected output spin supports: that deletes authentic terms of the physical nonlinear recurrence. A source-linked history must be retained alongside any disconnected reconstructed spin output.

This single small coefficient does **not** prove quantitative all-order connected-tree decay, a convergent vacuum fixed point, a gap at physical coupling \(\lambda=1\), a three-dimensional spatial lattice theorem, or the continuum Yang–Mills mass gap. The next mathematical task is a coefficient-sensitive, source-multigraded linked-cluster majorant capable of retaining and bounding such channels.