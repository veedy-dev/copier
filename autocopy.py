""" python script to copy MC BP & RP folders to multiple destinations
author: @veedy-dev
date: 22-06-2022
version: 1.0
license: MIT
usage: python autocopy.py """

import os
import shutil
from distutils.dir_util import copy_tree
import json


def copyBP(srcBP, dstBP):
    if os.path.exists(srcBP) and os.path.exists(dstBP):
        if os.listdir(dstBP) == []:
            copy_tree(srcBP, dstBP)
        else:
            shutil.rmtree(dstBP)
            copy_tree(srcBP, dstBP)
        print("BP files copied successfully")
    else:
        print("BP Source or destination folder does not exist")


def copyRP(srcRP, dstRP):
    if os.path.exists(srcRP) and os.path.exists(dstRP):
        if os.listdir(dstRP) == []:
            copy_tree(srcRP, dstRP)
        else:
            shutil.rmtree(dstRP)
            copy_tree(srcRP, dstRP)
        print("RP files copied successfully")
    else:
        print("RP Source or destination folder does not exist")


def savePaths():
    srcBP = input("Enter source BP folder: ")
    dstBP = input("Enter destination BP folder: ")
    srcRP = input("Enter source RP folder: ")
    dstRP = input("Enter destination RP folder: ")
    # replace all backslashes with forward slashes
    srcBP = srcBP.replace("\\", "/")
    dstBP = dstBP.replace("\\", "/")
    srcRP = srcRP.replace("\\", "/")
    dstRP = dstRP.replace("\\", "/")

    # dump the paths to a json file
    with open("paths.json", "w") as f:
        json.dump({"srcBP": srcBP, "dstBP": dstBP, "srcRP": srcRP, "dstRP": dstRP}, f, indent=4)
    print("Paths saved successfully")

if os.path.exists("paths.json"):
    # load paths.json and assign key to variables
    with open("paths.json", "r") as f:
        data = json.load(f)
        copyBP(data["srcBP"], data["dstBP"])
        copyRP(data["srcRP"], data["dstRP"])
else:
    savePaths()