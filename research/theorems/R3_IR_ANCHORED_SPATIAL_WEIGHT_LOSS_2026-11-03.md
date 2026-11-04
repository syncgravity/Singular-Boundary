# R3-IR — All-history anchored fusion with spatial-weight loss

**2026-11-03 research audit.** This is a conditional finite-open-straight-strip SU(2) theorem for the corrected original-link free-electric Poisson fusion. It uses the previously reported same-spin-radius projective Fourier estimate. **Not** fixed-history-weight nonlinear closure, physical interacting gap, or continuum Yang–Mills proof. Expanded proof/checker/log/hash archive: R3_IR_ANCHORED_SPATIAL_WEIGHT_LOSS_2026-11-03.zip (conversation).

## Input estimate and anchored histories

Let \(\mathcal B=K^{-1}Q\Gamma_K\). For coefficients on original-link supports of face intervals I,J, use the prior matrix Peter–Weyl inequality at the **same** spin radius \(\sigma\ge0\):
\[
\|\mathcal B(f_I,g_J)\|_{P_\sigma}\le C_0|E(I)\cap E(J)|\|f_I\|_{P_\sigma}\|g_J\|_{P_\sigma},
\quad C_0=24(1+a_*/a_0).
\]
The history-aware operation labels each interacting pair by its connected union I∪J, preserving all physical output channels. Define
\[
\|F\|_{\mathrm{anch},\kappa,\sigma}
=\sup_x\sum_{I\ni x}e^{\kappa|I|}\|f_I\|_{P_\sigma}.
\]

## All-history theorem with spatial weight loss

For \(\kappa_{\rm in}>\kappa_{\rm out}\ge0\), \(\delta=\kappa_{\rm in}-\kappa_{\rm out}>0\),
\[
\boxed{\|\mathcal B_{\rm hist}(F,G)\|_{\mathrm{anch},\kappa_{\rm out},\sigma}
\le\frac{96C_0}{e^2\delta^2}
\|F\|_{\mathrm{anch},\kappa_{\rm in},\sigma}
\|G\|_{\mathrm{anch},\kappa_{\rm in},\sigma}.}
\]
The constant is independent of strip size, spin labels and connected-history widths.

**Proof:** For any output anchor x∈I∪J, treat x∈I and x∈J symmetrically. If x∈I and original-link supports overlap, some y∈I and z∈J satisfy |y−z|≤1. Thus
\[
\sum_{J:E(I)\cap E(J)\ne\varnothing}e^{\kappa_{\rm in}|J|}\|g_J\|_{P_\sigma}
\le3|I|\|G\|_{\rm anch,\kappa_{\rm in},\sigma}.
\]
Also \(|E(I)\cap E(J)|\le|E(I)|\le4|I|\). Since \(\kappa_{\rm out}\ge0\) and |I∪J|≤|I|+|J|,
\[
e^{\kappa_{\rm out}|I\cup J|-\kappa_{\rm in}(|I|+|J|)}
\le e^{-\delta|I|}.
\]
The x∈I contribution is ≤12 C0 sup_{\ell≥1}(\ell²e^{-\delta\ell}) times the product of input anchored norms, and the symmetric x∈J part doubles it. Use \(\sup_{\ell≥1}\ell²e^{-\delta\ell}\le4/(e²\delta²)\). This gives 96 C0/(e²δ²).

## Consequences

This is **arbitrary two-history** anchored control, but consumes spatial-history exponent. The earlier Casimir split gave same-exponent control for one fundamental singleton insertion only. The exact nested-loop low-energy coefficient \((2N-1)/8\) rules out *unweighted* Haar-L² bilinear closure but does not disprove strong projective anchored closure at positive history weight. Repeated \(\kappa\)-loss cannot automatically close an infinite nonlinear recurrence. The decisive next problem is a same-\(\kappa\) physical estimate or a renormalized recurrence with genuinely summable losses. Interacting \(\lambda=1\), three-dimensional spatial geometry, nontrivial R4 Yang–Mills and physical continuum mass gap remain open.

**Verification:** 850,986 finite geometry and scalar assertions passed, not a machine proof of the operator estimate. Full code and report in the local archive.