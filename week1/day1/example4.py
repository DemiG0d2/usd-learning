from pxr import Usd, Sdf
import os

#Create a new stage
stage: Usd.Stage= Usd.Stage.CreateNew("week1/day1/root_layer.usda")

#Get the root layer object
root_layer: Sdf.Layer = stage.GetRootLayer()

#Use relpath to avoid printing build machine filesystem info.
print("Root layer identifier: ", os.path.relpath(root_layer.identifier))

#Add a simple prim
stage.DefinePrim("/World", "Xform")

#Create an additional layer and add it is sublayer
extra_layer: Sdf.Layer = Sdf.Layer.CreateNew("week1/day1/extra_layer.usda")

#Anchor the path relaticve to the root layer for better portaability
rel_path = "./" + os.path.basename(extra_layer.identifier)
root_layer.subLayerPaths.append(rel_path)

#Save both layers
stage.Save()
extra_layer.Save()

#Print the content of the root layer to the console
print("Root layer content:")
print(root_layer.ExportToString())