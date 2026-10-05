from pxr import Usd

#Define a filepath name
file_path = "week1/day1/hello_world.usda"

#create a stage at the file path
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
print(stage.ExportToString(addSourceFileComment=False))