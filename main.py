import os
import  sys
# import modules

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
	pass

# Checks to run the code
if runcode == True:
	main()