from pxr import Usd, UsdGeom

file_path = "week1/day2/relationship_ex2.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

high: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("HiRes"))

low: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Proxy"))

UsdGeom.Imageable(high).GetPurposeAttr().Set("render")
UsdGeom.Imageable(low).GetPurposeAttr().Set("proxy")

#Author the proxy link on the render prim
UsdGeom.Imageable(high).GetProxyPrimRel().SetTargets([low.GetPath()])

#Tools that honor proxyPrim should draw the proxy in preview
draw_prim = UsdGeom.Imageable(high).ComputeProxyPrim()

#Return USd. prim
print("Preview should draw:", str(draw_prim[0].GetPath() if draw_prim else high.GetPath()))

stage.Save()
