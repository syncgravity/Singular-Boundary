**You:**

Please continue the PF-I16 objective.

* * *

**ChatGPT:**

# The Singular Boundary — PF-I16 continuation

The active objective remains the source-volume-uniform connected-cycle estimate for the authentic five-direction Penrose–Fibonacci accepted-rhombus complex. The task is to control the full interacting SU(2) vacuum, including repeated fusion through shared original links—not merely to bound a fixed finite-support coefficient.

One important refinement from the recovered records: the complete colored incidence-graph audit now certifies all 18,900 connected four-face supports at $N_{\rm grid}=7$ as members of seven exact isomorphism classes. That removes the earlier census-classification caveat. It does not, by itself, prove an all-orders activity bound or uniform mixing.

PF_I16_FOUR_FACE_EXACT_ISOMORPHISM_AND_CAUCHY_GATE_2026_11_09.md

I’m treating the desired conclusion as a theorem to be earned, not an assumption: finite-support analyticity, exact low-order coefficients, and a combinatorial count of connected supports must be joined by a genuinely volume-uniform estimate on the interacting amplitudes.

## A structural issue to resolve before the all-orders estimate

The recovered source records contain a potentially consequential incidence discrepancy:

* The four-face cluster-count argument uses at most two accepted faces per original link, giving face-overlap degree at most four.
* The forest/cycle-cut report separately records an original-link rhombus-incidence bound $d_e\le 8$.

Those are not interchangeable. If the correct maximum is eight, the overlap degree bound is at most $4(8-1)=28$, not four. The connected-support count would then use $28^{2(k-1)}=784^{k-1}$, rather than $16^{k-1}$. I will not carry the sharper constant into a theorem until the source-level incidence is reconciled.

PF_I16_FOREST_HAAR_AND_CYCLE_CUT_INFORMATION_2026_11_09.md

PF_I16_FOUR_FACE_EXACT_ISOMORPHISM_AND_CAUCHY_GATE_2026_11_09.md

## 1. Reconciled incidence bound

The apparent discrepancy is now resolved:

* The elementary five-direction geometry gives a universal bound of eight candidate rhombi per original link.
* The eight recorded finite source crops show a stronger result: no original link has more than two accepted-face incidences. This is a verified finite-crop observation, not yet a theorem for every source region or refinement.
    
    PF_I16_CONDITIONAL_SCORE_INFORMATION_AND_MIXING_GATE.md

For the all-source-volume argument, I therefore use the conservative bound. A face has four links, and each link can be shared with at most seven other faces. Thus the face-overlap graph has degree at most 28.

The corrected rooted connected-support count is

