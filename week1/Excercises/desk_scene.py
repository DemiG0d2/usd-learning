from pxr import Usd, UsdGeom, Gf

file_path = "week1/Excercises/desk_scene.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
UsdGeom.SetStageMetersPerUnit(stage, 1.0)

world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

def make_box(path, size, pos, color):
    cube = UsdGeom.Cube.Define(stage, path)
    cube.GetSizeAttr().Set(1.0)
    api = UsdGeom.XformCommonAPI(cube)
    api.SetTranslate(Gf.Vec3d(*pos))
    api.SetScale(Gf.Vec3f(*size))
    cube.GetDisplayColorAttr().Set([Gf.Vec3f(*color)])
    return cube

#Desk: top surface sits at y = 0.75m
UsdGeom.Xform.Define(stage, "/World/Desk")
make_box("/World/Desk/Top", (1.2, 0.04, 0.7), (0, 0.73, 0), (0.55, 0.38, 0.2))
for i, (x,z) in enumerate([(-0.55, -0.3), (0.55, -0.3), (-0.55, 0.3), (0.55, 0.3)]):
    make_box(f"/World/Desk/Leg{i}", (0.05, 0.71, 0.05), (x, 0.355, z), (0.4, 0.28, 0.15))

#Item on the Desk
UsdGeom.Xform.Define(stage, "/World/Items")
for i in range(12):
    row, col = divmod(i, 4)
    h = 0.03 + 0.01 * (i % 3)
    make_box(f"/World/Items/Book{i}", (0.2, h, 0.15), (-0.45 + col * 0.3, 0.75 + h / 2, -0.2 + row * 0.2), (0.2, 0.4 + 0.05 *(i % 4), 0.7))

stage.Save()