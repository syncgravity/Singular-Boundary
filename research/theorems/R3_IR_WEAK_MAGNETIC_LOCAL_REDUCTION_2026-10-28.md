# R3-IR — independently proved local weak-magnetic reduction and exact response
**Date:** 2026-10-28. **Classification:** three independently proved finite-model lemmas; the uniform interacting Penrose spectral gap is **OPEN**. Original archives not modified; no simulations performed.

## Primary theorem audit
Source: D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, arXiv:math-ph/0412040, Theorem 1 and §2, https://arxiv.org/html/math-ph/0412040. The source allows infinite-dimensional local Hilbert spaces and unbounded local positive operators, but explicitly assumes translation-invariant interactions on `Z^ν` and (in its stated gap result) periodic cubic volumes. It therefore is **not directly applicable** to free-boundary, inhomogeneous Penrose patches. A subtler hypothesis is that the classical local term `h_x` have a nondegenerate gap **on the complete support of the perturbing term**. Pairing a one-link electric term with a four-link plaquette violates that local hypothesis; the decomposition below fixes this.

Comparison (not an applicable theorem here): Bravyi–DiVincenzo–Loss, *CMP* 284 (2008), arXiv:0707.1894, allows bounded-degree graphs but treats two-local **qubit** interactions, unlike unbounded SU(2) link rotors and four-link Wilson terms.

## Setup
Let `G=(V,E,F)` be a finite face complex of distinct simple oriented rhombi, with `|∂f|=4`, no repeated edges in a face, and each edge incident to `d_e∈{1,2}` included faces. Assume `a_e≥a_*>0` and `0≤b_f≤b_*`. On the **full link Hilbert space** `⊗_e L²(SU(2),dU_e)`, put `L_e=−Δ_e`, normalized so the first nonzero eigenvalue is `3/4`. Define `p_f=(1/2)ReTr W_f` and
```
H0 = Σ_e a_e L_e,          V=Σ_f b_f(1-p_f),        H(s)=H0+s V.
```
The product Haar vacuum `Ω0=1` is the unique free ground vector and the full-link free gap is at least `3 a_*/4`. For a fixed finite G the isolated ground eigenpair of H(s) is locally analytic in s by bounded-perturbation theory. No volume-uniform radius is implied. Gauge projection is taken **after** establishing a full-link estimate, not substituted for a tensor-product structure.

## Lemma 1 (exact face-based local gap and norm)
Set
```
h_f = Σ_{e∈∂f} (a_e/d_e) L_e,
φ_f = b_f(1-p_f),                 c_loc = 3a_*/8.
```
Then:
1. `Σ_f h_f=H0` exactly, including free-boundary edges, since every e occurs d_e times.
2. On the four-link tensor-product Hilbert space of ∂f, `h_f` has *unique product-constant vacuum* and a gap of at least `c_loc`, because the first excited SU(2) Casimir is 3/4 and `a_e/d_e≥a_*/2`.
3. The `h_f` commute and are simultaneously diagonal in the product Peter–Weyl resolution. Their supports **match** those of `φ_f`. In units `c_loc`, `\bar h_f=h_f/c_loc` has local gap ≥1 and `||\bar φ_f||≤(16/3)(b_*/a_*)=:β`, since `0≤1-p_f≤2`.
4. The face-overlap graph has degree ≤4: at most one other face shares each of four edges. For any set I of faces, at most `5|I|` local classical terms touch its link union, and those local terms together involve at most `20|I|` edges. These constants are independent of graph volume.

**Proof:** coefficient counting, the one-link Peter–Weyl Casimir spectrum and the elementary four-face incidences give the four claims without the desired interacting gap. If dangling edges of incidence zero are allowed, split off their decoupled electric rotors separately.

**Limitation:** Yarotsky's *global* translation-invariant cluster-expansion theorem is still not directly applicable. Local hypothesis certification is not a global gap theorem.

