# Exact noncommuting SU(2) homogeneous Wilson flow and a positive-probability finite tube

**Scientific classification:** finite classical nonlinear theorem in a *periodic* 3-dimensional cubic control, plus a strictly finite interacting-vacuum support consequence. It does **not** establish full non-Abelian positive-flow-time smoothing for typical interacting-vacuum configurations, any uniform probability, an infinite-volume state, a 4D quantum Yang–Mills theory, a physical-time Schur estimate, a mass gap, or a Penrose/gravity theorem.

## 1. Regulator, normalization, and model identity

Fix a 3D periodic spatial cubic lattice with `n>=2` sites per side, `h=1/n`, and `3n^3` original SU(2) links with bi-invariant metric normalized by orthonormal infinitesimal generators `T_j=i sigma_j/2`. There are `3n^3` four-distinct-edge elementary plaquettes, each link incident to four plaquettes. The *classical spatial* Wilson action and its genuine full-link gradient flow are

\[
 S_h(U)=\sum_{p}(1-\tfrac12\operatorname{tr}U_p),\qquad
 \frac{dU}{ds}=-\nabla S_h(U),\qquad \tau=h^2 s.
\]

This **periodic** model is a separate, explicit control of the same original-link Wilson action. It is not the earlier open-boundary 3D slab, the invariant Cartan-planar open model, or a 3D quasicrystal.

## 2. Exact non-Abelian homogeneous submanifold

Set `Ux=exp(theta T1)`, `Uy=exp(theta T2)`, `Uz=I` on every oriented link of its respective direction; `0<theta<=pi/2`. Because `T1` and `T2` do not commute, the elementary xy holonomy is a genuine SU(2) group commutator, with

\[
 \tfrac12\operatorname{tr}(U_xU_yU_x^{-1}U_y^{-1})
   =1-2\sin^4(\theta/2),\qquad
 S_h=2n^3\sin^4(\theta/2).
\]

The transverse xz and yz plaquettes are identity. The full periodic 3D SU(2) force at every x-edge lies along `T1`, at every y-edge along `T2`, and at every z-edge vanishes. Hence this homogeneous orthogonal-axis *noncommuting* family is invariant under the **full nonlinear** Wilson flow, and its exact scalar evolution is

\[
 \boxed{\frac{d\theta}{ds}=-2\sin^3(\theta/2)\cos(\theta/2)}. \tag{1}
\]

This follows from the full group-valued force, not replacing the action by a small-field quadratic form. The companion verifier independently checks the original-link 3D quaternion Wilson forces for `n=2,3,4` and multiple nonzero commutators.

## 3. Positive-physical-time noncommuting curvature bound

Let `z=sin^2(theta/2)`, `y=z/h^2`, and let the normalized **principal holonomy-angle curvature** be

\[
 \mathscr F_h(\tau)=\frac{2}{h^2}d_{SU(2)}(U_{xy}(\tau),I)
                    =\frac4{h^2}\arcsin z(\tau).
\]

Equation (1) gives exactly

\[
 \boxed{\frac{dy}{d\tau}=-2y^2(1-h^2y).}\tag{2}
\]

Because `0<theta(0)<=pi/2`, `z(0)<=1/2`; (1) decreases theta and preserves `0<z<=1/2`. Thus `y'<=-y^2`, so `y(tau)<=1/tau` for **every** positive physical time. On `0<=z<=1/2`, `arcsin z<=pi z/2`, hence

\[
 \boxed{\mathscr F_h(\tau)\le\frac{2\pi}{\tau},\qquad\tau>0,}\tag{3}
\]

independently of `h`, the number of periodic cells, and the initial theta in this exact homogeneous submanifold. When theta is held fixed as h shrinks, initial curvature and total physical action diverge, yet (3) still holds **inside this highly symmetric invariant sector**. For bounded physical initial connection amplitudes `theta=h a0`, the total physical action `8 S_h/h` tends to `a0^4`.

## 4. Explicit classical continuum homogeneous ODE

Writing `a_h=theta/h`, equation (1) becomes

\[
 a_h'(\tau)=-\frac2{h^3}\sin^3(h a_h/2)\cos(h a_h/2).
\]

For initial `a_h(0)=a0>=0` with `h a0<=1`, the continuum homogeneous Yang–Mills spatial-flow ODE in these conventions is

\[
 a'(\tau)=-a(\tau)^3/4,\qquad
 a(\tau)=\frac{a_0}{\sqrt{1+a_0^2\tau/2}}.
\]

