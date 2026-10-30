import math,json
from scipy.integrate import quad
L=4
checks=[]
for lam in [1,2,5,10,100,1000]:
    eps=1/(L*math.sqrt(lam))
    actual=(2/math.pi)*quad(lambda t: math.sin(t)**2,0,eps,epsabs=1e-15)[0]
    bound=8/(3*math.pi**3)*eps**3
    assert actual>=bound
    checks.append({'lambda':lam,'haar_ball_exact':actual,'haar_ball_lower':bound,'bound_valid':True})
with open('/mnt/data/r3_gibbs_smallball_audit_2026-10-28/checks.json','w') as f:json.dump({'description':'Numerical check of ball-volume inequality only; not a verification of Penrose R3','checks':checks},f,indent=2)
print('Verified',len(checks),'Haar-volume inequalities')
