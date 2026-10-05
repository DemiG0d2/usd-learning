#open an existing usd file and make changes to the stage and save the changes to the file

from pxr import Usd

#Open existing stage at the file path
stage: Usd.Stage = Usd.Stage.Open("week1/day1/hello_world.usda")

#Add a simple prim
stage.DefinePrim("/World", "Xform")

#Save the changes to the file
stage.Save()

#Print the stage as text so we can inspect the result
print(stage.ExportToString(addSourceFileComment=False))