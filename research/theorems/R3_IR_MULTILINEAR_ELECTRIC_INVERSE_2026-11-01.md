# Exact electric-inverse coefficient norms in multilinear SU(2) sectors

Date: 2026-11-01. Model: positive original-link electric operator on a finite, straight, open chain of SU(2) plaquette holonomies. Scope: multilinear fundamental-coordinate sectors on 1, 2, and 3 consecutive faces only.

For m faces, let W_m=span{prod_i x_{i,a_i}: a_i in {0,1,2,3}}, so dim W_m=4^m. Each quaternion coordinate is linear in its own face holonomy, and W_m is invariant under the original-link K. In coefficient coordinates,

K_m|W_m = 3m I + 2 sum_{i=1}^{m-1}sum_{k=1}^3 R_i^k L_{i+1}^k.

The left and right matrices are the quaternion infinitesimal generators e_k/2, transposed for action on polynomial coefficient vectors; see verify.py. This is the physically reconciled opposite shared-link orientation, and K is symmetric in these bases.

Exact SymPy rational inversion proves:

| m | dim W_m | eigenvalues (multiplicities) | induced coefficient l1 norm ||K_m^{-1}||_{1->1} |
|---|---:|---|---:|
|1|4|3 (4)|1/3|
|2|16|9/2 (4), 13/2 (12)|2/9|
|3|64|6 (4), 8 (24), 10 (36)|1/6|

For f in W_m, the coordinate analytic norm defined by ||f||_sigma^coef=sum_alpha |c_alpha|e^{sigma|alpha|} is simply e^{sigma m}||c||_1, so these operator bounds hold at the **same** sigma for each indicated W_m. The multilinear coefficient vector is unique on SU(2)^m, as its monomials are independent matrix-coefficient functions; the generic ambient quaternion-coordinate norm for arbitrary polynomial degrees is **not** an intrinsic quotient norm without choosing a representative or infimizing over sphere relations.

This is not a theorem that sup_m ||K_m^{-1}||_{1->1} is finite, nor that arbitrary mixed-degree Peter-Weyl/spin-network sectors have bounded inverse. The three matrices are finite-dimensional verification. In particular, a same-radius inverse in W_1,W_2,W_3 does not close the nonlinear analytic connected-score recurrence, because Gamma multiplies these sectors and generates higher degree and other representations.

## Reproduce

Run `python verify.py` using SymPy. The script prints the exact eigenvalues and induced column-sum inverse norm and verifies matrix inversion symbolically.