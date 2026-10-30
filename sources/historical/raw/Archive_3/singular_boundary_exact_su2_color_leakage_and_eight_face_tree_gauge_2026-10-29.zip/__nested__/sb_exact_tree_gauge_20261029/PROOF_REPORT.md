# The Singular Boundary — Exact physical SU(2) class-sector leakage and eight-face tree-gauge reconstruction

**Date:** 2026-10-29. **R3 independent reconstruction.** Mathematical classification: exact finite-volume, all-vertex Gauss-invariant SU(2) Wilson kinetic identity, plus a gauge-reduced construction applicable to the smallest connected eight-face patch. **The full-coupling, reflection-free Penrose cap bound remains OPEN.** The finite Q8 checks validate discrete nonabelian gauge-fixing algebra; **Q8 is not a discretization error estimate for SU(2)**, and no full eight-face SU(2) spectrum has been computed.

## 1. Physical Hamiltonian and the often-inadequate plaquette-class subspace

Consider a finite simply connected, face-complete, edge-to-edge planar rhombus disk with free boundary links, at most two faces incident to any link, and all-vertex Gauss invariance. Work in the full Haar product-link space, with its unique positive Gauss-invariant ground state. The Hamiltonian is

\[
H=\sum_{e\in E}a_e(-\Delta_e)+\sum_{q\in F}b_q(1-p_q),\qquad
p_q=\tfrac12\operatorname{ReTr}W_q,\quad a_e>0,\ b_q\ge0,
\]

where \(-\Delta\chi_j=j(j+1)\chi_j\). A face \(f\) may be magnetically deleted by taking \(b_f=0\). Denote by \(\mathcal C\) the closed subspace of physical states that are functions of the **individual** normalized plaquette traces \((p_q)_{q\in F}\), and by \(P_{\mathcal C}\) its orthogonal projection. This is the closure of tensor products of arbitrary individual SU(2) plaquette characters (the complete character-only basis), not a finite-spin truncation.

A planar primal-tree/dual-tree change of variables, with a free outer boundary, sends normalized product-link Haar on the gauge quotient to independent normalized Haar measures for each group-valued based plaquette holonomy. In particular, the \(p_q\) are independent with common density \(\rho(p)=2\sqrt{1-p^2}/\pi\) on \((-1,1)\). This is a property of the **kinematic Haar measure**, not the interacting vacuum.

## 2. SU(2) six-edge color channel

For distinct adjacent faces \(f,g\) sharing an edge \(e\), the exact normalized SU(2) gradient identity (with compatible orientations) is

\[
\boxed{\Gamma_e(p_f,p_g)
=\sum_{a=1}^3a_e\,(\nabla_e^a p_f)(\nabla_e^a p_g)
=\frac{a_e}{4}(p_{\partial(f\cup g)}-p_fp_g).}\tag{COL1}
\]

One may choose a common base point on the shared edge and write the based face matrices as \(U=p_f I+i\mathbf u\cdot\sigma\), \(V=p_g I+i\mathbf v\cdot\sigma\), with \(|\mathbf u|^2=1-p_f^2\), \(|\mathbf v|^2=1-p_g^2\). Up to harmless orientation conventions, \(p_{\partial(f\cup g)}=p(UV)=p_fp_g-\mathbf u\cdot\mathbf v\). The relative color axes are conditionally independent and uniformly oriented under kinematic product Haar, even when weighted by an arbitrary function of all individual plaquette traces. Thus

\[
\boxed{\mathbb E_0[p_{\partial(f\cup g)}-p_fp_g\mid(p_q)_{q\in F}]=0,}\tag{COL2}
\]
\[
\boxed{\mathbb E_0[(p_{\partial(f\cup g)}-p_fp_g)^2\mid(p_q)_{q\in F}]
=\tfrac13(1-p_f^2)(1-p_g^2).}\tag{COL3}
\]