## Lemma 2 (exact finite-volume mixed-response identities)
Allow independent real parameters `t_f`:
`H(t)=H0+Σ_f t_f(1-p_f)`. Set `κ_f=(3/4)Σ_{e∈∂f}a_e≥3a_*`. At t=0, for the normalized ground eigenpair and tangent gauge `<Ω0,∂Ω>=0`,
```
∂_{t_f} E0(0)                       = 1,
∂_{t_f} Ω(0)                        = p_f/κ_f,
∂_{t_f}∂_{t_g} E0(0)                = −δ_fg/(2κ_f),
∂_{t_f} <p_g>_{Ω(t)} |_{t=0}        =  δ_fg/(2κ_f).
```
**Proof:** normalized Haar character orthogonality gives `∫p_f=0`, `∫p_f²=1/4` and `∫p_fp_g=0` for distinct simple faces, because some edge is unique to one face and integrating it kills the fundamental trace. Also `H0 p_f=κ_f p_f`: the source has spin 1/2 on all four links. Differentiate the eigenvalue equation: `∂_{t_f}Ω(0)=−H0^{-1}Q(1−p_f)Ω0=p_f/κ_f`. Feynman–Hellmann and differentiation of the expectation give the remaining identities.

Along `t_f=s b_f`,
```
E0(s)= s Σ_f b_f − (s²/4) Σ_f b_f²/κ_f + O_G(s³),
<p_g>_s = s b_g/(2κ_g) + O_G(s²),
||Ω'(0)||² = Σ_f b_f²/(4κ_f²).
```
Remainders `O_G` are **not** uniform. The vacuum derivative can grow like `√|F|` for equal couplings; an extensive global-norm Kato estimate cannot give a uniform threshold. The exactly vanishing cross-plaquette response at first order **does not** establish higher-order clustering.

## Lemma 3 (uniform single-time inclusion–exclusion activity estimate)
Normalize `\bar H0=H0/c_loc=Σ_f\bar h_f≥0` and assume `0≤\bar φ_f≤β` in operator order, with `β=(16/3)(b_*/a_*)`. For a set I of faces and t>0 define
```
T_I(t) = Σ_{J⊆I} (−1)^{|I|−|J|} exp[−t(\bar H0+Σ_{f∈J}\bar φ_f)].
```
Whenever `tβ≤1`,
```
||T_I(t)|| ≤ (2 e t β)^|I| .
```
**Proof:** replace each `φ_f` by `z_f φ_f`, obtaining a jointly holomorphic operator-valued function of bounded complex perturbations. For `|z_f|≤r`, nonnegativity of `\bar H0` and the bounded perturbation inequality yield `||exp[-t(\bar H0+Σ_{f∈J} z_f\bar φ_f)]||≤exp(t r β|J|)`; hence `||T_I(z)||≤(2 exp(t rβ))^{|I|}`. If any z_f=0, the signed sum cancels in pairs. Apply the Schwarz lemma in each variable to get `||T_I(1)||≤(2exp(t rβ)/r)^{|I|}` for r≥1. Choose `r=(tβ)^{-1}`. All estimates are volume independent and permit unbounded `\bar H0`. Terms of `\bar H0` supported away from the link union of I commute out, leaving a localized factor on at most 20|I| link sites with the same estimate.

**Warning:** this is only a *single-time* activity estimate. A volume-uniform interacting gap requires a full, convergent **space–time** cluster expansion with excited-state propagation and uniform boundary control, or another complete noncircular argument. Neither is supplied by Lemma 3. Do not promote it to a mass-gap theorem.

## Exact rational fixture and research path
The deterministic checker in `scripts/audit/verify_weak_coupling_lemmas.py` uses two formal edge-sharing four-edge faces with seven distinct edges, all a_e=b_f=1. It verifies coefficient reconstruction, local gap 3/8, unperturbed full-link gap 3/4, κ_f=3, `E0'(0)=2`, quadratic coefficient `−1/6`, and `||Ω'(0)||²=1/18`. Its SU(2) Haar claims are mathematical identities in the proof, not simulated numbers.

**Critical next theorem (OPEN):** uniformly for arbitrary free-boundary Penrose face complexes with this bounded overlap and `b_*/a_*≤ε_*`, prove
`H_G−E0(G)≥c_*a_*(I−|Ω_G><Ω_G|)`
with constants independent of G, **without assuming** mixing or the desired gap. A valid certificate must either (i) prove the graph-uniform extension of the complete Yarotsky space–time polymer expansion (including excited spectral sectors and boundary terms), or (ii) identify a published theorem whose *literal* hypotheses cover the full rotor/hypergraph setup. A one-link electric / four-link magnetic same-support identification is invalid; the face splitting here supplies the corrected local reduction.

**Continuum limitation:** this is a fixed-scale weak-magnetic route; it is not uniform along the Penrose spatial continuum trajectory for which `b_f/a_e` grows. Source-level Stage 7/26 coefficient identity remains a separate verification task.
