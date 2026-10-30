# The Singular Boundary — R3 complete theorem/obstruction investigation

26 October 2026. Formal research memorandum. Status: **partial R3 theorems proved**; the full arbitrary-coupling, center-neutral, volume- and cutoff-uniform infrared estimate is **not proved**. This memorandum is not a continuum Yang–Mills mass-gap theorem.

## I. Model and scope

Let \(\mathcal C=(V,E,F)\) be a finite oriented 2-dimensional cell complex, with one \(SU(2)\) variable per chosen edge orientation, \(U_{\bar e}=U_e^{-1}\). Let \(\mathcal H=L^2(SU(2)^E,dU)\), \(\mathcal H_{\mathrm{phys}}=\mathcal H^{SU(2)^V}\), and
\[
H=\sum_{e\in E} a_e(-\Delta_e)+\sum_{f\in F}b_f\left(1-\tfrac12\operatorname{ReTr} W_f\right),\qquad a_e>0,\ b_f\ge0.
\]
This is the *Hamiltonian Kogut–Susskind class*. It is not automatically the exact finite-time-step logarithm of the heterogeneous Wilson transfer matrix used in Stage 26. An identification requires a separate temporal scaling/transfer-limit theorem (previous Gate D1 remains incomplete for the literal production action). Each finite H is elliptic on the compact connected product group and has bounded smooth real potential: the principal eigenfunction \(\Omega>0\) is unique and smooth, with eigenvalue \(E_0\). Gauge invariance forces \(\Omega\in\mathcal H_{\mathrm{phys}}\). Put \(K=(H-E_0)|_{\Omega^\perp\cap\mathcal H_{\mathrm{phys}}}\), and \(P_s=\mathbf 1_{(0,s]}(K)\). At fixed finite volume \(K^{-1}\) is bounded; uniformity in volume is NOT assumed.

For a smooth bounded gauge-invariant local multiplier \(B\), write \(b_B=Q B\Omega\), with \(Q=1-|\Omega\rangle\langle\Omega|\). The static infrared cross susceptibility is
\[
\chi^{<\eta}_{A,V}=-2\operatorname{Re}\langle Q A\Omega,K^{-1}P_\eta QV\Omega\rangle.
\]
This is well defined at each finite cutoff whenever the source vectors belong to the relevant domains.

## II. Theorem R3-D — Exact power-law infrared suppression for dynamical coboundaries

**Statement.** Let \(B\) be smooth, bounded, gauge invariant and local. Define \(J_B=i[H,B]\) on smooth vectors. It is a local, in general *unbounded* first-order differential observable (the magnetic multiplication potential commutes with B). The ground-state vector \(u_B=J_B\Omega\) belongs to \(\mathcal H_{\mathrm{phys}}\cap\Omega^\perp\), and for all \(s>0\):
\[
\boxed{\quad\|P_s u_B\|^2\le s^2\|QB\Omega\|^2\le s^2\|B\|_\infty^2.\quad}
\]
For any two such generators \(B,C\), the low-energy *current/current* static response satisfies
\[
\boxed{\quad |\chi^{<\eta}_{J_B,J_C}|\le 2\eta\|B\|_\infty\|C\|_\infty.\quad}
\]
Constants are independent of spatial volume, magnetic coupling and boundary topology. If \(H_a\) is normalized in physical energy units and \(\|B_a\|_\infty\) remains bounded, the purely algebraic bound is uniform in the cutoff \(a\) for the **dynamical source vectors**; this does not establish existence of their nontrivial renormalized continuum limits.

**Proof.** On \(\Omega\), \(u_B=i(H-E_0)B\Omega=iKQB\Omega\); the commutator is defined on the smooth ground state. The spectral projector commutes with K, so \(\|P_su_B\|\le s\|QB\Omega\|\). For \(u_C=iKQC\Omega\),
\[
|\langle u_B,K^{-1}P_\eta u_C\rangle|
=|\langle QB\Omega,KP_\eta QC\Omega\rangle|
\le\eta\|QB\Omega\|\|QC\Omega\|.
\]
Multiply by 2. No gap inequality was used. QED.

For \(k\ge1\) and vectors in the domain of K^k, \(u_B^{(k)}=K^k QB\Omega\) obeys \(\|P_su_B^{(k)}\|^2\le s^{2k}\|B\|_\infty^2\). This extends suppression for time derivatives but does **not** assert that higher commutators remain bounded local multipliers.

