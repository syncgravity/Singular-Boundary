# Independent State of the Proof — initial source-grounded audit (2026-10-28)

**Status:** initial independent reconstruction, not a completed historical source review or a mass-gap proof. **Read-only verification only.** Original historical archives, Monte Carlo chains and certificates are not modified or rerun. This report supplements rather than overwrites earlier, potentially conflicting interpretations.

## 1. Scope and primary-byte provenance

Repository `syncgravity/singular-boundary` was inspected before branching. On 2026-10-28 the default branch contains source *indexes*, existing status reports, theorem notes, `research/claims/CLAIM_LEDGER.csv` and `scripts/historical/verify.py`, but **not** the prepared 602-file historical import and not the large raw data archives. The existence of a previously prepared local Git root or a previous verification report is not proof that the underlying bytes were committed to this remote.

This audit directly opened and hashed the mounted:
- `Sharpe_dissertation_v10.7.tar.gz`, SHA-256 `c405acd6daa5a0a923429ab659b122b22231787d7a30e97db7f2974f278354d1`, containing a 23-page dissertation dated March 8, 2026, five papers and two experimental PDFs.
- Eight `{penrose,square}_seed{101,211,307,419}_stage26.zip` original saved-record exports, four per geometry; four further NPZ catalogues per geometry and `penrose_seed101_stage26_full.zip` (SHA-256 `6cfa12935428533cfeaff40a467705d632b19ede07b7f30e0bb9fb7a0cc68657`).
- Library-readable `HISTORICAL_Q14_CANONICAL.json`, `bianchi_certificate (1).json`, `counterexample_certificate.json`, `exact_rational_no_go.json`, `FORMAL_THEOREMS.md`, `LOCAL_STABILITY_THEOREM.md`, and `FORMAL_R3_R2_PROOF_AUDIT.md`.

The Library indexes `NOTES.zip` and many R3 original archives, but ZIP byte materialization failed in this runtime. The certificates' text can be read, but not all original generator scripts and witness matrices have been re-executed from their original bytes. Accordingly, published GitHub reconciliation reports are *secondary* evidence wherever their underlying originals are not mounted. Archive filenames and embedded dates are provenance claims, not authenticated creation timestamps.

## 2. Independently checked mathematics

**Finite Hamiltonian.** On finite connected SU(2) spatial link complex, with normalized Haar and
`H=Σ_e a_e(-Δ_e)+Σ_f b_f(1−p_f)` where `a_e>0,b_f≥0`, the compact connected configuration space and ellipticity give a unique strictly positive ground state in the full link Hilbert space; gauge invariance follows from uniqueness. Restriction to the gauge-invariant space cannot lower the full-link excitation gap. The fixed-volume gap is not uniform in volume, coupling or cutoff by this argument.

**Ground-state transform.** With `dν=Ω²dU`, `ψ=Ωf`,
`<ψ,(H−E0)ψ>=Σ_e a_e∫|∇_ef|²dν`.
Conditional edge Poincaré constants `c_loc` plus a uniform approximate tensorization constant `K` would give `gap≥a_*/(K c_loc)`, but those interacting-ground-state measure constants have NOT been established. This is an exact conditional criterion, not independent interacting mixing.

**Stationary completed temporal insertion.** Define `z(β)=2 exp(−β) I_1(β)/β` (and `z(0)=1`). On each SU(2) link, central Wilson convolution `C_β` has nonnegative Peter–Weyl eigenvalues `2exp(−β)I_{2j+1}(β)/β`, and `C_β ≽ z(β) C_0`, with `C_0` projection onto constants. For a finite periodic-time model with *stationary completed* spatial Wilson potential and nonnegative stationary temporal couplings, all temporal vertex/link variables integrated with Haar, deletion of any collection Q of **temporal-only** faces gives per-slab positive transfer factors `T_t ≼ z_t^{-1}T` where `z_t=∏_{q∈Q_t}z(β_q)` and `T` is the common completed transfer. For N time slices, Schatten–Hölder and eigenvalue monotonicity give
`Z_minus=Tr(∏_t T_t) ≤ ∏_t||T_t||_N ≤ (∏_t z_t^{-1})Tr(T^N)`.
Thus `Z_plus/Z_minus≥∏_{q∈Q} z(β_q)`. The Haar-ball estimate `z(β)≥exp(−1/2)/(6π(1+β)^(3/2))` produces an O(|Q|log(1+β)) deficit. This independent argument **does not** cover frozen exterior links, nonstationary completed masks, altered spatial faces, or source-inserted decay. Application to actual Q14 additionally requires matching its original generator to the completed stationary model.

