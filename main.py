import os
import  sys
# import modules
import modules.initilizeNew as initn
# Command help
commands = [
	"sourcey -h",
	"sourcey init"
]
# Get args
runcode = True
try:
	if sys.argv[1].lower() == "-h":
		runcode = False
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
# Checks to run the code
if runcode == True:
	main()