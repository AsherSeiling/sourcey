import json
import os
import sys
def loadJSON(dir):
    jsonMain = open(dir, "r").read()
    jsonMain = json.loads(jsonMain)
    return jsonMain
