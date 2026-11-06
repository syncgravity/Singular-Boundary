# P2/T2 — Finite non-Abelian positive-probability neighborhoods of the cubic Cartan flow

**Date:** 2026-11-06.  **Status:** exact *finite-regulator* classical stability and measure-positivity theorem; independent finite SU(2) numerical regression. **NOT** a mesh/volume-uniform non-Abelian regularity estimate, a quantum Yang–Mills mass-gap proof, or a Penrose/gauge-gravity transfer theorem.

## 1. Precise model and inherited estimates

On the finite **open three-dimensional cubic** SU(2) original-link configuration manifold \(\mathcal M_h=SU(2)^{E_h}\), put the product bi-invariant Riemannian metric in the convention \(T_a=i\sigma_a/2\) of unit Lie-algebra length. Write

\[
 S_h(U)=\sum_{p}\left(1-\tfrac12\operatorname{tr} U_p\right),\quad
 \Phi_s(U)=\text{the full nonlinear gradient flow }\dot U=-\nabla S_h(U),\quad s=\tau/h^2.
\]

Let \(d_2\) denote the product Riemannian distance. Every plaquette has four distinct original links and every edge lies on at most four plaquettes. The finite Wilson Hessian bound from **R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md** gives

\[
 \|\operatorname{Hess} S_h\|_{\rm op}\le4,
 \qquad d_2(\Phi_sU,\Phi_sV)\le e^{4s}d_2(U,V).\tag{1}
\]

The estimate holds for **the full noncommutative link configuration space**, not only the Cartan sector; however, at physical time \(\tau\) its factor is \(e^{4\tau/h^2}\), which is not UV-uniform. The group-quaternion curvature proxy

\[
 \mathscr F_{p,h}(U)=\frac2{h^2}\operatorname{Im}(U_p)\in\mathbb R^3\tag{2}
\]

transforms by the adjoint of the gauge element at the chosen plaquette basepoint. Its **norm** is gauge invariant. This is a group-valued *proxy*, not an independently constructed continuum curvature field; at a Cartan flux \(U_p=\exp(2q_pT_3)\), it equals \(2\sin q_p/h^2\) in a fixed color direction and is bounded by the lifted curvature \(2|q_p|/h^2\).

From the four-link telescoping identity, the bi-invariant group distance bound, and the product metric,

\[
 \max_p\left|\mathscr F_{p,h}(U)-\mathscr F_{p,h}(V)\right|
 \le\frac8{h^2}d_2(U,V).\tag{3}
\]

One may use the same bound after the flow and combine (1)–(3). No logarithm branch or commutative assumption is needed for (1)–(3).

## 2. A gauge-invariant, positive-probability noncommuting tube

Let \(U_h^{\rm C}\) be one *actual original-link* Cartan-planar configuration of the invariant class in **R3_EMBEDDED_CARTAN_NONLINEAR_POSITIVE_RADIUS_SMOOTHING_2026-11-06.md**. Assume its lifted flux is nonwinding and its **three-dimensional classical physical action** satisfies

\[
 \mathscr E_h(U_h^{\rm C})=\frac8h S_h(U_h^{\rm C})\le M.
\]

The Cartan/Nash theorem supplies a constant \(C_{\rm C}(M,\tau)\), independent of sufficiently small \(h\) and the specified box family, with

\[
 \max_p |\mathscr F_{p,h}(\Phi_{\tau/h^2}U_h^{\rm C})|
 \le C_{\rm C}(M,\tau),\qquad \tau>0.\tag{4}
\]

For every **finite** \(h,R,\tau>0\), put

\[
 \boxed{\delta_{h,R}(\tau)
 =\min\left\{\frac{h^2}{8}e^{-4\tau/h^2},\ \frac{h}{32F_h}\right\}>0.}\tag{5}
\]

Let \(\mathcal G_h=SU(2)^{V_h}\) act on link configurations by local gauge transformations. Define the **gauge-invariant open tube**

\[
 \mathcal U_{h,\tau}=\left\{U:\inf_{g\in\mathcal G_h}d_2\big(U,g\cdot U_h^{\rm C}\big)<\delta_{h,R}(\tau)\right\}.\tag{6}
\]

**Theorem (exact, finite regulator).** Every \(U\in\mathcal U_{h,\tau}\) obeys

\[
 \boxed{\mathscr E_h(U)<M+1,\qquad
 \max_p\left|\mathscr F_{p,h}(\Phi_{\tau/h^2}U)\right|
 \le C_{\rm C}(M,\tau)+1.}\tag{7}
\]

The tube is nonempty and contains a positive-product-Haar-measure subset of genuinely **noncommuting** SU(2) fields, for example those with two noncommuting based plaquette holonomies. The noncommutation condition is gauge invariant after parallel transport to a shared basepoint. The noncommuting configurations are generic inside this tube (the commuting commutator locus is a proper real-analytic zero set).

