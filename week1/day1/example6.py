from pxr import Usd, UsdGeom

file_path = "week1/day1/sphere_prim.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

#Define a prim of the type Sphere at the path /hello
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, "/hello")
sphere.CreateRadiusAttr().Set(2)

stage.Save()