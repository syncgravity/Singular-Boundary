# Exact all-length Peter–Weyl spectrum of the free original-link SU(2) straight chain

**Date: 2026-11-01.** Scope: independent face holonomies on a finite **open straight** chain, with the original-link electric generator and the previously reconciled shared-edge orientations.

Let `l_i>=0` be the SU(2) Peter–Weyl degree on face i, `s_i=l_i/2`, `c_i=s_i(s_i+1)`, and `d_i` its number of neighbors on the open path (`d_i=1` at the ends, `2` in the interior for m>=2). The original-link operator is

`K_m=4 sum_i C_i + 2 sum_{i=1}^{m-1} sum_{a=1}^3 R_i^a L_(i+1)^a`,

where `C_i=l_i(l_i+2)/4` on the fixed degree sector and the generator normalization is imaginary quaternion basis divided by 2. Put `B_i=2 sum_a R_i^a L_(i+1)^a`.

## Crucial exact commutation

For |i-j|>1, B_i,B_j act on disjoint face sets. For neighboring edges, B_i uses `L_(i+1)^a` and B_(i+1) uses `R_(i+1)^b` on their shared middle face. Since left- and right-invariant SU(2) vector fields commute, `[B_i,B_(i+1)]=0`. Consequently **every B_i commutes with every B_j**, and all commute with the face Casimirs. No noncommuting spin-chain diagonalization is required in this particular original-link open-path geometry. This corrects the previous assumption that neighboring terms did not generally commute.

## Full block spectrum and multiplicity

Each face Peter–Weyl space is `V_(s_i)^L tensor V_(s_i)^R`, dimension `(l_i+1)^2`. Each edge B_i couples the right spin of face i with the left spin of face i+1. All these coupled tensor factors are disjoint because the two chiral actions on an interior face are independent. For each edge choose

`J_i=|s_i-s_(i+1)|, |s_i-s_(i+1)|+1,...,s_i+s_(i+1)`.

The edge Casimir identity gives the B_i eigenvalue `J_i(J_i+1)-c_i-c_(i+1)`. Thus for m>=2

**`kappa_(l,J) = sum_i (4-d_i)c_i + sum_(i=1)^(m-1) J_i(J_i+1)`**

with exact multiplicity **`(l_1+1)(l_m+1) product_(i=1)^(m-1)(2J_i+1)`**. The endpoint factors are the unused left spin of face 1 and right spin of face m. The sum of multiplicities across all J choices is `product_i(l_i+1)^2`. For m=1, the eigenvalue is `l_1(l_1+2)` of multiplicity `(l_1+1)^2`.

## Exact uniform free spectral gap

For m>=2, every coefficient `(4-d_i)` is 2 or 3, and each edge Casimir `J_i(J_i+1)` is nonnegative. If precisely one l_i is nonzero, its fixed-degree block has eigenvalue `4c_i=l_i(l_i+2)>=3`, since the J's on incident zero-spin edges are forced to equal s_i. If two or more l_i are nonzero, `sum_i(4-d_i)c_i>=2*(3/4)*2=3`, and any equality with zero edge terms is excluded when only two nonzero face degrees would have to be interior and all neighboring J zero: at the boundary of any occupied cluster, an adjacent zero spin forces a positive J=s_i. More directly, the quadratic-form comparison `K_m >= 4 sum_i C_i -2 sum_adj sqrt(C_i C_(i+1)) >= sum_i(4-d_i)C_i` gives 3 as a universal lower bound when at least two occupied faces, and the strictness follows from the spectral edge term or from boundary forcing. The isolated one-face degree-l=1 modes have electric eigenvalue exactly 3 in every m. Thus the exact free gap is **`gap(K_m)=3`**, and the unrestricted normalized mean-zero Haar inverse norm is **`||K_m^-1||_(L2_0 to L2_0)=1/3`** for every finite open m.

This improves the previous valid but nonsharp `gap>=3/2` comparison. Any earlier derivation using the latter bound remains valid; constants in those estimates can potentially be sharpened. The sharpened gap alone **does not** establish an analytic-coefficient-ℓ¹ inverse bound: Peter–Weyl Haar-L² and coordinate ℓ¹ norms are different, and cancellations/basis condition numbers can depend on degree and interval length.

## Exact tests

`verify.py` enumerates degrees 0..3 on chains of lengths 1..5 using exact rational arithmetic, checks the entire spectral multiplicity against Peter–Weyl dimensions and the exact free gap, and checks previously archived small sectors. It constructs three-face 64x64 quaternion derivative matrices and verifies directly `[B_12,B_23]=0`. These finite checks complement the all-degree algebraic proof.

**Open:** intrinsic analytic-norm inverse bound, convergence of the connected vacuum-score expansion, interacting gap at lambda=1, Penrose signed-current theorem, and continuum Yang–Mills mass gap.