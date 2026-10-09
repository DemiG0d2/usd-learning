from pxr import Usd, UsdGeom, Sdf

stage: Usd.Stage = Usd.Stage.CreateNew("week1/day3/paths_build_and_nav.usda")

#buill prim paths via Sdf.Path
world_path = Sdf.Path("/World")
geometry_path = world_path.AppendChild("Geometry") #/World/Geometry
sphere_path = geometry_path.AppendChild("Sphere")  #/World/Geometry/Sphere

looks_path = world_path.AppendChild("Looks") #/World/Looks
material_path = looks_path.AppendChild("Material") ##/World/Looks/Material

#Define prims at those paths
stage.DefinePrim(world_path)
stage.DefinePrim(geometry_path)
UsdGeom.Sphere.Define(stage, sphere_path)
stage.DefinePrim(looks_path)
stage.DefinePrim(material_path)

#path check and basic navigation
print("sphere_path IsPrimPath:", sphere_path.IsPrimPath())
print("sphere_path parent:", sphere_path.GetParentPath())
print("Geometry prim valid:", stage.GetPrimAtPath(geometry_path).IsValid())
print("\nmaterial_path IsPrimPath:", material_path.IsPrimPath())
print("material_path parent:", material_path.GetParentPath())
print("Looks prim Valid:", stage.GetPrimAtPath(looks_path).IsValid())

stage.Save()