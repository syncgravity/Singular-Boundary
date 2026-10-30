# Buffered thin contours and exact Wilson post-integration polymer activities
Date: 2026-10-26

**Proof status.** Exact connected-component polymer representation and a rigorous continuum obstruction for its *unextracted strong-coupling activities* are proved. A cutoff-uniform Balaban-type residual activity estimate is **not** proved. No R3/R2 mass gap follows.

## Setup
A finite 2+1 dimensional SU(2) Penrose-derived spacetime cell complex has plaquettes P and links E, with bounded link/plaquette incidence. Define d_p(U)=1-(1/2)Tr W_p(U) in [0,2], β_p in [c_- λ,c_+ λ], λ=(g_3² h)^(-1). Haar is normalized on every link. The full partition function is Z=∫ ∏_p exp(-β_p d_p) ∏_e dU_e.

## Theorem A: exact connected plaquette-polymer identity
Let f_p(U)=exp(-β_p d_p(U))-1 in [-1,0]. A subset of plaquettes X is link-connected if the graph connecting plaquettes sharing a link is connected. For each nonempty link-connected X define its **actual integrated activity**

w_β(X) = ∫_{SU(2)^{E(X)}} ∏_{p∈X} f_p(U) ∏_{e∈E(X)} dU_e.

Expanding ∏_p(1+f_p) and decomposing each chosen subset into link-connected components, integration over disjoint link supports factorizes. Therefore exactly

Z = Σ_{ {X_1,...,X_n} pairwise link-disjoint connected polymers} ∏_{i=1}^n w_β(X_i),

including the empty collection of weight one. There is no assumption of independent plaquettes. Components touching via a shared link are incompatible. All activities are derived directly from the original spatial-temporal Wilson action.

The simple bound |w_β(X)|≤1 is volume-independent but not a convergence estimate.

## Theorem B: continuum obstruction to the *unextracted* plaquette polymer norm
For a singleton plaquette X={p}, the Haar holonomy W_p is Haar distributed, hence

w_β({p}) = e^{-β} z(β)-1, z(β)=2I_1(β)/β.

As β→∞, e^{-β}z(β) = sqrt(2/π) β^{-3/2}(1+O(β^{-1})), giving

w_β({p}) = -1+sqrt(2/π) β^{-3/2}(1+O(β^{-1})).

Thus |w_β({p})|→1, so for every size-weight α>0 and every plaquette p,

Σ_{X∋p}|w_β(X)|e^{α|X|} ≥e^α|w_β({p})|→e^α.

In particular this natural activity norm cannot tend to zero on the fixed g_3² physical trajectory β∼h^{-1}, and the elementary Kotecky–Preiss sufficient condition with size weight |X| fails already for singleton polymers when β large. This does **not** exclude alternate, resummed or background-subtracted expansions.

## Theorem C: why elementary thick buffering does not resolve thin-contour suppression
The previously established bulk–boundary comparison gives for a selected all-large set X:

log μ(L_X) ≤ -c_0√λ |X| + C_1 |X|(1+log λ)+ C_2 λ |Y(X)|,

with Y(X) exterior plaquettes touching links of X. For a three-dimensional regular cubical/rhombic-thick buffer B_R of lattice radius R around a singleton X, the buffer has |B_R|≈R³, |Y(B_R)|≈R², and |Y(B_R)|/|B_R|≈1/R. Achieving the previous thick-set criterion requires R≳√λ, corresponding to physical buffer radius h√λ=O(√h). But all-large on X does not imply all-large on B_R. Applying the Markov event estimate to B_R bounds a different (much smaller) event. Even if one artificially substitutes B_R as the region of integration while keeping the event on X, the small-ball partition estimate generates a bulk entropy cost O(|B_R| log λ)≈λ^{3/2} log λ, much larger than the negative -c√λ gain for the singleton X. Accordingly, geometry-only buffering does not prove a thin-contour Peierls bound; new conditional interpolation or gauge-covariant fluctuation estimates are required.

## Exact post-integration source coefficients
For retained boundary links Y and interior links X, define Z_B(Y; t)=∫ exp[-S_B(X,Y)+∑_i t_i O_i(X,Y)] dX. For all finite blocks, analyticity in real t and bounded sources yields the exact source-connected coefficients ∂_{t_{i1}}...∂_{t_{in}} log Z_B(Y;t)|_{t=0}=κ_n(O_{i1},...,O_{in}|Y). These cumulants are not automatically small. To define a *residual polymer activity* after local gauge-action extraction, one must specify a local projector or counterterm convention and prove summable bounds on the resulting connected coefficients. Neither bare singleton activity nor all-large event probability is such a bound.

## Precise next gate
1. Fix a gauge-equivariant block boundary/overlap construction on actual Penrose spacetime cells.
2. Specify a nonflat background, localized gauge fixing, scale-dependent Gaussian covariance and local relevant-action extraction (including determinant contributions).
3. Prove a conditional buffered contour estimate for an event on the *core* X, not an all-large event on its buffer, with constants depending on |X| rather than |B_R|; prove multi-block decoupling.
4. Obtain a cutoff-, volume- and scale-uniform root activity estimate on the **subtracted** effective action, for all polymers and Wilson source insertions.
5. Reconstruct transfer/Hamiltonian and demonstrate infrared gap independently; UV stability alone does not imply it.

## Relevant references
T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, Commun. Math. Phys. 102 (1985) 255–275. R. Kotecký and D. Preiss, *Cluster Expansion for Abstract Polymer Models*, Commun. Math. Phys. 103 (1986) 491–498.
