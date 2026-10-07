from pxr import Usd, UsdGeom, Gf

file_path = "week1/day2/relationship_ex1.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

#define a Sphere under world xform 
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))

#define a cube under the world xform and move it 5 units away from the sphere
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

#create typeless container for the group
group = stage.DefinePrim("/World/Group")

#Define the relationship
group.CreateRelationship("members", custom=True).SetTargets(
    [sphere.GetPath(), cube.GetPath()]
)

#List relationship targets
members_rel =  group.GetRelationship("members")
print("Group members:", [str(p) for p in members_rel.GetTargets()])

stage.Save()