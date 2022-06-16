from distutils.dir_util import copy_tree
import os
import shutil

dirs = ["D:/Minecraft Stuff/Addons Development/survival-expansion-ocean/Survival Expansion Ocean BP", "D:/Minecraft Stuff/Addons Development/survival-expansion-ocean/Survival Expansion Ocean RP"]
BP = "D:/Minecraft Stuff/Tools/bridge. v2/projects/Survival Expansion Ocean/BP"
RP = "D:/Minecraft Stuff/Tools/bridge. v2/projects/Survival Expansion Ocean/RP"

shutil.rmtree(BP)
shutil.rmtree(RP)

copy_tree(dirs[0], BP)
copy_tree(dirs[1], RP)