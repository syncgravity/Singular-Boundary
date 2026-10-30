# R3-IR — Physical third-spectral-moment Ward theorem and nonlinear Gaussian-scale force control

**Date:** 2026-10-28. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Classification:** exact finite-regulator gauge-invariant SU(2) triple-commutator identity and a uniform fixed-physical-region third-moment estimate under the explicitly stated Penrose coefficient, local-score and collar assumptions. Consequences: `m3(A_h)=O(h^-2)`, `m2(A_h)=O(h^-1)`, and the previously open `Var(F_h)=O(1)`. These assertions are **about the declared nonlinear Wilson Hamiltonian's true interacting vacuum**, not its Gaussian tangent. They do **not** establish a nonzero limiting source variance, an upper variance bound, a mass gap, a quartic resolvent estimate, or the Stage7/26 source correspondence. No Monte Carlo or modifications of original archives.

## 1. Hypotheses and source provenance

Current live audit-branch inputs inspected: `R3_IR_JOINT_FORCE_COVARIANCE_WARD_2026-10-28.md` (JF-1–JF-10), `R3_IR_WEIGHTED_SCORE_SECOND_SPECTRAL_MOMENT_2026-10-28.md` (WS-1–WS-9), `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-1/VF-8), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1), `R3_IR_QUANTUM_MIXED_HESSIAN_WARD_GAUSS_AUDIT_2026-10-28.md` (Gauss-sector distinction), and `R3_IR_SHARED_EDGE_GAUSSIAN_SECOND_MOMENT_2026-10-28.md` (separate tangent benchmark). The historical Stage7/26 Hamiltonian correspondence is not certified.

Let `G_h` be a finite edge-to-edge complete planar rhombus disk, four boundary links per face, each link incident to at most two faces. Work in `L²(SU(2)^E,dU)` with the physical invariant reducing subspace. Let

`H_h=T_h+V_h`, `T_h=sum_e a_e(-Delta_e)`, `V_h=sum_f b_f(1-p_f)`, `p_f=½ReTr W_f`, `a_min<=a_e<=a_max`, and `b_f>=0`.

Fix an interior physical disk region D, its incident links S, and crossing face collar C(D). Assume `b_min=β_min/h²` on D, `b_f<=β_max/h²` on D∪C, `|D|<=C_F/h²`, `|C|<=C_C/h`, and the **independently proved actual-vacuum regional comparison** `Δ_D=E0(H)-E0(H_out)<=C_E/h³`. This implies `Eν∑_D d_f<=C_E/(β_min h)`. The collar contributes `∑_C d_f<=2|C|` deterministically. Constants may depend on positive a_min, a_max, β_min, β_max, C_F, C_C and C_E, but not h or ambient volume when the full collar exists.

Take any real, **signed** weights `|q_f|<=q_*` on D, and define `Y_h=h∑_D q_f d_f`, `A_h=(Y_h−ν_hY_h)/√h`. Let Ω_h be the unique positive Gauss-invariant ground state, `K_h=H_h−E0` and ν_h=Ω_h²dU. The physical spectral moments are

`m_{k,h}(A_h)=〈A_hΩ_h,K_h^k A_hΩ_h〉=∫ E^k μ_h(dE)`.

The source is smooth and bounded at fixed finite h, so all stated commutator form calculations and spectral moments are finite on the smooth vacuum core.

## 2. Theorem TS-1 — The exact third spectral f-sum and magnetic separation

For any smooth real Gauss-invariant multiplication source Y, let `C=[H,Y]=[T,Y]`, an anti-selfadjoint first-order differential operator. Then

**`m3(Y) = −½〈Ω,[C,[H,C]]Ω〉`.** (TS-1)

This follows directly from the vacuum spectral resolution: for each excitation energy E>0, the contribution to `〈Ω,[C,[H,C]]Ω〉` is `−2 E³ |〈n,YΩ〉|²`. The entire commutator is gauge invariant because H and Y are, and is evaluated in the *physical* vacuum.

Since `[V,C]=2Γ(V,Y)` is a multiplication operator, and `[C,f]=−2Γ(Y,f)` for multiplication f,

**`m3(Y)=m3^T(Y)+m3^V(Y)`,**

**`m3^T(Y)=−½〈Ω,[C,[T,C]]Ω〉`,**

**`m3^V(Y)=2 Eν[Γ(Y,Γ(V,Y))]`.** (TS-2)

Here `Γ(f,g)=∑_e a_e∇_ef·∇_eg` and neither m3^T nor m3^V is required to be nonnegative separately. These identities are exact at finite nonlinear SU(2) coupling. No logarithmic-vacuum Hessian appears.

## 3. Theorem TS-2 — Local electric commutator estimate (all mixed links retained)

Fix an orthonormal basis of left-invariant SU(2) derivatives `D_i=D_e^α` (three per link), and put `a_i=a_e`, `Δ_a=∑_i a_iD_i²` and `T=−Δ_a`. SU(2) Casimir centrality gives `[T,D_i]=0` exactly. Define

`s=Δ_aY`, `v_j=2a_jD_jY`, `C=−s−∑_jv_jD_j`.

Repeated use of `[T,f]=−Δ_a f−2∑_i a_i(D_if)D_i` yields the **exact operator expansion**

`[T,C]=(Δ_a s)+2∑_i a_i(D_i s)D_i+∑_j(Δ_a v_j)D_j+2∑_{i,j}a_i(D_iv_j)D_iD_j`. (TS-3)

The commutator `[C,[T,C]]` has order **at most two**. The potential third-order symbols cancel by the Leibniz rule; commutators among orthonormal Lie derivatives on the same SU(2) link remain order two with uniformly bounded structure constants.

**Quantitative locality lemma.** For `Y=Y_h`, each nonzero derivative of Y of any fixed positive order is supported on a single face's four links, involves at most two incident faces per link, and has absolute value bounded by `c_k h q_*` for derivative order k. This is immediate from the fundamental 2×2 SU(2) matrix product: each derivative inserts a normalized Lie generator with uniformly bounded norm. In particular, derivatives of `s` and `v_i` are O(h) and have bounded edge-neighborhood overlap, although `s` itself may have an O(h^-1) *constant summation component*. That undifferentiated global component disappears from `[C,[T,C]]` because two multiplication operators commute and every nonmultiplication commutator differentiates s.

Expanding `[C, (TS-3)]` using `[D_i,f]=D_if` and `[D_i,D_j]=∑_k c_{ij}^kD_k` gives a second-order differential operator whose second-order coefficient matrix has uniformly O(h²) *row/column absolute sums*, and whose first-order and zero-order coefficients have total local size O(h²|D|). All coefficient derivatives needed for Haar integration by parts obey the same locality and O(h²) bounds. This follows term-by-term because every surviving coefficient is a product of two positive-order derivatives of Y; whenever the two derivatives live on different faces, their neighborhoods must intersect for the commutator to survive. There are at most 4 faces per edge neighborhood at any fixed commutator depth and at most 24 orthonormal components per face, independent of mesh refinement. **No term proportional to the undifferentiated O(h^-1) aggregate s survives.**

Using the uniform row-sum estimate for the second-order coefficients, integrating one derivative onto the real smooth Ω, and bounding first-order terms by Cauchy–Schwarz and Young gives the **finite-model kinetic commutator form bound**

**`|m3^T(Y_h)|<=C_T q_*² h² [ ∑_{e∈S}a_e||∇_eΩ_h||²+|D| ]`.** (TS-4)

The constant `C_T` depends only on SU(2) generator normalization, the four-edge/at-most-two-face incidence constraints, a_min and a_max, not on h, the number of faces or ambient volume. The above explicit formula TS-3 and local coefficient row-sum argument are a full finite-order differential-operator proof of this bound, rather than an assumption of bounded third moments. Since `∑_{e∈S}a_e||∇_eΩ_h||²=EνT_S<=Δ_D`, the regional score comparison gives

**`|m3^T(Y_h)|<=C_T q_*² h²(Δ_D+|D|)=O(h^-1)`.** (TS-5)

This bound uses **only first** derivatives of the true ground state. It is independent of the unresolved `Hess logΩ` contraction in the Bochner report.

## 4. Theorem TS-3 — Magnetic triple commutator controlled by regional curvature

With the same orthonormal Lie-derivative frame, the magnetic term has the **exact finite product expansion**

`Γ(Y,Γ(V,Y))=∑_{i,j}a_i a_j (D_jY)[(D_jD_i V)(D_iY)+(D_iV)(D_jD_iY)]`. (TS-6)

For a single plaquette f, the SU(2) trace derivative satisfies `|D_i p_f|²<=d_f/2` on incident links and `|D_jD_i p_f|<=c_2` uniformly for incident link pairs. All derivatives vanish on links outside the plaquette. Applied to the two Y-derivatives and V-derivatives in TS-6, these inequalities, edge incidence ≤2, and `2√(d_f d_g)<=d_f+d_g` yield the **pointwise locality bound**

**`|Γ(Y_h,Γ(V_h,Y_h))| <= C_V a_max²q_*² h² (β_max/h²) [∑_{f∈D}d_f+∑_{g∈C(D)}d_g]`.** (TS-7)

`C_V` is an absolute geometric constant; no independent-face factorization or clustering is used. Faces outside D∪C(D) cannot contribute because their Wilson derivatives have no shared link with the support of Y. Consequently

**`|m3^V(Y_h)| <= 2C_Va_max²q_*² β_max [C_E/(β_min h)+2C_C/h]=O(h^-1)`.** (TS-8)

The magnetic bound and electric bound hold at the **original nonlinear coupling**, not the Gaussian tangent approximation.

## 5. Theorem TS-4 — New interacting second moment and centered-score variance bounds

Combining TS-1 through TS-8 yields

**`0<=m3(Y_h)<=C_3/h`, `0<=m3(A_h)<=C_3/h²`.** (TS-9)

The independently established curvature-weighted f-sum gives `m1(A_h)<=C_1` for arbitrary bounded signed q. Cauchy–Schwarz on the *positive physical spectral measure* gives `m2(A_h)^2<=m1(A_h)m3(A_h)`. Therefore

**`m2(A_h)<=sqrt(C_1 C_3)/h`.** (TS-10)

By the exact previously proved joint-force identity (JF-8),

`Varν(F_h)=h m2(A_h)+Varν(D_h)+2EνΓ(D_h,Y_h)`.

The independently proved `Var(D_h)=O(1)` and `EΓ(D_h,Y_h)=O(h)` therefore give the major new **nonlinear** consequence

**`Varν(F_h)=O(1)`.** (TS-11)

Equivalently, the directional logarithmic-vacuum curvature from the full mixed-link Bochner formula (BW-6), `C_h(Y)=h m2(A)-Eν G_h(Y)`, is bounded above and below by constants; the previously **open** BW-7 upper bound is now satisfied under the declared regional assumptions. This does not imply the physical spectral gap or the source variance upper bound.

**Improved variance lower envelope (nonnegative macroscopic tests).** Under the extra conditions of VF-8 (`q_f>=0`, `h²∑q_f>=q_mass>0`, `a_min>0`), `m1(A_h)>=m_*>0`. Then `v_h m2(A_h)>=m1(A_h)^2` yields

**`Varν(A_h)>=c h`, equivalently `Varν(Y_h)>=c h²`.** (TS-12)

This is the **Gaussian-scale sharp-order lower envelope** for the critically normalized source, improving the preceding `c h³` normalized lower bound. The right side still tends to zero; nonzero continuum variance is **not** proved.

**Natural-energy spectral window.** With Λ_h=2sqrt(C_1C_3)/(m_*h),

`∫_(Λ_h,∞) E μ_h(dE)<=m2(A_h)/Λ_h<=m_*/2`; hence `∫_(0,Λ_h] E μ_h(dE)>=m_*/2` and

**`μ_h((0,Λ_h]) >=(m_*²/(4sqrt(C_1C_3)))h`.** (TS-13)

The last inequality is Cauchy–Schwarz on the restricted first moment and the full second moment. All energies in this result are **physical Gauss-invariant** excitation energies. It localizes a nonzero first spectral moment below the natural cutoff O(h^-1), compared to the former O(h^-3) result, but does not establish spectral mass at bounded energy as h→0.

## 6. Exact interacting physical SU(2) one-plaquette verification

For a single open four-link plaquette with equal electric a=1 and magnetic b≥0, the physical character Jacobi Hamiltonian is `Hχ_n=[n(n+2)+b]χ_n−(b/2)(χ_(n−1)+χ_(n+1))`, and `Y=h(1-p)` with h=0.1. The source p=(1/2)Tr U is multiplication by the 1/2-neighbor Jacobi matrix. Independently compute m1, m2, m3 from `K^k` and from the exact triple commutator `−½〈[C,[H,C]]〉`.

The magnetic contribution can be computed *independently* from SU(2) calculus as

`m3^V(Y)=4a² b h²〈p(1−p²)〉`.

Deterministic character-basis diagonalizations of sizes 24,36,48,72 give agreement between the spectral and triple-commutator m3 and between the commutator and SU(2) magnetic formula for b=0,0.5,5,20. At b=5: `m1(Y)=0.006076014573`, `m2(Y)=0.032552766040`, `m3(Y)=0.186776090537`, `m3^V(Y)=0.047406867062`, `m3^T(Y)=0.139369223475`. The spectral Cauchy inequality `m2²<=m1m3` holds. The verifier also checks the canonical three-face ten-edge Penrose **spatial** fixture and incidence two. This finite check is not a proof for every Penrose refinement or temporal Q14.

## 7. Evidence boundary and remaining tasks

**New independently proved nonlinear statements:** exact physical third spectral Ward decomposition TS-1/TS-2; electric finite-range commutator estimate TS-4 from explicit TS-3 and first-order regional Fisher energy; magnetic curvature-bound estimate TS-7; third spectral moment TS-9; Gaussian-compatible interacting second moment TS-10; centered score-force variance TS-11; improved source variance lower envelope TS-12 under additional nonnegative-source assumptions. The finite h theorem uses all **mixed** link derivatives, not diagonal Hessians or a Gaussian approximation.

**Still open:** source **variance upper** bound and a nonzero limiting variance lower bound; physical regulator-uniform gap and all-excitation control; quartic nonlinear inverse resolvent; infinite-volume quantum field; Stage7/26 source identity. A source-specific second spectral moment O(h^-1) is not itself a physical mass gap and does not imply variance survival.

**Next noncircular priority:** use the newly controlled third spectral moment and physical source response to bound *spectral weight at finite energies*, or establish an independent upper variance estimate / source-specific lower spectral edge without importing the Gaussian tangent. The Gaussian-scale moment improvement cannot be used as proof of an interacting continuum gap. Original archives unchanged, no Monte Carlo.