**Critical limit.** R3-D does NOT apply with the same constants to arbitrary Wilson-loop multipliers \(A\): representing \(QA\Omega=KQB\Omega\) needs \(\|QB\Omega\|\ge\|P_{I}QA\Omega\|/(\sup I)\) on an energy interval I. For a normalized eigenvector at energy \(\epsilon\), its K-preimage has norm \(1/\epsilon\), which can diverge as a gap closes. Thus extending R3-D to *all* physical sources through an inverse commutator would be circular.

## III. Theorem R3-C — Exact local current/current static-response cancellation

For smooth real gauge-invariant link multipliers B and C with **disjoint edge supports**, \(\chi_{J_B,J_C}=0\) for the full (untruncated) static susceptibility, at arbitrary magnetic coupling and any finite spatial volume. Indeed, by the exact ground-state Dirichlet form,
\[
\langle J_B\Omega,K^{-1}J_C\Omega\rangle
=\langle QB\Omega,KQC\Omega\rangle
=\sum_e a_e\int (\nabla_e B)\cdot(\nabla_e C)\,\Omega^2\,dU=0.
\]
This is an exact contact property; it does NOT imply that each infrared band contribution vanishes: low and high energy contributions can cancel. It applies to *dynamical current sources*, NOT an arbitrary remote magnetic Wilson perturbation.

## IV. Theorem R3-Z — Exact center one-form symmetry and infrared selection rule

Assume \(\mathcal C\) is a closed finite 2-complex with the plaquette Wilson action above. Let \(\alpha:E\to\{\pm1\}\) be a \(\mathbb Z_2\)-valued cellular 1-cocycle, i.e. \(\prod_{e\in\partial f}\alpha_e=1\) for each face (orientation signs immaterial in \(\mathbb Z_2\)). Define the unitary center translation
\[
(Z_\alpha\psi)(U)=\psi((\alpha_e U_e)_{e\in E}).
\]
Then \([Z_\alpha,H]=0\); it commutes with local gauge projection. If \(\alpha\) is a coboundary, \(Z_\alpha\) is a vertex-center gauge transformation and acts trivially on physical states. Thus the nontrivial action depends on \(H^1(\mathcal C;\mathbb Z_2)\). For a cellular torus, this is \((\mathbb Z_2)^2\).

The proof: Haar measure and each link Laplacian are invariant under multiplication by a fixed central sign; each plaquette holonomy acquires factor \(\prod_{\partial f}\alpha_e=+1\), so every magnetic term is invariant. Central translations commute with SU(2) gauge transformations. Uniqueness and strict positivity of the finite-volume ground state imply \(Z_\alpha\Omega=\Omega\). A Wilson loop along a closed cycle c transforms by the holonomy sign \((-1)^{\langle[\alpha],[c]\rangle}\). Every **contractible** Wilson loop and every gauge-invariant local observable supported in a contractible cell region is center-neutral. If \(P_q\) denotes a nontrivial center-charge spectral projection, then
\[
\boxed{\quad P_q A_{\mathrm{contractible}}\Omega=0,\quad
\langle A\Omega,K^{-1}P_q P_\eta V\Omega\rangle=0.\quad}
\]
This is exact for all energies, couplings and cutoffs where the torus complex and symmetry are defined; it also holds for the weighted Wilson transfer operator \(T=P e^{-V/2}C_K e^{-V/2}P\), because simultaneous central translations of its two time slices leave each temporal convolution factor invariant.

**Limits:** (a) It says nothing about the **neutral** physical glueball channel; (b) center-charged low-energy states may still exist and would matter for the gap of the entire physical Hilbert space; (c) a simply connected open Penrose patch has trivial first cohomology, so this *global* charge selection cannot be claimed there; (d) the result is a standard 1-form center symmetry realized here on a weighted Penrose gauge complex, not a consequence of the dissertation's J.

## V. Obstruction R3-O — Why the scalar sector is not controlled

For a generic local contractible plaquette multiplier \(A_f=1-\frac12\operatorname{ReTr}W_f\), the exact first-moment identity
\[
\int s\,d\mu_{A_f}(s)=\sum_e a_e\int|\nabla_e A_f|^2\Omega^2\,dU
\]
gives an upper bound on the first *positive* moment but no upper bound on \(\int_{(0,\eta]}s^{-1}d\mu_{A_f}(s)\), or on \(F_{A_f}(s)\). Local gauge Ward identities eliminate nonsinglet excitations only; \(A_f\) is a center-neutral gauge singlet and can overlap allowed arbitrarily-low-energy states in an abstract spectral model.

