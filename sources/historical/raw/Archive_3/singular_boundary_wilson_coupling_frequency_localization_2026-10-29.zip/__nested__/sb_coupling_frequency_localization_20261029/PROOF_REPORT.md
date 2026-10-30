# The Singular Boundary — Exact coupling–frequency localization of SU(2) Wilson response

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Status:** rigorous finite-volume, fully nonlinear Gauss-invariant SU(2) Wilson theorem for any adjacent face pair in an edge-to-edge planar disk, including fully connected, reflection-free interiors. This theorem is **about the neighboring plaquette's positive inverse-energy self-susceptibility**, not the **signed cap–neighbor mixed response**. The full physical Penrose flat-cap bound, uniform physical mass gap, quartic resolvent, fixed-support connected covariance and continuum reconstruction are OPEN.

## 1. Physical setup and the full-time spectral measure

For a target face f and edge-sharing neighbor g, permanently delete the magnetic term of f and interpolate g:

\[
H(u)=T+\sum_{q\notin\{f,g\}} b_qd_q +u b_gd_g,\quad W=b_gd_g,\quad d_q=1-p_q,\quad p_q=\tfrac12\operatorname{ReTr}W_q,\quad 0\le u\le 1.
\]

Every edge has a strictly positive electric coefficient a_e and is incident to at most two faces. Let \(A_g=\sum_{e\in\partial g}a_e\) and let \(e_0\) be the shared edge. The unique positive physical vacuum at u is \(\Omega_u\), its energy is \(E(u)\), \(Q_u=1-|\Omega_u\rangle\langle\Omega_u|\), and \(K_u=H(u)-E(u)\). No regulator-uniform spectral gap is presumed. At u=0 the shared edge e0 occurs in no retained magnetic term, so p_g has exactly Haar law and \(E'(0)=b_g\).

Define a positive Borel measure on coupling × excitation energy by

\[
\mu(J\times I)=\int_J\langle Q_uW\Omega_u,\;K_u^{-1}P_{u,I}Q_uW\Omega_u\rangle du,
\]

for measurable \(J\subset[0,1]\), \(I\subset(0,\infty)\). At finite volume the inverse is the reduced physical resolvent on Q, so this measure is finite. Its full excitation-energy mass at u is the **full-time** (time-integrated) susceptibility \(\chi_{WW}(u)=\langle Q_uW\Omega_u,K_u^{-1}Q_uW\Omega_u\rangle\). This is **not** the signed mixed cap–driver measure.

## CL-1 — Coupling boundary-layer localization (new joint consequence)

At each finite volume analytic perturbation theory gives \(E'(u)=\langle W\rangle_u=b_g\langle d_g\rangle_u\) and \(E''(u)=-2\chi_{WW}(u)\). Hence the exact identity is

\[
\mu([0,s]\times(0,\infty))=\tfrac12(E'(0)-E'(s))=\tfrac{b_g}2-\tfrac12 E'(s),\quad 0<s\le1.
\]

The previously proved *private-edge* magnetic restoration comparison applies to \(u\mapsto H(u)\) with magnetic coefficient \(s b_g\), and has uniform constant \(c_0=3/(2\sqrt2)\):

\[
E(s)-E(0)\le c_0\sqrt{A_gs b_g}.
\]

Because E is concave, \(E'(s)\le[E(s)-E(0)]/s\) (and is nonnegative). Thus, **uniformly in all other magnetic couplings and the number of faces**,

\[
\boxed{\mu([s,1]\times(0,\infty))\le\tfrac{c_0}2\sqrt{A_gb_g/s},\quad
\mu([0,s]\times(0,\infty))\ge\tfrac{b_g}2\left[1-c_0\sqrt{A_g/(s b_g)}\right].}\tag{CL1}
\]

Fix any \(0<\eta<1\), let \(A_g\le A_+\), and select a **fixed**, h-independent \(C\ge c_0^2A_+/\eta^2\). For \(b_g\ge C\), take \(s_C=C/b_g\). Then

\[
\boxed{\mu([0,s_C]\times(0,\infty))\ge(1-\eta)b_g/2.}\tag{CL2}
\]

The total mass is \(\mu([0,1]\times(0,\infty))=(b_g/2)\langle p_g\rangle_1\le b_g/2\), so the **fraction** of full-time neighboring susceptibility in the short restoration interval is at least \(1-\eta\). At the Penrose coefficient scale \(b_g\asymp h^{-2}\), that interval has width \(O(h^2)\). This result is nonperturbative at arbitrary fixed C; it does not use the small-coupling Taylor radius, which may be volume-dependent.

## CL-2 — Simultaneous low-excitation localization

The existing nonlinear integrated first spectral moment theorem is

\[
\int_0^1 m_{1,u}(W)du\le c_1A_g^{3/2}b_g^{3/2},\qquad c_1=\frac{3}{4\sqrt2}=c_0/2.
\]

For a positive spectral energy cutoff \(\Lambda\), \(\lambda^{-1}\mathbf1_{\lambda>\Lambda}\le\lambda/\Lambda^2\) implies

\[
\mu([0,1]\times(\Lambda,\infty))\le\frac{c_1 A_g^{3/2}b_g^{3/2}}{\Lambda^2}.
\]

Subtract the UV remainder from CL1 to obtain the **rigorous coupling–frequency rectangle bound**

\[
\boxed{\mu([0,s_C]\times(0,\Lambda])\ge \frac{b_g}2\left[1-c_0\sqrt{A_g/C}\right]-\frac{c_1A_g^{3/2}b_g^{3/2}}{\Lambda^2}.}\tag{CL3}
\]

With \(A_g\le A_+\), \(b_g\in[\beta_-h^{-2},\beta_+h^{-2}]\), \(C\ge c_0^2 A_+/\eta^2\) fixed and \(\Lambda_h=Lh^{-11/8}\), the high-frequency correction divided by \(b_g/2\) is \(O(h^{7/4})\). Therefore, for sufficiently small h,

\[
\boxed{\frac{\mu([0,C/b_g]\times(0,Lh^{-11/8}])}{\mu([0,1]\times(0,\infty))}
\ge 1-\eta-O_{A_+,\beta_\pm,L}(h^{7/4}).}\tag{CL4}
\]

This identifies where almost all positive **driver self-susceptibility** is located. It says nothing about the signed relative overlap with the target cap, and must not be represented as a low-energy cross-response estimate.

## CL-3 — Haar-order deleted cap *within the localized coupling layer*

For the same shared edge \(e_0\), at coupling \(u\) the **only** remaining magnetic plaquette depending on \(U_{e_0}\) is g, with coefficient \(ub_g\le C\). Separate the Hamiltonian into \(a_{e_0}(-\Delta_{e_0})+H_{\neg e_0}+V_{e_0}\), where \(0\le V_{e_0}\le 2C\) and \(H_{\neg e_0}\) is independent of that link. The already established LH-1 local heat-kernel Harnack theorem applies *without* any bound on the other retained face potentials. If \(k_1(U)\) is the positive SU(2) heat kernel at Laplacian time 1 and \(m_1=\min k_1>0\), \(M_1=\max k_1<\infty\), then for any two values of the shared link at fixed remaining links,

\[
\frac{\Omega_u(U_{e_0},\mathbf z)}{\Omega_u(U_{e_0}',\mathbf z)}\ge q_C,
\qquad q_C=e^{-2C/a_-}\frac{m_1}{M_1}>0.
\]

Thus, for every event \(B\) depending only on the target holonomy, the conditional one-link density is bounded below by \(q_C^2\) times normalized Haar. In particular, for every \(0\le u\le C/b_g\), every \(a\in(0,\pi/2)\), and the positive convolution cap \(k_a=\phi_a*\phi_a^\vee\),

\[
\boxed{\Pr_{\Omega_u}(W_f\in B_a)\ge q_C^2\operatorname{Haar}(B_a),\quad
F_a(u)=\langle k_a(W_f)\rangle_u\ge q_C^2\alpha_a^2.}\tag{CL5}
\]

At \(a_h=\arccos(1-h)\asymp h^{1/2}\), this gives \(\Pr(d_f\le h)\ge c_C h^{3/2}\) **throughout the boundary layer**. The constant \(c_C\) can be extremely small for large C, but is independent of h and volume. The nontrivial result is the *simultaneous* CL4 + CL5: an arbitrarily large fraction of full-time driver susceptibility lies in a gap-free Haar-cap-safe coupling-energy region. The single-link Harnack theorem itself is **prior work** and is not presented as a new isolated proof.

## CL-4 — Exact bridge-endpoint susceptibility witness

At u=0, p_g is Haar and \(\langle p_g\rangle_0=0\), \(\mathrm{Var}(p_g)=1/4\). The exact Wilson first f-sum is

\[
m_{1,0}(p_g)=\frac{A_g}{4}\langle1-p_g^2\rangle_0=\frac{3A_g}{16}.
\]

Spectral Cauchy yields \(\langle Qp_g\Omega_0,K_0^{-1}Qp_g\Omega_0\rangle\ge (1/4)^2/(3A_g/16)=1/(3A_g)\). Thus

\[
\boxed{\chi_{WW}(0)\ge\frac{b_g^2}{3A_g}.}\tag{CL6}
\]

This is a genuine physical SU(2) Wilson lower bound, uniform in volume, and provides an independent check of why the coupling layer starts at scale \(b_g^{-1}\) in the strong magnetic regime. It does not assert that the target mixed response is large; at the endpoint the target-cap mixed response vanishes by center-parity selection.

## CL-5 — Exact restricted *late-coupling* cap-response gate (not proved in the connected bulk)

Define the signed full-time mixed Wilson susceptibility

\[
\mathcal C_{a,g}(u)=\operatorname{Re}\langle Q_uk_a^+\Omega_u,K_u^{-1}Q_u(b_gd_g)\Omega_u\rangle.
\]

The exact ground-state perturbation identity yields

\[
\frac{d}{du}\sqrt{F_a(u)}=-\frac{\mathcal C_{a,g}(u)}{\sqrt{F_a(u)}}.
\]

By CL5, at the end of the susceptibility-concentrated interval \(s_C=C/b_g\) one has \(\sqrt{F_a(s_C)}\ge q_C\alpha_a\). Therefore the **exact inequality**

\[
\boxed{\sqrt{F_a(1)}\ge q_C\alpha_a-\int_{s_C}^1\frac{[\mathcal C_{a,g}(u)]_+}{\sqrt{F_a(u)}}du.}\tag{CL7}
\]

In particular a **sufficient but unproved** late-stage condition is \(\int_{s_C}^1[\mathcal C_{a,g}(u)]_+/\sqrt{F_a(u)}du\le q_C\alpha_a/2\). It would imply \(F_a(1)\ge q_C^2\alpha_a^2/4\) and, using \(k_a\le\nu_a\mathbf1_{B_a}\), a Haar-order \(\Pr_{\Omega_1}(W_f\in B_a)\ge q_C^2\alpha_a^2/(4\nu_a)\). This is a **reduced, explicitly late-coupling obligation**, not an estimate of the right-hand side. The large driver autocorrelation concentrated in the early layer is not a substitute for this signed mixed bound.

## Verification and scope

The deterministic companion script uses the **continuous SU(2) character basis**, not a finite group surrogate, to diagonalize the one-rotor Hamiltonian \(H(x)=n(n+2)+x(1-p)\) with A=4. It verifies the exact full-time energy-derivative sum rule by quadrature for b=100,400,1600, the coupling-layer lower bound, the spectral UV first-moment bound, and the SU(2) heat kernel positivity/normalization. The rotor is a finite fully nonlinear SU(2) benchmark for the identities and **not** a simulation of the connected Penrose many-link ground state. The analytical CL1–CL6 proofs are for the full physical Wilson Hamiltonian.

**Crucial remaining obligation:** prove the *signed* long-time cap–driver spectral overlap in the **late strong-coupling interval** \(u\in[C/b_g,1]\), or bypass that by establishing the polynomial deleted-cap probability directly at \(u=1\). The fact that the driver **self**-susceptibility has arbitrarily little relative mass there does not, by itself, control the **mixed** response because the cap's inverse self-susceptibility is large (the prior in-model Cauchy no-go). No continuum mass gap or nonlinear full-bulk claim is made.
