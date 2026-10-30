# The Singular Boundary — graded multilocal Wilson frames: noncircular contraction audit

**26 October 2026.** Scope: finite interacting SU(2) Wilson Hamiltonians on rhombic spatial complexes. **Conclusion: no interacting, continuum-uniform physical infrared contraction is proved.** New rigorous filtering obstruction and explicit, independently converged one-face interacting character calculation.

## 1. Precise setup

Let `H=Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f)` on `L²(SU(2)^E)^{SU(2)^V}` with a_e>0, b_f≥0 and `p_f=(1/2)Tr_fund W_f`. The normalized positive finite-volume ground state is Ω, and `K=(H-E0)` on its orthogonal complement. For centered Wilson multipliers `A_i`, set `v_i=Q A_i Ω`. Assume the positive operator series `S=Σ_i w_i |v_i><v_i|` is bounded. Write `P_s=1_(0,s](K)`. The desired bounds are `P_η S P_η≥c P_η` and `||P_s S P_s||≤C s^p` for cutoff/volume-independent c,C,p. This is a sufficient *mass-gap-strength* hypothesis; neither inequality pair is certified by the prior Stage 26 correlators.

## 2. Theorem A — energy filtering cannot close both halves noncircularly

Suppose `||S||≤C` and on `Ran P_η`, `P_η S P_η≥cP_η`. Let r≥1. Define the quadratic-form-filtered operator `S_r=K^r S K^r`. Even if `S_r` is not globally bounded (K is unbounded), its restriction `P_s S_r P_s` is bounded and

`||P_s S_r P_s||≤C s^(2r)` for all s>0.

If `ψ_E` is a normalized eigenstate of K with energy E∈(0,η],

`<ψ_E,S_r ψ_E>=E^(2r)<ψ_E,Sψ_E>`.

Hence the lower bound available from the original frame for this state is only `c E^(2r)`. To obtain a **uniform** lower bound for S_r one would already need a positive uniform lower bound for E, or a new independent theorem involving source amplitudes with compensating E-dependent divergence. In finite volume a commutator source `[H,A]Ω=KQAΩ` realizes this filtering, but the commutator is generally an unbounded differential operator, not a bounded Wilson multiplication observable.

**Proof:** For all ψ in Ran P_s, `||K^r ψ||≤s^r||ψ||`; apply S operator norm. For an eigenstate the expectation follows by Kψ_E=Eψ_E. QED.

**General spectral filter:** for a Borel f bounded on [0,η], `S_f=f(K)Sf(K)` obeys `||P_s S_fP_s||≤C sup_{0<E≤s}|f(E)|²`; the frame expectation on ψ_E is `|f(E)|²<ψ_E,Sψ_E>`. Thus filters vanishing at zero cannot by themselves establish uniform observability.

## 3. Theorem B — positive spectral measure and the non-extensive criterion

If `P_η SP_η≥c P_η` and `||P_s SP_s||≤C s^p` for every 0<s≤η and constants c,C,p>0 independent of volume/cutoff, then the vacuum-orthogonal gap is ≥min(η,(c/C)^(1/p)). Proof: a unit ψ in Ran P_s has c≤<ψ,Sψ>≤Cs^p. This is a conditional gap theorem, not an independent Wilson dynamics estimate. It highlights that proving both assumptions for the interacting continuum *is* the main open problem.

Unlike `Tr P_s SP_s`, the operator norm does not scale automatically with the dimension of a degenerate low-energy band. This repairs the earlier extensive trace obstacle but supplies no new bound by itself.

## 4. Exact interacting one-face gauge-singlet character kernel (test model)

For an isolated four-edge open rhombus with all a_e=a and one plaquette magnetic coupling b, gauge fixing identifies physical states with SU(2) class functions in W, with orthonormal basis `|j>=χ_j(W)`, j=0,1/2,1,... . Because `χ_1/2 χ_j=χ_(j+1/2)+χ_(j-1/2)` and `p=χ_1/2/2`, the **full interacting** Hamiltonian is the symmetric Jacobi matrix

`<j'|H|j>=[4a j(j+1)+b]δ_(j'j) -(b/2)(δ_(j',j+1/2)+δ_(j',j-1/2))`, omitting j<0.

