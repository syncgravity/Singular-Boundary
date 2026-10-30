import unittest,sys
from pathlib import Path
import numpy as np
from scipy.special import ive
from scipy.stats import vonmises_fisher
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage16_multihit import (_field, exact_su2_mean,exact_su2_heatbath,catalog_square,
  multihit_batched,action_delta_field,heatbath_source_line)
from stage13_transport import identity_field,small_square
from stage3_periodic_pilot import square_torus
from stage2_ym_calibration import assemble
from wilson_torus import face_trace_scalar

class TestStage16(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sp,cls.lat=small_square(nt=15,nx=8,ny=8)
  cls.links=np.random.default_rng(1337).normal(size=(cls.lat['L'],4))
  cls.links/=np.linalg.norm(cls.links,axis=1,keepdims=True)
  cls.paths=catalog_square(cls.sp,nanchors=16)
 def test_action_local_field_exact(self):
  for site in (0,3,10):
   eid=self.lat['nt']*self.sp['E']+site
   h=_field(self.links,self.lat['fi'],self.lat['sg'],self.lat['beta'],self.lat['adj'],self.lat['degree'],eid)
   q=np.random.default_rng(site+73).normal(size=4);q/=np.linalg.norm(q)
   d=action_delta_field(self.links,self.lat,eid,q)
   ref=np.dot(q-self.links[eid],h)
   self.assertAlmostEqual(d,ref,places=11)
 def test_su2_exact_moment_normalized(self):
  for k in (0,1e-6,0.1,2.,5.,20.,120.):
   h=np.array([k,0,0,0.])
   m=exact_su2_mean(h)
   ref=0. if k==0 else ive(2,k)/ive(1,k)
   self.assertAlmostEqual(m[0],ref,places=8)
   self.assertLessEqual(np.linalg.norm(m),1.+1e-13)
 def test_haar_conditional_heatbath(self):
  h=np.array([2.,0,0,0]);rng=np.random.default_rng(31)
  q=np.array([exact_su2_heatbath(h,rng) for _ in range(3000)])
  self.assertTrue(np.allclose(np.linalg.norm(q,axis=1),1.,atol=1e-12))
  self.assertLess(abs(q[:,0].mean()-exact_su2_mean(h)[0]),.045)
 def test_paths_are_contiguous_and_physical(self):
  for k in range(len(self.paths['u'])):
   cur=self.paths['u'][k];disp=np.zeros(2)
   for j in range(self.paths['length'][k]):
    e=self.paths['idx'][k,j];s=self.paths['sign'][k,j];a,b=self.sp['edges'][e]
    self.assertEqual(cur,a if s==1 else b)
    cur=b if s==1 else a
    disp+=s*self.sp['edge_vectors'][e]
   self.assertEqual(cur,self.paths['v'][k])
   self.assertTrue(np.allclose(disp,self.paths['dx'][k]))
  self.assertGreaterEqual(len(self.paths['u']),100)
 def test_direct_quaternion_matches_matrix(self):
  d,m=multihit_batched(self.links,self.lat,self.sp,self.paths)
  for k in (0,23,64,127):
   # Independent 2x2 faithful homomorphic representation, unlike legacy
   # stage13.mat() which is anti-homomorphic with respect to wilson_torus.mul.
   def Q(q):
    a,b,c,z=q
    return np.array([[a-1j*z,-c-1j*b],[c-1j*b,a+1j*z]])
   ident=np.eye(2,dtype=complex);S0=ident.copy();S1=ident.copy()
   for j in range(self.paths['length'][k]):
    e=self.paths['idx'][k,j];s=self.paths['sign'][k,j]
    x=Q(self.links[e]);y=Q(self.links[10*self.sp['E']+e]);S0=S0@(x if s==1 else x.conj().T);S1=S1@(y if s==1 else y.conj().T)
   A=ident.copy();B=ident.copy()
   for t in range(10):
    A=A@Q(self.links[15*self.sp['E']+t*self.sp['V']+self.paths['u'][k]])
    B=B@Q(self.links[15*self.sp['E']+t*self.sp['V']+self.paths['v'][k]])
   val=(np.trace(S0@B@S1.conj().T@A.conj().T).real)/2
   self.assertAlmostEqual(d[k],val,places=11)
  self.assertTrue(np.all(np.isfinite(m)))
 def test_flat_field_multihit(self):
  U=identity_field(self.lat)
  d,m=multihit_batched(U,self.lat,self.sp,self.paths)
  self.assertTrue(np.allclose(d,1.,atol=1e-14))
  self.assertTrue(np.all(m>=0))
  self.assertTrue(np.all(m<=1.))
 def test_original_stage9_wilson_kernel_agrees(self):
  from corrected_2p1_pilot import rect_path
  d,_=multihit_batched(self.links,self.lat,self.sp,self.paths,lag=4)
  for i in (0,5,42,127):
   p=self.paths
   x=rect_path(self.links,self.lat['nt'],self.sp['E'],self.sp['V'],p['idx'][i],p['sign'][i],p['length'][i],p['u'][i],p['v'][i],0,4)
   self.assertAlmostEqual(x,d[i],places=12)
 def test_heatbath_line_exact_support_and_action(self):
  x=heatbath_source_line(self.links,self.lat,self.sp,0,seed=88)
  ids=np.array([self.lat['nt']*self.sp['E']+t*self.sp['V'] for t in range(10)])
  mask=np.ones(self.lat['L'],bool);mask[ids]=False
  self.assertTrue(np.array_equal(x[mask],self.links[mask]))
  self.assertTrue(np.allclose(np.linalg.norm(x[ids],axis=1),1.,atol=1e-14))
  # No elementary temporal plaquette contains two members of this source line.
  for face in self.lat['fi']:
   self.assertLessEqual(sum(e in set(ids.tolist()) for e in face),1)
 def test_gauge_invariance_of_multihit(self):
  from wilson_torus import mul
  sp,lat=self.sp,self.lat;E,V,nt=sp['E'],sp['V'],lat['nt']
  rng=np.random.default_rng(91)
  g=rng.normal(size=(nt,V,4));g/=np.linalg.norm(g,axis=2,keepdims=True)
  altered=self.links.copy()
  for t in range(nt):
   for e,(a,b) in enumerate(sp['edges']):
    qb=g[t,b].copy();qb[1:]*=-1
    altered[t*E+e]=mul(mul(g[t,a],self.links[t*E+e]),qb)
   for v in range(V):
    qb=g[(t+1)%nt,v].copy();qb[1:]*=-1
    altered[nt*E+t*V+v]=mul(mul(g[t,v],self.links[nt*E+t*V+v]),qb)
  p={k:v[:4] for k,v in self.paths.items()}
  D,M=multihit_batched(self.links,lat,sp,p,lag=4)
  Dt,Mt=multihit_batched(altered,lat,sp,p,lag=4)
  self.assertTrue(np.allclose(D,Dt,atol=2e-12))
  self.assertTrue(np.allclose(M,Mt,atol=2e-12))
 def test_legacy_mapping_reverses_product(self):
  # Records the discovered Stage13 representation inconsistency explicitly.
  from stage13_transport import mat
  from wilson_torus import mul
  q=np.array([.5,.5,.5,.5]);r=np.array([.5,.5,-.5,-.5])
  self.assertTrue(np.allclose(mat(q)@mat(r),mat(mul(r,q))))
  self.assertFalse(np.allclose(mat(q)@mat(r),mat(mul(q,r))))
 def test_multihit_equals_weighted_haar_integration(self):
  # Independent importance integration of a selected link at modest h
  h=np.array([1.1,-.4,.5,.3]);rng=np.random.default_rng(234)
  q=rng.normal(size=(180000,4));q/=np.linalg.norm(q,axis=1,keepdims=True)
  w=np.exp(q@h-np.max(q@h));mc=(w[:,None]*q).sum(axis=0)/w.sum()
  self.assertTrue(np.allclose(mc,exact_su2_mean(h),atol=.008))

if __name__=='__main__': unittest.main()
