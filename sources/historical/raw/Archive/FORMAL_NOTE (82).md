# Exact open four-port spin-1/2 contraction on the four-prism loop

**Model.** The previously verified 2×2 combinatorial quadrilateral patch extruded over one time interval: 18 vertices, 33 edges, 20 faces, four prism cells, with four interior temporal faces Q=(3,4,10,13). This is *not* certified as a geometrically extracted Penrose patch.

**Object.** For each of the two parity-minimal eight-retained-face subsets S, compute the open four-port matrix

M_S = ∫ [∏_{p∈S} χ_{1/2}(W_p(U))] ⊗_{q∈Q} D_{1/2}(W_q(U)) dU,

where each face holonomy is based at the smallest-numbered incident vertex and traversed in its incidence orientation. The tensor-factor order of the four port matrices is Q=(3,4,10,13). All group integration is with normalized product Haar measure. The open matrices are matrix moments; their matrix positivity is basis-path dependent. They have not been identified with the Fourier coefficient of a globally gauge-fixed, *independent* interface-coordinate kernel.

**Exact integration.** Write each SU(2) fundamental matrix as U=x0 I+i∑_{k=1}^3 xk σk, where x lies uniformly on S^3. Each edge occurs either twice or four times in the twelve-face integrand. Integrate its tensor indices using

E[x_a x_b]=δ_ab/4,

E[x_a x_b x_c x_d]=(δ_ab δ_cd+δ_ac δ_bd+δ_ad δ_bc)/24.

For inverted edge orientation use U†. Contract remaining face trace indices exactly. The central four-valent link integral is thereby retained *without factorizing into independent pairings*; in a uniform-orientation basis its four-fundamental Haar integral is the projector onto a two-dimensional SU(2) singlet subspace.

**Result.** For the two minimal retained surface assignments S03=(0,1,2,5,16,17,18,19) and S12=(6,7,8,9,11,12,14,15), in this ordered based-face convention:

M_03 = (1/2048) SWAP_{34},   M_12=(1/4096) I_16,

where SWAP_{34} interchanges the third and fourth two-dimensional representation factors. Each has trace 1/256, verifying the earlier scalar six-face-sphere calculation. SWAP_{34} has eigenvalues +1 of multiplicity 12 and −1 of multiplicity 4. Hence

M_03+M_12=(2 SWAP_{34}+I_16)/4096

has eigenvalues +3/4096 (multiplicity 12) and −1/4096 (multiplicity 4), with trace 1/128. The eighth-order coefficient of the unnormalized Wilson-weighted open-port matrix (with all 16 retained faces assigned equal coupling β) is

A_8=(M_03+M_12)/2^8=(2 SWAP_{34}+I_16)/1048576.

Its trace is 1/32768, in agreement with the previous scalar result, and its spectrum has four strictly negative eigenvalues −1/1048576.

**Higher-order check.** The exact open-port Wilson matrix has the Taylor expansion M(β)=β^8 A_8+O(β^9) in operator norm at β↓0. Each port matrix element is bounded by 1 and the retained total action lies in [0,32β], giving the elementary norm bound

||M(β)-β^8 A_8|| ≤ 16 exp(32β) (32β)^9/9!

for β≥0 (safe factor 16 converts a uniform entrywise bound to operator norm). A rigorous representation-spin truncation also follows using the positive face-character absolute mass τ_J(β), with an operator norm bound ≤256 τ_J(β). Neither bound gives a coupling-independent correction at β→∞ with fixed J.

**Interpretation.** This is the complete *minimal-order* open fundamental matrix contraction, including the central two-dimensional intertwiner sector. The positive scalar trace does not imply positivity of the full matrix: the leading open matrix contains a negative sector. This is **not** a proof that the fully gauge-fixed effective boundary kernel fails positive-definiteness, or that the final insertion free-energy comparison fails at strong coupling. Those remain open and require a basepoint-consistent gauge-fixed kernel and higher-representation resummation.

Run `python compute.py` to regenerate the exact edge-moment tensor contraction and verify all matrix and scalar identities. The full `matrices.npz` and `certificate.json` are included.
