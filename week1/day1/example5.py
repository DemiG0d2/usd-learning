from pxr import Usd

stage: Usd.Stage = Usd.Stage.CreateNew("week1/day1/prims.usda")

#Define a new prim at the path
stage.DefinePrim("/hello")

#Define a new prim at the path with the prim type
stage.DefinePrim("/world", "Sphere")

stage.Save()