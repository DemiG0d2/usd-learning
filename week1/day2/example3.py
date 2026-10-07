from pxr import Usd, UsdGeom, UsdShade, Gf, Sdf

file_path = "week1/day2/relationship_ex3.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

cube_1: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube_1"))
cube_2: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube_2"))
UsdGeom.XformCommonAPI(cube_2).SetTranslate(Gf.Vec3d(5,0,0))
cube_3: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube_3"))
UsdGeom.XformCommonAPI(cube_3).SetTranslate(Gf.Vec3d(10,0,0))
sphere_1: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere_1"))
UsdGeom.XformCommonAPI(sphere_1).SetTranslate(Gf.Vec3d(0,5,0))

#Create typeless container for the materials
looks = stage.DefinePrim(("/World/Looks"))

#Create Simple green material for preview
green: UsdShade.Material = UsdShade.Material.Define(stage, looks.GetPath().AppendPath("GreenMat"))
green_ps = UsdShade.Shader.Define(stage, green.GetPath().AppendPath("PreviewSurface"))
green_ps.CreateIdAttr("UsdPreviewSurface")
green_ps.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3d(0.0,1.0,0.0))
green.CreateSurfaceOutput().ConnectToSource(green_ps.ConnectableAPI(), "surface")

#Create simple red material for preview
red: UsdShade.Material = UsdShade.Material.Define(stage, looks.GetPath().AppendPath("RedMat"))
red_ps = UsdShade.Shader.Define(stage, red.GetPath().AppendPath("PreviewSurface"))
red_ps.CreateIdAttr("UsdPreviewSurface")
red_ps.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3d(1.0,0.0,0.0))
red.CreateSurfaceOutput().ConnectToSource(red_ps.ConnectableAPI(), "surface")

#Create simple blue material for preview
blue: UsdShade.Material = UsdShade.Material.Define(stage, looks.GetPath().AppendPath("BlueMat"))
blue_ps = UsdShade.Shader.Define(stage, blue.GetPath().AppendPath("PreviewSurface"))
blue_ps.CreateIdAttr("UsdPreviewSurface")
blue_ps.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3d(0.0,0.0,1.0))
blue.CreateSurfaceOutput().ConnectToSource(blue_ps.ConnectableAPI(), "surface")

#Bind materials to the Prims
UsdShade.MaterialBindingAPI.Apply(cube_1.GetPrim()).Bind(green)
UsdShade.MaterialBindingAPI.Apply(cube_2.GetPrim()).Bind(green)
UsdShade.MaterialBindingAPI.Apply(cube_3.GetPrim()).Bind(red)
UsdShade.MaterialBindingAPI.Apply(sphere_1.GetPrim()).Bind(blue)

#Verify by printing the direct biniding
for prim in [cube_1, cube_2, cube_3, sphere_1]:
    mat = UsdShade.MaterialBindingAPI(prim).GetDirectBinding().GetMaterial()
    print(f"{prim.GetPath()} -> {mat.GetPath() if mat else 'None'}")

stage.Save()