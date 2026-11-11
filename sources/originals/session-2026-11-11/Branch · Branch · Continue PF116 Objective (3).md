**You:**

Proceed with the next obligation

* * *

**You:**

Please proceed with the next mathematical step: audit the revised comparison-matrix/Duhamel argument to extract (DF) with explicit constants, then close the two kernel and oscillation checks.

* * *

**ChatGPT:**

# PF-I16 — Derivative-flow audit

The revised comparison-matrix argument does yield a spatially weighted derivative-flow estimate, with an explicit kernel prefactor of one. The key is to retain the nonnegative matrix structure through Duhamel iteration, rather than estimate each derivative component separately and discard the spatial weights.

I will distinguish three things below: the matrix estimate and its consequences, the geometric kernel checks, and the remaining hypotheses needed to call the result a theorem for the Penrose regulator.

## 1. Comparison-matrix estimate

Let $d(e,g)$ be the original-link graph distance, with two links adjacent when they occur in a common accepted face. Write $A=(A_{eg})$ for the nonnegative derivative-coupling comparison matrix. The weighted row norm is

$$\|A\|_\mu =\sup_e\sum_g A_{eg}e^{\mu d(e,g)}.$$

The revised block calculation gives

$$\boxed{ \|A\|_\mu \le \left(\frac{512}{3}+704e^\mu\right)b_0 + \left(\frac{5120}{3}+5120e^\mu\right) \frac{b_0^2}{a_0}. } \tag{1}$$

At $\mu=\log25$, this becomes

$$\boxed{ \|A\|_{\log25} \le \frac{53312}{3}b_0 +\frac{389120}{3}\frac{b_0^2}{a_0}. } \tag{2}$$

The constants in (2) are the exact substitutions $704\cdot25+512/3$ and $5120\cdot25+5120/3$, respectively.

## 2. Duhamel iteration gives (DF)

The required componentwise differential inequality is

$$D^+u_e(t)\le-\frac{a_0}{2}u_e(t) +\sum_g A_{eg}u_g(t), \qquad u_e(t)=\|D_eP_tf\|_\infty. \tag{3}$$

Here $D^+$ is the upper right derivative. The inequality must hold with the same nonnegative matrix $A$ at every configuration and time. This is the Kato/Bochner input; it is not a consequence of the row-norm calculation alone.

Variation of constants and positivity give

$$u(t)\le e^{-a_0t/2}u(0) +\int_0^t e^{-a_0(t-s)/2}A u(s)\,ds,$$

and iteration yields

$$u(t)\le e^{-a_0t/2}e^{tA}u(0). \tag{4}$$

The important point is that the weighted row norm is stable under matrix multiplication. Indeed, the triangle inequality for graph distance gives

$$\begin{aligned} \sum_g(A^2)_{eg}e^{\mu d(e,g)} &=\sum_{z,g}A_{ez}A_{zg}e^{\mu d(e,g)}\\ &\le \sum_{z,g}A_{ez}A_{zg} e^{\mu d(e,z)}e^{\mu d(z,g)}\\ &\le \|A\|_\mu^2. \end{aligned}$$

Induction gives the corresponding $n$-th power bound. Consequently,

$$\sum_g(e^{tA})_{eg}e^{\mu d(e,g)} \le e^{t\|A\|_\mu}.$$

In particular,

$$(e^{tA})_{eg} \le e^{-\mu d(e,g)}e^{t\|A\|_\mu}.$$

Substitution into (4) proves the desired estimate:

$$\boxed{ \|D_eP_tf\|_\infty \le e^{-\lambda t} \sum_g e^{-\mu d(e,g)} \|D_gf\|_\infty, } \tag{DF}$$

where

$$\boxed{ \lambda= \frac{a_0}{2} -\left(\frac{512}{3}+704e^\mu\right)b_0 -\left(\frac{5120}{3}+5120e^\mu\right) \frac{b_0^2}{a_0}. } \tag{5}$$

There is no extra prefactor in (DF). In particular, the coefficient of the spatial kernel is exactly one. This is stronger than a bound obtained by estimating the components independently and then summing.

At $\mu=\log25$,

$$\lambda= \frac{a_0}{2} -\frac{53312}{3}b_0 -\frac{389120}{3}\frac{b_0^2}{a_0}.$$

If $b_0/a_0\le1/40000$, then

$$\boxed{ \lambda\ge \frac{26087}{468750}a_0 >0.0556522\,a_0. } \tag{6}$$

The comparison-matrix contribution at this endpoint is at most

$$\|A\|_{\log25} \le \frac{104144}{234375}a_0 <0.444348\,a_0.$$

Thus the positive decay margin is not marginal: the comparison matrix consumes less than $89\%$ of the available $a_0/2$ damping.

## 3. The two kernel checks

The geometry supplies the needed growth estimate. Each original link belongs to at most eight accepted faces, and each such face has three other boundary links. Therefore the link-dependency graph has maximum degree

$$\Delta\le 8\cdot3=24.$$

The number of links at distance $r\ge1$ from a fixed link is consequently bounded by

$$|S_r(e)|\le24\cdot23^{r-1}. \tag{7}$$

This gives two useful kernel facts.

Kernel check A — row and column summability.

For $K_\mu(e,g)=e^{-\mu d(e,g)}$, at $\mu=\log25$,

$$\begin{aligned} \sup_e\sum_gK_\mu(e,g) &\le1+\sum_{r\ge1}24\cdot23^{r-1}25^{-r}\\ &=1+\frac{24/25}{1-23/25}\\ &=\boxed{13}. \end{aligned}$$

Because the distance is symmetric, the same bound holds for column sums:

$$\boxed{ \sup_e\sum_gK_\mu(e,g) = \sup_g\sum_eK_\mu(e,g) \le13. } \tag{8}$$

This verifies both orientations needed when summing derivative estimates over output links or input links. The bound is independent of strip size.

Kernel check B — convolution with a controlled loss of exponent.

For any

$$0<\nu<\mu-\log23,$$

we have

$$\boxed{ \sum_z K_\mu(e,z)K_\mu(z,g) \le C_{\mu,\nu}K_\nu(e,g), } \tag{9}$$

where one explicit admissible constant is

$$C_{\mu,\nu} = 1+\frac{24e^{-(\mu-\nu)}} {1-23e^{-(\mu-\nu)}}. \tag{10}$$

To see this, put $s=d(e,z)+d(z,g)$ and $d=d(e,g)$. Since $s\ge d$ and $s\ge d(e,z)$,

$$e^{-\mu s} \le e^{-\nu d}e^{-(\mu-\nu)d(e,z)}.$$

Summing over $z$ and applying (7) proves (9)–(10).

For a concrete choice, take

$$\nu=\frac12\log\frac{25}{23}.$$

Then $\mu-\nu=\frac12\log575>\log23$, and

$$C_{\mu,\nu} = 1+\frac{24/(5\sqrt{23})}{1-\sqrt{23}/5} <25.511. \tag{11}$$

So the convolution check closes, but it costs spatial exponent: the composed kernel has exponent $\nu$, not $\mu$. That loss must be retained in any repeated-resolvent or higher-order argument.

## 4. Oscillation check

The link configuration space carries the product of radius-two $SU(2)$ metrics. Each factor has diameter $2\pi$. For two configurations $U,V$, change their link coordinates one at a time along minimizing geodesics. This gives

$$|P_tf(U)-P_tf(V)| \le 2\pi\sum_e\|D_eP_tf\|_\infty. \tag{12}$$

Now suppose $f$ depends only on a finite link set $S$. Its initial derivatives vanish outside $S$, so (DF) gives

$$\begin{aligned} \operatorname{osc}(P_tf) &\le 2\pi e^{-\lambda t} \sum_e\sum_{g\in S} K_\mu(e,g)\|D_gf\|_\infty\\ &\le 2\pi\cdot13\,e^{-\lambda t} \sum_{g\in S}\|D_gf\|_\infty. \end{aligned}$$

Hence

$$\boxed{ \operatorname{osc}(P_tf) \le 26\pi e^{-\lambda t} \sum_{g\in S}\|D_gf\|_\infty. } \tag{13}$$

This is a global oscillation estimate with no factor proportional to the total number of links. It is important that the column-kernel estimate (8) is used here; a row bound alone would not justify this summation.

There is also a useful localized version. If two configurations differ only at link $e$, then

$$\boxed{ \operatorname{osc}_{e}(P_tf) \le 2\pi e^{-\lambda t} \sum_{g\in S}e^{-\mu d(e,g)} \|D_gf\|_\infty. } \tag{14}$$

Thus the same argument gives both temporal decay and spatial decay of the response to a local observable.

## 5. Audit verdict

Algebraically closed, conditionally

|   Obligation   |   Result   |
| --- | --- |
|   Revised weighted comparison-matrix substitution   |   Exact constants in (2)   |
|   Duhamel iteration   |   Closes with kernel prefactor $1$   |
|   Positive derivative-flow rate   |   $0.0556522a_0$ at the stated endpoint   |
|   Kernel row and column sums   |   Both bounded by $13$   |
|   Kernel convolution   |   Closes with exponent loss and constant $<25.511$   |
|   Global oscillation   |   Closes with prefactor $26\pi$   |
|   Uniformity in finite strip length   |   Preserved by all these estimates   |

The remaining qualification is at the input to Duhamel, not in the iteration. To promote (DF) from a conditional estimate to a certified theorem, the pointwise componentwise Kato/Bochner inequality (3) must be independently verified from the dressed generator, including:

1. The sign and size of the diagonal damping $a_0/2$.
2. The off-diagonal Hessian-block domination by the stated nonnegative matrix.
3. The uniformity of that domination over configurations, not merely its validity after integration.

The numerical comparison-matrix arithmetic and the kernel/oscillation arguments do not establish those differential inequalities by themselves.

The appropriate research status is therefore: the comparison-matrix/Duhamel bridge and its two kernel estimates and oscillation consequence are closed under the stated local Kato/Bochner hypothesis; certification of that hypothesis remains the next obligation.

No repository files or theorem statuses have been changed. The result does not establish the interacting $\lambda=1$ gap or the continuum Yang–Mills mass gap.

The next mathematical step is to reconstruct the componentwise Kato/Bochner inequality directly from the refined mixed-Hessian blocks, checking every diagonal and off-diagonal term against the comparison matrix.

* * *

**You:**

Continue this mathematical step

* * *

**ChatGPT:**

The pointwise componentwise Kato–Bochner inequality does close, conditional only on the refined pulled-back face-Hessian estimates already derived. The key is to apply Bochner to the full product gradient, then project onto each link tangent block. The product geometry makes the Ricci term diagonal; all cross-link coupling is carried by the Hessian of $\Phi$.

## 1. Fix the generator and metric conventions

Let the finite configuration manifold be

