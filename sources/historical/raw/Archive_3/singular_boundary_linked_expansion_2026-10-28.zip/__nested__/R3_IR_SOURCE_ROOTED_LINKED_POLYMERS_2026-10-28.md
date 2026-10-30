# The Singular Boundary — source-rooted linked expansion and finite-temperature polymer convergence

**Date:** October 28, 2026. **Scope:** finite continuous-time SU(2) Wilson Hamiltonians on finite face-complete rhombus complexes, with original spatial incidence; no MCMC, no historical data replacement. **Evidence:** exact finite-order connectedness and center-parity theorems (independently proved); finite-temperature full-link polymer convergence and spatial clustering (deduced from the published Kotecký–Preiss criterion, whose statement and hypotheses are identified); interacting vacuum **temporal** infrared gap still **OPEN**.

## 1. Physical separation and normalized reference measure

Let `G=(V,E,F)` be a finite spatial quadrilateral complex, every edge in at most two simple faces. Let `L_e=-Δ_e` be the normalized SU(2) Laplacian with spin-j eigenvalue `j(j+1)` and `a_e>0`, `b_f≥0`. On **the full tensor product** `H_full=⊗_{e∈E}L²(SU(2))`, set

`H_s=H_E+s Σ_f b_f(1-p_f)`, `H_E=Σ_e a_e L_e`, `p_f(U)=Tr(U_f)/2`, `B_Σ=Σ_f b_f`.

`H_s` commutes with vertex gauge transformations, and its unique finite-volume strictly positive ground state is gauge invariant. At **finite** inverse physical time β, the full-space heat trace is **not** the physical gauge-projected trace. This distinction is essential. At each fixed finite G, however, its normalized zero-temperature limit is the same unique physical vacuum, provided the finite-volume ground-state separation (known by compact ellipticity) is used; no claim is made that this limit is uniform in G or regulator.

For `0<t<β` and bounded gauge-invariant real Wilson multipliers A,D, define

`Z_{β,t}(J,K;s)=Tr[e^{-(β-t)H_s} e^{JA}e^{-tH_s}e^{KD}]/Tr[e^{-βH_E}]`.

The connected thermal source derivative is

`C_{β,t}(A,D;s)=∂_J∂_K log Z_{β,t}(J,K;s)|_{J=K=0}`.

By the compact-group Feynman–Kac heat-trace representation, the normalized free electric trace is a **product over spatial links** of independent SU(2) Brownian **loops of period β**, with speed set by `a_e`. If `U_e(u)` is the loop at link e, define `X_f=∫_0^β p_f(U(u))du`, `|X_f|≤β`. The exact source-inserted partition function is

`Z_{β,t}(J,K;s)=exp(-s β B_Σ) E_0[exp(J A(U(0))+K D(U(t))+s Σ_f b_f X_f)]`.

The scalar prefactor does not affect the connected mixed derivative. The independent-link reference is valid here because this is the **full-link thermal trace**; inserting a finite-time Gauss-law projector without proving its factorization would invalidate this particular product-reference step.

## 2. Theorem R1: exact source-rooted finite-order cumulant identity (independently proved)

For every nonnegative integer `n`, the n-th Taylor coefficient of `C_{β,t}(A,D;s)` at s=0 is exactly

`c_n = (1/n!) Σ_{f_1,...,f_n∈F} (Π_i b_{f_i}) κ_0(A(U(0)), D(U(t)), X_{f_1},...,X_{f_n})`,

where `κ_0` is the joint cumulant in the product free-electric Brownian-loop measure. The coefficient formula holds as a finite derivative on each finite graph and any β>t>0. It is a Taylor identity, not an assertion that the series converges uniformly as β→∞ or b grows.

**Proof.** Differentiate the logarithm of the exact product-reference moment generating function. The general multivariate cumulant derivative formula gives the stated term, and multilinearity expands `X=Σ_f b_f X_f`. Every differentiation is justified by bounded A,D,X_f and compact finite-dimensional heat traces.

**Connectedness selection.** Form a dependency graph on two marked roots A,D and the n (possibly repeated) face insertions. Join two vertices if their spatial link supports intersect. If this graph is disconnected, the corresponding joint cumulant vanishes **exactly**, because two groups depend on independent sets of reference link paths. Thus all disconnected insertions cancel **before** any absolute bound is taken. This is the cancellation missing from the extensive operator-norm Dyson estimate.

For n≥1, all contributing insertions lie in the `(n−1)`-neighborhood of faces touching `supp(A)∪supp(D)` in the face-adjacency graph. If both source supports contain in total L distinct links, there are at most `2L` initial faces; the number of candidate faces is at most

