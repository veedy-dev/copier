""" python script to copy multiple folders to multiple destinations
author: @veedy-dev
date: 22-06-2022
version: 1.0
license: MIT
usage: python autocopy.py """

import os
import shutil
from distutils.dir_util import copy_tree


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

    with open("paths.json", "w") as f:
        f.write("{\"srcBP\":\"" + srcBP + "\",\"dstBP\":\"" + dstBP +
                "\",\"srcRP\":\"" + srcRP + "\",\"dstRP\":\"" + dstRP + "\"}")
        f.close()
    print("Paths saved successfully")


if os.path.exists("paths.json"):
    with open("paths.json", "r") as f:
        data = f.read()
        
        srcBP = data[data.find("srcBP") + 8:data.find("dstBP") - 1]
        dstBP = data[data.find("dstBP") + 8:data.find("srcRP") - 1]
        srcRP = data[data.find("srcRP") + 8:data.find("dstRP") - 1]
        dstRP = data[data.find("dstRP") + 8:data.find("}") - 1]

        # remove comma from the paths
        srcBP = srcBP.replace(",", "")
        dstBP = dstBP.replace(",", "")
        srcRP = srcRP.replace(",", "")
        dstRP = dstRP.replace(",", "")
        
        print(srcBP, dstBP, srcRP, dstRP)
else:
    savePaths()
