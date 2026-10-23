import math, re, urllib.request
from pathlib import Path
import numpy as np
import rasterio
from rasterio.transform import from_origin

ROOT=Path(__file__).resolve().parent
for sub in ("maps","rain","runs","results","logs"):
    (ROOT/sub).mkdir(exist_ok=True)

SOURCE="https://raw.githubusercontent.com/vjetten/openlisem/main_C/ui_full/LisUIDefaultNames.cpp"
raw=urllib.request.urlopen(SOURCE,timeout=45).read().decode("utf-8",errors="replace")
head,rest=raw.split("void lisemqt::defaultRunFile()",1)
block=rest.split("//---------------------------------------------------------------------------",1)[0]
entries=[]
last=""
for line in block.splitlines():
    line=line.split("//",1)[0].strip()
    m=re.search(r'namelist\[i\]\.value\s*=\s*QString\("(.*?)"\)',line)
    if m: last=m.group(1).replace("\\\\","\\")
    m=re.search(r'namelist\[i\+\+\]\.name\s*=\s*QString\("(.*?)"\)',line)
    if m:
        entries.append((m.group(1),last))
        last=""
assert len(entries)>200, ("incomplete original runfile",len(entries))
defaults=[]
for m in re.finditer(r'DEFmaps\.append\("(.*?)"\)',head):
    parts=m.group(1).split(";")
    if len(parts)==5 and parts[0]=="2":
        defaults.append((parts[4],parts[2]))
names=dict(defaults)
assert all(k in names for k in ("dem","grad","ldd","ID","cover","lai","ch","smax","manning","ksat1","coh"))

R,C,DX=25,15,1.0
tr=from_origin(337000,4062000,DX,DX)
Y,X=np.mgrid[0:R,0:C]
z=100+0.35*(R-1-Y)*DX+0.015*np.abs(X-(C-1)/2)*DX
ones=np.ones((R,C));zeros=np.zeros((R,C))
ldd=np.full((R,C),2,dtype=np.uint8)
ldd[R-1,:]=6
ldd[R-1,C-1]=5
outlet=np.zeros((R,C),dtype=np.int32)
outlet[R-1,C-1]=1
common={"dem":z,"grad":ones*math.sin(math.atan(.35)),
        "rr":ones,"litter":zeros,"ksat1":ones*2,"psi1":ones*1,
        "thetas1":ones*.45,"thetai1":ones*.25,"soildep1":ones*250,
        "stonefrc":ones*.1,"coh":ones*4,"cohadd":zeros,
        "aggrstab":ones*50,"d50":ones*100,"d90":ones*300,
        "crustfrc":zeros,"compfrc":zeros,"flowboundary":zeros}
noms={"ID":ones.astype(np.int32),"outlet":outlet,"outpoint":outlet,
      "landunit":ones.astype(np.int32),"ldd":ldd}
cases={
 "Miscanthus_dense":(.85,3.0,1.3,1.551,.20),
 "Oak_sprouts_sparse":(.40,1.2,1.8,.343,.12),
 "Miscanthus_canopy_only":(.85,3.0,1.3,1.551,.12),
 "Oak_canopy_only":(.40,1.2,1.8,.343,.12),
 "Oak_flat":(.40,1.2,1.8,.343,.12),
 "Miscanthus_flat":(.85,3.0,1.3,1.551,.20),
 "Oak_v_corrected":(.40,1.2,1.8,.343,.12),
 "Miscanthus_v_corrected":(.85,3.0,1.3,1.551,.20),
 "Oak_flat_corrected":(.40,1.2,1.8,.343,.12),
 "Miscanthus_flat_corrected":(.85,3.0,1.3,1.551,.20)}
def write_map(path,array,kind="scalar"):
    typ,vs={"scalar":("float32","VS_SCALAR"),"nominal":("int32","VS_NOMINAL"),"ldd":("uint8","VS_LDD")}[kind]
    with rasterio.open(path,"w",driver="PCRaster",width=C,height=R,count=1,dtype=typ,
                       transform=tr,crs="EPSG:32652",PCRASTER_VALUESCALE=vs) as ds:
        ds.write(np.asarray(array,dtype=typ),1)
    with rasterio.open(path) as ds:
        if ds.tags().get("PCRASTER_VALUESCALE")!=vs:
            raise RuntimeError("invalid PCRaster value scale "+str(path))

