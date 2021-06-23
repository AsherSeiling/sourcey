import os
import json
import sys
import datetime
import modules.loadJson as LJ
import modules.readSourceyignore as scig
mainConf = LJ.loadJSON(".sourcey/config.json")
branchConf = LJ.loadJSON(f".sourcey/branches/{mainConf['currentBranch']}/config.json")
ignore = scig.readIgnore()
def commitChanges(argument1):
    files = os.listdir()
    commitFiles = []
    for items in files:
        if items not in ignore:
            commitFiles.append(items)
    # Copy over the file
    os.system(f"mkdir .sourcey/branches/{mainConf['currentBranch']}/commits/{branchConf['commitsnum'] + 1}")
    for i in commitFiles:
        os.system(f"cp -a {i} .sourcey/branches/{mainConf['currentBranch']}/commits/{branchConf['commitsnum'] + 1}")
    branchConf["commitsnum"] += 1
    branchConf["commits"].append({"id" : f"{branchConf['commitsnum']}", "name" : f"{argument1}", "commitDate" : str(datetime.datetime.now())})
    branchConf["mostRecentCommit"] = str(datetime.datetime.now())
    branchConf1 = json.dumps(branchConf, indent=4)
    branchConf2 = open(f".sourcey/branches/{mainConf['currentBranch']}/config.json", "w")
    branchConf2.write(branchConf1)
    branchConf2.close()
    os.chdir(f".sourcey/branches/{mainConf['currentBranch']}/commits/")
    os.system(f"zip -r {branchConf['commitsnum'] - 1}.zip {branchConf['commitsnum'] - 1}")
    os.system(f"rm -rf {branchConf['commitsnum'] - 1}")
