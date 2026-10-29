# The Singular Boundary — Independent neighbor-flux parity and controlled small-coupling cap response

**Research date:** 2026-10-29. **Status:** exact finite nonlinear SU(2) Wilson symmetry and selection rule, exact gap-dependent perturbative response bound, and an exact general abelian planar deleted-face Haar theorem. These results do **not** establish the required Penrose-uniform adverse low-energy cap response bound, a regulator-uniform physical mass gap, or continuum construction.

## 1. Actual SU(2) physical setting

Let the spatial regulator be a finite, simply connected, face-complete planar rhombus disk with all-vertex Gauss invariance. Fix an interior target face `f` and an edge-sharing neighbor `g`. Take positive electric coefficients `a_e` and the SU(2) Hamiltonian

`H(t) = H0 + t b_g(1-p_g),   H0 = sum_e a_e(-Delta_e) + sum_{k not in {f,g}} b_k(1-p_k)`, `p_g=(1/2) ReTr W_g`, for all real `t` (the physical interpolation is 0<=t<=1). On each finite disk it has a unique strictly positive normalized Gauss-invariant ground state `Omega_t`. Let `O` be any bounded real gauge-invariant multiplication observable that depends only on `W_f` (in particular the positive convolution cap source `k_a(W_f)` in the prior theorem). Its exact expectation is `F_O(t)=<Omega_t,O Omega_t>`.

## 2. Theorem PF-1: independent neighboring-center flip gives an exact even response

Because **both** face magnetic terms `f,g` are absent in `H0`, the dual-center-string incidence equation `d_1 z=delta_g` has a solution on a disk with an exterior boundary. The corresponding SU(2) link sign-flip unitary `S_g` changes **only** the sign of the full neighboring plaquette word `W_g`, leaves the target plaquette `W_f` unchanged, preserves all other plaquette words, and commutes with each electric Laplacian. In particular,

`S_g H0 S_g=H0`,  `S_g p_g S_g=-p_g`, `S_g O S_g=O`.

Consequently

**`S_g H(t) S_g = H(-t)+2t b_g I`.**                               (PF-1)

Taking normalized positive ground states and using their uniqueness gives `F_O(t)=F_O(-t)` for all real `t`; its Taylor series contains only even powers. The physical energy has `E(t)-t b_g=E(-t)+t b_g` and therefore `E'(0)=b_g` (as independently follows from the exact Haar private-edge distribution of `p_g` at t=0). Most importantly,

**`F'_O(0)=0`.**                                                   (PF-2)

This is an **exact Wilson-specific endpoint selection rule**. It holds even when both `f` and `g` lie in a multiply connected face-dual environment and neither is a dual bridge in the original one-deleted Hamiltonian. It does not assert any sign or smallness for the response on `t∈(0,1]`.

## 3. Theorem PF-2: the zero-coupling *spectral* response vanishes in each energy window

Let `K0=H0-E(0)`, `Q0=I-|Omega0><Omega0|`, `G0=Q0 K0^{-1}Q0`, and `P_{0,I}` any Borel spectral projector of `K0` on strictly positive excitation energies within an interval `I`. Because `S_g` commutes with all of `K0,Q0,G0,P_{0,I}`, and `S_g Omega0=Omega0` while `S_g O S_g=O`, the physical spectral mixed term vanishes **separately for every energy interval**:

**`<Q0 O Omega0,G0 P_{0,I} Q0(b_g(1-p_g))Omega0>=0`.**       (PF-3)

Indeed `Q0(b_g(1-p_g))Omega0=-b_g p_g Omega0` is odd under `S_g`, whereas the first vector is even. Hence the complete low-energy and high-energy pieces in the earlier `DS-3` theorem **both vanish at the double-deleted endpoint** `t=0`. The nonzero adverse response is created only as the neighbor coupling increases.

## 4. Theorem PF-3: exact gap-dependent quadratic small-coupling estimate

Let `delta0=inf(sigma(H0)\{E(0)})-E(0)>0` be the **finite-volume physical excitation gap at the double-deleted endpoint**. It is positive for each compact finite regulator, but has **no proven lower bound uniform in h**. Put `B=b_g p_g`, so `||B||<=b_g`, and `H(t)=H0+t b_g-t B`. Because a scalar term does not affect the ground-state projection `P(t)`, consider the analytic family `H0-tB`. For real `|t|<=delta0/(4b_g)`, the Riesz contour at radius `delta0/2` is separated from the excited spectrum. The Neumann expansion gives `P(t)=P0+tP1+R2(t)` and

