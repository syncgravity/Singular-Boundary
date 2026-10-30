# The Singular Boundary — Deleted-face adjoint-flux diamagnetism and the uniform transverse zero-point barrier

**Date:** 2026-10-29. **Claim type:** exact quadratic/Hessian theorem on the *nonlinear SU(2) magnetic-deleted configuration manifold*, with a face-count-independent positive lower bound for the associated **harmonic normal-mode zero-point energy** on cycle-rich rhombus disks. The latter is **not** a theorem about the full nonlinear magnetic-deleted quantum vacuum or its flat-holonomy small-ball probability. All physical mass-gap and continuum claims remain open.

## 1. Model and zero-potential configurations

Let \(G\) be a finite face-complete simply connected edge-to-edge rhombus disk. Every face has four boundary edges and each electric edge is incident to at most two magnetic faces. Let \(a_e\in[a_-,a_+]\), \(a_->0\), and \(b_g=\beta_gh^{-2}\), \(\beta_g\in[\beta_-,\beta_+]\) on all faces \(g\ne f\). Fix any interior target face \(f\); its magnetic term is deleted. Work in the finite all-vertex Gauss-invariant SU(2) Hamiltonian with electric Casimir \(-\Delta\chi_j=j(j+1)\chi_j\):

\[
H^-_{f,h}=\sum_e a_e(-\Delta_e)+\sum_{g\ne f}b_g \bigl(1-\tfrac12\mathrm{Tr}W_g\bigr).
\]

The classical zero set \(\mathcal Z_f\) consists of configurations with \(W_g=I\) for every remaining face \(g\ne f\). Every based holonomy \(W_f=U\in SU(2)\) is attainable on \(\mathcal Z_f\) by a dual string ending at the exterior boundary; there is no planar face-Bianchi restriction fixing \(U\). Modulo Gauss conjugation, \(U\) is characterized by \(p_f=\cos\theta\), \(0\le\theta\le\pi\).

## 2. Exact covariant face–edge derivative of the nonlinear Wilson action

Choose any background link configuration \(U^{(0)}\in\mathcal Z_f\), varying each electric link along \(U_e(\varepsilon)=\exp(i\varepsilon X_e\cdot\sigma/2)U_e^{(0)}\). For each remaining plaquette, since \(W_g^{(0)}=I\), there is an exact first-order covariant coboundary map

\[
\delta W_g=\frac i2 (\mathsf B_U X)_g\cdot\boldsymbol\sigma,
\qquad (\mathsf B_U X)_g=\sum_{e\in\partial g}\mathrm{sgn}(g,e)\mathrm{Ad}_{T_{g,e}}X_e.
\]

The transporters \(T_{g,e}\) are products of background links up to the selected edge, including the extra inverse-edge transporter when the edge is traversed backwards. Hence the exact second variation of the **nonlinear** magnetic potential at the background is

\[
V^-_h(U^{(0)}e^{i\varepsilon X\cdot\sigma/2})
=\frac{\varepsilon^2}{8h^2}\sum_{g\ne f}\beta_g|(\mathsf B_U X)_g|^2+O_{G,U}(\varepsilon^3h^{-2}).
\]

Its nonzero normal-mode kinetic matrix is

\[
\mathsf L_U=\mathsf D_\beta^{1/2}\,\mathsf B_U\operatorname{diag}(a_e)\mathsf B_U^*\mathsf D_\beta^{1/2}
\]

acting on three-component Lie-algebra-valued face variables indexed by \(g\ne f\). For all backgrounds on the deleted-face zero set, the block diagonal is \(\mathsf L_{gg}=\beta_g(\sum_{e\in\partial g}a_e)I_3\), and each shared-edge off-diagonal is

