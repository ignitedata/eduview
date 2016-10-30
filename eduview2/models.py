from pymongo import MongoClient

client = MongoClient()
db = client.datasets

schools = db.schools
graduates = db.graduates

def get_by_id(sid):
	return schools.find_one({'id': sid})