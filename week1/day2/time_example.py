from pxr import Usd, UsdGeom, Gf

file_path = "week1/day2/timecode_sample.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world.GetPath().AppendPath("Sphere"))

box: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world.GetPath().AppendPath("Backdrop"))
box.GetDisplayColorAttr().Set([(0.0,0.0,1.0)])
cube_xform_api = UsdGeom.XformCommonAPI(box)
cube_xform_api.SetScale(Gf.Vec3f(5,5,0.1))
cube_xform_api.SetTranslate(Gf.Vec3d(0,0,-2))

stage.Save()