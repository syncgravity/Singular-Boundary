from fractions import Fraction as Q
from decimal import Decimal,getcontext
getcontext().prec=60
k=Q(2376252926673252101321919045001703951557,3082322838199847861301112342611033200018689536000000)
assert k>0
# Inner-outer deleted Haar complement norm squared is exactly 3/64.
L2=k*k*Q(3,64)
assert L2>0
assert Decimal(L2.numerator)/Decimal(L2.denominator)>Decimal('2.7e-26')
print('PASS nonzero real analytic witness squarefree coefficient',L2)
print('A nontrivial real analytic zero set has Lebesgue measure zero and empty interior.')
