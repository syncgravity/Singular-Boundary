# The Singular Boundary — Joint finite-spin trial families, fixed nonclass fraction, and the cap-selection obstruction

**Research continuation:** 2026-10-29; independent proof audit.  **Status:** proved finite-volume SU(2) variational constructions and their exact target marginals, plus a conditional cap-transfer criterion. **Not proved:** the actual eight-face deleted-vacuum cap bound, full-Hilbert Ritz isolation, Penrose-uniform signed-current estimate, physical mass gap or continuum reconstruction. No remote repository update was attempted.

## 1. Full physical SU(2) Wilson setting

Use a finite, simply connected open planar rhombus disk with one magnetically deleted target face `f` and seven retained faces `Q` in the connected eight-face fixture. Every original link has positive electric coefficient `a_e`; the seven retained magnetic couplings are `b c_q` with fixed `c_q>0`. The Hamiltonian on the **all-vertex Gauss-invariant** link-Haar Hilbert space is

\[
H_b=T+b\sum_{q\in Q}c_q(1-p_q),\quad
T=\sum_e a_e(-\Delta_e),\quad
p_q=\tfrac12\operatorname{Tr} W_q.
\]

The SU(2) convention is \((-\Delta)\chi_j=j(j+1)\chi_j\). Set \(A_q=\sum_{e\in\partial q}a_e\). An independent-face Haar coordinate system (a planar primal/dual spanning-tree gauge fixing) is legitimate for kinematic integrals. It **does not** make the interacting physical vacuum a product state.

## 2. Theorem JC-1: exactly normalized finite high-spin packet and its second deficit

For integer \(N\ge1\), define \(L=N+2\), \(\theta_N=\pi/L\), and the central SU(2) class-function packet

\[
\phi_N(W)=\sqrt{\frac8{3L}}\sum_{n=0}^N
\sin^2\!\left(\frac{(n+1)\pi}{L}\right)\chi_{n/2}(W).
\]

The finite character expansion is exactly normalized. Indeed, \(\sum_{k=1}^{L-1}\sin^4(k\pi/L)=3L/8\). The SU(2) fusion identity \(p\chi_{n/2}=(\chi_{(n+1)/2}+\chi_{(n-1)/2})/2\), with the negative-index character omitted, proves the **exact** deficit moments

\[
\boxed{\ \langle d\rangle_N=\frac23\sin^2\theta_N,\qquad
\langle d^2\rangle_N=\frac{2(2L-3)}{3L}\sin^4\theta_N,\quad d=1-p.\ }\tag{JC1}
\]

These identities hold in the full continuous SU(2) Hilbert space, without a group discretization. In particular

\[
\langle1-p^2\rangle_N=2\langle d\rangle_N-\langle d^2\rangle_N
\asymp N^{-2},\qquad
\frac{\langle d(1-p^2)\rangle_N}{\langle1-p^2\rangle_N}
\le\frac{2\langle d^2\rangle_N}{\langle1-p^2\rangle_N}=O(N^{-2}).\tag{JC2}
\]

The last estimate is why the **smoothed** packet is preferable to a sharp or sine-only spectral cutoff when a relative-color factor is normalized by its decreasing variance.

## 3. Theorem JC-2: simultaneous joint-spin trial with the correct square-root magnetic scale

For each retained face choose an integer \(N_q\asymp b^{1/4}\), and set

\[
\Phi_b(U)=\prod_{q\in Q}\phi_{N_q}(W_q(U)).
\]

This is normalized and gauge invariant. The electric Dirichlet cross terms between different face class functions have zero kinematic Haar expectation by conditional cancellation of the relative-color axes. Therefore the full Wilson **Rayleigh quotient** is exactly

\[
\boxed{\mathcal E_b(\Phi_b)
=\sum_{q\in Q}\left[
A_q\sum_{n=0}^{N_q}c_{q,n}^2\frac{n(n+2)}4
+b c_q\frac23\sin^2\!\left(\frac\pi{N_q+2}\right)
\right]=O(\sqrt b),}\tag{JC3}
\]

where \(c_{q,n}=\sqrt{8/[3(N_q+2)]}\sin^2[(n+1)\pi/(N_q+2)]\). Every original link belongs to at most two retained face boundaries, so the maximum original-link spin is \(O(b^{1/4})\). This state occupies high spin simultaneously across the retained plaquettes, unlike every independent single-plaquette-tower extension of the 433-state fundamental shell.

The target holonomy under \(|\Phi_b|^2\) is **exactly Haar**. The construction proves *energy-scale feasibility*; it does not prove the ground-state marginal is Haar.

## 4. Theorem JC-3: center-even cap suppression with only bounded additional energy

Fix an integer \(m\ge1\). Define the normalized target class factor