**Exact failure of naive three-factor trace monotonicity.** In the original Library two-state certificate, let `K=[[1,7/10],[7/10,1]]`, `P0=1/2[[1,1],[1,1]]`, `z=17/10`, `A=[[1,7/5],[7/5,4]]`, `B=[[4,7/5],[7/5,1]]`. All A,B,K are positive definite, while `K−zP0=(3/20)[[1,−1],[−1,1]]≽0`. Exact rational multiplication gives `Tr(A K B)=543/25`, `Tr(A P0 B)=324/25`, and `Tr(A(K−zP0)B)=−39/125<0`. Hence Loewner ordering **alone** does not justify insertion monotonicity inside three arbitrary positive factors. The Schatten–Hölder stationary proof is not affected.

**Electric-only and weak-magnetic distinction.** At b=0, the full-link product Haar vacuum has gap at least `(3/4)min_e a_e` because the first nonconstant SU(2) link Casimir is 3/4; physical projection cannot lower this. A uniform *weak but nonzero* magnetic theorem requires an additional many-body perturbative argument; summing `||Σ_f b_f(1−p_f)||` is volume-dependent and fails as a uniform proof.

## 3. Q14 certificate-level results and unresolved distinctions

Parsed the complete 24,024-byte canonical JSON text by combining its Library line ranges. At each recorded radius 5, 6.5, 8, 10: 14 *unique* canonical temporal face labels, seven in slab 0 and seven in slab 1, with **identical** canonical label sets across radii. Its fields report H=36 support links and A(H)=62 affected retained faces. Those two counts were **read from the certificate**, not rederived from original oriented generator words in this audit.

The recovered historical reports describe 54 retained Bianchi fill faces, including ten outside A(H), optimal rational fractional cover 22 via 54×101 primal/dual witnesses, and a 44-fold Bianchi energy coefficient. Without regenerating independent face-link matrices and checking every nonabelian conjugated identity, these remain **computationally/source certified pending independent full-word review**, not new independently proved results. A 54-face cover optimum and a Ward constant 33 are not an unconditional Gibbs staple-minimum bound.

The original Penrose Q14 (three spatial seed rhombi, fourteen temporal face insertions, three-periodic time and all links integrated) **must not** be equated to the historically older twelve-prism/four-spatial-face/37-independent-link fixed-boundary formulation. The latter's exact oriented words and boundary conventions remain unresolved. Constructed quadrilateral-prism demonstrations are separate models.

For a fixed finite cavity and fixed exterior `η`, define `Δ(η)=min(D_C+D_Q)−min D_C≥0`. Elementary compact-group Laplace bounds give `−log(Z_{C+Q}/Z_C)=λΔ(η)+O(m log λ+n+q)` for fixed finite support and bounded coefficients. Therefore a pointwise O(log λ) comparison demands `Δ(η)=0`; an **annealed** Gibbs comparison is a distinct proposition. The original Q14 report's exposed-star center-flip counterexamples invalidate fill-only pointwise Ward absorption under their certified incidence, not the annealed or stationary all-integrated theorem.

## 4. R3-IR: exact spectral target and circularity

For the physical transfer operator `T` and normalized `T_hat=T/λ0`, define `Q_Ω=I−|Ω><Ω|`. For gauge-invariant source `A`,
`C_A(n)=<Q_Ω AΩ,T_hat^n Q_Ω AΩ>`.
Uniform physical decay `C_A(n)≤M_A exp(−m n a_t)` with common m>0, together with **an observing family across all relevant vacuum-orthogonal sectors**, would establish a physical mass threshold. The bound must be *derived* from the interacting model, not assumed as equivalent observability, complete Wilson frames or transfer contraction.

