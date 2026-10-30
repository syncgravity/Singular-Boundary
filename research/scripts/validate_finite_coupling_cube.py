from fractions import Fraction as F
from decimal import Decimal,getcontext
getcontext().prec=65
k=F(2376252926673252101321919045001703951557,3082322838199847861301112342611033200018689536000000)
L=Decimal(k.numerator)*Decimal(3).sqrt()/(Decimal(k.denominator)*8)
q=F(1,10**16);r=F(3,320);t=r*q
error=2*((1-q)**(-10)-1)
assert error<F(22)*q
assert L>Decimal(22)*Decimal(q.numerator)/Decimal(q.denominator)
lower=(L-Decimal(22)/Decimal(10**16))/Decimal(1024*10**160)
assert lower>Decimal('1.6085e-176')
print('PASS r=',r,' t=',t,' L=',L,' corner bound=',lower)