Here \(\mathbb E_0\) denotes **kinematic link-Haar**, not the deleted-vacuum expectation. For rigorous use of COL2–3, choose a planar dual-tree coordinate system with the adjacent pair connected in the dual tree; this preserves the independent face-Haar law and represents the two-face union word as the product of their two face matrices. Conditioning on all individual traces then leaves their color axes Haar. The formula is independent of the coordinate choice because the left sides are gauge-invariant functions.

Haar moments are \(\mathbb E_0 p^2=1/4\) and \(\mathbb E_0 p^4=1/8\). Hence \(\mathbb E_0\Gamma_e(p_f,p_g)^2=3a_e^2/256\).

## 3. New theorem: complete plaquette-character compression is exactly a tensor product of rotors

For smooth \(\varphi,\psi\) depending only on \((p_q)\), the multivariate chain rule for the electric Dirichlet form has diagonal terms \(\Gamma(p_f,p_f)=A_f(1-p_f^2)/4\) and cross terms \(\Gamma_e(p_f,p_g)\) only when the faces share an edge. COL2 makes every cross contribution vanish upon taking kinematic Haar inner products with arbitrary \(\varphi,\psi\). The magnetic potential already preserves \(\mathcal C\), so the exact quadratic-form compression is

\[
\boxed{
P_{\mathcal C}HP_{\mathcal C}
=\sum_{f\in F}
\left\{
-\frac{A_f}{4}\left[(1-p_f^2)\partial_{p_f}^2-3p_f\partial_{p_f}\right]
+b_f(1-p_f)
\right\}
\quad\text{on }\mathcal C,\quad A_f=\sum_{e\in\partial f}a_e.}\tag{COL4}
\]

The equality means the self-adjoint Friedrichs operator associated with the compressed quadratic form, not that \(\mathcal C\) is invariant under the actual \(H\). In fact it is generally **not invariant**.

When \(b_f=0\), the unique lowest state of the compressed operator factorizes into the constant target-face rotor and independent positive single-face rotor ground states for all retained faces. Its target holonomy is therefore **exactly Haar** for every retained magnetic coupling. This is a statement about the **class-only Galerkin/compressed model**, not the actual interacting deleted vacuum. Thus even an *untruncated* basis consisting only of products of individual plaquette characters is structurally unable to decide the generic connected deleted-face cap response.

## 4. Explicit nonzero **physical center-even** leakage into the omitted color sector

The failure of invariance can be computed without perturbation theory. Let \(f,g\) share exactly one edge \(e\). The normalized physical class vector
\[
\Phi_{fg}=2\chi_1(W_f)p_g=2(4p_f^2-1)p_g,\qquad\|\Phi_{fg}\|_2=1
\]

is **target-center-even** (under the exact deleted-face center-flux involution). All retained magnetic multipliers preserve \(\mathcal C\). The individual radial electric contributions likewise stay in \(\mathcal C\). The only cross term comes from their shared link, where \(\partial_{p_f}(2\chi_1p_g)=16p_fp_g\) and \(\partial_{p_g}(2\chi_1p_g)=2\chi_1\), so their mixed second derivative is \(16p_f\). The electric operator therefore produces
\[
\boxed{(I-P_{\mathcal C})H\Phi_{fg}
=-2\Gamma_e(p_f,p_g)\,\partial_{p_f}\partial_{p_g}\Phi_{fg}
=-8a_ep_f\bigl[p_{\partial(f\cup g)}-p_fp_g\bigr].}\tag{COL5}
\]

Using COL3 and the exact Haar moments gives
\[
\boxed{\|(I-P_{\mathcal C})H\Phi_{fg}\|_2^2
=64a_e^2\frac{\mathbb E_0[p_f^2(1-p_f^2)]\,\mathbb E_0[1-p_g^2]}3
=\mathbf{2a_e^2}.}\tag{COL6}
\]

There is a second entirely center-even, unit-normalized example \(\chi_1(W_f)\chi_1(W_g)\):
\[
\boxed{\|(I-P_{\mathcal C})H[\chi_1(W_f)\chi_1(W_g)]\|_2^2=\frac{16}{3}a_e^2.}\tag{COL7}
\]

