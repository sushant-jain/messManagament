import urllib.request
import json

def auth(uid):
	string = "http://ediome.com:3001/rfid"
	string = string + "/add?uid=" + str(uid)
	content = urllib.request.urlopen(string).read()
	content = str(content,'utf-8')
	content = json.loads(content)
	# print(content["success"])
	if(content["success"]):
		status = 1
	else:
		status = 0
	return status

print(auth(101))