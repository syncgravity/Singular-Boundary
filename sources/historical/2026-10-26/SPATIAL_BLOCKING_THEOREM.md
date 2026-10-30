# R3: exact spatial-edge Feshbach blocking and Wilson source map

26 October 2026. **Proof status:** The edge-Haar projection formulas, the exact Feshbach interaction and source maps, and a precise failure of the naive continuum contraction are established. A cutoff-uniform physical low-energy contraction is NOT proved.

## Model
Take a finite spatial rhombic two-complex with SU(2) link Hilbert space `L²(SU(2)^E)`, physical Gauss invariant subspace, and `H=Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f)`, `a_e>0,b_f≥0`, `p_f=Tr_fund(W_f)/2`. Fix an interior edge `e` incident to exactly two simple faces `f1,f2`. Choose orientation so their holonomies are `AU` and `U^{-1}B`, U the selected link. Set `P=∫dU` (orthogonal projection onto constant functions of U), `Q_e=1-P`. P commutes with the vertex gauge action, hence respects Gauss's law. The symbols P and Q_e in this note are **spatial-blocking projections**, not vacuum/excited spectral projectors. Let `H_rest=H-a_e(-Δ_e)-b1(1-p1)-b2(1-p2)`; H_rest is independent of U, nonnegative and commutes with P.

## 1. Exact SU(2) Haar algebra
Character orthogonality gives

`Pp1P=Pp2P=0`, `P p1² P=P p2² P=(1/4)P`, and `Pp1p2P=(p12/4)P`, with `p12=(1/2)Tr_fund(AB)`.

**Proof:** `∫dU Tr(AU)Tr(U^{-1}B)=Tr(AB)/2`. Including the 1/4 factors of p1p2 gives Tr(AB)/8=p12/4. For the square, a Haar distributed SU(2) element has `∫(Tr U)^2dU=1`, giving 1/4. Gauge invariance of p12 follows because AB is a closed fused loop.

Write `V_e=b1(1-p1)+b2(1-p2)`. Then

`PHP=(H_rest+b1+b2)P`,

`PHQ_eHP=P V_e Q_e V_e P=[(b1²+b2²)/4+(b1b2/2)p12]P`.

The **cross term generates a fused two-face Wilson interaction** exactly in the interaction variance; it does not follow that PHP itself already contains this term.

## 2. Exact spatial Feshbach map (Theorem S-F)
For any real z such that the self-adjoint Q-block `Q_e H Q_e-z` is strictly positive and invertible, set `R_Q(z)=(Q_e H Q_e-z)^{-1}` and

`F_P(z)=P(H-z)P-PHQ_e R_Q(z)Q_e HP`.

If `HΨ=zΨ`, then `φ=PΨ` satisfies `F_P(z)φ=0`, and conversely any `φ` satisfying `F_P(z)φ=0` reconstructs an eigenvector

`Ψ=J_z φ`, `J_z=P-Q_eR_Q(z)Q_e HP`.

The identities follow by solving the Q-block of `(H-z)(φ+χ)=0` for `χ=-R_Q Q_e HPφ` and substituting into its P-block. Gauge invariance is preserved since P,H,Q_e,R_Q commute with the Gauss action. The map is isospectral **only in its specified resolvent window**. In general it depends on z, and effective interactions are operator-valued, not a closed nearest-neighbor plaquette action.

Since `H_rest≥0`, `V_e≥0`, and the first nonconstant SU(2) link representation has Casimir 3/4, `Q_eHQ_e≥(3/4)a_e Q_e`. Hence the map is rigorously available for z<3a_e/4; this elementary **absolute-energy** window is not necessarily near the many-body ground energy, which grows with the spatial volume. To use the map near the true many-body ground energy, an improved relative block spectral separation is required, and it has NOT been derived here.

The exact source map is the energy-dependent quadratic-form compression

`A_eff(z)=J_z† A J_z`.

For two eigenvectors Ψ_i=J_{z_i}φ_i and Ψ_j=J_{z_j}φ_j, the **off-diagonal** source matrix element is `⟨Ψ_i,AΨ_j⟩=⟨φ_i,J_{z_i}† A J_{z_j} φ_j⟩`. The blocked inner product similarly involves `J_{z_i}†J_{z_j}`. Retaining this metric is essential: projecting to P and using an unmodified norm does not preserve normalized low-energy overlaps. The exact map preserves physical overlaps algebraically, but it does not supply a uniform lower bound as volume/cutoff varies.

## 3. Leading induced interaction/source and its limits (Theorem S-L)
If `R_Q(z)` can be *independently* approximated in a controlled operator norm by a scalar r times Q_e in a given energy window, the first induced Hamiltonian correction is

`F_P(z)≈(H_rest+b1+b2-z)P -r[(b1²+b2²)/4+(b1b2/2)p12]P`.

The leading induced fused-loop coupling is `-(r b1 b2/2)p12`. For an electric dominated single-edge approximation `r≈4/(3a_e)`, it is `-(2b1b2/(3a_e))p12`.

For the first-face source A=p1, since `Pp1P=0`, its **leading** reconstructed source (linear in Q_eHP, with R_Q≈rQ_e) is

`A_eff(z)≈r[(b1/2)+(b2/2)p12]P`,

where the constant term drops on centering and the fused Wilson trace `p12` remains with coefficient `r b2/2`. This is **not** obtained by applying a vanishing-energy filter. It shows that the spatial source has a nonzero fused-loop component rather than being annihilated by blocking. Higher terms and the R_Q operator may generate arbitrarily many loops; the approximation only has force when its resolvent error has independently been bounded. The formula is not asserted to be an exact source RG at arbitrary b.

An elementary bound on the off-diagonal coupling is `||Q_eHP||≤b1+b2` (because `||p_f||∞≤1`). Consequently for z<3a_e/4,

`||J_z-P||≤(b1+b2)/(3a_e/4-z)`.

This is useful only if the right side is sufficiently small, and in a continuum geometric scaling `a_e=O(g3²)`, `b_f=O((g3²h²)^-1)`, it diverges as h→0. The Schur complement itself remains an exact algebraic construction when its resolvent assumptions hold; the **contractive estimate does not survive refinement from this bound**.

## 4. Explicit distinction between true spatial and temporal blocking
Exact temporal composition T→T² merely changes the physical time-step unit, preserving excitation energies. Spatial P integration removes an entire link's nonconstant Peter–Weyl sector, induces a fused-loop interaction, transforms Wilson sources, and generates an energy-dependent metric. It is a genuine change in spatial degrees of freedom. Neither operation alone proves a gap.

## 5. The remaining noncircular continuum-uniform gate
One needs a locally energy-renormalized Q-block lower bound relative to the **actual interacting ground and retained block energies**, giving a cutoff- and volume-uniform resolvent control; an operator/polymer norm handling all higher loops induced through repeated elimination; a bound on the condition numbers of the renormalized source metrics and an independent lower frame estimate on the neutral physical low-energy space; a contractive IR source estimate that does not follow merely from multiplying by powers of H-E0; and, independently (R2), a continuum construction with correct time/energy normalization. None has been shown at arbitrary magnetic coupling in the present model.

**Verdict:** Exact one-edge spatial interaction/source map **proved** in its resolvent window. The fused Wilson loop is generated by SU(2) dynamics at second order in the Schur complement. Preservation of every overlap is exact with the energy-dependent embedding and metric, but no uniform lower observability or interacting source contraction has been proved at continuum coupling. The requested physical mass-gap theorem remains open.