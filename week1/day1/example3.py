from pxr import Usd

#Create a new stage only in memory
stage: Usd.Stage = Usd.Stage.CreateInMemory()

#Add a prim
stage.DefinePrim("/World", "Xform")

#Print the stage content to the console
print("In-memory Stage:")
print(stage.ExportToString(addSourceFileComment=False))

#Export the stage to disk if needed
stage.Export("week1/day1/in_memory_stage.usda")