The first character/blocking identity mixes adjacent SU(2) spin labels under magnetic Wilson insertions; isolated Bessel factors do not iterate as an interacting spectral theorem. Positive first energy moments cannot bound low-energy spectral weight from above without independent information. Exact temporal decimation `T→T^k, a_t→k a_t` preserves physical energies. The one-rhombus b=0 source `p_f` has spectral norm² 1/4 and excitation energy `3a`; sending a→0 is an explicit obstruction to any all-electric-scale source-weight bound with fixed physical-unit constant. This does not refute a fixed-electric-scale or physical continuum theorem.

## 5. Strong-coupling literature check

Primary source: D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, arXiv:math-ph/0412040, Theorem 1, journal CMP 261 (2006) 799–819. The article expressly allows possibly infinite-dimensional on-site Hilbert spaces and unbounded local free operators. **However, its initial hypotheses expressly assume translation-invariant interactions on Z^ν and a fixed finite interaction range**, with local relative-form smallness. An irregular Penrose patch does not satisfy those literal hypotheses merely because its face degrees are bounded. A suitable inhomogeneous bounded-geometry adaptation or independently established applicable theorem, including arbitrary admissible boundaries, remains necessary.

This is a potentially tractable separate fixed-scale theorem, NOT an already verified volume-uniform Penrose strong-coupling gap.

## 6. Numerics and histories

Eight directly examined Stage 26 ZIP archives have 100 original saved outer records each, sweeps 10020 through 12000 with stride 20. Direct time-slice matrices are (20,4), conditional arrays (2,9,4,4); the recorded final record SHA-256 is directly matched to its ZIP payload in the local script. There are 800 saved records but not 800 independent measurements.

Repository historical reconciliation reports record: Stage16 corrected Stage13–15 Wilson-transporter conventions; Stage19 held-out screens 0/64 accepted; Stage20 none at later three consecutive positive 2-SE lags; Stage23 corrected temporal offsets; Stage29 direct/conditional standardized deviations around 2.36 and 2.28; Stage34 saved per-anchor equality ~1.13e-14; Stage35 helical implementation without completed production ensembles. Those claims have NOT been independently regenerated from the unavailable original Stage19–35 complete source ZIP bytes in this audit. No physical scalar mass is admitted from these reports. None is a spectral proof.

## 7. R2 and geometric J

At fixed graph, suitable anisotropic temporal Wilson coefficients yield a Kogut–Susskind Hamiltonian limit on finite Peter–Weyl cores; spatial quantum refinement is a separate mathematical gate. The fivefold geometric covariance of symmetric quadratic tensors can enforce macroscopic *classical* isotropy but does not create an interacting Hilbert space, positive physical gap, or 3+1-dimensional Yang–Mills. The March dissertation gives a Euclidean `J²=−I` and Wick-rotation interpretation; it does **not** construct a gauge-invariant physical operator implementing that J on the interacting Hilbert space, nor a dynamical intertwiner. Real rotations and nontrivial Lorentz boosts have different real spectral types, so equating them requires more than C5 representation theory.

## 8. Evidence-classified ledger

| Claim | Status | Core evidence / limiting assumption |
|---|---|---|
| Finite-volume SU2 Hamiltonian unique ground and positive gap | **Independently proved** (standard elliptic argument) | positive electric weights; finite connected compact link space |
| Ground-state transform LS-1 | **Independently proved** | exact quadratic form identity |
| LS-2 local-to-global bound | **Conditionally proved** | interacting conditional Poincaré and variance tensorization K unverified |
| Pure electric gap | **Independently proved** | b=0; full Hilbert, finite graph |
| Penrose weak-magnetic uniform gap | **Open** | cannot directly invoke Yarotsky's translation-invariant theorem |
| Stationary completed temporal deletion | **Independently proved under stated hypotheses** | Peter–Weyl, positive operators and Schatten–Hölder; original geometry match pending |
| Canonical Q14 14 labels, 7+7, radius invariance | **Computationally certified** | canonical JSON directly parsed; generator validation outstanding |
| Q14 H36, affected A62, 54-fill, cover 22 | **Source-proved / computationally certified, independent reconstruction pending** | stored count fields and prior witness report; original incidence not re-executed here |
| Q14 44 Bianchi inequality | **Source-proved, pending independent review** | full conjugated group-word proof not checked |
| Older 12-prism/37-link = authentic Q14 | **Unresolved provenance** | exact source words and exterior convention missing |
| Naive triple trace monotonicity | **Obstructed or disproved** | exact rational −39/125 counterexample checked |
| Pointwise fill-only Ward absorption for certified Q14 stars | **Source-proved pending independent incidence check; obstructed in claimed model** | center flips; annealed case unaffected |
| Generic interacting physical source decay / gap | **Open** | source-inserted uniform IR and all-sector observability absent |
| Fixed graph temporal limit | **Source-proved, pending independent full proof review** | Chernoff/Peter–Weyl normalization |
| Penrose quantum spatial continuum and surviving gap | **Open** | tightness, OS reconstruction, physical energy uniformity |
| Stage26 record inventory | **Computationally certified** | original ZIP/NPZ metadata and record hashes |
| Stage19/20 no accepted scalar mass | **Numerically supported by historical report; direct raw-data recheck pending** | original saved fit arrays not mounted |
| C5 geometric covariance → interacting spectral bound | **Open / unsupported implication** | missing physical J representation and intertwiner |

