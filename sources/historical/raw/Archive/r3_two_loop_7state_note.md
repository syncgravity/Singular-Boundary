# R3 continuation — seven-state two-loop audit (2026-10-27)

**Scope:** a four-plaquette 2×2 quadrilateral *spatial disk*, not a provenance-certified Penrose patch. The seven-state result applies to the spatial Wilson measure in the indicated subspace, not to the entire spin-network Hilbert space. The multi-loop mixed transfer sign remains open.

## States and normalization

Label faces 0,1 in the lower row and 2,3 in the upper row. Let `chi_a=Tr_fund(W_a)`. With the disk tree gauge fixing, its four plaquette holonomies are independent Haar under the unweighted measure. Define seven orthonormal states `1, chi_0, chi_1, chi_2, chi_3, chi_0 chi_3, chi_1 chi_2` in `L²(G^E)^G`. Diagonal pairs have no common edges, so they carry well-defined edge spins (1/2 on their disjoint boundary edges, zero elsewhere) and are eigenvectors of every normalized temporal edge-convolution operator. Products on adjacent faces do **not** have this property; those require nontrivial recoupling, and they are omitted.

## Exact spatial matrix

Let `f(U)=prod_{a=0}^3 exp[-kappa(1-chi_a/2)]` and `mu_0=q=2exp(-kappa)I_1(kappa)/kappa`, `mu_1=q*2I_2/I_1`, `mu_2=q*(1+3I_3/I_1)`.

For labels S,T as subsets of the four face indices, the exact 7x7 principal matrix `F_{S,T}=int f Psi_S Psi_T dU` is

`F_{S,T} = prod_{a=0}^3 mu_{1_{a in S}+1_{a in T}}`.

Every entry is strictly positive at kappa>0. This proves entrywise positivity of the mixed sector, but is not an invariance statement: `F` can take a chosen state outside the seven-state subspace.

## Two independent, overlapping temporal selections

Use periodic three-step temporal Wilson transfer with no temporal faces in step three. For step one turn on temporal links on the disjoint loop pair (0,3), each with coupling gamma1=3. For step two turn on temporal links on loop pair (1,2), each with gamma2=5. The supports differ and share spatial links through adjacency; in each step the pair of loops is edge-disjoint. An edge-spin network state S has temporal eigenvalue `x_S=prod_{e on boundary(S)} I_2(gamma1_e)/I_1(gamma1_e)` if every occupied edge has a positive coupling in step one, otherwise zero; similarly `y_S` for step two.

The exact included mixed trace contribution is

`M_7=sum_{S,T in seven labels except vacuum} x_S y_T F_{0,S} F_{S,T} F_{T,0} >=0`.

At kappa=2, the script computes `M_7=7.104434027835627e-10`, of which single/two-loop cross terms contribute `8.667218452045165e-11` and two/two-loop term `2.4363882325612055e-12` (all positive). These values are for UNNORMALIZED spatial Wilson multiplier and the indicated temporal Wilson normalizations. They cannot be interpreted as probabilities or a certified sign of the full mixed term.

## Unsettled recouplings and comparison

On adjacent faces, the shared edge carries 1/2 ⊗ 1/2 = 0 ⊕ 1. One must build orthonormal intertwiner-coupled eigenstates, compute `F_{alpha,beta}` including the one-loop cross terms, and **also control all omitted higher-spin states**. Positive entries on the seven-state block do not make the full coefficient positive: `F_{alpha,beta}` can change sign in other channels and the 7x7 principal block is not an invariant transfer subspace of F. No support-local `O(|Q| log lambda)` theorem for two arbitrary temporal supports follows.

`r3_two_loop_7state.py` reproduces the exact character moments and numerical example; `r3_two_loop_7state_certificate.json` and `r3_two_loop_7state_matrix.npz` preserve the results.
