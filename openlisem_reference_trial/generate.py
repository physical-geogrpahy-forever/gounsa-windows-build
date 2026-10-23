"""One-hectare OpenLISEM full-model reference/sensitivity input set.
Only creates official PCRaster maps and .run settings. Never simulates erosion itself.
"""
import math,re
from pathlib import Path
import numpy as np
import rasterio
from rasterio.transform import from_origin

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'openlisem_virtual_trial'
ROOT=HERE
R=C=50
DX=2.0
TRANSFORM=from_origin(337000,4062000,DX,DX)
for directory in ("maps","rain","runs","results","logs"):
    (ROOT/directory).mkdir(parents=True,exist_ok=True)

cases={
    "Oak": {"source":"Oak_sprouts_sparse","lai":1.2,"cover":.4,"height":1.8,"smax":.343,"n":.12},
    "Miscanthus": {"source":"Miscanthus_dense","lai":3.0,"cover":.85,"height":1.3,"smax":1.551,"n":.20},
}
variants=[
    ("Oak",5, "exponential",1),("Oak",10,"exponential",1),("Oak",20,"exponential",1),
    ("Miscanthus",5,"exponential",1),("Miscanthus",10,"exponential",1),("Miscanthus",20,"exponential",1),
    ("Oak",5, "linear",1),("Oak",10,"linear",1),
    ("Miscanthus",5,"linear",1),("Miscanthus",10,"linear",1),
    ("Oak",10,"exponential",2),("Miscanthus",10,"exponential",2),
]
def save_map(path, arr, kind):
    dtype, scale={
      "VS_SCALAR":("float32","VS_SCALAR"),
      "VS_NOMINAL":("int32","VS_NOMINAL"),
      "VS_BOOLEAN":("uint8","VS_BOOLEAN"),
      "VS_LDD":("uint8","VS_LDD"),
      "VS_ORDINAL":("int32","VS_ORDINAL"),
      "VS_DIRECTION":("float32","VS_DIRECTION"),
    }[kind]
    with rasterio.open(path,"w",driver="PCRaster",count=1,width=C,height=R,
                       dtype=dtype,crs="EPSG:32652",transform=TRANSFORM,PCRASTER_VALUESCALE=scale) as ds:
        ds.write(np.asarray(arr,dtype=dtype),1)
    with rasterio.open(path) as ds:
        assert ds.tags().get("PCRASTER_VALUESCALE")==scale,(path,ds.tags())

for species,attrs in cases.items():
    source=BASE/"maps"/attrs["source"]
    assert source.exists(),source
    target=ROOT/"maps"/species
    target.mkdir(exist_ok=True)
    for origin in source.glob("*.map"):
        with rasterio.open(origin) as ds:
            vs=ds.tags()["PCRASTER_VALUESCALE"]
            sample=ds.read(1)
        val=sample[5,5]
        a=np.full((R,C),val)
        name=origin.name.lower()
        if name=="dem.map":
            yy,xx=np.mgrid[:R,:C]
            a=100.0+0.25*(R-1-yy)*DX+0.0005*xx*DX
        elif name=="grad.map":
            a=np.full((R,C),math.sin(math.atan(.25)))
        elif name=="ldd.map":
            a=np.full((R,C),2,dtype=np.uint8)
            a[-1,:]=5
        elif name in ("outlet.map","outpoints.map"):
            a=np.zeros((R,C),dtype=np.int32);a[-1,C//2]=1
        elif name in ("id.map","landuse.map"):
            a=np.ones((R,C),dtype=np.int32)
        elif name=="per.map":a=np.full((R,C),attrs["cover"])
        elif name=="lai.map":a=np.full((R,C),attrs["lai"])
        elif name=="ch.map":a=np.full((R,C),attrs["height"])
        elif name=="smax.map":a=np.full((R,C),attrs["smax"])
        elif name=="n.map":a=np.full((R,C),attrs["n"])
        elif name=="ksat1.map":a=np.full((R,C),2.)
        elif name=="psi1.map":a=np.full((R,C),1.)
        elif name=="soildep1.map":a=np.full((R,C),250.)
        elif name=="coh.map":a=np.full((R,C),4.)
        if name=="ldd.map":
            # GDAL's PCRaster VS_LDD writer silently forces 1m cell size
            # irrespective of the requested transform. This LDD is the model's
            # master mask; using georeferenced GeoTIFF preserves the intended dx.
            with rasterio.open(target/"ldd.tif","w",driver="GTiff",count=1,
                               width=C,height=R,dtype="uint8",
                               crs="EPSG:32652",transform=TRANSFORM,nodata=0) as out:
                out.write(np.asarray(a,dtype="uint8"),1)
            with rasterio.open(target/"ldd.tif") as out:
                assert abs(out.res[0]-DX)<1e-8,(out.res,DX)
        else:
            save_map(target/origin.name,a,vs)

for species,dt,mode,det in variants:
    label=f"{species}_dt{dt}_{mode}_eff{det}"
    origin=BASE/"runs"/f"{cases[species]['source']}_P20.run"
    s=origin.read_text(encoding="utf8")
    mods={
        "Timestep":str(dt),
        "Flooding courant factor":"0.1",
        "Deposition exponential":"1" if mode=="exponential" else "0",
        "Deposition continuous":"1",
        "Detachment efficiency":str(det),
        "Map Directory":str((ROOT/"maps"/species).resolve())+"\\",
        "Result Directory":str((ROOT/"results"/label).resolve())+"\\",
        "Rainfall Directory":str((ROOT/"rain").resolve())+"\\",
        "Rainfall file":f"P20_dt{dt}.txt",
        # Hold cumulative rain near 20 mm across different host timesteps.
        "Rainfall Bias Correction":str(3600/(3600+dt)),
    }
    for k,v in mods.items():
        patt=re.compile(rf"(?m)^{re.escape(k)}=.*$")
        matches=patt.findall(s)
        assert len(matches)==1,(k,origin,len(matches))
        s=patt.sub(lambda m:k+"="+v,s)
    s,n=re.subn(r"(?m)^ldd=.*$", "ldd=ldd.tif", s)
    assert n==1,(label,"LDD assignment missing")
    (ROOT/"runs"/(label+".run")).write_text(s,encoding="utf8")
    (ROOT/"results"/label).mkdir(exist_ok=True)
    (ROOT/"rain"/f"P20_dt{dt}.txt").write_text(
       "# Constant 20 mm/h for 60 minutes\n2\ntime\ngauge 1\n001:0000 20.0\n001:0060 0\n001:0120 0\n",
       encoding="ascii")

assert len(list((ROOT/"runs").glob("*.run")))==len(variants)
assert len(list((ROOT/"maps").rglob("*.map")))>=60
print("Reference trials: 50 x 50 at 2m = 1 ha plan area,",
      len(variants),"full OpenLISEM runs",
      len(list((ROOT/"maps").rglob("*.map"))),"PCRaster maps")
