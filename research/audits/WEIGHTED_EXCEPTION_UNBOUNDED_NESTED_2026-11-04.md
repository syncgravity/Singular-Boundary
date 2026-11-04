# Weighted exceptional-energy charging: unbounded nested original-link SU(2) histories

**2026-11-04 · conditional analytic theorem / independent geometric counting argument.** Finite open, original-link, Gauss-invariant SU(2) straight-square strips only. This is a new proof mechanism and changed constants for the graded local-first tame architecture already archived in \`R3_IR_LOCAL_FIRST_TAME_2026-11-03.md\`, **not** the first local-first tame theorem, a convergent physical vacuum, or a continuum Yang–Mills mass gap. Full independent checker, log, report, and SHA-256 manifest are in companion \`sb_weighted_nested_history_audit_2026-11-04.zip\`.

## Existing results not duplicated

Prior \`R3_IR_CROSSING_NESTED_DECOMPOSITION_2026-11-03.md\` controls crossing histories and demonstrates the failure of *bare positive overlap counts* for nested histories. \`R3_IR_NESTED_BOUNDED_INNER_2026-11-03.md\` imposes a maximum inner-history length M and spin s. \`R3_IR_NESTED_UNBOUNDED_SPIN_RADIUS_TRADE_2026-11-03.md\` permits unbounded histories but loses spin-analytic radius. The archived \`R3_IR_LOCAL_FIRST_TAME_2026-11-03.md\` claims a graded tame estimate at fixed radius using a different exact-length energy count. Here we independently remove the width restriction of the earlier Casimir argument using an **exponentially weighted exceptional-history Markov charge** and obtain an alternate conditional graded estimate.

## Inherited analytic inputs: not independently certified here

On an original-link ladder let \(K=-\sum_e a_e\sum_jX_{ej}^2\), \(0<a_0\le a_e\le a_*\), \(R=a_*/a_0\), \(C_0=24(1+R)\). With \(Q\) removing only the global Haar-constant mode and \(\mathcal B=K^{-1}Q\Gamma_K\), assume the archived **coefficientwise trace-expansion matrix Peter–Weyl** multiplication estimate, its local bound
\[
\|\mathcal B(f_I,g_J)\|_{P_\sigma}
\le C_0|E(I)\cap E(J)|\,\|f_I\|_{P_\sigma}\|g_J\|_{P_\sigma},
\]
and the coefficientwise original-link gradient bound, for outer spin sector \(\mathbf n\) and inner sector \(\mathbf m\) with \(s=\max_e m_e\):
\[
\|\Gamma_K(f_{\mathbf n},g_{\mathbf m})\|_{P_\sigma}
\le(3a_*/4)s\sum_{e\in E(J)}n_e\|f_{\mathbf n}\|_{P_\sigma}\|g_{\mathbf m}\|_{P_\sigma}.
\]
The original-link inverse is spin-sector diagonal: all outer labels outside E(J) survive fusion, so output electric energy is at least \(a_0(q-q_J)\), where \(q=\sum_en_e(n_e+2)/4\), \(q_J=\sum_{e\in E(J)}n_e(n_e+2)/4\). These source-theorem operator hypotheses remain a separate certification obligation. Spin-zero outer coefficients have zero gradient.

For any integer \(r\ge0\), \(\kappa>0,\sigma\ge0\), the local-first norm is
\[
\|F\|_{L^{(r)}}=\sup_x\sum_{I\ni x}e^{\kappa|I|}
\sum_{\mathbf n} d_{\mathbf n}e^{\sigma|\mathbf n|}
(1+\max_e n_e)^r\|A_{I,\mathbf n}\|_{S_1}.
\]
No upper bound is placed on history widths or spin labels.

## Exact single-edge weighted incidence lemma

For each outer face interval I, every original link touches at most two faces. If \(J\subseteq I\) runs over **all** nested nonempty intervals and \(W_J\ge0\), write \(G_*=\sup_x\sum_{J\ni x}W_J\). At each original edge \(e\),
\[
\sum_{J\subseteq I:e\in E(J)} e^{-\kappa|J|/2}W_J
\le 2e^{-\kappa/2}G_* .\tag{1}
\]
The proof assigns each J to one of the at most two incident faces and uses \(|J|\ge1\). For any nonnegative edge-energy charges \(q_e\) of total \(q=\sum q_e>0\), put \(q_J=\sum_{e\in E(J)}q_e\) and \(\mathrm{Exc}=\{J:q_J>q/2\}\). Sum (1) against q_e, apply the weighted Markov inequality, and obtain
\[
\sum_{J\in\mathrm{Exc}}e^{-\kappa|J|/2}W_J
\le4e^{-\kappa/2}G_* .\tag{2}
\]
Since \(|E(J)|=3|J|+1\), define
\[
H_\kappa=\sup_{m\ge1}(3m+1)e^{-\kappa m/2}
\le1+\frac6{e\kappa}.
\]
Then **all exceptional intervals, of unlimited lengths**, obey
\[
\boxed{\sum_{J\in\mathrm{Exc}}(3|J|+1)e^{-\kappa|J|}W_J
\le4e^{-\kappa/2}H_\kappa G_* .}\tag{3}
\]
Crucially (3) counts **weighted energy concentration**, not the number of exceptional intervals in a history of fixed length. No M-dependent factor survives.

## One-sided nested graded tame estimate (conditional)

Let \(\mathcal B_{\mathrm{nest}}^{G\subseteq F}\) sum ordered nested pairs with inner J⊆outer I and retain the entire physical output at history I. For every integer \(r\ge0\),
\[
\boxed{\begin{aligned}
\|\mathcal B_{\mathrm{nest}}^{G\subseteq F}(F,G)\|_{L^{(r)}}
\le {}&4R e^{-\kappa}\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}\\
&+4C_0e^{-\kappa/2}H_\kappa\,
  \|F\|_{L^{(r)}}\|G\|_{L^{(r)}}.
\end{aligned}}\tag{4}
\]

**Good intervals** \(q_J\le q/2\): surviving outer-link spins give output energy ≥a0q/2. Combining the inherited differentiated coefficientwise PW estimate and inverse costs at most \((3Rs/2q)\sum_{e\in E(J)}n_e\) in normalized projective norm. The CG output-moment inequality
\((1+\max_e \ell_e)^r\le(1+\max_e n_e)^r(1+s)^r\)
and the factor s are absorbed by the *inner* \(L^{(r+1)}\) norm. Summing J with full discount \(e^{-\kappa|J|}\) via the two-face incidence bound and using \(\sum_e n_e\le4q/3\) gives exactly \(4Re^{-\kappa}\).

**Exceptional intervals** \(q_J>q/2\): apply the inherited local PW bilinear estimate with \(|E(I)\cap E(J)|=3|J|+1\). Keep the same output moment factor, absorbed by the inner \(L^{(r)}\) norm, and sum using (3). This gives the second term of (4). In both arguments the coefficientwise spin sum belongs **inside** the chosen outer anchor sum. No output-spin-sector count outside the supremum is allowed. If q=0, the outer derivative vanishes. Density extends (4) to the corresponding completion under the inherited operator hypotheses.

At \(\kappa=\log4\), \(H_\kappa=2\) exactly, since \((3m+1)/2^m\le2\). The two coefficients become \(R\) and \(4C_0\).

## Safe all-history and formal-series corollaries (conditional)

The earlier crossing bound is
\(C_{\mathrm{cross}}=4C_0[(1-t)^{-1}+3t(1-t)^{-2}]\), \(t=e^{-\kappa}\).
Applying (4) in both nested orientations (double-counting equal histories is safe) gives
\[
\|\mathcal B_{\mathrm{hist}}(F,G)\|_{L^{(r)}}\le
C_{\mathrm{same}}\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}
+C_{\mathrm{mom}}\big(
\|F\|_{L^{(r)}}\|G\|_{L^{(r+1)}}+
\|F\|_{L^{(r+1)}}\|G\|_{L^{(r)}}\big)
\tag{5}
\]
with \(C_{\mathrm{same}}=C_{\mathrm{cross}}+8C_0e^{-\kappa/2}H_\kappa\) and \(C_{\mathrm{mom}}=4Re^{-\kappa}\).

If, additionally, the archived source-order spin cap and a volume-independent first-order source norm \(M\) hold, (5) yields formal coefficient bound
\(a_n\le M^nD^{n-1}(n-1)!\) with \(D=3C_{\mathrm{same}}+12C_{\mathrm{mom}}\), and a **conditional** local Borel disk \(|\xi|<1/(MD)\). This neither proves Borel summability nor an interacting physical gap. These implications were already of the same type as the Observatory's previous conditional Gevrey/Borel argument; this audit changes the route and constants, not the proof status.

## Independent checks and next decisive gate

\`verify_weighted_exception.py\` and its SHA-256 manifest are in \`sb_weighted_nested_history_audit_2026-11-04.zip\`. **36,600 exact-rational tests** cover all nested subintervals in strips up to 28 faces, nonuniform nonnegative original-link Casimir charges, arbitrary positive inner interval weights, incidence, Markov energy charging, and the exact \(\kappa=\log4\) exponential envelope. These are checks of the new combinatorics **only**. The all-\(\kappa\) statement is derived analytically above and remains conditional on the listed PW operator inputs.

**Next:** independently certify the original-link **coefficientwise** matrix-PW product/local bilinear hypotheses and test whether the formal source-generated recurrence has a convergent or Borel-summable reconstruction. All 3D Penrose/refinement, OS reconstruction and continuum SU(2) mass-gap obligations remain open.