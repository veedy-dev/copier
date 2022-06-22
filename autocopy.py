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


copyBP(input("Enter source BP folder: "),
       input("Enter destination BP folder: "))
copyRP(input("Enter source RP folder: "),
       input("Enter destination RP folder: "))