\[
s_m(W_f)=\frac{(1-p_f^2)^m}{\sqrt{Z_m}},\qquad
Z_m=\frac2\pi B\!\left(\frac12,2m+\frac32\right).
\]

It is invariant under target-center flux. The target-dependent state \(X_{b,m}=s_m(W_f)\Phi_b\) is normalized and has the **exact** additional kinetic energy

\[
\boxed{\mathcal E_b(X_{b,m})=\mathcal E_b(\Phi_b)+\frac{A_fm^2}{4m+1}.}\tag{JC4}
\]

There is no deleted-target magnetic penalty. Its target-angle marginal is \(Z_m^{-1}\sin^{4m}(u)\,(2/\pi)\sin^2u\,du\). For \(B_a=\{u\le a\}\),

\[
\boxed{\Pr_{X_{b,m}}(B_a)\sim
\frac{2}{\pi Z_m(4m+3)}a^{4m+3},\qquad
\frac{\Pr_{X_{b,m}}(B_a)}{\Pr_{\rm Haar}(B_a)}=O(a^{4m}).}\tag{JC5}
\]

With \(a_h=\arccos(1-h)\asymp\sqrt h\), the cap is \(O(h^{2m+3/2})\). For \(m=1\), explicitly \(Z_1=5/8\), \(\Pr(B_a)\sim16a^7/(35\pi)\), and \(\Pr(B_a)/\Pr_{\rm Haar}(B_a)\sim(24/35)a^4\).

Conversely, the normalized center-even target factor \(s_+(p)=2\sqrt2p^2\) has kinetic energy exactly \(A_f\), target density \(8p_f^4\) times Haar, and cap probability asymptotic to **eight times Haar**. Both families retain the same \(O(\sqrt b)\) leading energy scale while having opposite small-cap behavior.

## 5. Theorem JC-4: fixed **nonclass** norm fraction with the same energy scale

Take a retained face \(g\) sharing an edge with the target, use based SU(2) face holonomies with coherent orientation, and define

\[
D_{fg}=p_{\partial(f\cup g)}-p_fp_g,
\qquad R_{fg}=p_fD_{fg}.
\]

The relative-color quantity \(R_{fg}\) is gauge invariant, **target-center-even**, and conditionally mean zero given all individual face traces. With \(X_{b,m}=s_m\Phi_b\), the exact conditional color-axis covariance gives

\[
r_b^2:=\|R_{fg}X_{b,m}\|^2
=\frac13\,\frac{4m+3}{4(2m+2)(2m+3)}
\langle1-p_g^2\rangle_{N_g}>0.
\]

Define the normalized true nonclass vector \(Z_{b,m}=R_{fg}X_{b,m}/r_b\). Then \(Z_{b,m}\perp X_{b,m}\) and \(Z_{b,m}\) is orthogonal to the **entire** individual-face class-function space. For fixed nonzero real \(\epsilon\),

\[
\boxed{\Xi_{b,m,\epsilon}=
\frac{X_{b,m}+\epsilon Z_{b,m}}{\sqrt{1+\epsilon^2}}.}\tag{JC6}
\]

The relative-color norm fraction is **exactly** \(\epsilon^2/(1+\epsilon^2)\), independent of \(b\). In particular \(\epsilon=1\) gives 50% physical relative-color norm at every magnetic strength. This is stronger than inserting an unnormalized bounded color factor, whose relative-color norm generally vanishes as \(b\to\infty\).

**Energy estimate.** Since \(Z_{b,m}\) is a polynomial character product of bounded local degree times the packets, every original-link spin remains bounded above by \(J_b=N_{\max}+m+2=O(b^{1/4})\). Hence its complete electric energy is bounded by \(A_{\mathrm{tot}}J_b(J_b+1)=O(\sqrt b)\). The exact conditional color law also gives

\[
\langle d_q\rangle_{Z_{b,m}}=
\begin{cases}
\langle d_q\rangle_{N_q}, &q\ne g,\\
\frac{\langle d_g(1-p_g^2)\rangle_{N_g}}{\langle1-p_g^2\rangle_{N_g}}, &q=g,
\end{cases}
\]

and JC2 bounds each term by \(O(b^{-1/2})\). Consequently the complete magnetic energy of the normalized nonclass vector is also \(O(\sqrt b)\). Since \(H_b\ge0\), energy-form Cauchy yields

\[
\boxed{\langle\Xi_{b,m,\epsilon},H_b\Xi_{b,m,\epsilon}\rangle
\le\frac{(\sqrt{\mathcal E_b(X_{b,m})}+|\epsilon|\sqrt{\mathcal E_b(Z_{b,m})})^2}{1+\epsilon^2}
=O(\sqrt b).}\tag{JC7}
\]

