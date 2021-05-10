import os
import sys

# Import the custom modules
import modules.loadJson as LJ

# Read json
mainJsondata = LJ.loadJSON(".sourcey/config.json")
BranchJson = LJ.loadJSON(f".sourcey/branches/{mainJsondata['currentBranch']}/config.json")
rows, columns = os.popen('stty size', 'r').read().split()
columnBar = ""
for i in range(int(columns)):
	columnBar += "-"
# Load commits
def commitLoad():
    commits = []
    CJS = BranchJson
    commits.append(columnBar)
    commits.append(f"Commits: {CJS['commitsnum']}")
    commits.append(columnBar)
    for i in CJS['commits']:
        buffer = ""
        buffer += f"Commit ID: {i['id']}\n"
        buffer += f"Commit Name: {i['name']}\n"
        buffer += f"Commit Date: {i['commitDate']}"
        commits.append(buffer)
        commits.append(columnBar)
    return commits
# Main function
def logCommits():
    commitsReturn = commitLoad()
    buffer = ""
    for i in commitsReturn:
        buffer += f"{i}\n"
    return buffer
