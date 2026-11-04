# P2: certified physical-response trace-norm brackets and finite-window Laplace errors

**2026-11-04 — corrected original-link finite open SU(2) straight-strip model, one face-coordinate Peter–Weyl projective norm.** Expanded derivation, full previous physical Fourier engine, independent dense-response/Neumann and exact-rational Borel verifiers, logs, SHA-256 manifest and integrity-tested ZIP: conversation artifact \`p2_certified_bounds_2026-11-04.zip\`. **No physical same-grade high-spin divergence or bound, global Borel summability, interacting infinite-volume state or continuum Yang–Mills gap is proved.**

## A. Certified all-width trace-norm brackets for the physical high-spin response

Let N≥2 be even and m≥3. Let F_N be the **Gauss-invariant, balanced SU(2)-twirled** degree-one outer intertwiner with trace-nuclear coefficient norm 1 and G_{N,m}=Σ_{j=1}^N[{j}]χ_m(U_j) the separately Gauss-invariant singleton inputs. The output channels (j,l) with l=m−1,m+1 are disjoint for different insertion sites and the full corrected original-link K preserves each multidegree. Denote the normalized first or higher max-spin moment response *without* its factor e^(−κ) by R_{N,m}^{(r)}, r≥0.

For an output sector c=(1,…,1,l,1,…,1), write e_i=c_i(c_i+2), D_c=Σ_i e_i and
\[
\alpha_c=\frac1{2D_c}\sum_{i=1}^{N-1}\sqrt{e_i e_{i+1}}\le\tfrac12.
\]
The actual original-link face Fourier matrix superoperator is K_c=D_c Id+H_c, with \(\|H_c\|_{S_1\to S_1}\le D_c\alpha_c\). Its q-order Neumann approximation \(R_{c,[q]}(Y)=D_c^{-1}\sum_{p=0}^q(-H_c/D_c)^pY\) satisfies
\[
\boxed{\|K_c^{-1}Y-R_{c,[q]}(Y)\|_1
\le\frac{\alpha_c^{q+1}}{D_c(1-\alpha_c)}\|Y\|_1.}\tag{1}
\]
Taking A_{N,m}=max_{j,l} α_c and D_min=3N+m²−4, the independently derived physical source bound \((9/2)m\) and the same-coordinate CG/Schatten/moment inequalities imply **for the complete summed gauge-invariant response**
\[
\boxed{|R_{N,m}^{(r)}-R_{N,m,[q]}^{(r)}|
\le \frac{9Nm}{2D_{\min}}\frac{A_{N,m}^{q+1}}{1-A_{N,m}}
\le\frac{9Nm}{3N+m^2-4}2^{-(q+1)}.}\tag{2}
\]
R_[q] means **sum of the nuclear norms of each approximate output sector**, not the norm of a sum of incompatible sectors. Thus R_[q] ± RHS supplies a certified two-sided bracket on the **unknown true response** once R_[q] is computed.

On N=2ceil(m²/2) with m→∞, the largest alpha (an interior insertion) tends to **3/8**. Derivation: ordinary (1,1) edges contribute 3/2 per edge to the numerator sum defining alpha; two adjacent exceptional edges contribute O(m), while D_c∼4m². Endpoint insertions are no worse. Hence constant q is sufficient to bound truncation uncertainty as a fixed fraction of the *possible* O(m) response scale. It does not compute the nuclear norm of R_[q] in polynomial time and does not establish any physical high-spin asymptotic.

Full physical matrix tests N=2,4 and m=3,4, depth q=0,1,2,4,8, all pass (1)-(2); exact output inverses/residuals and all gauge projections are retained in the independent engine. See complete archive for observed numbers.

**Next decisive target:** construct trace-norm dual certificates or a true transfer/recoupling contraction for R_[q] at N∼m². A Schatten dual test must be a legitimate unit-operator-norm output observable; a non-Gauss-invariant extremal input does not suffice.

## B. Explicit finite-history Borel/Laplace approximation certificates

For a fixed face window I of L faces, keep all connected subhistory labels and let \(C_L=2+6L\), \(M_L=(4/3)Le^\sigma\), \(B_L=4C_LM_L=(16/3)e^\sigma L(2+6L)\). The already proved same-coordinate pairwise operator estimate and the formal fundamental-source recursion give
\[
\|S_{I,n}\|\le\mathrm{Cat}_{n-1} C_L^{n-1}M_L^n\le M_L B_L^{n-1}.
\]
Therefore for any \(\xi\in\mathbb C\), the Borel transform on this *fixed window* is entire with certified order-p remainder
\[
\boxed{\left\|\widehat S_I(\xi)-\sum_{n=1}^p S_{I,n}\frac{\xi^n}{n!}\right\|
\le \frac{e^{B_L|\xi|}-\sum_{n=0}^p(B_L|\xi|)^n/n!}{4C_L}.}\tag{3}
\]
For real \(0\le\lambda<1/B_L\), finite-window Borel–Laplace reconstruction is absolutely valid; the order-p score truncation has certified error
\[
\boxed{\left\|S_I(\lambda)-\sum_{n=1}^p S_{I,n}\lambda^n\right\|
\le \frac{M_L\lambda(B_L\lambda)^p}{1-B_L\lambda}.}\tag{4}
\]
At half-radius this is ≤2M_Lλ·2^(−p). The local scores agree on common history coefficients and **common** small-coupling domains. Since 1/B_L∼[32e^\sigma L²]^(−1), the estimate does **not** give a volume-uniform positive-coupling Borel sum. The true infinite-row Borel Volterra map is already known to be Fréchet-entire **only in the weaker product-local topology**. The new bounds are quantitative **window-reconstruction** tools, not a new global continuation proof.

## C. Observatory version correction

The Observatory HTML banner remained at \`v0.2\` although its footer already said \`v2.3\`. Set both to **v2.4** and add a matching current-version entry in README, while preserving the separate scientific-status banner (4D continuum mass gap OPEN), manual-only Pages workflow, and private GitHub state. Add a version-sync checker to prevent the static-header regression.

## Reproducibility

Companion exact-archive checker \`verify_adaptive_brackets.py\` builds the real corrected original-link SU(2) Fourier response and solves the full matrix inverse; tests 4 physical (N,m) cases at five Neumann depths, plus alpha scaling through m=512 without dense matrices. \`verify_window_borel_tail.py\` checks **10,000 rational Catalan coefficients and 400 exact rational Laplace-tail bounds** for 100 finite-window sizes. Independent execution logs, per-file SHA-256 hashes and ZIP integrity passed. The analytical proofs provide the all-N/all-m statements; finite tests check implementations.

**Remaining:** physical N∼m² Schatten response scale; global anchored-norm Borel ray growth; positive interacting lattice and continuum reconstruction/OS positivity/mass gap. None is established here.