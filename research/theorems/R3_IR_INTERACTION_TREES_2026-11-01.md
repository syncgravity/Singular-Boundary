# Formal interaction-tree expansion — 2026-11-01

Under the corrected score recurrence with R=K^{-1}(1-P_0), X=-RV, B(f,g)=R Γ(f,g), the formal score S=λX+B(S,S) has exact coefficients

S_n=Σ_{τ∈T_n}F_τ, F_leaf=X, F_(L,R)=B(F_L,F_R),

where T_n consists of ordered full binary trees with n leaves and |T_n|=C_(n−1)=binom(2n−2,n−1)/n. Induction is by root split into j and n−j leaves, reproducing every ordered term in the recurrence. First coefficients are X, B(X,X), and B(X,B(X,X))+B(B(X,X),X). Symmetry of Γ may identify evaluations but not their multiplicities.

Each internal Γ vertex vanishes unless its two inputs have a common original-link derivative. In the fixed-coefficient invariant-derivative model, the centered reduced inverse commutes with all individual Haar averages, so it does not enlarge face support. Subject to single-face leaf decomposition and nearest-neighbor link incidence, nonzero contraction trees are recursively interaction-connected. This is not a canonical probabilistic cumulant statement; and it requires a separate physical gauge-fixing audit.

Catalan counts for n=1..9 were exhaustively checked by executable enumeration: 1,1,2,5,14,42,132,429,1430. The complete report, source checker, log, and checksums are in Library Proof Audits as R3_IR_INTERACTION_TREES_2026-11-01.zip.

**Research verdict:** The corrected-sign formal score admits an exact ordered binary interaction-tree expansion, with Catalan multiplicities and a necessary original-link selection rule at each internal vertex. Under the constant-coefficient invariant-derivative and nearest-neighbor hypotheses, nonzero trees assembled from single-face leaves form recursively connected contraction constructions. No chain-uniform weighted-tree majorant or analytic convergence is proved; the physical gauge-fixed operator audit, interacting λ=1 gap, Penrose signed-current estimate and continuum Yang–Mills mass gap remain open.