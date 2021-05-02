import os
import json
import sys

def readIgnore():
    ignore = [".sourcey"]
    if ".sourceyignore" in os.listdir():
        ignoretemp = open(".sourceyignore", "r").readlines()
        for i in ignoretemp:
            ignore.append(i.split("\n")[0])
    return ignore
