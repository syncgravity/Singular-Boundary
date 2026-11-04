# R3-IR — Exact gauge-invariant fixed-grade anchored bilinear no-go (2026-11-03)

**Status: rigorous explicit negative theorem for the specified history-aware original-link SU(2) free-electric bilinear map.** This disproves the conjectured **uniform** \(L^{(1)}\times L^{(1)}\to L^{(1)}\) bound and every fixed polynomial maximum-spin grade \(r\ge0\). It does *not* disprove nonlinear convergence on a smaller physically selected class, or the Yang–Mills mass gap. Expanded proof, exact Fraction verifier, log and hashes: current conversation archive R3_IR_FIXED_GRADE_PHYSICAL_NOGO_2026-11-03.zip.

## Norm/operator
On finite open straight square strips, \(K=-\sum_{e,a}X_{e,a}^2\), \(\Gamma(f,g)=[fKg+gKf-K(fg)]/2\), \(\mathcal B=K^{-1}Q\Gamma\). The standard original-link Fourier projective norm is \(\|f\|_{P_\sigma}=\sum_{\mathbf n}d_{\mathbf n}e^{\sigma\sum_en_e}\|A_{\mathbf n}\|_{S_1}\). For connected history intervals I use
\[
\|F\|_{L^{(r)}_{\kappa,\sigma}}=\sup_x\sum_{I\ni x}e^{\kappa|I|}\sum_{\mathbf n}d_{\mathbf n}e^{\sigma\sum_en_e}(1+\max_en_e)^r\|A_{I,\mathbf n}\|_{S_1}.
\]
History supports are connected but reconstructed occupied spin support may be disconnected, as in the project's retained-history definition. Fix any \(\kappa>0,\sigma\ge0,r\ge0\).

## Explicit physical family
Choose \(s\ge3\), \(k\ge2\), an open strip of \(N=2k-1\) square faces, and the k alternating odd faces \(p_i=2i-1\). Their four-link boundaries are pairwise edge-disjoint. Let \(W_n(p)=\chi_n(U_{\partial p})\), the gauge-invariant SU(2) Wilson character of integer twice-spin n, and
\[
F_k=[1,N]\otimes\prod_{i=1}^kW_1(p_i),\qquad
G_{k,s}=\sum_{i=1}^k[\{p_i\}]\otimes W_s(p_i).
\]
The first history is connected despite disconnected occupied spin support; all k nested fusion outputs retain history [1,N].

The original-link electric eigenvalues and character identity are
\[
K F_k=3k F_k,\quad K W_s(p_i)=s(s+2)W_s(p_i),\quad
W_1(p_i)W_s(p_i)=W_{s+1}(p_i)+W_{s-1}(p_i).
\]
Put \(F_{\widehat i}=\prod_{j\ne i}W_1(p_j)\). The exact physical Poisson output is
\[
\boxed{\mathcal B(F_k,W_s(p_i))=
F_{\widehat i}\left[
-\frac{s}{(s+1)(s+3)+3(k-1)}W_{s+1}(p_i)
+\frac{s+2}{(s-1)(s+1)+3(k-1)}W_{s-1}(p_i)\right].}
\]
There is no zero-mode output. All channels remain gauge invariant.

## Exact Fourier normalization
For the oriented square word \(U_1U_2U_3^{-1}U_4^{-1}\), in representation dimension \(d=n+1\), the original-link coefficient matrix (using conjugate reps on reversed links) is unitarily equivalent to
\[
A=\sum_{a,b,c,h=1}^d|b,c,c,h\rangle\langle a,b,h,a|.
\]
Its nonzero singular values are d repeated \(d^2\) times, so \(\|A\|_{S_1}=d^3\). With the Fourier dimension factor \(d^4\),
\[
\boxed{\|W_n(p)\|_{P_\sigma}=(n+1)^7e^{4\sigma n}.}
\]
Projective norms factor across disjoint link sets. For \(s\ge3\), distinct inserted faces and plus/minus output branches occupy distinct original-link spin sectors: their projective contributions therefore add without cancellation.

## No-go conclusion
The exact norm ratio (including both physical channels) is
\[
\begin{aligned}
\mathcal R_{k,s}^{(r)}&=
\frac{\|\mathcal B_{\rm hist}(F_k,G_{k,s})\|_{L^{(r)}_{\kappa,\sigma}}}
{\|F_k\|_{L^{(r)}_{\kappa,\sigma}}\|G_{k,s}\|_{L^{(r)}_{\kappa,\sigma}}}\\
&=e^{-\kappa}k\left[
\frac{s}{(s+1)(s+3)+3(k-1)}
\left(\frac{s+2}{2(s+1)}\right)^{7+r}\right.\\
&\hspace{63pt}\left.+
e^{-8\sigma}\frac{s+2}{(s-1)(s+1)+3(k-1)}
\left(\frac{s}{2(s+1)}\right)^{7+r}\right].
\end{aligned}
\]
The plus branch has **no spin-exponential penalty**. Choose \(k=s^2\), so the plus denominator equals \(4s(s+1)\). Consequently,
\[
\boxed{\mathcal R_{s^2,s}^{(r)}
\ge e^{-\kappa}\frac{s^2}{4(s+1)}
\left(\frac{s+2}{2(s+1)}\right)^{7+r}
\ge e^{-\kappa}\frac{s}{2^{10+r}}\longrightarrow\infty.}
\]
Therefore for no fixed \(r\ge0\), \(\kappa>0,\sigma\ge0\) can the unrestricted history-aware physical operator satisfy a bilinear \(L^{(r)}\times L^{(r)}\to L^{(r)}\) bound with constant uniform in ambient strip length.

This is a **standalone** no-go based on exact Wilson-character fusion and original-link Casimir eigenvalues, not on the previously assumed Peter–Weyl *upper* estimate. It explains why the earlier one-extra-inner-spin-moment tame estimate may be sharp in qualitative grade loss, and does not contradict the fundamental-singleton \(s=1\) insertion theorem.

**Next objective:** abandon same-fixed-grade closure for the *entire* unrestricted history space; investigate a physically selected linked-cluster/cumulant subspace stable under reconstruction and nonlinearity, or a graded/renormalized recurrence with quantitatively summable moment losses. No interacting \(\lambda=1\) gap, volume-uniform vacuum or R4 continuum theorem follows.

## Reproducibility
The companion Python Fraction checker passed **8,965 exact rational assertions** across \(s=3,\ldots,500\) and output grades 0,1,2,3,5, plus fixed-volume diagnostics. The proof is symbolic and valid for all integers s>=3; the checker does not instantiate full exponentially large lattice Hilbert spaces or constitute independent peer review. Complete local proof and checker in the conversation ZIP.