## 9. Dependency graph and ranked obligations

```
verified finite SU2 graph/action
   ├─ stationary all-links R3-PRISM ratio ──X──> spectral gap
   ├─ authentic Q14 incidence -> boundary/annealed R3-PRISM (separate gate)
   ├─ fixed-graph temporal Wilson -> Hamiltonian / physical time
   │     ├─ electric-only gap
   │     ├─ weak-magnetic Penrose gap [OPEN, attainable fixed-scale]
   │     └─ generic interacting source-inserted IR [OPEN]
   │           └─ uniform observing sectors / collective control [OPEN]
   └─ spatial continuum geometric consistency
         └─ renormalized quantum continuum Schwinger functions [OPEN]
               + physical uniform spectral control [OPEN]
               -> candidate positive-gap 2+1D continuum
2+1D candidate ──X──> 3+1D Yang–Mills without separate construction
```

Priorities: **(1)** independently prove uniform weak-magnetic gap at fixed lattice scale (tractable noncircular spectral advance), **(2)** derive interacting source-inserted IR control on the physical scaling trajectory, **(3)** reconstruct quantum spatial continuum observables and OS/sector limits, **(4)** authenticate remaining Q14 word-level, exterior-boundary and twelve-prism sources, **(5)** replay only saved-result deterministic Stage19/20 acceptance audits from original arrays. Neither R3-PRISM nor geometric isotropy substitutes for (2)–(3).

## 10. Recommended next theorem (NOT YET PROVED)

**Penrose finite-volume uniform strong-coupling theorem.** Let G range over finite face-complete genuine Penrose rhombus subcomplexes with free spatial boundary, edge degree uniformly bounded and each edge in at most two quadrilateral faces. On the full link Hilbert space set
`H_G=Σ_e a_e(-Δ_e)+Σ_f b_f(1−p_f)`, with `a_e≥a_*>0`, `0≤b_f≤ε a_*`. Prove existence of universal `ε_*>0,c_*>0` depending only on the finite-range bounded-geometry class such that for `ε≤ε_*` and any G the unique full-link ground state satisfies
`H_G−E0(G)≥c_*a_*(I−|Ω_G><Ω_G|)`.
Consequently the same lower bound holds after SU2 vertex gauge projection.

**Proof route:** extend finite-range bounded quantum product-vacuum perturbation theory to the nontranslation-invariant bounded-geometry Penrose edge interaction hypergraph, allowing single-site Hilbert spaces `L²(SU2)` and unbounded electric on-site Casimirs, with strictly bounded magnetic interaction terms. Alternatively establish LS-2's uniform interacting conditional Poincaré plus tensorization constants independently via a convergent cluster/quantum ground-state expansion. No assumption equivalent to the desired gap may be imported. **Certificate:** a complete theorem with explicit constants and volume-independent combinatoric estimates, domain control, gauge restriction, boundary stability and unambiguous physical energy units; verify an independent referee-checkable proof against the actual primary theorem assumptions. This would be a genuine interacting spectral result, but would apply only in the fixed-scale strong-coupling regime. Under geometric continuum scaling `b_f/a_e∼(g_3²a)^{-2}`, this smallness generally fails.

**Integrity:** No MCMC, new mass fits, forced history changes, or original source modification occurred. Keep archival imports immutable and commit only derived reviews/scripts on a separate branch before merging.