**Proof.** Pick a gauge representative \(g\cdot U_h^{\rm C}\) at distance \(d_2<\delta\). The plaquette action is Lipschitz:
\(|S_h(U)-S_h(g\cdot U_h^{\rm C})|\le4F_h\delta\). Hence
\(\mathscr E_h(U)\le M+32F_h\delta/h<M+1\). By gauge equivariance of \(\Phi_s\), (1)–(4) and the first term of (5),

\[
 \max_p|\mathscr F_{p,h}(\Phi_sU)|
 \le C_{\rm C}(M,\tau)+\frac8{h^2}e^{4\tau/h^2}\delta
 \le C_{\rm C}(M,\tau)+1.
\]

For the measure claim, a sufficiently small open perturbation of two suitably based plaquette holonomies in independent SU(2) directions makes their commutator nonzero. The commutator is a nontrivial real-analytic function of all links, so its zero set has zero Haar volume. The tube is open and contains a product neighborhood, hence has positive Haar volume. This completes the finite classical proof.

## 3. Exact positive measure under the *actual* finite Wilson vacuum

At each fixed regulator, the unique positive smooth **interacting quantum** ground state \(\Omega_{h,R}\) gives a probability density \(\Omega_{h,R}^2\) with respect to normalized link-product Haar. Its finite strict minimum \(m_{h,R}=\min\Omega_{h,R}^2>0\). Using normalized SU(2) Haar geodesic-ball volume in the stated metric,

\[
 p(r)=\operatorname{Haar}\{U:d_{SU(2)}(U,I)<r\}
 =\frac{r-\sin r}{2\pi},\quad 0<r<2\pi,\tag{8}
\]

and the product ball of per-link radius \(r=\delta/\sqrt{E_h}\), the exact lower bound is

\[
 \boxed{
 \nu_{h,R}(\mathcal U_{h,\tau})
 \ge m_{h,R}\left[p\left(\frac{\delta_{h,R}(\tau)}{\sqrt{E_h}}\right)\right]^{E_h}>0.}\tag{9}
\]

The subset of **noncommuting** fields has the same lower bound, since the commuting locus has Haar measure zero. This is a genuine positive-probability statement about the actual finite interacting measure, **not a simulation or calculation of its full vacuum density**.

### Why (9) does not transfer to the continuum

The certified tube radius is at most \((h^2/8)e^{-4\tau/h^2}\). For fixed positive \(\tau\), it shrinks *exponentially in* \(1/h^2\), and the product-ball probability certificate shrinks further as \(E_h\sim h^{-3}\) on a fixed box. Its unknown prefactor \(m_{h,R}\) is itself not uniform. **Neither (7) nor (9) produces an \(h,R\)-uniform lower probability bound**, a typical-field estimate, control over commutator terms for arbitrary interacting configurations, or a nontrivial continuum measure. In particular the infinitely narrow open tube is not a replacement for the full non-Abelian Nash estimate in the true vacuum.

## 4. Independent executable checks

The companion verifier `research/scripts/verify_nonabelian_cartan_tube_2026_11_06.py` reconstructs the actual full **3D cubic original-link** SU(2) Wilson gradient from the existing quaternion implementation, chooses exact Cartan-planar reference configurations, and adds random **three-axis noncommuting perturbations**. It integrates both full SU(2) flows and checks the product-group Hessian/Grönwall distance bound, the plaquette-imaginary-curvature stability bound, the analytic SU(2) Haar cap-volume expression, the finite action-tube radius and a nonzero gauge-covariant commutator of two based plaquettes. Tests on open cubic n=2,3,4 meshes are numerical regressions, **not samples from the actual quantum interacting vacuum**. Check data, source hashes and the script are archived together.

## 5. Open interfaces

1. Prove a **mesh- and volume-uniform, positive-probability** nonlinear curvature bound for noncommuting fields under the actual weak-coupling interacting Wilson vacuum. The exponential factor in (1) is much too large.
2. Establish a physically appropriate **four-dimensional** gauge-covariant flow and renormalized nonvanishing flowed-field covariance, rather than this spatial classical curvature proxy.
3. Prove a uniform complete interacting **energy-dependent Schur/long-physical-time correlation** comparison and nontrivial Osterwalder–Schrader reconstruction with positive infrared spectral threshold.
4. Construct/identify the genuine Penrose-associated 3D quasicrystalline source regulator and the **independent** physical gravitational UV operator. A cubic control does not prove either of these.

**All P0–P5 YM gates, T0–T5 transfer obligations and the independent gravity objective remain OPEN.** Inclusion in the theorem index is *document discovery*, not an independent proof endorsement.