$$\boxed{ \#\{S\ni f:|S|=k,\ S\text{ connected}\} \le 28^{2(k-1)}=784^{k-1}. }$$

The previous $16^{k-1}$ count remains valid for the eight recorded crops, and for any larger family where the two-face incidence property is independently proved. It is not yet the safe universal constant.

Consequently, if the quantum activity theorem eventually gives

$$|\zeta_G(S;\mathbf b)|\le A q^{|S|},$$

the universal combinatorial sum converges whenever

$$\boxed{q<\frac1{784}}, \qquad \sum_{S\ni f}|\zeta_G(S;\mathbf b)| \le \frac{Aq}{1-784q}.$$

This is a conditional implication, not an activity estimate.

## 2. New exact reduction: dress each face before treating shared-link interactions

The more substantial development is an exact finite-graph operator identity. It gives a way to absorb repeated insertions on an individual rhombus before expanding the interactions between rhombi.

Write the centered auxiliary Hamiltonian as

$$H=K-\sum_f b_fp_f,\qquad K=\sum_e a_eC_e,\qquad p_f=\tfrac12\operatorname{Tr}U_f.$$

Let $d_e$ be the number of accepted faces incident to link $e$. Allocate the electric coefficient of each link among its incident faces:

$$K_f=\sum_{e\in\partial f}\frac{a_e}{d_e}C_e, \qquad A_f=\sum_{e\in\partial f}\frac{a_e}{d_e}.$$

Let $\psi_f>0$ be the exact isolated-face ground state of $K_f-b_fp_f$, with energy $E_f$, and define

$$s_f=\log\psi_f,\qquad \Phi=\sum_f s_f.$$

For a shared link define $v_{fe}=\nabla_es_f$ and

$$R_e= a_e\left|\sum_{f:e\in\partial f}v_{fe}\right|^2 -\frac{a_e}{d_e}\sum_{f:e\in\partial f}|v_{fe}|^2.$$

Summing the isolated-face ground-state equations gives the exact identity

$$\boxed{ e^{-\Phi}He^\Phi = L_\Phi+\sum_fE_f-\sum_eR_e, \qquad L_\Phi=K-2\Gamma_K(\Phi,\cdot). }$$

Here $L_\Phi$ is nonnegative and symmetric in the weighted measure $e^{2\Phi}d\mu$. Multiplication by $e^\Phi$ implements a unitary equivalence between that weighted Hilbert space and the original one.

The important feature is:

$$\boxed{d_e=1\quad\Longrightarrow\quad R_e=0.}$$

The residual is supported only on links shared by multiple accepted faces. The repeated interactions internal to one face have been resummed into its exact isolated-face dressing.

This is an exact algebraic reduction, not a perturbative approximation.

## 3. Quantitative locality of the residual

Using the universal incidence bound $d_e\le8$, each residual $R_e$ depends on at most

$$1+3d_e\le25$$

original links.

Define

$$\ell_f=\max_{e\in\partial f}\|\nabla_es_f\|_\infty.$$

Then

$$|R_e| \le a_e(d_e^2+1) \max_{f:e\in\partial f}\ell_f^2.$$

If we establish the isolated-face derivative estimate

$$\ell_f\le C_1\frac{b_f}{A_f},$$

then $A_f\ge a_e/8$ for every face incident to $e$. Therefore

$$\boxed{ \|R_e\|_\infty \le 4160\,C_1^2\frac{b_0^2}{a_0}. }$$

The constant is conservative but independent of source volume.

There is also a crude overlap bound for the residual interactions: at most 800 link-indexed residual terms can have support intersecting any given residual support. The exact constant can likely be improved, but bounded support and bounded overlap are already established under the source incidence assumptions.

Exact finite-graph identity

The dressing identity, residual support count, and conditional norm arithmetic have been derived and checked.

Analytic gate remains open

The derivative estimate and the stability of the extensive residual sum are not yet proved.

## 4. What this changes in the proof strategy

The next stage is now more sharply defined:

1. Isolated-face regularity: derive explicit derivative and Hessian bounds for the SU(2) rotor ground state $\psi_f$, uniformly in the allocated kinetic scale $A_f$.
2. Dressed diffusion: use the bounded face incidence and Hessian estimate to establish a source-volume-uniform Bakry–Émery curvature or Poincaré bound for $L_\Phi$.
3. Residual stability: control $L_\Phi-\sum_eR_e$ using the residual's locality and connected cancellations.

The third step is essential. A uniform gap for $L_\Phi$ does not imply a uniform gap after adding an extensive sum of local potentials. A global operator-norm perturbation estimate would again grow with source volume. We need a local stability or time-space connected-cumulant argument.

This is a better-organized route to the connected-cycle estimate: the first-order face interactions are absorbed exactly, leaving a residual whose local size is conditionally quadratic in $b_0$.

## 5. Four-face results and research record

The four-face calculation is now fully supported for the $N_{\rm grid}=7$ census: all 18,900 connected supports passed the marked incidence-graph isomorphism audit, and the seven exact rational coefficients were computed and independently checked by two methods. The earlier concern about assigning representative coefficients to incompletely audited signature classes is resolved for this crop.

PF_I16_FOUR_FACE_EXACT_ISOMORPHISM_AND_CAUCHY_GATE_2026_11_09.md

The exact coefficients produce four distinct negative values. Their multiplicity-weighted sum is

$$-\frac{1952625908098133263} {7365901893304119459840}\,b^8 \approx -0.00026508986087272536\,b^8.$$

This is the fully four-face-connected eighth-order contribution on that finite source crop—not the complete eighth-order energy and not an all-orders gap result. [Seven-class exact coefficient theorem](https://github.com/syncgravity/singular-boundary/blob/main/research/theorems/PF_I16_EXACT_SEVEN_CLASS_FOUR_FACE_C2222_2026-11-09.md?utm_source=chatgpt.com).

The new incidence correction and dressing reduction, with executable rational checkers, have been committed and read back on the audit branch:

* [Connected-support incidence correction](https://github.com/syncgravity/singular-boundary/blob/audit/pf-i16-local-interacting-vacuum-2026-11-08/research/theorems/PF_I16_CONNECTED_SUPPORT_INCIDENCE_CORRECTION_2026_11_10.md?utm_source=chatgpt.com)
* [Exact shared-link dressing reduction](https://github.com/syncgravity/singular-boundary/blob/audit/pf-i16-local-interacting-vacuum-2026-11-08/research/theorems/PF_I16_LOCAL_DRESSING_SHARED_LINK_RESIDUAL_2026_11_10.md?utm_source=chatgpt.com)
* [Verification scripts](https://github.com/syncgravity/singular-boundary/tree/audit/pf-i16-local-interacting-vacuum-2026-11-08/research/verification?utm_source=chatgpt.com)

Download the combined PF-I16 correction and dressing package

ZIP integrity checked. SHA-256: `ffcc5ecfd1e4f5eacfdb69c2d72f73ddbd2f364e4576bf0e9c9c85faf584923c`.

Current proof verdict: PF-I16 now has exact finite four-face coefficients, a corrected source-uniform combinatorial count, and an exact reduction to shared-link residual interactions after single-face dressing. The volume-uniform residual stability theorem remains the decisive open step. The interacting physical gap, source-derived physical time, continuum construction, and four-dimensional Yang–Mills mass gap remain open.

* * *

**You:**

Please continue the strategy.

* * *

**ChatGPT:**

The isolated-face estimate can be strengthened substantially: a direct Bochner argument gives an explicit gradient bound, and the radial SU(2) equation then gives an explicit Hessian bound. This avoids the character-basis tail estimates I had identified as the next possible route.

The result is uniform in the source graph. It controls the single-face dressing itself; it does not yet establish the curvature or connected-cumulant estimate needed for the full interacting problem.

## 1. Uniform isolated-face derivative theorem

Write the isolated face operator as

$$H_f=A_f(-\Delta_{SU(2)})-b_f p,\qquad p(U)=\tfrac12\chi_{1/2}(U),$$

and put

$$\beta_f=\frac{|b_f|}{A_f}.$$

Use the SU(2) class angle $\theta\in[0,\pi]$, with the metric normalization for which the Laplacian eigenvalues are $n(n+2)/4$. This is the round three-sphere of radius $2$. In this normalization,

$$p(U)=\cos\theta,\qquad \operatorname{Ric}=\tfrac12 g,\qquad |\nabla p|\le\tfrac12.$$

Let $\psi_f>0$ be the normalized ground state and $s_f=\log\psi_f$. Since the potential is central and the positive ground state is unique, $\psi_f$ is central. Divide the eigenvalue equation by $\psi_f$, and write $\lambda_f=E_f/A_f$. Then

$$-\Delta s_f-|\nabla s_f|^2-\beta_f^{\rm signed}\cos\theta =\lambda_f, \qquad |\lambda_f|\le\beta_f.$$

The eigenvalue bound follows from the variational principle: the constant trial state gives $E_f\le0$, while $p$ is bounded in absolute value by one, giving $E_f\ge-|b_f|$.

Gradient bound. Set $w=|\nabla s_f|^2$. At a maximum of $w$, the Bochner identity gives

$$\frac12\Delta w = |\nabla^2s_f|^2+ \langle\nabla s_f,\nabla\Delta s_f\rangle+ \operatorname{Ric}(\nabla s_f,\nabla s_f).$$

Because

$$\nabla\Delta s_f=-\nabla w- \beta_f^{\rm signed}\nabla p,$$

the maximum-point condition $\nabla w=0$, together with $\Delta w\le0$, implies

$$\frac12w \le \beta_f|\nabla s_f|\,|\nabla p| \le\frac{\beta_f}{2}\sqrt w.$$

Consequently,

$$\boxed{\|\nabla s_f\|_\infty\le\beta_f.}$$

Hessian bound. In the radius-two class-angle coordinate,

$$\Delta s_f=\frac14(s_f''+2\cot\theta\,s_f'), \qquad |\nabla s_f|^2=\frac14(s_f')^2.$$

The logarithmic eigenvalue equation becomes

$$s_f''+2\cot\theta\,s_f' +(s_f')^2 +4\beta_f^{\rm signed}\cos\theta+4\lambda_f=0.$$

The gradient estimate gives $|s_f'|\le2\beta_f$. Hence, defining

$$M_f=4\beta_f^2+8\beta_f,$$

we have

$$\left| (s_f')^2+4\beta_f^{\rm signed}\cos\theta+4\lambda_f \right|\le M_f.$$

Multiplying the radial equation by $\sin^2\theta$ and integrating from the nearer regular endpoint gives

$$|\cot\theta\,s_f'|\le M_f.$$

Substitution back into the radial equation yields

$$|s_f''|\le3M_f.$$

The radial and transverse Hessian eigenvalues on the radius-two three-sphere are $s_f''/4$ and $\cot\theta\,s_f'/4$, respectively. Thus

$$\boxed{ \|\nabla^2s_f\|_\infty \le 3\beta_f^2+6\beta_f. }$$

In particular, for $0\le\beta_f\le1$,

$$\boxed{ \|\nabla s_f\|_\infty+ \|\nabla^2s_f\|_\infty \le10\beta_f. }$$

This is an analytic estimate, not a finite-crop numerical observation. The endpoint estimates extend by smoothness at $\theta=0,\pi$.

## 2. The dressed operator has a uniform curvature bound

The derivative theorem also controls the Hessian of the full dressing

$$\Phi=\sum_{f\in F}s_f(U_f),$$

but one extra geometric detail matters: $s_f$ is a function of the product of the four link holonomies, not of four independent copies of the face variable.

For a face holonomy map $h_f:G^4\to G$, varying one link is an isometry of $G$. For two distinct links, the mixed covariant derivative of the multiplication map is one-half of a Lie bracket of the corresponding transported tangent vectors. With the radius-two SU(2) metric,

$$|[X,Y]|\le |X|\,|Y|.$$

It follows that the Hessian blocks of the pulled-back single-face function obey

$$\begin{aligned} \|\nabla^2_{ee}(s_f\circ h_f)\|&\le H_f,\\ \|\nabla^2_{eg}(s_f\circ h_f)\|&\le H_f+\tfrac12G_f \quad(e\ne g), \end{aligned}$$

where

$$G_f=\beta_f,\qquad H_f=3\beta_f^2+6\beta_f.$$

Now put the electric coefficients into the product metric

$$\widetilde g=\bigoplus_{e\in E}a_e^{-1}g_e.$$

This is the metric for which $K=\sum_e a_e(-\Delta_e)$ is the positive Laplacian. Since $d_e\le8$, for any face $f$,

$$A_f=\sum_{e\in\partial f}\frac{a_e}{d_e} \ge\frac{a_0}{2},$$

and, for any two of its links $e,g$,

$$A_f\ge\frac{a_e+a_g}{8}.$$

Assume $a_e\ge a_0>0$, $|b_f|\le b_0$, and $b_0/a_0\le1/2$. Then $\beta_f\le2b_0/a_0\le1$, so the preceding Hessian estimates apply. In the weighted product metric, the diagonal face block is bounded by

$$a_e H_f\le72b_0,$$

and each off-diagonal block by

$$\sqrt{a_ea_g}\,(H_f+\tfrac12G_f)\le38b_0.$$

A face has four links, and at most eight faces meet a link. The block-row-sum bound therefore gives

$$\boxed{ \|\nabla_{\widetilde g}^{\,2}\Phi\|_{\rm op} \le8(72+3\cdot38)b_0 =1488b_0. }$$

The weighted measure for $L_\Phi$ is $e^{2\Phi}d\mu$. Its Bakry–Émery tensor is

$$\operatorname{Ric}_{\widetilde g} -2\nabla_{\widetilde g}^{\,2}\Phi.$$

Since each SU(2) factor has Ricci curvature $a_e/2$ in the weighted metric, we obtain

$$\boxed{ \operatorname{Ric}_{\rm BE}(L_\Phi) \ge \left(\frac{a_0}{2}-2976b_0\right)\widetilde g. }$$

In particular, if

$$\boxed{\frac{b_0}{a_0}<\frac1{5952},}$$

then $L_\Phi$ has a source-volume-independent positive curvature lower bound

$$\kappa=\frac{a_0}{2}-2976b_0>0.$$

The weighted Poincaré inequality follows:

$$\operatorname{Var}_{e^{2\Phi}\mu}(F) \le \frac1\kappa \int\sum_e a_e|\nabla_eF|^2\,e^{2\Phi}d\mu.$$

This closes the second analytic gate in the dressing strategy, subject to the stated SU(2) metric and incidence hypotheses. The constant $1/5952$ is a conservative sufficient threshold, not an optimized one.

## 3. The shared-link residual is now explicitly bounded

The exact residual identity was

$$e^{-\Phi}He^\Phi = L_\Phi+\sum_fE_f-\sum_eR_e.$$

The gradient theorem gives, without an additional one-face derivative hypothesis,

$$\ell_f=\max_{e\in\partial f}\|\nabla_es_f\|_\infty \le\frac{|b_f|}{A_f}.$$

Using the residual estimate

$$|R_e| \le a_e(d_e^2+1) \max_{f:e\in\partial f}\ell_f^2,$$

and the two bounds $A_f\ge a_e/d_e$ and $A_f\ge a_0/2$, we get

$$\frac{a_e}{A_f^2} \le\frac{d_e}{A_f} \le\frac{16}{a_0}.$$

Thus, with $d_e\le8$,

$$\boxed{ \|R_e\|_\infty \le 1040\,\frac{b_0^2}{a_0}. }$$

Each $R_e$ is supported on the union of the faces incident to $e$, hence on at most

$$1+3d_e\le25$$

original links. The crude overlap count remains at most $800$ residual terms per residual support.

So the reduction now has three quantitative pieces:

1. Exact single-face dressing, eliminating residuals on singly incident links.
2. A volume-uniform Poincaré bound for the dressed reference operator, when $b_0/a_0<1/5952$.
3. A uniformly bounded, finite-range shared-link residual of order $b_0^2/a_0$.

## 4. What remains: control the residual cumulants, not its total norm

The transformed Hamiltonian still contains

$$V=\sum_eR_e.$$

Although every $R_e$ is uniformly bounded and local, $\|V\|_\infty$ can grow with the number of links. A global Kato estimate would therefore reintroduce volume dependence. The Poincaré inequality alone does not solve this: it controls global fluctuations, but does not by itself give the spatially connected cumulant bounds required for an exact-support activity estimate.

The next proof should have three parts.

A. Spatially weighted semigroup estimate. Retain the block structure of the Bakry–Émery tensor instead of using only its scalar lower bound. Its off-diagonal blocks couple links belonging to a common face. The link-interaction graph has degree at most

$$3\cdot8=24.$$

A matrix-valued gradient estimate for the dressed semigroup should then give decay of influence with link-graph distance, provided the diagonal curvature dominates the off-diagonal influence matrix. The scalar curvature estimate above supplies a first sufficient small-coupling condition; the matrix estimate is needed for spatial decay.

B. Derivative control of the residuals. Since $R_e$ is quadratic in the first derivatives of $s_f$, its first derivatives involve only the second derivatives already bounded above. This is important: the next step does not require a third-derivative theorem merely to establish residual locality and Lipschitz control. The target is a bound of the form

$$\|\nabla R_e\|_{\widetilde g} \le C_R\,\frac{b_0^2}{a_0},$$

with $C_R$ independent of source volume. It must be derived with the weighted link metric and the actual face-incidence structure, not inferred from the scalar sup-norm bound alone.

C. Connected space-time cumulants. Use the Feynman–Kac representation for $L_\Phi-V$. The logarithm of its partition function is organized by connected time-ordered cumulants of the $R_e$. Combine temporal decay from the positive curvature with spatial decay from part A, and use a tree-graph bound to sum connected collections. The desired conclusion is a uniform estimate of the form

$$|\zeta_G(S;\mathbf b)| \le A q^{|S|}, \qquad q=O\!\left((b_0/a_0)^2\right),$$

where the constants do not depend on source volume. The precise $A$ and $q$ must come from the cumulant proof; they cannot yet be read off from the residual sup-norm estimate.

Only after that estimate is established can we invoke the conservative universal connected-support count

$$N_f(k)\le784^{k-1}.$$

It would then suffice to show $q<1/784$ for the corresponding rooted geometric sum.

### Updated proof ledger

|   Statement   |   Status   |
| --- | --- |
|   Exact isolated-face ground-state dressing   |   Established   |
|   Uniform isolated-face gradient bound $\|\nabla s_f\|\le\beta_f$   |   Established analytically   |
|   Uniform isolated-face Hessian bound $\|\nabla^2s_f\|\le3\beta_f^2+6\beta_f$   |   Established analytically   |
|   Uniform dressed-reference curvature and Poincaré bound for $b_0/a_0<1/5952$   |   Established under the stated incidence and metric hypotheses   |
|   Shared-link residual support size at most 25 links   |   Established   |
|   Residual sup-norm bound $1040b_0^2/a_0$   |   Established under those hypotheses   |
|   Spatially decaying dressed-semigroup influence   |   Open   |
|   Uniform connected space-time cumulant bound   |   Open   |
|   Source-volume-uniform exact-support activity $Aq^{|S|}$   |   Open   |
|   All-orders interacting vacuum or physical mass gap   |   Not established   |

The significant change is that the single-face analytic estimates and the dressed-reference Poincaré inequality are no longer speculative gates. The remaining bottleneck is now sharply localized: prove spatially connected cumulant control for the shared-link residual under the dressed reference dynamics. That is the next theorem to attack; it is also the point at which the argument must do more than ordinary spectral-gap perturbation theory.

* * *

**You:**

Proceed with the next theorem.

* * *

**ChatGPT:**

The next theorem is a spatially weighted semigroup estimate for the dressed reference dynamics. It strengthens the volume-uniform Poincaré inequality: instead of merely saying that fluctuations decay in time, it quantifies how influence propagates between distinct original links.

It also gives a concrete derivative bound for each shared-link residual. Together, these results put the residual cumulant problem on a more precise footing.

## Theorem 1 — Spatially weighted influence decay

Let $\mathcal L_\Phi$ denote the Markov generator corresponding to the positive operator $L_\Phi$, reversible in

$$d\pi_\Phi=Z_\Phi^{-1}e^{2\Phi}d\mu.$$

Let $\mathcal G$ be the graph whose vertices are original links, with two vertices adjacent when their links belong to a common accepted face. The incidence bound $d_e\le8$ gives

$$\deg(\mathcal G)\le24.$$

Assume the hypotheses and small-coupling condition already established:

$$a_e\ge a_0>0,\qquad |b_f|\le b_0,\qquad \frac{b_0}{a_0}<\frac1{5952}.$$

For $\mu>0$, define

$$\lambda_\mu= \frac{a_0}{2}-1152b_0-1824e^\mu b_0.$$

Whenever $\lambda_\mu>0$, the dressed semigroup $P_t=e^{t\mathcal L_\Phi}$ obeys

$$\boxed{ \|\nabla_eP_tF\|_\infty \le e^{-\lambda_\mu t} \sum_g e^{-\mu d_{\mathcal G}(e,g)} \|\nabla_gF\|_\infty. } \tag{1}$$

Here $d_{\mathcal G}$ is link-graph distance, and a derivative at a disconnected vertex is zero.

In particular, if $F$ is supported on a link set $X$,

$$\boxed{ \|\nabla_eP_tF\|_\infty \le e^{-\lambda_\mu t-\mu d_{\mathcal G}(e,X)} \sum_{g\in X}\|\nabla_gF\|_\infty. } \tag{2}$$

For every strict inequality $b_0/a_0<1/5952$, some positive $\mu$ exists. Thus the dressed reference process has both temporal decay and spatially decaying influence, uniformly in source volume.

### Proof

Write $\mathcal H_{eg}$ for the $e,g$ block of the Hessian of $\Phi$, expressed in the orthonormal frame of the weighted product metric. The isolated-face estimates give, after summing over incident faces,

$$\|\mathcal H_{ee}\|\le576b_0, \qquad \sum_{g\ne e}\|\mathcal H_{eg}\|\le912b_0.$$

The first sum is diagonal; the second involves only adjacent links.

The damped parallel-transport equation for the derivative of the diffusion semigroup has diagonal damping bounded below by

$$\frac{a_0}{2}-2(576b_0) =\frac{a_0}{2}-1152b_0,$$

and off-diagonal propagation bounded by the nonnegative matrix

$$J_{eg}=2\|\mathcal H_{eg}\|,\quad e\ne g, \qquad J_{ee}=0.$$

Its ordinary row sum is at most $1824b_0$. Since $J$ connects only adjacent vertices, its exponentially distance-weighted row sum is at most

$$\sup_e\sum_g e^{\mu d_{\mathcal G}(e,g)}J_{eg} \le1824e^\mu b_0.$$

The weighted matrix differential inequality therefore contracts at rate $\lambda_\mu$. The comparison semigroup has entries bounded by

$$e^{-\lambda_\mu t-\mu d_{\mathcal G}(e,g)}.$$

Applying this to the componentwise gradient of $F$ proves (1), and support localization gives (2). Compactness of each finite product of SU(2) factors ensures that the diffusion and its damped derivative flow are well-defined. The constants do not depend on the number of factors. $\square$

At $\mu=0$, the rate reduces to the previous curvature constant:

$$\lambda_0=\frac{a_0}{2}-2976b_0.$$

The spatial estimate is therefore a genuine strengthening of the earlier Poincaré result, not a separate small-coupling assumption at zero distance weight.

A convention needs to be made explicit in the theorem: the gradients in (1)–(2) are the weighted orthonormal components

$$D_eF:=\sqrt{a_e}\,\nabla_eF,$$

not the unweighted link gradients. This is the natural frame for the product metric and for the Dirichlet form

$$\mathcal E_\Phi(F,G) =\int\sum_e\langle D_eF,D_eG\rangle\,d\pi_\Phi.$$

With this convention, the covariance consequence has a clean form.

## Corollary — Spatial covariance clustering

For smooth functions $F,G$ supported on link sets $X,Y$, respectively,

$$\boxed{ |\operatorname{Cov}_{\pi_\Phi}(F,G)| \le \frac{e^{-\mu d_{\mathcal G}(X,Y)}}{\lambda_\mu} \left(\sum_{g\in X}\|D_gF\|_\infty\right) \left(\sum_{e\in Y}\|D_eG\|_\infty\right). } \tag{3}$$

Indeed, reversibility and semigroup convergence give the covariance representation

$$\operatorname{Cov}_{\pi_\Phi}(F,G) = \int_0^\infty \mathcal E_\Phi(P_tF,G)\,dt.$$

Insert the weighted gradient estimate, use the separation of $X,Y$, and integrate $e^{-\lambda_\mu t}$. This proves (3).

This is a two-observable clustering theorem. It is not yet the higher-cumulant theorem needed for the activity expansion.

## 5. Residual regularity: an explicit bound

Let $m=d_e$, and for each face incident to $e$, put

$$u_f=\nabla_es_f,\qquad A=\sum_{f:e\in\partial f}u_f.$$

Then

$$R_e=a_e\left(|A|^2-\frac1m \sum_{f:e\in\partial f}|u_f|^2\right).$$

The pulled-back Hessian block bounds imply, for every link $h$ in the support of $R_e$,

$$\|D_hu_f\|_\infty \le\frac{72b_0}{\sqrt{a_e}}.$$

Also, for every incident face,

$$\|u_f\|_\infty \le\beta_f \le\frac{8b_0}{a_e}.$$

Differentiating the exact residual expression therefore yields

$$\|D_hR_e\|_\infty \le 144b_0\sqrt{a_e}\, \max_{f:e\in\partial f}\beta_f\,(m^2+1) \le 74880\,\frac{b_0^2}{\sqrt{a_0}},$$

since $m\le8$.

There are at most 25 links in its support, so

$$\boxed{ \|D R_e\|_\infty \le 374400\,\frac{b_0^2}{\sqrt{a_0}}. } \tag{4}$$

Here the norm is the Euclidean norm of all weighted gradient components. The bound is deliberately conservative; its important features are its quadratic coupling order and independence from source volume.

Together with the already established bound

$$\|R_e\|_\infty\le1040\,\frac{b_0^2}{a_0},$$

this gives both amplitude and first-derivative control for every residual term.

## 6. Corollary — Summable residual covariance

Choose

$$\mu=\log25.$$

Then

$$\lambda_*= \frac{a_0}{2}-46752b_0.$$

Thus, under the stronger sufficient condition

$$\boxed{\frac{b_0}{a_0}<\frac1{93504},} \tag{5}$$

the residuals have exponentially decaying pair covariances.

Write $S_e$ for the link support of $R_e$. It lies within graph distance one of $e$, so

$$d_{\mathcal G}(S_e,S_g) \ge d_{\mathcal G}(e,g)-2.$$

Using (3) and (4), and the fact that each residual support has at most 25 links, gives

$$\boxed{ |\operatorname{Cov}_{\pi_\Phi}(R_e,R_g)| \le \frac{625(1\,872\,000)^2}{\lambda_*} \frac{b_0^4}{a_0} 25^{-d_{\mathcal G}(e,g)}. } \tag{6}$$

Because the link graph has degree at most 24,

$$\sum_g25^{-d_{\mathcal G}(e,g)} \le 1+\sum_{r\ge1}\left(\frac{24}{25}\right)^r =25.$$

Consequently,

$$\boxed{ \sup_e\sum_g |\operatorname{Cov}_{\pi_\Phi}(R_e,R_g)| \le \frac{25^2(1\,872\,000)^2}{\lambda_*} \frac{b_0^4}{a_0}. } \tag{7}$$

This is a source-volume-uniform, absolutely summable second-cumulant estimate for the shared-link residual.

## 7. The next theorem is now clearly identified

The argument has reached the following boundary:

|   Required result   |   Status   |
| --- | --- |
|   Dressed-reference spatial influence decay   |   Established   |
|   Two-observable covariance clustering   |   Established   |
|   Residual amplitude and derivative bounds   |   Established   |
|   Absolutely summable residual pair covariance   |   Established under (5)   |
|   Uniform higher connected cumulant tree bound   |   Open   |
|   Uniform exact-support activity $Aq^{|S|}$   |   Open   |

The remaining theorem must control, for every $n\ge3$, the connected cumulants

$$\kappa_{\pi_\Phi} (R_{e_1},\ldots,R_{e_n})$$

by a spanning-tree expression, with constants whose growth in $n$ is controlled well enough to sum the time-ordered Feynman–Kac expansion.

A useful target is

$$\left| \kappa_{\pi_\Phi}(R_{e_1},\ldots,R_{e_n}) \right| \le C^n \left(\frac{b_0^2}{a_0}\right)^n \sum_{T\in\mathcal T_n} \prod_{\{i,j\}\in T} e^{-\mu' d_{\mathcal G}(S_{e_i},S_{e_j})}, \tag{8}$$

for some $\mu'>0$, with $C,\mu'$ independent of source volume.

But (8) does not follow from pair covariance clustering alone. It needs a genuine higher-order mixing or iterated conditional-influence argument. In particular, the factor $C^n$ and the time integrations must be controlled together; a bound with uncontrolled $n!$ growth would not establish a nonzero uniform activity radius.

The important advance: the remaining problem is no longer to establish generic mixing of the original gauge system. It is to establish higher-order connected mixing for a specific, bounded, finite-range residual under a reference diffusion whose spatial influence and temporal decay are already quantified. That is a substantially narrower theorem, and it is the right next target for PF-I16.

* * *

**You:**

Continue on the problem.

* * *

**ChatGPT:**

The next useful step is to strengthen the spatial semigroup estimate into a conditional influence theorem. This matters because higher connected cumulants require control of how an entire conditional distribution responds to changes elsewhere—not merely a bound on pair covariances.

There is a particularly useful feature of the constants already obtained: the same small-coupling condition that made the weighted semigroup contractive also makes the conditional influence matrix summable.

## Theorem 2 — Dobrushin influence bound for the dressed reference measure

Let

$$d\pi_\Phi=Z_\Phi^{-1}e^{2\Phi}d\mu, \qquad \Phi=\sum_fs_f(U_f),$$

and let $\mathcal G$ be the original-link interaction graph. Define

$$\kappa_*=\frac{a_0}{2}-1152b_0, \qquad J_{eg}=2\|\nabla^2_{eg}\Phi\|_{\rm op} \quad(e\ne g).$$

Under the incidence and metric hypotheses from the preceding estimates,

$$\sum_{g\ne e}J_{eg}\le1824b_0, \qquad J_{eg}=0\quad\text{if }d_{\mathcal G}(e,g)>1.$$

For the conditional law of link $e$, with all other links fixed, the Bakry–Émery curvature is bounded below by $\kappa_*$. If only link $g$ is changed in the conditioning configuration, the Wasserstein distance between the two conditional laws satisfies

$$W_1\!\left( \pi_\Phi(dx_e\mid x_{\ne e}), \pi_\Phi(dx_e\mid x'_{\ne e}) \right) \le \frac{J_{eg}}{\kappa_*}\, d_g(x_g,x'_g). \tag{9}$$

Consequently, define the influence matrix

$$C_{eg}=\frac{J_{eg}}{\kappa_*},\quad e\ne g, \qquad C_{ee}=0.$$

Then

$$\boxed{ \sup_e\sum_g C_{eg} \le \frac{1824b_0}{a_0/2-1152b_0}<1 } \tag{10}$$

whenever

$$\frac{b_0}{a_0}<\frac1{5952}.$$

More strongly, for every $\mu>0$ for which

$$\lambda_\mu =\frac{a_0}{2}-1152b_0-1824e^\mu b_0>0,$$

we have

$$\boxed{ \sup_e\sum_g e^{\mu d_{\mathcal G}(e,g)}C_{eg} \le \frac{1824e^\mu b_0}{\kappa_*}<1. } \tag{11}$$

### Proof

For fixed values of all links other than $e$, the conditional density at $e$ is proportional to

$$\exp\left(2\sum_{f:e\in\partial f}s_f\right)d\mu_e.$$

Its curvature is bounded below by the single-link Ricci curvature $a_e/2$ minus the diagonal Hessian contribution $2\|\nabla^2_{ee}\Phi\|$. The previously established diagonal block estimate gives the lower bound $\kappa_*$.

Changing the conditioning value at $g$ changes the gradient of the conditional log density at $e$ by at most

$$2\|\nabla^2_{eg}\Phi\|_{\rm op}\,d_g(x_g,x'_g).$$

Interpolate between the two conditioning values along a minimizing geodesic. The curvature lower bound gives contraction of the conditional diffusion at rate $\kappa_*$; integrating the interpolated perturbation over time yields (9).

The row-sum estimates follow from the established off-diagonal Hessian bound. Since $J$ is supported on adjacent links, weighting by $e^{\mu d}$ costs at most $e^\mu$. This proves (10) and (11). $\square$

The result is stronger than ordinary uniqueness: it gives a spatially weighted influence resolvent. In fact, with

$$D=(I-C)^{-1}=I+C+C^2+\cdots,$$

the weighted row sums satisfy

$$\boxed{ \sup_e\sum_g e^{\mu d_{\mathcal G}(e,g)}D_{eg} \le \frac1{1-\rho_\mu}, \qquad \rho_\mu=\frac{1824e^\mu b_0}{\kappa_*}<1. } \tag{12}$$

This is a source-volume-independent bound.

## Theorem 3 — Static residual cluster expansion

There is a second route to higher cumulants which complements the conditional-influence argument: expand the dressed reference measure itself around product Haar measure. This gives a convergent spatial polymer expansion and controls equal-time residual cumulants.

It is important to distinguish this from the desired Feynman–Kac result: the theorem below concerns the static measure $\pi_\Phi$, not yet the stationary diffusion path measure.

### 1. The face interaction is a small polymer activity

The radius-two SU(2) factor has geodesic diameter $2\pi$. The gradient estimate gives

$$\operatorname{osc}(s_f) \le 2\pi\beta_f \le\frac{4\pi b_0}{a_0},$$

because $A_f\ge a_0/2$.

Subtract an arbitrary midpoint of the range of $2s_f$, which does not change the normalized measure. Define

$$g_f=e^{2s_f-c_f}-1.$$

Then

$$\|g_f\|_\infty\le \delta,\qquad \delta:=e^{4\pi b_0/a_0}-1. \tag{13}$$

The face-overlap graph has maximum degree 28. A connected set of $k$ faces containing a fixed face has at most $784^{k-1}$ possibilities by the established depth-first-walk encoding. Consequently, the total rooted connected-polymer weight is bounded by

$$\sum_{k\ge1}784^{k-1}(e\delta)^k = \frac{e\delta}{1-784e\delta}. \tag{14}$$

For the Kotecký–Preiss criterion, a polymer is incompatible with another if their face supports overlap. At most 29 face roots lie in the closed neighborhood of any given face. Thus the sufficient condition is

$$\boxed{813e\delta<1.} \tag{15}$$

This condition is satisfied throughout the stronger regime already being used,

$$\frac{b_0}{a_0}<\frac1{93504}.$$

Indeed, at that endpoint,

$$813e\left(e^{4\pi/93504}-1\right)<0.30.$$

Therefore the static partition function of the dressed reference measure has a volume-uniform convergent face-polymer expansion.

### 2. Insertions of the shared-link residual

Let

$$R_*:=1040\,\frac{b_0^2}{a_0}, \qquad \|R_e\|_\infty\le R_*.$$

Introduce independent source variables $t_e$:

$$Z(\mathbf t)= \int \exp\left( 2\sum_fs_f+\sum_et_eR_e \right)d\mu. \tag{16}$$

The normalized derivatives satisfy

$$\left. \partial_{t_{e_1}}\cdots\partial_{t_{e_n}} \log Z(\mathbf t) \right|_{\mathbf t=0} = \kappa_{\pi_\Phi}(R_{e_1},\ldots,R_{e_n}). \tag{17}$$

A source insertion is itself a local interaction,

$$h_e(t_e)=e^{t_eR_e}-1, \qquad \|h_e(t_e)\|_\infty \le e^{|t_e|R_*}-1.$$

The mixed interaction graph has the following conservative incidence bounds:

|   Interaction type   |   Number of incompatible interactions   |
| --- | --- |
|   Face with faces   |   28   |
|   Face with residual insertions   |   32   |
|   Residual insertion with faces   |   200   |
|   Residual insertion with residual insertions   |   800   |

The last two bounds follow from the residual support size of at most 25 links, at most eight faces per link, and four links per face.

Set

$$\epsilon_*= \frac12\min\left\{ \frac{1-28e\delta}{32e}, \frac{1-200e\delta}{800e} \right\}>0, \qquad t_*=\frac{\log(1+\epsilon_*)}{R_*}. \tag{18}$$

For $|t_e|\le t_*$, every residual insertion has activity at most $\epsilon_*$. The two-type branching bounds are then strictly subcritical:

$$28e\delta+32e\epsilon_*<1, \qquad 200e\delta+800e\epsilon_*<1. \tag{19}$$

The mixed polymer expansion therefore converges uniformly in source volume in this polydisc. Its logarithm consists only of connected clusters. Differentiating it at zero gives the equal-time connected cumulants in (17), with only spatially connected face/residual clusters contributing.

This establishes a nonzero, source-volume-independent analyticity radius for the static residual generating function. In particular, it rules out the possibility that the equal-time residual cumulant expansion has a radius collapsing merely because the source volume grows.

## 4. The key bridge: a space-time block-factorization estimate

The semigroup estimate can be used twice: first to propagate a residual insertion through a block of times, and then to measure the dependence between two successive time blocks.

Choose exponents

$$0<\nu<\mu-\log24, \qquad \lambda_\mu>0,$$

which is possible under the strict condition $b_0/a_0<1/93504$. Define

$$S_{\mu-\nu} = 1+\frac{24}{e^{\mu-\nu}-24}.$$

For a link set $X$, introduce the weighted derivative norm

$$\mathcal D_{\nu,X}(F) = \sum_g e^{\nu d_{\mathcal G}(g,X)} \|D_gF\|_\infty.$$

The spatial semigroup estimate implies

$$\boxed{ \mathcal D_{\nu,X}(P_tF) \le S_{\mu-\nu}e^{-\lambda_\mu t} \mathcal D_{\nu,X}(F). } \tag{20}$$

Set

$$M_R=\sup_e\mathcal D_{\nu,S_e}(R_e),$$

where $S_e$ is the residual support. The established residual derivative estimate gives the volume-independent bound

$$M_R\le 25\cdot374400\,\frac{b_0^2}{\sqrt{a_0}}.$$

Now take ordered times

$$t_1\le\cdots\le t_n$$

and residual observables $R_i(X_{t_i})$. Split them at any $k$, with

$$A=\{1,\ldots,k\},\quad B=\{k+1,\ldots,n\},\quad \Delta_k=t_{k+1}-t_k.$$

Define the conditional block functions

$$F_A(x)= \mathbb E\left[ \prod_{i\le k}R_i(X_{t_i})\mid X_{t_k}=x \right],$$

$$G_B(x)= \mathbb E\left[ \prod_{i>k}R_i(X_{t_i})\mid X_{t_{k+1}}=x \right].$$

Reversibility and the Markov property give the exact identity

$$\begin{aligned} &\mathbb E\prod_{i=1}^nR_i(X_{t_i}) -\mathbb E\prod_{i\in A}R_i(X_{t_i}) \mathbb E\prod_{i\in B}R_i(X_{t_i})\\ &\qquad= \operatorname{Cov}_{\pi_\Phi} \left(F_A,P_{\Delta_k}G_B\right). \end{aligned} \tag{21}$$

The product rule and (20) yield

$$\mathcal D_{\nu,X_A}(F_A) \le kS_{\mu-\nu}^{k-1}M_RR_*^{k-1},$$

and the analogous bound for $G_B$. Applying the covariance representation and the spatial gradient kernel then gives

$$\boxed{ \begin{aligned} &\left| \mathbb E\prod_{i=1}^nR_i(X_{t_i}) -\mathbb E\prod_{i\in A}R_i(X_{t_i}) \mathbb E\prod_{i\in B}R_i(X_{t_i}) \right|\\ &\quad\le \frac{S_{\mu-\nu}^{\,n-1}}{\lambda_\mu}\, k(n-k)\, M_R^2R_*^{n-2}\, e^{-\lambda_\mu\Delta_k} e^{-\nu d_{\mathcal G}(S_A,S_B)}. \end{aligned} } \tag{22}$$

Here $S_A=\bigcup_{i\in A}S_{e_i}$, and likewise for $S_B$.

This is a genuine space-time estimate. It controls factorization across every contiguous temporal cut, uniformly in source volume. It is stronger than the earlier pair-covariance estimate because the two blocks may contain arbitrarily many residual insertions.

## 5. The remaining combinatorial theorem

Equation (22) gives the analytic input for an ordered cluster expansion. The remaining issue is to convert these block-factorization defects into an all-order classical cumulant tree bound.

The desired form is

$$\boxed{ |\kappa(R_1(X_{t_1}),\ldots,R_n(X_{t_n}))| \le C_0^n R_*^n e^{-\lambda_\mu(t_n-t_1)} \sum_{T\in\mathcal T_n} \prod_{\{i,j\}\in T} e^{-\nu' d_{\mathcal G}(S_{e_i},S_{e_j})}, } \tag{23}$$

for some $0<\nu'<\nu$, with $C_0$ independent of source volume and $n$.

There is a useful reason for the particular temporal factor in (23). Integrating over the ordered time simplex gives

$$\begin{aligned} &\int_{0<t_1<\cdots<t_n<T} e^{-\lambda_\mu(t_n-t_1)}\,dt_1\cdots dt_n\\ &\qquad\le \frac{T}{\lambda_\mu^{n-1}}. \end{aligned} \tag{24}$$

Thus the time integration contributes one factor of $T$, as appropriate for an energy density, and only $\lambda_\mu^{-(n-1)}$ per order.

Likewise, the spatial tree sum can be rooted at one residual index. The bounded link degree and finite residual support make the sum over each additional tree vertex finite. The number of labelled trees is $n^{n-2}$, whose growth is compatible with the $1/n!$ in the exponential cumulant expansion if the coefficient in (23) is genuinely exponential in $n$.

But (23) has not yet been proved. The contiguous-cut estimate (22) alone does not automatically imply it: classical cumulants involve all set partitions, including interlaced temporal subsets. The missing argument is an ordered partition-to-tree lemma with an exponential-in-$n$ constant, not an $n!$-sized loss.

### Current proof boundary

|   Result   |   Status   |
| --- | --- |
|   Uniform face-polymer expansion of the dressed reference measure   |   Established under (15)   |
|   Dobrushin spatial influence and weighted resolvent   |   Established under the stated curvature hypotheses   |
|   Uniform residual amplitude and derivative bounds   |   Established   |
|   Space-time contiguous-block factorization (22)   |   Derived   |
|   All-partition cumulant-to-tree conversion   |   Open   |
|   Feynman–Kac connected-cycle activity $Aq^{|S|}$   |   Open   |

The next proof task is now sharply defined: establish the partition-to-tree conversion for the Markov path observables, preserving the exponential-in-$n$ constants. If it succeeds, (22) and (24) supply the analytic estimates needed to sum the time-ordered connected expansion. If it fails or incurs factorial growth, that identifies the precise obstruction rather than hiding it inside a generic mixing assumption.

* * *

**You:**

Proceed with the next proof.

* * *

**ChatGPT:**

The partition-to-tree step needs a more careful treatment than the previous outline suggested. I can establish a rigorous cut-to-cumulant estimate, but it exposes a factorial loss. That loss is important: it shows exactly why the contiguous-block estimate is not, by itself, enough to prove the desired all-orders activity bound.

## 1. A precise cut-to-cumulant lemma

Let $X_1,\ldots,X_n$ be bounded random variables, normalized so that $\|X_i\|_\infty\le1$. Let

$$A=\{1,\ldots,k\},\qquad B=\{k+1,\ldots,n\}.$$

Suppose their joint moments approximately factor across this cut: for every nonempty $I\subseteq\{1,\ldots,n\}$,

$$\left| \mathbb E\prod_{i\in I}X_i - \left(\mathbb E\prod_{i\in I\cap A}X_i\right) \left(\mathbb E\prod_{i\in I\cap B}X_i\right) \right| \le\epsilon, \tag{25}$$

where an empty-side moment is interpreted as one.

Then

$$\boxed{ |\kappa(X_1,\ldots,X_n)| \le n\,B_n\,\epsilon, \qquad B_n=\sum_{j=1}^n \left\{\begin{matrix}n\\j\end{matrix}\right\}(j-1)!. } \tag{26}$$

Here the braces denote Stirling numbers of the second kind.

Proof. The cumulant is the partition polynomial

$$\kappa(X_1,\ldots,X_n) = \sum_{\pi\in\Pi_n} (|\pi|-1)!(-1)^{|\pi|-1} \prod_{C\in\pi}m(C),$$

where $m(C)=\mathbb E\prod_{i\in C}X_i$.

Replace each $m(C)$ by its factorized counterpart across $A|B$. The resulting joint moment functional is the moment functional of two independent families, one on each side. Its mixed cumulant is zero.

For each partition term, telescope the difference between the original product of moments and the factorized product. Every moment has absolute value at most one, and each individual replacement costs at most $\epsilon$. A partition with $j$ blocks therefore costs at most $j\epsilon$. Summing the absolute partition coefficients gives (26). $\square$

The same result holds without normalization, with the right-hand side multiplied by $\prod_i\|X_i\|_\infty$.

## 2. The combinatorial constant has factorial growth

The exponential generating function of $B_n$ is explicit:

$$\begin{aligned} \sum_{n\ge1}B_n\frac{z^n}{n!} &=\sum_{j\ge1}\frac{(j-1)!}{j!}(e^z-1)^j\\ &=-\log(2-e^z). \end{aligned}$$

Its nearest singularity is at $z=\log2$. In particular, evaluating its positive-coefficient series at $z=1/2$ gives

$$\boxed{ B_n\le -\log(2-e^{1/2})\,2^n n!. } \tag{27}$$

Thus the straightforward partition argument incurs factorial growth.

## 3. Application to the PF-I16 path observables

Take

$$X_i=\frac{R_{e_i}(X_{t_i})}{R_*}, \qquad R_*=1040\,\frac{b_0^2}{a_0},$$

so that $\|X_i\|_\infty\le1$.

For a temporal cut at $k$, write $\Delta_k=t_{k+1}-t_k$. Applying the block-factorization estimate to each subset of the insertions gives the following conservative bound:

$$\epsilon_n(\Delta_k) \le \frac{n^2}{\lambda_\mu} S_{\mu-\nu}^{n-1} \left(\frac{M_R}{R_*}\right)^2 e^{-\lambda_\mu\Delta_k}. \tag{28}$$

Here we have discarded the additional spatial separation factor, so this estimate does not require any assumption on the relative locations of the residuals.

Combining (26)–(28),

$$\boxed{ \begin{aligned} |\kappa(R_{e_1}(X_{t_1}),\ldots,R_{e_n}(X_{t_n}))| \le{}& R_*^n\, \frac{n^3B_n}{\lambda_\mu} S_{\mu-\nu}^{n-1} \left(\frac{M_R}{R_*}\right)^2\\ &\times e^{-\lambda_\mu\Delta_k}. \end{aligned} } \tag{29}$$

Choosing the largest temporal gap,

$$\Delta_k\ge\frac{t_n-t_1}{n-1},$$

gives a bound with decay in the total time span. However, it does not give a product of decay factors along a spanning tree.

Insufficient for all-orders summability

The $B_n$ factor grows factorially. The estimate therefore does not prove the desired source-volume-uniform activity radius. It is a valid finite-order cumulant bound conditional on the preceding block estimate, but it is not the missing tree theorem.

## 4. The stronger theorem we actually need

The right target is a multi-cut factorization theorem. Instead of splitting the ordered insertions at just one temporal cut, take any collection of cuts

$$0\le k_1<k_2<\cdots<k_m\le n$$

and divide the insertions into consecutive temporal blocks.

We need to show that the joint path moment admits a connected-block expansion in which each connection between blocks costs an influence factor. Schematically,

$$\left|\kappa(X_1,\ldots,X_n)\right| \le C^n \sum_{T\in\mathcal T_n} \prod_{\{i,j\}\in T} w_{ij}, \tag{30}$$

where $w_{ij}$ combines temporal and spatial separation, and $C$ is independent of both $n$ and source volume.

There is a natural route to this result:

1. Use the Markov property to condition successively at every temporal boundary.
2. Represent each conditional block as a function of its boundary configuration.
3. Apply the weighted influence resolvent $D=(I-C)^{-1}$ to propagate the dependence of each block.
4. Expand the resulting block-dependence functional over connected trees, retaining one influence factor for every tree edge.
5. Sum the temporal gaps and spatial branches before taking the large-order limit.

The important distinction is that this method must retain the individual influence edges. Replacing them at the outset with one global mixing error is exactly what produced the factorial loss above.

### Updated proof ledger

|   Result   |   Status   |
| --- | --- |
|   Isolated-face derivative and Hessian estimates   |   Established   |
|   Dressed-reference curvature and Poincaré inequality   |   Established under stated hypotheses   |
|   Dobrushin influence matrix and weighted resolvent   |   Established under stated hypotheses   |
|   Static dressed-measure polymer expansion   |   Established under its stated smallness condition   |
|   Residual amplitude and derivative bounds   |   Established   |
|   Space-time contiguous-block factorization   |   Derived   |
|   Cut-to-cumulant estimate with explicit factorial constant   |   Proved   |
|   Multi-cut connected-block/tree expansion   |   Open   |
|   Uniform all-orders exact-support activity   |   Open   |

Conclusion: the next proof must preserve the full influence matrix through the cumulant calculation. A single covariance or mixing coefficient cannot do that. The multi-cut expansion is the remaining mathematical step; until it is proved, neither the all-orders quantum activity estimate nor an interacting spectral gap follows.

* * *

**You:**

Continue the next proof.

* * *

**ChatGPT:**

The next step is to move from time-ordered cumulants to the reduced resolvent of the dressed reference operator. This is a useful change of representation: the Feynman–Kac time integrals can be encoded by resolvents, and their spatial decay can be estimated before attempting the connected-tree combinatorics.

It also avoids trying to infer a higher-cumulant theorem directly from a single contiguous temporal cut.

## Theorem 4 — Uniform quasi-locality of the reduced resolvent

Let $L_\Phi$ be the nonnegative self-adjoint dressed operator, with invariant probability measure $\pi_\Phi$. Write

$$P_t=e^{-tL_\Phi},\qquad \Pi F=\pi_\Phi(F).$$

Assume the weighted semigroup estimate already derived, with

$$\lambda_\mu>0,\qquad \mu>\log24.$$

For a function $F$ supported on a finite link set $X$, define

$$\mathcal R F = \int_0^\infty P_t(F-\Pi F)\,dt.$$

Then

$$L_\Phi\mathcal R F=F-\Pi F, \qquad \Pi\mathcal R F=0.$$

The semigroup gradient estimate gives

$$\boxed{ \|D_e\mathcal R F\|_\infty \le \frac{e^{-\mu d_{\mathcal G}(e,X)}}{\lambda_\mu} \sum_{g\in X}\|D_gF\|_\infty. } \tag{31}$$

Here $D_e=\sqrt{a_e}\nabla_e$ is the weighted orthonormal link derivative.

Define

$$S_\mu=1+\frac{24}{e^\mu-24}.$$

Summing (31) over all links gives

$$\boxed{ \sum_e\|D_e\mathcal R F\|_\infty \le \frac{S_\mu}{\lambda_\mu} \sum_{g\in X}\|D_gF\|_\infty. } \tag{32}$$

More generally, for $0<\nu<\mu-\log24$,

$$\boxed{ \sum_e e^{\nu d_{\mathcal G}(e,X)} \|D_e\mathcal R F\|_\infty \le \frac{S_{\mu-\nu}}{\lambda_\mu} \sum_{g\in X}\|D_gF\|_\infty. } \tag{33}$$

### Proof

The first identity follows by integrating

$$\frac{d}{dt}P_t(F-\Pi F) =-L_\Phi P_t(F-\Pi F)$$

and using convergence to the invariant mean. For the derivative estimate, integrate the established semigroup bound:

$$\begin{aligned} \|D_e\mathcal R F\|_\infty &\le \int_0^\infty e^{-\lambda_\mu t-\mu d(e,X)} \sum_{g\in X}\|D_gF\|_\infty\,dt\\ &= \frac{e^{-\mu d(e,X)}}{\lambda_\mu} \sum_{g\in X}\|D_gF\|_\infty. \end{aligned}$$

The number of links at distance $r$ from a fixed link is bounded by $24^r$. The resulting geometric sum gives (32) and (33). $\square$

Interpretation. The inverse of the dressed operator on mean-zero functions does not destroy locality. It turns a local observable into a quasi-local one with an exponentially decaying derivative tail. The bound is independent of source volume.

## 5. Resolvent formulation of the interacting vacuum

Write the transformed Hamiltonian, after subtracting the constant $\sum_f E_f$, as

$$H_{\mathrm{dress}}=L_\Phi-V, \qquad V=\sum_eR_e.$$

For a finite source graph, introduce formal source variables $t_e$ and set

$$V(\mathbf t)=\sum_e t_eR_e.$$

Let $E(\mathbf t)$ be the eigenvalue emerging from zero and normalize its eigenfunction as

$$\psi(\mathbf t)=1+u(\mathbf t), \qquad \Pi u(\mathbf t)=0.$$

The eigenvalue equation gives the exact coupled identities

$$\boxed{ E(\mathbf t) =-\Pi\!\left[V(\mathbf t)(1+u(\mathbf t))\right], } \tag{34}$$

and

$$\boxed{ u(\mathbf t) = \mathcal R\!\left[ V(\mathbf t)(1+u(\mathbf t)) +E(\mathbf t)u(\mathbf t) \right]. } \tag{35}$$

These identities are exact as formal perturbation equations. They do not assume that the total norm of $V$ is small independently of volume.

They expose the useful structure:

* Each occurrence of $R_e$ is a local insertion.
* Each application of $\mathcal R$ creates a quasi-local propagation with the decay in (31).
* The projection implicit in $\mathcal R$ removes the constant component, which is the algebraic mechanism behind disconnected-term cancellation.
* The scalar $E(\mathbf t)$ couples branches in the recursive expansion.

Thus the connected expansion can be sought directly in the recursion (34)–(35), rather than reconstructed from the full set of classical path cumulants.

## 6. Exact coefficient recursion

The formal equations also give a useful finite-volume recursion. For a set $I$ of distinct source labels, let $u_I$ and $E_I$ denote the coefficients of $\prod_{i\in I}t_i$ in $u$ and $E$. With $u_\varnothing=1$,

$$E_I=-\sum_{i\in I}\pi_\Phi(R_i u_{I\setminus\{i\}}), \tag{36}$$

and

$$\boxed{ u_I= \mathcal R\left[ \sum_{i\in I}R_i u_{I\setminus\{i\}} + \sum_{\varnothing\ne J\subsetneq I} E_J u_{I\setminus J} \right]. } \tag{37}$$

These identities follow by comparing square-free coefficients in (34)–(35). They are exact, and they provide an algorithm for generating every finite-order coefficient without diagonalizing the full interacting Hamiltonian.

### Second-order connected coefficient

For two distinct residual labels $i,j$,

$$u_i=\mathcal R R_i$$

and

$$\boxed{ E_{\{i,j\}} = -\pi_\Phi(R_i\mathcal R R_j) -\pi_\Phi(R_j\mathcal R R_i). } \tag{38}$$

Since $\mathcal R$ is self-adjoint, the two terms agree. Furthermore,

$$\pi_\Phi(R_i\mathcal R R_j) = \int_0^\infty \operatorname{Cov}_{\pi_\Phi}(R_i,P_tR_j)\,dt.$$

Applying the Poincaré covariance inequality and the spatial semigroup estimate gives

$$\boxed{ |E_{\{i,j\}}| \le \frac{2e^{-\mu d_{\mathcal G}(S_i,S_j)}} {\kappa_*\lambda_\mu} \left(\sum_{h\in S_i}\|D_hR_i\|_\infty\right) \left(\sum_{g\in S_j}\|D_gR_j\|_\infty\right). } \tag{39}$$

This is the first explicit resolvent-tree estimate: the second-order coefficient has a single connection between the two residual supports, and its weight decays exponentially with their separation.

## 7. The higher-order tree lemma now has a precise formulation

The recursion (36)–(37) generates nested products and reduced resolvents. The desired induction must show that, after the scalar energy terms $E_J$ cancel disconnected contributions, each surviving coefficient is controlled by a connected rooted tree of resolvent connections.

The target is

$$\boxed{ |E_I| \le C_*^{|I|}R_*^{|I|} \sum_{T\in\mathcal T(I)} \prod_{\{i,j\}\in T} e^{-\nu' d_{\mathcal G}(S_i,S_j)} } \tag{40}$$

for some $0<\nu'<\mu$, with $C_*$ independent of source volume and $|I|$.

There are two distinct tasks in proving (40):

1. Algebraic cancellation: show that terms whose resolvent connections fail to connect all source labels cancel in (36)–(37).
2. Analytic propagation: bound every surviving resolvent connection using (31)–(33), retaining its individual spatial decay factor.

The first task is not automatic from the fact that $\mathcal R$ is mean-zero. The second task is not automatic from the one-resolvent estimate either: products can create overlapping quasi-local tails. Both must be tracked in the same induction.

### Current result and remaining boundary

|   Result   |   Status   |
| --- | --- |
|   Reduced-resolvent identity   |   Established   |
|   Uniform spatial quasi-locality of $\mathcal R$   |   Established   |
|   Exact finite-volume eigenvalue coefficient recursion   |   Established   |
|   Second-order connected resolvent estimate   |   Established   |
|   Higher-order disconnected-term cancellation in the recursion   |   Open   |
|   Uniform rooted-tree estimate (40)   |   Open   |
|   Source-volume-uniform all-orders activity   |   Open   |

The next concrete proof is therefore an induction on the source set $I$ in (36)–(37), with an explicit decomposition into connected and disconnected resolvent diagrams. The second-order case (38)–(39) is its base case.

The key advance is that the problem now has an exact algebraic object to analyze: the coefficient recursion for the dressed ground-state eigenvalue. This replaces the earlier attempt to extract a tree theorem from a single temporal mixing estimate. It does not yet establish the higher-order tree bound, but it gives a finite-volume identity and a volume-uniform analytic estimate for each individual resolvent edge.

* * *

**You:**

Continue with the next proof.

* * *

**ChatGPT:**

The next coefficient can now be proved explicitly: the third-order mixed ground-state coefficient has an exact six-term reduced-resolvent formula and a source-volume-independent bound. This is the first nontrivial test of whether the recursion can be controlled without a global operator-norm estimate.

I will keep the distinction important here: this proves a uniform third-order estimate, but not yet the spatial spanning-tree estimate at arbitrary order.

## 1. Center the residual insertions

Write

$$r_e=R_e-\pi_\Phi(R_e),\qquad G=L_\Phi^{-1}(1-\Pi),$$

where $G$ is the reduced resolvent and $\Pi F=\pi_\Phi(F)$.

Replacing $R_e$ by $r_e$ subtracts only the scalar

$$\sum_e t_e\pi_\Phi(R_e)$$

from the perturbed Hamiltonian. Therefore every mixed energy coefficient involving at least two distinct source labels is unchanged.

The advantage is

$$\pi_\Phi(r_e)=0,\qquad E_{\{e\}}=0.$$

For three distinct labels $i,j,k$, the exact recursion consequently reduces to

$$u_i=Gr_i,$$

$$u_{ij}=G(r_iGr_j+r_jGr_i),$$

and

$$E_{\{i,j,k\}} =-\pi_\Phi(r_i u_{jk}+r_j u_{ik}+r_k u_{ij}).$$

Substituting the second-order eigenfunction coefficients gives the exact identity

$$\boxed{ E_{\{i,j,k\}} = -\sum_{\sigma\in S_3} \pi_\Phi\!\left[ r_{\sigma(1)} G\!\left(r_{\sigma(2)}Gr_{\sigma(3)}\right) \right]. } \tag{41}$$

There are six terms, one for each ordering of the three residual insertions. This is the third-order connected resolvent expression; the first-order scalar pieces have disappeared through centering.

## 2. A uniform bound on one reduced-resolvent insertion

Let

$$M_e=\sum_{h\in S_e}\|D_hr_e\|_\infty, \qquad D_h=\sqrt{a_h}\nabla_h.$$

Use the spatial semigroup estimate with $\mu=\log25$, for which

$$S_\mu=1+\frac{24}{25-24}=25.$$

Then

$$\sum_h\|D_hGr_e\|_\infty \le\frac{25}{\lambda_\mu}M_e. \tag{42}$$

Because $Gr_e$ is centered, its supremum norm is bounded by its oscillation. Varying the link variables one at a time, using the SU(2) factor diameter $2\pi$, gives

$$\begin{aligned} \|Gr_e\|_\infty &\le 2\pi\sum_h\|\nabla_hGr_e\|_\infty\\ &\le \frac{50\pi}{\sqrt{a_0}\lambda_\mu}M_e. \end{aligned} \tag{43}$$

The bound is independent of the number of links: the spatially weighted derivative sum is summable.

## 3. The third-order coefficient theorem

The dressed-reference Poincaré inequality gives

$$\|Gf\|_{L^2(\pi_\Phi)} \le\frac1\kappa\|f-\pi_\Phi(f)\|_{L^2(\pi_\Phi)},$$

where

$$\kappa=\frac{a_0}{2}-2976b_0>0.$$

For any ordering $(i,j,k)$, Cauchy–Schwarz and (43) imply

$$\begin{aligned} &\left| \pi_\Phi\!\left[ r_iG(r_jGr_k) \right]\right|\\ &\quad\le \frac{\|r_i\|_\infty\|r_j\|_\infty}{\kappa} \|Gr_k\|_\infty\\ &\quad\le \frac{50\pi}{\kappa\sqrt{a_0}\lambda_\mu} \|r_i\|_\infty\|r_j\|_\infty M_k. \end{aligned}$$

Summing the six terms in (41) proves

$$\boxed{ |E_{\{i,j,k\}}| \le \frac{50\pi}{\kappa\sqrt{a_0}\lambda_\mu} \sum_{\sigma\in S_3} \|r_{\sigma(1)}\|_\infty \|r_{\sigma(2)}\|_\infty M_{\sigma(3)}. } \tag{44}$$

This is a genuine volume-uniform third-order coefficient estimate. It uses the reduced-resolvent spectral bound and the spatially summable derivative tail, rather than the norm of the extensive potential $\sum_eR_e$.

Substituting the established residual bounds,

$$R_* =1040\,\frac{b_0^2}{a_0}, \qquad \|r_e\|_\infty\le2R_*, \qquad M_e\le1\,872\,000\,\frac{b_0^2}{\sqrt{a_0}},$$

into (44) yields the explicit uniform estimate

$$\boxed{ |E_{\{i,j,k\}}| \le \frac{1.527\times10^{16}\,b_0^6} {a_0^3\kappa\lambda_\mu}. } \tag{45}$$

For $\mu=\log25$,

$$\lambda_\mu=\frac{a_0}{2}-46752b_0, \qquad \kappa=\frac{a_0}{2}-2976b_0.$$

Both are positive under $b_0/a_0<1/93504$. The large numerical prefactor is a conservative consequence of the preceding norm estimates, not an optimized constant.

## 4. What this proves—and what it does not

|   Third-order property   |   Status   |
| --- | --- |
|   Exact six-term resolvent identity   |   Proved   |
|   Cancellation of first-order scalar contributions   |   Proved   |
|   Source-volume-independent coefficient bound   |   Proved   |
|   Quadratic residual order propagated to cubic order   |   Proved   |
|   Exponential spanning-tree decay in the three support locations   |   Not proved   |

The last distinction is essential. Equation (45) controls the size of the third-order coefficient, but does not show that it becomes small when the three residual supports are mutually far apart. The second-order estimate has that spatial decay; the third-order estimate does not yet inherit a two-edge tree factor.

## 5. Next induction step: fourth order

The centered recursion gives an exact expression without needing a new perturbation argument:

$$\begin{aligned} u_{ijk}=G\big[& r_iG(r_jGr_k+r_kGr_j)\\ &+r_jG(r_iGr_k+r_kGr_i)\\ &+r_kG(r_iGr_j+r_jGr_i)\\ &+E_{ij}Gr_k+E_{ik}Gr_j+E_{jk}Gr_i \big], \end{aligned} \tag{46}$$

and

$$\boxed{ E_{\{i,j,k,l\}} =-\sum_{m\in\{i,j,k,l\}} \pi_\Phi(r_m u_{\{i,j,k,l\}\setminus\{m\}}). } \tag{47}$$

The pair-energy terms in (46) are precisely the subtraction terms that remove disconnected pair contributions. This is the first order at which the recursion explicitly mixes a three-insertion chain with a pair-energy times a one-insertion branch.

The next proof obligation is to establish that this subtraction leaves only connected resolvent diagrams, and then bound their spatial weights. I would not infer that cancellation merely from (46): it must be demonstrated by expanding (47), grouping terms by partitions, and verifying the disconnected cancellations.

Current conclusion: third-order volume-uniform control is now available. The all-orders theorem remains open, and the decisive next test is the fourth-order partition cancellation with spatial weights retained.

* * *

**You:**

Before we proceed to the fourth-order partition cancellation, please update the Singular-Boundary repository, including the observatory - the theorem index and atlas. Did the proof gates change with the introduction of the Penrose-Fibonacci groundwork?

* * *

**ChatGPT:**

Yes—the proof gates have changed in their structure, but the ultimate certification gates have not been discharged.

The Penrose–Fibonacci work adds a substantive, source-grounded geometric and finite-graph research track. It gives us a more precise route from the five coupled lattice directions to accepted-face incidence, local interactions, and a candidate quantum Poincaré mechanism. It does not yet certify the physical three-dimensional regulator, the refinement limit, or the continuum mass gap.

I’ll update the repository as a distinct PF-I16 research pathway, while keeping its status separate from the main Yang–Mills certification gates. The Observatory’s theorem index and atlas should show both the new results and the remaining dependencies—not make the new pathway look like a completed continuum proof.

## Repository update

Committed to PF-I16 review branch

I updated `audit/pf-i16-observatory-2026-11-09` and opened [draft PR #104](https://github.com/syncgravity/Singular-Boundary/pull/104?utm_source=chatgpt.com).

The update includes:

* Three new theorem records: the incidence correction, exact single-face dressing/shared-link residual, and centered third-order dressed-resolvent coefficient.
* An updated [current theorem index](https://github.com/syncgravity/Singular-Boundary/blob/audit/pf-i16-observatory-2026-11-09/docs/research/THEOREM_INDEX_CURRENT.md?utm_source=chatgpt.com).
* [Observatory v2.70](https://github.com/syncgravity/Singular-Boundary/blob/audit/pf-i16-observatory-2026-11-09/observatory/README.md?utm_source=chatgpt.com), with 282 curated nodes and 670 typed relationships.
* Updated interactive [Proof Atlas](https://github.com/syncgravity/Singular-Boundary/blob/audit/pf-i16-observatory-2026-11-09/observatory/graph.html?utm_source=chatgpt.com) and Penrose–Fibonacci research map.
* Updated proof dependencies and structural verification scripts.

The theorem registry now contains 758 source paths, with the historical 740-record baseline preserved. Readback checks confirmed unique index links, matching source hashes and byte counts for the new records, synchronized catalog and graph payloads, and all canonical gates still open.

Merge status: PR #104 is draft and not yet mergeable. The branch is 65 commits ahead and one behind `main`; I have not merged it or deployed GitHub Pages. The full Python verification scripts have been updated, but not executed in a complete local checkout.

## Did the proof gates change?

The acceptance gates did not change. The proof route became more detailed.

The canonical P0–P5 gates and the Penrose-specific PF-G0–G5 gates remain open. The new groundwork gives us a more precise internal sequence:

|   Area   |   What the Penrose–Fibonacci work now contributes   |   What remains open   |
| --- | --- | --- |
|   P0 / PF-G0–G1: geometry   |   Accepted-rhombus incidence and locality bounds   |   Source/operator identity and a genuine refining physical 3D regulator   |
|   P1 / PF-G2: gauge operator   |   Exact finite-graph SU(2) dressing identity   |   Source-derived physical kinetic coefficients, time, and physical Hamiltonian   |
|   P2 / PF-G3–G4: interaction   |   Shared-link residual reduction and exact third-order recursion   |   Fourth-order cancellation, spatial tree bounds, all-orders summability   |
|   P3–P5 / PF-G5: continuum   |   A more explicit candidate route to local interacting control   |   Physical vacuum, infrared spectrum, continuum reconstruction, positive physical mass gap   |

The new PF-I16 sub-sequence is now explicit:

1. Incidence: the universal bound is $d_e\le8$, giving face-overlap degree $D\le28$ and rooted connected-support count $784^{k-1}$. The sharper $D\le4$ remains evidence from eight finite crops only.
2. Dressing: the exact finite-graph conjugation absorbs isolated-face insertions and leaves a residual on shared links, with support at most 25 links.
3. Third order: the centered coefficient has an exact six-permutation resolvent formula. Its numerical volume-uniform bound remains conditional on the working analytic estimates and does not yet have spatial tree decay.
4. Fourth order: disconnected set-partition cancellation is the next explicit proof obligation.
5. All orders: a volume-independent connected-activity majorant is still required.

That distinction matters: the Penrose–Fibonacci work is no longer just a geometric alternative or a collection of finite spectral observations. It now supports a concrete local-interaction proof strategy. But it has not yet supplied the estimates that would turn that strategy into a continuum theorem.

My recommended next step is the fourth-order calculation: expand the exact recursion, enumerate the partition terms, and establish disconnected cancellation term by term before attempting a general tree bound. I can proceed with that proof and record its result against the new Observatory nodes.

* * *

**You:**

Thank you, please continue the fourth-order calculation.

* * *

**ChatGPT:**

# PF-I16 — Fourth-order mixed coefficient

We can now carry the centered reduced-resolvent recursion one order further. The important distinction at this stage is between:

1. Exact algebraic cancellation when the perturbed operator truly factorizes into independent subsystems; and
2. Spatial connectedness on a connected Penrose–Fibonacci graph, where distant supports can still communicate through the background generator. There, cancellation is not exact zero; it must be replaced by a quantitative connected-correlation or tree-decay estimate.

I will keep those two statements separate.

## 1. Fourth-order coefficient: exact expansion

Let $\pi=\pi_\Phi$, let $L=L_\Phi$, and let $G=L^{-1}(1-\Pi)$ be the centered reduced resolvent. For four distinct residual labels $i,j,k,l$, write

$$r_i=R_i-\pi(R_i),\qquad A_i=Gr_i.$$

The second-order eigenfunction and energy coefficients are

$$u_{ij}=B_{ij}:=G(r_iA_j+r_jA_i),$$

$$E_{ij}=-\pi(r_iA_j+r_jA_i).$$

The third-order eigenfunction coefficient is

$$u_{ijk} = G\left[ r_iB_{jk}+r_jB_{ik}+r_kB_{ij} +E_{ij}A_k+E_{ik}A_j+E_{jk}A_i \right].$$

The fourth-order energy coefficient is therefore exactly

$$\boxed{ E_{ijkl} =-\sum_{m\in\{i,j,k,l\}}\pi\!\left(r_m u_{\{i,j,k,l\}\setminus\{m\}}\right). }$$

Using self-adjointness of $G$, this becomes the more useful explicit expression

$$\boxed{ \begin{aligned} E_{ijkl} ={}&-\sum_{m\in I}\ \sum_{a\in I\setminus\{m\}} \pi\!\left[ A_m r_a B_{I\setminus\{m,a\}} \right]\\ &-\sum_{m\in I}\ \sum_{\substack{\{a,b\}\subset I\setminus\{m\}\\ \{c\}=I\setminus\{m,a,b\}}} E_{ab}\,\pi(A_mA_c), \end{aligned} } \tag{4.1}$$

where $I=\{i,j,k,l\}$.

This is the fourth-order formula before any connectedness estimate. It contains 24 nested-resolvent contributions in the first line and 12 pair-energy contributions in the second. It is an exact identity, not an asymptotic approximation.

## 2. The nontrivial $2+2$ partition

This is the most informative fourth-order disconnected case. Suppose, as an explicit factorization hypothesis, that the full dressed system splits into two independent subsystems:

$$L=L_A\otimes 1+1\otimes L_B,\qquad \pi=\pi_A\otimes\pi_B,$$

with $r_i,r_j$ acting only on subsystem $A$, and $r_k,r_l$ only on subsystem $B$.

Use superscripts to denote the component resolvents and coefficients:

$$A_i^A=G_A r_i,\quad B_{ij}^A=G_A(r_iA_j^A+r_jA_i^A),$$

and analogously for $B$.

Because the two subsystems are independent, their normalized eigenfunctions multiply. The mixed eigenfunction coefficients are consequently

$$\begin{aligned} u_{ijk}&=B_{ij}^A A_k^B,& u_{ijl}&=B_{ij}^A A_l^B,\\ u_{ikl}&=A_i^A B_{kl}^B,& u_{jkl}&=A_j^A B_{kl}^B,\\ u_{ijkl}&=B_{ij}^A B_{kl}^B. \end{aligned} \tag{4.2}$$

The fourth-order recursion itself confirms the product formula. In fact,

$$\begin{aligned} L(B_{ij}^A B_{kl}^B) ={}&r_i u_{jkl}+r_j u_{ikl} +r_k u_{ijl}+r_l u_{ijk}\\ &+E_{ij}u_{kl}+E_{kl}u_{ij}. \end{aligned} \tag{4.3}$$

The two surviving pair-energy terms are essential: they are precisely the terms that account for the separate second-order energy shifts of the two components. Cross-component pair energies vanish.

Now substitute (4.2) into the fourth-order energy formula:

$$\begin{aligned} E_{ijkl} ={}&-\big[\pi_A(r_iA_j^A)+\pi_A(r_jA_i^A)\big]\pi_B(B_{kl}^B)\\ &-\pi_A(B_{ij}^A) \big[\pi_B(r_kA_l^B)+\pi_B(r_lA_k^B)\big]. \end{aligned}$$

But the reduced resolvent produces centered eigenfunction coefficients:

$$\pi_A(B_{ij}^A)=0,\qquad \pi_B(B_{kl}^B)=0.$$

Therefore

$$\boxed{E_{ijkl}=0\qquad (\,\{i,j\}\mid\{k,l\}\text{ independent}\,).} \tag{4.4}$$

This is the explicit $2+2$ disconnected-partition cancellation. It is not an assumption that the 36 terms in (4.1) individually vanish: the cancellation follows from the full fourth-order recursion, including its pair-energy corrections.

## 3. The other fourth-order partitions

The same tensor-product argument treats the remaining disconnected patterns:

|   Partition of the four labels   |   Factorized fourth-order eigenfunction coefficient   |   Mixed energy   |
| --- | --- | --- |
|   $$1+3$$   |   $$A_i^A u_{jkl}^B$$   |   $$0$$   |
|   $$2+2$$   |   $$B_{ij}^A B_{kl}^B$$   |   $$0$$   |
|   $$1+1+2$$   |   $$A_i^A A_j^B B_{kl}^C$$   |   $$0$$   |
|   $$1+1+1+1$$   |   $$A_i^A A_j^B A_k^C A_l^D$$   |   $$0$$   |

In each case the full eigenfunction is a product of normalized component eigenfunctions, while the eigenvalue is a sum of component eigenvalues. A mixed coefficient involving labels from more than one independent component must therefore vanish.

More generally, this proves the following finite-system statement.

Fourth-order factorization lemma. If the dressed generator, invariant measure, and residual perturbations factor across independent subsystems, then every fourth-order mixed energy coefficient whose four labels meet more than one subsystem is zero.

This is an exact algebraic result.

## 4. Grouping the fourth-order terms by pair partitions

There is a useful further simplification of (4.1). Define

$$Q_{ij}:=r_iA_j+r_jA_i, \qquad B_{ij}=GQ_{ij}.$$

The 24 nested-resolvent terms group into the three pair partitions

$$(ij|kl),\qquad(ik|jl),\qquad(il|jk).$$

For each partition, self-adjointness of $G$ combines the two corresponding terms. The 12 pair-energy terms group into the same three partitions. The result is

$$\boxed{ \begin{aligned} E_{ijkl}=-2\sum_{\{ij|kl\}} \big[ &\pi(Q_{ij}GQ_{kl})\\ &+E_{ij}\pi(A_kA_l) +E_{kl}\pi(A_iA_j) \big]. \end{aligned} } \tag{4.5}$$

The sum is over all three unordered pair partitions of the four labels.

This is the most useful form of the fourth-order identity so far. It separates the coefficient into three pair-partition channels, each containing:

* a nested-resolvent interaction between two pair sources;
* the first pair's energy correction multiplied by the second pair's resolvent covariance;
* the complementary pair's energy correction multiplied by the first pair's resolvent covariance.

Important: the three channels need not vanish individually, even in the independent $2+2$ case. Their total cancellation is guaranteed by the factorization argument above. It would be incorrect to declare each pair-partition channel zero separately.

## 5. What this proves—and what it does not

Exact fourth-order algebra established

We now have:

1. The exact fourth-order recursion.
2. The complete 36-term expansion, organized into three pair-partition channels.
3. The exact disconnected-factorization cancellation for $1+3$, $2+2$, $1+1+2$, and $1+1+1+1$ independent subsystem decompositions.

There is, however, a crucial geometric qualification for PF-I16.

Disjoint residual supports on a connected Penrose–Fibonacci graph do not imply independent subsystems. The dressed generator can transmit dependence through intermediate links and faces. Thus (4.4) is not yet a spatial cluster theorem. On the connected graph, the mixed coefficient can be nonzero even when the four residual supports do not overlap.

The next analytic obligation is to control (4.5) by the geometry of the four supports—ideally by a spanning-tree factor such as

$$\exp\!\left[-\mu\,\ell_{\mathrm{tree}} (S_i,S_j,S_k,S_l)\right],$$

where $\ell_{\mathrm{tree}}$ is the minimum total connection length in the link interaction graph.

That estimate must account for cancellation among the three pair-partition channels. Bounding their absolute values independently would discard precisely the cancellation we need.

Current proof status: fourth-order algebra and exact factorization cancellation are established under the stated hypotheses. Spatial fourth-order tree decay, the all-orders connected-activity bound, and the continuum/gap conclusions remain open.

The next step is to derive a connected four-source estimate from (4.5), retaining the three-channel cancellation rather than taking absolute values prematurely.

* * *

**You:**

Continue with the objective.

* * *

**ChatGPT:**

The next step is to turn the fourth-order cancellation into a spatial connectedness estimate. The key distinction is that the three pairing channels in (4.5) cancel exactly in a factorized system, but on the connected Penrose–Fibonacci graph they need not vanish separately—or vanish at all. We therefore need to measure the failure of factorization, rather than bound the three channels independently.

I’ll formulate that failure through an interpolation that switches on the dressed interactions joining separated source regions. This gives a concrete route to a four-source tree bound while keeping the existing proof gates open.

### 1. Exact cut-interpolation identity

Work first on a finite accepted-rhombus graph. Choose a partition of its link coordinates into $A\sqcup B$, with $S_i,S_j\subset A$ and $S_k,S_l\subset B$. Split the face dressing into

$$\Phi=\Phi_A+\Phi_B+\Phi_\times,$$

where $\Phi_\times$ is the sum of face terms whose boundaries meet both $A$ and $B$. Introduce

$$\Phi_s=\Phi_A+\Phi_B+s\Phi_\times,\qquad 0\le s\le1,$$

and the normalized measure

$$d\mu_s=Z_s^{-1}e^{2\Phi_s}\,d\mu_{\rm Haar}.$$

Let $L_s$ be the corresponding reversible dressed generator. At $s=0$, both the measure and generator factor across $A|B$; at $s=1$, they are the original dressed system.

Use the uncentered residuals $R_m$ in the spectral perturbation

$$L_s-\sum_{m\in\{i,j,k,l\}}t_mR_m.$$

This is legitimate because subtracting a scalar multiple of any $t_m$ changes only the linear energy coefficient, not the mixed fourth-order coefficient. Denote the analytic ground eigenvalue by $\mathcal E_s(\mathbf t)$, and its normalized positive ground eigenfunction by $f_{s,\mathbf t}$, with

$$\pi_s(f_{s,\mathbf t}^{\,2})=1.$$

Set $W=2\Phi_\times$, so that

$$\partial_s d\mu_s=(W-\pi_sW)d\mu_s.$$

The Hellmann–Feynman identity for this varying weighted Dirichlet form is

$$\boxed{ \partial_s\mathcal E_s(\mathbf t) = \pi_s\!\left[ (W-\pi_sW) \left\{ \Gamma(f_{s,\mathbf t},f_{s,\mathbf t}) -\Big(\sum_m t_mR_m\Big)f_{s,\mathbf t}^{\,2} -\mathcal E_s(\mathbf t)f_{s,\mathbf t}^{\,2} \right\} \right]. } \tag{4.6}$$

Here $\Gamma$ is the carré du champ of the link kinetic operator. The subtraction of $\pi_sW$ is important: it accounts for normalization of the changing measure.

At $s=0$, the two subsystems are independent. Since the four source labels occupy both sides, additivity of the ground energy gives

$$[t_it_jt_kt_l]\,\mathcal E_0(\mathbf t)=0.$$

Integrating (4.6) therefore gives the exact identity

$$\boxed{ E_{ijkl} = \int_0^1 [t_it_jt_kt_l]\, \pi_s\!\left[ (W-\pi_sW) \left\{ \Gamma(f_{s,\mathbf t},f_{s,\mathbf t}) -V_{\mathbf t}f_{s,\mathbf t}^{\,2} -\mathcal E_s(\mathbf t)f_{s,\mathbf t}^{\,2} \right\} \right]ds, } \tag{4.7}$$

where $V_{\mathbf t}=\sum_m t_mR_m$.

This is the useful structural result: the mixed fourth-order coefficient is the response to the interactions crossing a cut that separates the source groups. It is not a sum of three independently estimated pairing channels. The exact cancellation in (4.5) is retained because the coefficient is extracted only after the normalized, coupled expression in (4.7) is formed.

### 2. What the spatial estimate must now control

The insertion $W$ is a sum over cross-cut face terms. Each such term is local: it depends only on the links around one accepted rhombus. If the cut is placed between two source regions at link-graph distance $d$, those cross-cut terms lie in a bounded-width layer around the cut. The source-to-layer distance is consequently of order $d/2$, up to the fixed interaction range.

The existing semigroup estimate gives exponential decay for the first derivative of a resolvent response to a local source. That is encouraging, but it does not by itself bound the fourth coefficient in (4.7): extracting four $t$-derivatives produces products of lower-order eigenfunction responses, and the measure $\mu_s$, the centering term $\pi_sW$, and the eigenvalue term all vary with $s$.

So the remaining task is precise:

1. Differentiate the normalized eigenfunction and eigenvalue in (4.7) using the reduced-resolvent recursion.
2. Group the resulting terms before taking absolute values, preserving the normalization and pair-channel cancellations.
3. Bound the resulting cut response by the distance from the source groups to the cross-cut layer.
4. Repeat this across a forest of cuts, rather than just one cut, to obtain decay in the total length of a connecting tree.

### 3. A more direct route: conjugate to a local rotor Hamiltonian

There is a useful alternative to estimating (4.7) directly. The dressed diffusion can be conjugated back to the product Haar space, where its interactions become an ordinary local potential.

Let

$$K=\sum_e a_e(-\Delta_e),\qquad L_\Phi=K-2\Gamma(\Phi,\cdot).$$

Multiplication by $e^\Phi$ is unitary from $L^2(e^{2\Phi}d\mu_{\rm Haar})$ to $L^2(d\mu_{\rm Haar})$. Direct differentiation gives

$$\boxed{ e^\Phi L_\Phi e^{-\Phi} = K+\mathcal U_\Phi,\qquad \mathcal U_\Phi = \sum_e a_e\left[ \Delta_e\Phi+|\nabla_e\Phi|^2 \right]. } \tag{4.8}$$

This identity matters because $K$ is a sum of independent link rotors. All spatial coupling is now in the multiplication potential $\mathcal U_\Phi$.

Writing $\Phi=\sum_f s_f$, define

$$U_e = a_e\left[ \sum_{f:e\in\partial f}\Delta_e s_f + \left|\sum_{f:e\in\partial f}\nabla_e s_f\right|^2 \right].$$

Then

$$\mathcal U_\Phi=\sum_e U_e.$$

Each $U_e$ depends only on links belonging to faces incident to $e$. By $d_e\le8$, its support satisfies

$$|\operatorname{supp}U_e|\le1+3d_e\le25.$$

Thus the dressed generator has become a product-rotor Hamiltonian with finite-range, bounded-support interactions. The residuals $R_i$ are also local multiplication operators, with the same support bound.

This is the structural feature needed for a linked-cluster argument. It is stronger than merely knowing that the dressed measure has a Poincaré inequality: the unperturbed operator $K$ has independent coordinates, and every mechanism that can connect two separated source supports is represented by a chain of overlapping local potential terms.

### 4. The finite-order connected-cluster lemma we need

Let $\mathcal I$ index the local terms $U_e$, and connect $e,h\in\mathcal I$ when their supports overlap. Since each support is contained in the radius-one link neighborhood of its anchor, the overlap graph has bounded degree; a crude bound from link degree $24$ is

$$\Delta_{\mathcal I}\le 24+24\cdot23=576.$$

The four residual supports are four distinguished terminal sets in this graph.

The required lemma is:

> Four-source linked-cluster lemma (to be proved). For the product-rotor operator \[ K+\sum_