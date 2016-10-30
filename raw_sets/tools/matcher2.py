from sys import argv
import json

graduates = open("../graduates.json", 'r')
graduates = json.loads(graduates.read())

schools = open("../schools.json", 'r')
schools = json.loads(schools.read())

count = 0
original_count = len(graduates)

for graduate in graduates:
	for school in schools:
		school_item = {}
		if school['name'] in graduate['school'] and school['location']['municipality'] == graduate['location']['city']:
			count = count + 1
			school_item['accuracy'] = 90
			school_item['id'] = school['id']
			school_item['name'] = school['name']
			break
		elif school['name'] == graduate['school'] and school['location']['municipality'] == graduate['location']['city']:
			count = count + 1
			school_item['accuracy'] = 60
			school_item['id'] = school['id']
			school_item['name'] = school['name']
			break
		else:
			school_item['accuracy'] = 30
			gradate_school_name = graduate['school'].split()
			original_school_name = school['name'].split()
			words_g = [word for word in gradate_school_name if len(word) >= 3]
			words_s = [word for word in original_school_name if len(word) >= 3]
			matches = set(words_g).intersection(words_s)
			if len(matches) >= 2 and school['location']['municipality'] == graduate['location']['city']:
				print("Found match, flag for manual review")
				print("%s vs. %s" % (school['name'], graduate['school']))
				print("%s vs. %s" % (school['location']['municipality'], graduate['location']['city']))
				school_item['id'] = school['id']
				school_item['name'] = school['name']
				count = count + 1
				break
			else:
				school_item = None

	graduate['school_data'] = school_item

print("%d records were matched by ftxrc/PulseData Matcher2(c)." % count)
percent = (count / original_count) * 100
print("%d percent of records could be matched using the algorithm." % percent)
echo = input("Print data? [Y/n] ")
print(graduates[1])
if len(argv) == 2:
	print("Writing to file")
	output_file = open(argv[1], 'w')
	output_file.write(json.dumps(graduates, indent=4))
	print("Done")