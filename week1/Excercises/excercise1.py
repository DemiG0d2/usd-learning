from pxr import Usd, UsdGeom, Gf

file_path = "week1/Excercises/excercise1.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Box"))
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Ball"))
UsdGeom.XformCommonAPI(sphere).SetTranslate(Gf.Vec3d(5,0,0))



stage.Save()