For comparison, the product of two normalized fundamental traces \(p_fp_g\) (not itself unit normalized) has off-class residual squared \(3a_e^2/64\). The exact leakage is independent of the other plaquette couplings and of the number of faces, and remains order one whenever \(a_e\) is bounded below. **It does not establish that the exact ground state has an order-one off-class component**, which depends on spectral denominators and the nonlinear dynamics. It shows why ignoring this sector can falsely produce an exactly Haar deleted face.

## 5. Exact spanning-tree gauge reduction on the first connected eight-face patch

For the 3×3 square-rhombus patch with the lower-left corner face omitted, there are 8 faces, 15 vertices and 22 edges. Choose a primal spanning tree \(T\) rooted at \(r\): it has 14 edges and leaves exactly \(E\setminus T\) with **8 chord variables**, one group variable for each face by Euler's formula. Let \(P_{r\to v}\) denote the oriented parallel transport along \(T\), and for every oriented chord \(e:s\to t\) define
\[
X_e=P_{r\to s}\,U_e\,P_{r\to t}^{-1}.
\]

Under all vertex gauge transformations this transforms only by simultaneous root conjugation \(X_e\mapsto g_rX_eg_r^{-1}\). Thus the physical Hilbert space is the conjugation-invariant subspace of \(L^2(SU(2)^8)\); the Haar norm and all magnetic plaquette words transfer exactly. On the gauge slice \(U_e=I\) for tree edges, retained Wilson potentials are explicit trace functions of products of chord variables.

The SU(2) electric kinetic energy **does not** simply become a sum of eight independent chord Casimirs. For a tree edge \(t\), let \(S_t\) be the descendant-vertex component cut off when \(t\) is removed, and write \(\mathcal L_e^a\), \(\mathcal R_e^a\) for the left and right Lie derivative on chord \(X_e\). A unit perturbation of that tree link acts on every chord as \(X_e\mapsto g^{1_{s(e)\in S_t}}X_e g^{-1_{t(e)\in S_t}}\), up to a global sign of the infinitesimal generator when the tree edge orientation points toward the root. Hence the exact physical electric form is
\[
\boxed{
\mathcal E_T(\Psi)=
\sum_{e\notin T}a_e\sum_{a=1}^3\|\mathcal L_e^a\Psi\|^2
+\sum_{t\in T}a_t\sum_{a=1}^3
\left\|\sum_{e\notin T}
\bigl[1_{s(e)\in S_t}\mathcal L_e^a-1_{t(e)\in S_t}\mathcal R_e^a\bigr]\Psi\right\|^2.}\tag{COL8}
\]

This is a complete, finite-volume, exactly Gauss-reduced SU(2) Hamiltonian specification, suitable for a genuine Peter–Weyl/spin-network truncation. Crucially it retains the noncommuting relative-color operators that COL4 removes. It is a computational construction, **not** a solution of the resulting eight-face spectral problem.

## 6. Independent deterministic audit and exact remaining gate

- `verify_su2_class_leakage.py` checks the SU(2) class-conditional color average and variance with an exact-degree-two spherical quadrature; tests the shared-link gradient identity on 34 noncommuting SU(2) configurations; verifies the exact Haar residuals \(3/64\), \(16/3\), and \(2\).
- `verify_exact_tree_gauge_q8.py` implements the exact nonabelian tree-gauge coordinate map on the eight-face graph and checks all tree- and chord-link actions, physical root conjugation, magnetic face words and the target center string. Q8 is a finite subgroup of SU(2) and checks **group action algebra**, not continuous SU(2) spectral convergence.

**PROVED:** COL1–COL8 within their declared finite-volume geometric domain. **OPEN:** a nonperturbative bound on the actual center-even *nonclass* low-frequency Schur-complement/spectral-overlap contribution and its signed effect on the deleted-face cap for a fully connected asymmetric Penrose disk; all-bulk magnetic deletion, fixed-support nonlinear covariance, physical mass gap and continuum reconstruction. Future finite-patch diagonalization must include relative-color spin-network channels and control its truncation error before it can supply evidence about these obligations.
