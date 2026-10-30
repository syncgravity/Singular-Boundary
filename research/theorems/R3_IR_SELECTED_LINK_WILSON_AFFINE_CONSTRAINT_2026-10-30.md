# Exact fundamental-affine selected-link Wilson constraint and the nonadiabatic escape

**Date:** 2026-10-30. **Status:** finite-volume original-link structural theorem for physical SU(2) Wilson Hamiltonians, including deleted-target completed cages; **not** a uniform bound on the derived nonlinear fiber energy or the continuum mass gap. This makes an algebraic restriction explicit but does not supersede the archived 2026-10-29 shared-edge spin-selection theorems.

## Setting

Let \(e\) be an original edge and \(x=U_e\in SU(2)\), with all other original link variables \(y\) held fixed. For a standard oriented simple rhombus face \(g\) incident to \(e\), its Wilson factor is \(p_g(U)=\frac12\operatorname{ReTr}W_g(U)\). Writing \(SU(2)\) as unit quaternions \(x=x_0I+i\sum_{k=1}^3x_k\sigma_k\), there is, for each \(g\ni e\), a unit quaternion \(v_g(y)\) such that
\[
p_g(x,y)=x\cdot v_g(y).
\]
This is true with either incidence orientation: cyclicity of trace moves the chosen edge to the front; inversion is a real orthogonal transformation in the quaternion coordinates. The choice of \(v_g\) depends on \(y\) but not on \(x\).

Assume the standard nonnegative Wilson magnetic term \(V=\sum_g b_g(1-p_g)\), \(b_g\ge0\). Split
\[
V(x,y)=V_{\neg e}(y)+\sum_{g\ni e}b_g(1-p_g(x,y)).
\]

## Theorem: exact affine fundamental representation restriction

Define \(B_e(y)=\sum_{g\ni e}b_gv_g(y)\in\mathbb R^4\) and \(C_e(y)=V_{\neg e}(y)+\sum_{g\ni e}b_g\). Then
\[
\boxed{V(x,y)=C_e(y)-x\cdot B_e(y),\qquad |B_e(y)|\le\sum_{g\ni e}b_g.}\tag{WA-1}
\]
Thus for each frozen environment \(y\), the selected-link dependence of the *bare* magnetic potential has only Peter–Weyl link spins \(0\) and \(1/2\). Equivalently,
\[
\boxed{V(-x,y)+V(x,y)=2C_e(y),\qquad
\Delta_e[V(x,y)-C_e(y)]=-\tfrac34[V(x,y)-C_e(y)].}\tag{WA-2}
\]
On an edge-to-edge rhombus disk, at most two faces meet a single edge; when the target face \(f\) is magnetic-deleted, each \(e\in\partial f\) touches at most one retained magnetic face. Hence the local field is a single fixed-environment fundamental coefficient or zero. The bound in WA-1 is independent of the *number* of other faces (although it can grow with \(h^{-2}\) at strong Wilson coupling).

**Proof.** SU(2) unit quaternions satisfy \(\frac12\operatorname{ReTr}(xq)=x\cdot\bar q\) for a suitable orthogonal identification; orientations and conjugations preserve unit norm. Each incident trace is a linear coordinate function in \(x\) for fixed other links. Summation gives WA-1 and its triangle bound. Replacing \(x\) by \(-x\) reverses the linear part. Every fundamental coefficient is a Laplacian eigenfunction of eigenvalue \(-3/4\), proving WA-2. The incidence bound is geometric. QED.

## Why the inverse-rotor obstruction does not directly transplant

The previously constructed adverse rotor Hamiltonian uses a smooth class potential \(V_L(u)\) on one SU(2) coordinate, with a nontrivial center-even part. Unless constant, such a potential cannot equal the frozen-environment bare Wilson selected-link potential \(C-x\cdot B\): under \(x\mapsto -x\), the latter's nonconstant part changes sign, whereas the rotor potential is even.

**Crucial limitation:** This distinction does **not** prove that a completed-cage Wilson vacuum excludes the adverse rotor-like *marginal*. The exact nonadiabatic effective fiber energy \(U_f(p)\) contains environmental conditional expectations and gradients of the normalized conditional state \(\Phi_f\). Eliminating/conditioning on environmental links can create integer-spin, center-even, nonmonotone effective interactions even though every frozen-link bare Wilson potential is fundamental-affine. Indeed the archived four-neighbor selection results require at least a second-order response to each neighbor coupling for a spin-one target observable; they do not force its coefficient's sign.

Therefore WA-1 is a **Wilson-specific structural restriction**, not a favorable sign theorem for the true physical cumulative current.

## Next proof obligation: close the conditional-response, not the bare-link, gap

Develop a signed comparison controlling the fundamental-affine incident interactions *after* accounting for the \(y\)-dependence of the full physical conditional state \(\Phi_f\), possibly using the pre-existing four-neighbor spin filtration and mixed-response structure. One must bound the adverse eighth-order mixed response at physical full coupling or establish a comparable Wilson-specific conditional-fiber inequality **without assuming the desired physical mass gap**. A frozen-environment Wilson affinity statement alone is insufficient.

## Source scope

Original-link Wilson Hamiltonian and geometric incidence as in archived \`R3_IR_FOUR_NEIGHBOR_SPIN_SELECTION_AND_MIXED_RESPONSE_2026-10-29.md\` and \`R3_IR_WILSON_BRIDGE_SPIN_SELECTION_AND_GAP_OBSTRUCTION_2026-10-29.md\`. The explicit quaternion-affine decomposition (WA-1/2) and its logical limitation are proved here. No new Monte Carlo evidence or independently verified continuum theorem is claimed.
