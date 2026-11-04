# R3-IR — Source multigrading and linked-history reachability
Research date 2026-11-03. **Exact necessary selection rules for the generated formal SU(2) vacuum score on finite original-link straight square strips; not convergence or mass gap.** Complete expanded proof and 313,864-check executable verifier in conversation archive R3_IR_SOURCE_MULTIGRADING_LINKED_HISTORY_2026-11-03.zip.

Let the original-link Gauss-invariant electric operator K have a positive free gap on Haar-centered functions, Q remove the constant, and B=K^{-1}Q Gamma_K. Assign independent formal source variables z_p to elementary magnetic sources V_p=-chi_1(U_boundary p)/2. The formal logarithmic vacuum score is uniquely determined by total-order recursion:
\[
S(\mathbf z)=\sum_pz_p(-K^{-1}QV_p)+B(S(\mathbf z),S(\mathbf z)).
\]
Every source leaf has singleton history, and nonzero interactions union their histories. A Γ_K interaction of two inputs with disjoint active original-link supports vanishes.

## Multigrading theorem
For every nonzero coefficient of z^m on connected history I, with output original-link SU(2) spin label n_e:
\[
\boxed{I=\{p:m_p>0\},\quad I\text{ connected},\quad |I|\le\sum_pm_p;}
\]
\[
\boxed{n_e\equiv\sum_{p:e\in\partial p}m_p\ (\mathrm{mod}\ 2),\quad
0\le n_e\le\sum_{p:e\in\partial p}m_p.}
\]
Consequently max_e n_e<=sum m_p and sum_e n_e<=4sum m_p. The coefficient is represented by binary source trees with exactly sum m_p fundamental leaves, connected by shared original-link derivatives at each internal vertex. This holds even when physical output spin support becomes disconnected.

Proof: induction on total source order. Each fundamental source has label 1 on its four boundary links. K^{-1}Q and original-link derivatives preserve spin sectors. SU(2) CG outputs satisfy ell<=n+m and ell≡n+m modulo 2, and no Γ interaction occurs without common dependent links. Independent link-center flips U_e→−U_e give an alternative direct parity proof. No convergence assumption is used.

## Strengthened reachability test on the prior fixed-grade no-go family
On N=2k−1 faces, let I=[1,N] and F_k=product of fundamental Wilson traces on odd faces, whose occupied spin support is disconnected. On the top boundary link of each odd face the desired spin is 1; on each even face it is 0. Since every face must have positive source count to belong to history I, parity implies m_odd>=1 odd, m_even>=2 even, hence
\[
\boxed{\sum_pm_p\ge k+2(k-1)=3k-2.}
\]
For the previous scaling k=s², a generated score coefficient of this form must have order >=3s²−2; the singleton spin-s input needs >=s source leaves; their combined quadratic operation cannot occur before order 3s²+s−2. **These are necessary lower bounds, not proof of actual nonzero coefficients or upper norm bounds.** The unrestricted bilinear no-go remains valid on the whole history Banach space.

If the link graph genuinely decouples into two systems, the positive ground state factorizes and its log score is additive, forbidding mixed cumulants. This cannot be invoked for alternate faces inside the full coupled strip. Source-order weights alone do not fix operator boundedness, since q^(a+b)/(q^a q^b)=1.

Next: compute exact original-link three-face coefficients in independent face couplings, in particular the first allowed disconnected two-loop output channel, and develop a coefficient-sensitive connected-tree majorant. Full interacting λ=1 gap, volume-uniform vacuum, 3D extension, and continuum R4 mass gap remain open.

Exact verifier: 313,864 parity, CG, source-order and incidence tests, not a proof of all-order analytic convergence.