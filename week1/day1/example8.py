from pxr import Usd

file_path = "week1/day1/prim_hierarchy.usda"
stage: Usd.Stage = Usd.Stage.Open(file_path)

prim: Usd.Prim = stage.GetPrimAtPath("/Geometry")
child_prim: Usd.Prim
if child_prim := prim.GetChild("GroupTransform"):
    print("Child prim exists")
else:
    print("Child prim does not exist")