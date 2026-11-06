#!/usr/bin/env python3
"""Review graph v2.40: periodic noncommuting SU2 control and finite positive tube.
Genuine quantum continuum P0-P5, Penrose T0-T5 and gravity remain open.
"""
import json
from pathlib import Path

SOURCE='research/theorems/R3_NONCOMMUTING_HOMOGENEOUS_CUBIC_SU2_FLOW_AND_POSITIVE_TUBE_2026-11-06.md'
SHA='827fb2ff04d60ea7ae31c8f8bb9dee3e2b3116d0'
BRANCH='audit/2026-11-06-nonabelian-homogeneous-and-theorem-index'

def attach(root):
 root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text(encoding='utf8'))
 if g['version']=='v2.40-draft':return g
 assert g['version']=='v2.39-draft',g['version']
 n=g['nodes'];e=g['edges'];by={x['id']:x for x in n}
 assert len(n)==136 and len(e)==302
 source={'title':'Exact noncommuting periodic cubic SU2 Wilson flow and finite positive-vacuum tube',
         'path':SOURCE,'git_blob_sha':SHA,
         'url':f'https://github.com/syncgravity/singular-boundary/blob/{SHA}/{SOURCE}'}
 def chk(label,state='open',note=''):return dict(label=label,state=state,note=note)
 def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
  assert id not in by
  z=dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,detail=detail,checks=checks,
         sources=[source],tags=tags,importance=importance,core=False,route=None)
  n.append(z);by[id]=z
 def edge(a,b,kind,label,status='open'):
  assert a in by and b in by
  e.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))
 add('R-NONABELIAN-HOMOGENEOUS',
     'Noncommuting SU(2) homogeneous periodic cubic Wilson flow',
     'result','finite','P2',
     'Full periodic 3D cubic original-link SU2 Wilson force preserves Ux=exp(theta T1), Uy=exp(theta T2), Uz=I, with nonzero xy commutator and exact theta_s=-2sin^3(theta/2)cos(theta/2).',
     'Distinct periodic spatial control rather than the previous open cubic or Cartan planar model; n>=2, 3n^3 original links, 3n^3 faces. Strong symmetry and homogeneity, measure-zero manifold, no typical true-vacuum regularity.',
     [chk('Full SU2 original-link quaternion force and nonzero commutator','met','9 independent periodic geometry/force cases'),
      chk('Exact invariant homogeneous nonabelian ODE','met'),
      chk('Generic noncommuting Wilson configurations','open','Homogeneity is not preserved by arbitrary perturbations')],
     ['cubic','periodic','SU2','nonabelian','classical'],5)
 add('R-NONABELIAN-PHYS-ODE',
     'Positive-physical-time nonabelian homogeneous curvature and O(h²) limit',
     'result','conditional','P2',
     'For 0<theta0<=pi/2, the full periodic homogeneous SU2 commutator plaquette has 2distance(U_p,I)/h²<=2pi/tau. With theta0=h a0, a_h converges at O(h²) to a0/sqrt(1+a0²tau/2).',
     'Classical nonlinear physically scaled flow in a genuinely noncommuting but homogeneous invariant family, not an interacting OS/Schur quantum theorem. The upper bound remains valid for theta0 fixed and diverging bare initial action, only in this sector.',
     [chk('Noncommuting curvature positive physical time bound','met','Exact z=sin²(theta/2) Riccati inequality'),
      chk('Explicit O(h²) classical homogeneous continuum ODE error','met','tau h² a0^5 /16'),
      chk('Arbitrary full 3D noncommuting initial configurations','open','No generic curvature/Nash estimate')],
     ['cubic','periodic','SU2','conditional','physical-flow'],5)
 add('R-NONABELIAN-FINITE-VACUUM-TUBE',
     'Open noncommuting curvature-control tube of positive finite Wilson-vacuum probability',
     'result','finite','P2',
     'Global Wilson Hessian <=4 and product plaquette geometry yield curvature difference <=4 exp(4tau/h²) d2(U,U*)/h². A radius r_h~h² exp(-4tau/h²) full-space tube satisfies the positive-time bound and has nonzero probability under the true finite strictly positive Wilson vacuum.',
     'The finite Haar-ball lower probability is m_h[((u-sin u)/(2pi))^(3n^3)], u=r_h/sqrt(3n^3). The radius, Haar mass and unknown m_h deteriorate rapidly; this is not a uniform true-vacuum or typical-configurations theorem. The gauge-invariant good-curvature event contains the tube.',
     [chk('Finite full-space open noncommuting tube around exact solution','met'),
      chk('Strictly positive true finite Wilson-vacuum probability','met','Compact positive ground-state density and product Haar geometry'),
      chk('Uniform positive probability on weak-coupling refinements','open','Haar tube shrinks exponentially in tau/h² and E grows')],
     ['cubic','SU2','finite-vacuum','noncommuting','open-neighborhood'],4)
 add('W-NONABELIAN-TYPICAL-VACUUM',
     'Non-Abelian physical-flow regularity on uniformly probable Wilson-vacuum sets',
     'work','open','P2',
     'Prove fixed-positive-physical-flow-time covariant curvature estimates for full 3D SU2 configurations on sets of uniformly positive probability under actual weak-coupling Wilson ground states, then compare full quantum-time Schur/connected correlations.',
     'The exact homogeneous nonabelian ODE and exponentially shrinking finite open tube lack any h/volume-uniform probability bound. Need multi-scale noncommutative parabolic control and state-dependent estimates; 4D OS and gap remain independent.',
     [chk('Noncommutative covariant-curvature smoothing on generic field sets'),
      chk('Refinement/volume-uniform true-Wilson-vacuum probability and nonzero renormalized covariance'),
      chk('Full interacting Schur / positive quantum-time decay uniform in h,R'),
      chk('Nontrivial 4D OS reconstruction and positive gauge-invariant gap')],
     ['cubic','SU2','nonabelian','vacuum','open'],5)
 edge('M-CUBIC','R-NONABELIAN-HOMOGENEOUS','distinct-boundary-control','Periodic cubic control, not open cubical physical regulator','finite')
 edge('R-NONABELIAN-HOMOGENEOUS','R-NONABELIAN-PHYS-ODE','exact-nonlinear-ODE','True noncommuting plaquette homogeneous physical-time regularization','conditional')
 edge('R-NONABELIAN-PHYS-ODE','R-NONABELIAN-FINITE-VACUUM-TUBE','stable-open-neighborhood','Finite Hessian Lipschitz control creates an open full-link tube','finite')
 edge('R-CUBIC-SPATIAL-WILSON-FLOW','R-NONABELIAN-FINITE-VACUUM-TUBE','flow-stability','Volume-independent Hessian bound but exponential physical-time loss','finite')
 edge('R-NONABELIAN-FINITE-VACUUM-TUBE','W-NONABELIAN-TYPICAL-VACUUM','nonuniform-probability','Strictly positive at each finite h, no uniform h,R mass','open')
 edge('R-PLANAR-CARTAN-EMBED','R-NONABELIAN-HOMOGENEOUS','distinct-invariant-sectors','Cartan open planar vs noncommuting periodic homogeneous','finite')
 edge('R-NONABELIAN-PHYS-ODE','W-FULL-NONABELIAN-PHYS-SMOOTHING','partial-nonabelian-control','Homogeneous noncommuting ODE does not prove generic 3D regularity','open')
 edge('W-NONABELIAN-TYPICAL-VACUUM','W-FULL-NONABELIAN-PHYS-SMOOTHING','refines-open-task','Needs full covariant parabolic and genuine vacuum estimates','open')
 edge('W-NONABELIAN-TYPICAL-VACUUM','W-PHYSICAL-FLOWED-SCHUR','open-quantum-time','Classical positive-time flow not quantum transfer/Schur','open')
 edge('W-NONABELIAN-TYPICAL-VACUUM','T2-OBSERVABLES','open-quantum-field','Nontrivial 4D flowed observable covariance unresolved','open')
 edge('W-NONABELIAN-TYPICAL-VACUUM','T3-TIME-COMPARE','open-IR-comparison','Positive quantum-time interacting spectral exclusion unresolved','open')
 edge('R-NONABELIAN-HOMOGENEOUS','T0-QC-3D','distinct-geometry','Periodic cubic noncommuting flow does not build genuine 3D Penrose','open')
 edge('R-NONABELIAN-PHYS-ODE','P2','scoped-finite-evidence','Positive classical time in homogeneous sector only','finite')
 edge('W-NONABELIAN-TYPICAL-VACUUM','G-GRAV','independent-UV-question','YM smoothing is not gravitational UV completion','open')
 g.update(version='v2.40-draft',git_branch=BRANCH,build_date='2026-11-06',
  scope='Exact periodic noncommuting cubic SU2 homogeneous classical flow, positive physical-time curvature in invariant sector, finite open tube positive Wilson-vacuum measure only. Complete theorem-file discovery catalogue and CI coverage; all continuum gates remain open.')
 assert len(n)==140 and len(e)==316,(len(n),len(e))
 assert len(set(x['id'] for x in n))==140
 assert len([x for x in n if x['kind']=='dataset'])==26
 assert all(x['status']=='open' for x in n if x['kind'] in ('goal','gate'))
 p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
 (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
 return g

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
 g=attach(ap.parse_args().root)
 print('PASS',g['version'],len(g['nodes']),len(g['edges']),'all theorem gates OPEN')