$$M=\prod_{e\in E}SU(2)_e, \qquad \widetilde g=\bigoplus_{e\in E}a_e^{-1}g_e,$$

where $g_e$ is the radius-two metric. Write

$$\mathscr G=-L_\Phi =\Delta_{\widetilde g} -2\langle\nabla_{\widetilde g}\Phi,\nabla_{\widetilde g}\,\cdot\,\rangle, \qquad P_t=e^{t\mathscr G}.$$

This is the diffusion convention corresponding to the positive operator $L_\Phi$ in the earlier identity.

The product connection preserves the link tangent splitting. Its Ricci endomorphism is block diagonal:

$$\operatorname{Ric}^{\sharp}_{\widetilde g} \big|_{T_eM} =\frac{a_e}{2}I_{T_eM}.$$

Indeed, scaling $g_e$ by $a_e^{-1}$ leaves its Levi-Civita connection unchanged and multiplies the Ricci endomorphism by $a_e$.

For $f_t=P_tf$, put $W=\nabla f_t$, with $W_e$ its $T_eM$ component.

## 2. The exact vector Bochner equation

For the drifted diffusion above, the covariant gradient equation is

$$\left( \partial_t-\Delta_{\widetilde g}^{\nabla} +2\nabla_{\nabla\Phi} \right)W = -\left(\operatorname{Ric}^{\sharp}_{\widetilde g} +2(\nabla^2\Phi)^\sharp\right)W. \tag{1}$$

Here $\Delta^\nabla$ is the connection Laplacian on vector fields. The sign of the Hessian term is important: the drift is $-2\nabla\Phi$, so the Bakry–Émery curvature is

$$\operatorname{Ric}^{\sharp}_{\widetilde g} +2(\nabla^2\Phi)^\sharp.$$

Because this is a product manifold with constant factor weights:

* the Ricci term has no off-diagonal link blocks;
* the product connection has no cross-factor curvature terms;
* differentiating the drift produces precisely the Hessian blocks of $\Phi$.

Thus there is no additional link-mixing commutator to add to (1). The noncommutativity of the four-factor face holonomy has already entered through the $\nabla dH_f$ term in the refined pulled-back Hessian.

## 3. Project onto one link and apply Kato

Define

$$u_e(t,x)=|W_e(t,x)|_{g_e}.$$

The connection Laplacian in (1) preserves the $T_eM$ bundle. Kato's inequality gives, wherever $u_e>0$,

$$\begin{aligned} (\partial_t-\mathscr G)u_e &\le -\frac{a_e}{2}u_e -2\left\langle \sum_g(\nabla^2\Phi)_{eg}W_g, \frac{W_e}{|W_e|} \right\rangle\\ &\le -\frac{a_0}{2}u_e +2\sum_g \big\|(\nabla^2\Phi)_{eg}\big\|_{\mathrm{op}}u_g, \end{aligned} \tag{2}$$

using $a_e\ge a_0$.

At zeros of $W_e$, this inequality holds in the upper-Dini or viscosity sense. One way to justify that extension is to apply the smooth Kato argument to

$$u_{e,\varepsilon}=(|W_e|^2+\varepsilon^2)^{1/2}$$

and pass to $\varepsilon\downarrow0$.

Now define the configuration-supremum components

$$U_e(t)=\sup_{x\in M}u_e(t,x).$$

The manifold is compact because the graph is finite. At a spatial maximum of $u_e$, the scalar diffusion satisfies

$$\mathscr G u_e\le0.$$

Taking the upper right Dini derivative of the supremum in (2) therefore yields

$$D^+U_e(t) \le -\frac{a_0}{2}U_e(t) +\sum_g A_{eg}U_g(t), \tag{3}$$

where the configuration-independent nonnegative matrix is

$$\boxed{ A_{eg} = 2\sup_{x\in M} \big\|(\nabla^2\Phi(x))_{eg}\big\|_{\mathrm{op}}. } \tag{4}$$

This is the required pointwise-to-supremum step. In particular, it does not infer a pointwise estimate from an integrated Bochner inequality.

## 4. Dominate the matrix using the refined face blocks

Since $\Phi=\sum_f s_f\circ H_f$, its Hessian blocks are sums of the face Hessian blocks. Define

$$h_{\rm d} =\frac{32}{3}b_0+\frac{320}{3}\frac{b_0^2}{a_0}, \qquad h_{\rm o} =\frac{44}{3}b_0+\frac{320}{3}\frac{b_0^2}{a_0}.$$

The refined estimates give

$$\big\|(\nabla^2(s_f\circ H_f))_{ee}\big\|_{\rm op} \le h_{\rm d},$$

and, for distinct links $e,g$ in the same face,

$$\big\|(\nabla^2(s_f\circ H_f))_{eg}\big\|_{\rm op} \le h_{\rm o}.$$

Set

$$A_{ee}=2\sum_{f\ni e}h_{\rm d}, \qquad A_{eg}=2\sum_{f:\,e,g\in\partial f}h_{\rm o} \quad(e\ne g). \tag{5}$$

This explicitly dominates (4), and it is independent of the configuration.

Each link belongs to at most eight accepted faces. Each such face contains three other links, all adjacent to $e$ in the link-overlap graph. Consequently, for $\mu>0$,

$$\begin{aligned} \sum_g A_{eg}e^{\mu d(e,g)} &\le 16\big(h_{\rm d}+3e^\mu h_{\rm o}\big)\\ &= \left(\frac{512}{3}+704e^\mu\right)b_0\\ &\quad+ \left(\frac{5120}{3}+5120e^\mu\right) \frac{b_0^2}{a_0}. \end{aligned} \tag{6}$$

At $\mu=\log25$, this is exactly

$$\boxed{ \|A\|_{\log25} \le \frac{53312}{3}b_0 +\frac{389120}{3}\frac{b_0^2}{a_0}. } \tag{7}$$

The counting includes diagonal blocks and all three off-diagonal blocks per incident face. No factor of two is missing: the factor $2$ from the drift Hessian is already included in (5).

## 5. Consequence: the derivative-flow estimate is now unconditional relative to the stated hypotheses

Equation (3) is a finite-dimensional cooperative differential inequality. Componentwise comparison gives

$$U(t) \le e^{-a_0t/2}e^{tA}U(0). \tag{8}$$

For the weighted row norm, the triangle inequality for graph distance gives

$$\sum_g(A^n)_{eg}e^{\mu d(e,g)} \le \|A\|_\mu^n.$$

Applying this to (8), and using $U_g(0)=\|D_gf\|_\infty$, yields

$$\begin{aligned} \|D_eP_tf\|_\infty &\le e^{-a_0t/2} \sum_g(e^{tA})_{eg}\|D_gf\|_\infty\\ &\le e^{-\lambda t} \sum_g e^{-\mu d(e,g)}\|D_gf\|_\infty, \end{aligned}$$

where

$$\boxed{ \lambda= \frac{a_0}{2} -\frac{53312}{3}b_0 -\frac{389120}{3}\frac{b_0^2}{a_0}. }$$

Thus the previously stated derivative-flow estimate (DF) follows from the refined Hessian bounds and the finite-product diffusion calculation.

At $b_0/a_0\le1/40000$,

$$\lambda\ge \frac{26087}{468750}a_0 >0.0556522a_0.$$

## 6. What this closes—and what it does not

Closed, conditional on refined face-Hessian bounds

The missing componentwise Kato–Bochner bridge is now supplied:

1. The diagonal Ricci damping is $a_e/2\ge a_0/2$.
2. The Hessian of $\Phi$ supplies all diagonal and off-diagonal coupling.
3. The nonnegative comparison matrix has the exact weighted row bound in (7).
4. The inequality is uniform over configurations on every finite graph satisfying the stated incidence and coefficient bounds.
5. The Duhamel derivative-flow estimate follows with kernel prefactor one.

The remaining qualifications are important. This argument assumes the refined face-Hessian estimates, including the four-factor mixed covariant Hessian calculation, are valid as stated. It establishes a finite-graph semigroup estimate; it does not establish the canonical Penrose gates, a continuum limit, all-orders summability, or a Yang–Mills mass gap.

The next useful mathematical step is to write this as a self-contained lemma with all sign conventions and regularization details, then independently audit the four-factor mixed-Hessian estimates feeding $$h_{\rm d}$$ and $$h_{\rm o}$$.

* * *

**You:**

Before we proceed to write this as a self-contained lemma with all sign conventions and regularization details, please update the Singular-Boundary repository, including the observatory - its theorem index map and atlases. Then merge the draft PR into main.

* * *

**ChatGPT:**

I checked PR #104 against the live repository before making changes. There is an important integration issue: the draft branch is 96 commits ahead but one commit behind `main`, and GitHub currently reports it as non-mergeable (`dirty`). Its latest head also has no reported Actions runs or status checks.

I will not force-merge that state or manufacture a merge commit that silently drops the newer `main` commit. The safe path is to reconcile the branch with `main`, add the new Kato–Bochner result and synchronized Observatory records, verify the resulting tree, and then merge only if GitHub accepts the reconciled PR.

The repository update is now committed on the PR branch as `abd61801066def217379b9960c035950af17fc5f`, with `main` and the prior draft head both retained as parents. The new Observatory edition is v2.72: 760 indexed theorem sources, 284 Atlas nodes, and 675 typed relationships.

The update records the componentwise Kato–Bochner/Duhamel bridge as conditional on the refined face-Hessian hypotheses, adds the four-factor working derivation and its remaining audit obligation, and replaces the superseded third-order numerical bound. The historical 740-source baseline and all canonical open-gate statuses are preserved.

The reconciled PR is now non-draft and GitHub reports it as mergeable, but I am holding the merge because its first Actions run failed in the theorem-source inventory verifier. The failure occurred before the catalog and Atlas checks ran. I’m tracing that inventory assertion and will correct it rather than bypassing the check.The verifier issues are corrected. The latest Actions run now passes all five substantive checks: theorem inventory and Git blob hashes, generated catalog/current navigator, curated graph, Observatory JavaScript syntax, and maintenance-script syntax. GitHub also reports PR #104 as clean and fully up to date with `main`.

Merged into `main`

PR #104 is closed and merged. The merge commit is [`346166f27994bb4ccd8cd69d10c77cdec75254fa`](https://github.com/syncgravity/Singular-Boundary/commit/346166f27994bb4ccd8cd69d10c77cdec75254fa?utm_source=chatgpt.com).

The final `main` Actions run passed, including:

* All 760 theorem-source hashes and inventory links.
* Generated theorem catalog and current navigator synchronization.
* Curated Proof Atlas graph verification.
* Observatory JavaScript syntax checks.
* Repository maintenance-script syntax check.

Updated repository records

