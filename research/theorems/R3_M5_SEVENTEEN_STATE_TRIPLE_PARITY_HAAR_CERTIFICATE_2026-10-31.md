# R3-IR-583 — Certified-degree 17-state M5 triple-trace Ritz by exact selection rules

Date 2026-10-31. This resolves the R3-IR-582 high-degree integration objection without recomputing its full 17-state tensor.

## Selection and polynomial degree

Let the three retained rooted Wilson holonomies be A=plaquette 4, B=29, D=33. The fourth active chord coordinates in tree gauge provide independent Haar-distributed A,B,D because each can be solved triangularly from independent chord variables. The 16-state trial space of R3-IR-581 comprises products of characters chi_{n/2}(A)chi_{m/2}(B), n,m∈{0,1,2}, and fundamental characters of D plus pairwise fused traces. Add the normalized oriented triple invariant T=sqrt(2/3)[Tr(ABD)−Tr(ADB)].

For each of three independent loop-center sign flips, the kinetic quadratic form is invariant: the edge-link center flip leaves adjoint-root transports unchanged, and Haar measure and K are unchanged. T has parity (1,1,1); among the old sixteen basis states, **only the ABD character-product vector** has this parity. Accordingly all other electric cross entries E_(old,T) vanish exactly, not merely numerically.

For the remaining two coefficients E_(T,T) and E_(ABD,T), both trial functions have quaternion polynomial degree ≤2 in each shared chord 1 and 75 and ≤1 in the private chords 26 and 95. Differentiating by a Lie derivative does not increase quaternion degree in a fixed chord; root gauge transport becomes identity pointwise and tree-link derivatives remain evaluated. Thus their electric bilinear integrands have degree ≤4 in each independent chord, so the old 24-point 24-cell SU2 degree-five design was already exact for THESE coefficients. The complete old 16×16 electric submatrix is taken from the separately degree-eight-certified R3-IR-581 result.

For projected magnetic multipliers Tr(A),Tr(B),Tr(D), consider simultaneous quaternion conjugation A→A*, B→B*, D→D* (negation of all vector parts). The product Haar law of independent A,B,D is invariant; all old basis vectors and all three Wilson trace multipliers are unchanged (the fused pair trace is also unchanged), whereas Tr(ABD)−Tr(ADB) changes sign. Hence ALL new magnetic offdiagonal entries vanish identically. The new magnetic diagonal vanishes additionally by the triple-state center parities. Other retained plaquette multipliers have zero projected matrix elements by the all-plaquette edge-center support audit inherited from R3-IR-581 (including the new triple state with identical underlying three-loop center support).

## Numerical reconstruction

Stitch the R3-IR-581 certified 16×16 electric and Wilson matrices to the new diagonal E_(T,T)=171.83982609738638 and the sole nonzero new offdiagonal E_(ABD,T)=1.0270082771441225. The reconstructed numerical first two Ritz eigenvalues are approximately E0=-4.83158384, E1=53.71453504, first difference **58.54611888297051**, compared with the 16-state gap 58.546120141058005 (difference -1.2580875e-6). The original 24-cell R3-IR-582 calculation has old E-block residual 5.69e-13; forbidden new electric entries ≤2.20e-16; new magnetic cross entries ≤3.52e-17; new Gram overlaps ≤4.84e-19.

This is a **mathematically degree-sufficient Haar contraction** with ordinary floating-point arithmetic, NOT certified interval bounds on Ritz eigenvalues. The gap difference is tiny and cannot be interpreted as spectral convergence. Neither this 17-state candidate prism Galerkin Hamiltonian nor the six unrelated M approximants establish a full Gauss-law-constrained gap or a continuum 3+1D Yang–Mills mass gap.

Executable: `certify_m5_triple17_parity.py`; output with complete 17×17 matrices: `m5_connected_seventeen_parity_certified_2026-10-31.json`, both in ChatGPT Library `/The Singular Boundary/Source/`. Original 16 and provisional 17 input JSON retained there.
