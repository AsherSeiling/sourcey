import os
import  sys
# import modules
try:
	import modules.initilizeNew as initn
	import modules.sourceyTrack as st
	import modules.commit as cmt
	import modules.logCommits as lgcmts
except:
	print("Sourcey configed")
# Command help
commands = [
	"sourcey -h",
	"sourcey init",
	"sourcey track",
	"sourcey commit <commit name>",
	"sourcey log"
]
# Get args
runcode = True
try:
	if sys.argv[1].lower() == "-h":
		runcode = False
		for i in commands:
			print(i)
	if len(sys.argv) == 1:
		runcode = False
except:
	print("Error: no command inputed try \"sourcey -h\" to see the list of commands")
	runcode = False

# Main Function
def main():
	command = sys.argv
	if command[1].lower() == "init":
		if ".sourcey" not in os.listdir():
			initn.initNew()
		else:
			print("Repo Already initilized in this directory")
	if command[1].lower() == "track":
		if ".sourcey" in os.listdir():
			st.sourceyTrack()
		else:
			print("Repo not initilized")
	if command[1].lower() == "commit":
		if ".sourcey" in os.listdir():
			cmt.commitChanges(command[2])
		else:
			print("Repo not ininitialized")
	if command[1].lower() == "log":
		if ".sourcey" in os.listdir():
			print(lgcmts.logCommits())
		else:
			print("Repo not initilized")

# Checks to run the code
try:
    if runcode == True:
	    main()
except:
    print("Error: Command not found")
