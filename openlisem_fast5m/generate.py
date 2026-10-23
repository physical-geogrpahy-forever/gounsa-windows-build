"""Fast 5m-grid OpenLISEM: preserve LDD cell size and avoid closed lower boundary."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
source_file=HERE.parent/"openlisem_reference_trial"/"generate.py"
s=source_file.read_text(encoding="utf8")
assert "R=C=50" in s and "DX=2.0" in s
s=s.replace("R=C=50","R=C=20").replace("DX=2.0","DX=5.0")
# Restore a single valid outlet observation point while retaining the
# non-pit open lower boundary elsewhere. Only diagnoses native init behaviour.
old="a=np.zeros((R,C),dtype=np.int32)\n        elif name in (\"id.map\",\"landuse.map\")"
new="a=np.zeros((R,C),dtype=np.int32);a[-1,C//2]=1\n        elif name in (\"id.map\",\"landuse.map\")"
assert s.count(old)==1
s=s.replace(old,new)
selection="""variants=[
    ("Oak",5,"exponential",1),
    ("Oak",10,"exponential",1),
    ("Oak",20,"exponential",1),
    ("Miscanthus",10,"exponential",1),
    ("Oak",10,"exponential",2),
    ("Miscanthus",10,"exponential",2),
]
def save_map"""
s,n=re.subn(r"variants=\[.*?\]\ndef save_map",selection,s,flags=re.S)
assert n==1,n
namespace={"__name__":"__main__","__file__":str(source_file)}
exec(compile(s,str(source_file),"exec"),namespace)

# Physics control: switch to the unmodified native kinematic-wave route for
# a steep-slope comparison. No new hydraulic or erosion equations are used.
run_root=HERE.parent/"openlisem_reference_trial"/"runs"
for p in run_root.glob("*.run"):
    text=p.read_text(encoding="utf8")
    old="Routing Kin Wave 2D=2"
    assert text.count(old)==1,(p,old)
    p.write_text(text.replace(old,"Routing Kin Wave 2D=0"),encoding="utf8")
print("Native OpenLISEM kinematic-wave runs:",len(list(run_root.glob("*.run"))))
