import json
import requests
import ast

gf = open("../originals/graduates.json", 'r')
data = json.loads(gf.read())

new_set = []
original_count = len(data)
print("Processing %s records..." % original_count)

for item in data:
	try:
		new_item = {}
		# Begin parsing the shitty encoded address
		address_set = ast.literal_eval(item['location_1']['human_address'])
		# Create a new location set
		new_item['location'] = {
			'city': address_set['city'],
			'coordinates': {
				'latitude': item['location_1']['latitude'],
				'longitude': item['location_1']['longitude']
			}
		}
		# Delete useless keys then merge
		del item['location_1']
		del item['calendario']
		# Merge keys 
		# TODO: Refactor
		new_item['igs'] = item['igs']
		new_item['gpa'] = item['gpa']
		new_item['program'] = item['program']
		new_item['campus'] = item['campus']
		new_item['escuela'] = item['institucion_de_procedencia'][8:]
		# Push to list
		new_set.append(new_item)
		print("%s items processed" % len(new_set))
	except KeyError:
		print("Skipped an incomplete error...")
		continue