`M_n = 2L Σ_{j=0}^{n-1}4^j`.

Let `K_m=Σ_{π partition of {1,...,m}} (|π|−1)!` (the explicit moment–cumulant absolute coefficient). The volume-independent finite-order estimate follows:

`|c_n|≤ (K_{n+2}/n!) ||A||∞||D||∞ (β b_*)^n M_n^n`.

This bound is deliberately crude and grows too fast to prove a common convergence radius by itself; its role is rigorous **finite-order source-locality**, not an infrared estimate.

For **disjoint** spatial source supports, `c_0=0`; the first derivative `c_1` is supported only on plaquettes intersecting both sets, and its bound is

`|c_1|≤ 6 β ||A||∞||D||∞ Σ_{f:∂f∩S_A≠∅,∂f∩S_D≠∅}b_f`

because `K_3=6`. In particular the first-order term vanishes if no single rhombus meets both sources.

## 3. Theorem R2: exact Z2 link-parity selection (independently proved)

For an oriented closed fundamental Wilson path γ, let `z_γ∈(F_2)^E` record its edge traversal multiplicities modulo 2, regardless of orientation. For a face f, let `z_f` be its four-edge incidence parity. On each free link Brownian loop, the simultaneous center translation `U_e(u)→−U_e(u)` at **all** Euclidean times preserves the electric loop law; it changes a fundamental Wilson trace by sign `(-1)^{z(e)}`.

Consequently, for any term in R1,

`κ_0(W_α(0), W_δ(t), X_{f_1},...,X_{f_n}) ≠0`

**requires**

`z_α ⊕ z_δ ⊕ z_{f_1} ⊕...⊕ z_{f_n} = 0` in `(F_2)^E`.

**Proof.** If the total parity at link e is odd, its center translation reverses the product of all variables. In every product of moments appearing in the cumulant partition formula, at least one moment block must have odd parity at e; that block has expectation zero. Hence the entire cumulant is zero.

For a given pair of source paths, the minimal perturbative order is at least the least number of plaquettes whose mod-2 sum equals `z_α⊕z_δ` (if such a filling exists), and can be **strictly higher** when the source-rooted connectedness rule is imposed. The conditions are necessary, never claimed sufficient for nonzero coefficients.

**All-coupling center-sector selection.** If `z_α⊕z_δ` is outside the F₂-span of all face parities, finite-dimensional F₂ duality produces an edge center assignment that leaves every plaquette potential invariant but flips the source product. The connected source correlation then vanishes for **every** nonnegative magnetic coupling, not merely order by order. The same reasoning explains the limitation of contractible source families in center/winding sectors.

### Historical three-rhombus seed fixture

Using precisely the three `seed_faces_z5` transcribed from the Library's `HISTORICAL_Q14_CANONICAL.json`, the finite seed has 10 distinct edges, face adjacency `f0—f1`, `f0—f2`, and no f1–f2 shared edge. The exact verifier exhaustively checked 2,186 ordered face-insertion strings across orders 0–6 for two source pairs:

* A=W_f0, D=W_f1: the first order **permitted by both parity and connectedness** is n=2.
* A=W_f1, D=W_f2: the first parity-permitted order is n=2, but the first order meeting **both** constraints is n=4. Two copies of the bridging f0 face are necessary to maintain center parity.

These are purely **necessary selection rules**, not claims that the permitted coefficient is actually nonzero. This is the *three-seed spatial subcomplex only*: adding faces in the full original Q14 Penrose disk may introduce other routes and change the minimum order. It must not be represented as a certificate for the complete historical Q14 insertion or its three-time-slab cavity.

## 4. Theorem R3: finite-temperature polymer resummation with explicit volume-independent criterion

Let `u_f=e^{s b_f X_f}−1`. For complex s, `||u_f||∞ ≤ u := e^{|s| β b_*}−1`. Expanding `∏_f(1+u_f)` produces a hard-core polymer gas: a polymer P is a connected **set of distinct spatial faces** in the shared-link adjacency graph; its activity is `w(P)=E_0∏_{f∈P}u_f`. Disjoint compatible polymers have disjoint underlying link-path supports, so their expectations factorize exactly. Two polymers are incompatible if their face sets intersect or are adjacent in the shared-link graph.

The face graph has degree at most 4. The number of size-k polymers containing a prescribed face is at most `16^{k−1}` by the original volume-independent connected-set bound. A polymer Q of size m has at most 5m faces in its one-step closed neighborhood. Thus for `16eu<1`,

