# Penrose 54-face frustration closure: proof obligations and a certified criterion

Date: 2026-10-27. Scope: local finite-rank SU(2) Wilson inequalities on 2D Penrose rhombus-prism spacetime patches. **No 54-face Penrose matrix has been certified here.** The standalone generator in Phase III constructs the spatial rhombus disk, but the 14-face insertion indexing, 54 retained fill faces, and complete nonabelian staple-word certificates are not supplied in the current mounted files. Reconstructing a different cavity or treating a demonstration matrix as the Penrose matrix would be unsound.

## Conditional matrix theorem

Let `G` be a *finite fixed* retained-face set containing `F=A_fill`. For each `p in G` choose an incident retained link `e(p)`. Define the local star `S_e=sum_{r in R: e in boundary r} d(W_r)` and its conditional minimum `m_e=min_{U_e} S_e` (all other links frozen). For the SU(2) Wilson Gibbs measure the exact conditional heat-bath inequality is `lambda E(S_e-m_e)<=3/2`. As `d(W_p)<=S_e`, we have

`x_p := lambda E d(W_p) <= 3/2 + lambda E m_{e(p)}`.

Suppose independently proved **pointwise for all link assignments** that

`m_{e(p)} <= sum_{r in G} B_{pr} d(W_r)`, where `B>=0` and is independent of surrounding volume and lambda.

Then `x<= (3/2)1+Bx`. If `rho(B)<1` then `x <= (3/2)(I-B)^(-1)1`, so `lambda E S_F <= (3/2) sum_{p in F}[(I-B)^(-1)1]_p`. This is volume-uniform. The matrix proof does *not* follow from Bianchi fillability alone.

There is also a useful *strict positive supersolution criterion*: it is enough to produce `h>0` with `Bh<=theta h` for an explicit `theta<1`. Then `rho(B)<=theta` by Collatz-Wielandt. A finite proof should include exact rational/interval certification of `Bh<=theta h`, a hash of the canonical incidence, and a **word-level nonabelian proof of each inequality**, not just Monte Carlo tests.

## Closure of the face set and boundary leakage

The inequality must include **all** faces appearing on its right side. If some pair-staple loops require plaquettes outside G, write `m<=B d_G + C d_out`. Then the correct vector inequality is `x<=1.5 1+B x + C y_out`. Even when `rho(B)<1`, the term `(I-B)^-1 C y_out` still needs volume-uniform control. A finite positive matrix has no power to remove an uncontrolled exterior boundary term.

## Why the naive Bianchi certificate cannot certify rho(B)<1

For any link `e`, `m_e<=S_e` follows by evaluating the minimum at the current link. This yields a nonnegative incidence-based B, often with row sums >=1; it is not a contraction certificate. Bianchi relations express products of noncommuting face words, but their squared-distance triangle bounds can have coefficients that accumulate, and need not create a contractive matrix. Numerically observing a small eigenvalue for a candidate B does not establish the necessary pointwise bound.

## Immediate reproducible result

`certify_B.py` reads a proposed face-labelled nonnegative matrix and screens its spectral radius and one positive supersolution. Its sample `example_B.json` has rho=0.5, **but it is an illustrative 2x2 algebraic matrix, not a Penrose geometric result**. The utility deliberately reports that the group-word inequalities have not been verified. It is a validation scaffold, not an R3 theorem.

## Next concrete task

1. Reconstruct/extract the exact 14-face Q support and complete 3-periodic-time prism incidence, with canonical link/face labels and hashes.
2. Enumerate the 54 retained fill faces, all link stars, and exact nonabelian pair-staple loop words.
3. Derive coefficientwise inequalities by direct group-word identities and SU(2) inequalities, including any faces outside G.
4. Search for an exactly certifiable nonnegative B with a strictly positive supersolution, and otherwise report the residual boundary leakage or a lower bound forcing rho>=1 in the selected inequality class.
5. If no such B exists, return to a **probabilistic** exterior-Gibbs suppression or a block-resampling/transport inequality; failure of this matrix strategy does not disprove the R3 theorem.