`||R2(t)|| <= r²/(1-r)`, `r=2|t|b_g/delta0 <= 1/2`, and `rank(P1)<=2`.

`Tr(O P1)=0` by PF-1. The trace-class operator `R2=P(t)-P0-tP1` has rank at most four; therefore for bounded O,

**`|F_O(t)-F_O(0)| <= 32 ||O|| (t b_g/delta0)²`.**               (PF-4)

The constant 32 is intentionally conservative. This is a genuine **second-order nonlinear physical-sector** estimate for small neighbor coupling; it does not use a Gaussian comparison. The severe limitation is that `b_g~h^-2` and nothing establishes `delta0` comparable to `b_g`. Thus PF-4 generally controls only `|t|=O(delta0 h²)`, not the full interpolation `t=1`. It cannot prove the prior low-energy response budget by itself.

## 5. PF-4: even response does not determine the sign of curvature

A separate positive finite-dimensional comparator makes this limitation exact. Set `H0=diag(0,2,3)`, center-flip `S=diag(1,-1,1)`, `B_{01}=B_{10}=1`, `B_{12}=B_{21}=±5`, all other B entries zero, and `O=[[1,0,.3],[0,0,0],[.3,0,.5]]`, a positive semidefinite S-even observable. Then `S B S=-B`, `S O S=O`, and the unique lowest eigenstate of `H0-t B` has an even O-expectation. Yet `F''(0)` is approximately `+0.5` for the plus sign and `-1.5` for the minus sign. This is **not** a Wilson lattice model; it proves only that center-flux selection rules and positivity of an observable do not, by themselves, fix the second-order sign. A Wilson-specific sign argument would have to use more structure.

## 6. PF-5: exact planar U(1) abelian deleted-face Haar theorem (contrast, not SU(2) evidence)

On a simply connected planar U(1) lattice with open boundary and all-vertex Gauss invariance, choose independent plaquette angles `theta_f`, with product Haar measure. The exact U(1) electric quadratic form in these coordinates has **constant** coefficients `M_fg=(B diag(a) B^T)_fg`, and hence

`H^-=-sum_{f,g} M_fg partial_theta_f partial_theta_g + sum_{g!=f} b_g(1-cos theta_g)`.

Let `phi(theta_{g!=f})>0` be the normalized strictly positive ground state of the operator on the `F-1` remaining angles using the principal matrix `M_{--}`. Its lift `Phi(theta)=phi(theta_{g!=f})` is an exact positive eigenstate of the full deleted Hamiltonian: every derivative containing `partial_theta_f` annihilates it. By positivity and simplicity of the finite-volume ground state, `Phi` is the ground state. Therefore

**`P_{Omega^-}(theta_f in A)=Haar_{U(1)}(A)` for every measurable A`.**

This is an **unconditional exact all-bulk theorem in the U(1) analogue**, including cycle-rich 3×3 square disks. It does not extend to SU(2), where the face-coordinate electric cross terms are configuration-dependent through adjoint parallel transport. Its value is to identify the genuinely nonabelian source of the remaining response.

The deterministic companion diagonalizes two charge sectors of an exact 3×3 U(1) gauge disk in a charge cutoff `[-1,1]` for the eight nondeleted face Fourier modes (6561 states per sector), verifying that the deleted-face charge-zero block lies below charge ±1 and showing the expected exact decoupling. The finite truncation is a **test** of the general analytic U(1) theorem, not a proof of SU(2) behavior.

## 7. Current remaining obligations

**Proved:** PF-1 through PF-5 in their explicitly declared domains. **Open:** quantitative control of the finite physical `DS-3` adverse normalized mixed response over the entire `t∈[0,1]`, the polynomial deleted SU(2) cycle-rich flat-holonomy mass, uniform interior magnetic deletion, fixed-support connected Wilson–angle covariance, positive physical continuum gap, quartic resolvent, and full nontrivial continuum reconstruction.

A valid next proof would exploit the Wilson-specific dynamics **away from t=0** rather than infer a global sign from endpoint parity or from the abelian analogue.