* [Pointwise Kato–Bochner theorem record](https://github.com/syncgravity/Singular-Boundary/blob/main/research/theorems/PF_I16_POINTWISE_KATO_BOCHNER_DERIVATIVE_FLOW_2026_11_10.md?utm_source=chatgpt.com)
* [Current theorem navigator](https://github.com/syncgravity/Singular-Boundary/blob/main/docs/research/THEOREM_INDEX_CURRENT.md?utm_source=chatgpt.com)
* [Interactive Proof Atlas](https://github.com/syncgravity/Singular-Boundary/blob/main/observatory/graph.html?utm_source=chatgpt.com)
* [Penrose program overview](https://github.com/syncgravity/Singular-Boundary/blob/main/observatory/penrose-program.html?utm_source=chatgpt.com)

The Observatory source and atlas assets are merged into the repository. I have not independently confirmed a separate GitHub Pages deployment.

Mathematical status remains carefully scoped: the derivative-flow result is conditional on the refined face-Hessian estimates. The standalone four-factor sign, trivialization, and regularization audit remains open. Fourth-order cancellation, spatial tree decay, all-orders summability, continuum reconstruction, and the Yang–Mills mass gap remain unproved. No canonical proof gate was promoted.

We can now proceed to the self-contained lemma against the merged theorem record.

* * *

**You:**

Proceed to this task

* * *

**ChatGPT:**

The four-factor calculation can be made self-contained. I have independently checked the orientation conversion, the transported Maurer–Cartan derivatives, the target Levi-Civita connection, the metric scaling, and the pointwise Kato regularization.

There is one normalization detail worth making explicit: the derivative in the final estimate must be measured in the scaled product metric. In terms of the unscaled link derivative, this introduces a factor $\sqrt{a_e}$. I incorporate that explicitly below rather than leave the convention implicit.

# PF-I16 — Four-factor holonomy Hessian and pointwise Kato–Bochner lemma

Finite-product differential identities established

Conditional on rotor estimates

## 1. Geometric setting and conventions

Let $E$ be a finite set of links and let

$$M=\prod_{e\in E}\mathrm{SU}(2)_e.$$

Each factor carries the radius-two bi-invariant metric $g_e$, and the product is equipped with

$$\widetilde g=\bigoplus_{e\in E}a_e^{-1}g_e, \qquad a_e\ge a_0>0.$$

Our Laplacian convention is

$$\Delta=\operatorname{div}\nabla,$$

so that its spectrum on a compact manifold is nonpositive. The product Levi-Civita connection is denoted by $\nabla$.

The radius-two metric has

$$\operatorname{Ric}_{g_e}=\frac12g_e.$$

Constant scaling does not change the Levi-Civita connection. It scales the Ricci endomorphism by $a_e$, so

$$\operatorname{Ric}^{\sharp}_{\widetilde g}|_{T_eM} =\frac{a_e}{2}I \ge \frac{a_0}{2}I. \tag{1}$$

The dressed potential is

$$\Phi=\sum_f s_f\circ H_f,$$

where each accepted face has four oriented link factors.

Define the Markov generator

$$\mathscr G = \Delta_{\widetilde g} -2\nabla_{\nabla\Phi}, \qquad P_t=e^{t\mathscr G}. \tag{2}$$

Equivalently,

$$L_\Phi=-\mathscr G = -\Delta_{\widetilde g} +2\langle\nabla\Phi,\nabla\,\cdot\,\rangle.$$

The sign of the drift in (2) determines the sign of the Hessian contribution below.

## 2. Four-factor mixed covariant derivative

Lemma 1 — Oriented four-factor holonomy Hessian.

Let

$$H=x_1x_2x_3x_4, \qquad x_i=U_i^{\epsilon_i}, \qquad \epsilon_i\in\{-1,+1\}.$$

Use original-link left-trivialized tangent vectors

$$\dot U_i=U_i\xi_i.$$

Write the corresponding face-factor variation as

$$\dot x_i=x_iX_i.$$

Then

$$X_i= \begin{cases} \xi_i,&\epsilon_i=+1,\\[2mm] -\operatorname{Ad}_{U_i}\xi_i,&\epsilon_i=-1, \end{cases} \tag{3}$$

or, equivalently,

$$X_i= \epsilon_i \operatorname{Ad}_{U_i^{(1-\epsilon_i)/2}}\xi_i.$$

In particular,

$$|X_i|_{g_i}=|\xi_i|_{g_i}. \tag{4}$$

Define

$$T_i=x_{i+1}\cdots x_4,\qquad T_4=1,$$

and

$$\eta_i=\operatorname{Ad}_{T_i^{-1}}X_i. \tag{5}$$

Then

$$H^{-1}\dot H=\sum_{i=1}^4\eta_i. \tag{6}$$

For variations supported on distinct factors $i,j$, the mixed covariant derivative is

$$\boxed{ (\nabla dH)(X_i,Y_j) = \begin{cases} \displaystyle \frac12[\eta_i(X_i),\eta_j(Y_j)],&i<j,\\[2mm] \displaystyle -\frac12[\eta_i(X_i),\eta_j(Y_j)],&i>j. \end{cases}} \tag{7}$$

For a variation supported on a single factor,

$$\boxed{(\nabla dH)(X_i,Y_i)=0.} \tag{8}$$

Proof.

For positive orientation, $x_i=U_i$, and (3) follows immediately from $\dot U_i=U_i\xi_i$.

For negative orientation,

$$\frac{d}{dt}U_i^{-1} =-U_i^{-1}\dot U_iU_i^{-1} =-\xi_iU_i^{-1}.$$

Since $x_i=U_i^{-1}$, writing this as $x_iX_i$ gives

$$X_i=-U_i\xi_iU_i^{-1} =-\operatorname{Ad}_{U_i}\xi_i.$$

This establishes (3) and (4).

Differentiating the product $H$ gives

$$H^{-1}\dot H = \sum_i \operatorname{Ad}_{T_i^{-1}}X_i,$$

which proves (6).

Now consider the derivative of $\eta_j$ with respect to a distinct factor $i$.

If $i<j$, the product $T_j$ does not contain $x_i$. Thus

$$D_i\eta_j=0. \tag{9}$$

If $i>j$, write

$$T_j=P x_i S,\qquad S=T_i.$$

Under $x_i(t)=x_i\exp(tX_i)$,

$$T_j(t) = T_j\exp\!\left(t\operatorname{Ad}_{S^{-1}}X_i\right) = T_j\exp(t\eta_i).$$

Consequently,

$$\begin{aligned} \eta_j(t) &=\operatorname{Ad}_{T_j(t)^{-1}}X_j\\ &=\operatorname{Ad}_{\exp(-t\eta_i)}\eta_j, \end{aligned}$$

and therefore

$$D_i\eta_j=-[\eta_i,\eta_j]. \tag{10}$$

For a bi-invariant metric, the target Levi-Civita connection in left trivialization is

$$(\nabla_{\dot H}W)_{\mathrm{left}} = D_{\dot H}w+\frac12[\eta,w], \qquad \eta=H^{-1}\dot H. \tag{11}$$

Combining (9)–(11) yields (7).

For (8), when only $U_i$ varies, the map $H$ is a composition of left and right translations with either the identity or inversion on the $i$-th group factor. Both translations and inversion are isometries for a bi-invariant metric. The same-factor covariant Hessian therefore vanishes. Constant rescaling of the domain metric leaves its connection unchanged, so this conclusion also holds for $\widetilde g$. $\square$

Bracket normalization. In the radius-two metric, the orthonormal basis

$$e_1=\mathbf i/2,\qquad e_2=\mathbf j/2,\qquad e_3=\mathbf k/2$$

satisfies

$$[e_a,e_b]=\epsilon_{abc}e_c.$$

Thus the bracket is the ordinary three-dimensional cross product in this basis:

$$|[X,Y]|\le |X|\,|Y|. \tag{12}$$

It follows from (7) that every distinct-factor mixed term obeys

$$\|(\nabla dH)(X_i,Y_j)\| \le \frac12\|X_i\|\|Y_j\|. \tag{13}$$

The formula is symmetric as a bilinear Hessian: exchanging the two arguments also exchanges the order in the Lie bracket.

## 3. Pulled-back face Hessian

Assume the universal incidence and coefficient bounds

$$d_e\le8,\qquad a_e\ge a_0,\qquad |b_f|\le b_0,$$

and define

$$A_f=\sum_{e\in\partial f}\frac{a_e}{d_e}, \qquad \beta_f=\frac{|b_f|}{A_f}.$$

Because each face has four links,

$$A_f\ge\frac{a_0}{2}, \qquad a_e\le8A_f \quad(e\in\partial f), \tag{14}$$

and hence

$$\beta_f\le\frac{2b_0}{a_0}. \tag{15}$$

Assume the isolated-rotor estimates

$$\|\nabla s_f\|_\infty\le\beta_f, \qquad \|\nabla^2s_f\|_{\mathrm{op}} \le \frac43\beta_f+\frac{20}{3}\beta_f^2. \tag{16}$$

These are the inherited one-face estimates; their first-derivative hypothesis is not being reproved here.

For a smooth map $H_f$, the covariant chain rule is

$$\begin{aligned} \nabla^2(s_f\circ H_f)(X,Y) ={}& \nabla^2s_f(dH_fX,dH_fY)\\ &+ \left\langle\nabla s_f, (\nabla dH_f)(X,Y)\right\rangle. \end{aligned} \tag{17}$$

For unit vectors in the scaled product metric, their original link-factor norms are $\sqrt{a_e}$ and $\sqrt{a_g}$. Thus the first term in (17) is bounded by

$$\sqrt{a_ea_g} \left(\frac43\beta_f+\frac{20}{3}\beta_f^2\right).$$

For a diagonal block, (8) makes the second term zero. Using (14)–(15),

$$\boxed{ h_{\mathrm d} = \frac{32}{3}b_0+ \frac{320}{3}\frac{b_0^2}{a_0}. } \tag{18}$$

For distinct links, (13) bounds the second term in (17) by

$$\frac12\beta_f\sqrt{a_ea_g} \le4b_0.$$

Therefore

$$\boxed{ h_{\mathrm o} = \frac{44}{3}b_0+ \frac{320}{3}\frac{b_0^2}{a_0}. } \tag{19}$$

These are bounds on the operator norms of the face-Hessian blocks in the scaled metric:

$$\|(\nabla^2(s_f\circ H_f))_{ee}\|_{\mathrm{op}} \le h_{\mathrm d},$$

$$\|(\nabla^2(s_f\circ H_f))_{eg}\|_{\mathrm{op}} \le h_{\mathrm o},\qquad e\ne g.$$

## 4. Pointwise vector Bochner equation

Lemma 2 — Componentwise Kato–Bochner inequality.

Let $f\in C^\infty(M)$, set $f_t=P_tf$, and let

$$W=\nabla_{\widetilde g}f_t.$$

Write $W_e$ for its $T_eM$ component and define

$$u_e(t,x)=|W_e(t,x)|_{\widetilde g_e}.$$

Let

$$H=(\nabla^2\Phi)^\sharp$$

be the Hessian endomorphism, with blocks $H_{eg}:T_gM\to T_eM$. Define

$$A_{eg} = 2\sup_{x\in M}\|H_{eg}(x)\|_{\mathrm{op}}. \tag{20}$$

Then $A$ is a finite, configuration-independent, nonnegative matrix, and

$$\boxed{ D^+U_e(t) \le -\frac{a_0}{2}U_e(t) +\sum_g A_{eg}U_g(t), } \tag{21}$$

where

$$U_e(t)=\sup_{x\in M}u_e(t,x).$$

Proof.

The gradient commutation identity, with the Laplacian convention and drift in (2), gives

$$\boxed{ \left( \partial_t-\Delta^\nabla_{\widetilde g} +2\nabla_{\nabla\Phi} \right)W = -\left( \operatorname{Ric}^{\sharp}_{\widetilde g} +2H \right)W. } \tag{22}$$

To check the sign, for a vector field $Z$,

$$\nabla(\Delta f+Zf) = \Delta^\nabla\nabla f -\operatorname{Ric}^{\sharp}\nabla f +\nabla_Z\nabla f +(\nabla Z)^\sharp\nabla f.$$

Here $Z=-2\nabla\Phi$, so

$$(\nabla Z)^\sharp=-2H.$$

This produces precisely the negative Hessian term on the right of (22).

Because the product connection preserves every link tangent bundle, the connection Laplacian also preserves $T_eM$. Taking its $e$-component gives

$$(\partial_t-\mathscr G^\nabla)W_e = -\operatorname{Ric}^{\sharp}_eW_e -2\sum_g H_{eg}W_g. \tag{23}$$

At points where $W_e\ne0$, Kato's inequality and (1) imply

$$(\partial_t-\mathscr G)u_e \le -\frac{a_0}{2}u_e + 2\sum_g\|H_{eg}\|_{\mathrm{op}}u_g. \tag{24}$$

We now justify the zeros of $W_e$ rather than simply assert the inequality there.

For $\varepsilon>0$, put

$$u_{e,\varepsilon} = \left(|W_e|_{\widetilde g_e}^2+\varepsilon^2\right)^{1/2}. \tag{25}$$

This is smooth, including where $W_e=0$. The regularized Kato calculation gives

$$\begin{aligned} (\partial_t-\mathscr G)u_{e,\varepsilon} \le{}& -\frac{a_0}{2} \frac{|W_e|^2}{u_{e,\varepsilon}}\\ &+ 2\sum_g \|H_{eg}\|_{\mathrm{op}} \frac{|W_e|\,|W_g|}{u_{e,\varepsilon}}. \end{aligned}$$

The nonpositive gradient-square remainder from the Kato calculation has been discarded. Since

$$\frac{|W_e|^2}{u_{e,\varepsilon}} = u_{e,\varepsilon} -\frac{\varepsilon^2}{u_{e,\varepsilon}} \ge u_{e,\varepsilon}-\varepsilon$$

and

$$\frac{|W_e|}{u_{e,\varepsilon}}\le1, \qquad |W_g|\le u_{g,\varepsilon},$$

we obtain the smooth pointwise inequality

$$\boxed{ (\partial_t-\mathscr G)u_{e,\varepsilon} \le -\frac{a_0}{2}u_{e,\varepsilon} +\sum_g A_{eg}u_{g,\varepsilon} +\frac{a_0}{2}\varepsilon. } \tag{26}$$

Now $M$ is compact. At a spatial maximum of $u_{e,\varepsilon}$, its gradient vanishes and its Laplacian is nonpositive. The drift term also vanishes there. Consequently,

$$D^+U_{e,\varepsilon} \le -\frac{a_0}{2}U_{e,\varepsilon} +\sum_g A_{eg}U_{g,\varepsilon} +\frac{a_0}{2}\varepsilon, \tag{27}$$

where $U_{e,\varepsilon}=\sup_xu_{e,\varepsilon}$.

Finite-dimensional cooperative comparison gives the corresponding matrix semigroup bound, with an additive error tending to zero as $\varepsilon\downarrow0$. Since

$$0\le U_{e,\varepsilon}-U_e\le\varepsilon,$$

letting $\varepsilon$ tend to zero establishes (21). This is a pointwise Kato calculation followed by a compact-manifold maximum principle. No integrated Bochner inequality is used. $\square$

## 5. Explicit comparison matrix

Each link belongs to at most eight accepted faces. Each such face contains three other links.

The face-Hessian bounds therefore give

$$A_{ee}\le16h_{\mathrm d},$$

and, for $e\ne g$,

$$A_{eg} \le 2h_{\mathrm o} \#\{f:e,g\in\partial f\}.$$

Let $d(e,g)$ denote distance in the link-overlap graph, where two links are adjacent when they share an accepted face.

For $\mu>0$, define

$$\|A\|_\mu = \sup_e\sum_g A_{eg}e^{\mu d(e,g)}.$$

Each of the at most eight incident faces contributes three off-diagonal incidences, each at distance one. Thus

$$\begin{aligned} \|A\|_\mu &\le16h_{\mathrm d}+48e^\mu h_{\mathrm o}\\ &=16(h_{\mathrm d}+3e^\mu h_{\mathrm o}). \end{aligned}$$

Substituting (18)–(19),

$$\boxed{ \|A\|_\mu \le \left(\frac{512}{3}+704e^\mu\right)b_0 + \left(\frac{5120}{3}+5120e^\mu\right) \frac{b_0^2}{a_0}. } \tag{28}$$

At $\mu=\log25$,

$$\boxed{ \|A\|_{\log25} \le \frac{53312}{3}b_0 + \frac{389120}{3}\frac{b_0^2}{a_0}. } \tag{29}$$

## 6. Duhamel derivative-flow conclusion

Set $c=a_0/2$. From (21), cooperative comparison gives

$$U(t)\le e^{-ct}e^{tA}U(0). \tag{30}$$

The weighted matrix norm is submultiplicative because graph distance satisfies the triangle inequality. In particular,

$$\sum_g(A^n)_{eg}e^{\mu d(e,g)} \le\|A\|_\mu^n. \tag{31}$$

Expanding the matrix exponential in (30) and applying (31),

$$U_e(t) \le e^{-ct} \sum_g e^{-\mu d(e,g)} \sum_{n=0}^\infty\frac{t^n}{n!}\|A\|_\mu^n U_g(0).$$

Therefore

$$U_e(t) \le e^{-(c-\|A\|_\mu)t} \sum_g e^{-\mu d(e,g)}U_g(0).$$

For $\mu=\log25$, define

$$\boxed{ \lambda = \frac{a_0}{2} -\frac{53312}{3}b_0 -\frac{389120}{3}\frac{b_0^2}{a_0}. } \tag{32}$$

The derivative-flow estimate is

$$\boxed{ \mathcal D_e(P_tf) \le e^{-\lambda t} \sum_g25^{-d(e,g)}\mathcal D_g(f), } \tag{33}$$

where the derivative normalization is explicitly

$$\boxed{ \mathcal D_e(f) = |(\nabla_{\widetilde g}f)_e|_{\widetilde g_e} = \sqrt{a_e}\,|d_ef|_{g_e^*}. } \tag{34}$$

If one instead writes the estimate using unscaled derivatives, the equivalent formula is

$$|d_eP_tf|_{g_e^*} \le e^{-\lambda t} \sum_g25^{-d(e,g)} \sqrt{\frac{a_g}{a_e}}\, |d_gf|_{g_g^*}. \tag{35}$$

This distinction matters if the electric coefficients are not all equal.

Finally, if

$$\frac{b_0}{a_0}\le\frac1{40000},$$

then

$$\begin{aligned} \frac{\lambda}{a_0} &\ge \frac12-\frac{53312}{3\cdot40000} -\frac{389120}{3\cdot40000^2}\\ &= \frac{26087}{468750}. \end{aligned}$$

Hence

$$\boxed{ \lambda\ge\frac{26087}{468750}a_0 >0.0556522a_0. } \tag{36}$$

The kernel $25^{-d(e,g)}$ has row and column sums at most 13 because the link-overlap graph has degree at most 24. With the scaled derivative convention (34), the radius-two factor diameter is $2\pi/\sqrt{a_e}$, so the corresponding finite-support oscillation estimate retains the factor $26\pi$:

$$\operatorname{osc}(P_tf) \le 26\pi e^{-\lambda t} \sum_{g\in S}\mathcal D_g(f). \tag{37}$$

## 7. Precise status of the lemma

The proof separates into three levels.

|   Statement   |   Status   |
| --- | --- |
|   Orientation conversion (3), transported derivative (10), and mixed covariant Hessian (7)   |   Established by direct calculation   |
|   Same-factor Hessian vanishing and radius-two bracket bound   |   Established   |
|   Product vector Bochner equation and regularized pointwise Kato inequality   |   Established for finite smooth products   |
|   Cooperative maximum principle and Duhamel comparison   |   Established   |
|   Numerical comparison matrix and positive $\lambda$ under the stated smallness condition   |   Established conditional on the face-block bounds   |
|   Face-block bounds (18)–(19)   |   Conditional on the isolated-rotor estimates and local incidence/coefficient assumptions   |
|   Uniformity in graph size   |   Conditional on those same uniform local bounds   |

Remaining mathematical qualification: the isolated-rotor estimate $\|\nabla s_f\|_\infty\le\beta_f$ is an input here, not a consequence of this lemma. The proof also assumes that the accepted-face holonomy is exactly the four-factor word on the original-link product group, with the stated product metric and incidence inventory.

The result is a finite-graph derivative-flow estimate. It does not establish all-orders connected-activity summability, physical kinetic-time normalization, continuum reconstruction, or a Yang–Mills mass gap. The canonical P0–P5 and PF-G0–G5 gates remain open.

My assessment: the previously identified sign/trivialization gap is now resolved by an explicit derivation, and the Kato regularization can be stated without a hidden appeal to an integrated inequality. The scaled-derivative convention in (34)–(35) should be retained in any formal theorem statement; it is the important precision correction to the earlier shorthand. The next useful check is to compare these exact conventions against the isolated-rotor source derivation and the residual-derivative estimates before treating the complete PF-I16 chain as internally certified.

* * *

**You:**

Please compare the check.

* * *

**ChatGPT:**

The revised PF-I16 third-order resolvent check is materially stronger than the historical check in three respects: it lowers the derivative bound, reduces the coefficient prefactor, and permits a less restrictive coupling threshold.

### Historical vs. revised check

|   Quantity   |   Historical check   |   Revised check   |
| --- | --- | --- |
|   Residual derivative bound $M_i$   |   $$1{,}872{,}000\,b_0^2/\sqrt{a_0}$$   |   $$211{,}250\,b_0^2/\sqrt{a_0}$$   |
|   Coupling threshold $b_0/a_0$   |   $$1/93{,}504$$   |   $$1/40{,}000$$   |
|   Third-order prefactor   |   $$1.527\times10^{16}$$   |   $$8.614\times10^{14}$$   |

Revised bound is stronger

### What improved?

1. Derivative estimate: The new $M_i$ is about 8.86 times smaller.
2. Third-order coefficient: The prefactor falls by approximately 17.7 times.
3. Admissible coupling: The revised threshold permits $b_0/a_0$ to be about 2.34 times larger.

The revised estimate is

$$|E_{ijk}| \le \frac{274185600000000\pi\,b_0^6} {a_0^3\kappa\lambda},$$

or, under $b_0/a_0\le1/40000$,

$$\boxed{ |E_{ijk}| \le 3.25\times10^{16}\frac{b_0^6}{a_0^5}. }$$

The improvement is not merely numerical: the revised derivation uses the sharper isolated-rotor Hessian estimate and the updated curvature and derivative-flow constants.

### What the comparison does not establish

The revised check remains conditional on the dressed curvature/Poincaré estimate, the derivative-flow semigroup bound, and the stated sup-resolvent estimate. It does not establish spatial separation of third-order terms, all-orders summability, or a Yang–Mills mass gap.

Assessment: The revised check supersedes the historical third-order estimate for the PF-I16 working route. It is a genuine improvement in the quantitative bound, but not a closure of the larger proof.

* * *

**You:**

Please proceed.

* * *

**ChatGPT:**

## PF-I16 third-order check: independent arithmetic audit

The revised coefficient is internally consistent with the stated resolvent argument. In particular, the numerical prefactor comes directly from

$$6R^2\frac{1}{\kappa} \frac{50\pi}{\sqrt{a_0}\lambda}M,$$

using

$$R=2080\frac{b_0^2}{a_0}, \qquad M=211250\frac{b_0^2}{\sqrt{a_0}}.$$

The integer coefficient is exactly

$$6\cdot50\cdot2080^2\cdot211250 =274185600000000.$$

Thus

$$|E_{ijk}| \le \frac{274185600000000\pi\,b_0^6} {a_0^3\kappa\lambda}$$

has the correct powers of $a_0$, $b_0$, and the stated combinatorial factor of six.

### Threshold substitution

Writing $x=b_0/a_0$, the revised curvature and flow rates give

$$\frac{\kappa}{a_0} =\frac12-\frac{2624}{3}x-\frac{20480}{3}x^2,$$

$$\frac{\lambda}{a_0} =\frac12-\frac{53312}{3}x-\frac{389120}{3}x^2.$$

At $x=1/40000$,

$$\frac{\kappa}{a_0}=0.4781290667\ldots, \qquad \frac{\lambda}{a_0}=0.0556522667\ldots.$$

So the conservative substitutions $\kappa\ge0.478a_0$ and $\lambda\ge0.0556a_0$ are valid. They yield

$$|E_{ijk}| \le 3.2411\ldots\times10^{16} \frac{b_0^6}{a_0^5},$$

which supports the safely rounded bound $3.25\times10^{16}b_0^6/a_0^5$.

### Resolvent contraction: the six-term argument

Let $P_0$ denote projection off constants and $G=L_\Phi^{-1}P_0$. For one permutation,

$$\begin{aligned} &\left|\nu_\Phi\!\left[ r_iG\left(r_jGr_k\right)\right]\right|\\ &\quad = \left|\left\langle r_i, G P_0(r_jGr_k)\right\rangle_{\nu_\Phi}\right|\\ &\quad\le \|r_i\|_\infty \|G\|_{L^2_0\to L^2_0} \|r_jGr_k\|_2\\ &\quad\le \frac{R^2}{\kappa}\|Gr_k\|_\infty\\ &\quad\le \frac{50\pi R^2M_k} {\sqrt{a_0}\,\kappa\lambda}. \end{aligned}$$

The projection is important: $r_jGr_k$ need not itself be centered, but the outer centered factor $r_i$ makes the constant component irrelevant. Summing the six permutations gives precisely the revised coefficient.

### What the comparison actually establishes

The raw prefactor improves by approximately $17.73$ relative to the historical $1.527\times10^{16}$ prefactor. The admissible coupling threshold also becomes less restrictive:

$$\frac{1/40000}{1/93504}=2.3376.$$

These are two distinct improvements. The larger permitted coupling does not mean that the worst-case bound evaluated at the new threshold is automatically smaller than the historical bound evaluated at its threshold: the estimate scales as $b_0^6$, and the threshold change matters substantially.

### Remaining analytic qualification

The algebra and numerical substitutions pass this audit. The result is still conditional on three analytic inputs:

1. The dressed Poincaré estimate $\|G\|_{L^2_0\to L^2_0}\le\kappa^{-1}$.
2. The derivative-flow estimate with its stated exponential rate and spatial kernel.
3. The sup-resolvent estimate \[ |Gr_i|_\infty \le\frac{50\pi}{\sqrt{a_0}\lambda}M_i. \]

There is one consistency check I would retain before promoting this calculation into a theorem: verify that the $M_i$ estimate and the sup-resolvent estimate use the same derivative normalization. The derivative-flow result naturally uses the scaled derivative $\mathcal D_e=\sqrt{a_e}|d_ef|$. Its conversion to unscaled derivatives carries coefficient ratios. Those ratios must be accounted for wherever $M_i$ is defined.

Verdict: The revised third-order coefficient is arithmetically verified, and its improvement in raw prefactor is real. The next priority is the derivative-normalization reconciliation, followed by the still-open fourth-order spatial path-block covariance audit. Neither is replaced by this third-order calculation.

* * *

**You:**

Please complete the remaining task.

* * *

**ChatGPT:**

I have completed the derivative-normalization reconciliation and independently reconstructed the principal fourth-order spatial path-block estimate. The results give a sharper third-order bound and a more explicit conditional fourth-order covariance theorem.

There is one important distinction: the path-block covariance calculation is now closed for contiguous chronological blocks. It does not, by itself, certify every interleaved four-time configuration or the complete Yang–Mills proof.

## 1. Derivative normalization is reconciled

The correct product metric is

$$\widetilde g=\bigoplus_e a_e^{-1}g_e.$$

Its natural derivative is

$$\boxed{\mathcal D_e f =\left|(\nabla_{\widetilde g}f)_e\right| =\sqrt{a_e}\,|d_ef|_{g_e^*}.}$$

Consequently,

$$\Gamma_{\widetilde g}(f,g) =\sum_e\langle \mathcal D_e f,\mathcal D_e g\rangle.$$

The conversion to unscaled derivatives is

$$|d_eP_tf|_{g_e^*} \le e^{-\lambda t} \sum_g25^{-d(e,g)} \sqrt{\frac{a_g}{a_e}}\, |d_gf|_{g_g^*}.$$

The coefficient ratio is essential. It cannot be discarded unless all link coefficients are equal.

### Oscillation and resolvent normalization

Using the radius-two $SU(2)$ diameter $2\pi$, and $a_e\ge a_0$,

$$\operatorname{osc}(f) \le \frac{2\pi}{\sqrt{a_0}} \sum_e\|\mathcal D_ef\|_\infty.$$

The link graph has degree at most 24. At $\mu=\log25$,

$$\sum_e e^{-\mu d(e,g)} \le 1+\frac{24/25}{1-23/25} =13.$$

This improves the earlier conservative kernel-sum constant of 25.

For centered $r_i$, define the scaled derivative budget

$$M_i=\sum_g\|\mathcal D_gr_i\|_\infty.$$

The derivative-flow estimate therefore gives

$$\boxed{ \|P_tr_i\|_\infty \le\frac{26\pi}{\sqrt{a_0}}e^{-\lambda t}M_i }$$

and, integrating in time,

$$\boxed{ \|Gr_i\|_\infty \le\frac{26\pi}{\sqrt{a_0}\lambda}M_i. }$$

This is the normalization-consistent replacement for the earlier $50\pi$ estimate.

## 2. Revised third-order coefficient

Retaining the previously established residual and derivative budgets,

$$R=2080\frac{b_0^2}{a_0}, \qquad M_i\le211250\frac{b_0^2}{\sqrt{a_0}},$$

the six-permutation resolvent calculation becomes

$$|E_{ijk}| \le \frac{6R^2}{\kappa} \frac{26\pi}{\sqrt{a_0}\lambda}M_i.$$

Thus

$$\boxed{ |E_{ijk}| \le \frac{142576512000000\pi\,b_0^6} {a_0^3\kappa\lambda}. }$$

Sharper bound

At $b_0/a_0\le1/40000$, the exact curvature and flow ratios are

$$\frac{\kappa}{a_0}=0.4781290667\ldots, \qquad \frac{\lambda}{a_0}=0.0556522667\ldots.$$

Therefore,

$$\boxed{ |E_{ijk}| \le1.69\times10^{16} \frac{b_0^6}{a_0^5}. }$$

The previous coefficient was $3.25\times10^{16}$. The improvement is approximately a factor of 1.93.

This sharpening is valid provided the recorded $M_i$ bound is indeed the sum of the scaled derivative suprema defined above. If the earlier $M_i$ calculation used unscaled derivatives or a maximum rather than this sum, that source estimate must be converted before adopting the sharper number.

## 3. Fourth-order path-block covariance: reconstructed estimate

I now give the path-block argument explicitly.

Let

$$K_\mu(e,g)=e^{-\mu d(e,g)},\qquad \mu=\log25,$$

and assume the pointwise derivative-flow estimate

$$\mathcal D_eP_tf \le e^{-\lambda t} \sum_gK_\mu(e,g)\mathcal D_gf. \tag{1}$$

Let $r_i$ be centered residual observables satisfying

$$\|r_i\|_\infty\le R, \qquad m_i(e)=\|\mathcal D_er_i\|_\infty, \qquad M_i=\sum_em_i(e).$$

For two chronologically paired insertions, set

$$F_{ij}(s)=r_iP_sr_j.$$

The product rule and the corrected oscillation estimate give

$$\boxed{ \mathcal D_eF_{ij}(s) \le e^{-\lambda s} \left[ C_0M_jm_i(e)+R(K_\mu m_j)(e) \right], } \tag{2}$$

where

$$C_0=\frac{26\pi}{\sqrt{a_0}}.$$

This is the key path-block estimate. It controls the derivative of the product without falsely treating $P_sr_j$ as compactly supported.

### Kernel convolution

For

$$0<\nu<\mu-\log23,$$

the graph shell estimate yields

$$K_\mu*K_\mu\le C_2K_\nu,$$

where

$$C_2= 1+\frac{24e^{-(\mu-\nu)}} {1-23e^{-(\mu-\nu)}}.$$

Choose

$$\nu=\frac12\log\frac{25}{23} \approx0.0416908.$$

Then

$$C_2<25.511, \qquad K_\mu^{*3}\le C_2^2K_\nu, \qquad C_2^2<650.81.$$

The third convolution bound follows by applying the two-kernel estimate and then summing the remaining kernel with the same shell estimate. This is the necessary finite-convolution justification; it is not legitimate simply to reuse the two-kernel constant without another summation.

### Covariance of two pair blocks

For a reversible generator,

$$\operatorname{Cov}_\pi(F,P_bG) = \int_0^\infty \pi[\Gamma(F,P_{t+b}G)]\,dt.$$

Applying (1) and (2) gives

$$\begin{aligned} &|\operatorname{Cov}_\pi(F_{ij}(s),P_bF_{k\ell}(t))|\\ &\quad\le \frac{e^{-\lambda(s+b+t)}}{\lambda} \sum_{e,h} E_{ij}(e)K_\mu(e,h)E_{k\ell}(h), \end{aligned}$$

where

$$E_{ij}=C_0M_jm_i+RK_\mu m_j.$$

Expanding the product produces exactly four kernel contributions:

$$K_\mu,\quad K_\mu^{*2},\quad K_\mu^{*2},\quad K_\mu^{*3}.$$

If the two spatial clusters are separated by distance $D$, the resulting bound is

$$\boxed{ |\operatorname{Cov}_\pi(F_{ij}(s),P_bF_{k\ell}(t))| \le \frac{C_{\rm sp}}{\lambda} e^{-\lambda(s+b+t)} e^{-\nu D} M_iM_jM_kM_\ell, }$$

with

$$\boxed{ C_{\rm sp} =C_0^2+2C_0RC_2+R^2C_2^2. }$$

This establishes simultaneous spatial and temporal decay for the pair-block covariance, conditional on (1).

### Full contiguous-block fourth cumulant

The exact decomposition is

$$\begin{aligned} \mathcal K_4={}& \operatorname{Cov}_\pi(F_{12}(a),P_bF_{34}(c))\\ &-C_{13}(a+b)C_{24}(b+c)\\ &-C_{14}(a+b+c)C_{23}(b), \end{aligned}$$

where $C_{ij}(t)=\operatorname{Cov}_\pi(r_i,P_tr_j)$.

The two cross-pair terms connect opposite spatial clusters. Each two-time covariance obeys

$$|C_{ij}(t)| \le \lambda^{-1}e^{-\lambda t} e^{-\nu D}M_iM_j.$$

Integrating the three time gaps, including the covariance-integral factor, gives

$$\boxed{ \begin{aligned} \int_{\mathbb R_+^3}|\mathcal K_4| &\le \left( \frac{C_{\rm sp}}{\lambda^4} +\frac{1}{\lambda^5} \right)\\ &\quad\times e^{-\nu D}M_1M_2M_3M_4. \end{aligned} } \tag{PB}$$

This is the explicit, volume-independent path-block covariance estimate.

It retains the pair-partition subtractions, has integrability in all three time gaps, and introduces no total-volume factor.

## 4. What this completes—and what it does not

|   Obligation   |   Result   |
| --- | --- |
|   Scaled versus unscaled derivative conversion   |   Reconciled   |
|   Oscillation and resolvent normalization   |   Reconciled   |
|   Improved third-order coefficient   |   Derived   |
|   Two-kernel spatial convolution   |   Verified   |
|   Three-kernel spatial convolution   |   Verified   |
|   Pair-block covariance and temporal integration   |   Derived conditionally   |
|   Contiguous-block fourth cumulant   |   Derived conditionally   |
|   All interleaved and nested chronology cases   |   Conditional; require their separate cancellation identities   |
|   Complete fourth-order all-label summability   |   Not independently recertified by this calculation   |
|   All-orders convergence and interacting gap   |   Open   |

The crucial limitation is that a spatial partition need not be a contiguous chronological partition. For interleaved configurations, one cannot simply reorder the four insertions and apply (PB). The within-cluster pair subtraction can be nondecaying by itself. It must first be canceled against the corresponding part of the middle bridge.

The existing cancellation-preserving interleaved decompositions remain the correct route. This audit supplies a cleaner derivative normalization and a rigorous contiguous-block covariance estimate, but it does not replace those decompositions.

## Final assessment

Two substantive pieces are now resolved:

1. The third-order derivative normalization has been reconciled, and the sharper $1.69\times10^{16}$ coefficient follows under the explicitly stated scaled-derivative budget.
2. The fourth-order pair-block covariance estimate has been reconstructed with explicit kernel convolution constants and all three time integrations.

The complete fourth-order theorem remains conditional on the pointwise derivative-flow hypothesis and on the separate interleaved/nested chronology arguments. No all-orders summability, continuum reconstruction, or Yang–Mills mass gap is established by this work.

* * *

**You:**

Please continue to the complete fourth-order theorem

* * *

**ChatGPT:**

The fourth-order calculation can now be consolidated into a single theorem. The important qualification is that it is a complete conditional finite-strip theorem, not an unconditional theorem about the interacting or continuum Yang–Mills theory.

The historical proof record contains the missing chronology, reflected-filtration, distance-offset, and normalization audits. I have reconciled those into the statement below rather than treating the earlier intermediate estimates as separate conclusions.

# Fourth-order extensivity theorem

## 1. Setting and hypotheses

Consider the finite open SU(2) strip with $N-1$ residual interactions,

$$H_N(t)=L_N+tW_N,\qquad W_N=\sum_{j=1}^{N-1}w_j,$$

where $L_N$ is the dressed reference generator and $E_N(t)$ its ground energy.

The theorem requires the following uniform analytic hypotheses.

H1 — SU(2) geometry and isolated dressing.

Use the bi-invariant radius-two metric, with orthonormal generators $i/2,j/2,k/2$. The plaquette and dressing estimates must satisfy

$$\|\nabla p_f\|_\infty\le\frac12, \qquad \|\operatorname{Hess}_{ed}p_f\|_{\rm op}\le\frac14,$$

and the isolated-dressing certificate

$$q_g=\|s_g'\|_\infty+\|s_g''\|_\infty \le\frac{49}{576}.$$

H2 — Reference curvature and weighted locality.

For the dressed reference generator,

$$\kappa\ge\frac{23}{144}.$$

For every original-link source set $S$, define

$$\Gamma_w(f) = \sum_e\left(\frac65\right)^{2d(e,S)} |\nabla_ef|^2.$$

The pointwise weighted Bochner estimate is

$$\Gamma_{2,w}(f) \ge\frac{11}{120}\Gamma_w(f).$$

It implies

$$\|\sqrt{\Gamma_w(P_tf)}\|_4 \le e^{-11t/120} \|\sqrt{\Gamma_w(f)}\|_4$$

and

$$\|\sqrt{\Gamma_w(Rf)}\|_4 \le\frac{120}{11} \|\sqrt{\Gamma_w(f)}\|_4, \qquad R=L_N^{-1}Q.$$

H3 — Conditional prefix inequalities.

Both left-to-right and right-to-left filtrations must obey the conditional future-link Poincaré inequality

$$\|u-P_ju\|_2^2 \le\frac{144}{23} \sum_{e\in T_{>j}}\|\nabla_eu\|_2^2.$$

The residual bonds must satisfy the appropriate centering identities, including the reflected identity. Repeated indices are not to be treated as though $P_jw_j^2=0$; that identity is not generally true.

H4 — Connected four-time estimates.

The six spatial-cluster chronological arrangements must have integrable connected-cumulant bounds, retaining all normalization subtractions and centered projections. In particular, the outer-gap and middle-gap estimates, after physical-link distance conversion, must satisfy the common allowance

$$\boxed{ \int_{\mathbb R_+^3} |\mathcal K_4(a,b,d)| \,da\,db\,dd \le 0.1\left(\frac56\right)^{\max(j-i,k-j,\ell-k)} } \tag{1}$$

for sorted labels $i\le j\le k\le\ell$, including repeated labels.

The two-cluster chronology classification is:

|   Chronology   |   Status under H1–H4   |
| --- | --- |
|   LLRR / RRLL   |   Controlled   |
|   LRLR / RLRL   |   Controlled   |
|   LRRL / RLLR   |   Controlled   |

The interleaved cases require the cancellation-preserving cumulant identity; taking absolute values before canceling the within-cluster pairings is not valid.

H5 — Correct physical-link geometry.

For residual-bond supports,

$$\boxed{ d_{\rm link}(S_i,S_k) =\max(0,k-i-2),\qquad i<k. }$$

Thus the spatial conversion costs a factor

$$\left(\frac65\right)^2=\frac{36}{25}.$$

The corrected chronology constants remain below the allocated $0.1$ allowance:

$$0.0541393940<0.1, \qquad 0.0541737884<0.1.$$

These hypotheses summarize the analytic dependencies documented in the fourth-order audits.

Resume 3D Proof Review.md

## 2. The theorem

Conditional fourth-order extensivity

Under H1–H5, the fourth derivative of the finite-strip ground energy at zero residual coupling obeys

$$\boxed{ |E_N^{(4)}(0)| \le 62553.6\,(N-1). }$$

The bound is uniform in strip length, includes repeated residual-bond labels, and is an extensive zero-coupling response estimate.

## 3. Proof

Step 1 — Fourth-order response identity.

For independently coupled centered perturbations $V_i$, the complete mixed derivative is

$$\partial_i\partial_j\partial_k\partial_\ell E(0) = -\sum_{\sigma\in S_4} \int_{\mathbb R_+^3} \mathcal K_{\sigma_1\sigma_2\sigma_3\sigma_4} (a,b,d)\,da\,db\,dd.$$

There are 24 chronological permutations, even when labels coincide. The complete permutation sum is essential: an individual chronological cumulant is not generally equal to an individual resolvent summand.

For a single perturbation, this gives

$$E_N^{(4)}(0) = -24\int_{\mathbb R_+^3} \mathcal K_{W_NW_NW_NW_N}(a,b,d) \,da\,db\,dd,$$

with the bond-label assignments expanded and counted separately.

Step 2 — Connected spatial decay.

The pointwise weighted Bochner estimate supplies the $L^4$ semigroup gradient contraction. The conditional Poincaré inequality supplies the future-link tail estimate. Together with the exact centered product-defect identity,

$$Q\mathcal D_t(F,G) = 2\int_0^t QP_s \Gamma(P_{t-s}F,P_{t-s}G)\,ds,$$

these control the evolved products and preserve the stationary projection.

The chronology-specific estimates then give (1). In the interleaved cases, the within-cluster pair subtraction must remain inside the connected expression until its cancellation with the middle bridge has occurred.

Step 3 — Three-gap summation.

Set

$$a=j-i,\qquad b=k-j,\qquad d=\ell-k.$$

Zero gaps are allowed. The exact sum is

$$\begin{aligned} \sum_{a,b,d\ge0} \left(\frac56\right)^{\max(a,b,d)} &= \sum_{m=0}^\infty \big[(m+1)^3-m^3\big] \left(\frac56\right)^m\\ &= \sum_{m=0}^\infty (3m^2+3m+1) \left(\frac56\right)^m\\ &=\boxed{1086}. \end{aligned}$$

For each smallest bond index, the remaining ordered-label sum is therefore bounded by

$$0.1\times1086=108.6.$$

There are at most $N-1$ choices of smallest index.

Step 4 — Multiplicities.

The fourth derivative introduces:

* 24 chronological permutations in the response identity;
* at most 24 ordered assignments of four bond labels for each sorted label tuple.

Thus

$$\begin{aligned} |E_N^{(4)}(0)| &\le 24\cdot24\cdot0.1\cdot1086\,(N-1)\\ &=\boxed{62553.6(N-1)}. \end{aligned}$$

This completes the conditional proof. The geometric-series identity, multiplicities, repeated-label enumeration, and response normalization have independent arithmetic or finite-state checks recorded in the project history.

Resume 3D Proof Review.md

## 4. What is now complete

|   Component   |   Assessment   |
| --- | --- |
|   SU(2) link metric and quaternion Hessian normalization   |   Analytically derived   |
|   Isolated-dressing input   |   Inherited certificate   |
|   Weighted pointwise Bochner estimate   |   Analytically derived under dressing input   |
|   Weighted $L^4$ semigroup and Poisson estimates   |   Derived   |
|   Conditional future-link Poincaré and prefix centering   |   Derived under geometric inputs   |
|   Reflected right-to-left centering   |   Derived   |
|   Connected cumulant identities and chronology classification   |   Audited   |
|   Corrected physical-link distance offset   |   Verified   |
|   Repeated-label and permutation counting   |   Verified   |
|   Fourth-order extensive bound   |   Established conditionally   |

The relevant consolidated archive is the [fourth-order theorem dependency certificate](https://github.com/syncgravity/singular-boundary/blob/main/research/theorems/R3_IR_FOURTH_ORDER_DEPENDENCY_CERTIFICATE_2026-11-02.md?utm_source=chatgpt.com), commit `75b63c77daba194db2e05505b3a6d97dd0d1ef1b`. It distinguishes the exact algebraic results from the inherited analytic assumptions.

Resume 3D Proof Review.md

## 5. The remaining boundary of the theorem

There are two distinct levels of completion:

1. Fourth-order theorem: The conditional finite-strip result above is assembled, with its hypotheses and coefficient explicitly identified.
2. Unconditional mathematical certification: The dressing certificate and continuous SU(2) analytic estimates must be independently certified in the exact regulator and measure under consideration. The historical numerical checks do not replace that proof.

And the fourth-order estimate alone does not establish

$$\inf_N\operatorname{gap}(H_N(1))>0.$$

That requires a volume-uniform interacting stability argument or an all-orders expansion whose convergence domain reaches $t=1$. A continuum Yang–Mills mass gap additionally requires the physical regulator and continuum reconstruction.

My assessment: We can now state the fourth-order result as a coherent, conditional theorem rather than an incomplete collection of chronology estimates. The next decisive mathematical task is not another fourth-order rearrangement; it is independent certification of the analytic hypotheses, especially the isolated-dressing estimate and the uniform conditional curvature/Poincaré chain. I have not changed the repository.

* * *

**You:**

Please continue with the next task

* * *

**ChatGPT:**

## Next task: establish the interacting Hessian bound

The dependency certificate identifies the next real obstacle: prove, uniformly in strip length and $0\leq\lambda\leq1$, that the interacting ground-state logarithm $u_{N,\lambda}$ satisfies

$$\operatorname{Hess}u_{N,\lambda}\leq\eta g, \qquad \eta<\frac{23}{288}.$$

That would imply the conditional gap bound

$$\operatorname{gap}(H_N(\lambda)) \geq\frac{23}{144}-2\eta>0.$$

The global perturbation estimate cannot do this: $\|W_N\|_\infty$ grows with $N$. We therefore need a local differential estimate, not a volume-dependent norm comparison. I’ll start by isolating the Hessian equation and the terms that must be controlled.

Resume 3D Proof Review.md

### 1. The exact flat-model Hessian identity

Write the logarithmic ground-state equation in the convention $L=-\Delta$:

$$-\Delta u-|\nabla u|^2+\lambda W=E.$$

Define the ground-state drift operator

$$\mathscr A_u=-\Delta-2\nabla u\cdot\nabla.$$

Differentiating once gives

$$\mathscr A_u(\nabla u)=-\lambda\nabla W.$$

Differentiating a second time gives the key identity

$$\boxed{ \mathscr A_u(\nabla^2u) =2(\nabla^2u)^2-\lambda\nabla^2W. } \tag{1}$$

Here $(\nabla^2u)^2$ denotes composition of the Hessian as a symmetric endomorphism.

On the product SU(2) manifold, the covariant version acquires curvature-commutator terms:

$$\boxed{ \mathscr A_u H =2H^2-\lambda\nabla^2W+\mathcal R(H), \qquad H=\nabla^2u. } \tag{2}$$

The precise sign and block form of $\mathcal R$ must be fixed against the project’s Laplacian and curvature conventions before using (2) quantitatively. The product geometry has parallel curvature, which removes derivatives of the curvature tensor, but does not remove the curvature action on $H$.

### 2. Why this does not yet close the gap estimate

There are three distinct obstacles.

1. The quadratic term has the wrong sign for a direct upper-bound argument. The $2H^2$ term is positive semidefinite. A naïve maximum-principle estimate does not turn (2) into the desired upper bound on the largest eigenvalue of $H$.

2. The source must be controlled in operator norm, not by its total size. Since $W_N=\sum_jw_j$, an estimate based on $\|\nabla^2W_N\|_\infty$ obtained by summing individual norms may grow with $N$. The useful estimate must exploit finite-range overlap and the block structure of the Hessian.

3. The drift resolvent is potentially circular. Inverting $\mathscr A_u$ requires control of the very interacting operator whose spectral gap we are trying to prove. Substituting the dressed-reference inverse without controlling the change of drift would silently assume the missing stability estimate.

### 3. The higher-derivative issue

The archived isolated-dressing $C^3$ and $C^4$ estimates are useful inputs for the reference drift. They do not bound the third and fourth derivatives of the interacting logarithm $u_{N,\lambda}$.

In a semigroup proof, differentiating the Hessian evolution introduces derivatives of the drift. In particular, the second-derivative commutator contains third derivatives of the drift potential. Consequently, the first-gradient Bochner estimate alone cannot establish the required Hessian-resolvent estimate.

Resume 3D Proof Review.md

### 4. The next calculation

The cleanest next test is to split the Hessian equation into reference and interacting pieces. Let

$$\mathscr A_0=L_N-2\Gamma(S_g,\cdot), \qquad \mathscr A_u=\mathscr A_0-2\Gamma(u,\cdot).$$

Then the Hessian equation can be organized schematically as

$$\mathscr A_0 H = 2H^2-\lambda\nabla^2W +\mathcal R(H) +2\,\nabla^2\!\bigl[\Gamma(u,\cdot)\bigr]_{\text{commutator}}, \tag{3}$$

where the final term must be expanded covariantly rather than bounded as an undifferentiated operator.

The decisive test is whether that final term can be expressed using:

* the already controlled reference curvature and local SU(2) geometry;
* $H$ itself;
* a localized, volume-uniform source involving derivatives of $W_N$;

without requiring an a priori bound on $\nabla^3u$.

If it cannot, we will need a separate third-derivative estimate before the Hessian bootstrap can close.

Current verdict: equation (1) identifies the Riccati structure; it does not prove the uniform Hessian bound. The next proof obligation is the covariant expansion and estimate of the commutator term in (3), followed by a volume-uniform bootstrap. The interacting $\lambda=1$ gap remains open.

* * *

**You:**

Continue the next calculation towards a solution to each obstacle

* * *

**ChatGPT:**

# Interacting Hessian estimate — next calculation

The next calculation can make progress on all three obstacles, but it also exposes a distinction we need to preserve: the local dressing terms can be bounded uniformly in strip length; the nonlinear drift generated by the interacting ground state cannot yet be bounded by those same estimates.

I’ll work at the reference semigroup first, derive the coupled estimate with explicit constants where the source data support them, and then identify the precise inequality needed to close the interacting bootstrap.

## 1. Expand the drift commutator without discarding the derivative order

Use the convention

$$L=-\Delta-2\nabla S_g\cdot\nabla,\qquad P_t=e^{-tL},$$

and write $b=\nabla S_g$, $H=\nabla^2f$.

At a point in a normal orthonormal frame, the drift part of the Hessian commutator is

$$\begin{aligned} &\nabla_i\nabla_j(b^k\nabla_k f) -b^k\nabla_kH_{ij}\\ ={}& (\nabla_i\nabla_jb^k)\nabla_kf +(\nabla_i b^k)H_{jk} +(\nabla_j b^k)H_{ik}\\ &\quad +b^k\big( \nabla_i\nabla_j\nabla_k f -\nabla_k\nabla_i\nabla_j f \big). \end{aligned} \tag{4}$$

Since $b=\nabla S_g$, the first three terms become

$$(\nabla_i\nabla_j\nabla^kS_g)\nabla_kf +(\nabla_i\nabla^kS_g)H_{jk} +(\nabla_j\nabla^kS_g)H_{ik}.$$

The last line is a curvature commutator acting on $\nabla f$. Thus the drift contribution to the Hessian heat evolution has the structure

$$\boxed{ \begin{aligned} \mathcal D_g(H,\nabla f)_{ij} ={}&4(\nabla^2S_g\circ H)_{(ij)} +2(\nabla^3S_g)_{ijk}\nabla^kf\\ &+2\mathcal R_{ij}(b,\nabla f), \end{aligned}} \tag{5}$$

where $\mathcal R$ denotes the ordered curvature-contraction term, with its sign fixed by the chosen curvature convention.

This reproduces the one-dimensional check:

$$(Lf)''-L(f'')=-4S_g''f''-2S_g'''f'.$$

In particular, the third derivative is not optional: it is a genuine forcing term.

## 2. Bound the reference third-derivative forcing locally

The archived directional estimate for one dressed plaquette is

$$|(\nabla_V)^3(s_g\circ p_f)| \le M_3\|V\|^3, \qquad M_3=\frac{320161}{1769472}<0.181. \tag{6}$$

It is a bound on the diagonal of the symmetrized third derivative, not yet on the ordered tensor.

Resume 3D Proof Review.md

For a symmetric trilinear form $T$, polarization gives

$$\|T\|_{\mathrm{op}} \le \frac{3^3}{3!} \sup_{\|v\|=1}|T(v,v,v)| =\frac92\sup_{\|v\|=1}|T(v,v,v)|.$$

Hence the fully symmetric third derivative of one plaquette dressing satisfies

$$\|\operatorname{Sym}\nabla^3(s_g\circ p_f)\|_{\mathrm{op}} \le\frac92M_3<0.815. \tag{7}$$

The remaining ordered part is controlled by commuting covariant derivatives. For a scalar $S$, the difference between ordered third derivatives is a curvature contraction with $\nabla S$. Therefore

$$\|\nabla^3S\|_{\mathrm{ordered}} \le 0.815+C_{\mathrm{curv}}\|\nabla S\|, \tag{8}$$

for a local curvature constant $C_{\mathrm{curv}}$ determined by the radius-two SU(2) convention.

This is a useful reduction: it replaces an uncontrolled ordered third derivative by a certified symmetric derivative plus a first-derivative curvature term.

Now use finite overlap. If each original link belongs to at most two plaquettes, and each plaquette dressing has the bound (8), then the contribution to the third-derivative forcing touching a fixed link is bounded independently of $N$. The same holds for the Hessian-drift term in (5).

What this resolves: the reference-dressing third-derivative forcing is local and has a volume-independent bound, conditional on the archived scalar dressing and curvature estimates.

What it does not resolve: the corresponding term for the interacting potential $S_g+u_{N,\lambda}$ also contains $\nabla^3u_{N,\lambda}$. Equation (8) does not control that term.

## 3. Bound the Hessian of the residual source without using its global norm

Let $S_j$ be the original-link support of $w_j$, and define

$$s_*=\sup_j|S_j|,\qquad m_*=\sup_e\#\{j:e\in S_j\},$$

and

$$h_2=\sup_j\|\nabla^2w_j\|_{\mathrm{op}}.$$

For any tangent vector $V=(V_e)_e$,

$$\begin{aligned} |\nabla^2W_N(V,V)| &\le h_2\sum_j\left(\sum_{e\in S_j}|V_e|\right)^2\\ &\le h_2s_*\sum_j\sum_{e\in S_j}|V_e|^2\\ &\le h_2s_*m_*\sum_e|V_e|^2. \end{aligned}$$

Consequently,

$$\boxed{ \|\nabla^2W_N\|_{\mathrm{op}} \le h_2s_*m_*, } \tag{9}$$

independently of the number of faces, provided $s_*,m_*,h_2$ are uniform.

This is the correct replacement for a bound involving $\|W_N\|_\infty$. It controls the local differential source rather than the extensive sum itself.

It also gives a concrete test: compute $s_*,m_*,h_2$ for the actual residual bond in the chosen regulator. Until $h_2$ is supplied for that $w_j$, (9) is a structural estimate, not a numerical curvature bound.

## 4. Recover coercivity on the trace modes from Hessian compatibility

The curvature commutator alone does not damp diagonal pure-trace blocks. But a scalar Hessian is not an arbitrary symmetric tensor: its trace blocks are Laplacians of the underlying scalar.

For an original link $e$, define

$$\phi_e=\operatorname{tr}(H_{ee})=\Delta_e f.$$

Under Haar measure, conditional on all other links,

$$\int_{\mathrm{SU}(2)}\phi_e\,dU_e=0.$$

The first nonzero eigenvalue of the radius-two SU(2) Laplacian is $3/4$. Therefore the conditional Poincaré inequality gives

$$\int|\nabla_e\phi_e|^2\,dU_e \ge\frac34\int|\phi_e|^2\,dU_e. \tag{10}$$

Since the pure-trace block is

$$H_{ee}^{\mathrm{tr}}=\frac{\phi_e}{3}g_e,$$

we have

$$|H_{ee}^{\mathrm{tr}}|^2=\frac{\phi_e^2}{3}, \qquad |\nabla H_{ee}^{\mathrm{tr}}|^2 =\frac{|\nabla\phi_e|^2}{3}.$$

Combining these identities yields

$$\boxed{ \|\nabla H_{ee}^{\mathrm{tr}}\|_2^2 \ge\frac34\|H_{ee}^{\mathrm{tr}}\|_2^2. } \tag{11}$$

Summing over links gives the same lower bound for the aggregate diagonal trace sector, provided the trace blocks are treated with their actual scalar-Hessian compatibility.

This is the missing mechanism in the unweighted reference calculation: the rough tensor Laplacian supplies coercivity where the curvature commutator supplies none.

There is an important limitation. The dressed reference measure is proportional to $e^{2S_g}d\mathrm{Haar}$, not Haar measure. The conditional mean of $\Delta_e f$ need not vanish under that measure. Thus (10) cannot simply be transferred to the dressed semigroup. We need a conditional weighted Poincaré estimate, or a perturbative comparison that explicitly accounts for the nonzero conditional mean.

## 5. Assemble the coupled reference estimate

Let

$$G_t=\|\nabla P_tf\|_w,\qquad H_t=\|\nabla^2P_tf\|_w.$$

The first-gradient weighted estimate supplies

$$\frac{d}{dt}G_t\le-\frac{11}{120}G_t$$

under the archived reference curvature assumptions.

For the Hessian, the corrected curvature commutator contributes damping on mixed blocks and diagonal trace-free blocks. Equation (11) supplies additional unweighted damping for compatible diagonal trace blocks.

The drift estimate (5), together with the local bounds (7)–(9), leads to the following candidate coupled inequality:

$$\boxed{ \frac{d}{dt} \begin{pmatrix}G_t\\H_t\end{pmatrix} \le \begin{pmatrix} -\frac{11}{120}&0\\ C_{\mathrm{ref}}&-\delta_{\mathrm{ref}} \end{pmatrix} \begin{pmatrix}G_t\\H_t\end{pmatrix}. } \tag{12}$$

Here $C_{\mathrm{ref}}$ collects the local third-derivative and curvature forcing, while $\delta_{\mathrm{ref}}$ must include:

* mixed-block curvature damping;
* diagonal trace-free curvature damping;
* rough-Laplacian damping on compatible trace blocks;
* losses from the reference drift and the spatial weights.

The calculation above explains why $\delta_{\mathrm{ref}}>0$ is plausible in the unweighted product geometry. It does not yet establish a positive value for the full dressed weighted norm. In particular, the weighted trace-sector Poincaré estimate is still missing.

If (12) is established with $\delta_{\mathrm{ref}}>0$, then integration gives

$$H_t\le e^{-\delta_{\mathrm{ref}}t}H_0+ C_{\mathrm{ref}}\int_0^t e^{-\delta_{\mathrm{ref}}(t-s)} e^{-11s/120}G_0\,ds.$$

Thus the Hessian is controlled by the initial Hessian and gradient, with no loss depending on strip length.

## 6. Remove the circularity by using the reference resolvent

The interacting drift cannot be used as its own inverse before its curvature is known. Instead, keep the reference resolvent fixed:

$$R_0=L_N^{-1}Q.$$

The logarithmic ground-state equation can be written

$$u_\lambda =-\lambda R_0QW_N+ R_0Q|\nabla u_\lambda|^2, \tag{13}$$

with the additive constant fixed by centering.

This suggests a genuine bootstrap in a local norm $X_N$ that controls both the gradient and the pointwise Hessian. Suppose we can prove

$$\|R_0QW_N\|_{X_N}\le A, \tag{14}$$

$$\|R_0Q\langle\nabla v,\nabla w\rangle\|_{X_N} \le C\|v\|_{X_N}\|w\|_{X_N}, \tag{15}$$

and

$$\lambda_{\max}(\nabla^2v)\le D\|v\|_{X_N}, \tag{16}$$

with constants independent of $N$.

Then the map in (13) preserves the ball of radius

$$r=\frac{1-\sqrt{1-4AC}}{2C}$$

and is contractive at $\lambda=1$, provided

$$\boxed{4AC<1.} \tag{17}$$

If in addition

$$\boxed{Dr<\frac{\kappa_0}{2},} \tag{18}$$

where $\kappa_0$ is the reference curvature lower bound, the interacting Bakry–Émery curvature remains positive.

This is the noncircular route: the inverse in (13) is always the already-controlled reference inverse. But the required $A,C,D$ estimates are not yet available in a single norm. The archived weighted Hessian-resolvent theorem controls an integrated Hessian norm, not the pointwise bound (16).

Resume 3D Proof Review.md

## 7. What each obstacle now requires

|   Obstacle   |   Progress from this calculation   |   Remaining decisive estimate   |
| --- | --- | --- |
|   Positive quadratic Hessian term $2H^2$   |   Identified as a Riccati term; avoid treating it as a dissipative term   |   Close a small-ball fixed point using (15)   |
|   Extensive source $W_N$   |   Replaced global norm by local Hessian bound (9)   |   Evaluate $h_2,s_*,m_*$ for the actual residual bond   |
|   Circular interacting resolvent   |   Replaced by fixed reference resolvent in (13)   |   Prove uniform $A,C,D$ in one norm   |
|   Third-derivative forcing   |   Reduced ordered third derivatives to symmetric derivatives plus curvature terms   |   Bound the interacting $\nabla^3u_\lambda$, not just $\nabla^3S_g$   |
|   Trace-mode noncoercivity   |   Found rough-Laplacian coercivity for compatible Hessians under Haar measure   |   Prove the corresponding weighted conditional Poincaré inequality   |
|   Volume dependence   |   Local overlap makes the source and reference-dressing terms uniform   |   Establish all constants in the actual strip geometry   |

### The next decisive calculation

The most productive next step is now a conditional weighted Poincaré calculation for the diagonal trace blocks. It has a sharper target than another general Hessian commutator:

$$\int |\nabla_e\phi_e|^2\,d\mu_g \stackrel{?}{\ge} c_{\mathrm{tr}}\int |\phi_e-\mathbb E_{\mu_g}[\phi_e\mid U_{\ne e}]|^2\,d\mu_g,$$

where $d\mu_g\propto e^{2S_g}d\mathrm{Haar}$, followed by an explicit estimate of the conditional-mean component.

If $c_{\mathrm{tr}}$ can be made uniform and the mean component controlled by the already localized gradient, it supplies the missing trace-sector damping in (12). If it cannot, we will know precisely why the Hessian route needs a different coercive mechanism.

Status: This calculation has identified concrete routes around the extensive-source and circular-resolvent problems, and a reference trace-mode coercivity mechanism. It has not established the weighted trace inequality, the interacting third-derivative bound, or the $A,C,D$ constants. The uniform interacting gap at $\lambda=1$, and hence the continuum Yang–Mills mass gap, remain open.