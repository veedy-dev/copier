from distutils.dir_util import copy_tree
import os
import shutil

dirs = ["D:/Minecraft Stuff/Tools/bridge. v2/projects/Security Gadgets/BP", "D:/Minecraft Stuff/Tools/bridge. v2/projects/Security Gadgets/RP"]
BP = "D:/Minecraft Stuff/Addons Development/security-gadgets/Security Gadgets BP"
RP = "D:/Minecraft Stuff/Addons Development/security-gadgets/Security Gadgets RP"

shutil.rmtree(BP)
shutil.rmtree(RP)

copy_tree(dirs[0], BP)
copy_tree(dirs[1], RP)