# Connected physical original-link SU(2) fusion: exact two- and three-face certificates (2026-11-03)

**Scope:** Corrected physical original-link free-electric generator, gauge-invariant Wilson observables, and explicitly connected original-link supports. This establishes exact local Poisson coefficients and a support preservation theorem, **not** an all-width anchored nonlinear algebra.

**SUPPORT LOCALITY LEMMA.** For any original-link subset S, the positive free-electric operator K=−Σ_(e,a)∇_(e,a)^2 preserves the subspace of gauge-invariant cylinder functions depending only on S. Its centered inverse K^−1Q also preserves this subspace by the unique centered inverse. Γ_K(f,g)=Σ_(e∈S_f∩S_g,a)(∇_ef)(∇_eg), hence Γ=0 for disjoint original-link supports; otherwise B(f,g)=K^−1QΓ depends only on S_f∪S_g. This is local in **original original-link variables**, not necessarily in maximal-tree based-loop coordinates. On the physical ladder the centered L2 inverse is uniformly ≤1/3, but no corresponding uniform spin-network coefficient-l1 bilinear estimate is inferred.

**TWO ADJACENT FACES.** Set x=χ_1(A)=tr A, y=χ_1(B)=tr B and z=χ_1(AB)=tr AB. Original-link SU(2) Haar integration gives ||xy||²=||z||²=1, <xy,z>=1/2. The corrected physical K obeys K(xy)=13xy/2−z and Kz=9z/2. Thus the orthonormal energy spin-network channels are Ψ_(9/2)=z and Ψ_(13/2)=(2/√3)(xy−z/2), with the connected product fusion **xy=(1/2)Ψ_(9/2)+(√3/2)Ψ_(13/2)**. Its coefficient-l1 multiplication factor is (1+√3)/2. The exact source and response are

**Γ_K(x,y)=z/2−xy/4=(3/8)Ψ_(9/2)−(√3/8)Ψ_(13/2)**,

**B(x,y)=K^−1QΓ=(1/12)Ψ_(9/2)−(√3/52)Ψ_(13/2)=−xy/26+4z/39**.

Hence ||B(x,y)||_(SN,l1)=1/12+√3/52, and **||B(x,y)||²_(L2)=49/6084**. The entire output depends on the seven physical original links of the adjacent two-square union.

**THREE ADJACENT FACES.** Let f=χ_1(A)χ_1(B), g=χ_1(C), and the invariant trace basis p=trA trB trC; u12=tr(AB)trC; u23=tr(BC)trA; u13=tr(AC)trB; w=tr(ABC). Because f and g share the original edge between faces 2 and 3, the original-link carré du champ is **Γ_K(f,g)=−p/4+u23/2**. The corrected ten-link physical K on this five-dimensional Gauss-invariant fundamental block, independently verified in the prior exact 64-dimensional original-link construction, is

    [[10,0,0,-2,0],
     [-1,8,0,1,0],
     [-1,0,8,1,0],
     [0,0,0,13,0],
     [0,-1,-1,-4,6]]

with spectrum {6,8,8,10,13}. **Exact physical centered inverse:**

**B(f,g)=−p/40−u12/320+19u23/320+3w/320.**

The physical Haar Gram matrix gives ||Γ||²_(L2)=3/16 and **||B||²_(L2)=647/204800**. The source's squared norm by electric energy shells E=6,8,10,13 is exactly **9/256,15/128,9/256,0**. Consequently, for any orthonormal physical energy eigenbasis, the resulting spin-network coefficient-l1 norm lies between **1/32+√30/128+3/160** and **1/32+√15/64+3/160**. The energy-8 eigenspace is two-dimensional, so a single basis-independent exact coefficient-l1 value would be unjustified.

**Distinct conceptual results:** The original-link Γ and its free inverse preserve connected union support; adjacent Wilson loops have nontrivial recoupling multiplicity; inversion mixes energy channels within the finite connected three-face region. The previous exponential disconnected-loop counterexample does not disprove connected support-weighted closure. The new local certificates do not **prove** such closure either. The next obligation is a fixed-basis, degree-graded connected original-edge fusion majorant with incidence counts and a provable support-weight budget.

A complete detailed proof report, independent exact verifier (342 checks; re-executes prior full ten-link SymPy matrix), passing log and SHA-256 manifest are in The Singular Boundary / Proof Audits Library. Neither an interacting λ=1 gap nor a continuum Yang–Mills mass gap is established.