import numpy as np

def haar_su2(rng):
    w,x,y,z=rng.normal(size=4)
    q=np.array([w,x,y,z])/np.linalg.norm([w,x,y,z])
    w,x,y,z=q
    return np.array([[w+1j*z, y+1j*x],[-y+1j*x,w-1j*z]])