\[
\mathsf L_{gg'}=-a_{e(g,g')}\sqrt{\beta_g\beta_{g'}}\,\mathsf O_{gg'},\qquad \mathsf O_{gg'}\in SO(3),\quad \mathsf O_{g'g}=\mathsf O_{gg'}^{-1}.
\]

All dual-face parallel transports around contractible loops are identity; a loop winding once around the missing face carries \(\mathrm{Ad}(U)\) (or its inverse). These are exact differential-geometric statements, not a replacement of the full non-linear vacuum by a Gaussian measure. The positive normal matrix has dimension \(3(F-1)\); gauge zero modes have been eliminated by passing to face normal coordinates.

## 3. Adjoint heat-trace diamagnetism for arbitrary face count

Let \(D_g=\beta_g\sum_{e\in\partial g}a_e\in[4a_-\beta_-,4a_+\beta_+]\). Write \(\mathsf L_U=D-W_U\), where all off-diagonal link weights \(w_{gg'}=a_e\sqrt{\beta_g\beta_{g'}}\) are nonnegative and \((W_U)_{gg'}=w_{gg'}\mathsf O_{gg'}\). Use the absolutely convergent Duhamel/Dyson expansion of \(e^{-t(D-W_U)}\), and trace over closed dual walks. Each closed walk has a positive scalar weight, while its holonomy factor is \(\operatorname{tr}_{\mathbb R^3}\mathsf O_{\mathrm{walk}}\le3\). For central \(U=\pm I\), all adjoint holonomies are trivial, so every walk has maximal trace three. Therefore for **all** \(t>0\)

\[
\boxed{\operatorname{Tr}e^{-t\mathsf L_U}\le\operatorname{Tr}e^{-t\mathsf L_I}.}\tag{DF-1}
\]

As both matrices are positive semidefinite, the exact square-root identity

\[
\operatorname{Tr}\sqrt{\mathsf L_U}-\operatorname{Tr}\sqrt{\mathsf L_I}
=\frac1{2\sqrt\pi}\int_0^\infty t^{-3/2}\bigl[\operatorname{Tr}e^{-t\mathsf L_I}-\operatorname{Tr}e^{-t\mathsf L_U}\bigr]\,dt
\]

proves

\[
\boxed{\operatorname{Tr}\sqrt{\mathsf L_U}\ge\operatorname{Tr}\sqrt{\mathsf L_I}.}\tag{DF-2}
\]

No uniform spectral gap for \(\mathsf L_U\) is required for the integral identity; in the complete disk setup the normal matrix is strictly positive anyway.

## 4. Uniform strict flux barrier from one local winding cycle

Suppose the face-dual graph after deleting \(f\) contains a directed closed walk \(\gamma\) winding exactly once around \(f\), with \(\ell=|\gamma|\le L\). The walk's adjoint trace is \(1+2\cos(2\theta)\), hence its difference from the central value is exactly \(4\sin^2\theta\).

Choose this single nonnegative contribution in the Duhamel trace difference. Every edge weight is at least \(w_-=a_-\beta_-\), while all diagonal potential entries are at most \(D_+=4a_+\beta_+\). The simplex integral for an \(\ell\)-step walk at time \(t\) is at least \(e^{-D_+t}t^\ell/\ell!\). Thus

\[
\operatorname{Tr}e^{-t\mathsf L_I}-\operatorname{Tr}e^{-t\mathsf L_U}
\ge 4\sin^2\theta\;w_-^\ell e^{-D_+t}t^\ell/\ell!.
\]

Restricting the integral in DF-2 to \(t\in[1,2]\) gives

\[
\boxed{\operatorname{Tr}\sqrt{\mathsf L_U}-\operatorname{Tr}\sqrt{\mathsf L_I}\ge c_{L,a_\pm,\beta_\pm}\sin^2\theta,}\tag{DF-3}
\]

where an explicit strictly positive constant, independent of \(h\) and of the **total number of faces**, is

\[
c_{L,a_\pm,\beta_\pm}=\min_{1\le n\le L}\frac{2w_-^n}{\sqrt\pi\,n!}\int_1^2 t^{n-3/2}e^{-D_+t}\,dt>0.
\]

For a full-collar **interior** face of an edge-to-edge rhombus tiling with minimum interior rhombus angle \(\pi/5\), the degree of each primal vertex is at most ten. Following the star of each of the four vertices of \(f\), excluding \(f\), constructs a dual walk winding once around \(f\) of length at most \(4(10-2)=32\). This elementary geometric estimate applies to the declared Penrose rhombus class; it does not certify the Stage7/26 original Hamiltonian data.

The corresponding **harmonic transverse** zero-point energy for the precisely defined quadratic normal Hamiltonian at flux \(U\) is

\[
\mathcal E_{\perp,h}(U)=\frac1{2\sqrt2 h}\operatorname{Tr}\sqrt{\mathsf L_U}.
\]

Hence

\[
\boxed{\mathcal E_{\perp,h}(U)-\mathcal E_{\perp,h}(\pm I)\ge\frac{c_{32,a_\pm,\beta_\pm}}{2\sqrt2\,h}\sin^2\theta.}\tag{DF-4}
\]

This is an exact, size-uniform **normal-mode** flux preference. It is *not* an inequality for the full quantum Hamiltonian after integrating out transverse modes: the longitudinal kinetic energy, metric/Jacobian effects, and volume-uniform nonlinear remainder have not been bounded.

## 5. Topological dichotomy

If every closed dual walk of remaining faces has trivial holonomy (e.g. the magnetic dual graph is a tree after removing \(f\)), then all connection blocks can be globally gauged to identity, so \(\mathsf L_U\) is unitarily equivalent to \(\mathsf L_I\) for every \(U\): the harmonic zero-point energy is flux-independent. This reproduces the *topological* reason the earlier private-edge/dual-bridge cases are simpler. If a once-winding cycle remains, DF-3 gives a strict positive preference for center holonomies. The center preference depends only on \(\mathrm{Ad}(U)\), so it treats \(+I\) and \(-I\) equally, consistently with exact deleted-face center-flux symmetry.

## 6. Deterministic nonabelian fixture

The independently defined **3x3 square-grid surrogate** has nine plaquettes and twenty-four electric edges. Delete its center magnetic face. Give the bottom and top edges of a dual string extending to the boundary a common link holonomy \(U=\exp(i\theta\sigma_3)\), leaving every remaining face holonomy exactly \(I\). The eight remaining faces form a dual eight-cycle. Exact SU(2) adjoint linearization gives an untwisted scalar color and two conjugate blocks with eigenvalues

\[
\lambda_k(2\theta)=4-2\cos((2\pi k+2\theta)/8),\qquad k=0,\ldots,7.
\]

At \(a_e=\beta_g=1\) and \(\theta=\pi/2\), the **three-color square-root trace penalty** is

\[
\operatorname{Tr}\sqrt{\mathsf L_{\pi/2}}-\operatorname{Tr}\sqrt{\mathsf L_0}=0.000041704162\ldots>0,
\]

and the zero-point energy difference is \(0.000014744648\ldots/h\). The explicit one-winding bound is \(c_8=8.657672142\times10^{-7}\), conservative but positive. The exact C8 Bessel heat-trace representation independently reproduces the matrix-exponential trace difference at five temperatures. **The 3x3 geometry is not a Penrose fixture.** The checker separately verifies the authentic original 3-rhombus ten-edge spatial Z^5 Penrose seed incidence; this small seed has no hole winding cycle and does not test DF-3.

## 7. Exact remaining proof obligation

The original objective was a **polynomial lower bound on deleted-vacuum probability** \(\nu^-_{f,h}(d_f\lesssim h)\). DF-1 through DF-4 prove only that the harmonic transverse zero-point *prefers center holonomies*; no probability bound for \(\nu^-_{f,h}\) follows without controlling the quantum ground-state fiber/longitudinal dynamics and the nonlinear remainder, uniformly over \(F_h\asymp h^{-2}\).

A natural next conditional bridge would be a uniform Born–Oppenheimer quadratic-form estimate with an \(o(h^{-1})\) error relating the true deleted Hamiltonian to \(\mathcal E_{\perp,h}(U)\), plus longitudinal kinetic and near-center lower-density estimates. Even near-center concentration would not alone imply the required polynomial probability in a ball of angular radius \(O(\sqrt h)\); a further lower bound at that resolution would still be necessary. The physical gap, quartic resolvent, continuum and original Stage7/26 correspondence all remain OPEN.

**Integrity:** no Monte Carlo, no modification of original data; exact matrix algebra and SU(2) holonomy differentiation only. A standalone Python verifier and execution log accompany this report.