Logical counterexample: \(K_\epsilon=\operatorname{diag}(\epsilon,1)\) in an excited sector, a neutral bounded local source with order-one weight at \(\epsilon\) has inverse moment \(1/\epsilon\) as \(\epsilon\downarrow0\), without violating any center selection rule or an upper first-moment estimate. This is a *logical independence example*, not a Yang–Mills counterexample.

Likewise, positivity \(H_E+B\ge H_E\) for \(B\ge0\) does not imply \(\operatorname{gap}(H_E+B)\ge\operatorname{gap}(H_E)\): e.g. \(H_E=\operatorname{diag}(0,1)\) and \(B=\operatorname{diag}(1,\epsilon)\) give \(H_E+B=\operatorname{diag}(1,1+\epsilon)\) with gap \(\epsilon\). The interacting ground state changes. This specifically warns against promoting a positive kinetic-operator gap into a full-Hamiltonian excitation gap merely from operator ordering. The August 2026 Nair preprint discusses such an ordering step; any application to the interacting spectrum must separately control the shift of the ground state and excited levels. The two-by-two example does not refute a stronger model-specific inequality, but it rules out the general monotonicity inference.

## VI. Controlled infrared-scale recursion — a sufficient, unproved multiscale gate

Fix a bounded local neutral Wilson observable A and physical threshold \(\eta\). Define \(s_n=2^{-n}\eta\), \(F_n=\|P_{s_n}QA\Omega\|^2\). Suppose a **model-derived** RG/Feshbach argument supplies, uniformly in volume,
\[
F_{n+1}\le 2^{-p}F_n+D2^{-(p+\delta)n},\qquad p>1,\ \delta>0,
\]
with constants independent of n (and ultimately after R2, independent of a). By induction,
\[
\boxed{F_n\le\left(F_0+\frac{2^pD}{1-2^{-\delta}}\right)2^{-pn}.}
\]
Consequently \(F_A(s)\le C(\eta)(s/\eta)^p\) for \(s\in(0,\eta]\), after absorbing a factor \(2^p\) for dyadic interpolation. The dyadic susceptibility test then bounds \(\int_{(0,\eta]}s^{-1}d\mu_A(s)\) when \(p>1\), with exponent \(p-1\).

**Proof of induction.** Iteration yields \(F_n\le 2^{-pn}F_0+D\sum_{k=0}^{n-1}2^{-p(n-1-k)}2^{-(p+\delta)k}\le2^{-pn}(F_0+2^pD/(1-2^{-\delta}))\). Dyadic interpolation uses \(s_{n+1}<s\le s_n\) and monotonicity. QED.

**What is NOT proved:** the RG recursion for the Wilson theory. The recursion is a concrete acceptance criterion, not an independent bound on its dynamics. Verifying it would require (i) exact spatial block decimation preserving gauge constraints, (ii) an induced transfer/Schur complement or source-inserted measure with controlled kernels, (iii) estimates on neutral low-energy projectors for every scale, (iv) a contraction smaller than \(1/2\) per energy halving, (v) boundary- and patch-uniform polymer/small-field/large-field errors, and (vi) control of the resulting constants as \(a\to0\). None follows solely from finite local complexity or C5 symmetry.

Note: a power-law spectral-weight bound for a chosen class of observables is **not a mass gap**; genuinely gapless theories can have suppressed overlaps for derivative observables. A gap proof would require a sharp common positive threshold for a dense gauge-invariant observable family, or an independent coercivity inequality on the entire physical vacuum-orthogonal Hilbert space.

## VII. A constructive alternative: source-inserted Euclidean crossing estimates

For each bounded local gauge-invariant multiplier A, assume a directly established, absolutely convergent connected polymer representation of its nonnegative Euclidean autocorrelation \(C_A(t)=\langle QA\Omega,e^{-tK}QA\Omega\rangle\), and a *dynamically established* sum of source-spanning polymer activities obeying
\[
\sum_{\gamma\colon (\operatorname{supp}A,0)\leadsto(\operatorname{supp}A,t)} |w_\gamma(A)|\le C_A e^{-mt}
\]
for a common **physical** \(m>0\) independent of patch/cutoff. Then \(C_A(t)\le C_A e^{-mt}\) for each A. By spectral positivity, \(d\mu_A((0,m))=0\): otherwise spectral mass below m would contradict the long-time bound. If the span of \(QA\Omega\) for these observables is dense in \(\Omega^\perp\cap\mathcal H_{\rm phys}\) (true at a fixed finite graph if the observable family contains the full gauge-invariant cylindrical multiplication algebra), then \(\sigma(K)\subset[m,\infty)\).

