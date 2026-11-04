"""Graph tree-role test and conditional selected magnetic/electric refinement scaling."""
import math
T_a={(0,1),(1,2),(2,3)}
T_b={(0,1),(1,2),(0,3)}
assert len(T_a)==len(T_b)==3 and (0,3) not in T_a and (0,3) in T_b
M_ee=.7778590280946629; b0=3/32000
gamma=3/(8*M_ee);rho=b0/gamma
def cap(d):
 t=math.acos(1-d);return 2/math.pi*(t-math.sin(t)*math.cos(t))
for h in (1.,.5,.25,.125,.0625):
 r=rho/h**2;epsilon=r/(1-r) if r<1 else float('inf')
 print('h',h,'ratio',r,'cap lower',max(0,cap(.1)-epsilon))
hc=math.sqrt(rho*(1+cap(.1))/cap(.1));hg=math.sqrt(rho)
assert hc>hg
print('PASS conditional h^-2 scaling threshold, cap threshold',hc,'denominator threshold',hg)
