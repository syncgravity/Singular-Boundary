from fractions import Fraction as Q
# Compare scaling exponents without choosing trace normalization.
for d in (2,3):
 electric=2-d
 magnetic=d-4
 ratio=magnetic-electric
 assert ratio==2*d-6
assert 2*2-6==-2 and 2*3-6==0
print('PASS dimensional scaling exponents d=2: h^-2; d=3: h^0 at fixed bare coupling')
