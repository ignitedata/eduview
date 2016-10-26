import requests
import time
import json
from sodapy import Socrata

sid = input("Set ID: ")
write_to_file = input("Should I make a new file? [Y/n] ")

count = 0
fetched = requests.get('https://data.pr.gov/resource/%s.json?$offset=%s&$limit=1000' % (sid, count)).json()

while True:
	count = count + 1000
	print("Iterating cycle #%s" % count)
	sets = requests.get('https://data.pr.gov/resource/%s.json?$offset=%s&$limit=1000' % (sid, count)).json()
	if sets == []:
		break
	else:
		fetched = fetched + sets
		print("So far dataset is %s records..." % len(fetched))

json2 = json.dumps(fetched, indent=4)
print("Received %s records." % len(fetched))

if write_to_file == 'y':
	filename = input("Output filename: ")
	f = open(filename, 'w')
	f.write(json2)
	print("Done.")