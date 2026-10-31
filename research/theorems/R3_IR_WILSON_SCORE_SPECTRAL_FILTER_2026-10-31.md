# R3-IR — Gap-free spectral filtering of the Wilson link-score response

**2026-10-31. Exact finite-volume consequence of the previously proved local Wilson f-sum (LR-2).** Not a uniform current theorem.

On the full original-link space let \(A=H_f^- - E_0\ge 0\), let \(w_{e,a}=X_{e,a}\Omega_f^-\), and let \(P_{\ge\delta}=1_{[\delta,\infty)}(A)\). The ground state is nondegenerate and \(w_{e,a}\perp\Omega\). The archived LR-2 theorem gives
\[
\sum_a\|A^{1/2}w_{e,a}\|^2=\frac38\sum_{g\ne f:e\in\partial g}b_g\,\mathbb E_\nu p_g\le B_e^*:=\frac38\sum_{g\ne f:e\in\partial g}b_g.
\]
For every \(\delta,t>0\), functional calculus proves the **exact gap-free estimates**
\[
\boxed{\sum_a\|P_{\ge\delta}w_{e,a}\|^2\le B_e^*/\delta},\qquad
\boxed{\sum_a\|(I-e^{-tA})w_{e,a}\|^2\le tB_e^*}.
\]
The first follows from \(1_{[\delta,\infty)}(\lambda)\le\lambda/\delta\), the second from \((1-e^{-t\lambda})^2\le t\lambda\) for \(\lambda\ge0\). More generally, a spectral multiplier \(m\) satisfying \(|m(0)|=0\), \(|m(\lambda)|^2\le C\lambda\) obeys \(\sum_a\|m(A)w_{e,a}\|^2\le CB_e^*\).

At the physical candidate strong-coupling scaling \(b_g\sim h^{-2}\), \(B_e^*=O(h^{-2})\). A high-energy threshold \(\delta\gg h^{-2}\) gives a vanishing high-energy norm; or \(t=o(h^2)\) yields a small semigroup change. Neither controls the low-energy sector \(0<\lambda<\delta\). For the abstract spectral triple \(A_\epsilon=\mathrm{diag}(0,\epsilon,1)\), \(w_\epsilon=\epsilon^{-1/2}e_2\), one has \(\|A_\epsilon^{1/2}w_\epsilon\|^2=1\) while \(\|w_\epsilon\|^2=\epsilon^{-1}\to\infty\). This demonstrates the missing inverse-moment information in general, **not** a Wilson-vacuum counterexample. Projection to the rare target center additionally needs a conditional density lower estimate or a direct one-sided current comparison.

The exact spectral bounds use the full Hilbert space, including non-gauge-invariant link derivative sectors. The numerical verifier uses randomized positive diagonal spectral matrices only, not an actual M55 Hamiltonian. The open obligations remain the low-energy Wilson response/collar control, \(\sup_f\mathfrak T_{f,h}=o(h^{-1/4})\), connected covariance and continuum mass gap.