# R3-IR — Connected 3×3 SU(2) Wilson activation and corner-sewing theorem

**Date:** 2026-10-29. **Scope:** finite Gauss-invariant Wilson Hamiltonian on a complete 3×3 square-rhombus disk with free boundary links. Full mathematical report and two independent deterministic verifiers are in the archive singular_boundary_connected_bulk_corner_sewing_2026-10-29.zip (SHA256 aa123b845f151648741b01e8aca551a9d14e413b053d9966276e7e13ef42654b). This result does **not** establish connected Penrose bulk flat-cap survival or a physical mass gap.

## CB-1: magnetic activation support theorem

Remove the central face f's magnetic potential. Surrounding magnetic faces are the four edge-sharing cardinal neighbors N,E,S,W and four connecting corners NE,NW,SW,SE, each having an independent positive coupling fraction. Every choice of activated surrounding faces among the 256 subsets defines a genuine finite nonlinear Wilson Hamiltonian.

If any cardinal is absent, a target edge is magnetically private and the deleted face holonomy is **exactly Haar**. If all cardinals are present but at most two corners are active, the remaining edge-connected magnetic components meet the target face along proper contiguous open arcs. By the prior full-coupling open-arc theorem, its deleted holonomy is again **exactly Haar**.

Exhaustive 3×3 face-incidence enumeration therefore gives **251 exactly Haar subsets**, and just **five not covered by the Haar theorem**: the four subsets containing all cardinals and exactly three corners, and the subset containing all eight surrounding faces. The five are not asserted to have non-Haar holonomy.

## CB-2: enhanced SU(2) character filtration

Let r=(r_N,r_E,r_S,r_W) and s=(s_NE,s_NW,s_SW,s_SE) be the coupling fractions and c_j(r,s) the normalized ground-state expectation of the target Wilson character of integer spin j>=1. Every surrounding face has a private boundary link on the complete 3×3 disk. Multiplying its boundary link by the center -I flips only that face's Wilson trace and preserves all other potentials and the link Laplacians. Thus c_j is **even in each of the eight couplings separately**.

At a given cardinal coupling r_k=0, its target-shared edge is magnetic-private; the unperturbed positive vacuum has shared-link spin zero, and the unperturbed reduced resolvent preserves this spin. One insertion of the restored neighboring fundamental Wilson trace changes that link spin by at most 1/2. Therefore any nonzero Taylor monomial of c_j must contain a power at least 2j of **each** of the four cardinal couplings.

CB-1 says c_j vanishes identically if at most two corners are active. Thus a nonzero monomial also needs at least **three distinct corner couplings**; independent center parity forces exponent at least two on each. Every nonzero Taylor monomial has total degree at least
\[
\boxed{8j+6.}
\]
For the simultaneous common-coupling specialization t at the finite-volume all-free origin, c_j(t)=O_j(t^(8j+6)). Thus spin 1 first *may* respond at order 14, spin 2 at 22, spin 3 at 30. No coefficient sign, nonvanishing, refinement-uniform analyticity radius, or full-coupling bound is asserted.

## CB-3: exact full-coupling corner-sewing decomposition

Set the four cardinal coupling fractions to one and let G_a(s)=expectation of the nonnegative SU(2) convolution cap observable k_a(W_f) at corner fractions s. Write alpha_a=int phi_a, nu_a=int phi_a^2, k_a=phi_a*phi_a^vee, so 0<=k_a<=nu_a 1_{B_a}. The exact Haar bridge theorem gives G_a(s_S,0_{S^c})=alpha_a^2 whenever |S|<=2. Independent center flips make G_a even in each corner fraction.

For S a subset of the four corners, write d_S^2=product over c in S of the second partial derivative with respect to s_c. The anchored multivariate fundamental theorem of calculus and separate evenness give the exact full-coupling identity
\[
\boxed{
G_a(1,1,1,1)-\alpha_a^2=
\sum_{S\subset\{NE,NW,SW,SE\},\ |S|\in\{3,4\}}
\int_{[0,1]^S}
\left(\prod_{c\in S}(1-s_c)\right)
d_S^2G_a(s_S,0_{S^c})\,ds_S.
}
\]
There are **four minimal eight-face triple-corner responses and one nine-face quadruple-corner response**. Taking the negative parts gives a sufficient cap criterion, but no bound on those signed derivatives is presently proved for the connected physical Wilson vacuum.

## CB-4: one-sided mixed-response budgets are not necessary

The positive analytic non-physical function F=alpha_a^2[1+M(product over four cardinals r_i^2(1-r_i^2)) s_1^2s_2^2s_3^2] obeys all coordinate-plane Haar conditions and separate coupling parity and returns exactly to Haar at the full endpoint. However its four-cardinal eighth mixed derivative has a negative region that grows with M. Thus taking negative parts of mixed derivatives before integration can be needlessly restrictive. This is a **scalar comparator**, not a Wilson Hamiltonian ground state.

## Independent verification and open claims

Companion scripts verify all 256 graph supports and 24 primal edges, SU(2) Haar character orthogonality, the rigorous order thresholds, the exact symbolic four-corner identity and the scalar comparator. They do not diagonalize the eight-face SU(2) physical vacuum.

**Proved:** CB-1–CB-4 in the explicitly stated finite domain. **Open:** estimate the signed full-coupling response in the **minimal eight-face connected physical SU(2) patch**, then obtain uniform estimates for the fully cycle-surrounded Penrose deleted vacuum; fixed-support connected covariance, regulator-uniform mass gap, quartic resolvent and continuum reconstruction.
