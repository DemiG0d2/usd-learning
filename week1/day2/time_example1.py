from pxr import Usd

#open stage created in time_example.py -> timecode_sample.usda
stage: Usd.Stage = Usd.Stage.Open("week1/day2/timecode_sample.usda")

#Set the start and end time codes for the stage
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(0)

#Export to a new flattened layer for this example
stage.Export("week1/day2/timecode_ex1.usda", addSourceFileComment=False)
