from fractions import Fraction as F
# Algebraic counterexample: squarefree product minus b1^2 b2 b4 b10 b3^5.
C={1,2,3,4,7,8,10,11,150,154}
mon1={g:1 for g in C}
mon2={1:2,2:1,4:1,10:1,3:5}
assert sum(mon1.values())==sum(mon2.values())==10
assert all(mon1.get(g,0)>=1 and mon2.get(g,0)>=1 for g in (1,2,4,10))
assert mon1!=mon2 and all(mon1.get(g,0)==1 for g in C)
assert sum((1,-1))==0  # Both monomials equal t^10 on the diagonal.
q=F(1,100)
upper=2*q**4/(1-q)**10
assert upper==F(2000000000000,90438207500880449001)
print('PASS exact analytic counterexample and diagonal upper bound',float(upper))
