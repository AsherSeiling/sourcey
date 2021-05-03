import os
import json
import sys
import math
import modules.loadJson as LJ
import modules.readSourceyignore as rsig
# Load Json Data
mainJsondata = LJ.loadJSON(".sourcey/config.json")
BranchJson = LJ.loadJSON(f".sourcey/branches/{mainJsondata['currentBranch']}/config.json")

def find_differences():
    ignore = rsig.readIgnore()
    referencelastcommit = os.listdir(f".sourcey/branches/{mainJsondata['currentBranch']}/commits/{BranchJson['commitsnum']}")
    refernceCurrentDataTemp = os.listdir()
    refernceCurrentData = []
    for items in refernceCurrentDataTemp:
        if items not in ignore:
            refernceCurrentData.append(items)
    print(refernceCurrentData)
    # Find the Changes
    change_log = {
        "changes" : [

        ],
        "creation" : [],
        "deletion" : []
    }
    changes_possible = []
    for i in refernceCurrentData:
        if i in referencelastcommit:
            changes_possible.append(i)
        elif i not in referencelastcommit:
            change_log["creation"].append(i)
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
        dispChangesBuffer += f"  File: {i['file']} | Changes percent: {i['changePercent']}%\n"
    dispChangesBuffer += "Creation:\n"
    for i in differencesDict["creation"]:
        dispChangesBuffer += f"  File: {i}\n"
    dispChangesBuffer += "Deleted:\n"
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