This is a precise **proof architecture**, not a proof that Wilson polymer activities satisfy the spanning bound. A sufficiently small source-inserted polymer norm can establish it in a strong-coupling region. Extending the polymer contraction through an unrestricted magnetic regime and across the continuum trajectory is the hard unproved constructive step. Unlike a Poincare reformulation, the target is a specific absolute-summability estimate of terms computed from the underlying Wilson action; however a formal invocation without verifying those terms would be circular.

## VIII. An exact microscopic spectral input, and its limitation

For the temporal one-link SU(2) Wilson kernel \(k_\beta(g)=\exp[(\beta/2)\operatorname{ReTr}g]\), the convolution eigenvalue in spin j is \(c_j/(2j+1)\), with \(c_j=I_{2j}(\beta)-I_{2j+2}(\beta)\). Relative to the trivial eigenvalue, the fundamental one-link ratio is
\[
\rho_{1/2}(\beta)=\frac{I_2(\beta)}{I_1(\beta)}<1\quad(\beta>0).
\]
For \(\beta\to\infty\), \(\rho_{1/2}=1-3/(2\beta)+O(\beta^{-2})\). This exact SU(2) microscopic calculation could seed a controlled Wilson-character RG. It is **not** the many-body spectral contraction, because magnetic Wilson interactions mix link representations and gauge projection enforces singlets. The actual Stage 26 transfer action also requires source-level D1 verification.

## IX. R2 is distinct

Physical-time evolution and energy thresholds require correct a_t and anisotropic matching; magnetic link couplings scale with a. The R3-D \(s^2\) inequality is algebraically scale-independent for uniformly bounded B_a when H_a uses physical energy units, but strong/operator limits for \(J_{B_a}\Omega_a\), renormalized Wilson fields, and nontrivial excitations are **not** supplied. For multiscale R3, a contraction \(\theta(a)\) deteriorating to one, polymer masses \(m(a)\to0\), or constants growing with a^{-1} fail R2. Carry R3 and R2 as separate gates.

## X. C5 and J

C5-compatible weighted graph isomorphisms transport H, its center cocycles, spectral measures and all proved bounds. The geometric complex structure J on the perpendicular/parallel cut-and-project representation has no constructed, gap-forcing representation in the neutral physical Hamiltonian. In particular, center 1-form selection is a gauge-theoretic topological symmetry, not a consequence of J. The 3:5:8 helical sampling pitches alter observer spectral overlaps, not the interacting neutral resolvent.

## XI. Evidence-status table

- R3-D: exact s^2 spectral weight for dynamical commutator sources — **PROVED, all finite couplings and volumes**.
- R3-C: zero full static current/current susceptibility for disjoint multiplier supports — **PROVED**.
- R3-Z: \(\mathbb Z_2\) one-form center superselection on periodic spatial 2-complexes — **PROVED**, all finite couplings and volumes.
- Neutral Wilson-loop low-energy weight suppression — **OPEN**.
- Neutral distance-sensitive cross-spectral inverse-energy bound — **OPEN**.
- All-scale Wilson RG/source-inserted polymer contraction — **OPEN**.
- R2 physical continuum reconstruction and cutoff-uniform neutral gap — **OPEN**.

## XII. Literature consulted (specific scope)

1. Shen, R. Zhu, X. Zhu, *A Stochastic Analysis Approach to Lattice Yang-Mills at Strong Coupling*, Comm. Math. Phys. 400 (2023), 805–851: functional inequalities and Euclidean Gibbs clustering under strong-coupling hypotheses, **not** a general result on the quantum Hamiltonian ground-state density \(|\Omega|^2\).
2. V. P. Nair, *Towards a Proof of Mass Gap in 3d Yang-Mills Theory*, arXiv:2608.10133 (August 2026): an outlined gauge-orbit Laplacian route; does not supply an independently verified Penrose Wilson RG or all-coupling bound.
3. J. Henheik and T. Wessel, *Response Theory for Locally Gapped Systems*, J. Stat. Phys. 193, 151 (2026): theory under a local dynamical-gap hypothesis; not verification of that hypothesis for infinite-dimensional SU(2) link systems.
4. Hastings and Koma, *Spectral Gap and Exponential Decay of Correlations*, Comm. Math. Phys. 265 (2006): gap implies clustering in suitable systems, not the converse required here.

**End state:** The full R3 neutral scalar/gauge-invariant infrared theorem has NOT been proved. We have exact nonperturbative partial R3 statements, identified the algebraic class on which they are effective, and isolated a concrete Wilson-source RG induction (or source-spanning polymer crossing estimate) that must be proved before any uniform mass-gap assertion can be made.
