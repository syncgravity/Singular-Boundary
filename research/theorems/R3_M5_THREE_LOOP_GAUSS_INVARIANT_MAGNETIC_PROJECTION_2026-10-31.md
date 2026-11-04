# R3-IR-571 — Genuine third Wilson loop on M5 prism: eight-state Gauss-invariant exact magnetic projection

Date 2026-10-31. This is a **three-loop exact Haar/plaquette projection**, not yet a computed eight-state mixed-electric Ritz spectrum.

The archived 3D prism M5 incidence matrix has 65 plaquettes, and the two previously retained chord-adjacent loops have incidence indices 4 (horizontal) and 29 (vertical), sharing one edge. A third bottom horizontal loop at incidence index 2 (base face ID 1) is **edge-disjoint** from both. It has an independent Haar holonomy. Therefore the eight product characters Φ_{abc}=χ_{1/2}(U_A)^a χ_{1/2}(U_B)^b χ_{1/2}(U_C)^c, a,b,c∈{0,1}, are Gauss invariant and exactly Haar orthonormal. The argument conditions on edge variables private to the loops; it does not assume interacting-vacuum independence.

The three weak-curvature-matched Wilson coefficients at illustrative g²=1 are b_A=25.71208103423584, b_B=19.38096560369536 and b_C=30.85449724108302. The last is computed for bottom face ID 1 from the same R3-IR-562 geometric coefficient prescription b_C=2 V/(g² A²).

The 8×8 projected nonconstant magnetic matrix has entries

  (H_B)_{abc,a'b'c'}=−(1/2)[b_A 1_{a≠a',b=b',c=c'} + b_B 1_{b≠b',a=a',c=c'} + b_C 1_{c≠c',a=a',b=b'}].

This is an exact tensor sum of three σ_x matrices. Its ordered eigenvalues are [−37.9737719395,−18.5928063358,−12.2616909053,−7.1192746984,7.1192746984,12.2616909053,18.5928063358,37.9737719395]. The identity shifts Σ_f b_f in the full magnetic energy are omitted, as they do not affect spectral differences.

A **complete support-XOR audit** over every other retained plaquette found no plaquette edge support equal to any symmetric difference of the three selected loop supports. By SU2 independent link-center parity, all remaining retained Wilson traces have identically vanishing 8-state projected matrix elements. Thus this is the full *projected magnetic multiplier*, not merely the selected three interactions. One should not infer the same result for the electric operator or for the full nonprojected Hamiltonian.

The full inverse-Whitney electric matrix on the eight states has **not yet been contracted**; the new eight-state Ritz eigenvalues and gaps have therefore NOT been computed or certified. Nor is this 8-state basis an extension of the prior nine-state two-loop basis (it extends the earlier four-state two-loop basis in a different direction). Independent enlargement directions must eventually be merged, with additional intertwiner channels.

Source and exact numerical JSON preserved in ChatGPT Library /The Singular Boundary/Source/ as three_loop_m5_extension.py and m5_three_loop_gauge_extension_2026-10-31.json. No binary data added to Git. No continuum Yang–Mills mass gap is proved.