This construction is *simultaneously high-spin, center-even, finite-support in Peter–Weyl degree, and genuinely nonclassical with nonvanishing color norm*.

Its **exact target marginal** is

\[
\boxed{\frac{d\nu_{\Xi}}{dU_f}=
|s_m(p_f)|^2
\frac{1+\epsilon^2\,p_f^2(1-p_f^2)/T_m}{1+\epsilon^2},
\quad T_m=\frac{4m+3}{4(2m+2)(2m+3)}.}\tag{JC8}
\]

The mixed class/color cross contribution vanishes after conditional color integration. Thus for \(\epsilon=1,m=1\), the small-cap ratio obeys

\[
\boxed{\frac{\Pr_{\Xi_{b,1,1}}(d_f\le h)}{\Pr_{\rm Haar}(d_f\le h)}
\sim\frac{48}{35}h^2\to0,}\tag{JC9}
\]

**uniformly in the retained magnetic coupling \(b\)**. Using the enhanced center factor \(s_+=2\sqrt2p^2\) in place of \(s_m\) and the corresponding normalized relative-color partner gives a second center-even, 50%-nonclass trial of energy \(O(\sqrt b)\) whose cap/Haar ratio tends to **4**. The two constructions make clear why leading energy-scale control, joint high-spin completeness and even a fixed fraction of relative-color norm **do not suffice by themselves** to determine the deleted-target cap of the *true* vacuum. Neither state is asserted to be a low-error approximation of that vacuum.

## 6. Certified Ritz-to-cap transfer: the missing quantitative obligation

There is a direct sufficient error criterion. For normalized exact ground state \(\Omega_b\) and a normalized Ritz trial \(\varphi_b\), with relative phase chosen to maximize overlap, let \(\epsilon_b=\|\Omega_b-\varphi_b\|\). For every measurable target cap \(B\), reverse triangle inequality gives

\[
\boxed{\Pr_{\Omega_b}(B)\ge
\bigl[\sqrt{\Pr_{\varphi_b}(B)}-\epsilon_b\bigr]_+^2.}\tag{JC10}
\]

If a **separate, valid full-Hilbert spectral-separation certificate** places \(e_0(\varphi_b)\) below every physical excited energy by at least \(d_b>0\), and its complete untruncated residual is \(r_b^{\rm Ritz}=\|(H_b-e_0)\varphi_b\|\), then

\[
\epsilon_b\le\sqrt2\,r_b^{\rm Ritz}/d_b.\tag{JC11}
\]

Thus, if the Ritz cap satisfies \(\Pr_{\varphi_b}(d_f\le h)\ge c h^{3/2}\), transferring a nonzero Haar-order cap coefficient requires, for example,

\[
\boxed{r_b^{\rm Ritz}/d_b=o(h^{3/4}).}\tag{JC12}
\]

This is a **conditional certification threshold**, not a computed bound for the eight-face Hamiltonian. The previously demonstrated large off-block Wilson channels and missing joint high-spin sectors show why verifying JC11 is a substantive task.

## 7. Relation to the signed radial-current alternative

For a strictly positive **trial** target factor \(s_{m,\varepsilon}(u)\propto\varepsilon+\sin^{2m}u\), the positive variation of its log radial amplitude over the northern hemisphere is exactly

\[\log\frac{1+\varepsilon}{\varepsilon}.\]

Setting \(\varepsilon=h^{m+1}\) yields a smooth, strictly positive marginal with cap mass \(O(h^{2m+3/2})\) but score-variation budget \(O(\log(1/h))=o(h^{-1/4})\). This is **consistent** with the earlier conditional signed-radial-current theorem: its \(o(h^{-1/4})\) gate is sufficient for the specified deletion comparison, **not** a claim of a uniform constant-times-Haar cap. These are trial marginal score calculations, **not** estimates of the unknown actual conditional score current of the interacting Penrose ground state.

## 8. Verification, evidence levels, next proof gate

The three executable deterministic checkers verify the Haar beta integrals, first and second magnetic-deficit moments for the finite packets, target Dirichlet energy, normalized nonclass color variance, asymptotic cap coefficients, fixed 50%-nonclass fraction, explicit finite coefficient energy upper estimates, and the algebra of the conditional Ritz cap transfer. The scripts use continuous SU(2) character identities and deterministic 1-D quadrature; they do not diagonalize the physical eight-face Hamiltonian.

**PROVED:** JC1–JC12 with their hypotheses, and a constructive counterexample to *inference from leading Rayleigh-energy scale plus representation completeness and color fraction alone*. **OPEN:** an independently certified full-Hilbert gap/residual small enough for JC12, or a direct one-sided true-vacuum radial-score/current estimate sufficient for the deleted-face cap and bulk magnetic-deletion comparison. The generic asymmetric Penrose bound, physical mass gap and continuum reconstruction remain open.
