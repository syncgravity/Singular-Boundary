# PF-I16 — Exact forest-Haar theorem and weak-coupling cycle-cut information

**Research 2026-11-09.** Source: original authenticated PF-I11/PF-I15 coupled-Z^5 accepted edge graph and genuine four-edge rhombi; PF-I16 one-link conditional-information work. This is a finite-graph theorem, not a certified physical Yang–Mills gap. Complete proof, executable checker, log and SHA-256 hashes: Library /The Singular Boundary/Proof Audits/PF_I16_FOREST_CYCLE_INFORMATION_2026_11_09.zip.

## A. Exact forest-Haar theorem — all couplings

Let \(\nu\) be **any** probability measure on \(SU(2)^E\) invariant under vertex gauge transformations \(U_{xy}\mapsto g_xU_{xy}g_y^{-1}\). For every set of edges \(S\) that is a forest,
\[
\boxed{(\pi_S)_*\nu=\bigotimes_{e\in S}dU_e.}
\]
Proof: On every tree component choose a root, then successively choose vertex gauge transformations that send all selected holonomies to identity. Acyclicity gives consistency; hence the vertex gauge group acts transitively on \(SU(2)^S\). The marginal is invariant and product Haar is the unique invariant probability on this compact homogeneous space. QED. No weak-coupling or vacuum-factorization assumption.

The source graph has basis-shift edges changing height by one, is simple and bipartite, and has four-edge genuine rhombi. Therefore any 1, 2 or 3 distinct original edges form a forest and have **exact independent Haar** joint distribution at arbitrary interacting coupling. Forests with more edges share this property. These open-link marginals are gauge-coordinate diagnostics, not physical open-link observables; the gauge-invariant correlations reside on cycles.

## B. Exact second-order cycle-cut information coefficient — finite graph

For fixed finite accepted graph, take an auxiliary finite Hamiltonian
\[
H_t=K+t\sum_fc_f(1-p_f),\quad K=\sum_ea_eC_e,\quad
p_f=\tfrac12\operatorname{Tr}U_{\partial f},\quad a_e>0.
\]
On each genuine simple four-edge rhombus, \(Kp_f=\lambda_fp_f\) with \(\lambda_f=\frac34\sum_{e\in\partial f}a_e\). The simple isolated constant electric vacuum and bounded analytic perturbation yield
\[
\Omega_t=1+t\sum_f(c_f/\lambda_f)p_f+O_G(t^2)
\]
in the fixed finite system.

For any edge bipartition \(E=S\sqcup S^c\), let \(F_{\rm cross}(S)\) be exactly the rhombi with at least one edge on each side, and define coordinate mutual information \(I_t(S:S^c)=D_{\rm KL}(\nu_t\Vert\nu_{t,S}\otimes\nu_{t,S^c})\). Then
\[
\boxed{I_t(S:S^c)=\frac{t^2}{2}\sum_{f\in F_{\rm cross}(S)}
(c_f/\lambda_f)^2+O_{G,S}(t^3).}
\]
Proof: The full vacuum-density first derivative is \(2\sum_f(c_f/\lambda_f)p_f\). Haar integration annihilates any face containing an integrated edge, so subtracting the product-marginal first derivative leaves precisely the crossing faces. The KL second variation at Haar is half the squared \(L^2\) norm of this difference. Distinct simple source rhombus traces are Haar-orthogonal, by integrating an edge in their symmetric difference; \(\int p_f^2d\mu=1/4\). Therefore the coefficient is \(\frac12\sum_{f\in F_{\rm cross}}(c_f/\lambda_f)^2\). QED.

For a single edge \(e\):
\[
\lim_{t\downarrow0}\frac{I_t(U_e;U_{-e})}{t^2}
=\tfrac12\sum_{f:e\in\partial f}(c_f/\lambda_f)^2
\le\frac{4c_0^2}{9a_0^2}
\]
when \(a_e\ge a_0>0\), \(c_f\le c_0\), and each source edge belongs to at most eight elementary rhombi. The coefficient is volume-independent; the error is **not** proved volume-uniform.

## C. Reproducibility and precise open gate

The local two-adjacent-rhombus seven-link checker verifies forest subsets of size at most three and cut coefficients \(1/9\) (shared edge; two rhombi) and \(1/18\) (outer edge; one rhombus) for unit coefficients. Independent one-rhombus SU(2) Jacobi diagonalization (36 characters) and Haar Gaussian quadrature (600 nodes) show \(I_b/b^2\to1/18\), with six verified couplings. These computations do not replay every original source crop and do not replace the all-graph proof.

Neither the exact forest theorem nor the finite-graph weak-coupling information coefficient proves collective Wilson-loop correlation decay, conditional Poincaré bounds, approximate tensorization, a volume-uniform interacting gap, source-selected physical time/kinetic scale, continuum reconstruction, or the 4D Yang–Mills mass gap. In particular, no uniform-in-volume perturbative remainder or radius is established. The next obstruction is a controlled all-order connected-cycle expansion for the true interacting vacuum on the genuine accepted geometry.

No historic source, dissertation, simulation archive, canonical claim ledger or Observatory gate was modified.