This representation mixes every adjacent gauge-invariant character sector; its off-diagonal matrix elements are exactly -b/2. It is not a free-character tensor product and not the full many-face Penrose Hamiltonian.

`one_rhombus_character.py` calculates its low spectrum at a=1 and b=0,0.1,1,10,100 by symmetric tridiagonal diagonalization, and recomputes the same results with 80 and 120 character basis elements. The checked discrepancy is <4e-15 for all reported quantities. Values:

| b | First gap E1-E0 | Var_Ω(p) | First spectral moment |
|---:|---:|---:|---:|
| 0 | 3.000000 | 0.250000 | 0.750000 |
| 0.1 | 3.001166 | 0.249844 | 0.749879 |
| 1 | 3.113864 | 0.235549 | 0.738463 |
| 10 | 7.496260 | 0.064397 | 0.495359 |
| 100 | 26.984487 | 0.007168 | 0.193763 |

These are deterministic **single-rhombus finite-graph computations**. As b grows, the **bare** fundamental Wilson source variance strongly decreases; normalization is therefore dynamically nontrivial. The dimensionless coupling b/a changes, but this table is not a continuum scaling trajectory and proves no uniform many-body gap. Values below energy 1 are zero in the tested one-face examples simply because their lowest excitation energy is above 1. This is not a nonperturbative uniform bound in the large Penrose patch.

## 5. Graded multilocal construction and exact selection audit

A natural grade-q family consists of symmetrized gauge-invariant products of q contractible Wilson traces with supports separated by controlled physical distances; mixed holonomy traces and winding operators must be added to obtain the full finite-graph gauge-invariant algebra. At b=0, products of q traces on edge-disjoint faces give exact normalized eigenstates of energy 3aq (equal a) and an orthonormal frame on their **particular** q-loop sector. A full fixed-energy free-theory frame can be formed using its spin-network eigenbasis with bounded total excited edges, but the number of sources grows with volume and some source components may be far apart.

At b>0, no argument transfers the free frame into a cutoff-uniform lower frame: the magnetic interaction b~h^-2 is not perturbatively small relative to the electric term, and the ground state depends on b. Local source-density bounds and individual K1/K2 inequalities do not control `||P_s S P_s||` for a complete interacting multilocal family. The renormalization of q-loop grades and winding sectors remains an independent construction problem.

**A key methodological constraint:** stage 26 `direct_timeslice`, four scalar channels, and conditional products sample selected Euclidean correlators from independent outer fields; these do **not** determine the full infinite-dimensional operator S or certify either all-sector frame bound. Keep the original full-volume scalar channels as controls; do not identify an observer-dependent helical or restricted basis with the complete physical spectral projector.

## 6. Exact missing estimates and a falsifiable finite-step gate

For a noncircular continuum-uniform proof one must derive directly from the Wilson action:

(a) a gauge-preserving effective action/source RG map after integrating a spatial scale on *actual* Penrose patches;

(b) bounded operator-norm control of generated multi-loop, higher-representation source tails, including correlations between widely separated components;

(c) a physical-energy normalized *lower* frame constant across the full center-neutral low-energy band, without post-selecting operators from unknown eigenstates;

(d) an independently derived low-energy *upper* operator-norm estimate for the same frame, not using an energy vanishing filter that destroys its lower frame;

(e) a stable inequality with all constants uniform in h, patch size and boundary, and a quantum continuum reconstruction. This is stronger than the current deterministic one-face character calculation.

A concrete finite-step numerical check on reduced graphs would be to compute the low-energy spectral projector by exact spin-network diagonalization, build the Wilson-source overlap matrix B from predeclared q=1,2,3 products plus mixed traces, then compute eigenvalues of `(P_η B W B† P_η)` and its low-energy compression. Such numerical tests can falsify a *proposed* contraction/observability pair but cannot establish uniform h,L limits.

## Conclusion

**New:** Exact no-go for gap-producing spectral filters, exact noncommuting interacting character kernel, converged finite-graph source diagnostics, and the correct test for a graded source frame. **Still unproved:** arbitrary-coupling interacting, continuum-uniform `||P_s S P_s||≤Cs^p` together with an h,L-independent lower frame bound, hence the R3 mass gap and full quantum R2 continuum theory. No valid full proof is currently obtained.