# R3-IR — Nested Wilson loops generate a linearly growing low-energy channel

**November 3, 2026.** Exact finite original-link SU(2) result; a no-go for *unweighted* \(L^2\)-based anchored bilinear closure. **Not** a counterexample to positive-history-weight/projective Fourier closure; not a mass-gap proof. Complete expanded proof, script, log and hashes in the current conversation archive R3_IR_NESTED_WILSON_LOW_CHANNEL_2026-11-03.zip.

## Setup

On a finite open straight row of \(N\ge2\) square faces, let \(F_N=\mathrm{Tr}(U_{C_N})\) be the fundamental Wilson trace of the full outer rectangle, \(G_N=\mathrm{Tr}(U_{C_{N-1}})\) the trace around its first \(N-1\) faces, and \(H_N=\mathrm{Tr}(U_{\partial p_N})\) the trace on the final face. For unit original-link coefficients let

\[
K=-\sum_{e,j}X_{ej}^2,\qquad
\Gamma_K(f,g)=\frac12(fKg+gKf-K(fg)),\qquad
\mathcal B(f,g)=K^{-1}Q\Gamma_K(f,g).
\]

All Wilson traces have Haar \(L^2\) norm 1. They are exact K eigenfunctions with eigenvalues \(3(2N+2)/4\), \(3(2N)/4\), and \(3\), respectively.

## Exact theorem

\[
\boxed{\langle H_N,\mathcal B(F_N,G_N)\rangle_{\mathrm{Haar}}
=\frac{2N-1}{8}=\frac N4-\frac18.}
\]

Proof: In plaquette-holonomy coordinates for an open simply connected strip write \(F_N=\operatorname{Tr}(AB)\), \(G_N=\operatorname{Tr}(A)\), \(H_N=\operatorname{Tr}(B)\), with independent Haar A,B. Fundamental SU(2) orthogonality gives \(E_A[\mathrm{Tr}(AB)\mathrm{Tr}(A)]=\frac12\mathrm{Tr}(B)\); hence \(\langle H_N,F_NG_N\rangle=1/2\). Apply K self-adjointness in the electric product identity:
\[
\langle H_N,\Gamma_K(F_N,G_N)\rangle
=\frac{\lambda_F+\lambda_G-\lambda_H}{2}\cdot\frac12
=\frac{3N-3/2}{4}.
\]
After \(K^{-1}Q\), divide by \(\lambda_H=3\) to obtain \((2N-1)/8\).

Thus \(\|\mathcal B(F_N,G_N)\|_2\ge(2N-1)/8\), whereas \(\|F_N\|_2=\|G_N\|_2=1\). No bilinear \(L^2\times L^2\to L^2\) constant can be uniform in strip length, **even at fundamental spin**.

## Anchored norm boundary

With histories \(I_N=[1,N]\), \(J_N=[1,N-1]\), an anchored norm based on ordinary \(L^2\) coefficients and no history penalty (\(\kappa=0\)) inherits this divergence. With a positive history-length penalty \(e^{\kappa|I|}\), the same single-pair ratio is instead
\[
\frac{2N-1}{8}e^{-\kappa(N-1)},
\]
bounded for every fixed \(\kappa>0\). The strong projective Fourier norm also penalizes extended representation support. Therefore this example does **not** refute the previously reported same-radius projective bilinear bound or a possible \(\kappa>0\) anchored theorem.

The decisive remaining task is an all-history anchored estimate retaining representation-dimension weights and connected-history penalties, with explicit summation of all history-pair recouplings. Uniform interacting vacuum, \(\lambda=1\), 3D spatial construction, and continuum Yang–Mills mass gap remain open.

Reproducible exact Fraction verifier: 20,004 arithmetic/scalar checks passed for N=2..10000. These checks validate explicit coefficients but do not replace the analytic Haar argument.