`Σ_{P incompatible with Q} |w(P)| exp(|P|) ≤ 5m Σ_{k≥1}16^{k−1}(eu)^k = 5m eu/(1−16eu)`.

In particular the **explicit sufficient condition**

`e^{|s| β b_*}−1 < 1/(21e)`

verifies the *literal* Kotecký–Preiss polymer criterion with `a(P)=|P|`. The standard KP theorem therefore implies an absolutely convergent polymer cluster representation of the normalized full-link finite-temperature `log Z`, including a uniform in-volume per-face rooted bound and partition zero-freeness in this complex coupling disk.

This is a valid **published-theorem deduction**; we did not independently reprove the abstract Kotecký–Preiss theorem. A modern accessible statement with the rooted tail is Theorem 2.2 of Jenssen et al. (2026), DOI 10.1112/jlms.70624; the classical source is Kotecký–Preiss (1986). No simulated Wilson configurations or original MCMC were used.

### Two marked sources and a spatial connected bound

Add two factor-graph vertices A,D with activities `u_A=e^{JA(U(0))}−1`, `u_D=e^{KD(U(t))}−1`. Marked vertices touch exactly the faces overlapping their link supports and one another when the sources overlap. If m=max(|supp A|,|supp D|), the expanded factor graph has maximum degree

`Δ'=max(6,2m+1)`.

Choose radii r_A,r_D>0 and θ>0 so that, for s=1,

`u_* := max{e^{β b_*}−1, e^{r_A||A||∞}−1, e^{r_D||D||∞}−1}`

satisfies

`u_* exp(1+θ)(Δ'^2+Δ'+1)<1`.

The same connected-set count and incompatibility argument verifies the **weighted** KP condition with `a(P)=|P|`, `g(P)=θ|P|`. Marked-polymer clusters contributing to the mixed source logarithmic derivative must contain both A and D, and their total polymer cardinality is at least the distance `d_H(A,D)` between the marks in the expanded factor-dependency graph. The KP rooted-cluster estimate, with a zero-weight auxiliary root at A, and two-variable Cauchy differentiation give the **finite-temperature spatial clustering estimate**

`|C_{β,t}(A,D;1)| ≤ (r_A r_D)^{-1} exp[−θ d_H(A,D)]`.

This bound is **independent of ambient spatial volume** (subject to the common finite β and smallness assumptions). All estimates are at the full-link thermal level, for any temporal separation `0<t<β`; they do **not** imply decay with t or the physical vacuum spectral gap. The published KP criterion and its rooted bound are the only imported convergence theorem; source-factor geometry, constants, and mark cancellation are derived here.

## 5. Where this proof succeeds—and where it stops

**Independently proved here:** exact finite-order source-rooted cumulant identity, cancellation of all disconnected terms, the F₂ parity constraint, explicit coefficient locality and the three-seed verification fixture. **Published-theorem deduction with checked hypotheses:** volume-independent polymer convergence and high-temperature **spatial** connected clustering under the explicit KP inequality.

**Not established:** a convergence radius uniform as β→∞; vacuum temporal connected decay at a common positive physical rate; interacting strong-magnetic Penrose spatial refinement; nontrivial quantum continuum fields; the complete original Q14 pointwise/annealed insertion comparison. The sufficient smallness `β b_*≈0.017` for unmarked polymers forces β to be small at fixed magnetic strength. With the historical geometric refinement `b_*∼a_sp^{−2}`, the threshold demands `β=O(a_sp²)` (even more restrictive when the marked-source complexity grows). A proof of infrared vacuum time decay **cannot** be extracted by sending β→∞ in this absolute-convergence estimate.

**Next noncircular gate:** prove a source-rooted connected expansion around the interacting ground-state measure, or a time-blocked/renormalized representation, whose cluster weights remain summable for arbitrarily long physical Euclidean time **and** along the strong-magnetic spatial trajectory. A single-face Poisson tail, finite β KP convergence, center parity, and finite-order selection do not establish such a bound. Any proposed extension must supply an independent large-field and low-energy mixing estimate rather than assuming the desired gap.

## Integrity and reproducibility

Primary fixture transcribed from immutable `HISTORICAL_Q14_CANONICAL.json/seed_faces_z5`. All script checks are integer combinatorics or exact rational calculations; no MCMC replay. The repo branch contains a new derived proof report, a read-only script and certificate hashes; original files remain untouched. The GitHub remote branch must be inspected before updates. See `LINKED_SELECTION_CERTIFICATE.json` and `verify_rooted_selection.py`.