for case,values in cases.items():
    cover,lai,height,smax,n=values
    dest=ROOT/"maps"/case
    dest.mkdir(exist_ok=True)
    maps=dict(common)
    if "_flat" in case:
        # Remove the artificial 1.5% V-shaped cross-slope.
        # Keep identical downstream 35% gradient and substrate/vegetation.
        maps["dem"] = 100+0.35*(R-1-Y)*DX
    maps.update({"cover":ones*cover,"lai":ones*lai,"ch":ones*height,
                 "smax":ones*smax,"manning":ones*n})
    for key,val in maps.items():
        if key in names: write_map(dest/names[key],val)
    nom_local=dict(noms)
    if case.endswith("_corrected"):
        ldd_local=np.full((R,C),2,dtype=np.uint8)
        if "_flat" in case:
            # Surface flow goes to the lower boundary with no lateral DEM gradient.
            # LDD bottom-row pits represent the terminal boundary cells.
            ldd_local[-1,:]=5
        else:
            # The V-shaped swale drains toward centre column c=7, not right edge.
            ldd_local[-1,:C//2]=6
            ldd_local[-1,C//2+1:]=4
            ldd_local[-1,C//2]=5
        out_local=np.zeros((R,C),dtype=np.int32)
        out_local[-1,C//2]=1
        nom_local.update({"ldd":ldd_local,"outlet":out_local,"outpoint":out_local})
    for key,val in nom_local.items():
        if key in names: write_map(dest/names[key],val,"ldd" if key=="ldd" else "nominal")
    for key,name in defaults:
        p=dest/name
        if p.exists() or not name.endswith(".map"): continue
        if key.lower().startswith("ldd"):write_map(p,ldd,"ldd")
        elif key in ("ETID","IDGauges","profmap","profcrst","profcomp","profgras","qinpoints"):
            write_map(p,zeros,"nominal")
        else:write_map(p,zeros)
    for key in ("dem","grad","ldd","outlet","ID","lai","cover","smax","ch","manning","ksat1","coh"):
        assert (dest/names[key]).exists(), (case,key)

for intensity in (5,10,20):
    (ROOT/"rain"/("P%02d.txt"%intensity)).write_text(
        "# Virtual one-hour rainfall\n2\ntime\ngauge 1\n001:0000  %d\n001:0060  0\n001:0120  0\n"%intensity,
        encoding="ascii")

changes={
 "Result datetime":"0","Add timestamp":"0","Begin time":"001:0000",
 "End time":"001:0120","Timestep":"10",
 "Include Rainfall":"1","Event based":"0","Include ET":"0",
 "Include Interception":"1","Canopy storage equation":"8","Include litter interception":"0",
 "Include Infiltration":"1","Infil Method":"3","Nr input layers":"1",
 "Include compacted":"0","Include crusts":"0","Impermeable sublayer":"0",
 "Routing Kin Wave 2D":"2","Flow Boundary 2D":"1","Flood initial level map":"0",
 "Include main channels":"0","Include GW flow":"0",
 "Include Infrastructure":"0","Include buildings":"0","Include road system":"0",
 "Include storm drains":"0","Hard Surfaces":"0",
 "Include Mitigation/Conservation":"0","Include Erosion simulation":"1",
 "Flooding SS method":"1","Flooding BL method":"1",
 "OutRunoff":"1","OutInf":"1","OutInterception":"1","OutDet":"1","OutDep":"1",
 "OutSL":"1","Output maps end":"1","OutWH":"1",
 "Nr user Cores":"1","End run report":"1","Report format GTiff":"0"}
for case in cases:
    for intensity in (5,10,20):
        label="%s_P%02d"%(case,intensity)
        mods=dict(changes)
        mods.update({
          "Map Directory":str((ROOT/"maps"/case).resolve())+"\\",
          "Result Directory":str((ROOT/"results"/label).resolve())+"\\",
          "Rainfall Directory":str((ROOT/"rain").resolve())+"\\",
          "Rainfall file":"P%02d.txt"%intensity})
        (ROOT/"results"/label).mkdir(exist_ok=True)
        lines=[]
        for k,v in entries:
            if not k:lines.append("");continue
            if k.startswith("["):lines.append(k);continue
            lines.append(k+"="+str(mods.get(k,v)))
        if "[map names]" not in lines:lines.append("[map names]")
        lines += [k+"="+v for k,v in defaults]
        (ROOT/"runs"/(label+".run")).write_text("\n".join(lines)+"\n",encoding="utf-8")
print("Generated",len(list((ROOT/"runs").glob("*.run"))),"runs,",
      len(list((ROOT/"maps").rglob("*.map"))),"PCRaster maps")
