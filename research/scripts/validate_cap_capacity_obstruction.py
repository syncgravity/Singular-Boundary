"""Radial SU2 test: vanishing electric energy yet zero double-center mass."""
import math
from scipy.integrate import quad

def evaluate(r):
    def h(t):
        d=min(t,math.pi-t)
        return 0. if d<=r else (d-r)/r if d<2*r else 1.
    knots=[r,2*r,math.pi-2*r,math.pi-r]
    z=quad(lambda t:2/math.pi*math.sin(t)**2*h(t)**2,
           0,math.pi,points=knots)[0]
    E=(r/2-(math.sin(4*r)-math.sin(2*r))/4)/(math.pi*r*r*z)
    haar=2/math.pi*(r-math.sin(r)*math.cos(r))
    return z,E,haar

for r in (.25,.125,.0625,.03125,.015625):
    z,E,haar=evaluate(r)
    assert z>.9 and E<r and haar>0
    print('r=',r,'delta=',1-math.cos(r),'energy=',E,'haar cap=',haar,'test cap=',0)
print('PASS cap mass zero while electric energy tends to zero')
