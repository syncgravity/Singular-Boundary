/* The Singular Boundary — local-only, source-linked Research Observatory Proof Atlas.
   This interface cannot certify a theorem. All review annotations are private browser state.
   Static build; no network calls, tracking, or external libraries. */
(()=>{'use strict';
const G=window.SB_KNOWLEDGE_GRAPH;
if(!G||G.schema!=='singular-boundary.knowledge-graph.v1'){document.body.textContent='Graph data missing or invalid. Keep knowledge-graph-data.js alongside graph.html.';return;}
const $=id=>document.getElementById(id), NS='http://www.w3.org/2000/svg';
const nodeById=new Map(G.nodes.map(n=>[n.id,n]));const neighbors=new Map(G.nodes.map(n=>[n.id,new Set()]));
for(const e of G.edges){neighbors.get(e.from_id).add(e.to_id);neighbors.get(e.to_id).add(e.from_id)}
const tone={open:'OPEN',finite:'FINITE MODEL',conditional:'CONDITIONAL',obstruction:'OBSTRUCTION',partial:'PARTIAL',candidate:'CANDIDATE',archived:'ARCHIVED',indexed:'INDEXED ONLY',unresolved:'UNRESOLVED'};
const watchStatuses=new Set(['open','obstruction','partial','candidate','unresolved','conditional']);
const notesKey='singular-boundary.atlas.notes.v1';let annotations={};try{const x=JSON.parse(localStorage.getItem(notesKey)||'{}');if(x&&typeof x==='object'&&!Array.isArray(x))annotations=x}catch(_){annotations={}}
let view='pf',filter='all',query='',selected='I-UV-COUPLING',highlightedPath=[],positions=new Map(),viewNodes=[],viewEdges=[],svgWidth=900,svgHeight=680;
let camera={x:0,y:0,k:1};let pointer=null;let scheduled=false;let noteTimer=null;
const graph=$('graphCanvas'),cam=$('camera'),edgeLayer=$('edgeLayer'),nodeLayer=$('nodeLayer');
function svg(tag,attrs={},text){const el=document.createElementNS(NS,tag);for(const [a,v] of Object.entries(attrs))el.setAttribute(a,String(v));if(text!==undefined)el.textContent=text;return el}
const cls=n=>n.kind==='gate'?'GATE':n.kind==='goal'?'TARGET':n.kind==='data_family'?'ARCHIVE FAMILY':n.kind==='dataset'?'DATA OBJECT':n.kind==='result'?'RESEARCH RESULT':n.kind==='work'?'OPEN WORK':n.kind==='interface'?'INTERFACE':n.kind==='manifest'?'SOURCE MANIFEST':n.kind==='model'?'MODEL':'PUBLICATION';
function labelLines(s,length=26){const words=s.replace(/·/g,' · ').split(/\s+/),lines=[];let cur='';for(const w of words){if((cur+' '+w).trim().length>length&&cur){lines.push(cur);cur=w}else cur=(cur+' '+w).trim();if(lines.length>=2)break}if(lines.length<2&&cur)lines.push(cur);if(lines.length>2)lines.length=2;if(lines.join(' ').length<s.length-3)lines[1]=(lines[1]||'').slice(0,length-2)+'…';return lines}
const gateXY={P0:[320,585],P1:[670,345],P2:[1010,345],P3:[1010,825],P4:[1390,585],P5:[1740,585],THEOREM:[2070,585]};
const special={
'M-CUBIC':[55,145],'M-Z5':[55,345],'M-PRISM':[55,890],'M-STRIP':[580,1135],
'R-CUBE':[380,90],'R-CUBE-H':[735,80],'R-TRANSFER':[1755,80],
'R-CURL':[360,260],'R-PRISM':[330,1030],'R-STRIP-THERMO':[1030,70],
'R-MPO':[1200,150],'R-DIRICHLET':[1470,270],'R-OBSTRUCT':[860,1050],
'R-WEAK':[1570,965],'R-NONINTERTWINE':[430,760],'R-FSUM':[1280,1010],
'R-OSBRIDGE':[1890,940],'R-INDEX':[350,1305],
'W-SOURCE':[95,635],'W-SCALING':[225,830],'W-EMBED':[430,940],
'W-Z5':[70,1240],'W-OPERATOR':[680,610],'W-SCHATTEN':[1030,590],
'W-3D-ANALYTIC':[1130,795],'W-BOREL':[1300,1130],
'W-PENROSE-CURRENT':[950,1260],'W-IR':[1440,750],
'W-DYNAMICS':[1600,1090],'W-OS':[1830,775],
'W-REVIEW':[1990,1160],'W-LFS':[240,1440],
'D-ARCHIVE':[80,1480],'D-SWEEPS':[350,1590],'D-SPECTRAL-SOURCES':[610,1540],
'D-FULL':[610,1670],'D-WHITNEY':[80,1650],'D-CONVO':[890,1660],
'D-MANIFEST':[1150,1670],'PUB-THEOREM-REVIEW':[2060,1320],
'G-GRAV':[2160,100],'M-PENROSE-2D':[120,420],'M-SQUARE-2D':[120,790],
'I-PENROSE-SQUARE':[710,575],'W-ORIGINAL-SOURCES':[780,1140],'W-GRAV-OP':[1710,160],
'S-SPECTRAL-DIMENSION':[390,50],'S-CUT-PROJECT-ZETA':[580,50],'S-COMPLEX-STRUCTURE':[780,50],'S-CONFORMAL-SPECTRAL':[980,50]
};
function basicPosition(n){if(gateXY[n.id])return gateXY[n.id];if(special[n.id])return special[n.id];if(n.kind==='interface'){let i=G.nodes.filter(x=>x.kind==='interface').findIndex(x=>x.id===n.id);return [950+i*200,1650]};if(n.kind==='dataset'){const i=G.nodes.filter(x=>x.kind==='dataset').findIndex(x=>x.id===n.id);return [120+(i%7)*235,1850+Math.floor(i/7)*130]};return [1350,1350]}
function dataPositions(){const p=new Map(); const places={'D-ARCHIVE':[155,115],'D-SWEEPS':[155,515],'D-FULL':[155,930],'D-WHITNEY':[650,930],'D-SPECTRAL-SOURCES':[1150,930],'D-CONVO':[155,1235],'D-MANIFEST':[1370,160]};for(const [id,xy] of Object.entries(places))p.set(id,xy);p.set('P0',[1750,160]);p.set('M-Z5',[1500,430]);p.set('M-PRISM',[1600,760]);p.set('PUB-DISS',[1400,1210]);
let j={};for(const n of G.nodes.filter(x=>x.kind==='dataset')){const group=n.tags[0];j[group]=(j[group]||0);let i=j[group]++;let x,y;if(group==='stage26'){x=110+(i%4)*270;y=265+Math.floor(i/4)*112}else if(group==='sweep10000'){x=110+(i%4)*270;y=670+Math.floor(i/4)*112}else if(group==='full_archive'){x=1100;y=1060}else if(group==='whitney'){x=620;y=1060}else if(group==='dissertation'){x=1370;y=1060}else{x=110+(i%4)*270;y=1370+Math.floor(i/4)*110}p.set(n.id,[x,y])}
return p}
const pfXY={
'M-Z5':[100,130],'PF-G0':[370,130],'PF-G1':[640,130],'PF-G2':[910,130],
'PF-G3':[1180,130],'PF-G4':[1450,130],'PF-G5':[1720,130],
'M-PENROSE-2D':[90,430],'PF-LORENTZ-OPEN':[640,430],
'PF-SCALAR-NOGO':[1180,430],'PF-GRAV-SEPARATE':[1730,430],
'M-CUBIC':[100,730],'I-PENROSE-SQUARE':[640,730],
'P0':[375,990],'P1':[645,990],'P2':[920,990],
'P3':[1200,990],'P4':[1470,990],'P5':[1740,990],
'G-GRAV':[1730,700],'THEOREM':[2050,990],
'T0-QC-3D':[490,1270],'T1-QC-ACTION':[780,1270],
'T2-OBSERVABLES':[1070,1270],'T3-TIME-COMPARE':[1360,1270],
'T4-OS-LIMIT':[1650,1270],'T5-GAP-TRANSFER':[1950,1270]
};
const compareXY={
'G-GRAV':[1250,180],'THEOREM':[1250,580],
'M-PENROSE-2D':[130,175],'M-SQUARE-2D':[130,595],
'M-Z5':[570,90],'M-CUBIC':[570,675],
'I-PENROSE-SQUARE':[525,380],'P0':[955,380],
'W-ORIGINAL-SOURCES':[940,700],'W-GRAV-OP':[965,85],
'D-ARCHIVE':[130,1120],'D-SWEEPS':[480,1120],'D-SPECTRAL-SOURCES':[650,25],
'S-SPECTRAL-DIMENSION':[280,30],'S-CUT-PROJECT-ZETA':[460,30],'S-COMPLEX-STRUCTURE':[650,90],'S-CONFORMAL-SPECTRAL':[840,170],
'W-Z5':[1150,720],'R-CUBE':[620,920],'R-P0-HK':[1230,1000]};
const bridgeXY={
'M-PENROSE-2D':[50,120],'M-Z5':[340,120],'I-QG-SPECTRAL-OP':[1280,120],'G-GRAV':[1610,120],
'T0-QC-3D':[240,400],'T1-QC-ACTION':[535,400],'T2-OBSERVABLES':[840,400],
'T3-TIME-COMPARE':[1140,400],'T4-OS-LIMIT':[1445,400],'T5-GAP-TRANSFER':[1750,400],
'M-CUBIC':[60,740],'R-CUBE':[345,740],'R-CUBE-H':[640,740],'R-P0-HK':[930,740],
'R-CUBIC-FINITE-GAP':[1220,740],'I-UV-COUPLING':[1520,740],'THEOREM':[1840,740],
'R-WEAK':[1280,970],'R-LOW-ENERGY-COUNTER':[1610,970],
'R-CUBIC-3D-SHELL':[970,1180],'W-3D-WILSON-TIME':[1320,1210],
'R-WILSON-EXP-SHELL':[1060,1370],'R-TEMPORAL-MEMORY':[1440,1370],
'R-TWO-TIME-INFLUENCE':[1120,1530],'R-DYADIC-BARE-MEMORY':[1470,1530],'W-RENORMALIZED-INFLUENCE':[1800,1510],
'R-VACUUM-WEIGHTED-BLOCK':[1030,1730],'R-SU2-STATIC-TIME-COUNTER':[1390,1740],'W-STATE-SCHUR-UNIFORM':[1760,1740],
'R-WILSON-MARGINAL-HARNACK':[740,1940],'R-WILSON-FIXED-LOOP-MOMENT':[1090,1940],'I-WILSON-STATIC-TIME-NORM':[1450,1940],'W-LOCAL-MARGINAL-UV':[1800,1940],
'R-LOCAL-LINK-ENERGY':[720,2130],'R-LOCAL-WILSON-FISHER':[1060,2130],'R-WILSON-THERMO-SUBSEQ':[1400,2130],'W-UV-UNIFORM-LOCAL-WILSON':[1780,2130],
'R-SU2-FISHER-GAP-COUNTER':[750,2320],'R-GROUP-HEAT-WILSON-NOGO':[1080,2320],'R-CUBIC-SPATIAL-WILSON-FLOW':[1420,2320],'I-FLOWED-WILSON-DIRICHLET':[1710,2320],'W-PHYSICAL-FLOWED-SCHUR':[2050,2350],
'R-LINEAR-CUBIC-PHYSFLOW':[780,2540],'R-PERIODIC-FLOW-FOURIER':[1140,2540],'R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE':[1500,2540],'W-NONLINEAR-PHYS-RADIUS':[1900,2540],
'R-NONLINEAR-PHYS-ACTION':[790,2760],'R-PLAQUETTE-HOLONOMY-ADMISSIBILITY':[1180,2770],'R-CUBIC-CURVATURE-ATOMIC':[1570,2790],'R-FINITE-FLOWED-VACUUM':[2000,2760],
'R-PLANAR-CARTAN-EMBED':[760,2990],'R-CARTAN-POSITIVE-FLOW-SMOOTH':[1160,3000],'R-CARTAN-ALLTIME-L2':[1560,3000],'W-FULL-NONABELIAN-PHYS-SMOOTHING':[2010,3000],
'R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE':[790,3210],'R-FULL-NONABELIAN-MAX-COUNTER':[1240,3210],'W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT':[1930,3210],
'P0':[480,1040],'P2':[800,1040],'P4':[1100,1040],'P5':[1850,1020]
};
function positionFor(n){if(view==='pf')return pfXY[n.id]||basicPosition(n);if(view==='bridge')return bridgeXY[n.id]||basicPosition(n);if(view==='data')return dataPositionsCache.get(n.id)||basicPosition(n);if(view==='comparison')return compareXY[n.id]||basicPosition(n);return basicPosition(n)}
let dataPositionsCache=dataPositions();
function matches(n){if(query){const x=[n.id,n.title,n.summary,n.detail,n.stage,...(n.tags||[]),n.asset?.filename||'',n.asset?.sha256||''].join(' ').toLowerCase();return x.includes(query)}return true}
function visibleSet(){let list=G.nodes.filter(n=>{
 if(view==='pf')return Object.prototype.hasOwnProperty.call(pfXY,n.id);
 if(view==='bridge')return Object.prototype.hasOwnProperty.call(bridgeXY,n.id);
 if(view==='comparison')return ['G-GRAV','THEOREM','M-PENROSE-2D','M-SQUARE-2D','M-Z5','M-CUBIC','I-PENROSE-SQUARE','P0','W-ORIGINAL-SOURCES','W-GRAV-OP'].includes(n.id);
 if(view==='spine')return n.kind==='gate'||n.kind==='goal'||n.kind==='model'||n.core&&(n.kind==='result'||n.kind==='work'||n.kind==='data_family'||n.kind==='publication');
 if(view==='evidence')return ['gate','goal','model','result','interface'].includes(n.kind);
 if(view==='work')return ['gate','goal','work','interface'].includes(n.kind)||n.kind==='result'&&n.status==='obstruction';
 if(view==='data')return ['dataset','data_family','manifest'].includes(n.kind)||['P0','M-Z5','M-PRISM','M-PENROSE-2D','M-SQUARE-2D','PUB-THEOREM-REVIEW'].includes(n.id);
 return true;
 });
 if(query){const matching=G.nodes.filter(matches),ids=new Set(matching.map(n=>n.id));for(const n of matching){for(const id of neighbors.get(n.id)){const x=nodeById.get(id);if(x.kind==='gate'||x.kind==='data_family'||x.kind==='model')ids.add(id)}}list=G.nodes.filter(n=>ids.has(n.id))}
 if(filter==='needs')list=list.filter(n=>n.kind==='gate'||n.kind==='goal'||watchStatuses.has(n.status));
 if(filter==='flagged')list=list.filter(n=>annotations[n.id]&&(annotations[n.id].flag||annotations[n.id].note));
 return list;
}
function ensurePositions(){for(const n of G.nodes){if(!positions.has(n.id))positions.set(n.id,[...positionFor(n)])}}
function setView(next){view=next;dataPositionsCache=dataPositions();positions=new Map();highlightedPath=[];
 document.querySelectorAll('.lens').forEach(x=>{const on=x.dataset.view===view;x.classList.toggle('selected',on);x.setAttribute('aria-pressed',String(on))});
 const headings={pf:'COUPLED-Z5 PENROSE–FIBONACCI PRIMARY ROUTE · PF-G0–G5',bridge:'CUBIC SU(2) CONTROL → GEOMETRIC TRANSFER · T0–T5',comparison:'PENROSE GEOMETRY · PERIODIC CONTROLS',spine:'THE PROOF SPINE',evidence:'RECORDED EVIDENCE',work:'UNRESOLVED PROOF WORK',data:'ARCHIVED DATA + CUSTODY',all:'ALL CURATED RELATIONSHIPS'};
 $('graphViewLabel').textContent=headings[view];applyGraph(true)}
function setFilter(next){filter=next;document.querySelectorAll('.filter').forEach(x=>{const on=x.dataset.filter===filter;x.classList.toggle('selected',on);x.setAttribute('aria-pressed',String(on))});applyGraph(true)}
function showError(s){const t=$('nodeLayer');t.replaceChildren();t.appendChild(svg('text',{x:100,y:130,fill:'#9fc0c8','font-size':18},s));edgeLayer.replaceChildren()}
function draw(){if(!viewNodes.length){showError(filter==='flagged'?'No flagged nodes. Select any node to add a review annotation.':'No nodes match this search.');return}
 const edgesFrag=document.createDocumentFragment();for(const e of viewEdges){const a=positions.get(e.from_id),b=positions.get(e.to_id);if(!a||!b)continue;const [ax,ay]=a,[bx,by]=b;const dx=bx-ax,dy=by-ay;const midX=(ax+bx)/2,midY=(ay+by)/2;let cy=-Math.min(56,Math.abs(dx)*.12)*(Math.abs(dy)>150?0.2:1);let d=`M ${ax} ${ay} Q ${midX} ${midY+cy} ${bx} ${by}`;
 const active=selected&&e.from_id===selected||selected&&e.to_id===selected;const pathHit=highlightedPath.includes(e.from_id)&&highlightedPath.includes(e.to_id)&&Math.abs(highlightedPath.indexOf(e.from_id)-highlightedPath.indexOf(e.to_id))===1;
 const pp=svg('path',{d,class:`svg-edge kind-${e.kind}${active||pathHit?' active':''}${selected&&!active&&!pathHit?' dim':''}`});if(e.kind==='dependency')pp.setAttribute('marker-end','url(#edgeArrow)');edgesFrag.appendChild(pp)}edgeLayer.replaceChildren(edgesFrag);
 const nodesFrag=document.createDocumentFragment();for(const n of viewNodes){const [x,y]=positions.get(n.id);const goal=n.kind==='goal',gate=n.kind==='gate',file=n.kind==='dataset';const w=goal?222:gate?205:file?225:190,h=goal?93:gate?88:67;
 const dim=selected&&selected!==n.id&&!neighbors.get(selected).has(n.id)&&!highlightedPath.includes(n.id);
 const g=svg('g',{class:`svg-node kind-${n.kind}${selected===n.id?' selected':''}${dim?' dim':''}`,transform:`translate(${x},${y})`,'data-node':n.id,role:'button',tabindex:0,'aria-label':`${n.title}, ${n.status}. Click for details.`});
 g.appendChild(svg('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:11,class:'node-face'}));
 const stripeColor= n.kind==='dataset'?'#75b3dc':n.status==='obstruction'?'#e49a8b':n.status==='finite'?'#8bd6ba':n.kind==='gate'?'#c9ad87':n.kind==='work'?'#e8b38c':'#9abdd3';
 g.appendChild(svg('rect',{x:-w/2,y:-h/2+13,width:2.5,height:h-26,rx:1,fill:stripeColor}));
 g.appendChild(svg('text',{x:-w/2+14,y:-h/2+20,class:'node-topline'},n.kind==='gate'?`${n.id}   •   NOT CLOSED`:cls(n).toUpperCase()));
 const ls=labelLines(n.kind==='gate'?n.title.split(' · ')[1]:n.title, file?28:goal?26:25);let ly=-h/2+40;for(const line of ls){g.appendChild(svg('text',{x:-w/2+14,y:ly,class:'node-text'},line));ly+=16}
 if(gate){const count=n.checks.filter(x=>x.state==='met').length;g.appendChild(svg('text',{x:w/2-12,y:h/2-11,class:'node-sub','text-anchor':'end'},`${count}/${n.checks.length} scoped checks`))}
 else if(!file)g.appendChild(svg('text',{x:w/2-12,y:h/2-9,class:'node-sub','text-anchor':'end'},tone[n.status]||n.status));
 const local=annotations[n.id];if(local?.flag){g.appendChild(svg('circle',{cx:w/2-10,cy:-h/2+11,r:5.2,class:'node-flag'}))}
 g.addEventListener('pointerdown',e=>onNodePointerDown(e,n.id));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();selectNode(n.id,{shift:e.shiftKey})}});
 nodesFrag.appendChild(g)}nodeLayer.replaceChildren(nodesFrag);cam.setAttribute('transform',`translate(${camera.x},${camera.y}) scale(${camera.k})`)
}
function scheduleDraw(){if(scheduled)return;scheduled=true;requestAnimationFrame(()=>{scheduled=false;draw()})}
function graphMetrics(){const v=new Set(viewNodes.map(n=>n.id));viewEdges=G.edges.filter(e=>v.has(e.from_id)&&v.has(e.to_id));$('visibleCount').textContent=`${viewNodes.length} NODES · ${viewEdges.length} LINKS`}
function applyGraph(refit){viewNodes=visibleSet();ensurePositions();graphMetrics();if(refit)requestAnimationFrame(fitGraph);else scheduleDraw()}
function fitGraph(){if(!viewNodes.length){draw();return}const rect=graph.getBoundingClientRect();svgWidth=rect.width||900;svgHeight=rect.height||680;graph.setAttribute('viewBox',`0 0 ${svgWidth} ${svgHeight}`);
 let xs=viewNodes.map(n=>positions.get(n.id)[0]),ys=viewNodes.map(n=>positions.get(n.id)[1]);const minX=Math.min(...xs)-165,maxX=Math.max(...xs)+165,minY=Math.min(...ys)-100,maxY=Math.max(...ys)+100;
 const k=Math.min(1.15,Math.max(.15,Math.min((svgWidth-70)/(maxX-minX),(svgHeight-100)/(maxY-minY))));camera={k,x:svgWidth/2-k*(minX+maxX)/2,y:svgHeight/2-k*(minY+maxY)/2};scheduleDraw()}
function reset(){positions=new Map();ensurePositions();fitGraph()}
function zoomAt(factor,px=svgWidth/2,py=svgHeight/2){const k=Math.min(2.9,Math.max(.19,camera.k*factor));const gx=(px-camera.x)/camera.k,gy=(py-camera.y)/camera.k;camera.x=px-gx*k;camera.y=py-gy*k;camera.k=k;scheduleDraw()}
function clientPt(e){const r=graph.getBoundingClientRect();return [e.clientX-r.left,e.clientY-r.top]}
function scenePt(pt){return [(pt[0]-camera.x)/camera.k,(pt[1]-camera.y)/camera.k]}
function onNodePointerDown(e,id){if(e.button!==0)return;e.stopPropagation();const pt=clientPt(e);pointer={mode:'node',id,start:pt,last:pt,origin:[...positions.get(id)],moved:false,shift:e.shiftKey};graph.setPointerCapture(e.pointerId)}
graph.addEventListener('pointerdown',e=>{if(e.button!==0||e.target.closest('.svg-node'))return;const pt=clientPt(e);pointer={mode:'pan',start:pt,last:pt,origin:[camera.x,camera.y],moved:false};graph.setPointerCapture(e.pointerId)});
graph.addEventListener('pointermove',e=>{if(!pointer)return;const pt=clientPt(e),dx=pt[0]-pointer.start[0],dy=pt[1]-pointer.start[1];pointer.last=pt;if(Math.hypot(dx,dy)>5)pointer.moved=true;
 if(pointer.mode==='pan'){camera.x=pointer.origin[0]+dx;camera.y=pointer.origin[1]+dy}else{positions.set(pointer.id,[pointer.origin[0]+dx/camera.k,pointer.origin[1]+dy/camera.k])}scheduleDraw()});
graph.addEventListener('pointerup',e=>{if(!pointer)return;const p=pointer;pointer=null;if(p.mode==='node'&&!p.moved)selectNode(p.id,{shift:p.shift});try{graph.releasePointerCapture(e.pointerId)}catch(_){}});
graph.addEventListener('pointercancel',()=>pointer=null);
graph.addEventListener('wheel',e=>{e.preventDefault();const pt=clientPt(e);zoomAt(e.deltaY<0?1.10:1/1.10,...pt)},{passive:false});
function shortestPath(a,b){if(a===b)return [a];const queue=[a],seen=new Set([a]),prev=new Map();for(let i=0;i<queue.length;i++){const cur=queue[i];for(const nxt of neighbors.get(cur)){if(!seen.has(nxt)){seen.add(nxt);prev.set(nxt,cur);queue.push(nxt)}}if(seen.has(b))break}if(!seen.has(b))return [];const path=[b];for(let p=b;p!==a;){p=prev.get(p);path.unshift(p)}return path}
function selectNode(id,{shift=false}={}){if(!nodeById.has(id))return;highlightedPath=shift&&selected?shortestPath(selected,id):[];selected=id;renderDetail();scheduleDraw();const n=nodeById.get(id);$('selectionTrail').textContent=`Selected: ${n.title}`;$('connectionSummary').textContent=highlightedPath.length?`Linked through ${highlightedPath.length} nodes. These are graph connections, not an accepted proof.`:`${neighbors.get(id).size} mapped relationships · ${tone[n.status]||n.status}`;
 document.querySelectorAll('.gate-tile').forEach(x=>x.classList.toggle('selected',x.dataset.gate===id));}
function element(tag,clsName,text){const el=document.createElement(tag);if(clsName)el.className=clsName;if(text!==undefined)el.textContent=text;return el}
function detailSection(parent,heading){const s=element('section','detailsection');s.append(element('h4','',heading));parent.append(s);return s}
function addLink(parent,r){const a=element('a','',r.title||r.path||'Source record');const url=r.url||((r.path&&r.git_blob_sha)?`https://github.com/syncgravity/singular-boundary/blob/${r.git_blob_sha}/${r.path}`:null);if(!url||!/^https:\/\/github\.com\/syncgravity\/singular-boundary\//.test(url))return;a.href=url;a.target='_blank';a.rel='noopener noreferrer';parent.append(a)}
function renderDetail(){const n=nodeById.get(selected);if(!n)return;const d=$('nodeDetail');d.replaceChildren();d.append(element('div','detail-kind',cls(n)));d.append(element('h2','detail-title',n.title));const badge=element('span','detail-status',tone[n.status]||n.status);badge.dataset.tone=n.status;d.append(badge);d.append(element('p','detail-summary',n.summary));if(n.detail)d.append(element('p','detail-description',n.detail));
 if(n.kind==='gate'){const r=detailSection(d,'CLOSURE CERTIFICATES · ALL REQUIRED');const list=element('div','checklist');for(const item of n.checks){const x=element('div','checkrow '+item.state);x.append(element('span','checkicon',item.state==='met'?'✓':item.state==='partial'?'~':item.state==='blocked'?'!':'×'));const body=element('div');body.append(element('span','',item.label));if(item.note)body.append(element('small','',item.note));x.append(body);list.append(x)}r.append(list);r.append(element('p','detail-description','Gate remains OPEN unless the entire model-specific acceptance record is independently verified.'))}
 else if(n.checks?.length){const r=detailSection(d,'EVIDENCE STILL REQUIRED');const list=element('div','checklist');for(const item of n.checks){const x=element('div','checkrow '+item.state);x.append(element('span','checkicon',item.state==='met'?'✓':'×'));x.append(element('span','',item.label));list.append(x)}r.append(list)}
 if(n.asset){const r=detailSection(d,'ORIGINAL DATA · HASHED CUSTODY');r.append(element('div','file-count',`${n.asset.bytes.toLocaleString()} bytes · ${n.asset.kind}`));r.append(element('div','hashbox',n.asset.sha256));r.append(element('div','library-path',n.asset.library_path));const button=element('button','copybtn','Copy SHA-256');button.addEventListener('click',()=>copyText(n.asset.sha256,button));r.append(button);r.append(element('div','detail-description','Git LFS: pending configuration · binary not committed to regular Git.'))}
 if(n.sources?.length){const r=detailSection(d,'SOURCE PINNING');const refs=element('div','ref-list');for(const item of n.sources)addLink(refs,item);r.append(refs)}
 const near=[...neighbors.get(n.id)].sort((a,b)=>(nodeById.get(a).kind==='gate'?-1:1)-(nodeById.get(b).kind==='gate'?-1:1));if(near.length){const r=detailSection(d,'CONNECTED RECORDS');const box=element('div','neighborlist');for(const id of near.slice(0,24)){const b=element('button','',id.startsWith('FILE-')?nodeById.get(id).title:id);b.title=nodeById.get(id).title;b.addEventListener('click',()=>{if(!viewNodes.some(n=>n.id===id)){query=id.toLowerCase();$('nodeSearch').value=id;applyGraph(true)}selectNode(id)});box.append(b)}r.append(box);if(near.length>24)r.append(element('small','detail-description',`+ ${near.length-24} more mapped neighbors`))}
 const note=annotations[n.id]||{};$('reviewFlag').value=note.flag||'';$('reviewNote').value=note.note||'';
}
function copyText(s,b){if(navigator.clipboard?.writeText){navigator.clipboard.writeText(s).then(()=>{b.textContent='Copied ✓'},()=>fallbackCopy(s,b))}else fallbackCopy(s,b)}
function fallbackCopy(s,b){const t=document.createElement('textarea');t.value=s;t.style.position='fixed';t.style.opacity='0';document.body.append(t);t.select();try{document.execCommand('copy');b.textContent='Copied ✓'}catch(_){b.textContent='Select SHA above'}t.remove()}
function persistNotes(){const flag=$('reviewFlag').value,note=$('reviewNote').value.trim();if(flag||note)annotations[selected]={flag,note,updated_at:new Date().toISOString()};else delete annotations[selected];try{localStorage.setItem(notesKey,JSON.stringify(annotations));$('noteSaveStatus').textContent='Saved locally. Export review JSON to propose a repository change.'}catch(_){$('noteSaveStatus').textContent='Browser storage unavailable. Export immediately to preserve annotations.'}
 $('flagCount').textContent=Object.values(annotations).filter(n=>n.flag||n.note).length; if(filter==='flagged')applyGraph(false);else scheduleDraw()}
function download(name,obj){const json=JSON.stringify(obj,null,2)+'\n';const url=URL.createObjectURL(new Blob([json],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),500)}
function renderGateStrip(){const strip=$('gateStrip');for(const n of G.nodes.filter(n=>n.kind==='gate')){const b=element('button','gate-tile');b.dataset.gate=n.id;b.append(element('span','gatecode',n.id),element('span','gatetitle',n.title.split(' · ')[1]),element('span','gatemeta',`OPEN · ${n.checks.filter(x=>x.state==='met').length}/${n.checks.length} scoped checks`));b.addEventListener('click',()=>{if(!viewNodes.some(x=>x.id===n.id)){query='';$('nodeSearch').value='';setView('spine')}selectNode(n.id);focusNode(n.id)});strip.append(b)}}
function focusNode(id){const pt=positions.get(id);if(!pt)return;camera.k=Math.max(.9,Math.min(camera.k,1.28));camera.x=svgWidth/2-pt[0]*camera.k;camera.y=svgHeight/2-pt[1]*camera.k;scheduleDraw()}
// UI bindings
for(const b of document.querySelectorAll('.lens'))b.addEventListener('click',()=>setView(b.dataset.view));
for(const b of document.querySelectorAll('.filter'))b.addEventListener('click',()=>setFilter(b.dataset.filter));
$('nodeSearch').addEventListener('input',e=>{query=e.target.value.trim().toLowerCase();applyGraph(true)});
$('zoomIn').addEventListener('click',()=>zoomAt(1.22));$('zoomOut').addEventListener('click',()=>zoomAt(1/1.22));$('fitGraph').addEventListener('click',fitGraph);$('resetGraph').addEventListener('click',reset);
$('reviewFlag').addEventListener('change',persistNotes);$('reviewNote').addEventListener('input',()=>{clearTimeout(noteTimer);noteTimer=setTimeout(persistNotes,380)});
$('exportNotes').addEventListener('click',()=>{persistNotes();download('singular-boundary-review-notes.json',{schema:'singular-boundary.review-annotations.v1',not_proof_certification:true,graph_version:G.version,exported_at:new Date().toISOString(),notes:annotations})});
$('importNotes').addEventListener('change',async e=>{const file=e.target.files?.[0];if(!file)return;try{const content=JSON.parse(await file.text());if(content.schema!=='singular-boundary.review-annotations.v1'||!content.notes||typeof content.notes!=='object')throw Error('Invalid annotation schema');for(const [k,v] of Object.entries(content.notes))if(nodeById.has(k)&&typeof v.note==='string'&&['','needs-proof','needs-evidence','review-ready'].includes(v.flag||'')){annotations[k]={flag:v.flag||'',note:v.note.slice(0,4000),updated_at:new Date().toISOString()}}try{localStorage.setItem(notesKey,JSON.stringify(annotations))}catch(_){}renderDetail();$('flagCount').textContent=Object.keys(annotations).length;applyGraph(false);$('noteSaveStatus').textContent='Review notes imported locally; canonical proof status unchanged.'}catch(err){$('noteSaveStatus').textContent='Import rejected: '+String(err.message)}e.target.value=''});
$('exportGraph').addEventListener('click',()=>download('singular-boundary-knowledge-graph.json',G));
window.addEventListener('resize',()=>{clearTimeout(window.__atlasResize);window.__atlasResize=setTimeout(fitGraph,90)});
$('countNodes').textContent=G.nodes.length;$('countEdges').textContent=G.edges.length;$('countFiles').textContent=G.nodes.filter(n=>n.kind==='dataset').length;$('flagCount').textContent=Object.values(annotations).filter(n=>n.flag||n.note).length;
renderGateStrip();ensurePositions();applyGraph(true);selectNode('PF-G0');
// Start at an inspectable reading scale; Fit view remains available for the entire atlas.
requestAnimationFrame(()=>requestAnimationFrame(()=>{if(view==='pf'&&!query&&filter==='all'){camera.k=.58;camera.x=svgWidth/2-1000*camera.k;camera.y=svgHeight/2-640*camera.k;scheduleDraw()}else if(view==='bridge'&&!query&&filter==='all'){camera.k=.6;camera.x=svgWidth/2-1100*camera.k;camera.y=svgHeight/2-550*camera.k;scheduleDraw()}else if(view==='comparison'&&!query&&filter==='all'){camera.k=.64;camera.x=svgWidth/2-650*camera.k;camera.y=svgHeight/2-375*camera.k;scheduleDraw()}else if(view==='spine'&&!query&&filter==='all'){camera.k=.71;camera.x=svgWidth/2-810*camera.k;camera.y=svgHeight/2-555*camera.k;scheduleDraw()}}));
})();
