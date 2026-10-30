# Joint spacetime Wilson character and polymer expansion: rigorous strong-coupling admission test

Date: 2026-10-26. Status: finite-volume identities and explicit sufficient high-temperature bound proved; physical continuum uniformity not established.

## Setup
Let L be a finite oriented SU(2) lattice gauge spacetime cell complex with plaquette set P, every plaquette involving at most four links, and plaquette-link overlap graph maximum degree Δ independent of volume and spatial refinement. Define p(U)=Tr(U)/2 and Z=∫∏_{p∈P}exp(β_p p(U_p))∏_{ℓ∈L}dU_ℓ for β_p≥0. This includes both spatial and temporal plaquettes, on square or suitably bounded-incidence Penrose spacetime stacks. Constants exp(-∑β_p) in the usual Wilson action do not change normalized expectations.

## Theorem 1: exact SU(2) character expansion
For β>0, exp(β p(U))=z(β) ∑_{j∈{0,1/2,...}} (2j+1) r_j(β) χ_j(U), where z=2 I_1(β)/β, r_j=I_{2j+1}(β)/I_1(β), r_0=1, and continuous β=0 convention. Integrating links contracts the representation matrices into SU(2) invariant projectors/intertwiners. The result is a coupled spatial-temporal spin foam. Positivity of individual character coefficients does not establish positivity of arbitrary spin foam recoupling amplitudes or a convergent cluster expansion at large β.

## Theorem 2: volume-uniform convergent polymer expansion at sufficiently small β
Define f_p=e^{β_p p(U_p)}-1 and u=max_p(e^{β_p}-1). Expand Z as a finite sum over subsets S⊂P of ∫ ∏_{p∈S}f_p. Connected components of S in the plaquette overlap graph have disjoint link supports, hence their integrals factor exactly. Define for connected nonempty X⊂P, w(X)=∫∏_{p∈X}f_p with Haar integration over incident links, and w(X) bounded by u^{|X|}. Distinct polymers are compatible when they are not neighboring in the plaquette overlap graph (including no shared plaquette). Hence Z is exactly the hard-core polymer gas partition function ∑_{compatible {X_i}} ∏w(X_i).

Count connected plaquette subsets of cardinality n containing a fixed p by at most (e Δ)^{n-1} for Δ≥1 (a standard conservative connected-animal bound, using a tree exploration; replace with a larger fixed counting constant if desired). Thus

 S_p=∑_{X∋p}|w(X)|exp(|X|) ≤ e u/(1-e² Δ u), if e² Δ u<1.

An incompatible Y with X must intersect the closed neighborhood N[X] of X in the overlap graph; |N[X]|≤(Δ+1)|X|. Hence

 ∑_{Y incompatible X}|w(Y)|exp(|Y|) ≤ (Δ+1)|X| e u/(1-e²Δu).

Under (Δ+1)e u/(1-e²Δu) ≤1, this is at most |X|. The Kotecký–Preiss criterion holds with a(X)=|X|. Therefore the Mayer/cluster expansion of log Z converges absolutely (in the thermodynamic-limit sense of uniformly bounded rooted cluster sums) with constants independent of volume. A less delicate, stronger sufficient condition is u ≤ 1/[2e(Δ+1)+2e²Δ], since then (Δ+1)eu/(1-e²Δu)≤1/2; can instead state a simple conservative alternative u≤1/[4e²(Δ+1)] which readily implies both for Δ≥1.

The bound controls sums of connected polymers rooted at plaquettes and local free-energy cumulants for bounded-support insertions with their own controlled expansion, not automatically a time-continuum spectral gap or the infinite graded Wilson-source operator norm.

## Continuum obstruction
For a_t=κh (κ bounded from zero and infinity) and fixed g_3², spatial and temporal Euclidean Wilson plaquette coefficients scale as β_p(h)=c_p/(g_3²h), 0<c_-≤c_p≤c_+. Consequently u(h)≥exp(c_-/(g_3²h))-1→∞. The sufficient polymer criterion becomes violently invalid. In normalized character variables r_{1/2}(β)=I_2(β)/I_1(β)→1 as β→∞, so changing to the character basis by itself also supplies no small local expansion parameter. Spatial-only block convolutions do not commute with integrating temporally coupled links.

## Exact retained-boundary step and necessary estimate
For retained boundary links Y and eliminated interior X, define the exact effective functional S_eff(Y)=-log[∫exp(-S(X,Y))dX] (up to an additive constant). This produces all gauge-invariant boundary Wilson network interactions, including temporally nonlocal interactions. A useful desired target would be a connected weighted polymer norm ∑_{Γ∋z} e^{m diam Γ+α|Γ|}|Φ_eff(Γ)| uniformly bounded by a constant in a stability region, together with (i) an independent reconstructed transfer-Hamiltonian gap, (ii) spectral overlap/source control, and (iii) a stable coupling flow. No such uniform estimate has been derived from the original Wilson theory at β(h)→∞.

## Logical conclusion
A rigorous strong-coupling joint spacetime polymer expansion exists and is volume-uniform, but it has no established continuum-stable regime for the specified Wilson trajectory. This does not disprove the continuum mass gap; it shows why this direct perturbative expansion does not prove R3/R2.