Using `|sin^3 x cos x - x^3|<=|x|^5` for `|x|<=1` and the monotonicity of `-a^3/4`, the *explicit fixed-physical-time* error is

\[
 \boxed{|a_h(\tau)-a(\tau)|\le\frac{\tau h^2 a_0^5}{16},\quad\tau\ge0.}\tag{4}
\]

The physical holonomy curvature converges to `a(tau)^2`, agreeing with a genuinely nonzero non-Abelian commutator. This is a **spatially homogeneous classical continuum ODE**, not 4D constructive quantum field theory.

## 5. A finite open set of genuinely noncommuting configurations

The homogeneous submanifold itself is still **Haar-null**. We therefore give a separate, genuinely positive-measure finite-regulator extension. Denote the full product Riemannian distance on `SU(2)^{3n^3}` by `d_2` and the homogeneous initial configuration by `U_h^*`. The existing exact Wilson Hessian bound `||Hess S_h||_op<=4` applies to this periodic cell geometry too (every four-edge face has distinct links; every link meets four faces). Thus, for the full nonlinear flow,

\[
 d_2(\Phi_sU,\Phi_sV)\le e^{4s} d_2(U,V).
\]

Plaquette products are `2`-Lipschitz from product `d_2` to the SU(2) bi-invariant geodesic distance, by four-edge Cauchy–Schwarz. Therefore

\[
 \boxed{\max_p\frac{2d(U_p(\Phi_{\tau/h^2}U),I)}{h^2}
  \le \frac{2\pi}{\tau}+\frac{4e^{4\tau/h^2}}{h^2}d_2(U,U_h^*)}.\tag{5}
\]

For prescribed `eta>0` and finite `tau*>0`, the **open** ball

\[
 B_h=\{U:d_2(U,U_h^*)<r_h\},\qquad
 r_h=\min\{\tfrac14\eta h^2e^{-4\tau_*/h^2},\,\tfrac18\phi_h\},
\]

with `phi_h=2 arcsin(sin^2(theta0/2))>0`, consists of **noncommuting** configurations and satisfies the finite physical-curvature bound `2pi/tau*+eta` at time `tau*`. The second radius constraint keeps at least one commutator plaquette nontrivial. This is a true *open set* in the **full** SU(2) link space, not just the Haar-null homogeneous family.

At any fixed `h,n` the finite full Wilson/Kogut–Susskind Hamiltonian has a smooth strictly positive gauge-invariant ground state `Omega_h`. Let `m_h=min Omega_h^2>0`. The normalized product Haar measure of `B_h` has the explicit lower bound

\[
 \boxed{\nu_h(B_h)\ge m_h\left[\frac{u_h-\sin u_h}{2\pi}\right]^{3n^3}>0,\quad
 u_h=\frac{r_h}{\sqrt{3n^3}},}\tag{6}
\]

where `u_h<2pi` and the SU(2) Haar geodesic-ball volume uses the generator normalization `T=i sigma/2`. The event **"curvature bounded after flow"** is gauge invariant and contains this ball, so it also has strictly positive true finite Wilson-vacuum probability. No **lower bound uniform in h or spatial volume** is obtained: `r_h` is exponentially small in `tau*/h^2`, the number of links grows as `h^-3`, and `m_h` is not controlled uniformly. This is an explicit *finite-model positive-probability* result, **not** a typical-configuration or continuum theorem.

## 6. Independent checks and scientific boundaries

The accompanying verifier builds the actual 3D periodic original-link cubical plaquette incidence and independently evaluates the full quaternion SU(2) force, including nonzero xy commutators and zero transverse forces. It checks the invariant scalar law for 9 cases, physical-time ODE and error (4) for 15 cases, and the global-Lipschitz/tube bound on 2 fully nonhomogeneous perturbed lattice-flow integrations. Numerical tests are consistency checks; the proof is algebraic, variational and based on finite-dimensional Riemannian flow stability.

**Not established:** a positive vacuum probability *uniform* in h,R; positive-flow-time curvature estimates on generic noncommuting initial data; source-derived small action at the true weak-coupling vacuum; physical 4D Wilson/gradient flow and quantum-time correlations; nontrivial Osterwalder–Schrader reconstruction; positive spectral mass gap; any genuine Penrose/coupled-Z5 3D regulator equivalence or physical gravitational UV finiteness.

This new theorem must be separately indexed as a theorem file, with **discovery status only** in the complete catalogue and **finite/conditional/open** status in the curated mathematical-physics proof graph. No Yang–Mills P0–P5 gate or Penrose T0–T5 transfer obligation is closed.
