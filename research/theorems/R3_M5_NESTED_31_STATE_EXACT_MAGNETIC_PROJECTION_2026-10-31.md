# R3-IR-584 — Systematic nested three-loop spin cutoff: 31-state exact Haar Gram and projected magnetic Hamiltonian

Date: 2026-10-31. The archived M5 candidate 3D prism has rooted retained plaquettes A=4, B=29, D=33, whose holonomies are independent Haar SU(2) variables under tree gauge fixing; their active non-tree chords are 1,26,75,95, with A using 1,26; B using 1,75; D using 75,95.

## The first systematic enlarged trial space

Define V_k (integer k>=2) by the (k+1)^3 products χ_{a/2}(A)χ_{b/2}(B)χ_{d/2}(D), 0<=a,b,d<=k, supplemented with fixed four normalized intertwined traces F_AB,F_AD,F_BD and T=sqrt(2/3)[Tr(ABD)-Tr(ADB)]. Then V_k is nested with dimension (k+1)^3+4; V_2 has **31 states**, contains every vector of the certified R3-IR-583 17-state space and V_3 has 68 states. This is a systematic **character-spin cutoff with four fixed low-spin intertwiners**, not a complete Peter-Weyl/intertwiner cutoff.

## Exact orthonormality

For independent Haar loop holonomies, product SU(2) characters are orthonormal by Peter-Weyl. Each pair fusion F_XY=(2/sqrt3)[Tr(XY)-Tr X Tr Y/2] equals -4/sqrt3 times the dot product of imaginary quaternion vectors. Its squared Haar norm is one, and its conditional average over relative SO(3) orientations vanishes, hence it is orthogonal to all products of class characters. T equals a normalized oriented scalar triple product of three imaginary vectors; its Haar squared norm is one, and orientation reflection gives orthogonality against all product characters and all F_XY. The fusion states have pairwise distinct independent loop-center parity sectors. Therefore the **31×31 Haar Gram matrix is exactly I_31**.

## Exact full projected Wilson magnetic operator

The character recursion χ_{1/2}χ_{n/2}=χ_{(n+1)/2}+χ_{(n-1)/2} (χ_{-1/2}=0), together with product-Haar orthogonality, gives the three 31×31 trace-multiplier matrices. On the 27 product characters, each is a nearest-neighbor index shift by one in its own coordinate, truncated at index 0 and 2. Pair fusions and T have zero trace-multiplier matrix elements among the 31 trial vectors by conditional rotational averaging, independent center parities, and orientation reflection. An all-retained-plaquette link-center XOR support audit confirms **only plaquette indices [4,29,33]** can contribute in this basis, so these are the complete projected magnetic multipliers, not a selected-term approximation.

Using the previously declared candidate Wilson coefficients b=(25.71208103423584,19.380965603695362,14.729533858808479), the nonconstant projected magnetic Hamiltonian is H_B=−(1/2) sum_k b_k T_k. Its 27-character eigenvalues are exactly −(1/sqrt2)(s_A b_A+s_B b_B+s_D b_D), s_k∈{−1,0,1}, and the four additional fusion/triple states have magnetic eigenvalue zero (the full projected energy includes an irrelevant identity shift). The matrix has 108 directed nonzero entries, its lowest eigenvalue is approximately −42.30095234. The entire old 17×17 magnetic block was recovered from independent R3-IR-583 numerical data with max residual 4.55e−15.

## Electric contraction complexity, NOT a new Ritz gap

For spin indices up to 2, per-link-quaternion maximal degrees are 4 on the shared A–B chord 1, 2 on private chord 26, 4 on shared B–D chord 75, and 2 on private chord 95. Electric bilinear integrands therefore have maximum polynomial degree 8,4,8,4, respectively. Hence degree-sufficient cubature is 120×24×120×24=8,294,400 nodes (two 600-cell designs and two 24-cell designs). **The 31×31 electric Ritz matrix has not been contracted; no 31-state Ritz gap is claimed**. A symmetry-sector and/or moment-tensor reduction is the next computational obligation.

The calculation remains a finite candidate M5 rooted-Whitney SU2 Haar Galerkin construction. It is not a full finite-prism Gauss-spectrum calculation, not an actual continuum refinement with calibrated physical running coupling, and not a solution to the continuum Yang–Mills mass gap.

Executable `build_m5_nested_31_magnetic.py` and full 31×31 numerical JSON `m5_nested31_exact_gram_magnetic_2026-10-31.json` are persisted to ChatGPT Library /The Singular Boundary/Source/. Original incidence and Whitney matrices remain in Library.
