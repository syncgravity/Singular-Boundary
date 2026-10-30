# Joint gauge-invariant rhombus blocking: exact boundary character kernel and connected influence audit

**26 October 2026.** Direct review of Sharpe dissertation v10.7 Papers 2, 3 and 4 included. **Result:** exact two-face boundary-preserving integration and a sharp worst-boundary counterexample to uniform connected-source contraction by positive magnetic coupling alone. No full interacting Hamiltonian RG or uniform mass gap is proved.

## Setup and gauge covariance

Take two rhombic faces sharing an edge `U`, with holonomies `W1=A U`, `W2=U^{-1}B`; `A,B` are parallel transport products of the other six boundary links. The product `V=AB` is the holonomy of the outer six-edge boundary (up to orientation/conjugation). Integrating `U` using Haar measure is gauge-covariant provided all transformations of boundary holonomies are retained. The resulting operator depends on `V` through gauge-invariant traces; it does not claim that `A`, `B` are individually gauge-invariant. This is a *Euclidean magnetic integral at fixed boundary*, not yet an exact spatial decimation of the quantum Hamiltonian with electric-link dynamics.

Define `p1=Tr(AU)/2`, `p2=Tr(U^{-1}B)/2`, couplings `t,s≥0`, and the positive boundary kernel

\[Z_{t,s}(V)=\int_{SU(2)}e^{t p_1+s p_2}\,dU.\]

Set `z(t)=∫exp[t Tr(U)/2]dU=2 I_1(t)/t` with `z(0)=1`, `d_j=2j+1`, and `r_j(t)=I_{2j+1}(t)/I_1(t)` (`r_j(0)=0` for positive j). The Peter–Weyl/character identity gives the **exact convergent character series**

\[\boxed{Z_{t,s}(V)=z(t)z(s)\sum_{j\in\{0,1/2,1,\ldots\}}d_j\,r_j(t)r_j(s)\,\chi_j(V).}\tag{1}\]

The `j=0` term is 1. This retains **all representations** and the complete fused outer boundary holonomy. Its effective induced magnetic interaction is `W_eff(V)=-log Z_{t,s}(V)` up to a constant (for a fixed Euclidean slab).

## Exact connected source map

The conditional expectation of the two elementary plaquette scalar sources is

\[m_1(V)=\partial_t\log Z_{t,s}(V),\quad m_2(V)=\partial_s\log Z_{t,s}(V).\]

The connected *joint* influence at fixed boundary is

\[\boxed{C_{12}(V;t,s)=\partial_t\partial_s\log Z_{t,s}(V)=\mathrm{Cov}_{t,s,V}(p_1,p_2).}\tag{2}\]

This is the correct scalar connected source response for the two-rhombus Euclidean block, not a raw single-link Fisher influence. It is bounded `|C12|≤1` for all t,s,V because p1,p2∈[-1,1] and their variances are ≤1. It is generally signed: no universal positivity or absolute contraction follows from magnetic positivity.

At weak coupling, exact Haar orthogonality gives

\[\int p_1\,dU=\int p_2\,dU=0,\qquad \int p_1p_2\,dU=\tfrac14 p_{\partial}(V),\quad p_{\partial}(V)=\tfrac12\mathrm{Tr}(V).\]

Consequently `C12(V;0,0)=p_∂(V)/4` and `-log Z` induces the fused loop coefficient `-ts p_∂(V)/4+O((|t|+|s|)^3)` (the separate t²,s² terms are V-independent).

### Exact frustrated-boundary obstruction

If the outer holonomy is the nontrivial central element `V=-I`, one may choose a boundary representation `A=I`, `B=-I`. Then `p_2=-p_1` **pointwise**, and at equal couplings `t=s`, the integrand is exactly `1`. Therefore the conditional distribution of U is Haar, irrespective of coupling strength, and

\[\boxed{C_{12}(-I;t,t)=-\mathrm{Var}_{Haar}(p_1)=-\tfrac14\quad\text{for every }t\ge0.}\tag{3}\]

Hence `sup_{V∈SU(2)}|C12(V;t,t)|≥1/4` for all t. In particular **no bound tending to zero uniformly over boundary holonomy** can hold for this particular connected influence by merely making the plaquette coupling large. At `V=I`, `p2=p1` pointwise and `C12(I;t,t)=Var_{e^{2tp}}(p)→0` as t→∞, showing that typical/good boundaries and frustrated boundaries behave differently. Averaged contraction, if valid, needs a rigorous bound on the boundary distribution; it cannot be substituted for the worst-case bound.

## Iteration and retained-source obligation

Gluing several rhombus blocks generates their full boundary-loop character algebras and connected cumulants of increasing order. Exact measure-level decimation composes by conditional integration; however the potential `-log Z` alone cannot encode the Kogut–Susskind electric kinetic terms, derivative-coupled effective operators, or ground-state reconstructed inner products. Quantum Hamiltonian spatial blocking must use an isometric conditional or Schur/Feshbach map retaining boundary gauge degrees and control of the eliminated-sector resolvent **relative to the interacting ground state**, not merely Haar integration.

The equal-coupling negative covariance (3) shows why a blanket strong-coupling-in-the-magnetic-potential ⇒ all-boundary connected influence contracts claim is false. It does not exclude contraction in a suitable boundary-average norm, good-boundary ensemble, or multi-scale polymer norm. To prove one of those requires a measure-level boundary large-deviation/tail inequality and stability of the complete generated operator family under iteration. Neither is presently proved here.

## Direct relevance of dissertation Papers 2–4

- **Paper 2**, `Sharpe_Paper2_Z5_Minkowski_Lapidus.pdf`: studies the Z5/C5 geometry, spectral zeta and Lapidus complex dimensions of tiling/graph operators. These describe geometric spectral structure, not the 2+1D SU(2) interacting Wilson cluster kernel or a uniform gauge-invariant conditional covariance estimate.
- **Paper 3**, `Sharpe_Paper3_J_Operator_Hidden_Domain.pdf`: identifies a complex structure J via C5 representation decomposition and hidden-domain geometry. No demonstrated positive intertwiner `J` with the fully interacting Wilson transfer Hamiltonian is supplied, so J cannot be used to replace (2) with a contraction estimate.
- **Paper 4**, `Sharpe_Paper4_Conformal_Boundary_CC.pdf`: discusses acceptance-window boundaries, factorization and a spectral triple. Its claimed one-loop suppression is not a proved 2+1D gauge-invariant mass gap and cannot fix the frustrated outer holonomy sector of (3).

**Bottom line:** exact, gauge-invariant boundary-preserving Euclidean two-rhombus block integration and its connected source map are proved. A uniform worst-boundary connected source contraction is refuted. All-coupling quantum Hamiltonian cluster RG and continuum R3/R2 closure remain open.
