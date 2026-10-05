from pxr import Usd, UsdGeom

file_path = "week1/day1/prim_hierarchy.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

#Define a Scope prim in stage at /Geometry
geom_scope: UsdGeom.Scope = UsdGeom.Scope.Define(stage, "/Geometry")

#Define a xform prim in the stage as a child of the /Geometry prim called grouptransform
xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, geom_scope.GetPath().AppendPath("GroupTransform"))

#Define a cube prim in the stage as a child of the /Geometry/GroupTransform prim called box
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, xform.GetPath().AppendPath("Box"))

stage.Save()