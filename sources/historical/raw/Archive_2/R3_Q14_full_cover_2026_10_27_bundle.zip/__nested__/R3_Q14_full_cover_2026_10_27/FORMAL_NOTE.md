# Original Q14: exact 54-face fractional cover and pair-staple SU(2) bounds

**Date:** 2026-10-27. **Scope:** the authenticated original `cavity_audit.py` in the uploaded `R3_uploaded_gaussian_audit_2026_10_27_bundle.zip`. All computations use its Q14 relative to the fixed central three Penrose rhombi and 3-periodic time. Four nested cutoff radii tested. This work is NOT a proof of the arbitrary-nonstationary Gibbs suppression theorem.

## 1. Recovery of the exact original insertion

The mounted Gaussian audit bundle includes `direct_cut_project.py`, `cavity_audit.py`, `construct_surgery.py`, and `verify_bianchi.py`. Running `Q_from_seed` on radii 5, 6.5, 8, 10 produces **Q=14**, **H=36** and **A(H)=62**. `solve_cover.py` independently reconstructs the actual 54-face Bianchi fill set by deterministic single-prism peeling and verifies `|F \ A(H)|=10`, `|F∩A(H)|=44`. The original `verify_bianchi.py` supplies an independent energetic certificate with coefficient 44. No surrogate 14-face support was used.

## 2. Exact 54-face fractional cover

Let F be the 54 retained Bianchi-fill faces, E_F the 101 links occurring in those faces, and M the 54-by-101 unsigned face/link incidence matrix. Solve

`min sum_e w_e`, subject to `M w >= 1`, `w >=0`.

The HiGHS linear-program solution is **22**, with **40 positive link weights**. A matching feasible nonnegative dual `y` satisfies `M^T y <= 1` and `sum_f y_f=22`, proving *global LP optimality*, not just an observed heuristic. The stored primal and dual numbers were converted to `fractions.Fraction` with denominator ≤10,000, and feasibility and equality of their objective values were checked using exact rational arithmetic. Each `cover_radius_*.json` contains both witness vectors, the full incidence matrix, and the exact rational objective `22`. Results are unchanged across all four volumes.

The original H links alone **cannot** cover the ten outside faces. The solved fractional cover uses 40 links and includes those ten faces. The union of all retained link stars on those 40 links has **103 faces**, of which **49 lie outside F**. This is **star-action leakage**, not a flaw in the fractional cover: the SU(2) heat-bath inequality applies to the whole retained star for each chosen link, not only faces in F.

For the actual retained Wilson Gibbs law, the sharp SU(2) single-link conditional excess inequality gives

`λ E S_F <= (3/2) sum_e w_e + λ sum_e w_e E m_e`

and hence the new **ambient-volume-independent conditional estimate**

\[
\boxed{\lambda\mathbb E_{\mu_{R,\lambda}}S_F\le 33+\lambda\sum_{e\in E_F}w_e\mathbb E_{\mu_{R,\lambda}}m_e.}
\]

This holds for each of the four tested volumes and, by identical local incidence, any larger disk preserving the local star data. The constant 33 is exact and depends on the original support only.

## 3. New explicit pair-staple loop inventory

For the 40 positively weighted links, `pair_bounds.py` constructs every retained-star staple word and its pair disagreement word `a_(p,e) a_(r,e)^(-1)`, preserving **free noncommutative word ordering**. There are **225** pair-loop words, each of freely reduced link length **6**. Star degrees are: 2 links of degree 2, 10 of degree 3, 23 of degree 4, 4 of degree 5, and 1 of degree 6. The 225 loops, their labels and ordered signed link words are in `pair_staple_radius_*.json` for all four volumes. Quaternion evaluation independently checked the identities for all 900 exported words; maximum residual <4e-16.

Write `a_i ∈ SU(2)=S^3` for the staples incident to a selected link `e`, `n=n_e`, `R=|Σ_i a_i|`, and `d(g)=1-ReTr(g)/2`. The following hold **pointwise** for every noncommuting SU(2) link assignment:

\[
 m_e=n-R=\frac{2\sum_{i<j}d(a_i a_j^{-1})}{n+R}\le \frac2n\sum_{i<j}d(a_i a_j^{-1}).
\]

If the current retained-star action is `S_e=Σ_i d(W_i) <= δ < n`, then `R>=n-δ`, giving the **good-field strengthened bound**

\[
 m_e\le\frac{2}{2n-\delta}\sum_{i<j} d(a_i a_j^{-1}).
\]

Moreover `d(a_i a_j^{-1}) <= 2[d(W_i)+d(W_j)]`, by the SU(2) Euclidean chord-distance triangle inequality and the common link's isometry. These bounds are exact and have no ambient-volume dependence. They turn the remaining frustration into a **finite weighted collection of 225 length-six loop energies**. They do not by themselves imply that its Gibbs expectation is `O(1/λ)`.

Combining cover and pair identity yields the explicit sufficient condition:

\[
 \lambda\mathbb E S_F \le33+\lambda\sum_{e\in C}\frac{2w_e}{n_e}\sum_{i<j}\mathbb E d(a_{i,e}a_{j,e}^{-1}).
\]

For all four volumes, `C` has 40 links and exactly 225 pair loops. A uniform bound on the weighted 225-loop expectation immediately gives a uniform bound on the 54-fill energy. The simple triangle bound does not close this estimate because it feeds the original plaquette energies and the 49 leakage faces back into the right-hand side.

## 4. Status of the B-contraction and arbitrary nonstationary theorem

The previously tested elementary 62-by-62 matrix has spectral radius 4, and this work does not derive a new B with `rho(B)<1`. The optimal fractional cover `22` is a **different** linear program from the proposed curvature contraction. No inference `rho(B)<1` is valid from the cover value. Nor do 225 bounded-length loop words constitute a Gibbs concentration estimate. To finish R3 one must either certify a genuinely contractive nonabelian loop-to-face domination (including the 49 leakage plaquettes), or prove uniform Gibbs suppression of the weighted length-six pair-loop energies by a correlated transport/resampling method.

## 5. Branch access and provenance

The model cannot guarantee access to every earlier branch's private session filesystem or conversation transcript. For this calculation, the original **Q14 selection code, prism words, and Bianchi certificate were actually recovered from the currently mounted Gaussian-audit archive**. The original 59-pivot implementation is not required for the cover computation and was not independently recovered or certified here. The calculation is reproducible using the sources inside this bundle.

## 6. Run

From the extracted directory: `OPENBLAS_NUM_THREADS=1 python solve_cover.py`, followed by `python pair_bounds.py` and `python verify_pair_words.py`. Dependencies: numpy, scipy. All 54x101 incidence data, primal/dual witnesses, 225 exact pair words per volume, and independently checked quaternion residuals are saved as JSON.
