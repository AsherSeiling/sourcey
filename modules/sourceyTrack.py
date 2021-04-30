import os
import json
import sys
import math

# Functions for the code
# Loads Json data
def loadJSON(dir):
    jsonMain = open(dir, "r").read()
    jsonMain = json.loads(jsonMain)
    return jsonMain
# Load Json Data
mainJsondata = loadJSON(".sourcey/config.json")
BranchJson = loadJSON(f".sourcey/branches/{mainJsondata['currentBranch']}/config.json")

def find_differences():
    ignore = [".sourceyignore"]
    referencelastcommit = os.listdir(f".sourcey/branches/{mainJsondata['currentBranch']}/commits/{BranchJson['commitsnum']}")
    refernceCurrentDataTemp = os.listdir()
    refernceCurrentData = []
    if ".sourceyignore" in refernceCurrentData:
        ignoretemp = open(".sourceyignore", "r").readlines()
        for i in ignoretemp:
            ignore.append(i.split("\n")[0])
    for items in refernceCurrentData:
        if items not in refernceCurrentDataTemp:
            refernceCurrentData.append(items)
    # Find the Changes
    change_log = {
        "changes" : [

        ],
        "creation" : [],
        "deletion" : []
    }
    changes_possible = []
    for i in range(len(refernceCurrentData)):
        if refernceCurrentData[i] in referencelastcommit:
            changes_possible.append(refernceCurrentData[i])
        elif refernceCurrentData[i] not in referencelastcommit:
            change_log["creation"].append(refernceCurrentData[i])
    for i in referencelastcommit:
        if i not in refernceCurrentData:
            change_log["deletion"].append(i)
    # Find the changes_possible
    for i in changes_possible:
        changes1 = open(i, "r").readlines()
        changes2 = open(f".sourcey/branches/{mainJsondata['currentBranch']}/commits/{BranchJson['commitsnum']}/{i}")
        changes_percent = 0
        if changes1 != changes2:
            lenchanges1 = len(changes1)
            lenchanges2 = len(changes2)
            changes_percent = ((lenchanges2 / lenchanges1) - math.floor(lenchanges2 / lenchanges1)) * 100
            change_log["changes"].append({"file" : f"{i}", "changePercent" : f"{changes_percent}"})
    return change_log

# Main Disp function
def sourceyTrack():
    print("Tracking...")
    differencesDict = find_differences()
    dispChangesBuffer = ""
    for i in differencesDict["changes"]:
        dispChangesBuffer += f"  File: {i["file"]} | Changes percent: {i["changePercent"]}%\n"
    dispChangesBuffer += "Creation:"
    for i in differencesDict["creation"]:
        dispChangesBuffer += f"  File: {i}\n"
    dispChangesBuffer += "Deleted:"
    for i in differencesDict["deletion"]:
        dispChangesBuffer += f"  File: {i}\n"
    disp_statments = [
        f"Creation Date: {mainJsondata['creation_date']}",
        f"Branches: {len(mainJsondata['branches'])} | {mainJsondata['branches']} | Current Branch: {mainJsondata['currentBranch']}",
        f"Commits: {BranchJson['commitsnum']} | Most Recent: \"{BranchJson['commits'][len(BranchJson['commits']) - 1]['name']}\"",
        f"Changes:",
        f"{dispChangesBuffer}"
    ]
    print(*disp_statments, sep="\n")

sourceyTrack()
