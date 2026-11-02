# R3-IR — Connected-polymer repetition barrier (2026-11-01)

**Proved only for the defined positive scalar interval envelope, not for the actual SU(2) coefficients.**

A straight strip face interval I=[a,b] has original-link set E(I), with two horizontal edges per face and a vertical edge on each boundary. Define c_1(I)=1 for singleton I, zero otherwise, and for n>=2
c_n(I)=sum_{i=1}^{n-1} sum_{J,H intervals: J∪H=I} |E(J)∩E(H)| c_i(J)c_{n-i}(H).
This includes repeated plaquette insertion, adjacent interactions and ordered binary trees, but is only an unrenormalized *positive envelope*.

For a length-ℓ interval I, the ordered pairs (I,{x}) and ({x},I) with x any of the ℓ faces contribute four shared links apiece. Hence c_{ℓ+m}(ℓ)≥(8ℓ)^m c_ℓ(ℓ), with c_ℓ(ℓ)≥1 from successive adjacent attachments. Taking m=ℓ yields c_{2ℓ}(ℓ)≥(8ℓ)^ℓ. Thus the sum of these positive envelopes has zero formal power-series radius by the root test. This does NOT prove divergence of the physical SU(2) score or disprove a rearranged/cumulant expansion; positive majorants can overcount massive cancellations.

An exact-integer verifier evaluated intervals through order 12 and checked the original-link overlap, singleton Catalan identity c_n(1)=4^(n−1)Cat(n−1), and insertion inequalities. Complete report, verifier, numerical table, log, and SHA256 manifest are in Library /The Singular Boundary/Proof Audits.

**Next obligation:** obtain connected-cumulant/linked-cluster subtraction with correct vacuum-energy normalization, and test whether repeated single-face insertions resum to dressed local activities; audit earlier three-face sign convention and matrix Peter–Weyl proof as separate dependencies. Interacting λ=1 and continuum mass gaps remain open.