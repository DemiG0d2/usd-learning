from pxr import Usd, UsdGeom, Sdf

file_path = "week1/day3/path_property_authoring.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

#A prim to work with
sphere = UsdGeom.Sphere.Define(stage, "/World/Geom/Sphere")

#Create a property path for the attribute /World/geom/Sphere.userProperties:tag
attr_property_path = sphere.GetPath().AppendProperty("userProperties:tag")

#working with the property path for the attribute
owner_prim = stage.GetPrimAtPath(attr_property_path.GetPrimPath())
attr_name = stage.GetPropertyAtPath(attr_property_path).GetPath().name 
print(f"Attribute Property '{attr_name}' has been defined on {owner_prim.GetPath()} after AppendProperty: {owner_prim.GetAttribute(attr_name).IsDefined()}")

#define the attribute on the ownr prim
attr = owner_prim.CreateAttribute(attr_name, Sdf.ValueTypeNames.String)
print(f"\nAttribute property '{attr_name}' has been defined on {owner_prim.GetPath()} after CreateAttribute: {owner_prim.GetAttribute(attr_name).IsDefined()}")

attr.Set("surveyed")
print(f"Attribute value afer Set: {stage.GetAttributeAtPath(attr_property_path).Get()}")

#Create a relationship from a property path
marker = UsdGeom.Xform.Define(stage, "/World/Markers/MarkerA")
#Create a property path for the relationship
rel_property_path = sphere.GetPath().AppendProperty("my:ref")

#Working with the property path for the relationship
owner_prim = stage.GetPrimAtPath(rel_property_path.GetPrimPath())
rel_name = stage.GetPropertyAtPath(rel_property_path).GetPath().name
print(f"\nRealtionship property '{rel_name}' has been defined on {owner_prim.GetPath()} after AppendProperty: {owner_prim.GetRelationship(rel_name).IsDefined()}")

#Define the relationship on the owner prim
rel = owner_prim.CreateRelationship(rel_name)
print(f"\nRelationship property '{rel_name}' has been defined on {owner_prim.GetPath()} after CreateRelationship: {owner_prim.GetRelationship(rel_name).IsDefined()}")

rel.AddTarget(marker.GetPath())
print(f"Relationship targets after AddTarget: {[str(p) for p in stage.GetRelationshipAtPath(rel_property_path).GetTargets()]}")

stage.Save()