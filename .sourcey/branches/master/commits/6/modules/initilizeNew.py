import os
import json
import datetime
def initNew():
	os.system("mkdir .sourcey")
	os.chdir(".sourcey")
	initilizeInstructions = [
		"mkdir branches",
		"mkdir branches/master",
		"touch config.json",
		"touch branches/master/config.json",
		"mkdir branches/master/commits",
		"mkdir branches/master/commits/1"
	]
	for i in initilizeInstructions:
		os.system(i)
	json_template_main_config = {
		"creation_date" : f"{datetime.datetime.now()}",
		"branches" : ["master"],
		"currentBranch" : "master"
	}
	jsondata = json.dumps(json_template_main_config, indent=4)
	jsonFile = open("config.json", "w+")
	jsonFile.write(jsondata)
	jsonFile.close()
	jsonmasterconfig = {
		"commitsnum" : 1,
		"commits" : [
			{
				"id" : "1",
				"name" : "Inital Commit",
				"commitDate" : f"{datetime.datetime.now()}"
			}
		],
		"fistCommit" : f"{datetime.datetime.now()}",
		"mostRecentCommit" : f"{datetime.datetime.now()}"
	}
	jsondata = json.dumps(jsonmasterconfig, indent=4)
	jsonFile = open("branches/master/config.json", "w+")
	jsonFile.write(jsondata)
	jsonFile.close()
